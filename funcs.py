import random
import glob, os
import time
from pathlib import Path
import platform
"""Mostra el menu principal i recull l'opcio de l'usuari
@return option. Opcio desitjada
@since 5/12/2017
@version 1.1
@author Vesperon51"""
def menu():
    print("Benvingut")
    print("1. Jugar partida")
    print("2. Historic de partides")
    print("3. Establir dificultat")
    print("4. Carregar fitxer de configuracio")
    print("5. Guardar configuracio actual")
    print("6. Cambiar mode de joc")
    print("7. Guardar estadistiques i sortir")
    option = input("Selecciona l'opcio: ")
    return option
"""Mostra el sub menu del mode de joc i recull l'opcio de l'usuari
@return option. Opcio desitjada
@since 17/12/2017
@version 1.0
@author Vesperon51"""
def subMenu():
    print("Selecciona el nou mode de joc")
    print("1. Activar/desactivar repeticions de color")
    print("2. Activar/desactivar lletres")
    print("3. Activar/desactivar numeros")
    print("4. Tornar al menu principal")
    subOption= input("Selecciona l'opcio: ")
    return subOption


"""Determina si un numero esta a una llista
Si el numero generat es repetit torna a generar un numero aleatori i "destrueix" el numero repetit
@param j. La quantitat de numeros que vols a la llista
@param maxRange. El rang maxim de generacio d'aleatoris
@return randNum. Llista amb numeros aleatoris diferents
@since 10/12/2017
@version 1.1
@author Vesperon51"""
def generarCodi(j, maxRange):
    i=0
    randNum=[]
    while i<int (j):
        num=generarRandom(maxRange)
        if not num in randNum:
            randNum.append(num)
            i=i+1
    return randNum
"""Introdueix numeros aleatoris a una llista independentment si estan repetits
@param j. La quantitat de numeros que vols a la llista
@param maxRange. El rang maxim de generacio d'aleatoris
@return randNum. Llista amb numeros aleatoris
@since 17/12/2017
@version 1.1
@author Vesperon51"""
def generarCodiRepeticions(j, maxRange):
    i=0
    randNum=[]
    while i<int (j):
        num=generarRandom(maxRange)
        randNum.append(num)
        i=i+1
    return randNum
    

"""Genera un numero aleatori
@num. El numero aleatori generat
@param maxRange. El rang maxim de generacio d'aleatoris
@since 10/12/2017
@version 1.0
@author Vesperon51"""
def generarRandom (maxRange):
    num=random.randint(1,maxRange)
    return num


"""Asigna un numero a un color
@param randNum. Llista amb numeros
@return randCode. Llista de colors
@since 10/12/2017
@version 1.0
@author Vesperon51"""
def desxifrarCodi(randNum):
    randCode=[]
    for w in randNum:
        if w==1:
            randCode.append("blau")
        elif w==2:
            randCode.append("vermell")
        elif w==3:
            randCode.append("verd")
        elif w==4:
            randCode.append("groc")
        elif w==5:
            randCode.append("rosa")
        elif w==6:
            randCode.append("lila")
        elif w==7:
            randCode.append("negre")
        elif w==8:
            randCode.append("blanc")
        elif w==9:
            randCode.append("turquesa")
        elif w==10:
            randCode.append("marro")
        elif w==11:
            randCode.append("daurat")
        elif w==12:
            randCode.append("carmesi")
        elif w==13:
            randCode.append("mari")
        elif w==14:
            randCode.append("cobre")
        elif w==15:
            randCode.append("coral")
    return randCode

"""Asigna un numero a una lletra
@param randNum. Llista amb numeros
@return randCode. Llista de colors
@since 17/12/2017
@version 1.0
@author Vesperon51"""
def desxifrarCodiLletres(randNum):
    randCode=[]
    for w in randNum:
        if w==1:
            randCode.append("a")
        elif w==2:
            randCode.append("b")
        elif w==3:
            randCode.append("c")
        elif w==4:
            randCode.append("d")
        elif w==5:
            randCode.append("e")
        elif w==6:
            randCode.append("f")
        elif w==7:
            randCode.append("g")
        elif w==8:
            randCode.append("h")
        elif w==9:
            randCode.append("i")
        elif w==10:
            randCode.append("j")
        elif w==11:
            randCode.append("k")
        elif w==12:
            randCode.append("l")
        elif w==13:
            randCode.append("m")
        elif w==14:
            randCode.append("n")
        elif w==16:
            randCode.append("o")
        elif w==17:
            randCode.append("p")
        elif w==18:
            randCode.append("q")
        elif w==19:
            randCode.append("r")
        elif w==20:
            randCode.append("s")
        elif w==21:
            randCode.append("t")
        elif w==22:
            randCode.append("u")
        elif w==23:
            randCode.append("v")
        elif w==24:
            randCode.append("w")
        elif w==25:
            randCode.append("x")
        elif w==26:
            randCode.append("y")
        elif w==27:
            randCode.append("z")
    return randCode


