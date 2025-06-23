
from flask import Flask, request, render_template
# import openai
import os
# from langchain.chat_models import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

import fitz  # PyMuPDF for PDFs
from docx import Document  # For .docx files

# OpenAI API Key from env variable
# openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_file = request.files['resume']
        job_description = request.form['job_description']

        # Extract text based on file type
        if resume_file.filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        elif resume_file.filename.endswith(".docx"):
            resume_text = extract_text_from_docx(resume_file)
        else:
            resume_text = resume_file.read().decode('utf-8', errors='ignore')

        feedback, compatibility_score = process_resume(resume_text, job_description)
        return render_template('index.html', feedback=feedback, compatibility_score=compatibility_score)

    return render_template('index.html')


def extract_text_from_pdf(file_storage):
    doc = fitz.open(stream=file_storage.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_text_from_docx(file_storage):
    document = Document(file_storage)
    return "\n".join([para.text for para in document.paragraphs])


import ollama

def process_resume(resume_text, job_description):
    prompt = f"""
    You are an AI assistant that evaluates resumes against job descriptions.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide:
    1. Feedback on the resume's strengths and weaknesses for this job.
    2. A compatibility score out of 100.
    """

    response = ollama.chat(model='mistral', messages=[
        {"role": "user", "content": prompt}
    ])

    result = response['message']['content']

    # Try to extract feedback and score
    if "score" in result.lower():
        parts = result.split("2.")
        feedback = parts[0].strip()
        compatibility_score = parts[1].strip() if len(parts) > 1 else "N/A"
    else:
        feedback = result
        compatibility_score = "N/A"

    return feedback, compatibility_score



if __name__ == '__main__':
    app.run(debug=True)
