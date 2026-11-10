while True:
    integer = input("Enter a positive integer: ")
    try: 
        integer = int(integer)
        if integer > 0:
            print(f"Great job! : {integer}")
            break
        else:
            print("Wrong! Enter a positive integer: ")

    except ValueError:
        print("Please enter a positive integer!")        



