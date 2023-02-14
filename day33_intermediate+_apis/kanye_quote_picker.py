import tkinter as tk
import requests

BG_IMG = "D:/python/100days/day33_intermediate+_apis/background.png"
FACE_IMG = "D:/python/100days/day33_intermediate+_apis/kanye.png"

def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    quote = response.json()["quote"]
    return quote

def change_quote():
    quote = get_quote()
    while len(quote)>112: quote = get_quote()
    quote_canvas.itemconfig(quote_text, text=quote)


root = tk.Tk()
root.config(padx=20, pady=20)

quote_img = tk.PhotoImage(file=BG_IMG)
kanye_img = tk.PhotoImage(file=FACE_IMG)

quote_canvas = tk.Canvas(root, width=300, height=414, highlightthickness=0)
quote_canvas.create_image(0,0, image=quote_img, anchor="nw")
quote = "Click for some Kanye quotes..."
quote_text = quote_canvas.create_text(150, 190, width=280, text=quote, font=("ariel",24,"bold"), justify="center")
quote_canvas.pack()

button = tk.Button(root, image=kanye_img, highlightthickness=0, command=change_quote)
button.pack()

root.mainloop()