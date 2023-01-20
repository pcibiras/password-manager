# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = email_entry.get()
    website = web_entry.get()
    password = passw_entry.get()
    with open("data.txt", "a") as file:
        file.write(f"{email} | {website} | {password}")
        file.write('\n')
    email_entry.delete(0,'end')
    passw_entry.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

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
passw_entry = Entry(width=21)
passw_entry.grid(column=1, row=3, sticky=W+E)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W+E)
generate_passw_button = Button(text="Generate Password")
generate_passw_button.grid(column=2, row=3, sticky=W+E)

print ("something")

window.mainloop()
