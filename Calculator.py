import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget.cget("text")))

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#87CEEB")  


entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right", bg="white")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)


buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

for row in buttons:
    frame = tk.Frame(root, bg="#87CEEB")
    frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(frame, text=char, font=("Arial", 18), bd=2, bg="#333333", fg="white")
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        if char == "=":
            btn.config(bg="#4CAF50", fg="white", command=evaluate)  
        else:
            btn.bind("<Button-1>", click)


clear_btn = tk.Button(root, text="C", font=("Arial", 18), bg="#f44336", fg="white", command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()

