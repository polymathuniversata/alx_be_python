#!/usr/bin/python3
"""
Shopping List Manager: A simple command-line application to manage a shopping list.

This script allows users to:
1. Add items to a shopping list
2. Remove items from the list
3. View all items in the list
4. Exit the program

The script demonstrates the use of lists in Python for data storage and manipulation.
"""

def display_menu():
    """
    Display the menu options for the shopping list manager.
    Presents four options to the user: add item, remove item, view list, and exit.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to control the shopping list application flow.
    
    Creates an empty shopping list and processes user input in a loop
    until the user chooses to exit.
    """
    # Initialize empty shopping list
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Option 1: Add an item to the shopping list
            item = input("Enter the item to add: ")
            # Use the append() method to add the item to the list
            shopping_list.append(item)
            # Confirm to the user that the item was added
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':
            # Option 2: Remove an item from the shopping list
            item = input("Enter the item to remove: ")
            # Check if the item exists in the list before attempting to remove it
            if item in shopping_list:
                # Use the remove() method to remove the item from the list
                shopping_list.remove(item)
                # Confirm to the user that the item was removed
                print(f"'{item}' has been removed from your shopping list.")
            else:
                # Inform the user if the item was not found in the list
                print(f"'{item}' was not found in your shopping list.")
        
        elif choice == '3':
            # Option 3: Display all items in the shopping list
            if shopping_list:
                print("\nYour Shopping List:")
                # Loop through each item in the list and print it
                for item in shopping_list:
                    print(item)
            else:
                # If the list is empty, inform the user
                print("Your shopping list is empty.")
        
        elif choice == '4':
            # Option 4: Exit the program
            print("Goodbye!")
            # Break out of the while loop to end the program
            break
        
        else:
            # Handle invalid menu choices gracefully
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # This ensures the main() function only runs when the script is executed directly
    main()
