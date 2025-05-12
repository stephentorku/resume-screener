from openai import OpenAI
from dotenv import load_dotenv
from keys import open_api_key
import os

load_dotenv() 

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def get_resume_improvement_advice(resume_text, job_description):
    prompt = f"""You are a career coach. Analyze the resume and job description. 
Include key things the resume is missing if there are any. 
Suggest 3 improvements to the resume to make it better match the job.

Resume:
{resume_text}

Job Description:
{job_description}"""

    response = client.chat.completions.create(
        model="gpt-4",  
        messages=[
            {"role": "system", "content": "You are an expert resume advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()