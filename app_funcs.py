import streamlit as st
from transformers import pipeline
import fitz
import docx
import re

# --------------------------------------------------
# Emotion detection (cached properly)
# --------------------------------------------------
@st.cache_data(show_spinner=False)
def emotion_generate(plain_text):
    """
    Returns: POSITIVE / NEGATIVE
    """
    emotion = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    result = emotion(plain_text)[0]["label"]
    return result.lower()  # normalize for UI consistency


# --------------------------------------------------
# TXT extraction
# --------------------------------------------------
@st.cache_data(show_spinner=False)
def extract_text_txt(uploaded_txt_file, downloaded_txt_file):
    with open(uploaded_txt_file, "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()

    words = re.findall("[a-zA-Z]+", data)

    with open(downloaded_txt_file, "w", encoding="utf-8") as out:
        out.write("\n".join(words))

    return " ".join(words)


# --------------------------------------------------
# PDF extraction
# --------------------------------------------------
@st.cache_data(show_spinner=False)
def extract_text_pdf(uploaded_pdf_file):
    text = ""
    with fitz.open(uploaded_pdf_file) as pdf:
        for page in pdf:
            text += page.get_text()
    return text


# --------------------------------------------------
# DOCX extraction
# --------------------------------------------------
@st.cache_data(show_spinner=False)
def extract_text_docx(uploaded_docx_file):
    document = docx.Document(uploaded_docx_file)
    full_text = [para.text for para in document.paragraphs]
    return " ".join(full_text)


# --------------------------------------------------
# Download success animation
# --------------------------------------------------
def download_success():
    """
    UI effect should NOT be cached
    """
    st.balloons()
