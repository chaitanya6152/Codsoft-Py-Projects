import json
import os

FILE_NAME = 'contacts.json'

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, 'w') as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact for '{name}' added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"\nName: {name}\nPhone: {info['phone']}\nEmail: {info.get('email', '')}")

# Search contact by name
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\nName: {name}\nPhone: {contacts[name]['phone']}\nEmail: {contacts[name].get('email', '')}")
    else:
        print("Contact not found.")

# Update a contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        print("Leave blank to keep old value.")
        phone = input(f"New phone (old: {contacts[name]['phone']}): ").strip()
        email = input(f"New email (old: {contacts[name].get('email', '')}): ").strip()
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        save_contacts(contacts)
        print("Contact updated.")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

# Run the program
if __name__ == "__main__":
    main()
