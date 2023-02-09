import tkinter as tk

window = tk.Tk()
window.title("Widgets")
window.minsize(width=500, height=500)

#Labels
label = tk.Label(text = "Tkinder Widgets")
label.pack()

#button
def button_click():
    print("Button clicked")
button = tk.Button(text='Click me', command=button_click)
button.pack()

#Entries (single line text box)
entry = tk.Entry(width=30)
# entry.insert(tk.END, string="Default text")
entry.insert(-1, string="Default text")                 #Add some text to begin with
print(entry.get())
entry.pack()

#text (Multiline text box)
text = tk.Text(width=30, height=5)
text.focus()                                                            #Puts cursor in textbox.
text.insert(tk.END, "Example of Multi-line Entry \nline1 \nline2")      #Add some text to begin with
print(text.get('1.0', tk.END))                                          #Get's current value in textbox at line 1, character 0
text.pack()

#spinbox
def spinbox_used():
    print(spinbox.get())                                        #gets the current value in spinbox.
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#scale (Slider)
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to=10, length=200, orient='horizontal', command=scale_used)
scale.set(5)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(check_state.get())            #Prints 1 if On button checked, otherwise 0.
check_state = tk.IntVar()               #variable to hold on to checked state, 0 is off, 1 is on.
checkbutton = tk.Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
checkbutton.pack()

#Radiobutton
def radiobutton_used():
    print(radio_state.get())
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Radiobutton 1", value=1, variable=radio_state, command=radiobutton_used)
radiobutton2 = tk.Radiobutton(text="Radiobutton 2", value=2, variable=radio_state, command=radiobutton_used)
radiobutton1.select()
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))          # Gets current selection from listbox
listbox = tk.Listbox(height=4)
fruits = ["Apple", "Orange", "Banana", "Mango"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()