import tkinter as tk

from quiz_master import QuizMaster

TRUE_IMG = "D:/python/100days/day34_intermediate+_quizz_app/images/true.png"
FALSE_IMG ="D:/python/100days/day34_intermediate+_quizz_app/images/false.png"

THEME_COLOR = "#375362"
LIGHT_GREEN = "#90EE90"
LIGHT_RED = "#EE9090"


class QuizInterface:

    def __init__(self, quiz_master:QuizMaster):
        self.quiz_master = quiz_master
        self.timer = None

        self.root = tk.Tk()
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)
        self.root.title("Qizzler")

        self.true_img = tk.PhotoImage(file=TRUE_IMG)
        self.false_img = tk.PhotoImage(file=FALSE_IMG)

        self.score_label = tk.Label(self.root, text=f"Score: 0", font=("Ariel",14, "bold"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.quiz_card = tk.Canvas(self.root, width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.quiz_card.create_text(
            150, 125, 
            width=280,
            text=self.quiz_master.get_question(), 
            font=("Ariel",20, "italic"),
            fill=THEME_COLOR, 
            justify="center"
            )
        self.quiz_card.grid(row=1, column=0, columnspan=2, pady=(20,50))

        self.button_true = tk.Button(self.root, image=self.true_img, highlightthickness=0, command=self.check_true)
        self.button_true.grid(row=2, column=1)
        self.button_false = tk.Button(self.root, image=self.false_img, highlightthickness=0, command=self.check_false)
        self.button_false.grid(row=2, column=0)

        self.root.mainloop()
        
    
    def check_true(self):
        if self.timer: return
        if self.quiz_master.check_answer(True):
            self.update_score()
            self.give_feedback(LIGHT_GREEN)
        else:
            self.give_feedback(LIGHT_RED)
            
        
    def check_false(self):
        if self.timer: return
        if self.quiz_master.check_answer(False):
            self.update_score()
            self.give_feedback(LIGHT_GREEN)
        else:
            self.give_feedback(LIGHT_RED)
            
            
    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz_master.score}")
        
    def give_feedback(self, color):
        self.quiz_card.config(bg=color)
        self.timer = self.root.after(1000, self.update_question)
        
        
    def update_question(self):
        self.timer = None
        self.quiz_card.config(bg="white")
        if self.quiz_master.next_question():
            self.quiz_card.itemconfig(self.question, text=self.quiz_master.get_question())
        else:
            self.button_true.config(command=lambda: None)
            self.button_false.config(command=lambda: None)
            self.quiz_card.itemconfig(self.question, text=f"You got \n{self.quiz_master.score} out of 10 \nanswers correct.")