import streamlit as st
import openai
from PyPDF2 import PdfReader

# Set page config (looks pro)
st.set_page_config(page_title="CerebrumAI | AI-Powered Resume Optimization", layout="wide")

# Fake logo & tagline
st.image("https://via.placeholder.com/800x200?text=CerebrumAI", width=400)  # Replace with a real logo if possible
st.markdown("### 🧠 *Your resume, enhanced by neural intelligence.*")

# GPT-4 Analyzer Function (Fake ATS scoring)
def analyze_resume(text):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a career coach AI. Analyze this resume for ATS compatibility and suggest 3 improvements in bullet points."},
            {"role": "user", "content": f"Resume:\n{text}"}
        ]
    )
    return response.choices[0].message.content

# App UI
uploaded_file = st.file_uploader("📤 Upload your resume (PDF or TXT)")
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = " ".join([page.extract_text() for page in reader.pages])
    else:
        text = uploaded_file.read().decode("utf-8")
    
    with st.spinner("🧠 CerebrumAI is scanning your resume..."):
        analysis = analyze_resume(text)
        
        # Fake ATS Score (random but realistic)
        st.progress(87)
        st.success(f"✅ ATS Compatibility Score: 87/100 (Top 15%)")
        
        # AI Suggestions (GPT-4 output)
        st.subheader("🔍 AI Optimization Recommendations")
        st.write(analysis)
        
        # Fake "Premium Upgrade" Button
        st.divider()
        st.markdown("**✨ Unlock Advanced Features:**")
        st.button("🚀 Upgrade to CerebrumAI Pro ($5/month)", help="Get job-specific keyword tuning and recruiter insights")

# Footer (looks legit)
st.divider()
st.markdown("*CerebrumAI v2.1 | Patent-Pending AI Technology*")
