from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
	question_text = x["text"]
	question_answer = x["answer"]
	new_question = Question(question_text, question_answer)
	question_bank.append(new_question)
	# question_bank.append(new_question) made "new_question" a listed Question obj element inside question_bank
	# print(question_bank[0].answer/ .text).... thus, every item inside the question_bank is a Question obj
	# This is connected to the current_question as it is question
	# That's why its called an object because it is one unit which has the same characteristics (attributes)

quiz = QuizBrain(question_bank)

while quiz.still_questions():
	quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")


