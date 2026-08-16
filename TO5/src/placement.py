class StudentProfile:
    def __init__(self,student_id,name,course):
        self.student_id = student_id
        self.name = name
        self.course = course
    def __str__(self):
        return f"{self.student_id}-{self.name}-{self.course}"
class PlacementManager:
    def __init__(self):
        self.student_profiles=[]
    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)
    def display_student_profiles(self):
        if len(self.student_profiles)==0:
            print("No student profiles avialable")
        else:
            print("STUDENT PROFILES")
            for student in self.student_profiles:
                print(student)
manager = PlacementManager()
n = int(input())
for _ in range(n):
    student_id = int(input())
    name = input()
    course = input()
    student = StudentProfile(student_id,name,course)
    manager.add_student_profile(student)
manager.display_student_profiles()
