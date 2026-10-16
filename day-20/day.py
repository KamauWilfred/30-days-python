import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format=("%(asctime)s - %(levelname)s - %(message)s")
)

logging.info("Application has started!")

student_info = []

while True:
    try:

        number = int(input("\nEnter the number of students to add: "))

        if number > 0:
            break

        else:
            logging.warning("Input is not a positive number!")
            print("Enter a positive number!")

    except ValueError:
        logging.warning("Input is not an integer value!")
        print("Enter an integer value!")

for i in range(number):
    print(f"\nstudent {i + 1}:")

    while True:
        try:
            student_id = int(input("Enter student's ID: "))    

            if student_id > 0:
                break

            else:
                logging.warning("Input is not apositive number!")
                print("Enter a positive number!")

        except ValueError:
            logging.warning("Input is not an integer value!")
            print("Enter an integer value!")
    
    while True:
        
        student_name = input("Enter name of student: ").strip().lower()

        if student_name:
            break

        else:
            logging.warning("No name entered!")
            print("Name cannot be empty")

    if student_id > 0 and student_name:
        logging.info("Student added successfully!")
        print("Student added successfully!")
        student_info.append((student_id, student_name))

while True:
    try:

        search = int(input("\nEnter student's ID to search: "))

        if search > 0:
            break

        else:
            logging.warning("Input is not apositive value!")
            print("Enter a positive value!")

    except ValueError:
        logging.warning("Input is not an integer value!")
        print("Enter an integer value!")

found = False

for student in student_info:
    if search == student[0]:
        logging.info("Student found!")
        print("\nStudent found!")
        print(
            f"ID: {student[0]} | Name: {student[1]}"
        )

        found = True

if not found:
    logging.warning("Student account not found!")
    print("Student account not found")
