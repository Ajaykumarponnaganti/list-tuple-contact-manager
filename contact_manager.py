# Contact manager application

contacts = []
# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    for contact in contacts:
        if contact[0] == name:
            print("Contact already exists!")
            return
    
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
        return
    print("\nList of Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} - {contact[1]} - {contact[2]}")

def search_contact():
    name = input("Enter name to search: ")
    for contact in contacts:
        if contact[0] == name:
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            return
    print("Contact not found!")

def update_contact():
    name = input("Enter name to update: ")
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            new_phone = input("Enter new phone number: ")
            contacts[i] = (contact[0], new_phone, contact[2])  # Replace the tuple
            print("Contact updated successfully!")
            return
    print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact[0] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found!")

while True:
    print("\nWelcome to Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")


------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 2: Implementing CRUD Operations

1. Add a New Contact. Prompt the user for name, phone number, and email. Append the contact as a tuple to the list. Prevent duplicate names.

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 1
Enter Name: Ajay
Enter Phone Number: 1234
Enter Email: qwe
Contact added successfully!

-------------------------------------------------------------------------

2. View All Contacts. Display all stored contacts in a formatted manner.

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 2
List of Contacts:
1. Ajay - 1234 - qwe

-------------------------------------------------------------------------

3. Search for a Contact by Name. Allow the user to enter a name. Find and display the corresponding contact.

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 3
Enter name to search: Ajay
Contact Found: Ajay - 1234 - qwe

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 3
Enter name to search: abc
Contact not found!

-------------------------------------------------------------------------

4. Update a Contact’s Phone Number. Search for a contact by name. If found, modify the phone number while keeping the name and email unchanged. Since tuples are immutable, replace the entire tuple in the list.

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
Enter your choice: 4
Enter name to update: Ajay
Enter new phone number: 4567
Contact updated successfully!

-----------------------------------------------------------------------------------

5. Delete a Contact. Search for a contact by name. Remove the contact from the list

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 5
Enter name to delete: Ajay
Contact deleted successfully!


Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 2
No contacts found!

------------------------------------------------------------------------------------

** Exiting from the contact manager

Welcome to Contact Manager
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 6
Exiting Contact Manager. Goodbye!

=== Code Execution Successful ===
