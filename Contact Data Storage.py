'''
Contact Data Storage:
Use nested dictionaries as the main data structure for storing contact information.
Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
Store contact details within the inner dictionary, including:
Name
Phone number
Email address
Additional information (e.g., address, notes).
'''

# Initialize an empty dictionary to store contacts
contacts = {}

# Add a new contact
contacts['john@example.com'] = {
    'Name': 'John Doe',
    'Phone number': '123-456-7890',
    'Email address': 'john@example.com',
    'Additional information': {
        'Address': '123 Main St, Anytown, USA',
        'Notes': 'Met at the conference in 2024'
    }
}

# Add another contact
contacts['jane@example.com'] = {
    'Name': 'Jane Smith',
    'Phone number': '987-654-3210',
    'Email address': 'jane@example.com',
    'Additional information': {
        'Address': '456 Maple Ave, Othertown, USA',
        'Notes': 'Colleague from previous job'
    }
}

# Print all contacts
for email, details in contacts.items():
    print(f"Email: {email}")
    for key, value in details.items():
        if key == 'Additional information':
            print('Additional information:')
            for add_key, add_value in value.items():
                print(f"  {add_key}: {add_value}")
        else:
            print(f"{key}: {value}")
    print()
