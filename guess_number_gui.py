import tkinter as tk
from tkinter import messagebox
import random

class GuessNumberGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("450x350")
        self.root.config(bg="#E8F5E9")

        self.number = random.randint(1, 100)
        self.attempts = 0

        title = tk.Label(root,
                         text="GUESS THE NUMBER",
                         font=("Arial", 18, "bold"),
                         bg="#E8F5E9",
                         fg="green")
        title.pack(pady=10)

        instruction = tk.Label(root,
                               text="Guess a number between 1 and 100",
                               font=("Arial", 12),
                               bg="#E8F5E9")
        instruction.pack()

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        tk.Button(root,
                  text="Check Guess",
                  font=("Arial", 12),
                  bg="blue",
                  fg="white",
                  command=self.check_guess).pack(pady=5)

        self.result = tk.Label(root,
                               text="",
                               font=("Arial", 13, "bold"),
                               bg="#E8F5E9")
        self.result.pack(pady=10)

        self.attempt_label = tk.Label(root,
                                      text="Attempts : 0",
                                      font=("Arial", 12),
                                      bg="#E8F5E9")
        self.attempt_label.pack()

        tk.Button(root,
                  text="New Game",
                  font=("Arial", 12),
                  bg="orange",
                  fg="white",
                  command=self.new_game).pack(pady=5)

        tk.Button(root,
                  text="Exit",
                  font=("Arial", 12),
                  bg="red",
                  fg="white",
                  command=root.quit).pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempt_label.config(text=f"Attempts : {self.attempts}")

        if guess < self.number:
            self.result.config(text="Too Low! Try Again.")

        elif guess > self.number:
            self.result.config(text="Too High! Try Again.")

        else:
            self.result.config(
                text=f"Congratulations! You guessed it in {self.attempts} attempts."
            )

    def new_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result.config(text="")
        self.attempt_label.config(text="Attempts : 0")


root = tk.Tk()
app = GuessNumberGame(root)
root.mainloop()