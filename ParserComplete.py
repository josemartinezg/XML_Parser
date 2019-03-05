import bs4 as bs
#Variables de uso global
xml_format = '<xml version="1.0"?>\n'
xml_format_2 = '<xml version="1.0"?>'
et = '<!ELEMENT'
mx_const = 100
nombrexml = ''


def bs_checker(minimum, maximum, tag, classified):
    # Aquí se utiliza la librería beautifulSoup para leer el archivo
    soup = bs.BeautifulSoup(open(nombrexml), 'lxml')
    #Aquí se guardan los elementos que coinciden con el nombre provisto en la variable 'tag'.
    tag_list = soup.find_all(tag)
    #Se cuenta la cantidad de elementos que BS encontró en el documento...
    quant_elements = len(tag_list)
    #Aquí confirmamos que la cantidad e elementos esté conforme a la regla.
    if quant_elements >= minimum and quant_elements <= maximum:
        print("El documento cumple con las reglas del elemento "+ classified + " '" + tag + "'")
    else:
        print("El documento NO cumple con las reglas del elemento "+ classified + " '" + tag + "'")


def ocurrences_rules(parent, children):
    #En esta función se verifica si a cada elemento se le aplica por lo menos una regla.
    #De ser así, se envía a que se verifique la regla
    for j in range(len(children)):
        if '+' in children[j]:
            bs_checker(1, mx_const, children[j].replace('+', ''), 'Hijo')
        elif '*' in children[j]:
            bs_checker(0, mx_const, children[j].replace('*', ''), 'Hijo')
        elif '?' in children[j]:
            bs_checker(0, 1, children[j].replace('?', ''), 'Hijo')
        elif children[j] != '':
            bs_checker(1, 1, children[j], 'Hijo')

    for k in range(len(parent)):
        bs_checker(1, mx_const, parent[k], 'Padre')


def children_cleanup(child):
    childish = []
    for k in range (len(child)):
            if '(' in child[k]:
                childish.append(child[k].replace('(', ''))
            elif ',' in child[k]:
                childish.append(child[k].replace(',', ''))
            elif ')' in child[k]:
                childish.append(child[k].replace(')', ''))
            elif '>' in child[k]:
                childish.append(child[k].replace('>', ''))
            else:
                childish.append(child[k])
    return childish


def element_verification(content, cant_lines):
    #En esta lista se guardarán los elementos de la defiición inicial del DTD
    content_list = []
    for i in range(cant_lines):
        #'et' = <!Element...
        if et in content[i]:
            if content[i].count('(') != content[i].count(')'):
                print("Error! La parentizacion no es adecuada.")
            else:
                #Hacer el split de los elementos que deben de tener espacio (los padres), guardar la lista y comenzar a tomar los elementos.
                content_list = content[i].split(" ")
    parents = []
    child = []
    for j in range(len(content_list)):
        '''En esta condición agrego a la lista de los elementos padre los elementos que no tengan los caracteres mencionados...
        ... a continuación.'''
        if content_list[j] != et and '(' not in content_list[j] and ',' not in content_list[j] \
                and ')' not in content_list[j]:
                parents.append(content_list[j])
        #Los elementos que si tengan dichos caracteres son los hijos.
        elif et not in content_list[j]:
            child.append(content_list[j])
    #Se envia la lista dos veces a limpiar, para poder obtener el nombre de los elementos y sus reglas por si solos.
    aux = children_cleanup(child)
    children = children_cleanup(aux)
    # print(parents)
    # print(aux)
    # print(children)
    ocurrences_rules(parents, children)


def start_dtd():
    #Apertura del archivo DTD en un puntero.
    with open("nota.dtd") as fp:
        content = fp.readlines()
        cant_lines = len(content)
    #Verifico en todas las líneas si tengo un DTD que tenga el mismo formato que el XML.
    for i in range(cant_lines):
            if content[i] == xml_format or content[i] == xml_format_2:
                print("EL DTD es de mismo formato que el XML.\n Se puede proseguir con la verificación\n\n")
                element_verification(content, cant_lines)
                break
            else:
                print("El formato del DTD no coincide con el del XML.\n  Favor verificar.")


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
    start_dtd()


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
