from tkinter import *
from tkinter import messagebox
import csv

root = Tk()
root.title('Hospital System')
root.geometry('500x500')

LOGGED_IN = False

ACTIVE_USER = []

main_frame = Frame(root).pack()

# Variabelen
login_email_string = StringVar()
login_password_string = StringVar()
register_email = StringVar()
register_retype_email = StringVar()
register_password = StringVar()
error_message = StringVar()


# Login page
def login_page():
    login_window = Toplevel(root)
    login_window.geometry("300x150")
    login_window.title("Login")
    
    login_frame = Frame(login_window)

    # Entry Fields
    label_email = Label(login_frame, text='E-Mail: ').grid(column=0, row=0, pady=5)
    entry_email = Entry(login_frame, textvariable=login_email_string).grid(column=1, row=0,pady=5)
    label_password = Label(login_frame, text='Password: ').grid(column=0, row=1, pady=5)
    entry_password = Entry(login_frame, show="*", textvariable=login_password_string).grid(column=1, row=1, pady=5)

    # Buttons
    btn_login = Button(login_frame, text="Login").grid(column=0, row=2)
    btn_register = Button(login_frame, text="Register", command=register_form).grid(column=1, row=2)
    btn_cancel = Button(login_frame, text="Cancel", command=login_window.destroy).grid(column=2, row=2)
    
    login_frame.pack()

# Register page
def register_form():
    register_window = Toplevel(root)
    register_window.geometry('400x250')
    register_frame = Frame(register_window)
    
    # Entry Fields
    label_email = Label(register_frame, text='E-Mail: ').grid(column=0, row=0, pady=5)
    entry_email = Entry(register_frame, textvariable=register_email).grid(column=1, row=0,pady=5)
    label_retype_email = Label(register_frame, text='Retype E-Mail: ').grid(column=0, row=1, pady=5)
    entry_retype_email = Entry(register_frame, textvariable=register_retype_email, validate='focusout', validatecommand=check_email).grid(column=1, row=1, pady=5)
    label_password = Label(register_frame, text='Password: ').grid(column=0, row=2, pady=5)
    entry_password = Entry(register_frame, show="*", textvariable=register_password).grid(column=1, row=2, pady=5)
        
    # Buttons
    btn_register = Button(register_frame, text="Register", command=add_registration).grid(column=0, row=3)
    btn_cancel = Button(register_frame, text="Cancel", command=register_window.destroy).grid(column=1, row=3)

    # Pack
    register_frame.pack()
    
# DEZE MOET NOG WERKEND GEMAAKT WORDEN!!
def add_registration(): 
    with open('les3/users.csv', 'a', newline='') as f:
        f.write([register_email, register_password])
        f.close

def check_email():
    if '@' not in register_email.get():
        messagebox.showerror('Error', 'Dit is geen geldig e-mail adres.')
        return False
    elif register_email.get() != register_retype_email.get():
        messagebox.showerror('Error', 'E-mail adressen komen niet overeen.')
        return False
    elif register_email.get() == register_retype_email.get():
        return True
    
if LOGGED_IN == False:
    main_label = Label(main_frame, text='Je bent nog niet ingelogd. Klik hieronder om in te loggen').pack()
    login_btn = Button(main_frame, text='Login', command=login_page).pack()
    
if LOGGED_IN == True:
    main_label = Label(main_frame, text='Je bent ingelogd. Hier komt nog meer functionaliteit').pack()


root.mainloop()




