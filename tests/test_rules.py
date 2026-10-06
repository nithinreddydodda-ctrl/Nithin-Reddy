import unittest

from expert_system.rules import get_final_status


class TestRules(unittest.TestCase):

    def test_eligible(self):

        result = get_final_status(80)

        self.assertEqual(
            result["status"],
            "Eligible"
        )

    def test_short_attendance(self):

        result = get_final_status(65)

        self.assertEqual(
            result["status"],
            "Short Attendance"
        )

    def test_critical_attendance(self):

        result = get_final_status(50)

        self.assertEqual(
            result["status"],
            "Critical Attendance"
        )

    def test_boundary_75(self):

        result = get_final_status(75)

        self.assertEqual(
            result["status"],
            "Eligible"
        )

    def test_boundary_60(self):

        result = get_final_status(60)

        self.assertEqual(
            result["status"],
            "Short Attendance"
        )

    def test_invalid_attendance(self):

        result = get_final_status(110)

        self.assertEqual(
            result["status"],
            "Invalid"
        )


if __name__ == "__main__":
    unittest.main()
