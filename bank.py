#Banking program 
full = 0
print("\n1.Deposit\n2.Withdraw\n3.Balance")


while True:
    user =int(input("Enter number: "))
    if user == 1:
        deposit = int(input("Enter amount to deposit: $"))
        full += deposit 
        print(f"You have deposited: ${deposit}")
        
    elif user == 2:
        withdraw = int(input("Enter amount to withdraw: "))
        full -= withdraw

        if withdraw > full:
            print("Insufficient amount")
            break
        else:
          print(f"You have withdrawn: ${withdraw}")  
    

    elif user == 3:

        balance = full 
        print(f"Your balance is: ${balance}")
        break
    else:
        print("Invalid input")
        break