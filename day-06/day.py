students = [
    {
        "name": "wilfred",
        "age": 21,
        "course": "computer science"
    },
    {
        "name": "john",
        "age": 20,
        "course": "economics"
    }
]
for student in students:
    print(student["name"])
    print(student["age"])
    print(student["course"])
    print(f"Name: {student['name']} | Age:{student['age']} | Course:{student['course']}")
search = input("search for student: ").lower()
found = False
for student in students:
    if search in student["name"]:
        print("Student found")
        found = True
    if not found: 
        print("No such student")