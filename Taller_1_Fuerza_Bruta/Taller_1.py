#------------------------ funciones ----------------------------
def funcion(x1,x2,tita):#ingresamos x1,x2 y tita
    fun=1.2*x1+1.16*x2-tita*((2*x1**2)+(x2**2)+(x1+x2)**2)#ocupamos la funcion del ejemplo
    return fun#retornamos el resultado

def encontrar(lista):
    maxi=max(lista[-1])#revisa el ultimo numero de la lista
    for i in lista:
        if i[-1]==maxi:#buscamos en la lista que numero es igual al numero maximo para obtener su fila dentro de la matriz
            return i#retornamos la fila

def ciclo(ti,delta):
    if delta==0.1:#dependiendo del delta
        lista=[]
        for i in range(51):#ya que es 0.1 son 51 ciclos
            for j in range(51):
                x1=i/10#al i lo dividimos en 10 para obtener el numero 
                x2=j/10#lo mismo
                if x1+x2<=5:#la suma de ambos debe ser menor o igual a 5
                    var=[x1,x2,funcion(x1,x2,ti)]#almcacenamos los valores en una lista
                    lista.append(var)#y esa lista en otra lista
    elif delta==0.01:
        lista=[]#lo mismo pero con 0.01
        for i in range(501):
            for j in range(501):
                x1=i/100
                x2=j/100
                if x1+x2<=5:
                    var=[x1,x2,funcion(x1,x2,ti)]
                    lista.append(var)
    return lista

#-------------------------- Actividad -----------------------------------
tita=0.001#el tita que se usara
delta=float(input("Ingrese DeltaX: "))#el deltax que se usara
lista=ciclo(tita,delta)#el ciclo donde se almacenara toda la lista de valores menor o igual a 5
maximo=encontrar(lista)#almacenamos el valor resultante mas grande en maximo
print("El numero maximo es "+str(maximo[-1])+" en x1="+str(maximo[0])+" y x2="+str(maximo[1]))