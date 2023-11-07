from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #

MILK = "#EEEEEE"
CREAM = "#FFFBF5"
YELLOW = "#f7f5dd"
PINK = "#e2979c"
RED = "#e7305b"
BLUE = "#068FFF"   # Unknown hex
OCEAN ="#39A7FF"
NAVYSEA = "#2B3499"
ROYALNAVY = "#190482"
TEAL = "#64CCC5"
SPRING_GREEN = "#D2DE32"
GREEN = "#9bdeac"
TREE = "#7A9D54"
CARROT = "#FF9209"
LILAC = "#D0A2F7"
MOIRA = "#7743DB"
BLACK = "#000000"

fg = TREE

FONT_NAME = "Courier"

# REPS
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# TIMER
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    count_down(5 * 60)              # 5 mins = 5 * 60
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=MOIRA)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=LILAC)
    else:
        count_down(work_sec)
        title_label.config(text="Focus", fg=OCEAN)
    
    # IF 1st, 3rd, 5th, 7th rep: WORK_MIN(25)  [All odd numbers] - valid, but changed.
    # if reps % 2 != 0 and reps % 8!=0:
    #     count_down(WORK_MIN)
    # elif reps % 2 == 0:
    #     count_down(SHORT_BREAK_MIN)
    # else:
    #     count_down(LONG_BREAK_MIN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:            # Dynamic Typing - Able to change data type by overwriting variables. Dynamic change.
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer 
        timer = window.after(1000, count_down, count - 1)         # 1000 ms = 1 sec
    else:
        start_timer()
        marks = ""                         # REFACTOR AND RENAME - CHANGE ALL OCCURRENCES
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔️"
        check_marks.config(text=marks)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 150, pady=75, bg=YELLOW)

title_label = Label(text="Timer", fg=TREE, bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=205,height=230, bg=YELLOW, highlightthickness=0)        # highlighthickness removes whitelines
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103, 115, image = tomato_img)           # This is the (x, y) values for canvas. Approx Half of H/W.
timer_text = canvas.create_text(103, 131, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))        # Font is a tuple value
canvas.grid(column=1, row=1)
count_down(5)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)      # command binds function to button
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg = YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()           # Event driven - Checks for user input


