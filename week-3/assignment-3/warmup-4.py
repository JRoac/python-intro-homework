number = int(input("Pick a number, any number "))

if number > 0:
    print(number, "is positive.")
elif number < 0:
    print(number, "is negative.")    
elif number == 0:
    print(number, "is zero.") 

if number % 2 == 0:
    print(number, "is even.")   
else:
    print(number, "is odd.")      