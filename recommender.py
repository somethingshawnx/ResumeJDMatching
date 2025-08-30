def recommend(resume_skills, jd_skills):
    missing = jd_skills - resume_skills
    suggestions = []
    for skill in missing:
        suggestions.append(f"Add a bullet point showing experience with '{skill}'.")
    return suggestions
