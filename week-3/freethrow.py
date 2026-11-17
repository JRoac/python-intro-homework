starter = input("Is the player a starter? y or n ")
free_throw = int(input("What is the player free throw percentage? "))

if starter == "y" and free_throw >= 80:
    print("Go shoot the technical foul free throws!")
elif starter == "y" and free_throw <= 80:
    print("No, somebody else will shoot.")
elif starter == "n" and free_throw >= 80:
    print("Ok, you will shoot if you're in the game!") 
else:
    print("No, you have to practice more!")