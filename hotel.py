import csv
from datetime import datetime

# Definición de constantes
NUM_PISOS = 5
HABITACIONES_POR_PISO = 8
PRECIOS = {
    1: 30000,
    2: 30000,
    3: 30000,
    4: 60000,
    5: 100000
}
ESTADO_LIBRE = "Libre"
ESTADO_RESERVADO = "Reservado"

habitaciones = {}
for piso in range(1, NUM_PISOS + 1):
    for num_hab in range(1, HABITACIONES_POR_PISO + 1):
        codigo = f"{piso}{num_hab}"
        habitaciones[codigo] = {
            "codigo": codigo,
            "estado": ESTADO_LIBRE,
            "precio_diario": PRECIOS[piso],
            "nombre": "",
            "apellido": "",
            "rut": "",
            "fecha_ingreso": "",
            "fecha_salida": ""
        }

def reservar_habitacion():
    codigo = input("Ingrese el código de la habitación que desea reservar (por ejemplo, 34 para piso 3, habitación 4): ")
    habitacion = habitaciones.get(codigo)
    if habitacion and habitacion["estado"] == ESTADO_LIBRE:
        nombre = input("Ingrese el nombre del responsable: ")
        apellido = input("Ingrese el apellido del responsable: ")
        rut = input("Ingrese el rut del responsable: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso (formato dd/mm/yyyy hh:mm): ")
        fecha_salida = input("Ingrese la fecha de salida (formato dd/mm/yyyy hh:mm): ")
        
        try:
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%d/%m/%Y %H:%M")
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Fecha ingresada en formato incorrecto.")
            return
        
        costo_total = habitacion["precio_diario"] * ((fecha_salida - fecha_ingreso).days + 1)
        print(f"Reserva confirmada para la habitación {codigo}. Costo total: ${costo_total}")
        
        habitacion["estado"] = ESTADO_RESERVADO
        habitacion["nombre"] = nombre
        habitacion["apellido"] = apellido
        habitacion["rut"] = rut
        habitacion["fecha_ingreso"] = fecha_ingreso.strftime("%d/%m/%Y %H:%M")
        habitacion["fecha_salida"] = fecha_salida.strftime("%d/%m/%Y %H:%M")
    else:
        print(f"La habitación {codigo} no está disponible para reserva.")

def buscar_habitacion():
    codigo = input("Ingrese el código de la habitación que desea buscar: ")
    habitacion = habitaciones.get(codigo)
    if habitacion:
        print("Información de la habitación:")
        print(f"Código: {habitacion['codigo']}")
        print(f"Estado: {habitacion['estado']}")
        if habitacion['estado'] == ESTADO_RESERVADO:
            print(f"Reservada por: {habitacion['nombre']} {habitacion['apellido']} ({habitacion['rut']})")
            print(f"Fecha de entrada: {habitacion['fecha_ingreso']}")
            print(f"Fecha de salida: {habitacion['fecha_salida']}")
        print(f"Precio diario: ${habitacion['precio_diario']}")
    else:
        print("La habitación no existe o el código ingresado es inválido.")

def ver_estado():
    for habitacion in habitaciones.values():
        print(f"Código: {habitacion['codigo']}")
        print(f"Estado: {habitacion['estado']}")
        if habitacion['estado'] == ESTADO_RESERVADO:
            print(f"Reservada por: {habitacion['nombre']} {habitacion['apellido']} ({habitacion['rut']})")
            print(f"Fecha de entrada: {habitacion['fecha_ingreso']}")
            print(f"Fecha de salida: {habitacion['fecha_salida']}")
        print(f"Precio diario: ${habitacion['precio_diario']}")
        print("---")

def ventas_diarias():
    total_ventas = 0
    for habitacion in habitaciones.values():
        if habitacion['estado'] == ESTADO_RESERVADO:
            total_ventas += habitacion['precio_diario']
    print(f"Total de ventas del día: ${total_ventas}")

def guardar_informacion():
    with open('estado_habitaciones.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Código', 'Estado', 'Precio Diario', 'Nombre', 'Apellido', 'RUT', 'Fecha de Entrada', 'Fecha de Salida'])
        for habitacion in habitaciones.values():
            writer.writerow([habitacion['codigo'], habitacion['estado'], habitacion['precio_diario'],
                             habitacion['nombre'], habitacion['apellido'], habitacion['rut'],
                             habitacion['fecha_ingreso'], habitacion['fecha_salida']])
    print("Información guardada correctamente en estado_habitaciones.csv")

def menu():
    while True:
        print("\nBienvenido al sistema de gestión de habitaciones de hotel")
        print("1. Reservar una habitación")
        print("2. Buscar una habitación")
        print("3. Ver estado de todas las habitaciones")
        print("4. Calcular ventas diarias")
        print("5. Guardar información de las habitaciones")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == '1':
            reservar_habitacion()
        elif opcion == '2':
            buscar_habitacion()
        elif opcion == '3':
            ver_estado()
        elif opcion == '4':
            ventas_diarias()
        elif opcion == '5':
            guardar_informacion()
        elif opcion == '6':
            print("Gracias por utilizar el sistema de gestión de habitaciones.")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 6.")

if __name__ == "__main__":
    menu()
