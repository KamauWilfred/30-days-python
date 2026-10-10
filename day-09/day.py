while True:
    print("\n1. search student")
    print("2. add student")
    print("3. exit")
    choice = input("Enter choice: ")
    if choice == "1":
        search = input("Search for student: ").lower()
        with open("student.txt", "r") as file:
            content = file.read()
        if search in content.lower():
            print(search, "found")
        else:
            print(search, "not found")
    elif choice == "2":
        number = int(input("Enter number of students: "))
        for i in range(number):
            name = input("Enter name: ").lower()
            course = input("Enter course: ").lower()
            with open("student.txt", "a") as file:
                file.write(f"Name: {name}\n")
                file.write(f"Course: {course}\n\n")
    elif choice == "3":
        print("Auf weidesehn!")
    else:
        print("Invalid choice!")
    if choice == "3":
        break
