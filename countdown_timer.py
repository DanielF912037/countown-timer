import time
import tkinter as tk
from tkinter import font
# Define the countdown function
def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))

        # Update the label with the current timer value
        label.config(text=timer)
        root.update()
        time.sleep(1)
        t -= 1

    # Display a message when the countdown reaches zero
    label.config(text="Your time is up")

# Function to start the countdown
def start_countdown():
    global t
    try:
        t = float(entry.get())
        countdown(t)
    except ValueError:
        label.config(text="Invalid input. Please enter a number.")

# Function to reset the timer
def reset_timer():
    global t
    label.config(text="")
    # Clear the input field
    entry.delete(0, tk.END) 

# Create a Tkinter window
root = tk.Tk()
root.title("Countdown Timer")

# Set the window size
root.geometry("400x200")

# Create an entry widget for user input
entry = tk.Entry(root, width=20, font=font.Font(size=16), justify='center')
entry.pack()

# Create a button to start the countdown
start_button = tk.Button(root, text="Start Countdown", command=start_countdown, font=font.Font(size=14), height=1)
start_button.pack()

# Create a label to display the countdown timer
label = tk.Label(root, text="", font=font.Font(size=28))
label.pack()

# Create a button to reset the timer
reset_button = tk.Button(root, text="Reset Timer", command=reset_timer, font=font.Font(size=14), height=1)
reset_button.pack()

root.mainloop()