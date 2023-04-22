# Importing NumPy Library
import np
import sys
import math

# Reading number of unknowns
n = int(input('Ingresar dimension de la matriz: '))

# Matriz extendida (coeficientes y vector independiente
a = np.zeros((n,n+1))

# Vector solución
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
         if (j<n+1): a[i][j]=1/((i+1)+(j+1)-1) #uso (i+1) y (j+1) en lugar de "i" y "j" xq la lista empieza en posición 0
         else: math.cos(2*math.pi/n-1)*i #uso i en lugar de (i-1) xq la lista empieza en posición 0

i=0

print("La matriz es:")
for i in a:
     for valor in i:
        print("\t", valor, end=" ")
        print()
         
 
