# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com) in co-creating this code.
# Rock–Paper–Scissors GUI Game (with Rules Popup + Timer)
# Author: Sameer Liaquat
# Date: 12- November 2025

import tkinter as tk
from tkinter import messagebox
import random

# --- Game Logic ---
OPTIONS = ["Rock", "Paper", "Scissors"]
EMOJIS = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}

player_score = 0
computer_score = 0
seconds_passed = 0  # timer counter


def play(player_choice):
    """Play one round of Rock–Paper–Scissors."""
    global player_score, computer_score

    computer_choice = random.choice(OPTIONS)

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


def show_rules():
    """Display a popup with game rules."""
    rules_text = (
        "🎮 Rock–Paper–Scissors Rules:\n\n"
        "• Rock beats Scissors\n"
        "• Scissors beats Paper\n"
        "• Paper beats Rock\n\n"
        "Select your move — the computer will choose too.\n"
        "Whoever wins earns a point!"
    )
    messagebox.showinfo("How to Play", rules_text)


def update_timer():
    """Update the timer every second."""
    global seconds_passed
    seconds_passed += 1
    timer_label.config(text=f"Time: {seconds_passed} seconds")
    root.after(1000, update_timer)  # schedule this function again after 1 second


# --- GUI Setup ---
root = tk.Tk()
root.title("Rock–Paper–Scissors Game")
root.geometry("400x400")
root.config(bg="#e8f0fe")  # soft blue background

# Top Frame (Title + Rules button)
top_frame = tk.Frame(root, bg="#e8f0fe")
top_frame.pack(fill="x", pady=5, padx=10)

title_label = tk.Label(
    top_frame,
    text="Rock–Paper–Scissors",
    font=("Arial", 16, "bold"),
    bg="#e8f0fe",
    fg="#202124",
)
title_label.pack(side="left")

rules_button = tk.Button(
    top_frame,
    text="❓",
    font=("Arial", 12, "bold"),
    bg="#f1f3f4",
    width=3,
    relief="raised",
    command=show_rules,
)
rules_button.pack(side="right")

# How to Play (static text)
how_to_play = tk.Label(
    root,
    text="Rock beats Scissors • Scissors beats Paper • Paper beats Rock",
    font=("Arial", 10),
    bg="#e8f0fe",
    fg="#5f6368",
)
how_to_play.pack(pady=2)

# Instruction Label
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

# Timer Label (NEW)
timer_label = tk.Label(
    root,
    text="Time: 0 seconds",
    font=("Arial", 10, "bold"),
    bg="#e8f0fe",
    fg="#5f6368",
)
timer_label.pack(pady=5)

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

# Start the timer
update_timer()

root.mainloop()
