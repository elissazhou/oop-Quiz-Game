from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quizBrain = QuizBrain(question_bank)

print(quizBrain.question_list)

while quizBrain.still_has_questions():
    quizBrain.next_question()
print("Congratulations! You've complete all the questions!")
print(f"Your final score is: {quizBrain.score}/{quizBrain.question_number}")