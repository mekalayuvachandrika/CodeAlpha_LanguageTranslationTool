import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍"
)

st.title("🌍 AI Language Translation Tool")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es"
}

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):

    translated = GoogleTranslator(
        source=languages[source],
        target=languages[target]
    ).translate(text)

    st.success(translated)