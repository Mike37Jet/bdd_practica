# logica/main.py
from logica.objetivo_carrera import ObjetivoCarrera
from logica.asignatura import Asignatura
from logica.historial_de_desempeño import HistorialDeDesempeño
from logica.estudiante import Estudiante
from logica.sistema import Sistema

# Ejemplo de uso:

# Crear algunas asignaturas
algoritmos = Asignatura("Algoritmos", {
    ObjetivoCarrera.SISTEMAS: 80,
    ObjetivoCarrera.CALIDAD: 30
})

proyectos = Asignatura("Gestión de Proyectos", {
    ObjetivoCarrera.PROYECTOS: 90,
    ObjetivoCarrera.EMPRENDIMIENTO: 40
})

# Crear historial de desempeño
historial_juan = HistorialDeDesempeño()
historial_juan.registrar_progreso(1, {
    ObjetivoCarrera.CALIDAD: 65,
    ObjetivoCarrera.PROYECTOS: 80,
    ObjetivoCarrera.SISTEMAS: 75
})

# Crear estudiantes
juan = Estudiante(
    "1726624289",
    "Juan Pérez",
    [algoritmos, proyectos],
    historial_juan,
    2
)

pepe = Estudiante(
    "172689",
    "Pepe García",
    [algoritmos],
    HistorialDeDesempeño(),
    1
)

# Crear sistema
sistema = Sistema(
    [juan, pepe],
    70,  # umbral
    ObjetivoCarrera.CALIDAD,
    ObjetivoCarrera.PROYECTOS,
    ObjetivoCarrera.INVESTIGACION,
    ObjetivoCarrera.SISTEMAS,
    ObjetivoCarrera.EMPRENDIMIENTO
)

# Ejecutar seguimiento
if __name__ == "__main__":
    progresos, media, recomendaciones = sistema.ejecutar_seguimiento("1726624289")
    print(f"Progresos de Juan: {[(obj.name, valor) for obj, valor in progresos.items()]}")
    print(f"Media del semestre: {media}")
    print(f"Recomendaciones: {recomendaciones}")