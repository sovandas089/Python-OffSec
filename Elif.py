#Coffee Menu
name = input("Hello! Wellcome to CatCafe....\n Your Name Please :\n")

menu = "Black Coffee, Cappucino, Frappuccino, Cold Coffee, Green Tea, Milk Tea"

order = input(name + " What would you like from our manu today? Here is what we are serving. \n" + menu +  "\n")
 
if order == "Black Coffee":
    price = 20

elif order == "Cappucino":
    price = 28

elif order == "Frappuccino":
    price = 30

elif order == "Cold Coffee":
    price = 17

elif order == "Green Tea":
    price = 16

elif order == "Milk Tea":
    price = 18

quantity = int(input("How many "+ order + "you want\n"))

total = quantity * price

print("Sir you've to Pay \n" )
print(total)