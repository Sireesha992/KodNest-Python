skills=[]
for i in range(1):
    skill = ("Python","SQL","Git","Communication","DSA")
    skills.append(skill)
skill_record = tuple(skills)
first_three = skill_record[0:3]
last_two = skill_record[-2:]
alternate_skills = skill_record[::2]
reversed_skills = skill_record[::-1]
print("Skill Record",skill_record)
print("First Three",first_three)
print("Last Two",last_two)
print("Alternate Skills:", alternate_skills)
print("Reversed Skills:", reversed_skills)