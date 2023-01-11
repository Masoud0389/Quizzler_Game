from tkinter import *
from data import question_data
from quize_brain import QuizBrain
import random as rn
import html
THEME_COLOR = "#375362"
num = None
red_timer = False


class UI(Tk):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.title("Quizzler")
        self.config(width=300, height=800, padx=50, pady=50, bg=THEME_COLOR)
        self.canvas = Canvas(width=400, height=300, bg="white")
        self.question = self.canvas.create_text(200, 150, width=300, text="hello", font=("Times New Roman", 22, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(width=100, height=97, image=true_image, highlightthickness=0, command=self.button_true)
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(width=100, height=97, image=false_image, highlightthickness=0, command=self.button_false)
        self.false_button.grid(column=1, row=2)
        self.score_label = Label(text="Score : 0/10", bg=THEME_COLOR, font=("Times New Roman", 20, "normal"))
        self.score_label.grid(column=1, row=0)
        self.red_timer = self.after(0, func=self.make_red)
        self.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.after_cancel(self.red_timer)
        global num
        num = rn.randint(0, len(question_data)-1)
        question = html.unescape(question_data[num]["question"])
        self.canvas.itemconfig(self.question, text=f"{question}")
        correct_answer = question_data[num]["correct_answer"]
        print(correct_answer)
        print(question_data[num]["category"])
    def button_true(self):
        global red_timer
        correct_answer = question_data[num]["correct_answer"]
        question_data.remove(question_data[num])
        if correct_answer == "True":
            self.next_question()
            self.score += 1
            self.update_score()
        else:
            red_timer = self.after(1000, func=self.make_red)
            self.canvas.config(bg="red")
    def button_false(self):
        global red_timer
        correct_answer = question_data[num]["correct_answer"]
        question_data.remove(question_data[num])
        if correct_answer == "False":
            self.next_question()
            self.score += 1
            self.update_score()

        else:
            red_timer = self.after(1000, func=self.make_red)
            self.canvas.config(bg="red")

    def make_red(self):
        self.next_question()

    def update_score(self):
        self.score_label.config(text=f"Score : {self.score}/10")

