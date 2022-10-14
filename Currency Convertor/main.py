from tkinter import *
from forex_python.converter import CurrencyRates
FONT = ("Arial", 20, "bold")
BG = "#B6D0E2"


def display_selected_1(choice):
    """ Select first currency from dropdown menu and display on label """
    choice = clicked_1.get()
    enter_amount_label.config(text=choice)


def display_selected_2(choice):
    """ Select second currency from dropdown menu and display on label """
    choice = clicked_2.get()
    curr_convert.config(text=choice)


def convert(*args):
    """ Convert select one currency to another elect currency """
    choice_1 = clicked_1.get()
    choice_2 = clicked_2.get()

    try:
        amount_enter = float(input_curr.get())
        cr = CurrencyRates()
        convert_cur = cr.convert(choice_1, choice_2, amount_enter)
        convert_amount.config(text=round(convert_cur, 2))
    except ValueError as value_error:
        error.config(text=value_error)


window = Tk()
window.title("Currency Converter")
window.config(padx=10, pady=10, width=500, height=300, background=BG)

heading = Label(text="Real Time Currency Converter", font=FONT, background=BG)
heading.grid(row=0, column=0, columnspan=4)

options = [
    "USD", "JPY", "BGN", "CYP", "CZK", "DKK", "EEK", "GBP",	"HUF",	"LTL", "LVL", "MTL", "PLN", "ROL",	"RON",	"SEK",
    "SIT",	"SKK",	"CHF",	"ISK",	"NOK",	"HRK",	"RUB",	"TRL",	"TRY",	"AUD",	"BRL",	"CAD",	"CNY",	"HKD",
    "IDR",	"ILS",	"INR",	"KRW",	"MXN",	"MYR",	"NZD",	"PHP",	"SGD",	"THB",	"ZAR"
]

# Setting clicked for currency
clicked_1 = StringVar()
clicked_1.set("USD")

clicked_2 = StringVar()
clicked_2.set("USD")

enter_amount = Label(text="Enter amount: ", background=BG)
enter_amount.grid(row=1, column=0)

input_curr = Entry()
input_curr.focus_set()
input_curr.grid(row=1, column=1)

# Creating widget ( Dropdown menu )
drop_1 = OptionMenu(window, clicked_1, *options, command=display_selected_1)
drop_1.grid(row=1, column=2)

to_label = Label(text="To", background=BG)
to_label.grid(row=1, column=3)

drop_2 = OptionMenu(window, clicked_2, *options, command=display_selected_2)
drop_2.grid(row=1, column=4)

convert_button = Button(text="Convert", width=15, command=convert)
convert_button.grid(row=2, column=3, pady=10)

enter_amount_label = Label(text="", background=BG)
enter_amount_label.grid(row=3, column=2)

convert_amount = Label(text="00")
convert_amount.grid(row=3, column=3)

curr_convert = Label(text="", background=BG)
curr_convert.grid(row=3, column=4)

error = Label(text="", background=BG)
error.grid(row=4, column=0, columnspan=2)

window.bind("<Return>", convert)
window.mainloop()
