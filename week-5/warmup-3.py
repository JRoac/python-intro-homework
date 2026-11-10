def linear_search(data, target):
    for n in range (len(data)):
        if data[n] == target:
            return n
    return -1    

name = input ("Type a name: ").title()
contact_list = ["Paige", "Angel", "Gabby", "A'ja", "Chelsea", "Shakira"]
result = linear_search(contact_list, name)

if result != -1:
    print(f"{name}, was found at index: {result}")
else:
    print(f"{name}, not found.")
