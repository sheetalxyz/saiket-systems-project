import tkinter as tk
from tkinter import messagebox
import os

# input.txt ka path
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

class FileHandler:

    def __init__(self, root):
        self.root = root
        self.root.title("Basic File Handling")
        self.root.geometry("600x500")
        self.root.config(bg="#E8F5E9")

        tk.Label(root,
                 text="Basic File Handling",
                 font=("Arial",18,"bold"),
                 bg="#E8F5E9",
                 fg="green").pack(pady=10)

        tk.Label(root,
                 text="Find Word",
                 bg="#E8F5E9",
                 font=("Arial",12)).pack()

        self.find_entry = tk.Entry(root, font=("Arial",12), width=30)
        self.find_entry.pack(pady=5)

        tk.Label(root,
                 text="Replace With",
                 bg="#E8F5E9",
                 font=("Arial",12)).pack()

        self.replace_entry = tk.Entry(root, font=("Arial",12), width=30)
        self.replace_entry.pack(pady=5)

        tk.Button(root,
                  text="Load File",
                  bg="green",
                  fg="white",
                  font=("Arial",12),
                  command=self.load_file).pack(pady=5)

        tk.Button(root,
                  text="Replace & Save",
                  bg="blue",
                  fg="white",
                  font=("Arial",12),
                  command=self.replace_text).pack(pady=5)

        self.text = tk.Text(root, width=65, height=15)
        self.text.pack(pady=10)

    def load_file(self):
        try:
            with open(file_path, "r") as file:
                data = file.read()

            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, data)

        except FileNotFoundError:
            messagebox.showerror("Error", "input.txt file not found.")

    def replace_text(self):
        try:
            with open(file_path, "r") as file:
                data = file.read()

            find_word = self.find_entry.get()
            replace_word = self.replace_entry.get()

            if find_word == "":
                messagebox.showwarning("Warning", "Enter a word to find.")
                return

            new_data = data.replace(find_word, replace_word)

            with open(file_path, "w") as file:
                file.write(new_data)

            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, new_data)

            messagebox.showinfo("Success", "Text replaced and saved successfully.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = FileHandler(root)
root.mainloop()