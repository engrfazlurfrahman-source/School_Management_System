import os

# ---------- File & Directory Setup ----------
DATA_DIR = "school_data"
FILE_PATH = os.path.join(DATA_DIR, "students.txt")

os.makedirs(DATA_DIR, exist_ok=True)


class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Student:
    def __init__(self, roll, name, enrolled_course, password):
        self.roll = roll
        self.name = name
        self.enrolled_course = enrolled_course
        self.__password = password  # Private (Encapsulation)

    # Getter for password
    def get_password(self):
        return self.__password

    # -------- SAVE --------
    def save_to_file(self):
        with open(FILE_PATH, "a") as file:
            file.write(f"{self.roll},{self.name},{self.enrolled_course},{self.__password}\n")

   # -------- UPDATE --------
    @staticmethod
    def update_student(roll_no, new_name, new_course,new_password):
        updated = False
        students = []

        with open(FILE_PATH, "r") as file:
            students = file.readlines()

        with open(FILE_PATH, "w") as file:
            for line in students:
                roll, name, course,password = line.strip().split(",")
                if roll == roll_no:
                    file.write(f"{roll},{new_name},{new_course},{new_password}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("\nStudent record updated successfully.")
        else:
            print("\nStudent not found.")

    # -------- DELETE --------
    @staticmethod
    def delete_student(roll_no):
        deleted = False

        with open(FILE_PATH, "r") as file:
            students = file.readlines()

        with open(FILE_PATH, "w") as file:
            for line in students:
                roll, _, _, _ = line.strip().split(",")
                if roll != roll_no:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("\nStudent deleted successfully.")
        else:
            print("\nStudent not found.")

 # -------- SHOW ALL --------
    @staticmethod
    def show_all_students():
        if not os.path.exists(FILE_PATH):
            print("\nNo records found.")
            return

        print("\n--- Student List ---")
        with open(FILE_PATH, "r") as file:
            for line in file:
                roll, name, course,_ = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Course: {course}")

    @staticmethod
    def get_password_by_roll_and_name(roll_input, name_input):
        if not os.path.exists(FILE_PATH):
            return "No student records found."

        with open(FILE_PATH, "r") as file:
            for line in file:
                roll, name, course, password = line.strip().split(",")

                if roll == roll_input and name.lower() == name_input.lower():
                    return f"Password for {name} : {password}"

        return "Student not found or details do not match."