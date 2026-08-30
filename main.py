orders = []
ordenes_eliminadas = []
id = 0
def menu_principal() :
    print("\n==============================================================")
    print("-- Bienvenid@ al sistema de ordenes de madriguera de hogazas--")
    print("==============================================================")

    print("\n1. Crear orden")
    print("2. Ver ordenes")
    print("3. Cancelar ordenes")
    print("4. Registro ordenes eliminadas")
    print("5. Ver hogazas disponibles")
    print("6. Salir del sistema")

    option = int(input("\nElije la funcion que quieras utilizar ej. '1': "))

    if (option == 1) :
        crear_orden()
    elif (option == 2) :
        ver_ordenes()
    elif (option == 3) :
        cancelar_orden()
    elif (option == 4) :
        registro_eliminadas()

def regresar_menu() :
    regresar = input("\n\n-----Deseas regresar al menu? teclea 'menu'-----: ")
    if regresar.lower() == 'menu' :
       menu_principal()

def crear_orden() :
    name = input("\nIngresa el nombre del cliente: ").strip()
    phone = input("Ingresa el numero de telefono del cliente: ").strip()
    date = input("Ingresa la fecha para recoger (dd-mm): ").strip()
    amount = int(input("Ingresa la cantidad de hogazas: "))
    global id
    id += 1

    new_order = {
        "id": id,
        "name": name,
        "phone": phone,
        "date": date,
        "amount": amount
    }
    orders.append(new_order)
    print(f"\nOrden creada con exito para {name}!")
    regresar_menu()

def ver_ordenes() :
    print("\n---Estas son las ordenes pendientes---")
    for index, order in enumerate(orders) :
        print(f"Orden #{order['id']}:")
        print(f"    Nombre: {order['name']}")
        print(f"    Numero de telefono: {order['phone']}")
        print(f"    Fecha: {order['date']}")
        print(f"    Cantidad de hogazas: {order['amount']}\n")
    regresar_menu()

def cancelar_orden() :
    id_eliminar = int(input("\n---Ingresa el numero de orden que quieras eliminar---"))
    for index, order in enumerate(orders) :
        if (id_eliminar == order['id']) :
            ordenes_eliminadas.append(orders.pop(index))
            print(f"\nOrden #{id_eliminar} eliminada con exito")
        
    regresar_menu()

def registro_eliminadas() :
    print("\n---Estas son las ultimas ordenes que fueron eliminadas ---")
    for index, orden_eliminada in enumerate(ordenes_eliminadas, 1):
        print(f"Orden #{orden_eliminada['id']}:")
        print(f"    Nombre: {orden_eliminada['name']}")
        print(f"    Numero de telefono: {orden_eliminada['phone']}")
        print(f"    Fecha: {orden_eliminada['date']}")
        print(f"    Cantidad de hogazas: {orden_eliminada['amount']}\n")

    regresar_menu()


menu_principal()