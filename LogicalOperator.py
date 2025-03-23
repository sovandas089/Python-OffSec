print("hello! wellcome to OffSec Journey ")

name = input(
    "Who are you ?\n"
)
#Or is a logical operator
if(name =="Psycho" or name == "Maddy"):
    psycho_status = input("Are you Psycho?\n")
    good_deeds = int(input("How many good deeds have you done\n"))
    #and is a logical operator
    #It is a nested if
    if psycho_status == "Yes" and good_deeds < 5:
     print("Sorry Man! I can't allow you!!!!")
     #Here is Nested else
    else:
       print("Most wellcome Brother") 
else:
    print("hey "+ name +", Most wellcome")
 