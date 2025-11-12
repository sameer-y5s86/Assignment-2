# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com) in co-creating this code.
# Rock–Paper–Scissors GUI Game
# Author: Your Name
# Date: November 2025

import tkinter as tk
import random

# --- Game Logic ---
OPTIONS = ["Rock", "Paper", "Scissors"]

def play(player_choice):
    """Handle one round of Rock–Paper–Scissors."""
    computer_choice = random.choice(OPTIONS)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock–Paper–Scissors Game")
root.geometry("300x250")

title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 12))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for option in OPTIONS:
    btn = tk.Button(button_frame, text=option, width=10, height=2,
                    command=lambda opt=option: play(opt))
    btn.pack(side="left", padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_button.pack()

root.mainloop()
