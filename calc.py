#print("This is a simple calculator")


print("1. Add\n 2. subtract\n 3. multiply\n 4. divide\n")
operations = int(input("Enter numbers 1-4: "))

if operations in [1, 2, 3, 4]:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    
    if operations == 1:
        total = first_number + second_number
        print("The total is : " + str(total))

    elif operations == 2:
        total = first_number - second_number
        print("The difference is : " + str(total))

    elif operations == 3:
    
        total = first_number * second_number
        print("The product is : " + str(total))
    elif operations == 4:

       if second_number == 0:

             print("Cant divide by zero")
       else:

             total = first_number / second_number
            
       print("The quotient is : " + str(total))
else:
    print("Invalid input")