"""Determina si dues llistes son iguals
@param userCode. String amb el codi de l'usuari
@param IACode. Llista amb el codi de l'IA
@return True si son iguals, o False si no
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def sonIguals(userCode, IACode):
    userCode=userCode.split(";")
    for i in range(0,len(userCode)):
        if(userCode[i] != IACode[i]):
            return False
    return True

"""Compta els encerts entre dues llistes
@param userCode. String amb el codi de l'usuari
@param IACode. Llista amb el codi de l'IA
@return encerts. Total d'encerts
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def comptaEncerts(userCode, IACode):
    userCode=userCode.split(";")
    """print(len(userCode))
    print(len(IACode))
    time.sleep(5.5)"""
    encerts=0
    for i in range(0,len(IACode)):
        if(userCode[i] == IACode[i]):
            encerts=encerts+1
    return encerts

"""Determina si una llista conte un valor
@param userCode. String amb el codi de l'usuari
@param IACode. Llista amb el codi de l'IA
@return coincidencies. Numero de coincidencies trobades
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def comptaCoincidencies(userCode, IACode):
    userCode=userCode.split(";")
    coincidencies=0
    for i in range(0,len(IACode)):
        if userCode[i] in IACode:
            coincidencies=coincidencies+1
    return coincidencies
"""Comprova que el codi de l'usuari sigui correcte
@param userCode. El codi de l'usuari
@param IACode. El codi de la IA
@return True si el codi es correcte o fals si no ho es
@since 10/12/2017
@version 1.0
@author Vesperon51"""
def esFormatCorrecte(userCode, IACode):
    code=[]
    if ';' in userCode:                 #TODO write a good REGEX for checking
        code=userCode.split(";")
        if len(code)==len(IACode):
            return True
    else:
        return False


"""Controla la partida fent les invocacions pertinents
es surt de la partida si les dues llistes son iguals o si s'esgoten  els intents
@param settings. Llista amb la configuracio de la partida(mida del codi[0], intents disponibles[1])
@param repeatMode. Boolea que determina si el mode repeticio esta activat
@param lettersMode. Boolea que determina si el mode lletres esta activat
@param numMode. Boolea que determina si el mode numero esta activat
@since 11/12/2017
@version 1.4
@author Vesperon51"""
def partida(settings, repeatMode, lettersMode, numMode):
    if lettersMode:
        IACode=desxifrarCodiLletres(generarCodi(settings[0], 24))
    else:
        if repeatMode:
            IACode=desxifrarCodi(generarCodiRepeticions(settings[0], 15))
        elif numMode:
            IACode=generarCodi(settings[0], 8)
        else:
            IACode=desxifrarCodi(generarCodi(settings[0], 15))
    intents=0
    victoria=True
    while victoria and intents<int(settings[1]):
        print (IACode)#debug
        print ("Escriu el teu codi de llargada", settings[0])
        userCode = input("")
        if esFormatCorrecte(userCode, IACode):     
            if sonIguals(userCode, IACode):
                print("Has guanyat!!!!!")
                victoria=False                                          #Surt del loop
                return True
            else:
                print ("Numero d'encerts: ", comptaEncerts(userCode, IACode))
                print ("Numero de coincidencies: ", comptaCoincidencies(userCode, IACode))
                print ("Intents restants: ", (int(settings[1])-intents)-1)
                intents=intents+1
        else:
            print("Format o llargada no correcte")
        if intents==int(settings[1]):
            print("Has esgotat els intents i has perdut")
            return False


"""Introdueix la configuracio de la partida controlant que sigui correcte.
El codi ha de ser superior a 2 o menor igual a 8
Els intents han de ser superior o igual a 2
L'unica forma de sortir del loop es introduir be les dades
@param lettersMode. Boolea que determina si el mode lletres esta activat
@return settings. Llista amb la configuracio de la partida(mida del codi[0], intents disponibles[1])
@since 11/12/2017
@version 1.2
@author Vesperon51"""
def definirDif(lettersMode):
    settings=[]
    flag1=False
    flag2=False
    oport=0
    maxLength=8
    if lettersMode==True:               #Si el mode de lletres esta activat vol dir que el num maxim del codi es 24
        maxLength=24
    while True:
        print("Escriu la mida del codi minim:2 maxim:", maxLength)
        mida=input("")
        if int(mida)<=maxLength and int (mida)>=2:
            flag1=True
            oport=input("Escriu les oportunitats minim:2 : ")
            if int (oport)>=2:
                flag2=True
            else:
                print("Els intents han de ser 2 o mes de 2")
        else:
            print("La mida a de ser superior a 2 o menor-igual a",maxLength)
        
        if flag1 and flag2:
            settings.append(mida)
            settings.append(oport)
            return settings
        else:
            print("Els valors introduits no son correctes")

"""Mostra les estadistiques
@param win. Partides guanyades
@param lost. Partides perdudes
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def estadistica(win,lost, total):
    print ("Partides guanyades: ", win)
    print ("Partides perdudes", lost)
    print ("Partides totals", total)
    saveStats(win, lost, total)


