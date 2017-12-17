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
subMenuController=True
#Booleans que controlen quin mode es juga
repeatMode=False
lettersMode=False
numMode=False
subOption=0                 #Variable que controla el submenu de mode de joc
settings=[]
while option != "7":
    if repeatMode:
        print("Mode de repeticio activat")
    if lettersMode:
        print("Mode de lletres activat")
    if numMode:
        print("Mode de numeros activat")
    if repeatMode==False and numMode==False and lettersMode==False:
        print("Mode normal activat")
    option=menu()
    subMenuController=True
    if option == "1":
        print("Nou joc")
        if not settings:                            #Si intenta jugar sense establir una dificultat
            print("Estableix abans dificultat")
        else:
            clearScreen()
            if partida(settings, repeatMode, lettersMode, numMode):
                partWin=int(partWin)+1
                partTot=int(partTot)+1                   #Si es determina la variable partTot com a resultat de victories+derrotes l'escripura al fitxer falla, coses del Python
            else:
                partLost=int(partLost)+1
                partTot=int(partTot)+1
    elif option == "2":
        estadistica(partWin, partLost, partTot)     #Mostra les stats i les salva al fitxer stats.txt al mateix directori
    elif option == "3":
        clearScreen()
        settings=definirDif(lettersMode)                       #Obligatori definir dificultat abans de jugar
    elif option == "7":                             
        saveStats(partWin, partLost, partTot)
        print("Adeu!")
    elif option == "4":
        clearScreen()
        listDir()
        cfgFile=input("Selecciona el fitxer que vols carregar: ")
        cfg=loadSettings(cfgFile)                   #Emmagatzemo a la llista cfg la config o el 0
        if cfg:                                     #Si la llista te cotingut significa que SI que carrega la config
            settings=cfg                            #Igualo la llista settings a cfg per poder carregar la configuracio a la partida i poder iniciar el joc
    elif option=="5":
        if not settings:
            clearScreen()
            print("No hi ha cap configuracio definida")
        else:
            clearScreen()
            if lettersMode:                         #Si s'esta amb un mode extra no es pot guardar la config per evitar errors
                print("No pots guardar la configuracio si estas en un mode extra")
            else:
                configName=input("Escriu el nom de la teva configuracio: ")
                if generarConfig(settings, configName):
                    print("La configuracio s'ha guardat correctament")
                else:
                    print("Error en guardar la configuracio. El fitxer ja existeix")
    elif option=="6":
        clearScreen()
        while subOption!="4" and subMenuController:     #Nomes es pot tenir un mode extra activat a la vegada
            subOption=subMenu()
            settings=[]                                 #Reinicia les settings per evitar errors
            if subOption=="1":                          #Repeat mode
                if repeatMode:
                    repeatMode=False
                    lettersMode=False
                else:
                    repeatMode=True
                    lettersMode=False
                subMenuController=False
            elif subOption=="2":                        #Letters mode
                if lettersMode:
                    lettersMode=False
                    repeatMode=False
                else:
                    repeatMode=False
                    lettersMode=True
                subMenuController=False
            elif subOption=="3":                        #Numb mode
                if numMode:
                    numMode=False
                    repeatMode=False
                    lettersMode=False
                else:
                    numMode=True
                    repeatMode=False
                    lettersMode=False
                subMenuController=False
            elif subOption=="4":
                print("Tornant al menu principal")
                subMenuController=False
            else:
                print("Selecciona una opcio correcte")
    else:
        print("Escriu una opcio adequada")
