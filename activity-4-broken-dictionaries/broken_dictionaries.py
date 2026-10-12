# Three things below are wrong. Nothing crashes.

student_grades = {
    "Elara": 85,
    "Kwame": 92,
    "Siobhan": 78,
    "Kai": 96
}

class_list = ["Elara", "Kwame", "Siobhan", "Kai", "Aisha"]


def class_average(grades, names):
    """Return the average grade of the students in names."""
    total = 0
    for name in names:
        total = total + grades.get(name, 0)
    return total / len(grades)


def is_registered(grades, name):
    """Return True if name has a grade recorded, False if not."""
    return name in grades


def record_grade(grades, name, score):
    """Record a score for a student who does not already have one.
    Leave an existing grade alone."""
    if name in grades:
        return
    else:
        grades[name] = score


print(f"Class average: {class_average(student_grades, class_list):.1f}")

print(f"Is Kwame registered? {is_registered(student_grades, 'Kwame')}")
print(f"Is Aisha registered? {is_registered(student_grades, 'Aisha')}")

record_grade(student_grades, "Aisha", 61)
record_grade(student_grades, "Kai", 12)
print(student_grades)
