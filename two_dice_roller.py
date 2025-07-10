import tkinter as tk
import random

# Map dice number to emoji
dice_faces = {
    1: '⚀',
    2: '⚁',
    3: '⚂',
    4: '⚃',
    5: '⚄',
    6: '⚅'
}

# Function to roll the dice
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    dice1_label.config(text=dice_faces[die1])
    dice2_label.config(text=dice_faces[die2])
    total_label.config(text=f"Total: {total}")

# Set up main window
root = tk.Tk()
root.title("Emoji Dice Roller")
root.geometry("250x300")
root.configure(bg="lightyellow")

# Dice 1
dice1_label = tk.Label(root, text='⚀', font=('Arial', 60), bg="lightblue")
dice1_label.pack(pady=10)

# Dice 2
dice2_label = tk.Label(root, text='⚀', font=('Arial', 60), bg="lightpink")
dice2_label.pack(pady=10)

# Roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=('Arial', 14))
roll_button.pack(pady=5)

# Total display
total_label = tk.Label(root, text="Total: ", font=('Arial', 14), bg="lightyellow")
total_label.pack(pady=5)

# Quit button
quit_button = tk.Button(root, text="Quit", command=root.quit, font=('Arial', 14))
quit_button.pack(pady=5)

# Start the GUI loop
root.mainloop()
