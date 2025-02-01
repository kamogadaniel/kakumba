print("Hello, you are most welcome to internetchuck coffee!")

name = input("What is your name?\n")

if name == "Dave":
    print("You are not welcome, evil Dave. Get out now!!!!"):
    exit()

else:
    print("Thanks so much for coming " + name)


menu = "tea, coffee, capucinno, latte, water"

print(name + ", what would you like to have today " + "heres our menu for the day\n" + menu)


 
menu = input()

price = 10

quantity = print("each coffee costs " + str(price) +" how many do you want")

quantity = input()

total = price * int(quantity)

print("Your total is " + str(total) + ", please keep in mind.")

print("Thats great, " + name + ", we shall have your " + str(quantity) + " " + menu + " ready in a moment ")

