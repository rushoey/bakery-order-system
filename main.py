import json
orders = []
ordenes_eliminadas = []
id = 0
corriendo = True # booleano para que el sistema corra mientras sea verdadero

with open("id.json", "r") as file: # importa el archivo de id que contiene la cuenta de pedidos hasta el momento
    id = json.load(file)

with open("orders.json", "r", encoding="utf-8") as file: # importa el archivo de ordenes activas
    orders = json.load(file)

with open("ordenes_eliminadas.json", "r", encoding="utf-8") as file: # importa el archivo de ordenes eliminadas
    ordenes_eliminadas = json.load(file)

def get_valid_int(prompt, min_val = None, max_val = None) : # funcion para verificar que cierto input este dentro de un valor minimo y maximo
    while True :
        try :
            value = int(input(prompt)) # le pide al usuario un int con el prompt pasado cuando se llama la funcion
            if min_val is not None and value < min_val : # checa si el valor del usuario es menor que el minimo o nulo y le pide que ingrese uno valido
                print(f"El valor que ingresaste no es valido. El valor tiene que ser minimo {min_val}")
                continue
            if max_val is not None and value > max_val : # checa si el valor del usuario es mayor que el maximo o nulo y le pide que ingrese uno valido
                print(f"El valor que ingresaste no es valido. El valor tiene que ser maximo {max_val}")
                continue
            return value # si el valor ingresado es un valor valido, lo regresa por la funcion
        except ValueError : # si el valor no es un numero entero, le pide que ingrese uno
            print(f"Formato invalido, recuerda ingresar un numero entero")

def crear_orden() :
    name = input("\nIngresa el nombre del cliente: ").strip() # le pide el nombre del cliente para la orden
    phone = get_valid_int("Ingresa el numero de telefono del cliente: ", min_val = 1000000000, max_val = 9999999999) # utiliza la funcion get_valid_int, paso el prompt y valor min/max
    date = input("Ingresa la fecha para recoger (DD-MM): ") # le pide al usuario la fecha para recoger en cierto formato, POSIBILIDAD DE USAR LIBRERIA DE DATETIME EN FUTURO
    amount = get_valid_int("Ingresa la cantidad de hogazas: ", min_val = 1, max_val = 8) # NOTA PARA FUTURO: cambiar el max_val por variable que maneje disponibilidad de hogazas segun el dia que el usuario ingrese
    global id 
    id += 1 

    new_order = { # crea un nuevo diccionario llamado new_order para la lista de orders
        "id": id,
        "name": name,
        "phone": phone,
        "date": date,
        "amount": amount
    }
    orders.append(new_order) 

    with open("orders.json", "w", encoding="utf-8") as file: # abre el archivo de orders.json 
        json.dump(orders, file, indent=4) # escribe la lista de orders en el archivo abierto de orders.json

    with open("id.json", "w", encoding="utf-8") as file: # abre el archivo de id.json
        json.dump(id, file) # actualiza el id en el archivo abierto de id.json
    print(f"\nOrden creada con exito para {name}!")

def ver_ordenes() : # imprime todas las ordenes en la lista orders usando un for loop
    print("\n---Estas son las ordenes pendientes---")
    for index, order in enumerate(orders) :
        print(f"Orden #{order['id']}:")
        print(f"    Nombre: {order['name']}")
        print(f"    Numero de telefono: {order['phone']}")
        print(f"    Fecha: {order['date']}")
        print(f"    Cantidad de hogazas: {order['amount']}\n")

def cancelar_orden() :
    global id
    if not orders : # termina la funcion cancelar_orden y regresa al menu
        print("No hay ninguna orden hasta ahora" ) 
    else :
        id_eliminar = input("\n---Ingresa el numero de orden que quieras eliminar--- ") # variable para guardar el numero de orden que el usuario quiere eliminar
        keep_running = True
        while (keep_running) :
            for index, order in enumerate(orders) :
                if (id_eliminar == "salir"): 
                    keep_running = False
                    break
                elif (int(id_eliminar) == order['id'] and int(id_eliminar) <= id) : # verifica que el id_eliminar sea menor o igual al numero de ordenes y si coincide con order['id']
                    ordenes_eliminadas.append(orders.pop(index)) # agrega la orden a la lista ordenes_eliminadas, y la elimina de la lista orders
                    print(f"\nOrden #{id_eliminar} eliminada con exito")
                    with open("orders.json", "w", encoding="utf-8") as file: # abre el archivo orders.json
                        json.dump(orders, file, indent=4) # actualiza el archivo de orders.json con la lista actual de orders (quita la orden eliminada)
                    with open("ordenes_eliminadas.json", "w", encoding="utf-8") as file: # abre el archivo ordenes_eliminadas.son
                        json.dump(ordenes_eliminadas, file, indent=4) # actualiza el archivo de ordenes_eliminadas.json con la lista actual de ordenes_eliminadas (agrega la orden eliminada)
                    keep_running = False
                    break
            else :
                id_eliminar = input("\n---Ingresa el numero de orden que quieras eliminar ('salir' para ir al menu)--- ")
                if (id_eliminar == "salir"):
                    keep_running = False
        
def registro_eliminadas() : # imprime la lista de ordenes_eliminadas usando un for loop
    print("\n---Estas son las ultimas ordenes que fueron eliminadas ---")
    for index, orden_eliminada in enumerate(ordenes_eliminadas, 1):
        print(f"Orden #{orden_eliminada['id']}:")
        print(f"    Nombre: {orden_eliminada['name']}")
        print(f"    Numero de telefono: {orden_eliminada['phone']}")
        print(f"    Fecha: {orden_eliminada['date']}")
        print(f"    Cantidad de hogazas: {orden_eliminada['amount']}\n")

def main() : 
    global corriendo # trae el booleano corriendo a la funcion main
    while (corriendo) : # verifica que el booleano sea verdadero, y mientras lo sea, imprimira el menu principal
        print("\n==============================================================")
        print("-- Bienvenid@ al sistema de ordenes de madriguera de hogazas--")
        print("==============================================================")

        print("\n1. Crear orden")
        print("2. Ver ordenes")
        print("3. Cancelar ordenes")
        print("4. Registro ordenes eliminadas")
        print("5. Ver hogazas disponibles")
        print("6. Salir del sistema")

        option = get_valid_int("\nElije la funcion que quieras utilizar ej. '1': ", min_val = 1, max_val = 6)
        if (option == 1) :
            crear_orden()
        elif (option == 2) :
            ver_ordenes()
        elif (option == 3) :
            cancelar_orden()
        elif (option == 4) :
            registro_eliminadas()
        elif (option == 6) :
            corriendo = False  # cambia el estado del booleano corriendo, y termina el sistema

main()