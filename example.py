total = 0
while True:

    inputt = (input("enter numbers to add; "))
    if inputt == "done":
        break
    try:
        numbers = float(inputt)

        total += numbers
    except ValueError:
        print("INVALID INPUT")


print(f"Total is: {total}")   
    
        