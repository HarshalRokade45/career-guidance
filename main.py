from engine import QuestionEngine
from model import CareerModel

qe = QuestionEngine("questions.json")

cm = CareerModel()
cm.train("train.csv")   # your dataset

answers = []
asked = set()

print("\n----- AI CAREER GUIDANCE SYSTEM (CS/IT) ------\n")

current_qid = 1

while len(answers) < 100:
    answers.append(2)

    if current_qid > 100 or current_qid <= 0 or current_qid in asked:
        found = False
        for qid in range(1, 101):
            if qid not in asked:
                current_qid = qid
                found = True
                break
        if not found:
            break

    q = qe.get_question_by_id(current_qid)
    if q is None:
        break

    asked.add(current_qid)

    print(f"\nQ{q['id']}: {q['question']}")
    for opt, text in q["options"].items():
        print(f"{opt}. {text}")

    user_choice = input("Enter choice (A/B/C/D): ").upper().strip()

    weight = q["weights"][user_choice]
    answers.append(weight)

    next_qid = q["next_question_map"].get(user_choice, -1)

    if next_qid == -1 or next_qid in asked:
        found = False
        for qid in range(1, 101):
            if qid not in asked:
                current_qid = qid
                found = True
                break
        if not found:
            break
    else:
        current_qid = next_qid

print("\nTotal answers collected =", len(answers))

rf, knn = cm.predict(answers)

print("\n----- RESULTS -----")


print("\nRandom Forest Prediction:")
print("Career:", rf[0])
print("Confidence:", rf[1])

print("\nKNN Prediction:")
print("Career:", knn[0])
print("Confidence:", knn[1])