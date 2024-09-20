
users = []


def create_user():
    user_id = input("Enter user ID: ")
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    
    
    users.append({"id": user_id, "name": name, "email": email})
    print("User added successfully!\n")


def read_users():
    if not users:
        print("No users available.")
        return
    
    print("\nList of users:")
    for user in users:
        print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    print()


def update_user():
    user_id = input("Enter user ID to update: ")
    
    
    for user in users:
        if user['id'] == user_id:
            name = input(f"Enter new name (current: {user['name']}): ")
            email = input(f"Enter new email (current: {user['email']}): ")
            user['name'] = name
            user['email'] = email
            print("User updated successfully!\n")
            return
    
    print("User not found!\n")


def delete_user():
    user_id = input("Enter user ID to delete: ")
    
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            print("User deleted successfully!\n")
            return
    
    print("User not found!\n")

def main():
    while True:
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            create_user()
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.\n")

if __name__ == "__main__":
    main()

