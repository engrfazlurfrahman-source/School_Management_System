from school_management import Course, Student


def main():
    while True:
        print("\n===== School Management System =====")
        print("1. Admit New Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Show All Students")
        print("5. Show student Password")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            course_name = input("Enter Course Name: ")
            password = input("Set Student Password: ")

            course = Course(course_name)
            student = Student(roll, name, course.course_name, password)
            student.save_to_file()

            print("\nStudent added successfully.")

        elif choice == "2":
            roll = input("Enter roll to update: ")
            name = input("New name: ")
            course = input("New course: ")
            password = input("New password: ")
            Student.update_student(roll, name, course, password)
            print("\nStudent updated successfully.")

        elif choice == "3":
            roll = input("Enter roll to delete: ")
            Student.delete_student(roll)

        elif choice == "4":
            Student.show_all_students()

        elif choice == "5":
            roll = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")

            result = Student.get_password_by_roll_and_name(roll, name)
            print(result)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
