import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# -----------------------------
# Load Environment Variables
# -----------------------------
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

api_key = os.getenv("GROQ_API_KEY")

# -----------------------------
# Streamlit Config
# -----------------------------
st.set_page_config(
    page_title="AI Email Tone Corrector",
    page_icon="📧",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.block-container{
    max-width:900px;
    padding-top:2rem;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    font-size:18px;
}

/* Result Box */
.result-box{
    background-color:#f4f4f4;
    color:#000000;
    padding:20px;
    border-radius:12px;
    border:1px solid #d9d9d9;
    margin-top:15px;
    margin-bottom:15px;
}

/* Make markdown inside result visible */
.result-box h1,
.result-box h2,
.result-box h3,
.result-box h4,
.result-box p,
.result-box li,
.result-box strong{
    color:#000000 !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("📧 AI Email Tone Corrector")
st.write("Rewrite, analyze and improve professional emails using Groq AI.")

# -----------------------------
# Inputs
# -----------------------------
recipient = st.selectbox(
    "Recipient",
    [
        "HR",
        "Recruiter",
        "Team Lead",
        "Manager",
        "Client",
        "Professor",
        "Colleague"
    ]
)

purpose = st.selectbox(
    "Purpose",
    [
        "Job Application",
        "Leave Request",
        "Follow-up",
        "Status Update",
        "Meeting Request",
        "Apology",
        "General"
    ]
)

email = st.text_area(
    "Paste your email draft",
    height=250
)

# -----------------------------
# AI Function
# -----------------------------
def analyze_email(text):

    client = Groq(api_key=api_key)

    prompt = f"""
You are a professional business communication expert.

Recipient: {recipient}
Purpose: {purpose}

Analyze the email and provide the following sections.

# Rewritten Email

Rewrite the email professionally.

# Tone Analysis

Explain the tone.

# Missing Details

Mention missing dates, attachments, subject line, deadlines, contact details etc.

# Improvement Suggestions

Provide actionable suggestions.

# Overall Rating

Give a score out of 10.

Email:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


# -----------------------------
# Button
# -----------------------------
if st.button("✨ Analyze & Improve"):

    if not api_key:
        st.error("❌ GROQ_API_KEY not found!")

        st.write("Current Folder:", os.getcwd())
        st.write("Looking for:", dotenv_path)
        st.write("Does .env exist?", dotenv_path.exists())

        st.stop()

    if email.strip() == "":
        st.warning("Please paste an email first.")
        st.stop()

    try:

        with st.spinner("Analyzing your email..."):
            result = analyze_email(email)

        st.success("Analysis Complete!")

        st.subheader("📄 Result")

        # Display as markdown (correct colors)
        st.markdown(result)

        with st.expander("View Raw Response"):
            st.code(result)

    except Exception as e:
        st.error(f"Error: {e}")