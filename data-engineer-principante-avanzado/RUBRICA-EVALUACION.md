# Hoja de evaluación — Data Engineer Semi Senior

## Candidato

- **Nombre:**
- **Fecha:**
- **Evaluador:**
- **Tiempo utilizado:**
- **Repositorio:**
- **Entorno:** Databricks Free Edition / local / otro

## Rúbrica

| Sección | Criterio | Máx | Obtenido | Notas |
|---|---|---:|---:|---|
| Ingesta y Bronze | Esquemas, metadatos, persistencia Delta y reproducibilidad | 50 | | |
| Ingesta y Bronze | Manejo de archivos o registros inválidos | 25 | | |
| Ingesta y Bronze | Claridad del notebook y configuración | 25 | | |
| **Subtotal** | **Ingesta y Bronze** | **100** | | |
| Silver PySpark | Tipos, fechas, nulos y deduplicación | 30 | | |
| Silver PySpark | Joins, ventanas y reglas de transformación | 30 | | |
| Silver PySpark | Cuarentena y trazabilidad | 25 | | |
| Silver PySpark | Legibilidad y modularidad | 15 | | |
| **Subtotal** | **Silver PySpark** | **100** | | |
| Gold y Spark SQL | Tres productos Gold correctos | 35 | | |
| Gold y Spark SQL | Consultas de negocio correctas | 30 | | |
| Gold y Spark SQL | Elección razonada entre PySpark y SQL | 20 | | |
| Gold y Spark SQL | Modelo y nombres mantenibles | 15 | | |
| **Subtotal** | **Gold y Spark SQL** | **100** | | |
| Calidad | Completitud, unicidad, validez e integridad | 45 | | |
| Calidad | Métricas y evidencia de resultados | 30 | | |
| Calidad | Separación entre error y advertencia | 25 | | |
| **Subtotal** | **Calidad** | **100** | | |
| Workflow | Dependencias y parámetro de fecha | 35 | | |
| Workflow | Reintentos y ejecución demostrable | 35 | | |
| Workflow | Configuración sin secretos ni rutas personales | 30 | | |
| **Subtotal** | **Workflow** | **100** | | |
| GitHub y documentación | Validación automatizada y commits | 25 | | |
| GitHub y documentación | README reproducible | 30 | | |
| GitHub y documentación | Decisiones y evidencias | 25 | | |
| GitHub y documentación | Tests de transformaciones | 20 | | |
| **Subtotal** | **GitHub y documentación** | **100** | | |

## Resultado ponderado

| Sección | Peso | Puntaje | Aporte |
|---|---:|---:|---:|
| Ingesta y Bronze | 20% | | |
| Silver PySpark | 25% | | |
| Gold y Spark SQL | 20% | | |
| Calidad | 15% | | |
| Workflow | 10% | | |
| GitHub y documentación | 10% | | |
| **TOTAL** | **100%** | | **___ / 100** |

### Nivel alcanzado

- [ ] No aprobado — menor de 50
- [ ] En desarrollo — 50 a 69
- [ ] Aprobado — 70 a 89
- [ ] Sobresaliente — 90 a 100

## Condiciones críticas

No se recomienda aprobar si el candidato no puede ejecutar el pipeline completo,
no distingue datos válidos de inválidos o no puede explicar cómo evitar duplicados.

## Preguntas de revisión

| Pregunta | Evidencia / respuesta | Puntaje cualitativo |
|---|---|---|
| ¿Cómo reprocesarías una fecha? | | |
| ¿Qué ocurre con un archivo corrupto? | | |
| ¿Qué transformación optimizarías primero? | | |
| ¿Cómo probarías una regla de calidad? | | |

## Observaciones y recomendación

```text

```

- [ ] Apto para Data Engineer Semi Senior
- [ ] Apto con plan de desarrollo
- [ ] Repetir evaluación
- [ ] No apto para el rol