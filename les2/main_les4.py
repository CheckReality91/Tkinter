from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Ik leer Python GUI maken bij NHA")
root.geometry("640x480")

def create_db():
    try:
        sqliteConnection = sqlite3.connect('les2\database.db')
        sqlite_create_persoon_query = """
            CREATE TABLE IF NOT EXISTS `persoon` (
                `idpersoon` INTEGER PRIMARY KEY AUTOINCREMENT
                `voornaam` VARCHAR(45) NOT NULL,
                `tussenvoegsel` VARCHAR(45) NULL,
                `achternaam` VARCHAR(45) NOT NULL,
                `mobiel` VARCHAR(45) NOT NULL
            );
            """
        sqlite_create_adres_query = """
            CREATE TABLE IF NOT EXISTS `adres` (
                `idadres` INTEGER PRIMARY AUTOINCREMENT,
                `straat` VARCHAR(45) NOT NULL,
                `huisnr` VARCHAR(45) NOT NULL,
                `postcode` VARCHAR(45) NOT NULL,
                `woonplaats` VARCHAR(45) NOT NULL,
                `idpersoon` INTEGER NOT NULL
            );
            """
        cursor = sqliteConnection.cursor()
        print('Succesfully Connected to SQLite')
        cursor.execute(sqlite_create_persoon_query)
        cursor.execute(sqlite_create_adres_query)
        sqliteConnection.commit()
        print("SQLite table created")
        
        cursor.close()
        
    except sqlite3.Error as error:
        return f"Error while creating a sqlite table {error}"
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return "sqlite connection is closed"


def show_message():
    gelukt_db = create_db()
    messagebox.showinfo("SQLite database aangemaakt", gelukt_db)
    
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

