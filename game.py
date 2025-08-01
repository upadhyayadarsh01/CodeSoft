import tkinter as tk
import random


player_score = 0
computer_score = 0
tie_score = 0

def play(user_choice):
    global player_score, computer_score, tie_score

    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)

    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result = "It's a Tie!"
        tie_score += 1
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    update_scores()
    root.focus()  

def update_scores():
    score_label.config(
        text=f"Score - You: {player_score}  |  Computer: {computer_score}  |  Ties: {tie_score}")

def reset_game():
    global player_score, computer_score, tie_score
    player_score = computer_score = tie_score = 0
    update_scores()
    user_label.config(text="You chose:")
    comp_label.config(text="Computer chose:")
    result_label.config(text="")
    root.focus()  


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x450")
root.resizable(False, False)
root.config(bg="#2c3e50")  


tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"),
         bg="#2c3e50", fg="white").pack(pady=20)


user_label = tk.Label(root, text="You chose:", font=("Arial", 14),
                      bg="#2c3e50", fg="white")
user_label.pack()

comp_label = tk.Label(root, text="Computer chose:", font=("Arial", 14),
                      bg="#2c3e50", fg="white")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"),
                        fg="#2ecc71", bg="#2c3e50")  
result_label.pack(pady=10)


button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)


def create_choice_button(choice):
    return tk.Button(button_frame,
                     text=choice,
                     width=10,
                     font=("Arial", 14),
                     bg="#34495e",
                     fg="white",
                     activebackground="#34495e",
                     activeforeground="white",
                     relief="flat",
                     command=lambda: play(choice))

for choice in ["Rock", "Paper", "Scissors"]:
    btn = create_choice_button(choice)
    btn.pack(side="left", padx=10)


score_label = tk.Label(root, text="Score - You: 0  |  Computer: 0  |  Ties: 0",
                       font=("Arial", 12), bg="#2c3e50", fg="white")
score_label.pack(pady=10)


tk.Button(root, text="Reset Game", font=("Arial", 12), bg="#e74c3c",
          fg="white", activebackground="#c0392b", activeforeground="white",
          relief="flat", command=reset_game).pack(pady=10)


root.mainloop()

   
   