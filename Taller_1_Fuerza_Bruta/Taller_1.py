import matplotlib.pyplot as plt

#------------------------ funciones ----------------------------

def funcion(x1,x2,tita):
    fun=1.2*x1+1.16*x2-tita*((2*x1**2)+(x2**2)+(x1+x2)**2)
    return fun

def encontrar(lista):
    maxi=max(lista[-1])
    for i in lista:
        if i[-1]==maxi:
            return i

def ciclo(ran,ti):
    lista=[]
    for x1 in range(ran):
        for x2 in range(ran):
            if x1+x2<ran:
                var=[x1,x2,funcion(x1,x2,ti)]
                lista.append(var)
    return lista

#-------------------------- Actividad -----------------------------------

tita=0.0001
x1=x2=delta=0
lista=ciclo(6,tita)

maximo=encontrar(lista)
print("El numero maximo es "+str(maximo[-1])+" en x1="+str(maximo[0])+" y x2="+str(maximo[1]))

#-------------------------- Grafico ------------------------------

fig, ax = plt.subplots()

# Graficamos la lista
ax.scatter(maximo[0], maximo[1], color='green', label='x1='+str(maximo[0])+', x2='+str(maximo[1])+' y Max='+str(maximo[-1]))

# Graficamos la restricción
ax.plot(range(6), [5-i for i in range(6)], color='red', label='Restricción <=6')

# Añadimos una leyenda y mostramos el gráfico
ax.set_title("Funcion=1.2*x1+1.16*x2-tita*((2*x1**2)+(x2**2)+(x1+x2)**2)")
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.legend()
plt.show()