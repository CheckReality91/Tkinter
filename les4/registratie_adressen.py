from tkinter import *
import sqlite3



# GUI init
root = Tk()
root.geometry("350x350")
root.title("Adressen Registratie")

# StringVar()
voornaam = StringVar()
achternaam = StringVar()
adres = StringVar()
postcode = StringVar()
land = StringVar()

# Make Database

try:
    sqlite_connection = sqlite3.connect('les5/NAW_gegevens_les5.db')
    sqlite_create_adres_query = """
        CREATE TABLE IF NOT EXISTS `adressen` (
            `id_adres` INTEGER PRIMARY KEY AUTOINCREMENT,
            `voornaam` VARCHAR(45) NOT NULL,
            `achternaam` VARCHAR(45) NOT NULL,
            `adres` VARCHAR(45) NOT NULL,
            `postcode` VARCHAR(45) NOT NULL,
            `land` VARCHAR(45) NOT NULL
        )"""
    cursor = sqlite_connection.cursor()
    print("Connected to database")
    cursor.execute(sqlite_create_adres_query)
    sqlite_connection.commit()
    print("Table Created")
    cursor.close()
except sqlite3.Error as error:
    print(f"Error while creating datatbase or table: {error}")
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Database connection is closed || Ready for input.")       

# Insert adres in database function
def insert_database():
    database_connection = sqlite3.connect('les4/adressen.db')
    with database_connection:
        cursor = database_connection.cursor()
        cursor.execute("INSERT INTO adressen (voornaam, achternaam, adres, postcode, land) VALUES ('{}', '{}', '{}', '{}', '{}')".format(voornaam.get(), achternaam.get(), adres.get(), postcode.get(), land.get()))
        database_connection.commit()
        print("Entry Inserted in Database")


# Labels
top_label = Label(root, text='Registereer uw adres', font=('bold', 20)).place(x=50, y=25)
voornaam_label = Label(root, text='Voornaam:', font=('bold', 10)).place(x=50, y=75)
achternaam_label = Label(root, text='Achternaam:', font=('bold', 10)).place(x=50, y=100)
adres_label = Label(root, text='Adres:', font=('bold', 10)).place(x=50, y=125)
postcode_label = Label(root, text='Postcode:', font=('bold', 10)).place(x=50, y=150)
land_label = Label(root, text='Land:', font=('bold', 10)).place(x=50, y=175)

# Entrys
voornaam_entry = Entry(root, textvariable=voornaam).place(x=150,y=75)
achternaam_entry = Entry(root, textvariable=achternaam).place(x=150,y=100)
adres_entry = Entry(root, textvariable=adres).place(x=150,y=125)
postcode_entry = Entry(root, textvariable=postcode).place(x=150,y=150)
land_entry = Entry(root, textvariable=land ).place(x=150,y=175)

submit_button = Button(root, text='Submit', command=insert_database, width=30).place(x=50, y=200)


root.mainloop()
