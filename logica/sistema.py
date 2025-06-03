# logica/sistema.py
from typing import Dict, List, Tuple
from logica.objetivo_carrera import ObjetivoCarrera
from logica.estudiante import Estudiante

class Sistema:
    def __init__(self, estudiantes: List[Estudiante] = None, umbral: int = 70, *objetivos: ObjetivoCarrera):
        self.estudiantes = estudiantes if estudiantes else []
        self.objetivos = list(objetivos) if objetivos else list(ObjetivoCarrera)
        self.umbral = umbral

    def ejecutar_seguimiento(self, id_estudiante: str) -> Tuple[Dict[ObjetivoCarrera, float], float, List[str]]:
        estudiante = next((e for e in self.estudiantes if e.id == id_estudiante), None)
        if not estudiante:
            return {}, 0, ["Estudiante no encontrado"]

        progresos = estudiante.calcular_progreso_actual(self.objetivos)
        media = self.calcular_media(estudiante.semestreActual)
        recomendaciones = self.generar_recomendaciones(progresos)

        return progresos, media, recomendaciones

    def calcular_media(self, semestre: int) -> float:
        # Calcula la media de progreso de todos los estudiantes para el semestre indicado
        total = 0
        count = 0

        for estudiante in self.estudiantes:
            if semestre in estudiante.historial.registros:
                valores = list(estudiante.historial.registros[semestre].values())
                if valores:
                    total += sum(valores) / len(valores)
                    count += 1

        return total / count if count > 0 else 0

    def generar_recomendaciones(self, progresos: Dict[ObjetivoCarrera, float]) -> List[str]:
        recomendaciones = []
        for objetivo, valor in progresos.items():
            if valor < self.umbral:
                recomendaciones.append(f"Mejorar en {objetivo.name}: {objetivo.value}. Actual: {valor}%")
        return recomendaciones