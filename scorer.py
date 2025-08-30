from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text, jd_text):
    emb = model.encode([resume_text, jd_text])
    sim = cosine_similarity([emb[0]], [emb[1]])[0][0]
    return round(sim * 100, 2)

def compute_score(similarity, resume_skills, jd_skills):
    skill_overlap = len(resume_skills & jd_skills) / max(len(jd_skills), 1) * 100
    final_score = 0.5 * similarity + 0.5 * skill_overlap
    return round(final_score, 2), round(skill_overlap, 2)
