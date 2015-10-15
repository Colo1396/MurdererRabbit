def creartxt():
    archi=open('Puntajes.txt','w')
    archi.close()

def grabartxt():
    archi=open('Puntajes.txt','a')
    archi.write('Linea 1\n')
    archi.write('Linea 2\n')
    archi.write('Linea 3\n')
    archi.write('http://pythonya.appspot.com/detalleconcepto?deta=Creaci%C3%B3n,%20carga%20y%20lectura%20de%20archivos%20de%20texto')
    archi.close()

def leertxt():
    archi=open('Puntajes.txt','r')
    linea=archi.readline()
    while linea!="":
        print linea
        linea=archi.readline()
    archi.close()
     
def leertxtenlista():
    archi=open('Puntajes.txt','r')
    lineas=archi.readlines()
    print lineas
    archi.close()

def leertxtenlista2():  #mostrando linea por linea
    archi=open('Puntajes.txt','r')
    lineas=archi.readlines()
    for li in lineas:
        print li
    archi.close()


creartxt()
grabartxt()
leertxt()
leertxtenlista()
leertxtenlista2()
