from .rule_engine import RuleEngine


class InferenceEngine:

    def __init__(self):
        self.rule_engine = RuleEngine()

    def infer(self, attendance):

        return self.rule_engine.evaluate(
            attendance
        )
