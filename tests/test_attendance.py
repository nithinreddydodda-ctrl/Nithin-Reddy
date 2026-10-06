import unittest

from models.attendance import Attendance


class TestAttendance(unittest.TestCase):

    def test_present(self):

        attendance = Attendance(
            "ST001",
            "2026-10-01",
            "Present"
        )

        self.assertTrue(
            attendance.is_present()
        )

        self.assertFalse(
            attendance.is_absent()
        )

    def test_absent(self):

        attendance = Attendance(
            "ST001",
            "2026-10-02",
            "Absent"
        )

        self.assertTrue(
            attendance.is_absent()
        )

    def test_invalid_status(self):

        with self.assertRaises(ValueError):

            Attendance(
                "ST001",
                "2026-10-01",
                "Holiday"
            )

    def test_to_dict(self):

        attendance = Attendance(
            "ST001",
            "2026-10-01",
            "Present"
        )

        data = attendance.to_dict()

        self.assertEqual(
            data["student_id"],
            "ST001"
        )

        self.assertEqual(
            data["status"],
            "Present"
        )


if __name__ == "__main__":
    unittest.main()
import unittest

from models.attendance import Attendance


class TestAttendance(unittest.TestCase):

    def test_present(self):

        attendance = Attendance(
            "ST001",
            "2026-10-01",
            "Present"
        )

        self.assertTrue(
            attendance.is_present()
        )

        self.assertFalse(
            attendance.is_absent()
        )

    def test_absent(self):

        attendance = Attendance(
            "ST001",
            "2026-10-02",
            "Absent"
        )

        self.assertTrue(
            attendance.is_absent()
        )

    def test_invalid_status(self):

        with self.assertRaises(ValueError):

            Attendance(
                "ST001",
                "2026-10-01",
                "Holiday"
            )

    def test_to_dict(self):

        attendance = Attendance(
            "ST001",
            "2026-10-01",
            "Present"
        )

        data = attendance.to_dict()

        self.assertEqual(
            data["student_id"],
            "ST001"
        )

        self.assertEqual(
            data["status"],
            "Present"
        )


if __name__ == "__main__":
    unittest.main()
