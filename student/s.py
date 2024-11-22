# Student Management System

# Class to represent a student
class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

# Class to handle the student management operations
class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    # Add a new student
    def add_student(self, student_id, name, age, course):
        if student_id not in self.students:
            new_student = Student(student_id, name, age, course)
            self.students[student_id] = new_student
            print(f"Student {name} added successfully!")
        else:
            print("Student ID already exists!")

    # Display all students
    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            print("Student ID | Name     | Age | Course")
            for student_id, student in self.students.items():
                print(f"{student.student_id} | {student.name} | {student.age} | {student.course}")

    # Update student details
    def update_student(self, student_id):
        if student_id in self.students:
            print(f"Updating details for Student ID {student_id}")
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            course = input("Enter new course: ")

            student = self.students[student_id]
            student.name = name
            student.age = age
            student.course = course
            print(f"Student ID {student_id} updated successfully!")
        else:
            print("Student ID not found.")

    # Delete a student
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student ID {student_id} deleted successfully!")
        else:
            print("Student ID not found.")

# Main program
def main():
    system = StudentManagementSystem()
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            system.add_student(student_id, name, age, course)
        
        elif choice == '2':
            system.display_students()

        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            system.update_student(student_id)

        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            system.delete_student(student_id)

        elif choice == '5':
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the system
if __name__ == "__main__":
    main()
