import json
import os

from models.attendance import Attendance


class AttendanceService:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_attendance(self):

        if not os.path.exists(self.file_path):
            return []

        try:
            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            return [
                Attendance.from_dict(item)
                for item in data
            ]

        except (json.JSONDecodeError, KeyError):
            return []

    def save_attendance(self, records):

        directory = os.path.dirname(
            self.file_path
        )

        if directory:
            os.makedirs(
                directory,
                exist_ok=True
            )

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [
                    record.to_dict()
                    for record in records
                ],
                file,
                indent=4
            )

    def get_student_attendance(self, student_id):

        records = self.load_attendance()

        return [
            record
            for record in records
            if record.student_id == student_id
        ]

    def add_attendance(
        self,
        student_id,
        date,
        status
    ):

        records = self.load_attendance()

        for record in records:

            if (
                record.student_id == student_id
                and record.date == date
            ):
                return False

        try:

            record = Attendance(
                student_id,
                date,
                status
            )

        except ValueError:
            return False

        records.append(record)

        self.save_attendance(records)

        return True

    def update_attendance(
        self,
        student_id,
        date,
        status
    ):

        records = self.load_attendance()

        for record in records:

            if (
                record.student_id == student_id
                and record.date == date
            ):

                try:
                    status = status.capitalize()

                    if status not in (
                        "Present",
                        "Absent"
                    ):
                        return False

                    record.status = status

                except ValueError:
                    return False

                self.save_attendance(records)

                return True

        return False

    def delete_attendance(
        self,
        student_id,
        date
    ):

        records = self.load_attendance()

        updated = [
            record
            for record in records
            if not (
                record.student_id == student_id
                and record.date == date
            )
        ]

        if len(updated) == len(records):
            return False

        self.save_attendance(updated)

        return True

    def count_present_days(self, student_id):

        records = self.get_student_attendance(
            student_id
        )

        return sum(
            record.is_present()
            for record in records
        )

    def count_absent_days(self, student_id):

        records = self.get_student_attendance(
            student_id
        )

        return sum(
            record.is_absent()
            for record in records
        )

    def count_total_days(self, student_id):

        return len(
            self.get_student_attendance(
                student_id
            )
        )

    def calculate_percentage(self, student_id):

        total = self.count_total_days(
            student_id
        )

        present = self.count_present_days(
            student_id
        )

        if total == 0:
            return 0.0

        return round(
            (present / total) * 100,
            2
        )

    def get_attendance_summary(self, student_id):

        return {
            "student_id": student_id,
            "present_days":
                self.count_present_days(student_id),
            "absent_days":
                self.count_absent_days(student_id),
            "total_days":
                self.count_total_days(student_id),
            "attendance_percentage":
                self.calculate_percentage(student_id)
        }
