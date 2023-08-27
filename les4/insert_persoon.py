import sqlite3
from tkinter import *




# Insert peroon
def insert_persoon():
    try:
        sqliteConnection = sqlite3.connect('les4/SQLite_Python.db')
        insert_persoon_query = """ 
            INSERT INTO PERSOON (voornaam, tussenvoegsel, achternaam, mobiel) values ('jan', '', jansen', '0612345678');"""
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")
        cursor.execute(insert_persoon_query)
        sqliteConnection.commit()
        print('Persoon ingevoerd')
        
        cursor.close()
    
    except sqlite3.Error as error:
        print(f"Persoon niet ingevoerd :/n {error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return "sqlite connection is closed"
        
        
# Maak de database en maak een connectie
try:
    sqliteConnection = sqlite3.connect('les4/SQLite_Python.db')
    sqlite_create_persoon_query = '''
        CREATE TABLE IF NOT EXISTS `persoon` (
            `idpersoon` INTEGER PRIMARY KEY AUTOINCREMENT,
            `voornaam` VARCHAR(45) NOT NULL,
            `tussenvoegsel` VARCHAR(45) NULL,
            `achternaam` VARCHAR(45) NOT NULL,
            `mobiel` VARCHAR(23) NOT NULL
        );
    '''
    
    sqlite_create_adres_query = """
        CREATE TABLE IF NOT EXISTS `adres` (
            `idadres` INTEGER PRIMARY KEY AUTOINCREMENT,
            `straat` VARCHAR(45) NOT NULL,
            `huisnr` VARCHAR(45) NOT NULL,
            `postcode` VARCHAR(45) NOT NULL,
            `woonplaats` VARCHAR(45) NOT NULL,
            `idpersoon` INTEGER NOT NULL
        );
    """
    
    cursor = sqliteConnection.cursor()
    print('Database created and Succesfully Connected to SQLite')
    
    cursor.execute(sqlite_create_persoon_query)
    cursor.execute(sqlite_create_adres_query)
    sqliteConnection.commit()
    print("SQLite table created")
    
    cursor.close()
    
except sqlite3.Error as error:
    print('Error while connecting to sqlite', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('The SQlite connection is closed')
        
# Insert Persoon in database    
def database():
    conn = sqlite3.connect('les4/SQLite_Python.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO persoon (voornaam, tussenvoegsel, achternaam, mobiel) VALUES ('{}', '{}', '{}', '{}')".format(voornaam.get(), tussenvoegsel.get(), achternaam.get(), mobiel.get()))
        conn.commit()
        
# GUI Scherm
root = Tk()
root.geometry('500x300')
root.title('Registration Form')

# Variables
voornaam = StringVar()
tussenvoegsel = StringVar()
achternaam = StringVar()
mobiel = StringVar()

        
reg_label = Label(root, text='Registration Form', width=20, font=("bold", 20))
reg_label.place(x=90, y=53)

voornaam_label = Label(root, text='Voornaam', width=20, font=('bold', 10))
voornaam_label.place(x=68, y=130)

voornaam_entry = Entry(root, textvar=voornaam)
voornaam_entry.place(x=240, y=130)

tussenvoegsel_label = Label(root, text='Tussenvoegsel', width=20, font=('bold', 10))
tussenvoegsel_label.place(x=68, y=160)

tussenvoegsel_entry = Entry(root, textvar=tussenvoegsel)
tussenvoegsel_entry.place(x=240, y=160)

achternaam_label = Label(root, text='Achternaam', width=20, font=('bold', 10))
achternaam_label.place(x=68, y=190)

achternaam_entry = Entry(root, textvar=achternaam)
achternaam_entry.place(x=240, y=190)

mobiel_label = Label(root, text='Mobiel', width=20, font=('bold', 10))
mobiel_label.place(x=68, y=220)

mobiel_entry = Entry(root, textvar=mobiel)
mobiel_entry.place(x=240, y=220)

Button(root, text='Submit', width=20, bg='brown', fg='black', command=database).place(x=180, y=250)


root.mainloop()