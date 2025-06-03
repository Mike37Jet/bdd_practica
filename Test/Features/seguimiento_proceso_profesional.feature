# Created by Emilio Jacome at 27/5/2025
# language: es

Característica: Seguimiento de autoevaluación de progreso profesional
  Como estudiante de la EPN
  Quiero conocer mi progreso profesional a lo largo de cada semestre en relación a los objetivos de carrera
  Para determinar posibles falencias en mi proceso académico y tomar acciones correctivas

  Antecedentes:
    Dado que el estudiante tiene registrado al menos un historial de perfil estudiantil

  Esquema del escenario: Seguimiento sin falencias
    Y el umbral de aceptación mínimo es de 70
    Y la carrera de sistemas tiene los siguientes objetivos "<VALUE>", "<VALUE>"
    Cuando consulte el progreso del historial
    Entonces mostrará un porcentaje de progreso por cada objetivo
    Ejemplos:
      | Objetivo   | Definición                                                                                                   |
      | objetivo 1 | Verificación, validación y aseguramiento de la calidad del Software                                          |
      | objetivo 1 | Administración de proyectos de Software                                                                      |
      | objetivo 1 | Investigación aplicada en proyectos de conceptualización, desarrollo, innovación y transferencia de Software |
      | objetivo 1 | Ingeniería de Software para el desarrollo de Sistemas de Información y Sistemas Inteligentes                 |
      | objetivo 1 | Emprendimiento de empresas de investigación, innovación, desarrollo y comercialización de Software           |
    #feature_seguimineto_001
    Y se mostrará la media de progreso de estudiantes

    #Tarea - Leer documentación Cucumber
  Escenario: Seguimiento con falencias
    Y el umbral de aceptación mínimo es de 70
    Cuando consulte el progreso del historial
    Entonces mostrará un porcentaje de progreso por cada objetivo
    #feature_seguimineto_001
    Y se mostrará la media de progreso de estudiantes
    Y se mostrará una serie de recomendaciones para mejorar el progreso

