import tkinter as tk


def button_pressed():
    # print(input_txt.get())
    my_label['text'] = input_txt.get()
    
    
window = tk.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

#label
my_label = tk.Label(text="This is a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label['text'] = 'New text'
my_label.config(text = 'New New Text')

#buttton
button = tk.Button(text="Click me", command=button_pressed)
button.pack()

#Entry
input_txt = tk.Entry(width=10, )
input_txt.pack()
input_txt.insert(tk.END, "default")

    

window.mainloop()