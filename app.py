import streamlit as st
from engine import QuestionEngine
from model import CareerModel

qe = QuestionEngine("questions.json")
cm = CareerModel()
cm.train("train.csv")


if "qid" not in st.session_state:
    st.session_state.qid = 1
    st.session_state.answers = []

q = qe.get_question_by_id(st.session_state.qid)

st.title("AI Career Guidance")


if q and len(st.session_state.answers) < 100:

    st.write(q["question"])

    if st.button(f"A. {q['options']['A']}"):
        st.session_state.answers.append(q["weights"]["A"])
        st.session_state.qid = q["next_question_map"]["A"]

    if st.button(f"B. {q['options']['B']}"):
        st.session_state.answers.append(q["weights"]["B"])
        st.session_state.qid = q["next_question_map"]["B"]

    if st.button(f"C. {q['options']['C']}"):
        st.session_state.answers.append(q["weights"]["C"])
        st.session_state.qid = q["next_question_map"]["C"]

    if st.button(f"D. {q['options']['D']}"):
        st.session_state.answers.append(q["weights"]["D"])
        st.session_state.qid = q["next_question_map"]["D"]


else:
    while len(st.session_state.answers) < 100:
        st.session_state.answers.append(2)

    rf, knn = cm.predict(st.session_state.answers)

    if rf[1] > knn[1]:
        career, conf = rf
    else:
        career, conf = knn

    st.write("Career:", career)
    st.write("Confidence:", conf)
