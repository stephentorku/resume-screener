# 🧠 AI-Powered Resume Screener

This is a lightweight AI-based resume screener and improvement assistant built with **Streamlit**. 
It uses **OpenAI's GPT models** to analyze a resume against a job description and offer improvement suggestions. Perfect for job seekers and recruiters alike.

---

## ✨ Features

- ✅ Automatically detects key skills and gaps between resume and job description using embeddings and cosine similarity
- ✅ Uses LLMs (OpenAI API) to generate improvement advice
- ✅ Clean UI with Streamlit
- ✅ Simple to run locally or host via Render/Docker

---

## 📂 Project Structure
├── app/
│ ├── init.py
│ ├── advice.py 
│ ├── main.py 
│ ├── matcher.py
│ └── parser.py 
├── models/ # (Optional) LLM models if using llama.cpp (now deprecated)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

