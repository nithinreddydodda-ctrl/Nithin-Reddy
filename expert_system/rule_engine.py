from .rules import (
    rule_eligible,
    rule_short_attendance,
    rule_critical_attendance
)


class RuleEngine:

    def evaluate(self, attendance):

        rules = [
            rule_eligible,
            rule_short_attendance,
            rule_critical_attendance
        ]

        for rule in rules:

            result = rule(attendance)

            if result is not None:
                return result

        return {
            "status": "Unknown",
            "message": "No rule matched.",
            "recommendation": "",
            "alert": True
        }
