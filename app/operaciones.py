"""
Módulo de operaciones para la gestión de tareas.
Diseñado bajo un enfoque funcional puro: recibe los datos por parámetro y retorna resultados precisos.
"""

from typing import List, Dict, Any
from app.modelos import crear_tarea

def agregar_tarea(tareas: List[Dict[str, Any]], nombre: str, **kwargs: Any) -> List[Dict[str, Any]]:
    """
    Agrega una nueva tarea a una copia de la lista de tareas y la retorna.

    Args:
        tareas (List[Dict[str, Any]]): Lista actual de tareas.
        nombre (str): Nombre o título principal de la tarea.
        **kwargs: Metadatos opcionales (prioridad, fecha_limite, etiqueta, etc.).

    Returns:
        List[Dict[str, Any]]: Nueva lista que incluye la tarea recién creada.
    """
    nueva_tarea = crear_tarea(nombre, **kwargs)
    
    tareas_actualizadas = tareas.copy()
    tareas_actualizadas.append(nueva_tarea)
    
    return tareas_actualizadas

def buscar_tareas(tareas: List[Dict[str, Any]], filtro: str) -> List[Dict[str, Any]]:
    """
    Busca tareas dentro de una lista que coincidan con un texto en su nombre o metadatos opcionales.

    Args:
        tareas (List[Dict[str, Any]]): Lista de tareas donde realizar la búsqueda.
        filtro (str): Palabra clave o término de búsqueda.

    Returns:
        List[Dict[str, Any]]: Subconjunto de tareas que coinciden con el filtro.
    """
    filtro_lower = filtro.lower()
    resultados: List[Dict[str, Any]] = []
    
    for tarea in tareas:
        if filtro_lower in tarea["nombre"].lower():
            resultados.append(tarea)
            continue
        
        encontrado_en_kwargs = any(
            filtro_lower in str(valor).lower() 
            for clave, valor in tarea.items() 
            if clave not in ("nombre", "completada")
        )
        
        if encontrado_en_kwargs:
            resultados.append(tarea)
            
    return resultados

def mostrar_lista_tareas(tareas: List[Dict[str, Any]]) -> None:
    """
    Muestra en la consola la lista completa de tareas.

    Args:
        tareas (List[Dict[str, Any]]): Lista de tareas a mostrar.
    """
    if not tareas:
        print("No hay tareas registradas todavía.")
        return

    for i, tarea in enumerate(tareas, start=1):
        estado = "[Completada]" if tarea.get("completada") else "[Pendiente]"
        print(f"{i}. {tarea['nombre']} - {estado}")
        
        for clave, valor in tarea.items():
            if clave not in ("nombre", "completada"):
                print(f"   └─ {clave.capitalize()}: {valor}")