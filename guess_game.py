import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

# Random number generate
number = random.randint(1,100)

def check_guess():
    global nummber
    try:
        guess = int(entry.get())

        if guess < number:
            result_label.config(text="Too Low! Try Again.")
        elif guess > number:
            result_label.config(text="Too High! Try Again.")
        else:
            result_label.config(text="Correct Guess!")
    except:
            result_label.config(text="Please enter a valid number!")       

def reset_game():
    global number
    nummber = random.randint(1,100)
    print(number)
    result_label.config(text="")
    entry.delete(0,tk.END)

# Title Label
title_label = tk.Label(root,text="Guess the Number(1-100",font=("Arial",14))
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=10)

# Buttons
guess_btn = tk.Button(root,text="Check Guess",command=check_guess)
guess_btn.pack(pady=5)

reset_btn = tk.Button(root,text="Reset Game",command=reset_game)
reset_btn.pack(pady=5)

# Result label
result_label = tk.Label(root,text="",font=("Arial",12))
result_label.pack(pady=20)

root.mainloop()