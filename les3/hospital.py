from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x200')
root.title("Hospital Login")

frame = Frame(root, pady=25)

# Text Variables
log_email = StringVar()
log_password = StringVar()
retype_email = StringVar()
reg_email = StringVar()
reg_password = StringVar()

def check_email():
    if email == retype_email:
        return True
    else:
        messagebox.showerror(title="Error", message='E-mail is not the same.')
        return False

# Registration Window
def register_window():
    window = Toplevel(root)
    register_frame = Frame(window,pady=25)
    window.title('Register')
    window.geometry('300x300')
    
    
    email_label = Label(register_frame, text='E-Mail').grid(column=0, row=0)
    email_entry = Entry(register_frame, textvariable=reg_email).grid(column=1, row=0, columnspan=2)
    retype_email_label = Label(register_frame, text='Retype E-Mail').grid(column=0, row=1)
    retype_email_entry = Entry(register_frame, textvariable=retype_email, validate='focusout', validatecommand=check_email).grid(column=1, row=1, columnspan=2)
    password_label = Label(register_frame, text='Password').grid(column=0, row=2)
    password_entry = Entry(register_frame, textvariable=reg_password, show='*').grid(column=1, row=2, columnspan=2)
    
    register_btn = Button(register_frame, text='Register').grid(column=1, row=3, pady=10)
    cancel_btn = Button(register_frame, text="Cancel").grid(column=2, row=3, pady=10)
    
    register_frame.pack()
    


# Login widgets
email_label = Label(frame, text='E-Mail').grid(column=0, row=0)
email_entry = Entry(frame, textvariable=log_email).grid(column=1, row=0, columnspan=2)
password_label = Label(frame, text='Password').grid(column=0, row=1)
password_entry = Entry(frame, textvariable=log_password, show='*').grid(column=1, row=1, columnspan=2)

# Buttons
login_btn = Button(frame, text='Login').grid(column=0, row=2,pady=10)
register_btn = Button(frame, text='Register', command=register_window).grid(column=1, row=2,pady=10)
cancel_btn = Button(frame, text='Cancel').grid(column=2, row=2,pady=10)



frame.pack()
root.mainloop()
