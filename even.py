def main():
    while True:
        try:
            start = int(input("Enter the first number: "))
            end = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid integers.")
    
    if start > end:
        start, end = end, start
    
    print("Even numbers between", start, "and", end, "are:")
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number)

if __name__ == "__main__":
    main()