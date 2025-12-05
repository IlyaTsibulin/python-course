from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(text=i["text"], answer=i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.steel_has_questions():
    quiz.next_question()
