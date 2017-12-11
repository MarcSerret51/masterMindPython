from funcs import *
stats=loadStats()           #Carrega el fitxer stats
if stats:                   #Si existex fitxer de stats
    partWin=stats[0]
    partLost=stats[1]
    partTot=stats[2]
else:                       #Si no s'inicien les variables a 0 per evitar errors en tems d'execucio
    partWin=0
    partLost=0
    partTot=0
option=0
settings=[]
while option != "4":
    option=menu()
    if option == "1":
        print("Nou joc")
        if not settings:                            #Si intenta jugar sense establir una dificultat
            print("Estableix abans dificultat")
        else:
            if partida(settings):
                partWin=partWin+1
                partTot=partTot+1                   #Si es determina la variable partTot com a resultat de victories+derrotes l'escripura al fitxer falla, coses del Python
            else:
                partLost=partLost+1
                partTot=partTot+1
    elif option == "2":
        print("Visualitza i guarda les estadistiques")
        estadistica(partWin, partLost, partTot)     #Mostra les stats i les salva al fitxer stats.txt al mateix directori
    elif option == "3":
        print("Dificultat")
        settings=definirDif()                       #Obligatori definir dificultat abans de jugar
    elif option == "4":                             #TODO Carregar dificultat d'un fitxer
        print("Adeu!")
    else:
        print("Escriu una opcio adequada")
