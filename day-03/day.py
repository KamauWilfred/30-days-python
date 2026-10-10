Students = int(input("How many students do you want to enter?"))
passed = 0
failed = 0
for i in range(Students):
    Marks = int(input("Enter marks"))
    if 100>=Marks>=80:
        print("Grade A")
    elif 79>=Marks>=70:
        print("Grade B")
    elif 69>=Marks>=60:
        print("Grade C")
    elif 59>=Marks>=50:
        print("Grade D")
    elif 49>=Marks>=0:
        print("Fail")
    else:
        print("Invalid input")
    if 100>=Marks>=0:
        if  100>=Marks>=50:
            passed += 1
        else:
            failed += 1
    else:
        print("Invalid mark")
print("==========Summary==========")
print("Total students entered is", i+1)
print("Passed students:",passed)
print("Failed students:",failed)