import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Dice emojis
dice_faces = {
    1: '\u2680',
    2: '\u2681',
    3: '\u2682',
    4: '\u2683',
    5: '\u2684',
    6: '\u2685'
}

# Game state
player1_name = "Player 1"
player2_name = "Player 2"
player1_score = 0
player2_score = 0
round_count = 0
MAX_ROUNDS = 5

# === Main Window ===
root = tk.Tk()
root.title("Two Dice Roller - Best of 5")
root.attributes("-fullscreen", True)
root.configure(bg="grey")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# === Background ===
bg_image = Image.open("DICE.png")
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# === Functions ===

def reset_game():
    global player1_score, player2_score, round_count
    player1_score = player2_score = round_count = 0
    dice1_label.config(text='\u2680')
    dice2_label.config(text='\u2680')
    total_label.config(text="Click 'Roll Dice' to start")
    score_label.config(text=f"{player1_name}: 0 | {player2_name}: 0")
    round_label.config(text="Round: 0 / 5")
    result_label.config(text="")

def confirm_quit():
    if messagebox.askyesno("Exit Confirmation", "Are you sure you want to quit?"):
        root.attributes("-fullscreen", False)
        root.destroy()

def hide_game_elements():
    dice1_label.pack_forget()
    dice2_label.pack_forget()
    round_label.pack_forget()
    total_label.pack_forget()
    score_label.pack_forget()
    result_label.pack_forget()
    button_frame.pack_forget()

def show_game_elements():
    dice1_label.pack(pady=20)
    dice2_label.pack(pady=20)
    round_label.pack()
    total_label.pack(pady=10)
    score_label.pack(pady=5)
    result_label.pack(pady=5)
    button_frame.pack(pady=30)

def start_game():
    global player1_name, player2_name
    player1_name = p1_entry.get() or "Player 1"
    player2_name = p2_entry.get() or "Player 2"
    score_label.config(text=f"{player1_name}: 0 | {player2_name}: 0")
    name_frame.place_forget()
    start_button.place_forget()
    show_game_elements()

def animate_dice(count=0):
    if count < 5:
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        dice1_label.config(text=dice_faces[d1])
        dice2_label.config(text=dice_faces[d2])
        root.after(100, lambda: animate_dice(count + 1))
    else:
        roll_dice()

def roll_dice():
    global player1_score, player2_score, round_count
    if round_count >= MAX_ROUNDS:
        return

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    dice1_label.config(text=dice_faces[die1])
    dice2_label.config(text=dice_faces[die2])
    total_label.config(text=f"Total: {total}")

    if die1 > die2:
        player1_score += 1
    elif die2 > die1:
        player2_score += 1

    round_count += 1
    round_label.config(text=f"Round: {round_count} / {MAX_ROUNDS}")
    score_label.config(text=f"{player1_name}: {player1_score} | {player2_name}: {player2_score}")

    if round_count == MAX_ROUNDS:
        if player1_score > player2_score:
            result = f"🎉 {player1_name} Wins!"
        elif player2_score > player1_score:
            result = f"🎉 {player2_name} Wins!"
        else:
            result = "🤝 It's a Draw!"
        result_label.config(text=result)

# === Name Entry ===
name_frame = tk.Frame(root, bg="white", bd=2, relief="ridge", padx=20, pady=15)
name_frame.place(relx=0.5, rely=0.4, anchor="center")

p1_label = tk.Label(name_frame, text="Player 1 Name:", font=('Arial', 14))
p1_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
p1_entry = tk.Entry(name_frame, font=('Arial', 14), bd=2, width=20)
p1_entry.grid(row=0, column=1, padx=10, pady=5)

p2_label = tk.Label(name_frame, text="Player 2 Name:", font=('Arial', 14))
p2_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
p2_entry = tk.Entry(name_frame, font=('Arial', 14), bd=2, width=20)
p2_entry.grid(row=1, column=1, padx=10, pady=5)

start_button = tk.Button(
    root, text="Start Game", font=('Arial', 14, 'bold'),
    bg="lightgreen", activebackground="limegreen",
    width=15, command=start_game
)
start_button.place(relx=0.5, rely=0.53, anchor="center")

# === Game UI Widgets ===
dice1_label = tk.Label(root, text='\u2680', font=('Arial', 100), bg="lightblue")
dice2_label = tk.Label(root, text='\u2680', font=('Arial', 100), bg="lightpink")

round_label = tk.Label(root, text="Round: 0 / 5", font=('Arial', 20, 'bold'), bg="white", relief="solid", bd=1)
total_label = tk.Label(root, text="Click 'Roll Dice' to start", font=('Arial', 18), fg="red")
score_label = tk.Label(root, text="Player 1: 0 | Player 2: 0", font=('Arial', 18))
result_label = tk.Label(root, text="", font=('Arial', 18, "bold"), fg="green")

button_frame = tk.Frame(root, bg=root["bg"], bd=0)

tk.Button(button_frame, text="Roll Dice", command=animate_dice,
          font=('Arial', 14, 'bold'), bg="lightblue", activebackground="deepskyblue", width=12).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Reset Game", command=reset_game,
          font=('Arial', 14, 'bold'), bg="mistyrose", activebackground="lightgreen", width=12).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Quit", command=confirm_quit,
          font=('Arial', 14, 'bold'), bg="lightcoral", activebackground="red", width=12).grid(row=0, column=2, padx=10)

# Hide game UI until game starts
hide_game_elements()

# Handle window close
root.protocol("WM_DELETE_WINDOW", confirm_quit)

# Start the app
root.mainloop()
