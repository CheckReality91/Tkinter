import tkinter as tk
from tkinter import filedialog

# Make root
root = tk.Tk()
root.title('NHA les 8 / Menubar')
root.geometry('600x300')

### Functions

def make_empty_mockup_screen() :
    # Dit maakt een Toplevel scherm met een knop die niks doet.
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text='Dit doet niks, maar wel leuk dat je op mij wil klikken')
    button.pack(padx=40, pady=40)

def write_file():
    # Write to a file
    path_to_save = filedialog.asksaveasfilename(defaultextension='.txt')
    content = textfield.get("1.0", tk.END)
    with open(path_to_save, 'w') as file:
        file.write(content)
    
    # De data uit en entryfield moet gepakt worden
    # Er moet een manier komen om een andere bestandsnaam te geven zodat er meerdere bestand gemaakt kunnen worden.
    print('Doet nog niks')

def open_file() :
    # opent een tekstbestand
    file_to_open = filedialog.askopenfilename() # Hier krijg ik de filename. Die kan ik daarna gebruiken om te openen naar het entryfield.
    #check of het een .txt file is.
    if file_to_open[-4:] == ".txt":
        # Open het bestand en zet het in de Text widget
        file = open(file_to_open)
        textfield.insert('1.0', file.read())
    else:
        print('Er is geen .txt bestand geslecteerd')
    
def menu_maker() :

    

    ### Makes the menu
    # Menubar
    menubar = tk.Menu(root, tearoff=0)

    # Filemenu
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=make_empty_mockup_screen)
    filemenu.add_command(label="Open", command=open_file) # Wat moet ik met de data doen als ik het open?
    filemenu.add_command(label="Save", command=write_file)
    filemenu.add_command(label="Save as...", command=write_file)
    filemenu.add_command(label="Quit", command=root.quit)

    # Edit menu
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label='Undo', command=make_empty_mockup_screen)
    editmenu.add_command(label='Redo', command=make_empty_mockup_screen)
    editmenu.add_separator()
    editmenu.add_command(label='Copy', command=make_empty_mockup_screen)
    editmenu.add_command(label='Cut', command=make_empty_mockup_screen)
    editmenu.add_command(label='Past', command=make_empty_mockup_screen)
    editmenu.add_command(label='Delete', command=make_empty_mockup_screen)
    editmenu.add_command(label='Select All', command=make_empty_mockup_screen)
    editmenu.add_command(label='Deselect All', command=make_empty_mockup_screen)

    # Help menu
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Info", command=make_empty_mockup_screen)
    helpmenu.add_command(label="Info", command=make_empty_mockup_screen)

    # add cascades
    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Edit', menu=editmenu)
    menubar.add_cascade(label='Help', menu=helpmenu)
    
    #configure the menu
    root.config(menu=menubar)

#Entryfield
textfield = tk.Text()
textfield.pack()

menu_maker()
root.mainloop()