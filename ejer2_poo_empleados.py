class Empleados:
    def __init__(self, nombre, edad, cargo, salario):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

def input_empleados():
    lista = []  
    for i in range(10):  
        print(f"empleado {i+1}:")
        nombre = input("Escriba el nombre: ").lower()        
        edad = int(input("Escriba la edad: "))
        cargo = input("Escriba el cargo: ").lower()  
        salario = int(input("Escriba el salario: "))
        lista.append(Empleados(nombre, edad, cargo, salario))  
    return lista  

def ingenieros_4millones(lista):
    cantidad = 0
    for Empleados in lista:
        if Empleados.cargo == "ingeniero" and Empleados.salario >= 4000000:
            cantidad += 1
    print(f"La cantidad de ingenieros que ganan más de 4 millones es: {cantidad}")

def acumulado_salario_mayor30(lista):
    cantidad2 = 0
    for Empleados in lista:
        if Empleados.salario < 2500000 and 18 < Empleados.edad < 30:
            cantidad2 += Empleados.salario
    print(f"El acumulado de los empleados que cobran menos de 2.500.000 y tienen una edad entre 18 y 30 años es de: {cantidad2}")

def promedio_analistas(lista):
    cantidad3 = 0
    suma = 0
    for Empleados in lista:
        if Empleados.cargo == "analista":
            suma += Empleados.salario
            cantidad3 += 1
    if cantidad3 > 0:
        promedio = suma / cantidad3
        print(f"El promedio de analistas es de: {promedio}")
    else:
        promedio = 0 
        print(f"El promedio de analistas es de: {promedio}")

def mayores_50(lista):
    cantidad = 0
    for Empleados in lista:
        if Empleados.edad > 50 and (Empleados.cargo == "gerencia" or Empleados.cargo == "direccion"):
            cantidad += 1
    print(f"La cantidad de adultos mayores de 50 años con cargo de gerencia o dirección es: {cantidad}")


print("Lista de empleados:")
lista = input_empleados()  
ingenieros_4millones(lista)  
acumulado_salario_mayor30(lista)  
promedio_analistas(lista)  
mayores_50(lista)  
