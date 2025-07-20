import tkinter as tk

# Make root
root = tk.Tk()
root.title('NHA les 8 / Menubar')
root.geometry('600x300')

def doe_niks() :
    filewin = tk.Toplevel(root)
    button = tk.Button(filewin, text='Dit doet niks')
    button.pack(padx=20, pady=20)
    

# Menubar
menubar = tk.Menu(root, tearoff=0)

# Filemenu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=doe_niks)
filemenu.add_command(label="Open", command=doe_niks)
filemenu.add_command(label="Save", command=doe_niks)
filemenu.add_command(label="Save as...", command=doe_niks)
filemenu.add_command(label="Quit", command=root.quit)

# Edit menu
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label='Edit text', command=doe_niks)
editmenu.add_command(label='')




# add cascades
menubar.add_cascade(label='Bestand', menu=filemenu)



root.config(menu=menubar)
root.mainloop()