
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TOMATO_IMAGE = "d:/python/100days/day28_intermediate_pomodoro_timer/tomato.png"

reps = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps
    if timer: 
        window.after_cancel(timer)
        heading_label.config(text="Timer", fg=PINK)
        canvas.itemconfig(timer_text, text="00:00")
        checkmarks["text"] = ''
        timer = None
        reps = 0
        
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_button_press():
    global timer
    if not timer: start_timer()

def start_timer():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    window.bell()
    global reps
    reps += 1
    if reps % 8 == 0:
        reps = 0
        heading_label.config(text="Long Break", fg=RED)
        count_down(int(LONG_BREAK_MIN*60))
        # count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        heading_label.config(text="Break", fg=PINK)
        count_down(int(SHORT_BREAK_MIN*60))
        # count_down(SHORT_BREAK_MIN*60)
    else:
        if reps == 1: checkmarks["text"] = ''
        heading_label.config(text="Work", fg=GREEN)
        count_down(int(WORK_MIN*60))
        # count_down((WORK_MIN*60))
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    if time == 0:
        if reps%2: checkmarks["text"] += '✔'
        # checkmarks["text"] = ''.ljust((reps+1//2), '✔')
        start_timer()
    else:
        global timer
        minute = time//60
        second = time%60
        time_text = f"{str(minute).rjust(2,'0')}:{str(second).rjust(2,'0')}"
        canvas.itemconfig(timer_text, text=time_text)
        timer = window.after(1000, count_down, time-1)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=50, pady=20)

canvas = tk.Canvas(window , width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = tk.PhotoImage(file=TOMATO_IMAGE)
canvas.create_image(100,112,image=bg_image, anchor = "center")
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 26, 'bold'), fill=YELLOW) 
canvas.grid(row=1,column=1)

heading_label = tk.Label(window, text="Timer", font=(FONT_NAME, 26, 'bold'), fg=PINK, bg=YELLOW)
heading_label.grid(row=0, column=1)

start_button = tk.Button(window, text="Start", width=5, command=start_button_press)
start_button.grid(row=2, column=0)

reset_button = tk.Button(window, text="Reset", width=5, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = tk.Label(window, font=(FONT_NAME, 14, 'bold'), fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)


window.mainloop()