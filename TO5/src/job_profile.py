class JobDescription:
    def __init__(self,job_id,company,role,location="Remote",minimum_score=0.0,
    required_skills=None,is_active=True):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = float(minimum_score)
        self.required_skills = [] if required_skills is None else list(required_skills)
        self.is_active = is_active
    def __str__(self):
        skills_text = (", ".join(self.required_skills)if self.required_skills else "Not Specified")
        status = "Active" if self.is_active else "Closed"
        return(
            f"Job Id: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}\n"
            f"Location: {self.location}\n"
            f"Minimum Score: {self.minimum_score: .1f}\n"
            f"Required skills: {skills_text}\n"
            f"Status: {status}"
        )
job = JobDescription(
    job_id=101,
    company="Kodnest",
    role="Python Developer"
)
print(job)

