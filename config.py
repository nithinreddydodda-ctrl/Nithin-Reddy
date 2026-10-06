import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

STUDENTS_FILE = os.path.join(
    DATA_DIR,
    "students.json"
)

ATTENDANCE_FILE = os.path.join(
    DATA_DIR,
    "attendance.json"
)

RULES_FILE = os.path.join(
    DATA_DIR,
    "rules.json"
)

ATTENDANCE_THRESHOLD = 75
SHORT_ATTENDANCE_THRESHOLD = 60
