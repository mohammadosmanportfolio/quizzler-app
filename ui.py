from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMAGE_PATH = 'images/true.png'
FALSE_IMAGE_PATH = 'images/false.png'
FEEDBACK_FONT = ('Arial', 24, 'bold')

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score = 0
        self.score_text = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg='white', font=('Arial', 10, 'bold'))
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(bg='white', height=250, width=300)
        self.load_next_question()
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.true_photo = PhotoImage(file=TRUE_IMAGE_PATH)
        self.true_button = Button(bg=THEME_COLOR, image=self.true_photo, command=self.true_button_pressed)
        self.true_button.grid(column=0, row=2)
        
        self.false_photo = PhotoImage(file=FALSE_IMAGE_PATH)
        self.false_button = Button(bg=THEME_COLOR, image=self.false_photo, command=self.false_button_pressed)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop() 

    def load_next_question(self):
        if self.quiz_brain.still_has_questions():
            question = self.quiz_brain.next_question()
            self.canvas.delete('all')
            self.canvas.create_text(150, 125, text=question, 
                                    font=("Arial", 20, 'italic'),
                                    width=280)
        else:
            self.end_game_report()
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        
    def true_button_pressed(self):
        if self.quiz_brain.check_answer('true'):
            self.print_correct()
            self.increment_score()
        else:
            self.print_wrong()
        self.canvas.after(2000, func=self.load_next_question)


    def false_button_pressed(self):
        if self.quiz_brain.check_answer('false'):
            self.print_correct()
            self.increment_score()
        else:
            self.print_wrong()
        self.canvas.after(2000, func=self.load_next_question)

    def print_correct(self):
        self.canvas.delete('all')
        self.canvas.create_text(150, 125, text="Correct! " + "\U0001F44D", fill='green', font=FEEDBACK_FONT)

    def print_wrong(self):
        self.canvas.delete('all')
        self.canvas.create_text(150, 125, text="Wrong " + "\U0001F44E", fill='red', font=FEEDBACK_FONT)

    def increment_score(self):
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")

    def end_game_report(self):
        self.canvas.delete('all')
        self.canvas.create_text(150, 125, text="That was the last question", font=('Arial', 20, 'italic'), width=200)
        self.canvas.after(3000, func=self.print_final_score_on_screen)


    def print_final_score_on_screen(self):
        self.canvas.delete('all')
        self.canvas.create_text(150, 125, text=f"You answered {self.score} questions correctly",
                                font=('Arial', 20, 'italic'),
                                width=280)
        self.canvas.after(3000, func=self.print_smiley_face)
        
    def print_smiley_face(self):
        self.canvas.delete('all')
        self.canvas.create_text(150, 125, text="\U0001F642", font=('Arial', 60))
        self.window.after(3000, func=self.window.destroy)

    # def enable_buttons(self):
    #     self.true_button.config(state='normal')
    #     self.false_button.config(state='normal')
    
    # def disable_buttons(self):
    #     self.true_button.config(state='disabled')
    #     self.false_button.config(state='disabled')