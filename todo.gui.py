import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x500")
        self.root.config(bg="#E8F0FE")

        self.tasks = []

        title = tk.Label(root, text="TO-DO LIST", font=("Arial", 18, "bold"),
                         bg="#E8F0FE", fg="blue")
        title.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=10)

        tk.Button(root, text="Add Task", bg="green", fg="white",
                  font=("Arial", 12), command=self.add_task).pack(pady=5)

        self.listbox = tk.Listbox(root, width=45, height=12,
                                  font=("Arial", 12))
        self.listbox.pack(pady=10)

        tk.Button(root, text="Mark Completed", bg="orange", fg="white",
                  font=("Arial", 12), command=self.complete_task).pack(pady=5)

        tk.Button(root, text="Delete Task", bg="red", fg="white",
                  font=("Arial", 12), command=self.delete_task).pack(pady=5)

        tk.Button(root, text="Exit", bg="black", fg="white",
                  font=("Arial", 12), command=root.quit).pack(pady=10)

    def add_task(self):
        task_text = self.entry.get().strip()

        if task_text == "":
            messagebox.showwarning("Warning", "Please enter a task.")
            return

        task = Task(task_text)
        self.tasks.append(task)
        self.entry.delete(0, tk.END)
        self.update_list()

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index].completed = True
            self.update_list()
        except:
            messagebox.showwarning("Warning", "Select a task first.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_list()
        except:
            messagebox.showwarning("Warning", "Select a task first.")

    def update_list(self):
        self.listbox.delete(0, tk.END)

        for task in self.tasks:
            status = "✔ Completed" if task.completed else "❌ Pending"
            self.listbox.insert(tk.END,
                                f"{task.description} - {status}")

root = tk.Tk()
app = TodoApp(root)
root.mainloop()