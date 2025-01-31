def main():
    total = 0
    for i in range(5):
        while True:
            try:
                number = float(input(f"Enter number {i + 1}: "))
                total += number
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    print(f"The sum of the numbers is: {total}")

if __name__ == "__main__":
    main()
