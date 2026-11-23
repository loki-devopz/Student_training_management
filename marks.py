from file_handler import read_records, append_record
from student import search_student
from exceptions import InvalidMarksError, StudentNotFoundError

FILE = "marks.txt"


def enter_marks():
    """Enter subject marks for a student."""

    student_id = input("Enter Student ID: ").strip()

    try:
        student = search_student(student_id)

        print("Student:", student[1])

        subject_count = int(
            input("Enter number of subjects: ")
        )

        if subject_count <= 0:
            print("Enter at least one subject.")
            return

        for i in range(1, subject_count + 1):

            subject = input(
                f"Enter Subject {i} Name: "
            ).strip()

            mark = float(
                input(f"Enter {subject} Marks: ")
            )

            validate_marks(mark)

            append_record(
                FILE,
                [student_id, subject, mark]
            )

        print("Marks recorded successfully!")

    except ValueError:
        print("Please enter valid numerical values.")

    except InvalidMarksError as error:
        print("Invalid marks:", error)

    except StudentNotFoundError as error:
        print(error)


def validate_marks(mark):
    """Validate marks between 0 and 100."""

    if not 0 <= mark <= 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    assert 0 <= mark <= 100


def calculate_average(student_id):
    """Calculate average marks of a student."""

    records = read_records(FILE)

    student_marks = [
        float(record[2])
        for record in records
        if record[0] == student_id
    ]

    if not student_marks:
        return None

    average = sum(student_marks) / len(student_marks)

    return average


def calculate_grade(average):
    """Assign grade based on average marks."""

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 50:
        return "C"

    else:
        return "Fail"


def view_marks():
    """Display all student marks."""

    records = read_records(FILE)

    if not records:
        print("No marks records found.")
        return

    print("\nID\tSubject\tMarks")
    print("-" * 40)

    for record in records:
        print(
            f"{record[0]}\t{record[1]}\t{record[2]}"
        )
