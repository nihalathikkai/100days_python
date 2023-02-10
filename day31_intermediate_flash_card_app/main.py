import tkinter as tk
import pandas as pd
from time import sleep
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

CARD_FRONT_IMG = "D:/python/100days/day31_intermediate_flash_card_app/images/card_front.png"
CARD_BACK_IMG = "D:/python/100days/day31_intermediate_flash_card_app/images/card_back.png"
RIGHT_IMG = "D:/python/100days/day31_intermediate_flash_card_app/images/right.png"
WRONG_IMG = "D:/python/100days/day31_intermediate_flash_card_app/images/wrong.png"
DATA_FILE = "D:/python/100days/day31_intermediate_flash_card_app/data/french_words.csv"
PROGRESS_FILE = "D:/python/100days/day31_intermediate_flash_card_app/data/words_to_learn.csv"

#--------------------------------------- MANAGE DATA ---------------------------------------#
to_learn = []
current_card = {}
try:
    data = pd.read_csv(PROGRESS_FILE)
except FileNotFoundError:
    data = pd.read_csv(DATA_FILE)
finally:
    to_learn = data.to_dict(orient="records")

def save_progress():
    pd.DataFrame(data=to_learn).to_csv(PROGRESS_FILE , index=False)

#--------------------------------------- BUTTON LOGIC ---------------------------------------#
def wrong():
    new_flashcard()
    print(len(to_learn))

def right():
    to_learn.remove(current_card)
    new_flashcard()
    print(len(to_learn))

def new_flashcard():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = choice(to_learn)
    card.itemconfig(card_face, image=card_front_img)
    card.itemconfig(language, text="French", fill="Black")
    card.itemconfig(word, text=current_card["French"], fill="Black")
    flip_timer = root.after(3000, flip, current_card["English"])
    
    
def flip(english):
    global on_front_side
    card.itemconfig(card_face, image=card_back_img)
    card.itemconfig(language, text="English", fill="White")
    card.itemconfig(word, text=english, fill="White")
     

# #--------------------------------------- UI SETUP ---------------------------------------#
root = tk.Tk()
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.title("Flashy")

# Loading images into objects
card_front_img = tk.PhotoImage(file=CARD_FRONT_IMG)
card_back_img = tk.PhotoImage(file=CARD_BACK_IMG)
wrong_img = tk.PhotoImage(file=WRONG_IMG)
right_img = tk.PhotoImage(file=RIGHT_IMG)

# Creating Card
card = tk.Canvas(root, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_face = card.create_image(0,0, image=card_front_img, anchor="nw")
card.grid(row=0, column=0, columnspan=2)
language = card.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Creating Buttons
wrong_button = tk.Button(root,image=wrong_img, background=BACKGROUND_COLOR, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=0)

right_button = tk.Button(root, image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

# Calling the first card
flip_timer = root.after(0, lambda : None)
new_flashcard()

root.mainloop()

save_progress()