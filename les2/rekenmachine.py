from tkinter import *

root = Tk()

# Functions
def on_click(item):
    # Voegt de waarde van de button aan de entry field toe als er op geklickt wordt
    lenght = len(entry_field.get())
    entry_field.insert(lenght, item)
    
def make_calculation():
    # Als het = teken wordt aangeklikt worden de waardes in een lijst gezet
    lst = entry_field.get().split() # maakt een lijst met de waardes op index 0, 1, 2
    num1 = int(lst[0]) # waarde 1
    num2 = int(lst[2]) # waarde 2
    
    # op index 1 van lst staat welk rekenteken er gebruikt moet worden. 
    if lst[1] == '+': 
        uitkomst['text'] = "Uitkomst: " + str(num1 + num2)
    elif lst[1] == '-':
        uitkomst['text'] = "Uitkomst: " + str(num1 - num2)
    elif lst[1] == '*':
        uitkomst['text'] = "Uitkomst: " + str(num1 * num2)
    elif lst[1] == '/':
        uitkomst['text'] = "Uitkomst: " + str(num1 / num2)
        
def clear():
    # maakt de entry_field leeg. En ookde uitkomst label
    entry_field.delete(0, END)
    uitkomst['text'] = "Uitkomst: "
    
title = Label(root, text="Dit is een rekenmachine")
title.grid()

entry_field = Entry(root)
entry_field.grid()

uitkomst = Label(root, text='Uitkomst: ')
uitkomst.grid()

btn_frame = Frame(root, bd=4)
btn_frame.grid()

# buttons nummers
btn_1 = Button(btn_frame, text='1', width=10, bd=5, command=lambda: on_click('1'))
btn_2 = Button(btn_frame, text='2', width=10, bd=5, command=lambda: on_click('2'))
btn_3 = Button(btn_frame, text='3', width=10, bd=5, command=lambda: on_click('3'))
btn_4 = Button(btn_frame, text='4', width=10, bd=5, command=lambda: on_click('4'))
btn_5 = Button(btn_frame, text='5', width=10, bd=5, command=lambda: on_click('5'))
btn_6 = Button(btn_frame, text='6', width=10, bd=5, command=lambda: on_click('6'))
btn_7 = Button(btn_frame, text='7', width=10, bd=5, command=lambda: on_click('7'))
btn_8 = Button(btn_frame, text='8', width=10, bd=5, command=lambda: on_click('8'))
btn_9 = Button(btn_frame, text='9', width=10, bd=5, command=lambda: on_click('9'))
btn_0 = Button(btn_frame, text='0', width=10, bd=5, command=lambda: on_click('0'))
# buttons rekentekens
btn_plus = Button(btn_frame, text='+', width=10, bd=5, command=lambda: on_click(' + '))
btn_min = Button(btn_frame, text='-', width=10, bd=5, command=lambda: on_click(' - '))
btn_keer = Button(btn_frame, text='x', width=10, bd=5, command=lambda: on_click(' * '))
btn_gedeeld = Button(btn_frame, text='/', width=10, bd=5, command=lambda: on_click(' / '))
# = teken
btn_uitkomst = Button(btn_frame, text='=', width=10, bd=5, command=make_calculation)
# Clear entryfield
btn_clear = Button(btn_frame, text="CE", width=10, bd=5, command=clear)

# hier wordt alles op het scherm gezet
btn_1.grid(column=0, row=4)
btn_2.grid(column=1, row=4)
btn_3.grid(column=2, row=4)
btn_4.grid(column=0, row=5)
btn_5.grid(column=1, row=5)
btn_6.grid(column=2, row=5)
btn_7.grid(column=0, row=6)
btn_8.grid(column=1, row=6)
btn_9.grid(column=2, row=6)
btn_0.grid(column=1, row=7)
btn_plus.grid(column=3, row=4)
btn_min.grid(column=3, row=5)
btn_keer.grid(column=3, row=6)
btn_gedeeld.grid(column=3, row=7)
btn_uitkomst.grid(column=2, row=7)
btn_clear.grid(column=0, row=7)

#mainloop
root.title("Rekenmachine Les 2")
root.mainloop()