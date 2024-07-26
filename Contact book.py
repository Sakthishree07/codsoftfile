class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email)
            print("Contact added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for name, contact in self.contacts.items():
                print(contact)

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            print("Contact updated.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("\n2. View Contacts")
        print("\n3. Update Contact")
        print("\n4. Delete Contact")
        print("\n5. Exit")
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
