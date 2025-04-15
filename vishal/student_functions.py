from student_data import load_students, save_students

students = load_students()

def register_student():
    print("\n--- Student Registration ---")
    student = {}
    student['ID'] = input("Enter Student ID: ")
    student['Name'] = input("Enter Name: ")
    student['Contact'] = input("Enter Contact Number: ")
    student['Email'] = input("Enter Email Address: ")

    # Multiple education entries
    education_list = []
    while True:
        education = input("Enter Education: ")
        year = input("Which year did you complete this education? (e.g., 2022): ")
        education_list.append({"Education": education, "Year": year})

        more = input("Do you want to add another education? (yes/no): ").strip().lower()
        if more != 'yes':
            break

    student['Education'] = education_list
    students.append(student)
    save_students(students)
    print("Student registered successfully!\n")

def display_students():
    if not students:
        print("\nNo students registered yet.\n")
        return
    print("\n--- Registered Students ---")
    for i, student in enumerate(students, 1):
        print(f"\nStudent {i}:")
        print(f"ID      : {student['ID']}")
        print(f"Name    : {student['Name']}")
        print(f"Contact : {student['Contact']}")
        print(f"Email   : {student['Email']}")
        print("Education Details:")
        for edu in student['Education']:
            print(f"  - {edu['Education']} (Completed in {edu['Year']})")
    print()
