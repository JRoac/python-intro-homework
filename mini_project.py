numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return(smallest)      

def find_max(numbers):
    largest = numbers [0]
    
    for number in numbers:
        if number > largest:
            largest = number
    
    return(largest)     

def search(numbers, target):
    for n in range(len(numbers)):
        if numbers[n] == target:   
            return(n)    

    return(-1)

def bubble_sort(numbers):
    sorted_numbers = numbers.copy()   
    swapped = True
    
    while swapped:
        swapped = False

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i +1]:
                sorted_numbers[i], sorted_numbers[i + 1] = (sorted_numbers[i + 1], sorted_numbers[i])
                swapped = True

    return sorted_numbers

def show_menu():
    print("---Number Cruncher---")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a number")
    print("4. Sort Numbers")
    print("5. Quit")

    choice = input("Pick an option (1-5): ")
    return choice


def main():
    while True:
        choice = show_menu()

        if choice == "1":
            minimum = find_min(numbers)
            print(f"The minimum number is {minimum}")

        elif choice == "2":
            maximum = find_max(numbers)
            print(f"The maximum number is {maximum}")

        elif choice == "3":
            try:
                target = int(input("What number do you want to search? "))
                result = search(numbers, target)

                if result != -1:
                    print(f"{target} is at index {result}")
                else:
                    print(f"Cannot find {target}. Sorry.")

            except ValueError:
                print("Please enter an integer!")

        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print(f"Sorted numbers: {sorted_numbers}")

        elif choice == "5":
            print("See you next time!")
            break

        else:
            print("Please pick an option 1-5.")


main()


