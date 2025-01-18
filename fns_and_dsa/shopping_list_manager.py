# define the display menu function 
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# define the shopping list
shopping_list = []
    
while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # prompt for add item
            item = input("Enter name of item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} has been added to the shopping list.")
            else:
                print("Item name cannot be empty!")

        elif choice == "2":
            # prompt to remove item
            item = input("Enter name of item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not in the shopping list")

        elif choice == "3":
            # prompt to view shopping list
            if shopping_list:
                print("Your shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == "4":
            # prompt to exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")