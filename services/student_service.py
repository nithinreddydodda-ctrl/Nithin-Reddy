import json
import os

from models.student import Student


class StudentService:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_students(self):

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
                Student.from_dict(item)
                for item in data
            ]

        except (json.JSONDecodeError, KeyError):
            return []

    def save_students(self, students):

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
                    student.to_dict()
                    for student in students
                ],
                file,
                indent=4
            )

    def get_all_students(self):
        return self.load_students()

    def find_student(self, student_id):

        students = self.load_students()

        for student in students:

            if student.student_id == student_id:
                return student

        return None

    def add_student(self, student):

        students = self.load_students()

        if self.find_student(student.student_id):
            return False

        students.append(student)

        self.save_students(students)

        return True

    def update_student(
        self,
        student_id,
        **data
    ):

        students = self.load_students()

        for student in students:

            if student.student_id == student_id:

                if "name" in data:
                    student.name = data["name"]

                if "class" in data:
                    student.student_class = data["class"]

                if "year" in data:
                    student.year = int(data["year"])

                if "department" in data:
                    student.department = data["department"]

                if "email" in data:
                    student.email = data["email"]

                self.save_students(students)

                return True

        return False

    def delete_student(self, student_id):

        students = self.load_students()

        updated = [
            student
            for student in students
            if student.student_id != student_id
        ]

        if len(updated) == len(students):
            return False

        self.save_students(updated)

        return True

    def search_students(self, keyword):

        keyword = keyword.lower()

        students = self.load_students()

        return [
            student
            for student in students
            if keyword in student.student_id.lower()
            or keyword in student.name.lower()
        ]
