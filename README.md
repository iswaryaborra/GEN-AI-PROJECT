📘 Keyword Extraction System

A Hybrid NLP Web Application for Journalists, Researchers & Analysts

📌 Overview

The Keyword Extraction System is a Streamlit-based web application designed to automatically extract keywords, generate summaries, and create word-cloud visualizations from any text document.
It uses a hybrid NLP approach combining rule-based processing and the TextRank algorithm (from the Summa library).

This tool helps users analyze large documents quickly—ideal for journalists, research scholars, corporate analysts, and students.

The complete functionality and workflow align with the detailed project description and diagrams in the PDF report (pages 1–4) 

Group13

.

✨ Features

✔ Keyword Extraction using TextRank (Summa NLP)
✔ Text Summarization (extractive)
✔ Word Cloud Visualization
✔ Upload .txt files or paste text directly
✔ Downloadable results (keywords & summary)
✔ Clean, interactive UI built with Streamlit

Screenshots in the report (pages 11–12) show how the UI appears in action 

Group13

.

🛠️ Tech Stack

Python 3.x

Streamlit (Frontend UI)

Summa NLP (Keyword extraction & summarization)

WordCloud + Matplotlib (Visualization)

These match the technologies listed in your PPT (Technologies Used section) 

GENAIPPT_Group13

.

📦 Installation
1️⃣ Clone the repository
git clone <your-repository-url>
cd <project-folder>

2️⃣ Install dependencies

Dependencies are taken directly from your requirements.txt file 

requirements

:

pip install streamlit
pip install summa
pip install wordcloud
pip install matplotlib


OR simply:

pip install -r requirements.txt

▶️ Running the App

Execute the Streamlit app:

streamlit run app.py


The app will open in your browser at:

http://localhost:8501/

🧠 How It Works (Workflow)

Based on the workflow in the PPT and report (pages 3–5) :

User uploads text file or pastes text

Preprocessing (cleaning, formatting)

Keyword extraction using TextRank

Summary generation

Word cloud creation

Results displayed with download buttons

The diagram on page 3 visually explains this pipeline.

📁 Project Structure
📂 Keyword-Extraction-System
│── app.py               # Main Streamlit application :contentReference[oaicite:9]{index=9}
│── requirements.txt     # Dependencies :contentReference[oaicite:10]{index=10}
│── README.md            # Project documentation
│── Purpose.txt          # Purpose + Q&A notes :contentReference[oaicite:11]{index=11}
│── /assets              # (Optional) screenshots, diagrams

📜 Code Summary

Your application contains three major functions (from app.py 

app

):

🔹 extract_keywords(text)

Uses TextRank (Summa)

Handles short text gracefully

Returns ranked keyword list

🔹 generate_summary(text)

Creates extractive summaries

Error-handled for short inputs

🔹 Word Cloud Builder

Uses WordCloud + Matplotlib

Generates high-frequency word visualization

📚 Use Cases

From your project report (pages 2–3) 

Group13

:

1. Investigative Journalism

Process long confidential reports and instantly extract important concepts.

2. Research Literature Review

Summaries & keywords help scholars understand papers faster.

3. Corporate Report Analysis

Analysts quickly extract insights from business documents.

🔮 Future Enhancements

Taken from PPT & report future scope sections (pages 13–14) :

PDF & DOCX upload support

Multi-language keyword extraction

Integration with BERT / Transformer models

Named Entity Recognition (NER)

Topic Modeling (LDA, BERTopic)

API version (FastAPI)

👥 Team

As listed in the PPT (cover slide) 

GENAIPPT_Group13

:

M. Kalyani – AP23110010343

B. Jahnavi – AP23110010342

B. Ishwarya – AP23110010646

D. Turvi – AP23110010391

S. L. S. Sanjana – AP23110010295
