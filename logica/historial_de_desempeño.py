# logica/historial_desempeño.py
from typing import Dict, List
from logica.objetivo_carrera import ObjetivoCarrera

class HistorialDeDesempeño:
    def __init__(self, registros: Dict[int, Dict[ObjetivoCarrera, float]] = None):
        self.registros = registros if registros else {}

    def registrar_progreso(self, semestre: int, progreso: Dict[ObjetivoCarrera, float]) -> None:
        self.registros[semestre] = progreso

    def obtener_progreso(self, semestre: int) -> Dict[ObjetivoCarrera, float]:
        return self.registros.get(semestre, {})

    def calcular_evolucion(self, obj: ObjetivoCarrera) -> List[float]:
        return [self.registros[semestre].get(obj, 0) for semestre in sorted(self.registros.keys()) if obj in self.registros[semestre]]