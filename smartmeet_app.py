import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit config
st.set_page_config(page_title="SmartMeet GPT", layout="wide")

#  Stylish SaaS-like UI
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}
.stApp {
    background: linear-gradient(to right, #f5f7fa, #c3cfe2);
}
h1 {
    font-size: 38px !important;
    font-weight: 600;
    color: #1a237e;
    padding-bottom: 1rem;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
    margin: auto;
    background-color: #ffffff;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.stTextArea textarea {
    background-color: #f7f9fc !important;
    border: 1px solid #ced4da !important;
    border-radius: 8px !important;
    padding: 14px !important;
    font-family: 'Courier New', monospace !important;
    font-size: 15px;
    color: #333;
}
.stTextArea textarea:focus {
    border: 2px solid #1a73e8 !important;
    box-shadow: 0 0 4px rgba(26, 115, 232, 0.2);
    outline: none;
}
.stButton>button {
    background-color: #1a73e8;
    color: white;
    font-weight: bold;
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    transition: 0.3s ease;
}
.stButton>button:hover {
    background-color: #1558b0;
    transform: translateY(-1px);
}
</style>
""", unsafe_allow_html=True)

#  Title
st.markdown("""
<h1 style='
    font-size: 38px;
    font-weight: bold;
    color: #ff6f00;
    text-shadow: 1px 1px 2px #ffa000;
'>
 SmartMeet GPT – AI Meeting Insight Generator
</h1>
""", unsafe_allow_html=True)


#  Input notes
user_input = st.text_area("📝 Paste Your Meeting Notes", height=200, placeholder="E.g. John confirmed the launch, Priya is updating the UI...")

#  Setup session state
if "summary" not in st.session_state:
    st.session_state["summary"] = ""
if "email_output" not in st.session_state:
    st.session_state["email_output"] = ""
if "action_output" not in st.session_state:
    st.session_state["action_output"] = ""

#  GPT call wrapper
def ask_openai(prompt, temperature=0.4, max_tokens=600):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f" Error: {e}"

#  Prompts
def analyze_notes(notes):
    return ask_openai(f"""
You are an expert meeting analyst assistant.
Analyze the following meeting notes or transcript. Then return:
1. Summary of discussion  
2. Key decisions made  
3. Action items (with deadlines and owners)  
4. Questions raised or unresolved  
5. Tone of meeting (optional)

Meeting Notes:
{notes}
""", max_tokens=700)

def generate_email(summary):
    return ask_openai(f"""
You are a professional assistant. Based on the following meeting summary, write a polite, concise email update to the stakeholders.

Meeting Summary:
{summary}
""", temperature=0.5, max_tokens=500)

def suggest_actions(summary):
    return ask_openai(f"""
You are a productivity coach. Based on the meeting summary, list 3–5 prioritized next steps I should take today. Be direct and action-oriented.

Meeting Summary:
{summary}
""", temperature=0.5, max_tokens=300)

#  Analyze button
if st.button("🔍 Analyze Notes"):
    if not user_input.strip():
        st.warning("Please paste some meeting notes to analyze.")
    else:
        with st.spinner("Generating summary..."):
            st.session_state["summary"] = analyze_notes(user_input)
            st.session_state["email_output"] = ""
            st.session_state["action_output"] = ""
            st.success(" Summary ready!")

#  Display summary and actions
if st.session_state["summary"]:
    st.text_area(" AI Structured Summary", value=st.session_state["summary"], height=300)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📧 Generate Email Update"):
            with st.spinner("Creating email..."):
                st.session_state["email_output"] = generate_email(st.session_state["summary"])

    with col2:
        if st.button("📋 Suggest Next Steps"):
            with st.spinner("Generating next steps..."):
                st.session_state["action_output"] = suggest_actions(st.session_state["summary"])

if st.session_state["email_output"]:
    st.text_area("📧 Email Update", value=st.session_state["email_output"], height=250)

if st.session_state["action_output"]:
    st.text_area("📋 Recommended Next Steps", value=st.session_state["action_output"], height=200)

#  Footer
st.markdown("<hr><div style='text-align:center; color:gray;'>Built by Prasanth A · Powered by Streamlit & OpenAI</div>", unsafe_allow_html=True)
