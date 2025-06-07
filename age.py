def checkAge():
    try:
        age = input("Enter your age: ")
        age = int(age)
        if age<0:
            raise ValueError("Age cannot be negative.")
        if age%2 == 0:
            print("Age is Even.")
        else:
            print("Age is Odd.")
    except ValueError as e:
        print("Error: ", e)

checkAge()



