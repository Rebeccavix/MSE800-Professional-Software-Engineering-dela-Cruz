from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, add_course, create_course_table, search_course


def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Add Course")
    print("6. Search Course by ID or Name")
    print("7. Exit")


def main():
    create_table()
    create_course_table()

    while True:
        menu()
        choice = input("Select an option (1-7): ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            name = input("Enter course name: ")
            unit = int(input("Enter unit count: "))
            add_course(name, unit)
        elif choice == '6':
            course_id = input(
                "Enter course ID (leave blank if searching by name): ")
            name = input(
                "Enter course name (leave blank if searching by ID): ")
            courses = search_course(
                course_id if course_id else None, name if name else None)
            for course in courses:
                print(course)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
