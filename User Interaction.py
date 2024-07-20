'''
User Interaction:
Utilize input() to enable users to select menu options and provide contact details.
Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
'''
import os
import json
import re

# Initialize an empty dictionary to store contacts
contacts = {}

def validate_email(email):
    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

def validate_phone(phone):
    # Regular expression for validating a Phone number
    regex = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.match(regex, phone)

def add_contact():
    email = input("Enter email address: ")
    if not validate_email(email):
        print("Invalid email address.")
        return
    if email in contacts:
        print("A contact with this email already exists.")
    else:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        if not validate_phone(phone):
            print("Invalid phone number.")
            return
        additional_info = input("Enter additional information: ")
        contacts[email] = {'Name': name, 'Phone number': phone, 'Additional information': additional_info}
        print("Contact added successfully.")

# ... rest of the functions ...

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
        # ... rest of the choices ...

if __name__ == "__main__":
    main()
