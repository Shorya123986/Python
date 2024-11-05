import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions organized by category
questions = {
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
            "answer": "A",
        },
        {
            "question": "What is capital of Shimla?",
            "options": ["A) Manali", "B) Dharamshala", "C) Shimla", "D) Solan"],
            "answer": "C",
        },
    ],
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) O2", "B) H2O", "C) CO2", "D) NaCl"],
            "answer": "B",
        },
        {
            "question": "What is the speed of light?",
            "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
            "answer": "A",
        },
    ],
    "Math": [
        {
            "question": "What is the square root of 64?",
            "options": ["A) 6", "B) 7", "C) 8", "D) 9"],
            "answer": "C",
        },
        {
            "question": "What is 7 times 8?",
            "options": ["A) 54", "B) 56", "C) 58", "D) 60"],
            "answer": "B",
        },
    ],
}

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Generator")
        self.score = 0
        self.questions = []
        self.question_index = 0

        self.category_label = tk.Label(master, text="Select a category:")
        self.category_label.pack()

        self.category_var = tk.StringVar(value=list(questions.keys())[0])
        self.category_menu = tk.OptionMenu(master, self.category_var, *questions.keys())
        self.category_menu.pack()

        self.start_button = tk.Button(master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

        self.question_label = tk.Label(master, text="", wraplength=400)
        self.question_label.pack()

        self.options_var = tk.StringVar(value="")
        self.option_buttons = []

        for i in range(4):
            button = tk.Radiobutton(master, text="", variable=self.options_var, value="", command=self.check_answer)
            button.pack(anchor='w')
            self.option_buttons.append(button)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack()
        self.next_button.config(state=tk.DISABLED)

    def start_quiz(self):
        self.score = 0
        self.question_index = 0
        selected_category = self.category_var.get()
        self.questions = questions[selected_category]
        random.shuffle(self.questions)
        self.show_question()

    def show_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option, value=option[0])  # Set value to the answer option
                self.option_buttons[i].select() if i == 0 else self.option_buttons[i].deselect()
            self.result_label.config(text="")
            self.next_button.config(state=tk.DISABLED)
        else:
            self.end_quiz()

    def check_answer(self):
        selected_option = self.options_var.get()
        correct_answer = self.questions[self.question_index]["answer"]
        if selected_option == correct_answer:
            self.result_label.config(text="Correct!")
            self.score += 1
        else:
            self.result_label.config(text=f"Wrong! The correct answer was {correct_answer}.")
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.question_index += 1
        self.show_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(self.questions)}")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
