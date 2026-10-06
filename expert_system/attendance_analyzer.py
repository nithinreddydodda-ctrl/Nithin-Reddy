from .inference_engine import InferenceEngine


class AttendanceAnalyzer:

    def __init__(self, attendance_service):
        self.attendance_service = attendance_service
        self.inference_engine = InferenceEngine()

    def analyze(self, student_id):

        summary = self.attendance_service.get_attendance_summary(
            student_id
        )

        percentage = summary["attendance_percentage"]

        result = self.inference_engine.infer(
            percentage
        )

        return {
            **summary,
            **result
        }
