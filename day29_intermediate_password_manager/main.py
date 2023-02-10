import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import json

LOGO_IMAGE = "D:/python/100days/day29_intermediate_password_manager/logo.png"
SAVE_FILE = "D:/python/100days/day29_intermediate_password_manager/data.json"

# ASCII values:
# 0-9: 48-57
# A-Z: 65-90
# a-z: 97-122

CAPS_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SMALL_LETTERS = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%&*()-_=+[{]};:,<.>/?'\""

# [chr(_) for _ in list(range(65,91))+list(range(97,123))]
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# list(range(48,58))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = ([choice(CAPS_LETTERS) for _ in range(randint(4,5))] 
                     + [choice(SMALL_LETTERS) for _ in range(randint(4,5))] 
                     + [choice(NUMBERS) for _ in range(randint(2,4))] 
                     + [choice(SYMBOLS) for _ in range(randint(2,4))]
                     )
    shuffle(password_list)
    new_password = ''.join(password_list)
    password_input.delete(0, tk.END)
    password_input.insert(0, new_password)
    root.clipboard_clear()
    root.clipboard_append(new_password)
    
# ---------------------------- FIND PASSWORD  ------------------------------- #
def search_password():
    website = website_input.get().strip()
    if not website: return
    try: 
        with open(SAVE_FILE, mode='r') as data_file:
            data = json.load(data_file)            
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Error", message=f"Data file not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            if messagebox.askokcancel(title=website, message=f"Email:\t\t{email}\nPassword:\t{password}"):
                root.clipboard_clear()
                root.clipboard_append(password)
        else:
            messagebox.showinfo(title="Password not Found", message=f"Details for {website} not found")
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().strip()
    email = email_input.get().strip()
    password = password_input.get().strip()
    
    if not website:
        messagebox.showerror(title="No Website", message="Website cannot be blank")
        return
    if not email:
        messagebox.showerror(title="No Email/Username", message="Email/Username cannot be blank")
        return
    if not password:
        messagebox.showerror(title="No password", message="Password cannot be blank")
        return
        
    is_ok = messagebox.askokcancel(title=f"Add password for {website}", message=f"Email:\t\t{email}\nPassword:\t{password}\n\nClick ok to save")
    # is_ok = True
    if is_ok:        
        new_data = {
            website: {
                "email": email, 
                "password": password
                }
            }
        
        try: 
            with open(SAVE_FILE, mode='r') as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        # except Exception as e: print(e, type(e))
        else:
            data.update(new_data)
            # data[website] = new_data[website]
        finally:
            with open(SAVE_FILE, mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        
        website_input.delete(0, tk.END)
        password_input.delete(0, tk.END)
    
    
# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.config(padx=20, pady=20)

#Logo Image
canvas = tk.Canvas(root, width=110, height=160, highlightthickness=0)
logo_image = tk.PhotoImage(file=LOGO_IMAGE)
canvas.create_image(0,0, image=logo_image, anchor='nw')
canvas.grid(row=0, column=1)


#labels
website_label = tk.Label(root, text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(root, text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)


# Entries
website_input = tk.Entry(root, width=30)
website_input.focus()
website_input.grid(row=1, column=1)

email_input = tk.Entry(root, width=49)
email_input.insert(0, "exapmledummy@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = tk.Entry(root, width=30)
password_input.grid(row=3, column=1)


#Buttons
search_button = tk.Button(root, text="Search", command=search_password, width=15)
search_button.grid(row=1, column=2)

generate_button = tk.Button(root, text="Generate", command=generate_password, width=15)
generate_button.grid(row=3, column=2)

add_button = tk.Button(root, text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

root.mainloop()