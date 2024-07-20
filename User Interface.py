'''
User Interface (UI):
Create a user-friendly command-line interface (CLI) for the Contact Management System.
Display a welcoming message and provide a menu with the following options:

Welcome to the Contact Management System! 
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit
'''

def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            # Add a new contact
            pass
        elif choice == '2':
            # Edit an existing contact
            pass
        elif choice == '3':
            # Delete a contact
            pass
        elif choice == '4':
            # Search for a contact
            pass
        elif choice == '5':
            # Display all contacts
            pass
        elif choice == '6':
            # Export contacts to a text file
            pass
        elif choice == '7':
            # Import contacts from a text file
            pass
        elif choice == '8':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
