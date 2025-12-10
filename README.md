📘 Keyword Extraction System – Researcher’s Assistant

A Streamlit-based NLP application that extracts keywords, generates summaries, and visualizes word clouds from any text document.
Built using Python, Streamlit, Summa NLP, WordCloud, and Matplotlib.

🚀 Features
🔑 Keyword Extraction

Uses the TextRank algorithm (Summa library) to extract the most important words and keyphrases.

📄 Text Summarization

Generates an extractive summary by identifying the highest-ranked sentences.

☁️ Word Cloud Visualization

Creates a word cloud based on word frequency distribution.

📤 Input Options

Upload a .txt file

Or paste text manually into the interface

📥 Download Support

Download:

Extracted keywords

Generated summary

🗂️ Project Workflow

User uploads/pastes text

System preprocesses text

TextRank extracts keywords

Summary is generated

Word cloud is displayed

Results are available for download

🛠️ Technologies Used

Python

Streamlit (Frontend UI)

Summa NLP (TextRank algorithm)

WordCloud

Matplotlib

📦 Installation
1️⃣ Clone the repository
git clone <your-repo-link>
cd keyword-extraction-system

2️⃣ Install dependencies

(From requirements.txt)

pip install -r requirements.txt

▶️ Running the Application

Run the Streamlit app using:

streamlit run app.py


The application will open in your default browser:

http://localhost:8501

📁 Project Structure
├── app.py                # Main Streamlit application
├── requirements.txt      # Required packages
├── README.md             # Project documentation

🧠 How It Works (Core Logic)
extract_keywords(text)

Uses summa.keywords()

Returns ranked keywords

Handles short or empty text gracefully

generate_summary(text)

Uses summa.summarizer.summarize()

Extracts key sentences

Word Cloud

Created using WordCloud()

Rendered via Matplotlib in Streamlit

🎯 Use Cases

Journalists analyzing long investigation reports

Researchers summarizing literature papers

Business analysts extracting insights from corporate documents

Students summarizing study materials

🌱 Future Enhancements

PDF / DOCX upload support

Multi-language keyword extraction

BERT / Transformer-based summarization

Named Entity Recognition (NER)

Topic Modeling (LDA / BERTopic)

API deployment using FastAPI

🧑‍💻 Team Members

M. Kalyani

B. Jahnavi

B. Ishwarya

D. Turvi

S. L. S. Sanjana

📌 Conclusion

The Keyword Extraction System is a powerful, lightweight NLP tool that helps users quickly analyze large text documents. With automated keyword extraction, summarization, and visualization, the application enhances productivity and supports informed decision-making across multiple domains.