"""
Punto de entrada principal (main.py) para la aplicación de gestión de tareas.
Maneja el menú interactivo en la terminal utilizando colorama y la arquitectura funcional.
"""

from colorama import init, Fore, Style
from app.operaciones import agregar_tarea, buscar_tareas, mostrar_lista_tareas

# Inicializar colorama para asegurar el reseteo automático de colores en cada línea
init(autoreset=True)

def mostrar_menu() -> None:
    """Muestra las opciones del menú principal en la terminal con formato visual."""
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== GESTOR DE TAREAS ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Ver lista de tareas")
    print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Agregar nueva tarea")
    print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Buscar tareas")
    print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Salir")

def main() -> None:
    """Función principal que ejecuta el bucle interactivo del programa."""
    mis_tareas = []

    while True:
        mostrar_menu()
        opcion = input(f"\n{Fore.GREEN}Selecciona una opción (1-4): {Style.RESET_ALL}").strip()

        if opcion == "1":
            print(f"\n{Fore.CYAN}--- LISTA DE TAREAS ---{Style.RESET_ALL}")
            mostrar_lista_tareas(mis_tareas)

        elif opcion == "2":
            print(f"\n{Fore.CYAN}--- AGREGAR NUEVA TAREA ---{Style.RESET_ALL}")
            nombre = input(f"{Fore.GREEN}Nombre de la tarea: {Style.RESET_ALL}").strip()
            if not nombre:
                print(f"{Fore.RED}El nombre no puede estar vacío.{Style.RESET_ALL}")
                continue

            print(f"{Fore.YELLOW}(Opcional) Introduce metadatos adicionales (deja en blanco para omitir){Style.RESET_ALL}")
            prioridad = input("Prioridad (ej. Alta, Media, Baja): ").strip()
            fecha_limite = input("Fecha límite (ej. 2026-12-31): ").strip()
            etiqueta = input("Etiqueta (ej. Trabajo, Casa): ").strip()

            kwargs_opcionales = {}
            if prioridad:
                kwargs_opcionales["prioridad"] = prioridad
            if fecha_limite:
                kwargs_opcionales["fecha_limite"] = fecha_limite
            if etiqueta:
                kwargs_opcionales["etiqueta"] = etiqueta

            mis_tareas = agregar_tarea(mis_tareas, nombre, **kwargs_opcionales)
            print(f"{Fore.GREEN}¡Tarea agregada exitosamente!{Style.RESET_ALL}")

        elif opcion == "3":
            print(f"\n{Fore.CYAN}--- BUSCAR TAREAS ---{Style.RESET_ALL}")
            filtro = input(f"{Fore.GREEN}Introduce palabra clave o término a buscar: {Style.RESET_ALL}").strip()
            if not filtro:
                print(f"{Fore.RED}El término de búsqueda no puede estar vacío.{Style.RESET_ALL}")
                continue

            resultados = buscar_tareas(mis_tareas, filtro)
            if not resultados:
                print(f"{Fore.YELLOW}No se encontraron tareas coincidentes con '{filtro}'.{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}Se encontraron {len(resultados)} coincidencia(s):{Style.RESET_ALL}")
                mostrar_lista_tareas(resultados)

        elif opcion == "4":
            print(f"\n{Fore.CYAN}¡Gracias por usar el gestor de tareas! Saliendo...{Style.RESET_ALL}")
            break
        else:
            print(f"\n{Fore.RED}Opción inválida. Por favor, selecciona un número entre 1 y 4.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()