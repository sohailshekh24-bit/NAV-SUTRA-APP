import streamlit as st
import PyPDF2
import google.generativeai as genai

# --- 1. CONFIG ---
st.set_page_config(page_title="Sheikh Nav-Sutra AI Pro", page_icon="🎬")

# Brain Connect (Secrets se key uthayega)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # 2026 ka sabse naya model
    model = genai.GenerativeModel('gemini-3-flash')
except Exception as e:
    st.error("⚠️ API Key Error! Streamlit Secrets check karein.")

# --- 2. THE NAV-SUTRA BRAIN ---
def analyze_with_gemini(text):
    prompt = f"""
    Analyze this script using Sohail Sheikh's 9-Sutra (Nav-Sutra) method. 
    Focus on structure from Shunya to Poornata.
    Give specific advice as an expert script doctor in Hindi/English mixed.
    Script Content: {text[:15000]}
    """
    response = model.generate_content(prompt)
    return response.text

# --- 3. UI DESIGN ---
st.title("🎬 Sheikh Nav-Sutra AI: PRO")
st.markdown("The Karma-GPS Engine for Professional Writers")

uploaded_file = st.file_uploader("📂 PDF Script Upload Karein", type=['pdf'])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    content = "".join([p.extract_text() for p in reader.pages])
    st.success("✅ Script Scanned!")

    if st.button("🧠 Deep Scan (Gemini Brain)"):
        with st.spinner('Gemini is reading your script...'):
            try:
                report = analyze_with_gemini(content)
                st.markdown("### 📊 THE NAV-SUTRA REPORT")
                st.write(report)
            except Exception as e:
                st.error(f"Error during analysis: {e}")
