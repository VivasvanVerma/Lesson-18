try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1/num2
    print("Result: ", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except SyntaxError:
    print("Did you put the comma there?")

else:
    print("No Error")

finally:
    print("This will print no matter what.")