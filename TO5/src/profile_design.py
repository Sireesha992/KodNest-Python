class StudentProfile:
    def __init__(self,student_id,name,course,score=0.0,skills=None,is_placed=False):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = float(score)
        self.skills = [] if skills is None else list(skills)
        self.is_placed = is_placed
    def __str__(self):
        skills_text = (", ".join(self.skills) if self.skills else "Not Added")
        placement_status = ("Placed" if self.is_placed else "Not placed")

        return (
            f"Student Id: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.2f}\n"
            f"Placement Status: {placement_status}"
        )
student = StudentProfile("101","Siree","Python","85.5",["python","SQL","Git"],True)
print(student)
