import json
students = [
    {
        "name": "wilfred",
        "age": 21,
        "course": "computer science"
    },
    {
        "name": "john",
        "age": 20,
        "course": "computer science"
    }
]
with open("student.json", "w")as file:
    json.dump(students, file, indent=4)

with open("student.json", "r")as file:
    students = json.load(file)
    print(students)
    

