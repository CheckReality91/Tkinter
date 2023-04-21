from tkinter import *

root = Tk()
root.geometry("1024x768")
label = Label(root, text='Dit is een label')
label.pack()
frame = Frame(root, bg="blue", bd=40)
frame.pack()

frame_mid = Frame(root, bg='green', bd=60)
frame_mid.pack()


label = Label(frame, text="Dit is mijn eerste tkinter GUI programma")
label.pack()

button1 = Button(frame_mid, text='Dit is een knop!')
button1.pack()

leftframe = Frame(root, bg='red',bd=50)
leftframe.pack(side=LEFT)

button2 = Button(leftframe, text="Dit is de linkerkant")
button2.pack()

rightframe = Frame(root, bg="white", bd=50)
rightframe.pack(side=RIGHT)

button3 = Button(rightframe, text='Deze knop zit rechts')
button3.pack()

root.title("Mijn eerste tkinter gui app.")
root.mainloop()