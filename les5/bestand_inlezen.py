achternaam = []

def inlezen(bestand):
    global achternaam
    regels = []
    
    with open(bestand) as f:
        regels.append(f.readline())
        
    for regel in regels:
        for persoonsgegevens in regel:
            achternaam.append(persoonsgegevens.split(',')[0])
            print(achternaam)
            
            
    return achternaam