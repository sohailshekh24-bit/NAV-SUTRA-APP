import streamlit as st
import PyPDF2
import google.generativeai as genai

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Sheikh Nav-Sutra AI Pro", page_icon="🎬")

# Gemini Brain Link
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Using the stable model name
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ API Key Error! Secrets check karein.")

# --- 2. THE NAV-SUTRA ENGINE ---
def analyze_with_gemini(text):
    prompt = f"""
    You are Sohail Sheikh's expert script consultant. 
    Analyze this script using the 'Sheikh Nav-Sutra' (9-Sutra) method.
    Check structure from Shunya to Poornata.
    Give specific advice in Hindi/English mixed.
    Script Content: {text[:15000]}
    """
    response = model.generate_content(prompt)
    return response.text

# --- 3. INTERFACE DESIGN ---
st.title("🎬 Sheikh Nav-Sutra AI: PRO")
st.markdown("The Karma-GPS Engine for Professional Writers")

uploaded_file = st.file_uploader("📂 PDF Script Upload Karein", type=['pdf'])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    content = "".join([p.extract_text() for p in reader.pages])
    st.success(f"✅ {uploaded_file.name} Scanned!")

    if st.button("🧠 Deep Scan (Gemini Brain)"):
        with st.spinner('Gemini is reading your script...'):
            try:
                report = analyze_with_gemini(content)
                st.markdown("---")
                st.markdown("### 📊 THE NAV-SUTRA ANALYSIS REPORT")
                st.write(report)
            except Exception as e:
                st.error(f"Analysis failed: {e}")
