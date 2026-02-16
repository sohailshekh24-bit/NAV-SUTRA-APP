import streamlit as st
import PyPDF2
import google.generativeai as genai

# --- 1. SETTINGS ---
st.set_page_config(page_title="Sheikh Nav-Sutra AI", page_icon="🎬")

# Brain Connect
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # 2026 ka sabse stable engine
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("⚠️ Secrets check karein!")

# --- 2. ENGINE ---
def analyze_script(text):
    prompt = f"Analyze this script using Sohail Sheikh's 9-Sutra logic (Nav-Sutra). Focus on Shunya, Beej, and Garbh. Script: {text[:15000]}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"System Error: {str(e)}"

# --- 3. UI ---
st.title("🎬 Sheikh Nav-Sutra AI: PRO")
uploaded_file = st.file_uploader("📂 PDF Script Upload Karein", type=['pdf'])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    content = "".join([p.extract_text() for p in reader.pages])
    st.success("✅ Script Scanned!")
    
    if st.button("🧠 Deep Scan (Gemini Brain)"):
        with st.spinner('Gemini is reading...'):
            report = analyze_script(content)
            st.markdown("### 📊 THE NAV-SUTRA REPORT")
            st.write(report)
