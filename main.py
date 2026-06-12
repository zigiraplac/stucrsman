""" The Main Program lies here """
# Import classes: Student and Course
import student
import course
from service import display, findById
# Menu Function 
print("\nWelcome to Student Course Management System ")
print("---------------------------------------------\n")
def menu ():

    print("1. Add New Student")
    print("2. Add New Course")
    print("3. View ")
    print("4. Enroll ")
    print("5  Search")
    print("6  Delete ")
    print("7. Exit\n")

    option = int(input("Enter your choice: "))

    return option



# List of all Students
studentList = []
# List of all courses
courseList = []

# Print The Menu and the Option

# 0788628527
choice = menu()
while True:
    if choice == 1:
        code = input("Enter student ID: ")
        name = input("Enter student name: ")
        gpa = float(input("Enter student gpa: "))
        stu = student.Student(code,name,gpa)
        studentList.append(stu)
        print(f"Student {stu.name} was added successfully !!")
    elif choice == 2:
        code = input("Enter course ID: ")
        name = input("Enter course name: ")
        quota = int(input("Enter max student: "))
        crs = course.Course(code,name,quota)
        courseList.append(crs)
        print(f"Course {crs.name} was added successfully !!")
    elif choice == 3:
        print("1. View Students")
        print("2. View Courses")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            if studentList:
                print("All Students")
                display(studentList)
                print()
            else:
                print("No students available.")
                print()
        elif opt == 2:
            if courseList:
                print("All Courses")
                display(courseList)
                print()
            else:
                print("No courses available.")
                print()
    elif choice == 4:
        if not courseList:
            print("No courses available. Please add a course first.")
        elif not studentList:
            print("No students available. Please add a student first.")
        else:
            print("All Courses")
            display(courseList)

            course_id = input("Select course to enroll in: ")
            crs = findById(courseList,course_id)

            if crs:
                print("All Students")
                display(studentList)
                student_id = input("Select student to enroll: ")
                stu = findById(studentList,student_id)

                if stu:
                    crs.enrollStudent(stu)
                else:
                    print("Student not found.")
            else:
                print("Course not found")
    elif choice == 5:
        print("1. Search Student")
        print("2. Search Course")
        opt = int(input("Enter your choice: "))
        if opt == 1:
            
            search_id = input("Enter the ID of the student to search: ")
            found_student = findById(studentList, search_id)
            if found_student:
                print("Student found:")
                found_student.getAll()
            else:
                print("Student not found.")
        elif opt == 2:
            search_id = input("Enter the ID of the course to search: ")
            found_course = findById(courseList, search_id)
            if found_course:
                print("Course found:")
                found_course.getAll()
            else:
                print("Course not found.")
    elif choice == 6:
        # Implementation for deleting a student or course
             print("1. Delete Student")
             print("2. Delete Course")
             opt = int(input("Enter your choice: "))
             if opt == 1:
                    display(studentList)
                    del_id = input("Enter the ID of the student to delete: ")
                    item_to_delete = findById(studentList, del_id)
                    if item_to_delete:
                            studentList.remove(item_to_delete)
                            print(f"{item_to_delete.name} has been deleted successfully.")
                            
                    else:
                        print("Student not found.")
             elif opt == 2:
                 display(courseList)
                 del_id = input("Enter the ID of the course to delete: ")
                 item_to_delete = findById(courseList, del_id)
                 if item_to_delete:
                        courseList.remove(item_to_delete)
                        print(f"{item_to_delete.name} has been deleted successfully.")
                 else:
                    print("Course not found.")
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please select a valid option.")
    choice = menu()

