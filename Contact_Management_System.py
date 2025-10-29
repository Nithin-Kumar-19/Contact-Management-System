# Contact Management System

# Global dictionary to store contacts
contacts = {}


# Function to add a new contact
def add_contact(name, phone):
    """Add a new contact to the dictionary."""
    if name in contacts:
        print(f"{name} already exists.")
    else:
        contacts[name] = phone
        print(f"Contact {name} added successfully.")


# Function to search for a contact
def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        return f"Name: {name}, Phone: {contacts[name]}"
    else:
        return f"{name} not found."


# Function to display all contacts
def display_contacts():
    """Display all saved contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


# Main function to control user interaction
def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to search: ").strip()
            print(search_contact(name))
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point
if __name__ == "__main__":
    main()
