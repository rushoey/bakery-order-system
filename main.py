orders = []
def menu_principal() :
    print("\n==============================================================")
    print("-- Bienvenid@ al sistema de ordenes de madriguera de hogazas--")
    print("==============================================================")

    print("\n1. Crear orden")
    print("2. Ver ordenes")
    print("3. Cancelar ordenes")
    print("4. Ver hogazas disponibles")
    print("5. Salir del sistema")

    option = int(input("\nElije la funcion que quieras utilizar ej. '1': "))

    if (option == 1) :
        crear_orden()
    elif (option == 2) :
        ver_ordenes()

def crear_orden() :
    name = input("\nIngresa el nombre del cliente (o escribe 'menu' para regresar al menu): ").strip()
    if name.lower() == 'menu' :
       menu_principal()
    phone = input("Ingresa el numero de telefono del cliente: ").strip()
    date = input("Ingresa la fecha para recoger (dd-mm): ").strip()
    amount = int(input("Ingresa la cantidad de hogazas: "))

    new_order = {
        "name": name,
        "phone": phone,
        "date": date,
        "amount": amount
    }
    orders.append(new_order)
    print(f"\nOrden creada con exito para {name}!")
    menu_principal()

def ver_ordenes() :
    print("\n---Estas son las ordenes pendientes---")
    for index, order in enumerate(orders, 1):
        print(f"Order #{index}:")
        print(f"    Nombre: {order['name']}")
        print(f"    Numero de telefono: {order['phone']}")
        print(f"    Fecha: {order['date']}")
        print(f"    Cantidad de hogazas: {order['amount']}\n")
        
menu_principal()