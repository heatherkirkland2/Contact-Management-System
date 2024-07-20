'''
Menu Actions:
Implement the following actions in response to menu selections:
Adding a new contact with all relevant details.
Editing an existing contact's information (name, phone number, email, etc.).
Deleting a contact by searching for their unique identifier.
Searching for a contact by their unique identifier and displaying their details.
Displaying a list of all contacts with their unique identifiers.
Exporting contacts to a text file in a structured format.
Importing contacts from a text file and adding them to the system. * BONUS
'''
import os
import json

# Initialize an empty dictionary to store contacts
contacts = {}

def add_contact():
    email = input("Enter email address: ")
    if email in contacts:
        print("A contact with this email already exists.")
    else:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        additional_info = input("Enter additional information: ")
        contacts[email] = {'Name': name, 'Phone number': phone, 'Additional information': additional_info}
        print("Contact added successfully.")

def edit_contact():
    email = input("Enter email address of the contact to edit: ")
    if email in contacts:
        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        additional_info = input("Enter new additional information: ")
        contacts[email] = {'Name': name, 'Phone number': phone, 'Additional information': additional_info}
        print("Contact edited successfully.")
    else:
        print("No contact found with this email address.")

def delete_contact():
    email = input("Enter email address of the contact to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully.")
    else:
        print("No contact found with this email address.")

def search_contact():
    email = input("Enter email address of the contact to search: ")
    if email in contacts:
        print("Contact details:")
        print(contacts[email])
    else:
        print("No contact found with this email address.")

def display_contacts():
    print("All contacts:")
    for email, details in contacts.items():
        print(f"Email: {email}, Details: {details}")

def export_contacts():
    with open('contacts.txt', 'w') as f:
        f.write(json.dumps(contacts))
    print("Contacts exported successfully.")

def import_contacts():
    if os.path.exists('contacts.txt'):
        with open('contacts.txt', 'r') as f:
            imported_contacts = json.loads(f.read())
        contacts.update(imported_contacts)
        print("Contacts imported successfully.")
    else:
        print("No contacts file found.")

def main():
    while True:
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
