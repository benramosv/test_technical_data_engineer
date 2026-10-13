# Evaluación Data Engineer — Senior

## Propósito

Esta evaluación práctica está diseñada para un Data Engineer Senior. Evalúa la
capacidad de diseñar y entregar una solución de datos preparada para producción
con **Databricks, PySpark, Spark SQL, Delta Lake, Workflows, Notebooks y GitHub**.

El candidato recibe un problema, datos sintéticos y restricciones. Debe tomar y
justificar las decisiones de arquitectura. No recibe una solución de referencia.

## Contexto

Kyndryl necesita industrializar un pipeline operacional de clientes, proyectos,
registros de trabajo e incidentes. El pipeline se ejecutará diariamente, recibirá
datos retrasados y deberá soportar reintentos y reprocesamiento sin duplicar datos.

Los datos son sintéticos y no representan información real de Kyndryl ni de sus
clientes.

```text
Fuentes -> Landing/Bronze -> Silver -> Gold -> consumidores analíticos
                  |             |          |
             auditoría      calidad    métricas
```

## Tiempo y modalidad

- Duración total: 3.5 horas.
- Trabajo práctico cronometrado: 3 horas.
- Revisión técnica: 30 minutos.
- Entrega: al finalizar la sesión o dentro del plazo acordado con Kyndryl.
- Se permite consultar documentación oficial y utilizar herramientas de IA.
- El candidato debe defender, modificar y diagnosticar su solución en vivo.

## Requisitos del entorno

Se recomienda Databricks Free Edition. También se acepta ejecución local con
PySpark para las transformaciones, pero el candidato debe documentar las
diferencias y entregar la definición del Workflow aunque no pueda ejecutarlo.

GitHub es obligatorio para la entrega y la trazabilidad. El repositorio puede ser
privado y compartirse únicamente con los evaluadores. Nunca deben subirse tokens,
secretos ni datos reales.

## Material entregado por Kyndryl

- `data/`: archivos CSV y JSON sintéticos, con problemas intencionales.
- `data/DATA-DICTIONARY.md`: contrato inicial de campos.
- `requirements/business-rules.md`: requisitos funcionales y restricciones.
- `templates/`: esqueletos sin solución.

El candidato debe completar el diseño y puede proponer una estructura distinta si
la justifica en un ADR.

## Estructura esperada de la entrega

```text
mi-solucion/
├── data/
├── notebooks/
│   ├── 01_incremental_bronze.py
│   ├── 02_silver_scd2.py
│   ├── 03_gold_metrics.sql
│   └── 04_quality_observability.py
├── workflows/
│   └── daily-etl.yml
├── tests/
├── docs/
│   ├── architecture.md
│   ├── ADR-001-incremental-processing.md
│   ├── data-quality.md
│   └── runbook.md
├── .github/workflows/
│   ├── validate.yml
│   └── deploy.yml
└── README.md
```

## Tareas

### Distribución del tiempo

| Bloque | Tiempo sugerido |
|---|---:|
| Lectura del caso y diseño | 20 min |
| Ingesta incremental y Silver | 70 min |
| Gold y SCD Tipo 2 | 35 min |
| Calidad, Workflow y CI/CD | 35 min |
| Documentación y evidencias | 20 min |
| **Trabajo práctico** | **180 min** |
| Revisión técnica | 30 min |
| **Total** | **210 min / 3.5 h** |

El entregable mínimo debe demostrar un flujo ejecutable, idempotencia, una
dimensión histórica o su diseño detallado, controles de calidad y una estrategia
operativa. El análisis profundo de rendimiento, observabilidad avanzada y
promoción multiambiente puede entregarse como extensión si el tiempo restante no
permite implementarlo completamente.

### 1. Arquitectura — 20 puntos

Entrega un diagrama y una descripción de la solución. Debe explicar:

- Capas Bronze, Silver y Gold.
- Formato Delta y estrategia de tablas.
- Separación de ambientes.
- Seguridad y gestión de configuración.
- Freshness esperada y consumidores.
- Decisiones de costo y operación.

### 2. Ingesta incremental y Delta Lake — 20 puntos

Implementa una ingesta que soporte ejecuciones repetidas y archivos o registros
retrasados. Debe incluir una estrategia clara para:

- Idempotencia.
- Watermark o control table.
- Detección de datos ya procesados.
- `MERGE` o mecanismo equivalente.
- Reprocesamiento de una fecha.
- Fallo a mitad de una ejecución.
- Evolución de esquema.

### 3. Silver, SCD Tipo 2 y Gold — 20 puntos

Implementa una dimensión histórica, como `dim_customer` o `dim_project`, con
`effective_from`, `effective_to` e `is_current`. Crea productos Gold para las
métricas de negocio y consultas Spark SQL que respondan las preguntas entregadas.

### 4. Rendimiento y escalabilidad — 15 puntos

Incluye un análisis técnico con evidencia o razonamiento sobre:

- Particiones y tamaño de archivos.
- `repartition` frente a `coalesce`.
- Broadcast joins.
- Shuffles y posibles datos sesgados.
- Selección de columnas y filtros tempranos.
- Small files y mantenimiento de Delta.
- Cuándo usar persistencia o cache.

No basta con mencionar términos: relaciona cada decisión con este pipeline.

### 5. Calidad y observabilidad — 15 puntos

Implementa controles reutilizables para completitud, unicidad, validez, integridad
referencial, volumen y freshness. El sistema debe registrar métricas por ejecución,
distinguir errores críticos de advertencias y permitir auditar registros rechazados.

### 6. Workflow y resiliencia — 5 puntos

Define tareas con dependencias, parámetros, timeouts, reintentos, notificación ante
fallo y una tarea de calidad. Incluye evidencia de una ejecución correcta y un caso
de fallo o reprocesamiento.

### 7. CI/CD, operación y documentación — 5 puntos

Incluye validación en Pull Request, tests, lint o compilación, validación de la
configuración del Workflow y una estrategia de promoción entre ambientes. Entrega
un runbook, un ADR y una guía de despliegue sin secretos en el repositorio.

## Entregables

1. Repositorio GitHub con historial trazable.
2. Notebooks y consultas ejecutables.
3. Workflow de Databricks parametrizado.
4. Tests y resultados de calidad.
5. Diagrama y ADRs.
6. Análisis de rendimiento.
7. Runbook de fallo, reprocesamiento y rollback lógico.
8. Evidencia de ejecución y README reproducible.

## Revisión técnica

El evaluador puede introducir una modificación en vivo y preguntar:

- ¿Cómo harías el pipeline idempotente?
- ¿Qué ocurre si llega un registro tardío después del cierre del día?
- ¿Cómo detectarías data skew y un shuffle costoso?
- ¿Cómo promoverías el Workflow entre desarrollo y producción?
- ¿Qué harías ante una ejecución parcialmente fallida?
- ¿Qué regla de calidad bloquearía el pipeline?

## Condiciones críticas

Para aprobar, el candidato debe demostrar dominio suficiente de incrementalidad,
calidad de datos y manejo de fallos. Una solución con transformaciones correctas
pero sin estrategia operacional no alcanza el nivel Senior.