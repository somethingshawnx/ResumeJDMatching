from rapidfuzz import fuzz

def extract_skills(text, skills_list, threshold=80):
    found = []
    for skill in skills_list:
        if fuzz.partial_ratio(skill.lower(), text.lower()) >= threshold:
            found.append(skill.lower())
    return set(found)
