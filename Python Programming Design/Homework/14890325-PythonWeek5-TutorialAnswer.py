# Student ID: 14890325
# Student Name: Nguyen Ba Gia Hien

shopping_list = ["milk", "bread", "eggs", "cheese", "fruits"]

item = input("Please input the item you want to search: ")
index = 0
found = False
while index < len(shopping_list):
    if shopping_list[index] == item:
        found = True
        break
    index += 1

if found:
    print("Yes, the item '{}' is found in the shopping list.".format(item))
else:
    print("No, the item '{}' is not found in the shopping list.".format(item))