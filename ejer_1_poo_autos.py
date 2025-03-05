class Vehiculo:
    def __init__(self, marca, modelo, ano, tipo_de_combustible, precio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.tipo_de_combustible = tipo_de_combustible
        self.precio = precio

def proceso_vehiculos():
    lista_de_15 = []
    for i in range(15):
        print(f"Vehículo {i+1}:")
        marca = input("Escribe la marca del vehículo: ").lower()
        modelo = input("Escribe el modelo: ").lower()
        ano = int(input("Escribe el año del vehículo: "))
        tipo_de_combustible = input("Escribe el tipo de combustible (electrico/hibrido/gasolina): ").lower()
        precio = int(input("Escribe el precio: "))
        lista_de_15.append(Vehiculo(marca, modelo, ano, tipo_de_combustible, precio))
    return lista_de_15

def acumulado_electricos(lista_de_15):
    acumulado = 0
    for vehiculo in lista_de_15:
        if vehiculo.tipo_de_combustible == "electrico":
            acumulado += vehiculo.precio
    print(f"\nAcumulado del precio total de vehículos eléctricos: {acumulado}")

def cantidad_ano(lista_de_15):
    cantidad = 0
    for vehiculo in lista_de_15:
        if vehiculo.tipo_de_combustible == "hibrido" and vehiculo.ano > 2020:
            cantidad += 1
    print(f"\nCantidad de vehículos híbridos fabricados después de 2020: {cantidad}")

def toyotas(lista_de_15):
    suma = 0
    cantidad = 0
    for vehiculo in lista_de_15:
        if vehiculo.marca == "toyota":
            suma += vehiculo.precio
            cantidad += 1
    if cantidad > 0:
        promedio = suma / cantidad
        print(f"\nEl promedio de los precios de los vehículos Toyota es: {promedio}")
    else:
        print("\nNo hay vehículos Toyota en la lista.")

def menor_de_50m_gasolina(lista_de_15):
    cantidad = 0
    for vehiculo in lista_de_15:
        if vehiculo.tipo_de_combustible == "gasolina" and vehiculo.precio < 50000000:
            cantidad += 1
    print(f"\nCantidad de vehículos de gasolina con precio menor a 50 millones: {cantidad}")

print("Lista de Vehículos:")
lista_de_15 = proceso_vehiculos()

acumulado_electricos(lista_de_15)
cantidad_ano(lista_de_15)
toyotas(lista_de_15)
menor_de_50m_gasolina(lista_de_15)
