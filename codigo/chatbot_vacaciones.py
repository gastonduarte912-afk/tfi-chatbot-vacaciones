import csv

print("=== CHATBOT DE VACACIONES ===")

legajo = input("Ingrese su legajo: ")

encontrado = False

with open("empleados_vacaciones.csv", newline="", encoding="latin-1") as archivo:
    lector = csv.DictReader(archivo)

    for empleado in lector:

        if empleado["legajo"] == legajo:

            encontrado = True

            dias_disponibles = int(empleado["dias_disponibles"])

            print("Empleado:", empleado["nombre"])
            print("Días disponibles:", dias_disponibles)

            dias_solicitados = input("¿Cuántos días desea solicitar? ")

            if dias_solicitados.isdigit():

                dias_solicitados = int(dias_solicitados)

                if dias_solicitados <= dias_disponibles:

                    print("Solicitud aprobada")

                else:

                    print("Solicitud rechazada: saldo insuficiente")

            else:

                print("Error: debe ingresar un número")

if not encontrado:
    print("Legajo inexistente")