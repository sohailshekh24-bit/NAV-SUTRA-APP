
     import streamlit as st
import PyPDF2
import google.generativeai as genai

# --- CONFIG ---
st.set_page_config(page_title="Sheikh Nav-Sutra AI Pro", page_icon="🎬")

# Brain Connect (Secrets se key uthayega)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3-flash')
except Exception as e:
    st.error("⚠️ API Key Error! Settings -> Secrets mein quotes check karein.")

# --- THE NAV-SUTRA BRAIN ---
def analyze_with_gemini(text):
    prompt = f"""
    Analyze this script using Sohail Sheikh's 9-Sutra (Nav-Sutra) method. 
    Analyze the structure and flow based on Shunya to Poornata.
    Give specific advice as an expert script doctor.
    Script Content: {text[:15000]}
    """
    response = model.generate_content(prompt)
    return response.text

st.title("🎬 Sheikh Nav-Sutra AI: PRO")
st.markdown("The Karma-GPS Engine for Professional Writers")

uploaded_file = st.file_uploader("📂 PDF Script Upload Karein", type=['pdf'])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    content = "".join([p.extract_text() for p in reader.pages])
    st.success("✅ Script Scanned!")

    if st.button("🧠 Deep Scan (Gemini Brain)"):
        with st.spinner('Gemini is reading your script...'):
            report = analyze_with_gemini(content)
            st.markdown("### 📊 THE NAV-SUTRA REPORT")
            st.write(report)
