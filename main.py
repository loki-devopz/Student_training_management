from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from attendance import (
    mark_attendance,
    view_attendance
)

from marks import (
    enter_marks,
    view_marks
)

from reports import generate_report

from exceptions import StudentNotFoundError


def search_student_menu():

    student_id = input("Enter Student ID: ").strip()

    try:
        student = search_student(student_id)

        print("\nStudent Found!")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Course:", student[2])

    except StudentNotFoundError as error:
        print(error)


def main():
    """Main application function."""

    while True:

        print("\n")
        print("=" * 45)
        print("     STUDENT TRAINING MANAGEMENT")
        print("=" * 45)

        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Mark Attendance")
        print("7. View Attendance")
        print("8. Enter Student Marks")
        print("9. View Student Marks")
        print("10. Generate Student Report")
        print("11. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student_menu()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            mark_attendance()

        elif choice == "7":
            view_attendance()

        elif choice == "8":
            enter_marks()

        elif choice == "9":
            view_marks()

        elif choice == "10":
            generate_report()

        elif choice == "11":
            print("Thank you for using STMS!")
            break

        else:
            print("Invalid choice! Please try again.")
            continue


if __name__ == "__main__":
    try:
        main()

    except (ValueError, OSError) as error:
        print("Application error:", error)

