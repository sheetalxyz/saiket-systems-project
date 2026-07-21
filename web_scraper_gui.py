import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class WebScraper:

    def __init__(self, root):
        self.root = root
        self.root.title("Basic Web Scraper")
        self.root.geometry("700x500")
        self.root.config(bg="#E8F5E9")

        tk.Label(root,
                 text="Basic Web Scraper",
                 font=("Arial",18,"bold"),
                 bg="#E8F5E9",
                 fg="green").pack(pady=10)

        tk.Label(root,
                 text="Website URL",
                 font=("Arial",12),
                 bg="#E8F5E9").pack()

        self.url_entry = tk.Entry(root, width=60, font=("Arial",12))
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "https://example.com")

        tk.Button(root,
                  text="Scrape Website",
                  bg="blue",
                  fg="white",
                  font=("Arial",12),
                  command=self.scrape).pack(pady=10)

        self.text = tk.Text(root, width=80, height=20)
        self.text.pack(pady=10)

    def scrape(self):

        url = self.url_entry.get()

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            self.text.delete(1.0, tk.END)

            title = soup.title.string if soup.title else "No Title Found"

            self.text.insert(tk.END, f"Website Title:\n{title}\n\n")

            self.text.insert(tk.END, "Headings:\n\n")

            headings = soup.find_all(["h1","h2","h3"])

            if headings:
                for h in headings:
                    self.text.insert(tk.END, h.get_text(strip=True)+"\n")
            else:
                self.text.insert(tk.END, "No headings found.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = WebScraper(root)
root.mainloop()