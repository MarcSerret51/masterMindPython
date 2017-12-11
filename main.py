from funcs import *
stats=loadStats()           #Carrega el fitxer stats
cfg=[]
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
while option != "6":
    option=menu()
    if option == "1":
        print("Nou joc")
        if not settings:                            #Si intenta jugar sense establir una dificultat
            print("Estableix abans dificultat")
        else:
            if partida(settings):
                partWin=int(partWin)+1
                partTot=int(partTot)+1                   #Si es determina la variable partTot com a resultat de victories+derrotes l'escripura al fitxer falla, coses del Python
            else:
                partLost=int(partLost)+1
                partTot=int(partTot)+1
    elif option == "2":
        print("Visualitza i guarda les estadistiques")
        estadistica(partWin, partLost, partTot)     #Mostra les stats i les salva al fitxer stats.txt al mateix directori
    elif option == "3":
        print("Dificultat")
        settings=definirDif()                       #Obligatori definir dificultat abans de jugar
    elif option == "6":                             
        saveStats(partWin, partLost, partTot)
        print("Adeu!")
    elif option == "4":
        print("Carrega de configuracio")
        listDir()
        cfgFile=input("Selecciona el fitxer que vols carregar: ")
        cfg=loadSettings(cfgFile)                   #Emmagatzemo a la llista cfg la config o el 0
        if cfg:                                     #Si la llista te cotingut significa que SI que carrega la config
            settings=cfg                            #Igualo la llista settings a cfg per poder carregar la configuracio a la partida i poder iniciar el joc
    elif option=="5":
        if not settings:
            print("No hi ha cap configuracio definida")
        else:
            configName=input("Escriu el nom de la teva configuracio: ")
            if generarConfig(settings, configName):
                print("La configuracio s'ha guardat correctament")
            else:
                print("Error en guardar la configuracio. El fitxer ja existeix")
    else:
        print("Escriu una opcio adequada")
