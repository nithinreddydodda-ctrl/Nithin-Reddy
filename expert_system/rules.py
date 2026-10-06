def rule_eligible(attendance):

    if 75 <= attendance <= 100:
        return {
            "status": "Eligible",
            "message": "Student has satisfactory attendance.",
            "recommendation":
                "Student is eligible for regular academic activities.",
            "alert": False
        }

    return None


def rule_short_attendance(attendance):

    if 60 <= attendance < 75:
        return {
            "status": "Short Attendance",
            "message": "Student has short attendance.",
            "recommendation":
                "Student should attend more classes.",
            "alert": True
        }

    return None


def rule_critical_attendance(attendance):

    if 0 <= attendance < 60:
        return {
            "status": "Critical Attendance",
            "message":
                "Student has critically low attendance.",
            "recommendation":
                "Immediate attendance improvement is required.",
            "alert": True
        }

    return None
