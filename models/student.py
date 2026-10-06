class Student:

    def __init__(
        self,
        student_id,
        name,
        student_class,
        year,
        department,
        email
    ):
        self.student_id = str(student_id)
        self.name = str(name)
        self.student_class = str(student_class)
        self.year = int(year)
        self.department = str(department)
        self.email = str(email)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "class": self.student_class,
            "year": self.year,
            "department": self.department,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["class"],
            data["year"],
            data["department"],
            data.get("email", "")
        )

    def __str__(self):
        return f"{self.student_id} - {self.name}"
