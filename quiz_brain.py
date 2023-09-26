class Quiz_Brain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_q(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"{self.question_number}:{current_question.question} (True/False)?? ")
        self.check_answer(answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print(f"You're right correct answer is {correct_answer}")
            self.score += 1
        else:
            print(f" correct answer is {correct_answer}")

        print(f"current score is {self.question_number}/ {self.score}")
    