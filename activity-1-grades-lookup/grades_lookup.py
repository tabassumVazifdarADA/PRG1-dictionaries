student_grades = {
    "Elara": 85,
    "Kwame": 92,
    "Siobhan": 78,
    "Kai": 96
}

print(student_grades["Kwame"])
print(student_grades.get("Aisha", "Not found"))

result = student_grades["Elara"]
print(result)

print(student_grades.get("Aisha", "Missing"))
student_grades["Tabassum"] = 100
print(student_grades["Tabassum"])
student_grades["Kwame"] = 45
print(student_grades["Kwame"])
#print(student_grades["Aisha", ])
