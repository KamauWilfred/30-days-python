while True:
    try:
        number = int(input("Enter number: "))
        if 0 <= number <= 100:
            print(number)
            break
        else:
            print("Invalid marks")
    except ValueError:
        print("invalid number")

