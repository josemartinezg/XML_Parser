import bs4 as bs

string ='<tag> Mamaguevaso </tag>\n <taggy> Niema </taggy>'



tag = 'altura'
string = []
#soup = bs.BeautifulSoup(string, 'lxml')
#print(soup)
#print(soup.tag)
#print(soup.tag.string)

soup = bs.BeautifulSoup(open("C:\\Users\\José Manuel Martínez\\Google Drive\\Semestre 11\\Lenguajes de Programacion\\2. Practica\\Ejercicios XML\\E5.xml"), 'lxml')
#'tags' es una 'coleccion' de objetos.
tags = soup.find_all(tag)
print(tags)
print(len(tags))

