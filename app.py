import streamlit as st
from deep_translator import GoogleTranslator

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

/* Main title */
.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 40px;
    font-size: 20px;
}

/* Glass container */
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 4px 30px rgba(0,0,0,0.3);
}

/* Text Areas */
textarea {
    background-color: #1e293b !important;
    color: white !important;
    border-radius: 12px !important;
    border: 1px solid #475569 !important;
}

/* Selectbox */
div[data-baseweb="select"] {
    background-color: #1e293b;
    border-radius: 10px;
}

/* Button */
.stButton > button {
    width: 100%;
    background: linear-gradient(to right, #3b82f6, #06b6d4);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<div class="title">🌍 AI Language Translator</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Translate text instantly into multiple languages</div>',
    unsafe_allow_html=True
)

# ================= LANGUAGES =================
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

# ================= MAIN UI =================
st.markdown('<div class="glass">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Input Text")

    text = st.text_area(
        "Enter Text",
        height=250,
        placeholder="Type something here..."
    )

    source = st.selectbox(
        "🌐 Source Language",
        list(languages.keys())
    )

with col2:
    st.subheader("🌍 Translation")

    target = st.selectbox(
        "🎯 Target Language",
        list(languages.keys())
    )

    translated_placeholder = st.empty()

# ================= TRANSLATE =================
if st.button("🚀 Translate Now"):

    if text.strip() == "":
        st.warning("Please enter text to translate.")
    else:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        translated_placeholder.success(translated)

st.markdown('</div>', unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("---")
st.caption("✨ Built using Python, Streamlit & GoogleTranslator")