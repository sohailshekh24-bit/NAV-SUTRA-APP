import streamlit as st
import PyPDF2
import google.generativeai as genai

# --- 1. CONFIG ---
st.set_page_config(page_title="Sheikh Nav-Sutra AI Pro", page_icon="🎬")

# Brain Connect
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Sabse stable model try karte hain
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ Setup Error! Please check your API Key in Secrets.")

# --- 2. THE NAV-SUTRA BRAIN ---
def analyze_with_gemini(text):
    prompt = f"""
    You are Sohail Sheikh's expert script analyst. 
    Analyze this script using the 'Sheikh Nav-Sutra' (9-Sutra) method.
    Check structure from Shunya to Poornata.
    Provide specific advice in Hindi/English mixed.
    Script Content: {text[:15000]}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Model Error: {str(e)}. Please refresh or check API access."

# --- 3. UI DESIGN ---
st.title("🎬 Sheikh Nav-Sutra AI: PRO")
st.markdown("The Karma-GPS Engine for Professional Writers")

uploaded_file = st.file_uploader("📂 PDF Script Upload Karein", type=['pdf'])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    content = "".join([p.extract_text() for p in reader.pages])
    st.success(f"✅ {uploaded_file.name} Scanned!")

    if st.button("🧠 Deep Scan (Gemini Brain)"):
        with st.spinner('Gemini is reading your script...'):
            report = analyze_with_gemini(content)
            st.markdown("---")
            st.markdown("### 📊 THE NAV-SUTRA ANALYSIS REPORT")
            st.write(report)
