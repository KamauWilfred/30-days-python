import csv

with open("students.csv", "w", newline="")as file:
    writer = csv.writer(file)

    rows = [
        ["name", "age", "course"],
        ["wilfred", 21, "computer science"],
        ["john", 19, "medicine"],
        ["jane", 20, "accounts"]
    ]

    writer.writerows(rows)

with open("students.csv", "r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        