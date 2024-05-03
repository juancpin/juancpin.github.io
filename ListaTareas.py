
import os

def limpiar_pantalla():
    # Verificar el sistema operativo y limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

class ListaTareas:
    def __init__(self):
        # Inicializa la lista de tareas vacía
        self.tareas = []

    def agregar_tarea(self, tarea):
        # Agrega una nueva tarea a la lista con estado inicial 'False' (pendiente)
        self.tareas.append({'tarea': tarea, 'completada': False})

    def marcar_completada(self, posicion):
        try:
            # Intenta marcar como completada la tarea en la posición especificada
            self.tareas[posicion]['completada'] = True
            print(f"Tarea en la posición {posicion+1} marcada como completada.\n")
        except IndexError:
            # Captura la excepción si la posición especificada no existe en la lista de tareas, alerta en rojo
            print("\033[91mLa posición especificada no existe.\033[0m")

    def mostrar_tareas(self):
        # Muestra todas las tareas pendientes junto con su estado (completada o pendiente)
        print("\nTareas pendientes:")
        for i, tarea in enumerate(self.tareas):
            # Cambia el color del estado de la tarea según su completitud, amarillo si Pendiente, verde si Completada
            estado = "\033[92mCompletada\033[0m" if tarea['completada'] else "\033[93mPendiente\033[0m"
            print(f"{i + 1}. {tarea['tarea']} - Estado: {estado}")
        print("\n")
    def eliminar_tarea(self, posicion):
        try:
            # Intenta eliminar la tarea en la posición especificada
            del self.tareas[posicion]
            print(f"\033[92mTarea en la posición {posicion+1} eliminada correctamente.\033[0m")
        except IndexError:
            # Captura la excepción si la posición especificada no existe en la lista de tareas, alerta en rojo
            print("\033[91mLa posición especificada no existe.\033[0m")

# Para enmarcar el texto en cuadro ascii
def imprimir_cuadro(texto):
    lines = texto.split('\n')
    width = max(len(line) for line in lines)
    border = '+' + '-' * (width + 2) + '+'
    print(border)
    for line in lines:
        print(f'| {line.ljust(width)} |')
    print(border)

# Texto del menú principal
menu_texto = """
SUPER TO-DO LIST

1. Agregar tarea

2. Mostrar todas las tareas

3. Marcar tarea como completada

4. Eliminar tarea

5. Salir

Puedes limpiar la pantalla introduciendo 'R'.
"""




def main():
    # Limpia la pantalla al inicio del programa
    limpiar_pantalla()
    # Crea una instancia de la clase ListaTareas
    lista = ListaTareas()

    # Imprimir el texto del menú principal en un cuadro ASCII
    imprimir_cuadro(menu_texto)

    while True:
        
        opcion = input("Escoja una opción: ")
        #lo pasamos a minúsculas
        opcion = opcion.lower()

        if opcion == "1":
            # Solicita al usuario ingresar una nueva tarea y la agrega a la lista
            tarea_nueva = input("\nIngresa Nueva Tarea: ")
            lista.agregar_tarea(tarea_nueva)
        elif opcion == "2":
            # Muestra todas las tareas pendientes
            lista.mostrar_tareas()
        elif opcion == "3":
            # Muestra las tareas pendientes y solicita al usuario la posición de la tarea completada
            lista.mostrar_tareas()
            posicion = int(input("\nIngresa Posición Tarea Completada: ")) - 1
            lista.marcar_completada(posicion)
        elif opcion == "4":
            # Muestra las tareas pendientes y solicita al usuario la posición de la tarea a eliminar
            lista.mostrar_tareas()
            posicion = int(input("\nIngresa Posición Tarea a Eliminar: ")) - 1
            lista.eliminar_tarea(posicion)
        elif opcion.lower() == "r":
            # Limpia pantalla y pone el menú de nuevo
            limpiar_pantalla() 
            imprimir_cuadro(menu_texto)       
        elif opcion == "5":
            # Finaliza el programa
            print("\u00A9 Juan Carlos Pin 2024 -- Desarrollo Web con Python | BeJob x IBM -- NOS VEMOS!!!")
            break
        else:
            # Captura la opción no válida ingresada por el usuario
            print("\033[91mOpción no válida. Por favor, selecciona una opción válida.\033[0m")

if __name__ == "__main__":
    main()
