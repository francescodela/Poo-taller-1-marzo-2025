class Paciente:
    def __init__(self, nombre, edad, sexo, presion_arterial):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.presion_arterial = presion_arterial

def proceso_paciente():
    lista = []
    for i in range(20): 
        print(f"Paciente {i+1}:")
        nombre = input("Escriba el nombre: ").lower()
        edad = int(input("Escriba la edad: "))
        sexo = input("Escriba el sexo (M/F): ").lower()
        presion_arterial = int(input("Escriba la presión arterial: "))
        lista.append(Paciente(nombre, edad, sexo, presion_arterial))
    return lista

def mas_de_50(lista):
    cantidad = 0
    for paciente in lista:
        if paciente.edad > 50 and paciente.presion_arterial > 140:
            cantidad += 1
    print(f"Los/as pacientes mayores de 50 años y con la P.A. mayor de 140 son: {cantidad}")

def menores30(lista):
    cantidad = 0
    for paciente in lista:
        if paciente.edad < 30 and 90 <= paciente.presion_arterial <= 120:
            cantidad += 1
    print(f"Pacientes menores de 30 años con presión arterial entre 90 y 120: {cantidad}")

def prom_mayor_130(lista):
    cantidad = 0
    suma = 0
    for paciente in lista:
        if paciente.presion_arterial > 130:
            cantidad += 1
            suma += paciente.edad
    if cantidad > 0:
        promedio = suma / cantidad
        print(f"Promedio de edad de pacientes con presión arterial mayor a 130: {promedio}")
    else:
        print("No hay pacientes con presión arterial mayor a 130.")

def presion_baja(lista):
    cantidad = 0
    for paciente in lista:
        if paciente.edad > 60 and paciente.presion_arterial < 90:
            cantidad += 1
    print(f"Pacientes mayores de 60 años con presión arterial menor a 90: {cantidad}")

print("Pacientes:")
lista = proceso_paciente()
mas_de_50(lista)
menores30(lista)
prom_mayor_130(lista)
presion_baja(lista)
