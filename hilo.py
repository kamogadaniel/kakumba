import random

correct = random.randint(1,10)
user = None

while user != correct:
    user = int(input("Guess(1-10): "))
    if user > correct:
        print("too high ")
    elif user < correct:
        print("too low ")
    else:

        print("you're correct")