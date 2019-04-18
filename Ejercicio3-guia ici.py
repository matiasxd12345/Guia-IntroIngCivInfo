#Matias Nuñez - Ejercicio 3

a = float(input("Ingrese angulo 1: "))
n = float(input("Ingrese angulo 2: "))
g = float(input("Ingrese angulo 3: "))
if (a==90):
    print("El un triangulo rectangulo")
elif (a>90):
    print("Es un triangulo obtusangulo")
elif (a and n and g < 90):
    print("Es un triangulo acutangulo")
else:
    print("Error")