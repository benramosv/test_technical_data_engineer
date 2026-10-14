# Evaluaciones Técnicas Data Engineer

Guía de evaluación práctica para los perfiles **Data Engineer Principiante Avanzado** y
**Data Engineer Competente** de Kyndryl.

Las evaluaciones están diseñadas para medir la capacidad de construir, validar y
operar pipelines de datos usando Databricks, PySpark, Spark SQL, ETL, Delta Lake,
Workflows, Notebooks y GitHub.

## Evaluaciones disponibles

| Nivel | Evaluación | Duración | Enfoque |
|---|---|---:|---|
| Principiante Avanzado | [02-data-engineer-principiante-avanzado/](./02-data-engineer-principiante-avanzado/) | 3.5 horas | Pipeline ETL completo, calidad y orquestación |
| Competente | [03-data-engineer-competente/](./03-data-engineer-competente/) | 3.5 horas | Incrementalidad, SCD Tipo 2, rendimiento y operación |

Cada evaluación incluye sus propias instrucciones, dataset, reglas de negocio,
templates y rúbrica:

- [Evaluación Principiante Avanzado](./02-data-engineer-principiante-avanzado/README.md)
- [Rúbrica Principiante Avanzado](./02-data-engineer-principiante-avanzado/RUBRICA-EVALUACION.md)
- [Evaluación Competente](./03-data-engineer-competente/README.md)
- [Rúbrica Competente](./03-data-engineer-competente/RUBRICA-EVALUACION.md)

## Objetivo de la evaluación

El candidato recibe un caso de negocio y un dataset sintético preparado por Kyndryl.
Debe implementar una solución funcional y explicar sus decisiones técnicas.

El candidato recibe:

- Dataset sintético en CSV y JSON.
- Diccionario de datos.
- Reglas de negocio y calidad.
- Templates iniciales de notebooks, tests y Workflows.
- Rúbrica de evaluación.

El candidato debe construir:

- Ingesta de datos.
- Capas Bronze, Silver y Gold.
- Transformaciones con PySpark.
- Consultas con Spark SQL.
- Tablas Delta.
- Controles de calidad y cuarentena.
- Databricks Workflow.
- Tests y validación en GitHub.
- Documentación y evidencias de ejecución.

Los datos son completamente sintéticos y no representan información real de
Kyndryl, sus empleados ni sus clientes.

## Duración y modalidad

Cada evaluación dura **3.5 horas / 210 minutos**:

| Actividad | Tiempo |
|---|---:|
| Trabajo práctico | 3 horas / 180 minutos |
| Revisión técnica | 30 minutos |
| **Total** | **3.5 horas / 210 minutos** |

Durante la revisión técnica, el candidato debe explicar la solución y resolver una
modificación o diagnóstico pequeño en vivo.

## Requisitos

### Obligatorio

- Cuenta de GitHub.
- Repositorio Git compartido con el evaluador.
- Capacidad para trabajar con Python y SQL.
- No incluir secretos, tokens ni datos reales en el repositorio.

### Recomendado

- Databricks Free Edition.
- Experiencia práctica con PySpark, Spark SQL y Delta Lake.
- Uso de GitHub Actions para validaciones.

### Alternativa de ejecución

Si Databricks Free Edition no está disponible, se acepta PySpark local para las
transformaciones. El candidato debe documentar las diferencias del entorno y
entregar la definición del Workflow solicitada.

Databricks Free Edition es el entorno recomendado, pero no debe convertirse en una
barrera administrativa para evaluar las competencias técnicas.

## Proceso de evaluación

1. El evaluador asigna el nivel correspondiente.
2. El candidato crea un fork o copia del repositorio base.
3. El candidato configura Databricks o el entorno local.
4. El candidato implementa la solución dentro de las 3 horas prácticas.
5. El candidato comparte el repositorio y las evidencias.
6. El evaluador revisa la entrega con la rúbrica correspondiente.
7. Se realiza una revisión técnica de 30 minutos.
8. Se calcula el puntaje final y la recomendación.

## Criterios generales

La evaluación considera tanto el resultado como el criterio de ingeniería:

- Corrección de las transformaciones.
- Calidad y confiabilidad de los datos.
- Reproducibilidad e idempotencia.
- Claridad y mantenibilidad del código.
- Uso apropiado de PySpark y Spark SQL.
- Diseño de Workflows y manejo de errores.
- Trazabilidad mediante GitHub.
- Capacidad de explicar y defender las decisiones.

## Escala de resultados

| Puntaje | Resultado |
|---:|---|
| 90–100 | Sobresaliente |
| 70–89 | Aprobado |
| 50–69 | En desarrollo |
| Menor de 50 | No aprobado |

Para el nivel Competente, además del puntaje mínimo, el candidato debe demostrar un
nivel suficiente de incrementalidad, calidad de datos y manejo de fallos.

## Preguntas de revisión sugeridas

### Principiante Avanzado

- ¿Por qué separaste Bronze, Silver y Gold?
- ¿Cómo evitas duplicados en una segunda ejecución?
- ¿Qué harías si llega un archivo corrupto?
- ¿Cuándo usarías PySpark y cuándo Spark SQL?
- ¿Qué regla de calidad consideras crítica?

### Competente

- ¿Cómo harías el pipeline idempotente?
- ¿Cómo manejarías datos que llegan tarde?
- ¿Cómo implementarías SCD Tipo 2?
- ¿Dónde puede aparecer un shuffle costoso o data skew?
- ¿Cómo recuperarías una ejecución parcialmente fallida?
- ¿Cómo promoverías el Workflow entre ambientes?

## Estructura del repositorio

```text
.
├── README.md
├── README-DATA-ENGINEER.md
├── 02-data-engineer-principiante-avanzado/
│   ├── README.md
│   ├── RUBRICA-EVALUACION.md
│   ├── data/
│   ├── requirements/
│   └── templates/
└── 03-data-engineer-competente/
    ├── README.md
    ├── RUBRICA-EVALUACION.md
    ├── data/
    ├── requirements/
    └── templates/
```
