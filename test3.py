xml_format = '<xml version="1.0"?>\n'
xml_format_2 = '<xml version="1.0"?>'
et = '<!ELEMENT '
etl= 10 #Element Tag Length

def element_verification(content, cant_lines):
    for i in range(cant_lines):
        if et in content[i]:
            #Hacer el split, guardar la lista y comenzar a tomar los elementos. 
            print(content[i].split(" "))


with open("C:\\Users\\José Manuel Martínez\\Google Drive\\Semestre 11\\Lenguajes de Programacion\\2. Practica\\Ejercicios DTD\\nota.dtd") as fp:
    content = fp.readlines()
    cant_lines = len(content)
    print(cant_lines)
#print(content[1])

for i in range(cant_lines):
        if content[i] == xml_format or content[i] == xml_format_2:
            print("EL DTD es de mismo formato que el XML.")
            element_verification(content, cant_lines)



                #flag
            #else:
             #   print("No Es un archivo XML.")
               # continue



