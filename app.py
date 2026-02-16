import streamlit as st
import PyPDF2
import google.generativeai as genai

st.set_page_config(page_title="Sheikh Nav-Sutra AI", page_icon="🎬")

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Check Secrets!")

st.title("🎬 Sheikh Nav-Sutra AI")
file = st.file_uploader("Upload Script", type=['pdf'])

if file and st.button("Deep Scan"):
    with st.spinner('Reading...'):
        reader = PyPDF2.PdfReader(file)
        text = "".join([p.extract_text() for p in reader.pages])
        try:
            res = model.generate_content(f"Analyze this script using Nav-Sutra logic: {text[:10000]}")
            st.write(res.text)
        except Exception as e:
            st.error(f"Error: {e}")
