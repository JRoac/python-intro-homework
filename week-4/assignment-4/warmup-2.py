student = {
    "name": "Issac",
    "grade": "11th",
    "subjects": ["math", "history", "science"]
}

for key, value in student.items():
    print(key, value)

student["graduated"] = False

print(student)