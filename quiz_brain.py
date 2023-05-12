import html


class QuizBrain:
    """Class QuizBrain
    # Instance
    question_list, question_number, score, question_current
    Method:
    still_has_question, check_answer, nex_question
    """
    def __init__(self, question_list):
        # instance
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        self.question_current = None

    # Method to check if is still question left
    def still_has_question(self):
        """
        Method to check if are still question left
        return:
        has_question -> bool
        """
        has_question = False
        len_question = len(self.question_list)
        if self.question_number < len_question:
            has_question = True

        return has_question

    # Method to check if the answer are correct
    def check_answer(self, user_answ):
        """
        Method to check if the answer are correct
        accept:
        user_answ -> bool ( True / False )
        """
        answer_correct = self.question_current.answer
        if user_answ.lower() == answer_correct.lower():
            # print("Your answer has correct\n")
            self.score += 1
            return True
        else:
            # print("Sorry your answer is not correct")
            # print(f"The correct answer was {self.question_list[self.question_number].answer}\n")
            return False

    # Method to show next question
    def nex_question(self):
        """
        Method to show next question
        """
        self.question_current = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.question_current.text)
        return f"Qn.{self.question_number} : {q_text}"

        # user_answer = input(f"Question number {self.question_number} : {question_current.text} (True/False?): ")
        # self.check_answer(user_answer, question_current.answer)
