print("=================STUDENT MANAGER===============")
student = []
while True:
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Goodbye")
    choice = input("Enter choice: ")
    if choice == "1":
        number = int (input("Enter number of students: "))
        for i in range(number):
            name = input("Add student: ").lower()
            student.append(name)
    elif choice == "2":
        view = input("View students").lower()
        for name in student:
            print("Student: ",name)
    elif choice == "3":
        search = input("search for a student: ").lower()
        if search in student:
            print("Student: ",search)
        else:
            print("Student not found")
    elif choice == "4":
        print("Auf Wiedersehen")
    else:
        print("Invalid choice")
    if choice == "4":
        break
