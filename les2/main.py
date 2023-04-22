from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ik leer Python GUI maken bij NHA")
root.geometry("640x480")

def show_message():
    messagebox.showinfo('Dit is het bericht', berichtje.get())
    
frame = Frame(root)
frame.pack()

berichtje = StringVar()
lbl_bericht = Label(frame, width=30, text="Type een bericht")
lbl_bericht.pack()
txt_bericht = Entry(frame, width=30, textvariable=berichtje)
txt_bericht.pack()
btn_show_berichtje = Button(frame, width=25, text="Laat berichtje zien", command=show_message)
btn_show_berichtje.pack()
root.mainloop()

