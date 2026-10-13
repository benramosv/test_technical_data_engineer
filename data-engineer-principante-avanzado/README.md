# Evaluación Data Engineer — Semi Senior

## Propósito

Esta evaluación práctica está diseñada para candidatos Data Engineer Semi Senior.
Evalúa la capacidad de construir un pipeline ETL reproducible sobre **Databricks,
PySpark, Spark SQL, Delta Lake, Workflows, Notebooks y GitHub**.

El candidato recibe el dataset sintético y las reglas del negocio. No recibe la
solución, las consultas finales ni los workflows resueltos.

## Contexto

Kyndryl necesita consolidar información operacional de clientes, proyectos,
registros de trabajo e incidentes. Las fuentes llegan como CSV y JSON y contienen
problemas intencionales de calidad: duplicados, nulos, fechas inconsistentes,
valores fuera de rango y registros que deben ser enviados a cuarentena.

El objetivo es construir un flujo:

```text
Archivos raw -> Bronze -> Silver -> Gold -> controles de calidad
```

Los datos de esta evaluación son sintéticos y no representan información real de
Kyndryl ni de sus clientes.

## Tiempo y modalidad

- Duración total: 3.5 horas.
- Trabajo práctico cronometrado: 3 horas.
- Revisión técnica: 30 minutos.
- Entrega: al finalizar la sesión o dentro del plazo acordado con Kyndryl.
- Se permite consultar documentación oficial y utilizar herramientas de IA.
- El candidato debe poder explicar y modificar su solución durante la revisión.

## Requisitos del entorno

### Opción recomendada: Databricks Free Edition

1. Crear una cuenta de Databricks Free Edition.
2. Crear un workspace o entorno de trabajo disponible.
3. Crear un repositorio personal o clonar el repositorio de entrega.
4. Subir la carpeta `data/` al volumen, catálogo o ubicación de archivos elegida.
5. Ejecutar los notebooks en el orden indicado.

La disponibilidad de Free Edition puede variar por región o por las características
habilitadas en la cuenta. No se debe compartir ningún token con el evaluador.

### Alternativa local

Se acepta PySpark local si Databricks no está disponible. El candidato debe
documentar las diferencias del entorno y demostrar que las transformaciones son
equivalentes. La evaluación de Workflows se puede entregar como definición YAML o
JSON documentada, aunque la ejecución en Databricks es preferible.

## Material entregado por Kyndryl

- `data/`: archivos CSV y JSON sintéticos.
- `data/DATA-DICTIONARY.md`: definición de campos.
- `requirements/business-rules.md`: reglas funcionales y de calidad.
- `templates/notebooks/`: esqueletos de notebooks sin solución.
- `templates/tests/`: estructura para pruebas unitarias.
- `templates/workflows/`: ejemplo de estructura, sin tareas resueltas.

## Estructura esperada de la entrega

```text
mi-solucion/
├── data/
├── notebooks/
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transformations.py
│   ├── 03_gold_transformations.py
│   └── 04_data_quality.py
├── tests/
├── workflows/
│   └── daily-etl.yml
├── docs/
│   └── architecture.md
├── .github/
│   └── workflows/
│       └── validate.yml
└── README.md
```

## Tareas

### Distribución del tiempo

| Bloque | Tiempo sugerido |
|---|---:|
| Lectura del caso y configuración | 15 min |
| Bronze y Silver | 75 min |
| Gold y Spark SQL | 45 min |
| Calidad y Workflow | 30 min |
| README, tests y evidencias | 15 min |
| **Trabajo práctico** | **180 min** |
| Revisión técnica | 30 min |
| **Total** | **210 min / 3.5 h** |

El candidato debe priorizar una solución ejecutable de extremo a extremo. Las
optimizaciones adicionales no son obligatorias si comprometen la ejecución completa.

### 1. Ingesta y Bronze — 20 puntos

Implementa `01_bronze_ingestion` para leer todos los archivos de entrada y
persistir tablas o rutas Delta Bronze. Debe:

- Definir esquemas explícitos para las fuentes principales.
- Añadir `ingestion_timestamp` y `source_file`.
- Conservar los datos originales tanto como sea razonable.
- Registrar o separar archivos y registros no procesables.
- Hacer la carga reproducible para una segunda ejecución.

### 2. Silver con PySpark — 25 puntos

Implementa `02_silver_transformations` para limpiar y estandarizar los datos:

- Convertir tipos y fechas.
- Eliminar duplicados con una regla explicada.
- Tratar nulos según las reglas del negocio.
- Validar rangos y relaciones básicas.
- Usar joins, agregaciones y funciones de ventana donde corresponda.
- Enviar registros inválidos a cuarentena.

### 3. Gold y Spark SQL — 20 puntos

Implementa `03_gold_transformations` y crea al menos tres productos analíticos:

- Resumen de proyectos y horas trabajadas.
- Actividad y carga operacional por cliente.
- Métricas de incidentes y tiempo de resolución.

Incluye consultas Spark SQL que respondan las preguntas de negocio en
`requirements/business-rules.md`. Explica en el README cuándo elegiste PySpark y
cuándo Spark SQL.

### 4. Calidad de datos — 15 puntos

Implementa `04_data_quality` con controles de completitud, unicidad, validez,
integridad referencial y conteo de rechazados. El resultado debe dejar evidencia
de qué reglas pasaron, cuáles fallaron y cuántos registros fueron afectados.

### 5. Workflow — 10 puntos

Define un Databricks Workflow con tareas dependientes:

```text
ingestion -> silver -> gold -> data_quality
```

Incluye un parámetro de fecha de proceso, reintentos razonables y evidencia de una
ejecución exitosa. No hardcodees credenciales ni rutas específicas de tu usuario.

### 6. GitHub y documentación — 10 puntos

El repositorio debe incluir historial de commits entendible, un workflow de
validación, instrucciones reproducibles, decisiones técnicas y capturas o enlaces
a las ejecuciones relevantes.

## Entregables

1. Repositorio GitHub compartido con el evaluador.
2. Notebooks ejecutables y código fuente.
3. Definición del Workflow y evidencia de ejecución.
4. README con instrucciones, decisiones y resultados.
5. Tests de las transformaciones principales.
6. Evidencia de controles de calidad y registros en cuarentena.

## Revisión técnica

El candidato debe explicar el pipeline y resolver una modificación pequeña en vivo.
El evaluador puede preguntar:

- ¿Por qué separaste Bronze, Silver y Gold?
- ¿Cómo evitas duplicados en una segunda ejecución?
- ¿Qué harías si llega un archivo corrupto?
- ¿Por qué una transformación está en PySpark y otra en Spark SQL?
- ¿Qué regla de calidad consideras crítica?

## Restricciones

- No usar datos reales ni secretos de Kyndryl.
- No incluir tokens, contraseñas o credenciales en el repositorio.
- No entregar tablas Gold preconstruidas como sustituto del código.
- Todas las decisiones relevantes deben estar documentadas.