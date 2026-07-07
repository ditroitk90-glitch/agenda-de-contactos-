lista_contactos = []
def menu(): 
    opciones = [
    "Agregar contacto",
    "Ver contactos",
    "Buscar contacto",
    "Modificar contacto",
    "Eliminar contacto",
    "salir"
    ]
    operaciones = {
    1: agregar_contactos,
    2: ver_contactos,
    3: buscar_contacto,
    4: modificar_contacto,
    5: eliminar_contacto,
    6: salir
    }
    while True:
     print("------MENU DE CONTACTOS------")
     for i, opciones1 in enumerate(opciones, start=1):
      print(f"{i}. {opciones1}")
     try:
      opcion = int(input("seleccione una opcion: "))
     except ValueError:
      print("Por favor, ingrese un número válido.")
      continue
     if opcion == 6: # salir del archivo
        print("hasta luego!!")
        break
     if opcion in operaciones:
        accion = operaciones[opcion]
        accion()
     if opcion < 1 or opcion > 6:
        print("Por favor, ingrese un número válido.")
def cargar_contactos():
    try:
        with open("contactos.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 3:               # ← validación defensiva
                    contacto = {
                        "nombre": datos[0],
                        "telefono": datos[1],
                        "correo": datos[2]
                    }
                    lista_contactos.append(contacto)
        print("Contactos cargados:", len(lista_contactos))
    except FileNotFoundError:
        print("No existe ningún archivo de contactos todavía.")
def agregar_contactos():
    nombre = input("introduzca su nombre y apellido: ")
    telefono = input("introduzca su telefono: ")
    correo = input("introduzca su correo: ")
    contactos_dic = {
        "nombre": nombre, 
        "telefono": telefono, 
        "correo": correo
        }
    lista_contactos.append(contactos_dic)
    guardar_contactostxt()
def ver_contactos():
    if not lista_contactos:
        print("No hay contactos guardados.")
    else:
        for i, contacto in enumerate(lista_contactos, start=1):
            print(f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
    encontrado = False
    for contacto in lista_contactos:
        if contacto['nombre'].lower() == nombre_buscar.lower():
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
            encontrado = True
    if not encontrado:
        print("Contacto no encontrado.")
def modificar_contacto():
    if not lista_contactos:
        print("no se encontraron contactos para modificar.")
    for i, contacto in enumerate(lista_contactos, start=1):
        print(f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
    try:
      indice = int(input("Ingrese el número del contacto a modificar: ")) - 1
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    if 0 <= indice < len(lista_contactos):
        nombre = input("Ingrese el nuevo nombre (deje vacío para no cambiar): ")
        telefono = input("Ingrese el nuevo teléfono (deje vacío para no cambiar): ")
        correo = input("Ingrese el nuevo correo (deje vacío para no cambiar): ")
        if nombre:
            lista_contactos[indice]['nombre'] = nombre
        if telefono:
            lista_contactos[indice]['telefono'] = telefono
        if correo:
            lista_contactos[indice]['correo'] = correo
        guardar_contactostxt()
def eliminar_contacto():
    print("Contactos guardados:")
    for i, contacto in enumerate(lista_contactos, start=1):
        print(f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}")
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
    for i, contacto in enumerate(lista_contactos):
        if contacto['nombre'].lower() == nombre_eliminar.lower():
            del lista_contactos[i]
            print("Contacto eliminado.")
            guardar_contactostxt()
            return
def salir():
    pass
def guardar_contactostxt():
        with open("contactos.txt", "w") as f:
            for contacto in lista_contactos: 
                f.write(f"{contacto['nombre']},{contacto['telefono']},{contacto['correo']}\n")
        print("Contactos guardados en un archivo de texto...")

cargar_contactos()
menu()
