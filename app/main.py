import streamlit as st
from parser import parse_resume
from matcher import match_resume_to_job
from advice import get_resume_improvement_advice

st.title("AI Resume Screener")

uploaded_resume = st.file_uploader("Upload a resume", type=["pdf", "docx", "txt"])
job_description = st.text_area("Paste the job description")

if uploaded_resume and job_description:
    # Read and cache resume bytes early to reuse
    resume_bytes = uploaded_resume.read()
    resume_text = parse_resume(resume_bytes, uploaded_resume.name)

    st.subheader("Extracted Resume Text:")
    st.write(resume_text[:1000])  # Show first 1000 characters

    similarity = match_resume_to_job(resume_text, job_description)

    st.subheader("Match Score:")
    st.metric(label="Resume vs Job Description", value=f"{similarity:.2f}")

    # Now safely place the button to generate tips
    if st.button("Get Resume Improvement Tips"):
        with st.spinner("Thinking..."):
            tips = get_resume_improvement_advice(resume_text, job_description)
        st.subheader("LLM-Suggested Resume Improvements")
        st.markdown(tips)
