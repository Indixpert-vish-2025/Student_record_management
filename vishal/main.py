from student_functions import register_student, display_students

def main():
    while True:
        print("1. Register Student")
        print("2. Display All Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
