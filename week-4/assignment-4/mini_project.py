students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_score = 50
top_student = ""

for student in students:
    if student["score"] > top_score:
        top_score = student["score"]
        top_student = student["name"]

print("Top Scorer:", top_student)
print("Highest score:", top_score)

total = 0

for student in students:
    total += student["score"]
average = total / len(students)     
print("Class average:", average)

unique_subjects = set()

for student in students:
    unique_subjects.add(student["subject"])
print("Unique Subjects:", unique_subjects)

high_scorers = []

for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])
print("High scorers:", high_scorers)        