# Clase que gestiona una lista de tareas, las guarda y las lee desde un archivo JSON.

import json
from tarea import Tarea

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()


    def cargar_tareas(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                return [Tarea.from_dict(t) for t in datos]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("El archivo de tareas está dañado. Se iniciará una lista vacía.")
            return []


    def guardar_tareas(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump([t.to_dict() for t in self.tareas], f, indent=4)
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")


    def agregar_tarea(self, descripcion):
        if not descripcion.strip():
            print("La descripción no puede estar vacía.")
            return
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        self.guardar_tareas()
        print("Tarea agregada con éxito.")


    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return False
        print("\n📋 Lista de tareas:")
        for i, tarea in enumerate(self.tareas, start=1):
            estado = "Completada ✅" if tarea.completada else "Sin completar ❌"
            print(f"{i}. {tarea.descripcion} | {estado} | Creada: {tarea.fecha_creacion}")
        return True


    def completar_tarea(self, indice):
        if not self.validar_indice(indice):
            return
        tarea = self.tareas[indice]
        if tarea.completada:
            print("La tarea ya está marcada como completada.")
            return
        tarea.marcar_completada()
        self.guardar_tareas()
        print("Tarea marcada como completada.")


    def eliminar_tarea(self, indice):
        if not self.validar_indice(indice):
            return
        tarea_eliminada = self.tareas.pop(indice)
        self.guardar_tareas()
        print(f"Tarea '{tarea_eliminada.descripcion}' eliminada correctamente.")


    def validar_indice(self, indice):
        """Valida que el índice esté dentro del rango de tareas."""
        if not (0 <= indice < len(self.tareas)):
            print("Número de tarea no válido.")
            return False
        return True