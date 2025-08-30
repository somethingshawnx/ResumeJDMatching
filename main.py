import os
from extractor import load_text
from skills_ner import extract_skills
from scorer import semantic_similarity, compute_score
from recommender import recommend

# Load files
resume_text = load_text("../data/resume.txt")
jd_text = load_text("../data/job_description.txt")

# Load skills list
with open("../skills/skills_list.txt", "r") as f:
    skills_list = [line.strip() for line in f if line.strip()]

# Extract skills
resume_skills = extract_skills(resume_text, skills_list)
jd_skills = extract_skills(jd_text, skills_list)

# Compute similarity and scores
similarity = semantic_similarity(resume_text, jd_text)
final_score, skill_overlap = compute_score(similarity, resume_skills, jd_skills)

# Recommendations
suggestions = recommend(resume_skills, jd_skills)

# Print report
print("=== Resume ↔ Job Description Match Report ===")
print(f"Semantic similarity: {similarity}%")
print(f"Skill overlap: {skill_overlap}%")
print(f"Final match score: {final_score}%\n")
print("Missing skills:", jd_skills - resume_skills)
print("\nSuggestions:")
for s in suggestions:
    print("-", s)
