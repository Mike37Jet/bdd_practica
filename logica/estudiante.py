# logica/estudiante.py
from typing import Dict, List
from logica.objetivo_carrera import ObjetivoCarrera
from logica.asignatura import Asignatura
from logica.historial_de_desempeño import HistorialDeDesempeño

class Estudiante:
    def __init__(self, id: str, nombre: str, asignaturas: List[Asignatura] = None, historial: HistorialDeDesempeño = None, semestreActual: int = 1):
        self.id = id
        self.nombre = nombre
        self.asignaturas = asignaturas if asignaturas else []
        self.historial = historial if historial else HistorialDeDesempeño()
        self.semestreActual = semestreActual

    def calcular_progreso_actual(self, objetivos: List[ObjetivoCarrera]) -> Dict[ObjetivoCarrera, float]:
        resultado = {}
        for objetivo in objetivos:
            # Lógica simplificada para el cálculo del progreso
            total_contribucion = sum(asignatura.valor_para(objetivo) for asignatura in self.asignaturas)
            # Normalizar a un porcentaje (suponiendo 100 como máximo posible por objetivo)
            resultado[objetivo] = min(100, (total_contribucion / 100) * 100) if total_contribucion > 0 else 0
        return resultado