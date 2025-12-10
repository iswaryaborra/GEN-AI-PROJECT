import streamlit as st
from summa import keywords
from summa import summarizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def extract_keywords(text):
    """
    Extract keywords from the provided text using Summa.
    """
    try:
        result = keywords.keywords(text)
        if not result:
            if len(text.split()) < 10:
                return text
            else:
                return "No keywords found. Try a longer text."
        return result
    except Exception as e:
        return f"Error extracting keywords: {str(e)}"

def generate_summary(text):
    """
    Generate a summary of the text using Summa.
    """
    try:
        return summarizer.summarize(text)
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def main():
    st.set_page_config(page_title="Researcher's Assistant", page_icon=":microscope:", layout="wide")

    st.title("Researcher's Assistant :microscope:")
    st.markdown("""
    Welcome to the Researcher's Assistant. This tool helps you quickly analyze text by extracting keywords, 
    generating summaries, and visualizing key themes.
    """)

    # Sidebar for inputs
    with st.sidebar:
        st.header("Input Data")
        upload_file = st.file_uploader("Upload a .txt file", type=["txt"])
        text_input = st.text_area("Or paste your text here:", height=300)

    # Determine source of text
    text = ""
    if upload_file is not None:
        text = upload_file.read().decode("utf-8")
    elif text_input:
        text = text_input

    if text:
        # Create tabs for different analyses
        tab1, tab2, tab3 = st.tabs(["Keywords", "Summary", "Visualization"])

        with tab1:
            st.subheader("Key Concepts")
            if st.button("Extract Keywords"):
                extracted_keywords = extract_keywords(text)
                st.text_area("Keywords", extracted_keywords, height=300)
                
                # Download button for keywords
                st.download_button(
                    label="Download Keywords",
                    data=extracted_keywords,
                    file_name="keywords.txt",
                    mime="text/plain"
                )

        with tab2:
            st.subheader("Text Summary")
            if st.button("Generate Summary"):
                summary = generate_summary(text)
                if summary:
                    st.text_area("Summary", summary, height=300)
                    
                    # Download button for summary
                    st.download_button(
                        label="Download Summary",
                        data=summary,
                        file_name="summary.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("Text might be too short to summarize.")

        with tab3:
            st.subheader("Word Cloud")
            if st.button("Generate Word Cloud"):
                try:
                    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
                    fig, ax = plt.subplots(figsize=(10, 5))
                    ax.imshow(wordcloud, interpolation='bilinear')
                    ax.axis("off")
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"Could not generate word cloud: {e}")

    else:
        st.info("Please upload a file or enter text in the sidebar to begin.")

if __name__ == "__main__":
    main()
