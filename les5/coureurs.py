import tkinter as tk
from tkinter import ttk
from bestand_inlezen import inlezen


namen = []

def inlezen_bestand():
    global namen
    cbo_coureurs.delete(0, END)
    namen = inlezen('patienten.reg')
    for naam in namen:
        coureurs.append(naam)

def change_coureurs():
    cbo_coureurs['values'] = ['Niki Lauda',
                    'Maria Andretti',
                    'Emerson Fitipaldi',
                    'Juan Manuel Fangio',
                    'Jos Verstappen']

    

coureurs = ['Max Verstappen',
            'Lando Norris',
            'Alexander Albon',
            'Lewis Hamilton',
            'Carlos Sainz']

root = tk.Tk()
root.title('Coureurs')
root.geometry('400x400')

vraag_label = ttk.Label(root, text='Kies uw favoriete coureur')
vraag_label.grid(column=0, row=0)

str_coureur = tk.StringVar()
print(str_coureur)

cbo_coureurs = ttk.Combobox(root, values=coureurs, textvariable=str_coureur, postcommand=change_coureurs)

cbo_coureurs.grid(column=0, row=1)
cbo_coureurs.current(0)


coureur_label = ttk.Label(root, textvariable=str_coureur)
coureur_label.grid(column=0, row=2)

button = ttk.Button(root, text='For the clicks').grid(column=0, row=3)

print(str_coureur)
# Mainloop
root.mainloop()

