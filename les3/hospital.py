from tkinter import *

root = Tk()
root.geometry('300x200')
root.title("Hospital Login")

frame = Frame(root, pady=25)


def validate_email():
    email = email.get()
    retype_email = retype_email.get()
    
    if email == retype_email:
        return True
    
    else:
        return 'Email is not the same'

def register():
    with open('user.csv', 'w') as f:
        f.write(email, password)

# Registration Window
def register_window():
    window = Toplevel(root)
    register_frame = Frame(window,pady=25)
    window.title('Register')
    window.geometry('300x300')
    
    email = StringVar()
    retype_email = StringVar()
    password = StringVar() 
    
    email_label = Label(register_frame, text='E-Mail').grid(column=0, row=0)
    email_entry = Entry(register_frame, textvariable=email).grid(column=1, row=0, columnspan=2)
    retype_email_label = Label(register_frame, text='Retype E-Mail').grid(column=0, row=1)
    retype_email_entry = Entry(register_frame, textvariable=retype_email, validate="focusout", validatecommand=validate_email).grid(column=1, row=1, columnspan=2)
    password_label = Label(register_frame, text='Password').grid(column=0, row=2)
    password_entry = Entry(register_frame, textvariable=password, show='*').grid(column=1, row=2, columnspan=2)
    
    register_btn = Button(register_frame, text='Register', command=register).grid(column=1, row=3, pady=10)
    cancel_btn = Button(register_frame, text="Cancel").grid(column=2, row=3, pady=10)
    
    
    
    register_frame.pack()
    

# Text Variables
email = StringVar()
password = StringVar()

# Login widgets
email_label = Label(frame, text='E-Mail').grid(column=0, row=0)
email_entry = Entry(frame, textvariable=email).grid(column=1, row=0, columnspan=2)
password_label = Label(frame, text='Password').grid(column=0, row=1)
password_entry = Entry(frame, textvariable=password, show='*').grid(column=1, row=1, columnspan=2)

# Buttons
login_btn = Button(frame, text='Login').grid(column=0, row=2,pady=10)
register_btn = Button(frame, text='Register', command=register_window).grid(column=1, row=2,pady=10)
cancel_btn = Button(frame, text='Cancel').grid(column=2, row=2,pady=10)



frame.pack()
root.mainloop()
