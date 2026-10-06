import json
import os


class Database:
    """
    Simple JSON database for the Student Attendance
    Expert System.
    """

    def __init__(self, data_dir="data"):
        self.data_dir = data_dir

        os.makedirs(self.data_dir, exist_ok=True)

        self.students_file = os.path.join(
            self.data_dir,
            "students.json"
        )

        self.attendance_file = os.path.join(
            self.data_dir,
            "attendance.json"
        )

        self.rules_file = os.path.join(
            self.data_dir,
            "rules.json"
        )

        self._create_files()


    # ==================================================
    # CREATE DATA FILES
    # ==================================================

    def _create_files(self):

        if not os.path.exists(self.students_file):
            self._write_json(
                self.students_file,
                []
            )

        if not os.path.exists(self.attendance_file):
            self._write_json(
                self.attendance_file,
                []
            )

        if not os.path.exists(self.rules_file):
            self._write_json(
                self.rules_file,
                []
            )


    # ==================================================
    # JSON READ / WRITE
    # ==================================================

    def _read_json(self, filename):

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                return data

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []


    def _write_json(self, filename, data):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )


    # ==================================================
    # STUDENTS
    # ==================================================

    def get_students(self):

        return self._read_json(
            self.students_file
        )


    def save_students(self, students):

        self._write_json(
            self.students_file,
            students
        )


    def add_student(self, student):

        students = self.get_students()

        students.append(student)

        self.save_students(students)

        return student


    def get_student(self, student_id):

        students = self.get_students()

        for student in students:

            if str(student.get("id")) == str(student_id):

                return student

        return None


    def update_student(
        self,
        student_id,
        updated_student
    ):

        students = self.get_students()

        for index, student in enumerate(students):

            if str(student.get("id")) == str(student_id):

                students[index] = updated_student

                self.save_students(students)

                return updated_student

        return None


    def delete_student(self, student_id):

        students = self.get_students()

        updated_students = [
            student
            for student in students
            if str(student.get("id")) != str(student_id)
        ]

        deleted = (
            len(updated_students)
            != len(students)
        )

        if deleted:

            self.save_students(updated_students)

        return deleted


    # ==================================================
    # ATTENDANCE
    # ==================================================

    def get_attendance(self):

        return self._read_json(
            self.attendance_file
        )


    def save_attendance(self, attendance):

        self._write_json(
            self.attendance_file,
            attendance
        )


    def add_attendance(self, record):

        attendance = self.get_attendance()

        attendance.append(record)

        self.save_attendance(attendance)

        return record


    def get_student_attendance(self, student_id):

        attendance = self.get_attendance()

        return [
            record
            for record in attendance
            if str(record.get("student_id"))
            == str(student_id)
        ]


    # ==================================================
    # RULES
    # ==================================================

    def get_rules(self):

        return self._read_json(
            self.rules_file
        )


    def save_rules(self, rules):

        self._write_json(
            self.rules_file,
            rules
        )