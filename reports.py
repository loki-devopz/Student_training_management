from student import search_student
from marks import calculate_average, calculate_grade
from attendance import calculate_attendance
from file_handler import append_record
from exceptions import StudentNotFoundError

FILE = "reports.txt"


def generate_report():
    """Generate an individual student performance report."""

    student_id = input("Enter Student ID: ").strip()

    try:
        student = search_student(student_id)

        average = calculate_average(student_id)

        attendance = calculate_attendance(student_id)

        if average is None:
            print("No marks available for this student.")
            return

        grade = calculate_grade(average)

        print("\n========== STUDENT REPORT ==========")

        print("Student ID:", student[0])
        print("Student Name:", student[1])
        print("Course:", student[2])

        print("Average Marks:", round(average, 2))
        print("Grade:", grade)

        print(
            "Attendance Percentage:",
            round(attendance, 2), "%"
        )

        print("====================================")

        append_record(
            FILE,
            [
                student[0],
                student[1],
                student[2],
                round(average, 2),
                grade,
                round(attendance, 2)
            ]
        )

        print("Report saved successfully!")

    except StudentNotFoundError as error:
        print(error)

