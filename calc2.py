# Simple Calculator

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
operations = int(input("Choose an operation (1-4): "))

if operations in [1, 2, 3, 4]:  # Ensure valid input
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    if operations == 1:
        total = first_number + second_number
        print(f"The total is: {total}")
    elif operations == 2:
        total = first_number - second_number
        print(f"The difference is: {total}")
    elif operations == 3:
        total = first_number * second_number
        print(f"The product is: {total}")
    elif operations == 4:
        if second_number == 0:
            print("Error: Cannot divide by zero!")
        else:
            total = first_number / second_number
            print(f"The quotient is: {total}")
else:
    print("Invalid choice! Please enter a number between 1 and 4.")
