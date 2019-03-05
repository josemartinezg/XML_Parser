# Validar que esté bien formado
# XML Documents Must Have a Root Element
# All XML Elements Must Have a Closing Tag boop
# XML Elements Must be Properly Nested
# XML Tags are Case Sensitive
# Tag names cannot contain spaces.
# XML Attribute Values Must Always be Quoted

def formatear(file,lista):
    for line in file:  # "borro" los saltos de linea
        lista.append(line.replace("\n", ""))
    return lista

def verificarPL(lista):
    for i in range(aux):  # recorro la lista linea por linea
        if lista[0] != '<?xml version="1.0"?>' and '<<?xml version="1.0" encoding="UTF-8"?>':#comparo con los prologs
            print("Alerta, el prolog no se encuentra en la primera linea o la sintaxis es incorrecta")#alerto
            break

    print("EL documento XML está bien formado.")
    start_dtd_ver()

def verificarOpenClose(lista):
    for i in range(aux):  # recorro la lista linea por linea
        if lista[i].count('<') != lista[i].count('>'):  # cuento y comparo la cantidad de opening y closing tags
            print("Error! Hay una discrepancia entre los opening y closing tags.")#alerto
            break

#nombredtd = input("Ingrese nombre del DTD: ")
nombrexml = input("Ingrese nombre del XML: ")
with open(nombrexml) as file:
    lista = []
    formatear(file,lista)#quitar salto de lineas
    aux = len(lista)
    verificarOpenClose(lista)# <  >
    verificarPL(lista) #<?xml version="1.0"?>










