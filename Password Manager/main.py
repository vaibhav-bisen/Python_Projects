# ---------------------------- START ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT = ("Arial", 15, "bold")
BLACK = "#000000"
WHITE = "#ffffff"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    
    password_letter = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_symbol = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_number = [choice(NUMBERS) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbol + password_number

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    # Messagebox
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered: "
                                                                   f"\nEmail: {email_data} "
                                                                   f"\nPassword: {password_data} "
                                                                   f"\n Is it ok to save.")
        if is_ok:
            with open(file="data.txt", mode="a") as data_file:
                data_file.write(f"{website_data.title()} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background=BLACK)

# Canvas setup
canvas = Canvas(width=200, height=200, background=BLACK, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, ipadx=60)

# Labels
website_label = Label(text="Website :", background=BLACK, foreground=WHITE, font=FONT)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username :", background=BLACK, foreground=WHITE, font=FONT)
email_label.grid(row=2, column=0)

password_label = Label(text="Password :", background=BLACK, foreground=WHITE, font=FONT)
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Button
generate_button = Button(width=20, text="Generate Password", font=("Arial", 10, "bold"), command=generate_password)
generate_button.grid(row=4, column=1)

add_button = Button(width=20, text="Add", font=("Arial", 10, "bold"), command=add_data)
add_button.grid(row=5, column=1, rowspan=2)

window.mainloop()
# ---------------------------- END ------------------------------- #
