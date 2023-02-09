import tkinter as tk


def button_pressed():
    # print(input_txt.get())
    my_label['text'] = input_txt.get()
    
    
window = tk.Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=10)

#label
my_label = tk.Label(text="This is a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label['text'] = 'New text'
my_label.config(text = 'New New Text')
my_label.config(padx=20, pady=50)

#buttton
button = tk.Button(text="Click me", command=button_pressed)
button.grid(row=1, column=1)

#buttton2
button2 = tk.Button(text="New Button", command=button_pressed)
button2.grid(row=0, column=2)

#Entry
input_txt = tk.Entry(width=10, )
input_txt.grid(row=2, column=3)
input_txt.insert(tk.END, "default")

    

window.mainloop()