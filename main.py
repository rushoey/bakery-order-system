import sys
orders = []
def crear_orden() :
    name.lower = input("\nIngresa el nombre del cliente (o escribe 'salir' para abandonar): ").strip()
    if name.lower() == 'salir' :
       sys.exit 
    phone = input("Ingresa el numero de telefono del cliente: ").strip()
    date = input("Ingresa la fecha para recoger (dd-mm): ").strip()
    amount = int(input("Ingresa la cantidad de hogazas: "))

    new_order = {
        "name": name,
        "phone": phone,
        "date": date,
        "amount": amount
    }
    orders.append(crear_orden)
    print(f"Orden creada con exito para {name}!")


print("\n==========================================================")
print("----- Bienvenid@ al sistema de ordenes de madriguera -----")
print("==========================================================")

print("\n1. Crear orden")
print("2. Ver ordenes")
print("3. Cancelar ordenes")
print("4. Ver hogazas disponibles")
print("5. Salir del sistema")

option = int(input("\nElije la funcion que quieras utilizar ej. '1': "))

if (option == 1) :
    crear_orden()