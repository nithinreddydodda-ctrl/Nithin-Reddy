class Attendance:

    VALID_STATUSES = [
        "Present",
        "Absent"
    ]

    def __init__(
        self,
        student_id,
        date,
        status
    ):
        status = status.capitalize()

        if status not in self.VALID_STATUSES:
            raise ValueError(
                "Status must be Present or Absent."
            )

        self.student_id = str(student_id)
        self.date = str(date)
        self.status = status

    def is_present(self):
        return self.status == "Present"

    def is_absent(self):
        return self.status == "Absent"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "date": self.date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["date"],
            data["status"]
        )
