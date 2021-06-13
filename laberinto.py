class Cuarto():
    def __init__(self, norte, este, sur, oeste, contenido):
        self.contenido=contenido
        self.norte=norte
        self.este=este
        self.sur=sur
        self.oeste=oeste
    def __str__(self):
        if self.norte==1 and self.este==1 and self.sur==1 and self.oeste==1:
            return "X"
        elif self.norte==1 and self.este==0 and self.sur==1 and self.oeste==0:
            return "NS"
        elif self.norte==0 and self.este==1 and self.sur==0 and self.oeste==1:
            return "EO"

class Nivel():
    def __init__(self, cols, rows):
        self.arreglo=[]
        i, j=0, 0
        while i<cols:
            self.columnas=[]
            while j<rows:
                self.columnas.append(0)
                j+=1
            self.arreglo.append(self.columnas)
            j=0
            i+=1



cols=5
rows=5
inicio=Cuarto(1,1,1,1, "A")
ns=Cuarto(1,0,1,0,"")
eo=Cuarto(0,1,0,1,"")
n=Cuarto(1,0,0,0,"")
e=Cuarto(0,1,0,0,"")
s=Cuarto(0,0,1,0,"")
o=Cuarto(0,0,0,1,"")
nivel=Nivel(cols,rows)
nivel.arreglo[int(cols/2)][int(rows/2)]=inicio
i=0
j=0
while i<cols:
    while j<rows:
        if nivel.arreglo[i][j]==inicio:
            nivel.arreglo[i-1][j]=ns
            nivel.arreglo[i][j+1]=eo
            nivel.arreglo[i+1][j]=ns
            nivel.arreglo[i][j-1]=eo
        j+=1
    j=0
    i+=1
i=0
j=0
linea=""
for fila in nivel.arreglo:
    for item in fila:
        linea+="["+str(item)+"]"
    linea+="\n"
print(linea)
nivel.arreglo[2][1].norte=1
nivel.arreglo[2][1].sur=1
i=0
j=0
linea=""
for fila in nivel.arreglo:
    for item in fila:
        linea+="["+str(item)+"]"
    linea+="\n"
print(linea)
