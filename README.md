# 🍽️ AI Restaurant Name & Menu Generator  
**LangChain (LCEL) × Google Gemini 2.5 Flash**

An AI-powered Python application that generates a **fancy restaurant name** and a **custom menu** based on a given cuisine using **LangChain Expression Language (LCEL)** and **Google Gemini**.

This project demonstrates real-world **Generative AI development**, correct **prompt engineering**, and **secure API key management**.

---

## ✨ Features

- 🧠 Generates a unique restaurant name for any cuisine  
- 📋 Produces five menu items for the generated restaurant  
- ⚡ Uses Google Gemini 2.5 Flash (fast & efficient)  
- 🔗 Built with LangChain Expression Language (LCEL)  
- 🔐 Secure environment variable handling  
- 🧩 Clean and modular Python code  

---

## 🛠️ Tech Stack

- Python 3.10+
- LangChain
- Google Gemini (`gemini-2.5-flash`)
- python-dotenv

---

## 📁 Project Structure

LangChain_P1/
│
├── app.py
├── langchain_helper.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example


---

## 🔑 Environment Setup

### 1️⃣ Create a virtual environment

Using Conda:
```bash
conda create -n lenv python=3.10 -y
conda activate lenv

Or using venv:
python -m venv venv
venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Configure API key
Create a .env file in the project root:

GOOGLE_API_KEY=your_google_gemini_api_key_here

📜 License:

Educational / Learning purpose only

⭐ If you find this project useful, consider starring the repository!!