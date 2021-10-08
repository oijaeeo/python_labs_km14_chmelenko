# Task 2

items = input("Please enter objects names (example : orange apple cherry) :  ").split(" ")

print(items[0], end="")
for i in range(1, len(items) - 1):
    print(", " + items[1], end="")
if len(items) > 1:
    print(" and " + items[-1])
