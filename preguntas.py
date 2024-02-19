"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import sys
import preguntas
from datetime import datetime

file=open("data.csv","r") #Obtengo el archivo y lo guardo en file
lines=file.readlines() #Lee el archivo y devuelve una lista
file.close()
data=[]
for line in lines:
    nline=line.replace("\n","")
    raw=nline.split("\t")
    raw[1]=int(raw[1])
    raw[2]=raw[2].split("-")
    raw[3]=raw[3].split(",")
    raw[4]=raw[4].split(",")
    data.append(raw) #Creando una lista de listas


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    i=0
    for raw in data:
        i=i+raw[1]
    return i

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    letras=list(dict.fromkeys(raw[0] for raw in data)) #manera fácil para filtrar y resulta en un diccionario
    letras=sorted(letras)

    pup=[]

    for letra in letras:
        count=0
        for raw in data:
            if raw[0]==letra:
                count=count+1
        
        pup.append((letra,count))

    return pup


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    letras=list(dict.fromkeys(raw[0] for raw in data))
    letras=sorted(letras)

    lista3=[]

    for letra in letras:
        suma=0
        for raw in data:
            if raw[0]==letra:
                suma=suma+raw[1]
        lista3.append((letra, suma))

    return lista3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    fechas=list(dict.fromkeys(raw[2][1] for raw in data)) #manera fácil para filtrar y resulta en un diccionario
    fechas=sorted(fechas)

    fech=[]

    for fecha in fechas:
        count=0
        for raw in data:
            if raw[2][1]==fecha:
                count=count+1
        
        fech.append((fecha,count))

    return fech


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    columnap5=list(dict.fromkeys(raw[0] for raw in data)) #manera fácil para filtrar y resulta en un diccionario
    columnap5=sorted(columnap5)

    column5=[]

    for columna in columnap5:
        nums=[int(raw[1]) for raw in data if raw[0]==columna]
        
        column5.append((columna,max(nums),min(nums)))

    
    return column5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    listakeys=[]
    for raw in data:
        for key in raw[4]:
            listakeys.append(key.split(":"))


    columnap6=list(dict.fromkeys(listakey[0] for listakey in listakeys)) #manera fácil para filtrar y resulta en un diccionario
    columnap6=sorted(columnap6)

    column6=[]

    for columna in columnap6:
        nums=[int(lk[1]) for lk in listakeys if lk[0]==columna]  #Se usa int para cambiar el tipo de dato de la lista que es un string
        column6.append((columna,min(nums),max(nums)))

    
    return column6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    numeros=list(dict.fromkeys(raw[1] for raw in data)) #manera fácil para filtrar y resulta en un diccionario
    numeros=sorted(numeros)

    
    lista=[]

    for numero in numeros:
        lista_letras=[]
        for raw in data:
            if raw[1]==numero:
                lista_letras.append(raw[0])
        
        lista.append((numero,lista_letras))
    
    
    return lista


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numeros=list(dict.fromkeys(raw[1] for raw in data)) #manera fácil para filtrar y resulta en un diccionario
    numeros=sorted(numeros)

    
    lista=[]

    for numero in numeros:
        lista_letras=[]
        for raw in data:
            if raw[1]==numero:
                lista_letras.append(raw[0])
            
        
        lista_letras=list(dict.fromkeys(lista_letras))
        lista.append((numero,lista_letras))
    

    return lista


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lista_claves=[]
    for raw in data:
        for clave in raw[4]:
            lista_claves.append(clave[0:clave.index(":")])

    dicc=list(dict.fromkeys(lista_claves)) #manera fácil para filtrar y resulta en un diccionario
    dicc=sorted(dicc)

    claves={} 

    for dic in dicc:
        count=0
        for clave in lista_claves:
            if clave==dic:
                count=count+1
        
        claves[dic]=count

    
    #print(claves)
    
    return claves


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_10=[]
    for raw in data:
        lista_10.append((raw[0],len(raw[3]),len(raw[4])))

    
    
    return lista_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import json 
    diccionario={}

    for raw in data:
        for letra in raw[3]:
            if letra not in diccionario:
                diccionario[letra]=0
            diccionario[letra]=diccionario[letra]+raw[1]
    
    diccionario=json.dumps(diccionario,sort_keys=True)

    diccionario=json.loads(diccionario)
    
    
    return diccionario




def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    with open ("data.csv","r") as file:
        data = file.readlines()

    data = [row.replace('\n','')for row in data]
    data1 = [(row.split('\t')[0],(row.split('\t')[-1])) for row in data]
    data2 = []
    for i in data1:
        data3 = i[1].split(",")
        for h in data3:
            data4 = int(h.split(":")[1])
            data5= (i[0], data4)
            data2.append(data5)
    diccionario = {}
    for row in data2:
        key = row[0]
        valor = int(row[1])
        if key in diccionario:
            diccionario[key] += valor
        else:
            diccionario[key] = valor

    diccionario1 = dict(sorted(diccionario.items(), key=lambda item: item[0]))
    
    return diccionario1
