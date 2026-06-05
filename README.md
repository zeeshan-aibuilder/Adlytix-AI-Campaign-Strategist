# 🚀 Adlytix AI Campaign Strategist

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B.svg)
![Gemini AI](https://img.shields.io/badge/Google_Gemini-LLM-orange.svg)

## 📌 Project Overview
A Micro-SaaS web application designed to automate the creation of high-converting Meta Ads strategies. This tool leverages a decoupled Client-Server architecture, utilizing a **FastAPI** backend for robust AI integration and a **Streamlit** frontend for a premium, interactive user experience.

## 🏗️ System Architecture
1. **Frontend (Streamlit):** A clean, glassmorphism-inspired UI that takes user inputs (Product Name & Target Audience) and handles state management.
2. **Backend (FastAPI):** Acts as the central intelligence hub. It uses `pydantic` for strict data validation before constructing dynamic prompts.
3. **AI Engine:** Integrated with Google's latest `genai` SDK to generate tailored marketing angles, ad hooks, and targeting demographics.

## 🚀 How to Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/Adlytix-AI-Campaign-Strategist.git](https://github.com/YOUR_USERNAME/Adlytix-AI-Campaign-Strategist.git)
cd Adlytix-AI-Campaign-Strategist

2. Install dependencies:

pip install fastapi "uvicorn[standard]" streamlit google-genai pydantic requests
3. Add your API Key:
Open main.py and replace "ENTER_YOUR_API_KEY_HERE" with your Google Gemini API key.

4. Start the Backend (Terminal 1):

uvicorn main:app --reload
5. Start the Frontend (Terminal 2):

streamlit run frontend.py

👨‍💻 Developed By
M Zeeshan
AI Developer & Digital Marketing Strategist
