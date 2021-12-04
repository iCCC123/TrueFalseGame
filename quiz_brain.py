class QuizBrain:

	def __init__(self, qlist):
		self.question_num = 0
		self.score = 0
		self.question_list = qlist

	def still_questions(self):
		return self.question_num < len(self.question_list)
		# while the question number is greater than the number of items on question list

	def next_question(self):
		current_question = self.question_list[self.question_num]
		# "current_question" is a Question(class) object from "new_question" variable in "main.py"
		# we can now use the 'quiz' object of 'QuizBrain' class so we call the
		# 'quiz.next_question()' method in the 'while' loop where we set the current
		# 'question_list[question_number]' to the 'current_question', so 'current_question'
		# now contains the 'text' and 'answer' values of the current question.
		self.question_num += 1
		u_ans = input(f"Q.{self.question_num}: {current_question.text} (True/ False): ")
		self.check_answer(u_ans, current_question.answer)

	def check_answer(self, u_ans, correct_ans):
		if u_ans.lower() == correct_ans.lower():
			self.score += 1
			print("Correct")
		else:
			print("Wrong")
		print(f"The correct answer was: {correct_ans}.")
		print(f"Your current score is: {self.score}/{self.question_num}\n")



