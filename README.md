# Student Course Management CLI

A simple Python command-line application for managing students and course enrollments.

## Features

- Add new students with ID, name, and GPA
- Add new courses with ID, name, and maximum quota
- View all students or courses (prints a friendly message when lists are empty)
- Enroll a student in a course
- Prevent enrolling when the course is full
- Prevent duplicate enrollments
- Search for students or courses by ID
- Delete a student or a course

## Files

- `main.py` - Application entry point and menu loop (supports add, view, enroll, search, delete)
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
- `5` to search for a student or course by ID
- `6` to delete a student or a course
- `7` to exit

## Notes

- Add at least one student and one course before enrolling.
- The app checks if a course is full before enrollment and prevents duplicates.
- Viewing lists prints a friendly message when there are no students or courses.
- The search option (`5`) looks up an entry by ID and prints details if found.
- The delete option (`6`) removes the selected student or course from memory for the current run.
- Data is not persisted to disk; all records are lost when the program exits.

## Future Enhancements

- Add persistent storage (save/load from JSON or CSV).
- Add update/edit operations for students and courses.
- Add validation and better input handling (ID format, numeric ranges).
- Add listing filtered by course or student, and exporting reports.

## Example

```text
Welcome to Student Course Management System
---------------------------------------------
1. Add New Student
2. Add New Course
3. View
4. Enroll
5. Search
6. Delete
7. Exit

Enter your choice: 1
Enter student ID: S001
Enter student name: Alice
Enter student gpa: 3.7
Student Alice was added successfully !!
```
