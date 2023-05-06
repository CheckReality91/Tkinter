from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hospital System')
root.geometry('500x500')

LOGGED_IN = False

ACTIVE_USER = []

main_frame = Frame(root).pack()



# Login page
def login_page():
    login_window = Toplevel(root)
    login_window.geometry("300x150")
    login_window.title("Login")
    
    login_frame = Frame(login_window)

    # Variables for names
    email = StringVar()
    password = StringVar()


    # Entry Fields
    label_email = Label(login_frame, text='E-Mail: ').grid(column=0, row=0, pady=5)
    entry_email = Entry(login_frame, textvariable=email).grid(column=1, row=0,pady=5)
    label_password = Label(login_frame, text='Password: ').grid(column=0, row=1, pady=5)
    entry_password = Entry(login_frame, show="*", textvariable=password).grid(column=1, row=1, pady=5)

    # Buttons
    btn_login = Button(login_frame, text="Login").grid(column=0, row=2)
    btn_register = Button(login_frame, text="Register", command=register_form).grid(column=1, row=2)
    btn_cancel = Button(login_frame, text="Cancel").grid(column=2, row=2)
    
    login_frame.pack()

# Register page
def register_form():
    register_window = Toplevel(root)
    register_window.geometry('400x250')
    
    register_frame = Frame(register_window)
    
    email = StringVar()
    retype_email = StringVar()
    password = StringVar()


    # Entry Fields
    label_email = Label(register_frame, text='E-Mail: ').grid(column=0, row=0, pady=5)
    entry_email = Entry(register_frame, textvariable=email).grid(column=1, row=0,pady=5)
    label_retype_email = Label(register_frame, text='Retype E-Mail: ').grid(column=0, row=1, pady=5)
    entry_retype_email = Entry(register_frame, textvariable=retype_email).grid(column=1, row=1, pady=5)
    label_password = Label(register_frame, text='Password: ').grid(column=0, row=2, pady=5)
    entry_password = Entry(register_frame, show="*", textvariable=password).grid(column=1, row=2, pady=5)

    # Buttons
    btn_register = Button(register_frame, text="Register", command=check_registration).grid(column=0, row=3)
    btn_cancel = Button(register_frame, text="Cancel").grid(column=1, row=3)

    register_frame.pack()
    
    
    
    
def check_registration():
    print(email)
    print(retype_email)



        

if LOGGED_IN == False:
    main_label = Label(main_frame, text='Je bent nog niet ingelogd. Klik hieronder om in te loggen').pack()
    login_btn = Button(main_frame, text='Login', command=login_page).pack()
    
if LOGGED_IN == True:
    main_label = Label(main_frame, text='Je bent ingelogd. Hier komt nog meer functionaliteit').pack()


root.mainloop()




