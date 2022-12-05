from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for text in question_data :
    data = text["text"]
    answer = text["answer"]
    # print(data)
    # print(answer)
    question_bank.append(Question(data, answer))
    # print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_question() :
    quiz.next_question()

print("\nYou complete the quiz ")
print(f"You final score is {quiz.score}/{len(question_bank)}")
