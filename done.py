def main():
    total = 0
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)
            total += number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"The sum of the entered numbers is: {total}")

if __name__ == "__main__":
    main()