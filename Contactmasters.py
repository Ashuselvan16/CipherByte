import json

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

def select_contact(contacts):
    name = input("Enter contact name to select: ")
    if name in contacts:
        print(f"Contact {name}: {contacts[name]}")
    else:
        print(f"Contact {name} not found.")

def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)
    
    while True:
        print("\n1. Add contact")
        print("2. Delete contact")
        print("3. Select contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            select_contact(contacts)
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
