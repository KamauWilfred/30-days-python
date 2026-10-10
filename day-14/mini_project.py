marks = [45,72,65,20,35,87,42,56,93.39]
doubled_marks = map(lambda x: x * 2, marks)
passed = filter(lambda x: x >= 50, marks)
top_students = filter(lambda x: x > 80, marks)
bonus_marks = map(lambda x: x + 5, marks)
grades = ['A'if mark >= 90 else 'B' if mark >= 80 else 'C' if mark >= 70 else 'D' if mark >= 60 else 'F' for mark in marks ]
print("Doubled marks: ", list(doubled_marks))
print("Passed: ", list(passed))
print("Top students: ", list(top_students))
print("Bonus marks: ", list(bonus_marks))
print("Grades: ", grades)
