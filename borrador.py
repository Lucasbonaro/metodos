
import math

print('Ingrese n entre 3 y 12:')
print()
n=int(input())
print()

matriz=[]
filas=n;columnas=n
def elementos():
    for inicializar in range(filas):
        matriz.append([0]*columnas)

    for i in range(filas):
        for j in range(columnas):
            matriz[i][j]=1/((i+1)+(j+1)-1) #uso (i+1) y (j+1) en lugar de "i" y "j" xq la lista empieza en posición 0

def Mostrar1(): #muestra matriz de n x n
    print("La matriz es:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
        
elementos()

Mostrar1()


vector=[]

def elementos():
    for inicializar in range(filas):
        vector.append([0])

    for i in range(filas):
            vector[i]= math.cos(2*math.pi/n-1)*i #uso i en lugar de (i-1)xq la lista empieza en posición 0

def Mostrar2(): #muestra vector independiente
    i=0
    print("El vector es:")
    for fila in vector:
            print("\t", vector[i], end=" ")
            i=i+1
            print()
       
        
elementos()

Mostrar2()

    
