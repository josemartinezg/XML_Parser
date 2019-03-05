import bs4 as bs

xml_format = '<xml version="1.0"?>\n'
xml_format_2 = '<xml version="1.0"?>'
et = '<!ELEMENT'
etl= 10 #Element Tag Length
mx_const = 100

def bs_checker(minimum, maximum, tag):
    soup = bs.BeautifulSoup(open("text.xml"), 'lxml')
    tag_list = soup.find_all(tag)
    quant_elements = len(tag_list)
    #print(tag_list)
    print(len(tag_list))
    if quant_elements >= minimum and quant_elements <= maximum:
        print("El documento cumple con las reglas del elemento '" + tag + "'")
    else:
        print("El documento NO cumple con las reglas del elemento '" + tag + "'")

def ocurrences_rules(parent, children):
    count = 0
    for i in range(len(children)):
        if children[i] == '':
            count += 1

    #print(count)
    for j in range(len(children)):
        if '+' in children[j]:
            bs_checker(1, mx_const, children[j].replace('+', ''))
        elif '*' in children[j]:
            bs_checker(0, mx_const, children[j].replace('*', ''))
        elif '?' in children[j]:
            bs_checker(0, 1, children[j].replace('?', ''))

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
                print(content[i].split(" "))
                #Hacer el split de los elementos que deben de tener espacio (los padres), guardar la lista y comenzar a tomar los elementos.
                content_list = content[i].split(" ")
                print("=============================================================")
    parents = [] * 100
    aux1 = []
    child = []
    children = []

    for j in range(len(content_list)):
        if content_list[j] != et and '(' not in content_list[j] and ',' not in content_list[j] and ')' not in content_list[j]:
                parents.append(content_list[j])
        elif et not in content_list[j]:
            child.append(content_list[j])

    aux1 = children_cleanup(child)
    children = children_cleanup(aux1)
    print(parents)
    print(aux1)
    print(children)
    ocurrences_rules(parents, children)


#Apertura del archivo DTD en un puntero.
with open("nota.dtd") as fp:
    content = fp.readlines()
    cant_lines = len(content)
#Verifico en todas las líneas si tengo un DTD que tenga el mismo formato que el XML.
for i in range(cant_lines):
        if content[i] == xml_format or content[i] == xml_format_2:
            print("EL DTD es de mismo formato que el XML.")
            element_verification(content, cant_lines)
        else:
            print("El formato del DTD no coincide con el del XML.\n  Favor verificar.")



