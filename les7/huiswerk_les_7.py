import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Root
root = tk.Tk()
root.title("Huiswerk les 5 || NHA Software Developer")
root.geometry("800x800")
root.minsize(800, 800)

# Variabelen
# Login Variabelen
login_email = tk.StringVar()
login_wachtwoord = tk.StringVar()

# Registreer variabelen

email = tk.StringVar()
voornaam = tk.StringVar()
achternaam = tk.StringVar()
adres = tk.StringVar()
postcode = tk.StringVar()
land = tk.StringVar()

# Combobox Variabelen
db_list = []
naam_list = []

# Maak de database
try:
    sqlite_connection = sqlite3.connect("naw_gegevens.db")
    sqlite_create_adres_query = """
        CREATE TABLE IF NOT EXISTS `naw_gegevens` (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `voornaam` VARCHAR(45) NOT NULL,
            `achternaam` VARCHAR(45) NOT NULL,
            `adres` VARCHAR(45) NOT NULL,
            `postcode` VARCHAR(45) NOT NULL,
            `land` VARCHAR(45) NOT NULL,
            `email` VARCHAR(45) NOT NULL
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

# Functies


def insert_into_database():
    database_connection = sqlite3.connect("naw_gegevens.db")
    with database_connection:
        cursor = database_connection.cursor()
        cursor.execute(
            "INSERT INTO naw_gegevens (voornaam, achternaam, adres, postcode, land, email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
                voornaam.get(),
                achternaam.get(),
                adres.get(),
                postcode.get(),
                land.get(),
                email.get(),
            )
        )
        database_connection.commit()
        print("Entry Inserted in Database")


def get_data_from_database():
    global db_list
    db_list = []
    db_connection = sqlite3.connect("naw_gegevens.db")
    with db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM naw_gegevens")
        data = cursor.fetchall()
        for item in data:
            db_list.append(item)


def make_values_combobox():
    global db_list
    global naam_list
    get_data_from_database()
    naam_list = []

    for item in db_list:
        naam_list.append(f"{item[2]}")
    combobox_box["values"] = naam_list
    print("New Combobox Values Made")


def set_data():
    global db_list
    selected_value = combobox_box.get()
    for item in db_list:
        if item[2] == selected_value:
            voornaam.set(item[1])
            achternaam.set(item[2])
            adres.set(item[3])
            postcode.set(item[4])
            land.set(item[5])
            email.set(item[6])


def clear_data():
    """
    Functie voor de annuleer/clear button op het registratiescherm. Alle StringVar() worden op een lege string gezet
    """
    email.set("")
    voornaam.set("")
    achternaam.set("")
    adres.set("")
    postcode.set("")
    land.set("")


def check_is_email():
    if "@" and "." in email.get():
        return True
    else:
        messagebox.showerror(message="Geen geldige e-mailadres ingevoerd.")
        return True


# Inlog Window


def login_window():
    login_frame = tk.Toplevel(root)
    login_email_label = ttk.Label(login_frame, text="E-mail:")
    login_email_entry = ttk.Entry(login_frame)
    login_wachtwoord_label = ttk.Label(login_frame, text="Wachtwoord: ")
    login_wachtwoord_entry = ttk.Entry(login_frame)
    login_login_button = ttk.Button(login_frame, text="Login")
    login_cancel_button = ttk.Button(login_frame, text="Annuleer")

    # Inlog Frame Placement
    login_email_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
    login_email_entry.grid(row=0, column=1, pady=5, padx=5)
    login_wachtwoord_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
    login_wachtwoord_entry.grid(row=1, column=1, pady=5, padx=5)
    login_login_button.grid(row=2, column=0, pady=5, padx=5, sticky="e")
    login_cancel_button.grid(row=2, column=1, pady=5, padx=5, sticky="e")


# Registreer Window


def register_window():
    register_frame = tk.Toplevel(root)
    register_email_label = ttk.Label(register_frame, text="E-Mail:")
    register_email_entry = ttk.Entry(
        register_frame,
        textvariable=email,
        validate="focusout",
        validatecommand=check_is_email,
    )
    register_voornaam_label = ttk.Label(register_frame, text="Voornaam:")
    register_voornaam_entry = ttk.Entry(register_frame, textvariable=voornaam)
    register_achternaam_label = ttk.Label(register_frame, text="Achternaam:")
    register_achternaam_entry = ttk.Entry(
        register_frame, textvariable=achternaam)
    register_adres_label = ttk.Label(register_frame, text="Adres:")
    register_adres_entry = ttk.Entry(register_frame, textvariable=adres)
    register_postcode_label = ttk.Label(register_frame, text="Postcode:")
    register_postcode_entry = ttk.Entry(
        register_frame,
        textvariable=postcode,
    )
    register_land_label = ttk.Label(register_frame, text="Land:")
    register_land_entry = ttk.Entry(register_frame, textvariable=land)
    register_registreer_button = ttk.Button(
        register_frame, text="Registreer", command=insert_into_database
    )
    register_cancel_button = ttk.Button(
        register_frame, text="Annuleer / Clear", command=clear_data
    )

    # Register Frane Placement
    register_email_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")
    register_email_entry.grid(column=1, row=0, padx=5, pady=5)
    register_voornaam_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")
    register_voornaam_entry.grid(column=1, row=1, padx=5, pady=5)
    register_achternaam_label.grid(column=0, row=2, padx=5, pady=5, sticky="w")
    register_achternaam_entry.grid(column=1, row=2, padx=5, pady=5)
    register_adres_label.grid(column=0, row=3, padx=5, pady=5, sticky="w")
    register_adres_entry.grid(column=1, row=3, padx=5, pady=5)
    register_postcode_label.grid(column=0, row=4, padx=5, pady=5, sticky="w")
    register_postcode_entry.grid(column=1, row=4, padx=5, pady=5)
    register_land_label.grid(column=0, row=5, padx=5, pady=5, sticky="w")
    register_land_entry.grid(column=1, row=5, padx=5, pady=5)
    register_registreer_button.grid(
        column=0, row=6, padx=5, pady=5, sticky="e")
    register_cancel_button.grid(column=1, row=6, padx=5, pady=5, sticky="e")


# Ontvangst Scherm
start_frame = tk.Frame(root, relief="sunken", padx=10, pady=10,)
start_label = ttk.Label(start_frame, text="Welkom bij het ziekenhuis")
start_login_button = ttk.Button(
    start_frame, text="Login", command=login_window)
start_register_button = ttk.Button(
    start_frame, text="Registreer", command=register_window
)

# Ontvangst Scherm Placement
start_frame.pack(fill="x")
start_label.pack(side="left", padx=40, pady=20)
start_register_button.pack(side="right", padx=20, pady=20)
start_login_button.pack(side="right", padx=20, pady=20)

# Combobox Scherm
combobox_frame = tk.Frame(root)
combobox_label = ttk.Label(
    combobox_frame,
    text="Kies hier een gebruiker uit de database om de gegevens in het registreer veld te tonen.",
)
combobox_box = ttk.Combobox(
    combobox_frame, values=naam_list, postcommand=make_values_combobox
)
combobox_button = ttk.Button(combobox_frame, text="Get data", command=set_data)

# Combobox Placement
combobox_frame.pack()
combobox_label.pack()
combobox_box.pack(pady=10)
combobox_button.pack(pady=10)

# NAW-Gegevens Scherm
gegevens_frame = tk.Frame(root)
gegevens_email_label = ttk.Label(gegevens_frame, text="E-mail:")
gegevens_email_data = ttk.Label(gegevens_frame, textvariable=email)
gegevens_voornaam_label = ttk.Label(gegevens_frame, text="Voornaam:")
gegevens_voornaam_data = ttk.Label(gegevens_frame, textvariable=voornaam)
gegevens_achternaam_label = ttk.Label(gegevens_frame, text="Achternaam:")
gegevens_achternaam_data = ttk.Label(gegevens_frame, textvariable=achternaam)
gegevens_adres_label = ttk.Label(gegevens_frame, text="Adres:")
gegevens_adres_data = ttk.Label(gegevens_frame, textvariable=adres)
gegevens_postcode_label = ttk.Label(gegevens_frame, text="Postcode:")
gegevens_postcode_data = ttk.Label(gegevens_frame, textvariable=postcode)
gegevens_land_label = ttk.Label(gegevens_frame, text="Land:")
gegevens_land_data = ttk.Label(gegevens_frame, textvariable=land)


# NAW-Gegevens Placement
gegevens_frame.pack()
gegevens_email_label.grid(row=0, column=0, sticky="w")
gegevens_email_data.grid(row=0, column=1, sticky="w")
gegevens_voornaam_label.grid(row=1, column=0, sticky="w")
gegevens_voornaam_data.grid(row=1, column=1, sticky="w")
gegevens_achternaam_label.grid(row=2, column=0, sticky="w")
gegevens_achternaam_data.grid(row=2, column=1, sticky="w")
gegevens_adres_label.grid(row=3, column=0, sticky="w")
gegevens_adres_data.grid(row=3, column=1, sticky="w")
gegevens_postcode_label.grid(row=4, column=0, sticky="w")
gegevens_postcode_data.grid(row=4, column=1, sticky="w")
gegevens_land_label.grid(row=5, column=0, sticky="w")
gegevens_land_data.grid(row=5, column=1, sticky="w")


# Listbox Scherm

# De waardes voor in de listbox
lbo_aandoeningen = ['Leukemie', 'Jicht', 'Astma',
                    'Aambeien', 'Oost-Indisch Doof', 'Aanstelleritus']
lbo_artsen = ['Dr. van Bemmel', 'Dr. Njoo',
              'Mevr. de Vries', 'Dr. Jansen', 'Dr. Smit']


# Functie voor het selecteren van de waardes in de listbox en ook en plaatsen van de label onder de boxen als de waardes zijn geselecteerd.

def item_selected_aandoening(event):
    selected_indice = lbo_box_aandoeningen.curselection()
    for i in selected_indice:
        aandoening_string = lbo_aandoeningen[i]
    lbo_label_info_aandoening.config(
        text=f'voor een behandeling voor {aandoening_string}')


def item_selected_arts(event):
    selected_indice = lbo_box_artsen.curselection()
    for i in selected_indice:
        arts_string = lbo_artsen[i]
    lbo_label_info_arts.config(text=f'U heeft gekozen voor {arts_string}')


# Widgets voor de listbox
lbo_frame = tk.Frame(root, padx=10, pady=10)
lbo_label_intro = tk.Label(
    lbo_frame, text='Kies hier uw aandoeningen en gewenste arts.')
lbo_box_aandoeningen = tk.Listbox(
    lbo_frame, height=10, selectmode='single', exportselection=0)
lbo_box_artsen = tk.Listbox(
    lbo_frame, height=10, selectmode='single', exportselection=0)
lbo_label_info_aandoening = tk.Label(
    lbo_frame, text='')
lbo_label_info_arts = tk.Label(
    lbo_frame, text='')

# Event Binding voor de listboxen
lbo_box_aandoeningen.bind('<<ListboxSelect>>', item_selected_aandoening)
lbo_box_artsen.bind('<<ListboxSelect>>', item_selected_arts)

# Vul de boxen met de waardes u de lists
i = 0
for aandoening in lbo_aandoeningen:
    lbo_box_aandoeningen.insert(i, aandoening)
    i += 1

i = 0
for arts in lbo_artsen:
    lbo_box_artsen.insert(i, arts)
    i += 1

#  Placement op het scherm voor de listbox
lbo_frame.pack(pady=10)
lbo_label_intro.grid(row=0, column=0)
lbo_box_aandoeningen.grid(row=1, column=0, sticky='w')
lbo_box_artsen.grid(row=1, column=1, sticky='w')
lbo_label_info_arts.grid(row=2, column=0, sticky='e', pady=10)
lbo_label_info_aandoening.grid(row=2, column=1, sticky='w', pady=10)


# Radio Button.
rbo_frame = tk.Frame(root)
rbo_label_intro = tk.Label(
    rbo_frame, text="Die is een label voor de radiobutton.")


# Placement radio buttons
rbo_frame.pack()
rbo_label_intro.grid(row=0, column=0)


# Get data from database
get_data_from_database()

# Mainloop
root.mainloop()
