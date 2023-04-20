from tkinter import *

root = Tk()
root.geometry("1024x768")

frame = Frame(root)
frame = Frame(root, bd=5, bg='red')
frame.pack()

leftframe = Frame(root, bg='white', bd=3)
leftframe.pack(side=LEFT)

rightframe = Frame(root, bg='blue', bd=3)
rightframe.pack(side=RIGHT)

root.title("Ik leer python gui maken bij NHA")
root.mainloop()