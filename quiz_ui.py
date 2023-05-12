from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMAGE = "./image/true.png"
FALSE_IMAGE = "./image/false.png"


# Class QuizUi
class QuizUi:
    """
    # Class QuizUi
    Method:
    get_question, check_true, check_false, get_feedback
    
    """
    def __init__(self, quiz_populate: QuizBrain):
        self.quiz = quiz_populate
        self.window = Tk()
        self.window.title("Quiz Game Ui")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(fg="white", font=("Arial", 15, "italic"))
        self.score_label.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_question = self.canvas.create_text(150, 125, width=200, fill="black", font=("Arial", 15, "italic"))

        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_answer_image = PhotoImage(file=TRUE_IMAGE)
        self.true_answer_button = Button(image=self.true_answer_image, highlightthickness=0, command=self.check_true)
        self.true_answer_button.grid(padx=20, pady=20, row=2, column=0)

        self.false_answer_image = PhotoImage(file=FALSE_IMAGE)
        self.false_answer_button = Button(image=self.false_answer_image, highlightthickness=0, command=self.check_false)
        self.false_answer_button.grid(padx=20, pady=20, row=2, column=1)

        self.get_question()

        self.window.mainloop()

    # Method to get question
    def get_question(self):
        """# Method to get question"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.nex_question()
            self.canvas.itemconfig(self.canvas_question, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_question, text="You've reached the end of the quiz.")
            self.true_answer_button.config(state="disabled")
            self.false_answer_button.config(state="disabled")
    
    # Method to get 'true_answer_button' click
    def check_true(self):
        """# Method to get 'true_answer_button' click"""
        is_right = self.quiz.check_answer("True")
        self.get_feedback(is_right)
    
    # Method to get 'false_answer_button' click
    def check_false(self):
        """# Method to get 'false_answer_button' click"""
        is_right = self.quiz.check_answer("False")
        self.get_feedback(is_right)
    
    # Method to give feedback from your answer
    def get_feedback(self, is_right):
        """# Method to give feedback from your answer
        accept:
        is_right -> bool ( True / False )
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
