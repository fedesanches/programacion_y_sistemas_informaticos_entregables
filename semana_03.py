import random

def crear_album(figus_total):
    return [0] * figus_total

def album_incompleto(A):
    return True if 0 in A else False

def comprar_figu(figus_total):
    return random.randint(0, figus_total-1)

def cuantas_figus(figus_total):
    album_nuevo = crear_album(figus_total)
    compras = 0
    
    while album_incompleto(album_nuevo):
        compras += 1
        album_nuevo[comprar_figu(figus_total)] += 1

    return compras

def experimento_figus_sueltas(n_repeticiones, figus_total):
    res = []
    for i in range(n_repeticiones):
        res.append(cuantas_figus(figus_total))
    return round(sum(res) / len(res))


def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete): paquete.append(comprar_figu(figus_total))
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    album_nuevo = crear_album(figus_total)
    compras = 0
    
    while album_incompleto(album_nuevo):
        compras += 1
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figura in paquete:
            album_nuevo[figura] += 1

    return compras

def experimento_figus(n_repeticiones, figus_total, figus_paquete):
    res = []
    for i in range(n_repeticiones):
        res.append(cuantos_paquetes(figus_total, figus_paquete))
    return res, round(sum(res) / len(res))


n_repeticiones = 1000
figus_total = 860
figus_paquete = 5