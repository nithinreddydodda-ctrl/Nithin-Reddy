from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

import os
import secrets

import config

from models.student import Student

from services.student_service import StudentService
from services.attendance_service import AttendanceService

from expert_system.attendance_analyzer import (
    AttendanceAnalyzer
)


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)


student_service = StudentService(
    config.STUDENTS_FILE
)

attendance_service = AttendanceService(
    config.ATTENDANCE_FILE
)

analyzer = AttendanceAnalyzer(
    attendance_service
)


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/")
def index():

    students = student_service.get_all_students()

    total_students = len(students)

    return render_template(
        "index.html",
        students=students,
        total_students=total_students
    )


# ============================================================
# STUDENTS
# ============================================================

@app.route("/students")
def students():

    all_students = student_service.get_all_students()

    return render_template(
        "students.html",
        students=all_students
    )


# ============================================================
# ADD STUDENT
# ============================================================

@app.route(
    "/students/add",
    methods=["GET", "POST"]
)
def add_student():

    if request.method == "POST":

        student_id = request.form["student_id"].strip()
        name = request.form["name"].strip()
        student_class = request.form["class"].strip()
        year = request.form["year"].strip()
        department = request.form["department"].strip()
        email = request.form["email"].strip()

        if student_service.find_student(student_id):

            flash(
                "Student ID already exists.",
                "danger"
            )

            return redirect(
                url_for("add_student")
            )

        try:

            student = Student(
                student_id,
                name,
                student_class,
                year,
                department,
                email
            )

            student_service.add_student(
                student
            )

            flash(
                "Student added successfully.",
                "success"
            )

            return redirect(
                url_for("students")
            )

        except ValueError:

            flash(
                "Invalid year.",
                "danger"
            )

    return render_template(
        "add_student.html"
    )


# ============================================================
# DELETE STUDENT
# ============================================================

@app.route(
    "/students/delete/<student_id>"
)
def delete_student(student_id):

    if student_service.delete_student(
        student_id
    ):

        flash(
            "Student deleted successfully.",
            "success"
        )

    else:

        flash(
            "Student not found.",
            "danger"
        )

    return redirect(
        url_for("students")
    )


# ============================================================
# ATTENDANCE
# ============================================================

@app.route("/attendance")
def attendance():

    students = student_service.get_all_students()

    return render_template(
        "attendance.html",
        students=students
    )


# ============================================================
# MARK ATTENDANCE
# ============================================================

@app.route(
    "/attendance/add",
    methods=["POST"]
)
def add_attendance():

    student_id = request.form["student_id"]
    date = request.form["date"]
    status = request.form["status"]

    result = attendance_service.add_attendance(
        student_id,
        date,
        status
    )

    if result:

        flash(
            "Attendance marked successfully.",
            "success"
        )

    else:

        flash(
            "Attendance record already exists "
            "or the data is invalid.",
            "danger"
        )

    return redirect(
        url_for("attendance")
    )


# ============================================================
# REPORT
# ============================================================

@app.route(
    "/report/<student_id>"
)
def report(student_id):

    student = student_service.find_student(
        student_id
    )

    if not student:

        flash(
            "Student not found.",
            "danger"
        )

        return redirect(
            url_for("students")
        )

    result = analyzer.analyze(
        student_id
    )

    records = attendance_service.get_student_attendance(
        student_id
    )

    return render_template(
        "report.html",
        student=student,
        records=records,
        result=result
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
