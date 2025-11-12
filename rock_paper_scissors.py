# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com) in co-creating this code.
# Rock–Paper–Scissors GUI Game (Improved Version)
# Author: Your Name
# Date: November 2025

import tkinter as tk
import random

# --- Game Logic ---
OPTIONS = ["Rock", "Paper", "Scissors"]
EMOJIS = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

player_score = 0
computer_score = 0

def play(player_choice):
    """Play one round of Rock–Paper–Scissors."""
    global player_score, computer_score

    computer_choice = random.choice(OPTIONS)
    result_text = ""

    if player_choice == computer_choice:
        result_text = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result_text = "You win!"
        player_score += 1
    else:
        result_text = "Computer wins!"
        computer_score += 1

    # Update result and score display
    result_label.config(
        text=f"You chose {EMOJIS[player_choice]}  |  Computer chose {EMOJIS[computer_choice]}\n{result_text}"
    )
    score_label.config(text=f"Player: {player_score}    Computer: {computer_score}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock–Paper–Scissors Game")
root.geometry("400x350")
root.config(bg="#e8f0fe")  # soft blue background

# Title
title_label = tk.Label(
    root,
    text="Rock–Paper–Scissors",
    font=("Arial", 16, "bold"),
    bg="#e8f0fe",
    fg="#202124",
)
title_label.pack(pady=15)

# Instruction
instruction_label = tk.Label(
    root,
    text="Make your choice:",
    font=("Arial", 12),
    bg="#e8f0fe",
)
instruction_label.pack(pady=5)

# Button Frame
button_frame = tk.Frame(root, bg="#e8f0fe")
button_frame.pack(pady=10)

def on_enter(e):
    e.widget.config(bg="#d2e3fc")

def on_leave(e):
    e.widget.config(bg="#f1f3f4")

for option in OPTIONS:
    btn = tk.Button(
        button_frame,
        text=f"{EMOJIS[option]} {option}",
        width=12,
        height=2,
        bg="#f1f3f4",
        relief="raised",
        command=lambda opt=option: play(opt),
    )
    btn.pack(side="left", padx=8)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Result Label
result_label = tk.Label(
    root, text="", font=("Arial", 12), bg="#e8f0fe", fg="#1a73e8", justify="center"
)
result_label.pack(pady=20)

# Score Label
score_label = tk.Label(
    root,
    text="Player: 0    Computer: 0",
    font=("Arial", 12, "bold"),
    bg="#e8f0fe",
    fg="#202124",
)
score_label.pack(pady=10)

# Exit Button
exit_button = tk.Button(
    root,
    text="Exit Game",
    width=12,
    height=1,
    bg="#ea4335",
    fg="white",
    font=("Arial", 10, "bold"),
    command=root.destroy,
)
exit_button.pack(pady=10)

root.mainloop()
