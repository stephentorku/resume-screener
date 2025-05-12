from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_resume_to_job(resume_text: str, job_text: str) -> float:
    resume_emb = model.encode(resume_text, convert_to_tensor=True)
    job_emb = model.encode(job_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(resume_emb, job_emb)
    return float(similarity.item()) 