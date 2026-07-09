def extract_skills(text):
    skills_list = [
        "Python", "Java", "C", "C++", "SQL", "HTML", "CSS",
        "JavaScript", "React", "Node.js", "Flask", "Django",
        "Machine Learning", "Deep Learning", "Data Analysis",
        "Pandas", "NumPy", "Matplotlib", "Seaborn",
        "Git", "GitHub", "Docker", "Kubernetes",
        "AWS", "Azure", "Linux", "MySQL", "SQLite",
        "Excel", "Power BI", "Tableau"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
