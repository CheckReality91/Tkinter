from tkinter import *


# Main Frame
root = Tk()
root.title("MST")
root.geometry('300x100')

logged_in = False

def main_page():
    # Frame inside mainframe
    frame = Frame(root)

    # Variables for names
    username = StringVar()
    password = StringVar()


    # Entry Fields
    label_name = Label(frame, text='Name: ').grid(column=0, row=0, pady=5)
    entry_name = Entry(frame, textvariable=username).grid(column=1, row=0,pady=5)
    label_password = Label(frame, text='Password: ').grid(column=0, row=1, pady=5)
    entry_password = Entry(frame, show="*", textvariable=password).grid(column=1, row=1, pady=5)

    # Buttons
    btn_login = Button(frame, text="Login", command=page_after_login).grid(column=0, row=2)
    btn_register = Button(frame, text="Register", command=register_form).grid(column=1, row=2)
    btn_cancel = Button(frame, text="Cancel").grid(column=2, row=2)

def page_after_login():
    print('Hello')
    # Na inloggen moet er een nieuwe window komen en de login page moet gesloten worden.


def register_form():
    register_window = Toplevel(root)
    register_window.title('Registreren')
    register_window.geometry("300x300")
    

if logged_in == False:
    main_page()


# Packs and Mainloop

root.mainloop()