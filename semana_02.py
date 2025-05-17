def invertir_lista(lista):
    list_invertida = []
    for i in range(len(lista)): list_invertida.append(lista[-(i + 1)])
    return list_invertida

def collatz(x):
    c = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        c += 1
    return c
    
def contar_definiciones(d):
    new_dict = {}
    for key in d:
        new_dict[key] = len(d[key]) 
    return new_dict


def cantidad_de_claves_letra(d, l):
    c = 0
    for key in d:
        if key[:1].upper() == l.upper(): c += 1
    return c

def propagar(l):
    for i in range(len(l)-1):
        if l[i] == 1 and l[i + 1] == 0: l[i + 1] = 1
    for i in range(len(l)-1, 0, -1):
        if l[i] == 1 and l[i - 1] == 0: l[i - 1] = 1      
    return l