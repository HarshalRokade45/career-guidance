import json

class QuestionEngine:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            self.questions = json.load(f)

    def get_question_by_id(self, qid):
        for q in self.questions:
            if q["id"] == qid:
                return q
        return None