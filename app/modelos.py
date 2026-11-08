"""
Módulo de modelos de datos para la aplicación de tareas.
Define la estructura básica de una tarea.
"""

from typing import Dict, Any

def crear_tarea(nombre: str, **kwargs: Any) -> Dict[str, Any]:
    """
    Crea un diccionario que representa una tarea con metadatos flexibles.

    Args:
        nombre (str): Nombre o título principal de la tarea.
        **kwargs: Metadatos opcionales (ej: prioridad, fecha_limite, etiqueta).

    Returns:
        Dict[str, Any]: Estructura completa de la tarea.
    """
    tarea = {
        "nombre": nombre,
        "completada": False
    }
    tarea.update(kwargs)
    return tarea