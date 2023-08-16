from tkinter import *

# Login Scherm
root = Tk()
root.title("Login")
user_name = StringVar()
name_label = Label(root, text="Username: ").grid(column=0, row=0)
name_entry = Entry(root, textvariable=user_name).grid(column=1, row=0)




root.mainloop()