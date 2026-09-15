import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    contacts = load_contacts()
    contacts.append({
        "name": input("Enter name: "),
        "phone": input("Enter phone number: "),
        "email": input("Enter email: ")
    })
    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n===== 📞 Contacts =====")
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")

def search_contact():
    contacts = load_contacts()
    search = input("Enter name to search: ").lower()
    found = False
    for contact in contacts:
        if search in contact["name"].lower():
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
    if not found:
        print("❌ Contact not found.")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("✅ Contact deleted.")
            return
    print("❌ Contact not found.")

def main():
    while True:
        print("\n===== 📞 Contact Book =====")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Delete Contact\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1": add_contact()
        elif choice == "2": view_contacts()
        elif choice == "3": search_contact()
        elif choice == "4": delete_contact()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else: print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
