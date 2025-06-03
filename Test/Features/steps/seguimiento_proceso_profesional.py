from behave import *
from logica.objetivo_carrera import ObjetivoCarrera
from logica.asignatura import Asignatura
from logica.historial_de_desempeno import HistorialDeDesempeño
from logica.estudiante import Estudiante
from logica.sistema import Sistema

use_step_matcher("re")


@step("que el estudiante tiene registrado al menos un historial de perfil estudiantil")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    algoritmos = Asignatura("Algoritmos", {
        ObjetivoCarrera.SISTEMAS: 80,
        ObjetivoCarrera.CALIDAD: 30
    })

    proyectos = Asignatura("Gestión de Proyectos", {
        ObjetivoCarrera.PROYECTOS: 90,
        ObjetivoCarrera.EMPRENDIMIENTO: 40
    })

    # Crear historial de desempeño
    historial_estudiante = HistorialDeDesempeño()
    historial_estudiante.registrar_progreso(1, {
        ObjetivoCarrera.CALIDAD: 65,
        ObjetivoCarrera.PROYECTOS: 80,
        ObjetivoCarrera.SISTEMAS: 75
    })

    # Crear estudiante de prueba
    context.estudiante = Estudiante(
        "1726624289",
        "Juan Pérez",
        [algoritmos, proyectos],
        historial_estudiante,
        2
    )

    # Crear otro estudiante para la media
    historial_otro = HistorialDeDesempeño()
    historial_otro.registrar_progreso(2, {
        ObjetivoCarrera.CALIDAD: 70,
        ObjetivoCarrera.SISTEMAS: 85
    })

    otro_estudiante = Estudiante(
        "172689",
        "Pepe García",
        [algoritmos],
        historial_otro,
        2
    )

    # Lista de estudiantes para el sistema
    context.estudiantes = [context.estudiante, otro_estudiante]


@step("el umbral de aceptación mínimo es de 70")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.umbral = 70

@step('la carrera "Sistemas" tiene definidos los siguientes objetivos de aprendizaje:')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verificamos que la tabla de datos exista
    assert context.table, "La tabla de objetivos de aprendizaje no está definida"

    # Guardamos los objetivos de aprendizaje en el contexto para usarlos en pasos posteriores
    context.objetivos_aprendizaje = []
    for row in context.table:
        # La columna se llama "Objetivo de carrera" según el feature
        context.objetivos_aprendizaje.append(row["Objetivo de carrera"])

    # Verificamos que se hayan cargado todos los objetivos
    assert len(context.objetivos_aprendizaje) == 5, "No se cargaron todos los objetivos de aprendizaje esperados"

    # Creamos el sistema con los objetivos
    context.sistema = Sistema(
        context.estudiantes,
        context.umbral,
        ObjetivoCarrera.CALIDAD,
        ObjetivoCarrera.PROYECTOS,
        ObjetivoCarrera.INVESTIGACION,
        ObjetivoCarrera.SISTEMAS,
        ObjetivoCarrera.EMPRENDIMIENTO
    )

@step("consulte el progreso del historial")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Ejecutamos el seguimiento para el estudiante
    progresos, media, recomendaciones = context.sistema.ejecutar_seguimiento(context.estudiante.id)

    # Guardamos los resultados en el contexto
    context.progresos = progresos
    context.media = media
    context.recomendaciones = recomendaciones

@step("mostrará un porcentaje de progreso por cada objetivo")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verificamos que se hayan generado progresos para cada objetivo
    assert context.progresos, "No se obtuvieron progresos"

    # Verificamos que haya al menos un objetivo con progreso
    assert len(context.progresos) > 0, "No hay objetivos con progreso"

    # Verificamos que los porcentajes estén en el rango correcto
    for objetivo, valor in context.progresos.items():
        assert 0 <= valor <= 100, f"El progreso para {objetivo.name} está fuera del rango (0-100): {valor}"


@step("se mostrará la media de progreso de estudiantes")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verificamos que la media se haya calculado
    assert context.media is not None, "No se calculó la media de progreso"

    # Verificamos que la media esté en el rango correcto
    assert 0 <= context.media <= 100, f"La media de progreso está fuera del rango (0-100): {context.media}"

    # Mostrar resultados (opcional, para debug)
    print(f"Progresos: {[(obj.name, valor) for obj, valor in context.progresos.items()]}")
    print(f"Media del semestre: {context.media}")
    print(f"Recomendaciones: {context.recomendaciones}")


# OTRO ESCENARIO: Recomendaciones para mejorar el progreso
@step("se mostrará una serie de recomendaciones para mejorar el progreso")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # Verificamos que se hayan generado recomendaciones
    assert context.recomendaciones, "No se generaron recomendaciones"

    # Verificamos que haya al menos una recomendación
    assert len(context.recomendaciones) > 0, "No hay recomendaciones para el estudiante"

    # Verificamos que cada recomendación tenga el formato esperado
    for recomendacion in context.recomendaciones:
        assert "Mejorar en" in recomendacion, f"La recomendación no tiene el formato esperado: {recomendacion}"

    # Mostrar recomendaciones (opcional, para debug)
    print(f"Recomendaciones generadas: {context.recomendaciones}")