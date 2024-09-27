import tkinter as tk
from tkinter import messagebox
import random

class MathGame:
    def __init__(self, root):
        # Initialize the game window
        self.root = root
        self.root.title("Math Game")
        
        # Game state variables
        self.level = 1
        self.score = 0
        self.high_score = 0
        self.correct_answers = 0
        
        # Initialize the GUI components
        self.create_widgets()
        self.update_expression()
    
    def create_widgets(self):
        # Instruction label
        self.label_instruction = tk.Label(self.root, text="Solve the expression:")
        self.label_instruction.pack(pady=10)
        
        # Label to display the math expression
        self.label_expression = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.label_expression.pack(pady=10)
        
        # Entry box for user input
        self.entry_answer = tk.Entry(self.root, font=("Helvetica", 24))
        self.entry_answer.pack(pady=10)
        
        # Button to check the user's answer
        self.button_check = tk.Button(self.root, text="Check Answer", command=self.check_answer)
        self.button_check.pack(pady=10)
        
        # Button to move to the next level
        self.button_next = tk.Button(self.root, text="Next", state=tk.DISABLED, command=self.next_level)
        self.button_next.pack(pady=10)
        
        # Label to display the current score
        self.label_score = tk.Label(self.root, text=f"Score: {self.score}")
        self.label_score.pack(pady=10)
        
        # Label to display the high score
        self.label_high_score = tk.Label(self.root, text=f"High Score: {self.high_score}")
        self.label_high_score.pack(pady=10)
        
        # Label to display the correct answers needed to level up
        self.label_progress = tk.Label(self.root, text=f"Correct Answers to Level Up: {2 - self.correct_answers}")
        self.label_progress.pack(pady=10)
        
        # Button to restart the game
        self.button_restart = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.button_restart.pack(pady=10)
        
        # Button to reset high score
        self.button_reset_high_score = tk.Button(self.root, text="Reset High Score", command=self.reset_high_score)
        self.button_reset_high_score.pack(pady=10)
    
    def get_random_number(self, min_value, max_value):
        # Generate a random number between min_value and max_value
        return random.randint(min_value, max_value)
    
    def generate_level1_expression(self):
        # Generate a simple addition or subtraction expression for level 1
        number1 = self.get_random_number(10, 100)
        number2 = self.get_random_number(10, number1)
        operator1 = random.choice(["+", "-"])
        expression = f"{number1} {operator1} {number2}"
        answer = eval(expression)
        return {"number1": number1, "operator1": operator1, "number2": number2, "answer": answer}
    
    def generate_level2_expression(self):
        # Generate a more complex expression with two operations for level 2
        number1 = self.get_random_number(10, 100)
        number2 = self.get_random_number(2, number1)
        number3 = self.get_random_number(2, number2)
        operator1 = random.choice(["+", "-"])
        operator2 = "-" if operator1 == "+" else "+"
        expression = f"{number1} {operator1} {number2} {operator2} {number3}"
        answer = eval(expression)
        return {"number1": number1, "operator1": operator1, "number2": number2, "operator2": operator2, "number3": number3, "answer": answer}
    
    def generate_level3_expression(self):
        # Generate a multiplication expression for level 3
        number1 = self.get_random_number(10, 100)
        number2 = self.get_random_number(2, 10)
        operator1 = "*"
        expression = f"{number1} {operator1} {number2}"
        answer = number1 * number2
        return {"number1": number1, "operator1": operator1, "number2": number2, "answer": answer}
    
    def generate_level4_expression(self):
        # Generate a division expression for level 4
        number2 = self.get_random_number(2, 10)
        multiples = [i for i in range(number2, 101) if i % number2 == 0]
        number1 = random.choice(multiples)
        operator1 = "/"
        expression = f"{number1} {operator1} {number2}"
        answer = round(number1 / number2, 2)  # Now the answer is a float rounded to 2 decimal places
        return {"number1": number1, "operator1": operator1, "number2": number2, "answer": answer}
    
    def generate_level5_expression(self):
        # Generate a complex expression combining multiple operations for level 5
        number3 = self.get_random_number(2, 10)
        operator1 = random.choice(["+", "-"])
        operator2 = random.choice(["*", "/"])
    
        if operator2 == "/":
            multiples = [i for i in range(number3, 101) if i % number3 == 0]
            number2 = random.choice(multiples)
            number1 = self.get_random_number(number2, 100)
        else:
            number2 = self.get_random_number(2, 100)
            number1 = self.get_random_number(number2 * number3, 1000)
    
        expression = f"{number1} {operator1} {number2} {operator2} {number3}"
        answer = eval(expression)
        return {"number1": number1, "operator1": operator1, "number2": number2, "operator2": operator2, "number3": number3, "answer": answer}
    
    def get_expression(self):
        # Select and generate the appropriate expression based on the current level
        if self.level == 1:
            return self.generate_level1_expression()
        elif self.level == 2:
            return self.generate_level2_expression()
        elif self.level == 3:
            return self.generate_level3_expression()
        elif self.level == 4:
            return self.generate_level4_expression()
        elif self.level == 5:
            return self.generate_level5_expression()
    
    def update_expression(self):
        # Update the displayed math expression based on the current level
        self.expr = self.get_expression()
        if self.level in [1, 3, 4]:
            expression_str = f"{self.expr['number1']} {self.expr['operator1']} {self.expr['number2']}"
        else:
            expression_str = f"{self.expr['number1']} {self.expr['operator1']} {self.expr['number2']} {self.expr['operator2']} {self.expr['number3']}"
        self.label_expression.config(text=expression_str)
        self.entry_answer.delete(0, tk.END)
        self.button_next.config(state=tk.DISABLED)
        self.button_check.config(state=tk.NORMAL)
    
    def check_answer(self):
        # Check if the user's answer is correct
        try:
            user_answer = float(self.entry_answer.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return
        
        if user_answer == self.expr['answer']:
            # If the answer is correct
            messagebox.showinfo("Correct!", "🎉 Correct!")
            self.score += 1
            self.correct_answers += 1
            if self.score > self.high_score:
                self.high_score = self.score
            if self.correct_answers >= 2:
                # Advance to the next level
                self.level += 1
                self.correct_answers = 0
                messagebox.showinfo("Level Up!", f"Proceeding to level {self.level}.")
                self.update_expression()
            self.button_next.config(state=tk.NORMAL)
        else:
            # If the answer is incorrect
            messagebox.showerror("Wrong!", f"😞 Wrong! The correct answer was {self.expr['answer']}.")
        
        # Update score and high score displays
        self.label_score.config(text=f"Score: {self.score}")
        self.label_high_score.config(text=f"High Score: {self.high_score}")
        self.label_progress.config(text=f"Correct Answers to Level Up: {2 - self.correct_answers}")
        self.button_check.config(state=tk.DISABLED)
    
    def next_level(self):
        # Move to the next level
        self.update_expression()
    
    def restart_game(self):
        # Restart the game, resetting level and score
        self.level = 1
        self.score = 0
        self.correct_answers = 0
        self.update_expression()
        self.label_score.config(text=f"Score: {self.score}")
        self.label_high_score.config(text=f"High Score: {self.high_score}")
        self.label_progress.config(text=f"Correct Answers to Level Up: {2 - self.correct_answers}")
        self.button_next.config(state=tk.DISABLED)
        self.button_check.config(state=tk.NORMAL)
    
    def reset_high_score(self):
        # Reset the high score to 0
        if messagebox.askyesno("Reset High Score", "Are you sure you want to reset the high score?"):
            self.high_score = 0
            self.label_high_score.config(text=f"High Score: {self.high_score}")

if __name__ == "__main__":
    # Create the main window and run the game
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