"""Guarda les estadistiques a un  fitxer
@param win. Partides guanyades
@param lost. Partides perdudes
@param total. Partides totals
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def saveStats(win, lost, total):
    myFile=open('stats.txt', 'w')
    cadena=(str(win)+";"+str(lost)+";"+str(total))
    myFile.write(cadena)
    myFile.close

"""Carrega les estadistiques d'un fitxer
@return stats. Llista amb les partides guanyades, perdudes i totals respectivament 
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def loadStats():
    my_File = Path("./stats.txt")                   #Ruta del fitxer, per determinar si existeix.
    if my_File.is_file():                           #Si aquesta comprovacio no existeix el programa falla en execucio perque intenta carregar i treballar amb un fitxer que no existeix
        print("Carregat correctament el fitxer d'estadistiques")
        myFile=open('stats.txt', 'r')
        stats=myFile.read().split(";")
        myFile.close
        return stats
    else:
        print("No hi ha cap fitxer d'estadistiques")


"""Carrega les settings d'un fitxer. L'usuari decideix quin fitxer vol
@param cfgFile. L'arxiu de que vol obrir
@return settings. Llista amb la configuracio
@since 11/12/2017
@version 1.2
@author Vesperon51"""
def loadSettings(cfgFile):
    option=0
    pth="./configFiles/"+cfgFile+".txt"             #Genero la ruta al ficher. Directori actual/directori"configFiles"/L'arxiu que l'usuari demana + l'extensio txt
    my_File = Path(pth)                             #Ruta del fitxer, per determinar si existeix.
    if my_File.is_file():                           #Si aquesta comprovacio no existeix el programa falla en execucio perque intenta carregar i treballar amb un fitxer que no existeix
        print("Carregat correctament el fitxer de configuracio "+cfgFile)
        myFile=open(pth, 'r')                       #Obro l'arxiu amb la ruta genera previament emmagatzenada a la variable pth en mode lectura
        settings=myFile.read().split(";")
        myFile.close
        print ("Mida del codi: "+settings[0])       #Mostro la configuracio
        print ("Intents disponibles "+settings[1])
        if confirm():
            return settings
        else:
            print("No es carregara cap configuracio")
    else:
        print("No hi ha cap fitxer de configuracio")#Si el fitxer no existeix

"""Llista el directori de configuracio
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def listDir():
    files = os.listdir('./configFiles')
    print (files)

"""Espera confirmacio
@return True si vol el fitxer
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def confirm():
    option = input ("Estas segur que vols carregar aquesta configuracio Si=1 No=0: ")
    if option=="1":                            
        return True
    else:
        return False

"""Guarda les settings a un fitxer. L'usuari decideix quin nom te el fitxer
@param settings. Llista amb la configuracio
@param cfgFile. L'arxiu de que vol obrir
@return True. Si s'ha guardat correctament. Fals si no
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def generarConfig(settings, cfgFile):
    option=0
    pth="./configFiles/"+cfgFile+".txt"             #Genero la ruta al ficher. Directori actual/directori"configFiles"/L'arxiu que l'usuari demana + l'extensio txt
    my_File = Path(pth)                             #Ruta del fitxer, per determinar si existeix.
    if my_File.is_file():                           #Si aquesta comprovacio no existeix el programa falla en execucio perque intenta carregar i treballar amb un fitxer que no existeix
        return False
    else:
        myFile=open(pth, 'w')
        cadena=(str(settings[0])+";"+str(settings[1]))
        myFile.write(cadena)
        myFile.close
        return True
"""Determina quin sistema operatiu s'esta executant i llença l'ordre de netejar pantalla adient
@since 17/12/2017
@version 1.0
@author Vesperon51"""
def clearScreen():
    if platform.system()=="Windows":
        os.system('cls')
    if platform.system()=="Linux":
        os.system("clear")
