class Student:
    def __init__(self,stuID,stuName,stuGpa):
        self.id = stuID
        self.name = stuName
        self.gpa = stuGpa

    def getAll(self):
        print(f"ID:{self.id}  Name: {self.name} GPA: {self.gpa}")