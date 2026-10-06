import unittest

from models.student import Student


class TestStudent(unittest.TestCase):

    def test_create_student(self):

        student = Student(
            "ST001",
            "Rahul Sharma",
            "BCA",
            1,
            "Computer Applications",
            "rahul@gmail.com"
        )

        self.assertEqual(
            student.student_id,
            "ST001"
        )

        self.assertEqual(
            student.name,
            "Rahul Sharma"
        )

    def test_to_dict(self):

        student = Student(
            "ST001",
            "Rahul Sharma",
            "BCA",
            1,
            "Computer Applications",
            "rahul@gmail.com"
        )

        data = student.to_dict()

        self.assertEqual(
            data["student_id"],
            "ST001"
        )

        self.assertEqual(
            data["class"],
            "BCA"
        )

    def test_from_dict(self):

        data = {
            "student_id": "ST002",
            "name": "Priya",
            "class": "BCA",
            "year": 2,
            "department": "Computer Applications",
            "email": "priya@gmail.com"
        }

        student = Student.from_dict(data)

        self.assertEqual(
            student.student_id,
            "ST002"
        )


if __name__ == "__main__":
    unittest.main()
