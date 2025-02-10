shopping_list = []
# Limit the number of items
MAX_ITEMS = 10  

print("Welcome to the Shopping List Manager!")

while True:
    print("\nMenu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        if len(shopping_list) < MAX_ITEMS:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        else:
            print("Shopping list is full! You cannot add more items.")
    
    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print("Item not found in the shopping list.")
    
    elif choice == "3":
        print("\nCurrent Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    
    elif choice == "4":
        print("Exiting the Shopping List Manager. Have a great day!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
