import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = password_length.get()
    if length < 4:
        messagebox.showwarning("Warning", "Password should be at least 4 characters long")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x260")
root.resizable(False, False)
root.config(bg="#2c3e50")  


tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"),
         bg="#2c3e50", fg="white").pack(pady=10)

tk.Label(root, text="Select Password Length:", font=("Arial", 12),
         bg="#2c3e50", fg="white").pack()
password_length = tk.IntVar(value=12)
tk.Scale(root, from_=4, to=32, orient="horizontal", variable=password_length,
         length=300, bg="#34495e", fg="white", troughcolor="#95a5a6",
         highlightthickness=0).pack()


password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), justify="center",
         width=28, bg="#ecf0f1", fg="#2c3e50", relief="flat").pack(pady=10)


tk.Button(root, text="Generate Password", command=generate_password,
          font=("Arial", 12), bg="#27ae60", fg="white", activebackground="#1e8449",
          relief="flat", width=20).pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          font=("Arial", 12), bg="#2980b9", fg="white", activebackground="#1f618d",
          relief="flat", width=20).pack()


root.mainloop()
