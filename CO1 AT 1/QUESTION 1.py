import re

resume = """
Name: Ram
Email: ram@gmail.com
Mobile: 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
"""

name = re.search(r"Name:\s*(.*)", resume)
email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', resume)
mobile = re.findall(r'\b\d{10}\b', resume)

skills_list = ["Python", "Java", "SQL", "Machine Learning", "NLP"]
skills_found = []

for skill in skills_list:
    if re.search(skill, resume, re.IGNORECASE):
        skills_found.append(skill)

experience = re.search(r'(\d+)\s+years', resume)

print("----- Candidate Profile -----")

if name:
    print("Name:", name.group(1))

print("Email:", email[0])
print("Mobile:", mobile[0])
print("Skills:", ", ".join(skills_found))

exp_years = int(experience.group(1))
print("Experience:", exp_years, "years")

print("\nEligibility Status")

if exp_years >= 2 and "Python" in skills_found:
    print("Eligible for Shortlisting")
else:
    print("Not Eligible")
