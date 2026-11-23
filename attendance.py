from datetime import date
from file_handler import read_records, append_record
from student import search_student
from exceptions import StudentNotFoundError

FILE = "attendance.txt"

def mark_attendance():
    """Record student attendance."""

    student_id = input("Enter Student ID: ").strip()

    try:
        student = search_student(student_id)

        print("Student:", student[1])

        status = input("Enter attendance (P/A): ").strip().upper()

        if status not in ("P", "A"):
            print("Invalid attendance status!")
            return

        today = date.today().isoformat()

        records = read_records(FILE)

        if any(r[0] == student_id and r[1] == today
               for r in records):
            print("Attendance already marked today!")
            return

        append_record(FILE, [student_id, today, status])

        print("Attendance recorded successfully!")

    except StudentNotFoundError as error:
        print(error)


def view_attendance():
    """Display attendance records."""

    records = read_records(FILE)

    if not records:
        print("No attendance records found.")
        return

    print("\nID\tDate\t\tStatus")
    print("-" * 40)

    for record in records:
        print(
            f"{record[0]}\t{record[1]}\t{record[2]}"
        )


def calculate_attendance(student_id):
    """Calculate student attendance percentage."""

    records = read_records(FILE)

    student_records = [
        record for record in records
        if record[0] == student_id
    ]

    if not student_records:
        return 0

    present = sum(
        1 for record in student_records
        if record[2] == "P"
    )

    total = len(student_records)

    return (present / total) * 100