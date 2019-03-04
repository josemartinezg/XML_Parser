string ='<tag> Mamaguevaso </tag>'

result = string.find('<')

if result != -1:
    print("We have opening tag @ "+ str(result+1))
    result = string.find('>')
    if result != -1:
        print("We have a symetric closing tag @ " + str(result+1))



