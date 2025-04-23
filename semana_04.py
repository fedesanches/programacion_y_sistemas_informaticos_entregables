import csv
from collections import Counter

def arboles_parque(nombre_archivo, nombre_parque=None):
    arboles = {}

    with open(nombre_archivo, 'r', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if nombre_parque is None:
                arboles[reader.line_num] = row
            elif row['espacio_ve'] == nombre_parque:
                arboles[reader.line_num] = row
                
    return arboles


def arbol_mas_popular(nombre_parque=None):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    arboles_nombres = []

    for arbol in arboles.values():
        arboles_nombres.append(arbol['nombre_com'])
        
    return Counter(arboles_nombres).most_common(1)[0][0]


def n_mas_altos(nombre_parque, n):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    arboles_altos = dict(sorted(arboles.items(), key=lambda x: float(x[1]['altura_tot']), reverse=True)[:n])
    return arboles_altos


def altura_promedio(nombre_parque, especie=None):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    alturas = []

    for arbol in arboles.values():
        if especie is None:
            alturas.append(float(arbol['altura_tot']))
        elif arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))

    return sum(alturas) / len(alturas)


def cantidad_de_arboles(nombre_parque):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    return len(arboles)


def cantidad_de_especies(nombre_parque):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    especies = set()

    for arbol in arboles.values():
        especies.add(arbol['nombre_com'])

    return len(especies)


def especies_exoticas_autoctonas(nombre_parque=None):
    arboles = arboles_parque('arbolado-en-espacios-verdes.csv', nombre_parque)
    especies_exoticas = 0
    especies_autoctonas = 0

    for arbol in arboles.values():
        if arbol['origen'] == 'Exótico':
            especies_exoticas += 1
        elif arbol['origen'] == 'Nativo/Autóctono':
            especies_autoctonas += 1

    return especies_exoticas / especies_autoctonas



arboles = arboles_parque('arbolado-en-espacios-verdes.csv')
parques = {arboles[i]['espacio_ve'] for i in arboles}

_cantidad_de_arboles = []
_altura_promedio = []
_cantidad_de_especies = []

for parque in parques:
    _cantidad_de_arboles.append((parque, cantidad_de_arboles(parque)))
    _altura_promedio.append((parque, altura_promedio(parque)))
    _cantidad_de_especies.append((parque, cantidad_de_especies(parque)))
    
    
_cantidad_de_arboles = sorted(_cantidad_de_arboles, key=lambda x: x[1], reverse=True)[:5]
_altura_promedio = sorted(_altura_promedio, key=lambda x: x[1], reverse=True)[:5]
_cantidad_de_especies = sorted(_cantidad_de_especies, key=lambda x: x[1], reverse=True)[:5]

print(_cantidad_de_arboles)
print(_altura_promedio)
print(_cantidad_de_especies)
print(arbol_mas_popular())
print(especies_exoticas_autoctonas())