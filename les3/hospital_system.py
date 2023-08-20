from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.title('Startscherm || Ziekenhuis NHA')

#  Variables
login_email = StringVar()
login_wachtwoord = StringVar()

register_email_1 = StringVar()
register_email_2 = StringVar()
register_wachtwoord = StringVar()

### Hulp Functies

# Check of het ingevoerde een email adres is
def check_is_email():
     if '@' and '.' in register_email_1.get():
        return True
     else:
        messagebox.showerror(title='Geen Email', message='Geen gelidig email adres ingevoerd')
        return True
    
# Check of de twee emailadressen in het registereer form hetzelfde zijn
def check_register_email():
    if register_email_1.get() == register_email_2.get():
        
        return True
    else:
        messagebox.showerror(title='Email komt niet overeen', message='Emailadressen zijn niet hetzelfde')
        
    return True

# Login Form
def login_form():  
    login_window = Toplevel(root)
    login_window.title('Login')
    login_window.geometry('300x200')
   
    email_label = Label(login_window, text='E-Mail: ').grid(column=0, row=0)
    email_entry = Entry(login_window, textvariable=login_email).grid(column=1 , row=0)
    wachtwoord_label = Label(login_window, text='Wachtwoord: ').grid(column=0, row=1)
    wachtwoord_entry = Entry(login_window, textvariable=login_wachtwoord).grid(column=1, row=1)
    login_button = Button(login_window, text='Login', command=login_window.destroy).grid(column=0, row=2)
    annuleer_button = Button(login_window, text='Annuleer', command=login_window.destroy).grid(column=1, row=2)
    

# Registreer Form
def register_form():
    register_window = Toplevel(root)
    register_window.title('Registreren')
    register_window.geometry('350x250')
    
    
    email_label1 = Label(register_window, text='Email: ').grid(column=0, row=0)
    email_entry1 = Entry(register_window, textvariable=register_email_1, validate='focusout', validatecommand=check_is_email).grid(column=1, row=0)
    email_label2 = Label(register_window, text='Retype Email: ').grid(column=0, row=1)
    email_entry2 = Entry(register_window, textvariable=register_email_2, validate='focusout', validatecommand=check_register_email).grid(column=1, row=1)
    password_label = Label(register_window, text='Password: ').grid(column=0, row=2)
    password_entry = Entry(register_window, textvariable=register_wachtwoord).grid(column=1, row=2)
    
    register_button = Button(register_window, text='Registreer', command=register_window.destroy).grid(column=0, row=3)
    annuleer_button = Button(register_window, text='Anuleer', command=register_window.destroy).grid(column=1, row=3)
    

# Startscherm
main_frame = Frame(root).pack(side=TOP)

tekst_frame = Frame(main_frame).pack()
welkom_label = Label(tekst_frame, pady=5, text='Welkom bij het ziekenshuis. Kies hieronder wat u wilt doen.')
welkom_label.pack()

button_frame = Frame(main_frame).pack()
login_button = Button(button_frame, text='Login',width=20, command=login_form).pack()
register_button = Button(button_frame, text='Registreren', width=20, command=register_form).pack()



root.mainloop()