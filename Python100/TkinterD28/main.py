from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CREAM = "FFFBF5"
MOIRA = "#7743DB"
fg = GREEN

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)              # 5 mins = 5 * 60

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:            # Dynamic Typing - Able to change data type by overwriting variables. Dynamic change.
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)         # 1000 ms = 1 sec

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 150, pady=75, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=205,height=230, bg=YELLOW, highlightthickness=0)        # highlighthickness removes whitelines
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 115, image = tomato_img)           # This is the (x, y) values for canvas. Approx Half of H/W.
timer_text = canvas.create_text(103, 131, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))        # Font is a tuple value
canvas.grid(column=1, row=1)
count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)      # command binds function to button
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔️", fg=GREEN, bg = YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()           # Event driven - Checks for user input


