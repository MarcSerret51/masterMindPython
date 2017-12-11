import random
import time
from pathlib import Path
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
    print("4. Sortir")
    option = input("Selecciona l'opcio: ")
    return option


"""Determina si un numero esta a una llista
Si el numero generat es repetit torna a generar un numero aleatori i "destrueix" el numero repetit
@param j. La quantitat de numeros que vols a la llista
@return randNum. Llista amb numeros aleatoris diferents
@since 10/12/2017
@version 1.0
@author Vesperon51"""
def generarCodi(j):
    i=0
    randNum=[]
    while i<int (j):
        num=generarRandom()
        if not num in randNum:
            randNum.append(num)
            i=i+1
    return randNum
    

"""Genera un numero aleatori
@num. El numero aleatori generat
@since 10/12/2017
@version 1.0
@author Vesperon51"""
def generarRandom ():
    num=random.randint(1,15)
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
@return True si el codi es correcte o fals si no ho esa
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
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def partida(settings):
    IACode=desxifrarCodi(generarCodi(settings[0]))
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
@return settings. Llista amb la configuracio de la partida(mida del codi[0], intents disponibles[1])
@since 11/12/2017
@version 1.0
@author Vesperon51"""
def definirDif():
    settings=[]
    flag1=False
    flag2=False
    while True:
        mida=input("Escriu la mida del codi: ")
        if mida<="8" and mida>="2":
            flag1=True
        else:
            print("La mida a de ser superior a 2 o menor-igual a 8")
        oport=input("Escriu les oportunitats: ")
        if oport>="2":
            flag2=True
        else:
            print("Els intents han de ser 2 o mes de 2")
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
    if my_File.is_file():                           #Si aquesta comprovacio no existeix el programa falla en execució perque intenta carregar i treballar amb un fitxer que no existeix
        print("Carregat correctament el fitxer d'estadistiques")
        myFile=open('stats.txt', 'r')
        stats=myFile.read().split(";")
        myFile.close
        return stats
    else:
        print("No hi ha cap fitxer d'estadistiques")    