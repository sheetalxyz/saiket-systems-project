import tkinter as tk
from tkinter import messagebox
from collections import Counter
import os

file_path = os.path.join(os.path.dirname(__file__), "sample.txt")

class WordCountTool:

    def __init__(self, root):
        self.root = root
        self.root.title("Word Count Tool")
        self.root.geometry("700x550")
        self.root.config(bg="#F3E5F5")

        tk.Label(root,
                 text="Word Count Tool",
                 font=("Arial",18,"bold"),
                 bg="#F3E5F5",
                 fg="purple").pack(pady=10)

        tk.Button(root,
                  text="Analyze File",
                  bg="blue",
                  fg="white",
                  font=("Arial",12),
                  command=self.analyze).pack(pady=10)

        self.text = tk.Text(root, width=80, height=25)
        self.text.pack()

    def analyze(self):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = file.read()

            words = data.split()

            word_count = len(words)
            line_count = len(data.splitlines())
            char_count = len(data)

            frequency = Counter(word.lower().strip(".,!?") for word in words)

            self.text.delete(1.0, tk.END)

            self.text.insert(tk.END, "FILE ANALYSIS\n")
            self.text.insert(tk.END, "-"*40 + "\n")
            self.text.insert(tk.END, f"Total Lines : {line_count}\n")
            self.text.insert(tk.END, f"Total Words : {word_count}\n")
            self.text.insert(tk.END, f"Total Characters : {char_count}\n\n")

            self.text.insert(tk.END, "Word Frequency\n")
            self.text.insert(tk.END, "-"*40 + "\n")

            for word, count in frequency.most_common():
                self.text.insert(tk.END, f"{word} : {count}\n")

        except FileNotFoundError:
            messagebox.showerror("Error", "sample.txt file not found.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = WordCountTool(root)
root.mainloop()