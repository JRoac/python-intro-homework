import os

print(os.getcwd())

if os.path.exists("data/expenses.csv"):
    print("Found!")
else:
    print("I can't find it!")    

path = os.path.join("..", "data", "expenses.csv")
print(path)    

