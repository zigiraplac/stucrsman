from service import display
class Course:
    def __init__(self,courseID,courseName,maxstudent):
        self.id = courseID
        self.name = courseName
        self.students= []
        self.quota = maxstudent

    def enrollStudent(self,student):
        if len(self.students) < self.quota:
            if student in self.students:
                print(f"{student.name} is already enrolled in {self.name}")
                return
            self.students.append(student)
            print(f"{student.name} has been enrolled in {self.name}")
            if self.students:
                print("Enrolled Students:")
                display(self.students)
        else:
            print(f"Cannot enroll {student.name}, {self.name} is full")

    def getAll(self):
        print(f"ID:{self.id}  Name: {self.name} Max Student: {self.quota}")
        if self.students:
            print("Students Enrolled:")
            display(self.students)
        else:
            print("Students Enrolled: None")