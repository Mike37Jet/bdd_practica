# logica/asignatura.py
from typing import Dict
from logica.objetivo_carrera import ObjetivoCarrera

class Asignatura:
    def __init__(self, nombre: str, contribuciones: Dict[ObjetivoCarrera, int] = None):
        self.nombre = nombre
        self.contribuciones = contribuciones if contribuciones else {}

    def contribuye_a(self, obj: ObjetivoCarrera) -> bool:
        return obj in self.contribuciones and self.contribuciones[obj] > 0

    def valor_para(self, obj: ObjetivoCarrera) -> int:
        return self.contribuciones.get(obj, 0)

    def establecer_valor_para(self, obj: ObjetivoCarrera, valor: int) -> None:
        self.contribuciones[obj] = valor