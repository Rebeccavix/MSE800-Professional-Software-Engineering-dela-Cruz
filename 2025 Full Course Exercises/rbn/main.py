from database import create_table
from user_manager import add_user, view_users, search_user, delete_user, search_user_by_id, insert_course, search_course, create_enrollment_table, enroll_user_in_course, create_course_table


def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Search User by Name and ID")
    print("6. Insert Course")
    print("7. Enroll User in Course")
    print("8. Search Course by ID and User Name")
    print("9. Exit")


def main():
    create_table()
    create_enrollment_table()
    create_course_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
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
            name = input("Enter name to search: ")
            user_id = int(input("Enter ID to search: "))

            # Separate searches
            users_by_name = search_user(name)
            users_by_id = search_user_by_id(name, user_id)

            for user in users_by_name:
                print("Found by name:", user)
            for user in users_by_id:
                print("Found by name and ID:", user)

        elif choice == '6':
            course_id = int(input("Enter Course ID: "))
            course_name = input("Enter Course Name: ")
            course_unit = int(input("Enter Course Unit: "))
            insert_course(course_id, course_name, course_unit)

        elif choice == '7':
            user_id = int(input("Enter User ID to enroll: "))
            course_id = int(input("Enter Course ID to enroll in: "))
            enroll_user_in_course(user_id, course_id)

        elif choice == '8':
            course_id = int(input("Enter Course ID to search: "))
            user_name = input("Enter User Name to match: ")
            results = search_course(course_id, user_name)
            for row in results:
                print("Found:", row)

        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
