# Student Training Management System

A menu-driven Python application for managing student records, attendance, subject marks, and generated performance reports. Data is stored locally in pipe-separated text files.

## Features

- Register, view, search, update, and delete students
- Mark daily attendance with duplicate protection for the same student and date
- Enter and view subject marks
- Calculate student averages and assign grades
- Calculate attendance percentages
- Generate and save individual student reports
- Handle missing records, invalid marks, and unknown student IDs

## Requirements

- Python 3.8 or newer
- No third-party Python packages

## Getting Started

1. Open a terminal in the project directory.
2. Run the application:

```bash
python main.py
```

3. Choose an option from the menu by entering a number from 1 to 11.

## Menu Options

| Option | Action |
| --- | --- |
| 1 | Register a student |
| 2 | View all students |
| 3 | Search for a student by ID |
| 4 | Update a student's name or course |
| 5 | Delete a student |
| 6 | Mark attendance for the current date |
| 7 | View attendance records |
| 8 | Enter marks for one or more subjects |
| 9 | View student marks |
| 10 | Generate and save a student report |
| 11 | Exit the application |

## Project Structure

```text
.
|-- main.py          # Application entry point and menu
|-- student.py       # Student record operations
|-- attendance.py    # Attendance entry and calculations
|-- marks.py         # Marks entry, validation, and grade calculation
|-- reports.py       # Performance report generation
|-- file_handler.py  # Shared text-file read and write operations
|-- exceptions.py    # Custom application exceptions
`-- data/
    |-- students.txt
    |-- attendance.txt
    |-- marks.txt
    `-- reports.txt
```

The `data` directory and missing data files are created automatically as needed.

## Data Format

Records use `|` as the field separator.

### Students

```text
student_id|name|course
```

### Attendance

```text
student_id|YYYY-MM-DD|P-or-A
```

- `P` represents present
- `A` represents absent

### Marks

```text
student_id|subject|marks
```

Marks must be between `0` and `100`.

### Reports

```text
student_id|name|course|average_marks|grade|attendance_percentage
```

## Grading Scale

| Average Marks | Grade |
| --- | --- |
| 90-100 | A |
| 75-89.99 | B |
| 50-74.99 | C |
| Below 50 | Fail |
