class StudentProfile:
    def __init__(self,student_id,name,course):
        self.student_id = student_id
        self.name = name
        self.course = course
first_id = int(input())
first_name = input()
first_course = input()
second_id = int(input())
second_name = input()
second_course = input()
student1 = StudentProfile(first_id,first_name,first_course)
student2 = StudentProfile(second_id,second_name,second_course)
print(student1)
print(f"Student ID: {first_id}")
print(f"Name: {first_name}")
print(f"Course: {first_course}")
print(student2)
print(f"Student ID: {second_id}")
print(f"Name: {second_name}")
print(f"Course: {second_course}")