numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("---Number Cruncher---")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a number")
    print("4. Sort Numbers")
    print("5. Quit")

    choice = input("Pick an option (1-5): ")

    if choice == "5":
        print("See you next time! ")
        break

    elif choice == "1":
        print("Finding minimum! ")
        smallest = numbers[0] 
        for number in numbers:
            if number < smallest:
                smallest = number
        print(f"The minimum number is {smallest}")    

    elif choice == "2":
        print("Finding maximum! ")    
        largest = numbers [0]
        for number in numbers:
            if number > largest:
                largest = number
        print(f"The maximum number is {largest}")   

    elif choice == "3":
        print("Searching..... ") 

        try:
            search = int(input("What number do you want to search? "))
            found = False 
            for n in range(len(numbers)):
                if numbers[n] == search:
                    found = True
                    print(f"I've found {search} at index {n}")
                    break
            if found == False:
                print(f"I didn't find {search}. Sorry.")
        except ValueError:
            print("Please pick an integer!")        

    elif choice == "4":
        print("Sorting..... ") 
        sorted_numbers = numbers.copy()   
        swapped = True

        while swapped:
            swapped = False
            for i in range(len(sorted_numbers) - 1):
                if sorted_numbers[i] > sorted_numbers[i +1]:
                    sorted_numbers[i], sorted_numbers[i + 1] = sorted_numbers[i + 1], sorted_numbers[i]
                    swapped = True
        print(f"Sorted numbers: {sorted_numbers}")           
    else:
        print("Please pick an option 1-5.")                             
