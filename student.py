from file_handler import read_records, append_record, write_records
from exceptions import StudentNotFoundError

FILE = "students.txt"


def add_student():
    """Register a new student."""

    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()

    if not student_id or not name or not course:
        print("All fields are required!")
        return

    students = read_records(FILE)

    if any(s[0] == student_id for s in students):
        print("Student ID already exists!")
        return

    append_record(FILE, [student_id, name, course])
    print("Student registered successfully!")


def view_students():
    """Display all registered students."""

    students = read_records(FILE)

    if not students:
        print("No student records found.")
        return

    print("\nID\tName\tCourse")
    print("-" * 40)

    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}")


def search_student(student_id):
    """Find a student using their ID."""

    students = read_records(FILE)

    for student in students:
        if student[0] == student_id:
            return student

    raise StudentNotFoundError("Student not found!")


def update_student():
    """Update an existing student's details."""

    student_id = input("Enter Student ID: ").strip()

    students = read_records(FILE)

    try:
        student = next(
            (record for record in students if record[0] == student_id),
            None,
        )

        if student is None:
            raise StudentNotFoundError("Student not found!")

        new_name = input("Enter new name: ").strip()
        new_course = input("Enter new course: ").strip()

        if new_name:
            student[1] = new_name

        if new_course:
            student[2] = new_course

        write_records(FILE, students)

        print("Student updated successfully!")

    except StudentNotFoundError as error:
        print(error)


def delete_student():
    """Delete a student record."""

    student_id = input("Enter Student ID: ").strip()

    students = read_records(FILE)
    print(students)

    try:
        search_student(student_id)
        #print(students)

        students = [
            student for student in students
            if student[0] != student_id
        ]

        write_records(FILE, students)

        print("Student deleted successfully!")

    except StudentNotFoundError as error:
        print(error)