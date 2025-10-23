# Este archivo define la estructura de una tarea: qué información guarda, cómo se marca como completada, y cómo se convierte a/desde JSON.


import datetime

class Tarea:
    def __init__(self, descripcion, completada=False, fecha_creacion=None):
        self.descripcion = descripcion.strip()  
        self.completada = completada    
        self.fecha_creacion = fecha_creacion or datetime.datetime.now().strftime("%d-%m-%Y %H:%M")


    def marcar_completada(self):
        self.completada = True


    def to_dict(self):
        """Convierte el objeto Tarea a un diccionario (para guardar en JSON)."""
        return {
            "descripcion": self.descripcion,
            "completada": self.completada,
            "fecha_creacion": self.fecha_creacion
        }


    @classmethod
    def from_dict(cls, data):
        """Crea una tarea(objeto) a partir de un diccionario (lee del JSON)."""
        return cls(
            descripcion=data["descripcion"],
            completada=data["completada"],
            fecha_creacion=data["fecha_creacion"]
        )
