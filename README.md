# Student Course Management CLI

A simple Python command-line application for managing students and course enrollments.

## Features

- Add new students with ID, name, and GPA
- Add new courses with ID, name, and maximum quota
- View all students or courses
- Enroll a student in a course
- Prevent enrolling when the course is full
- Prevent duplicate enrollments

## Files

- `main.py` - Application entry point and menu loop
- `student.py` - `Student` class definition
- `course.py` - `Course` class definition and enrollment logic
- `service.py` - Utility functions for displaying items and finding entries by ID

## Requirements

- Python 3.x

## Usage

1. Open a terminal in the project folder.
2. Run the app with:

```bash
python main.py
```

3. Use the menu options:

- `1` to add a new student
- `2` to add a new course
- `3` to view students or courses
- `4` to enroll a student in a course
- `5` to exit

## Notes

- Add at least one student and one course before enrolling.
- The app checks if a course is full before enrollment.
- The app also checks for duplicate enrollment attempts.

## Future Enhancements

- Add the ability to remove students or courses.
- Show course enrollment counts and available seats.
- Save data to a file so records persist between runs.
- Add search by student or course ID.

## Example

```text
Welcome to Student Course Management System
---------------------------------------------
1. Add New Student
2. Add New Course
3. View
4. Enroll
5. Exit

Enter your choice: 1
Enter student ID: S001
Enter student name: Alice
Enter student gpa: 3.7
Student Alice was added successfully !!
```
