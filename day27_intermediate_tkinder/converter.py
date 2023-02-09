import tkinter as tk

def miles_to_kms():
    miles = float(miles_input.get())
    kms = round(1.609 * miles)
    kms_output['text'] = str(kms)
    

window = tk.Tk()
window.title("Miles to Kilometer")
window.config(padx=20, pady=20)

miles_input = tk.Entry(width=10)
miles_input.insert(tk.END, '0')
miles_input.grid(row=0, column=1)

miles_label = tk.Label(text='Miles')
miles_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kms_output = tk.Label(text='0')
kms_output.grid(row=1, column=1)

kms_label = tk.Label(text="kms")
kms_label.grid(row=1, column=2)

button = tk.Button(text="Calculate", command=miles_to_kms)
button.grid(row=2, column=1)


window.mainloop()




