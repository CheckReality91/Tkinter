from tkinter import *

root = Tk()
root.title("Rekenmachine 1")
root.geometry("400x200")

# Functions
def plus():
    num1 = int(number1.get())
    num2 = int(number2.get())
    sum = num1 + num2
    uitkomst['text'] = 'Uitkomst: ' + str(sum)

def min():
    num1 = int(number1.get())
    num2 = int(number2.get())
    sum = num1 - num2
    uitkomst['text'] = 'Uitkomst: ' + str(sum)
    
def keer():
    num1 = int(number1.get())
    num2 = int(number2.get())
    sum = num1 * num2
    uitkomst['text'] = 'Uitkomst: ' + str(sum)
    
def gedeeld():
    num1 = int(number1.get())
    num2 = int(number2.get())
    sum = num1 / num2
    uitkomst['text'] = 'Uitkomst: ' + str(sum)


frame = Frame(root)
frame.pack()

label1 = Label(frame, text="Getal 1: ")
label1.pack()
number1 = Entry(frame)
number1.pack()
label2 = Label(frame, text="Getal 2: ")
label2.pack()
number2 = Entry(frame)
number2.pack()


btn_plus = Button(frame, text="+", command = plus)
btn_min = Button(frame, text="-", command = min)
btn_keer = Button(frame, text="x", command = keer)
btn_gedeeld = Button(frame, text="/", command = gedeeld)
btn_plus.pack()
btn_min.pack()
btn_keer.pack()
btn_gedeeld.pack()

uitkomst = Label(frame, text="Uitkomst: ")
uitkomst.pack()

root.mainloop()