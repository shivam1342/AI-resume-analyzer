# 🧠 AI Resume & Job Match Analyzer

A simple web app that evaluates a candidate's resume against a job description and provides:
- ✅ Tailored feedback
- 📊 A compatibility score (out of 100)

Powered by open-source LLMs via [Ollama](https://ollama.com/) running **Mistral** locally.  
No internet or OpenAI API required.

---

## ⚙️ Features

- 🔍 Analyze `.pdf`, `.docx`, or `.txt` resumes
- 🤖 Uses local LLM (`mistral`) via Ollama
- 💡 Flask web interface with upload + prompt
- 📄 Resume feedback + compatibility scoring

---

## 🛠️ Tech Stack

- Python 3.11+
- Flask (for web app)
- Ollama (for LLMs)
- Mistral (local language model)
- PyMuPDF (`fitz`) for `.pdf` reading
- `python-docx` for `.docx` reading

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-job-analyzer.git
cd ai-resume-job-analyzer
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3. Install Ollama (if not already)
Download from: https://ollama.com/download
Then run:

bash
Copy
Edit
ollama run mistral
This starts the LLM server locally.

4. Start the Flask app
Open a new terminal:

bash
Copy
Edit
venv\Scripts\activate
python app.py
Visit: http://127.0.0.1:5000

📦 Requirements
requirements.txt:

txt
Copy
Edit
Flask
python-docx
PyMuPDF
ollama
Install with:

bash
Copy
Edit
pip install -r requirements.txt
📸 Screenshot

![Screenshot 2025-06-23 173008](https://github.com/user-attachments/assets/102fd8e2-8425-4ce8-ac5f-853003cb28c0)


# 🧠 AI Resume & Job Match Analyzer

A simple web app that evaluates a candidate's resume against a job description and provides:
- ✅ Tailored feedback
- 📊 A compatibility score (out of 100)

Powered by open-source LLMs via [Ollama](https://ollama.com/) running **Mistral** locally.  
No internet or OpenAI API required.

---

## ⚙️ Features

- 🔍 Analyze `.pdf`, `.docx`, or `.txt` resumes
- 🤖 Uses local LLM (`mistral`) via Ollama
- 💡 Flask web interface with upload + prompt
- 📄 Resume feedback + compatibility scoring

---

## 🛠️ Tech Stack

- Python 3.11+
- Flask (for web app)
- Ollama (for LLMs)
- Mistral (local language model)
- PyMuPDF (`fitz`) for `.pdf` reading
- `python-docx` for `.docx` reading

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-job-analyzer.git
cd ai-resume-job-analyzer
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
3. Install Ollama (if not already)
Download from: https://ollama.com/download
Then run:

bash
Copy
Edit
ollama run mistral
This starts the LLM server locally.

4. Start the Flask app
Open a new terminal:

bash
Copy
Edit
venv\Scripts\activate
python app.py
Visit: http://127.0.0.1:5000

📦 Requirements
requirements.txt:

txt
Copy
Edit
Flask
python-docx
PyMuPDF
ollama
Install with:

bash
Copy
Edit
pip install -r requirements.txt
📸 Screenshot

(Add screenshot of the app running in browser)

🧠 Example Prompt Sent to LLM
text
Copy
Edit
You are an AI assistant that evaluates resumes against job descriptions.

Resume:
[Extracted Resume Text]

Job Description:
[User Provided Job JD]

Provide:
1. Feedback on the resume's strengths and weaknesses for this job.
2. A compatibility score out of 100.

