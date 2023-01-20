from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    passw_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    website = web_entry.get()
    password = passw_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops!", message="Please don't leave any fields blank")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email},"
                               f"\n Password: {password} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{email} | {website} | {password}")
                file.write('\n')
            web_entry.delete(0,'end')
            passw_entry.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
passw_label = Label(text="Password:")
passw_label.grid(column=0, row=3)
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky=W+E)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W+E)
email_entry.insert(0, "some@email.com")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W+E)
generate_passw_button = Button(text="Generate Password", command=generate_password)
generate_passw_button.grid(column=2, row=3, sticky=W+E)
passw_entry = Entry(width=21)
passw_entry.grid(column=1, row=3, sticky=W+E)

window.mainloop()
