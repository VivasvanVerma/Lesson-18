try:
    n = int(input("Enter a number: "))
    if n%2 == 0:
        while n == n:
            print("bye")

except ValueError:
    print("Only numbers allowed.")