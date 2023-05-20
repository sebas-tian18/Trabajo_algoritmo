import sympy as sym
import numpy as num 

def fun_x(x): return 3 * x**2 + 8 * x - 24 #funcion cuadratica 

# primera parte 

x = float(input("Ingrese el valor de x: "))
del_x = float(input("Ingrese el valor para delta x: "))

f = (fun_x(x + del_x) - fun_x(x))/del_x # calculamos derivada
print("La derivada es: ", f)

#segunda parte 

def fun_x2(x):return (5 + x**2) - 25

xd = sym.Symbol('x') #asignaos uso matematico
s = (5 + xd**2) - 25

der_1 = float(input("Ingrese el valor para la derivada: "))
x = der_1/10 # despejamos x
print("el valor de x es: ",x)

ep = 2.22 * 10**-16 #aproximacion para epsilon
r = 0
while r < ep:
    rz = num.sqrt(ep)
    delt = rz * x
    r = abs(der_1 - ((fun_x2(x + delt) - fun_x2(x)) /delt ))#valor absoluto
print("El resultado es: ",r) 