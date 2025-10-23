# Interfaz por consola para interactuar con el usuario.

from gestor import GestorTareas

def menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

gestor = GestorTareas()

while True:
    menu()
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        desc = input("Descripción de la tarea: ")
        gestor.agregar_tarea(desc)

    elif opcion == "2":
        gestor.listar_tareas()

    elif opcion == "3":
        if not gestor.listar_tareas():
            continue
        try:
            num = int(input("Número de la tarea a completar: ")) - 1
            gestor.completar_tarea(num)
        except ValueError:
            print("Ingresá un número válido.")

    elif opcion == "4":
        if not gestor.listar_tareas():
            continue
        try:
            num = int(input("Número de la tarea a eliminar: ")) - 1
            gestor.eliminar_tarea(num)
        except ValueError:
            print("Ingresá un número válido.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Elegí un número del 1 al 5.")