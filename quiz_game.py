import tkinter as tk
from tkinter import messagebox


quiz_data = [
    {"question": "What is the name of the holy book of Islam?", "answer": "Quran"},
    {"question": "Who is considered the last prophet in Islam?", "answer": "Prophet Muhammad(S.A.W)"},
    {"question": "What is the name of the first pillar of Islam?", "answer": "Shahada (Faith)"},
    {"question": "During which month do Muslims fast from dawn until sunset?", "answer": "Ramadan"},
    {"question": "In which city is the Kaaba located?", "answer": "Makkah"}
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz Game")
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 14))
        self.submit_button.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Helvetica", 14))
        self.next_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)
        
        self.show_question()
        
    def show_question(self):
        question = quiz_data[self.current_question]["question"]
        self.question_label.config(text=question)
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")
    
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = quiz_data[self.current_question]["answer"]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Incorrect! The correct answer is {correct_answer}.", fg="red")
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
    
    def next_question(self):
        self.current_question += 1
        if self.current_question < len(quiz_data):
            self.show_question()
            self.submit_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Quiz Complete", f"You've completed the quiz! Your score is {self.score}/{len(quiz_data)}")
            self.root.destroy()
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
    