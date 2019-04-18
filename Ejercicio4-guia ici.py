#Matias Nuñez- Ejercicio 4

x = str(input("Ingrese nombre de clavadista: "))
y = float(input("Ingrese grado de dificultad: "))
print("Ingrese puntajes de los 7 jueces (1-10)")
a = float(input("Ingrese puntaje de juez 1: "))
s = float(input("Ingrese puntaje de juez 2: "))
d = float(input("Ingrese puntaje de juez 3: "))
f = float(input("Ingrese puntaje de juez 4: "))
g = float(input("Ingrese puntaje de juez 5: "))
h = float(input("Ingrese puntaje de juez 6: "))
j = float(input("Ingrese puntaje de juez 7: "))

lista = [a,s,d,f,g,h,j]
m = sorted(lista)

p = (m[1]+m[2]+m[3]+m[4]+m[5])*(3/5)
p1 = p*y
print("El puntaje total es:",p1)
            
    
