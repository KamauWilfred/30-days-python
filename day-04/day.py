Student = ["Wilfred","Brian","John"]
print(Student[0])
Student.append("Grace")
print(Student[3])
Student.append("Kevin")
print(Student)
print(len(Student))
Student.remove("John")
del Student[1]
Student.pop(2)
print(Student)
Student.insert(2,"John")
print(Student)
student="Wilfred","john"
for student in Student:
    print("Student:" +student)