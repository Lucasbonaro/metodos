
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
print()


vector=[]

def elementos2():
    for inicializar in range(filas):
        vector.append([0])

    for i in range(filas):
            vector[i]= math.cos(2*math.pi/n-1)*i #uso i en lugar de (i-1) xq la lista empieza en posición 0

#muestra vector independiente
def Mostrar2(): 
    i=0
    print("El vector es:")
    for fila in vector:
            print("\t", vector[i], end=" ")
            i=i+1
            print()
       
        
elementos2()
Mostrar2()
print()


#Matriz de coeficientes L

L=[]
def elementos3():
    for inicializar in range(filas):
        L.append([0]*columnas)

elementos3()

def Mostrar3(): #muestra matriz L
    print("La matriz L es:")
    for fila in L:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

#Eliminiación de Gauss


for j in range (columnas):
       for i in range (filas):
          if (i>j): L[i][j]=matriz[i][j]/matriz[j][j]
          for k in range (columnas):
            matriz[i][k]=matriz[i][k]-matriz[j][k]*L[i][j]
          if (i==j): L[i][j]=1   
          if (i>j): vector[i]=vector[i]-vector[j]*L[i][i-1]

#imprimir matriz L
               
def Mostrar3():
    print("La matriz L es:")
    for fila in L:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

#mostrar matriz U
def Mostrar4():
    print("La matriz U es:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


Mostrar3()

print()

Mostrar4()

print()

Mostrar2()






           
   
