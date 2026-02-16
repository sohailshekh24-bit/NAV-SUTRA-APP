import streamlit as st
import PyPDF2
import google.generativeai as genai

# --- 1. CONFIG ---
st.set_page_config(page_title="Sheikh Nav-Sutra AI Pro", page_icon="🎬")

# Brain Connect
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ API Key Error! Secrets check karein.")

# --- 2. THE PROMPT ---
def analyze_with_gemini(script_content):
    prompt = f"""
    You are an expert script analyst working for filmmaker Sohail Sheikh. 
    Analyze the following script using his 'Sheikh Nav-Sutra' method (9 Sutras).
    
    Script: {script_content[:15000]} # Reading first 15k characters
    
    Please provide:
    1. Pacing analysis (Slow/Fast).
    2. Check 'Garbh' (Midpoint) impact.
    3. Check if 'Poornata' (Loop) closes properly.
    4. Sheikh Karma-GPS Advice (in Hindi/English mixed).
    """
    response = model.generate_content(prompt)
    return response.text

# --- 3. UI ---
st.title("🎬 Sheikh Nav-Sutra AI: PRO")
st.image("https://cdn-icons-png.flaticon.com/512/2965/2965302.png", width=80)

uploaded_file = st.file_uploader("📂 PDF Script Upload Karein", type=['pdf'])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = "".join([p.extract_text() for p in reader.pages])
    st.success("✅ PDF Scanned!")

    if st.button("🧠 Deep Scan (Gemini Brain)"):
        with st.spinner('Gemini is thinking...'):
            report = analyze_with_gemini(text)
            st.markdown("### 📊 THE NAV-SUTRA REPORT")
            st.write(report)
