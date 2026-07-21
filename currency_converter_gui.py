import tkinter as tk
from tkinter import messagebox
import requests

class CurrencyConverter:

    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("500x400")
        self.root.config(bg="#EDE7F6")

        tk.Label(root,
                 text="Currency Converter",
                 font=("Arial",18,"bold"),
                 bg="#EDE7F6",
                 fg="purple").pack(pady=10)

        tk.Label(root, text="Amount", bg="#EDE7F6").pack()
        self.amount = tk.Entry(root, font=("Arial",12))
        self.amount.pack()

        tk.Label(root, text="From Currency (e.g. USD)", bg="#EDE7F6").pack()
        self.from_currency = tk.Entry(root, font=("Arial",12))
        self.from_currency.pack()

        tk.Label(root, text="To Currency (e.g. INR)", bg="#EDE7F6").pack()
        self.to_currency = tk.Entry(root, font=("Arial",12))
        self.to_currency.pack()

        tk.Button(root,
                  text="Convert",
                  bg="blue",
                  fg="white",
                  command=self.convert).pack(pady=10)

        self.result = tk.Label(root,
                               text="",
                               font=("Arial",14,"bold"),
                               bg="#EDE7F6")
        self.result.pack(pady=10)

    def convert(self):
        try:
            amount = float(self.amount.get())
            from_curr = self.from_currency.get().upper()
            to_curr = self.to_currency.get().upper()

            url = f"https://open.er-api.com/v6/latest/{from_curr}"
            response = requests.get(url)
            data = response.json()

            if data["result"] != "success":
                messagebox.showerror("Error", "Invalid Currency Code")
                return

            rate = data["rates"][to_curr]
            converted = amount * rate

            self.result.config(
                text=f"{amount} {from_curr} = {converted:.2f} {to_curr}"
            )

        except KeyError:
            messagebox.showerror("Error", "Invalid Currency Code")

        except ValueError:
            messagebox.showerror("Error", "Enter a valid amount")

        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
app = CurrencyConverter(root)
root.mainloop()