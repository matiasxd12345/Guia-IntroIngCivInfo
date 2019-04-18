#Matias Nuñez - Ejercicio 1

lista = [2,3,4,5,6,7,2,3,4,5,6,7]
rut = input("Ingrese RUT sin digito verificador: ")
rut = rut[::-1]
m = 0
d = 0
dv = 12
suma = 0
    
while m < len(rut):
    d = int(rut[m])*int(lista[m])
    suma = suma + d
    m = m + 1
v = 11 - (suma % 11)
    
if 0 < v < 10:
        dv = v
elif v == 11:
    dv = 0
elif v == 10:
    str(dv)
    dv = "K"
        
print ("El digito verificador es: ", dv)
    
