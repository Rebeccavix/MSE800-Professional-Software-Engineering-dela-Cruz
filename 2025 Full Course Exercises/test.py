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
