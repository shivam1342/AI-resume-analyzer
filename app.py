from flask import Flask, request, render_template
import os
import fitz  # PyMuPDF for PDFs
from docx import Document  # For .docx files
import ollama
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_description = request.form['job_description']

        if resume_file.filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        elif resume_file.filename.endswith(".docx"):
            resume_text = extract_text_from_docx(resume_file)
        elif resume_file.filename.endswith(".txt"):
            resume_text = resume_file.read().decode('utf-8', errors='ignore')
        else:
            resume_text = "Unsupported file format."

        feedback, compatibility_score = process_resume(resume_text, job_description)
        return render_template('index.html', feedback=feedback, compatibility_score=compatibility_score)

    return render_template('index.html')


def extract_text_from_pdf(file_storage):
    doc = fitz.open(stream=file_storage.read(), filetype="pdf")
    return "".join(page.get_text() for page in doc)


def extract_text_from_docx(file_storage):
    document = Document(file_storage)
    return "\n".join(para.text for para in document.paragraphs)


def process_resume(resume_text, job_description):
    prompt = f"""
You are an AI assistant that evaluates resumes against job descriptions.

Resume:
{resume_text}

Job Description:
{job_description}

Respond strictly in the format below.
Use bullet points only (with - or •) and keep each section cleanly separated.

---

1. Strengths:

- (list each point clearly on a new line)

---

2. Weaknesses:

- (list each point clearly on a new line)

---

3. Compatibility Score (out of 100): <numeric score only>

DO NOT include summaries, explanations, or additional paragraphs outside this format.
DO NOT merge content into one paragraph.
"""


    try:
        response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
        result = response['message']['content']
    except Exception as e:
        return "LLM processing failed. Make sure Ollama & Mistral are running.", "N/A"

    # Extract the compatibility score using regex
    score_match = re.search(r'(score|compatibility)[^\d]{0,10}(\d{1,3})', result, re.IGNORECASE)
    compatibility_score = score_match.group(2) if score_match else "N/A"

    formatted = format_feedback(result)
    return formatted, compatibility_score



def format_feedback(text):
    import re

    # Extract strengths
    strengths_match = re.search(r"(?i)1\.\s*strengths?:?\s*(.*?)(?:2\.|weaknesses:)", text, re.DOTALL)
    strengths = strengths_match.group(1).strip() if strengths_match else ""

    # Extract weaknesses
    weaknesses_match = re.search(r"(?i)2\.\s*weaknesses?:?\s*(.*?)(?:3\.|compatibility)", text, re.DOTALL)
    weaknesses = weaknesses_match.group(1).strip() if weaknesses_match else ""

    # Force bullet formatting
    strength_lines = re.split(r"-\s*|\n", strengths)
    weakness_lines = re.split(r"-\s*|\n", weaknesses)

    strength_lines = [f"- {line.strip()}" for line in strength_lines if line.strip()]
    weakness_lines = [f"- {line.strip()}" for line in weakness_lines if line.strip()]

    result = ""
    if strength_lines:
        result += "🔹 **Strengths:**\n" + "\n".join(strength_lines) + "\n\n"
    if weakness_lines:
        result += "🔸 **Weaknesses:**\n" + "\n".join(weakness_lines)

    return result.strip()





if __name__ == '__main__':
    app.run(debug=True)
