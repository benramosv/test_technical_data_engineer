# Cronograma de sesiones · Data Engineer

**AI & Data Summer Bootcamp · Technical Evolution**

| | |
|---|---|
| Versión | 0.6 preliminar · 19-nov-2026 · para revisión de los coaches de Data Engineer y aprobación del Workstream Lead |
| Base | Material del Upskilling Program de junio 2026 (Niveles 1–5), más material nuevo |
| Sesiones | 41 de 1 hora, lunes a viernes de 17:00 a 18:00, del 1-dic-2026 al 19-feb-2027 |
| Breaks | 7–9 dic y 21 dic – 8 ene (sin clases) |

## Resumen

| Origen | Sesiones |
|---|---|
| Material base: Upskilling Program, Niveles 1–5 | 25 |
| Material nuevo: Databricks | 4 |
| Material nuevo: Modeling & Reliability, Streaming, Quality & Governance y caso integrador | 12 |
| **Total** | **41** |

El curso reutiliza el material del Upskilling Program de junio 2026, organizado en cinco niveles, y lo completa con material nuevo. Los módulos llevan los nombres de los bloques de la infografía "Data Engineer Interview Prep", que usamos como referencia de los conceptos que necesita un Data Engineer. La columna "Material base" indica qué nivel del Upskilling Program se usa en cada módulo.

Los módulos van en el orden de ese material. Diciembre cubre completos Fundamentals & Architecture y Storage & Modeling. Fundamentals & Architecture tiene una sesión adicional de práctica guiada de SQL, porque es el módulo más denso y SQL es el piso de todo el programa. Databricks entra justo antes de Ingestion & Processing III · Apache Spark, para que los laboratorios de Spark se hagan en notebooks de Databricks, y vuelve después con Unity Catalog, Delta y orquestación. Modeling & Reliability y Streaming, Quality & Governance cubren lo que el Upskilling Program no trae: modelado dimensional, cargas incrementales, idempotencia, streaming, CDC, calidad de datos y CI/CD. Todos los laboratorios trabajan sobre un mismo caso práctico.

Cada módulo termina con una sesión de caso práctico. Las 2 horas semanales de autoestudio se usan para terminar ese caso.

| Módulo | Material base | Sesiones | N.º de sesión | Fechas |
|---|---|---|---|---|
| Fundamentals & Architecture | Nivel 1 · Fundamentos de Datos | 7 | 1–7 | mar 1 dic – lun 14 dic |
| Storage & Modeling | Nivel 2 · Arquitectura Moderna de Datos | 4 | 8–11 | mar 15 dic – vie 18 dic |
| Ingestion & Processing I · Azure Data Platform | Nivel 3 · Azure Data Platform | 5 | 12–16 | lun 11 ene – vie 15 ene |
| Ingestion & Processing II · Python | Nivel 4 · Python para Ingeniería de Datos | 4 | 17–20 | lun 18 ene – jue 21 ene |
| Databricks | — (material nuevo) | 4 | 21, 27–29 | vie 22 ene – mié 3 feb |
| Ingestion & Processing III · Apache Spark | Nivel 5 · Apache Spark y PySpark | 5 | 22–26 | lun 25 ene – vie 29 ene |
| Modeling & Reliability | — (material nuevo) | 4 | 30–33 | jue 4 feb – mar 9 feb |
| Streaming, Quality & Governance | — (material nuevo) | 4 | 34–37 | mié 10 feb – lun 15 feb |
| Caso integrador | — (material nuevo) | 4 | 38–41 | mar 16 feb – vie 19 feb |

## Detalle por sesión

La columna "Material base" indica qué láminas del Upskilling Program (o qué guías, en el Nivel 3) sirven de base para cada sesión.

| # | Fecha | Módulo | Tema | Material base |
|---|---|---|---|---|
| 1 | mar 1 dic | Fundamentals & Architecture | ¿Qué es Data Engineering? Ciclo de vida del dato, OLTP vs OLAP, datos estructurados, semiestructurados y no estructurados | Nivel 1, láminas 2–7 |
| 2 | mié 2 dic | Fundamentals & Architecture | Formatos de archivo: CSV, JSON, XML, BLOB, Parquet, Avro y Delta Lake | Nivel 1, láminas 8–14 |
| 3 | jue 3 dic | Fundamentals & Architecture | Bases relacionales y NoSQL, B-Tree; data warehouse, data mart, data lake y lakehouse | Nivel 1, láminas 15–23 |
| 4 | vie 4 dic | Fundamentals & Architecture | SQL: JOINs, CTE, GROUP BY, EXTRACT. Ejercicios 1, 2, 3 y 5 | Nivel 1, láminas 24–26, 34–38, 40 |
| 5 | jue 10 dic | Fundamentals & Architecture | SQL: funciones de ventana (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD). Ejercicios 4 y 6 | Nivel 1, láminas 27–33, 39, 41 |
| 6 | vie 11 dic | Fundamentals & Architecture | Práctica guiada de SQL: errores comunes (NULL, LEFT vs INNER JOIN, WHERE vs HAVING) sobre el modelo de ventas | Nivel 1, láminas 24–35 (práctica adicional) |
| 7 | lun 14 dic | Fundamentals & Architecture | Caso práctico: ejercicio 7 (reporte integrador SQL) y revisión | Nivel 1, lámina 42 |
| 8 | mar 15 dic | Storage & Modeling | Evolución de las arquitecturas de datos; warehouse vs lake vs lakehouse | Nivel 2, láminas 2–6 |
| 9 | mié 16 dic | Storage & Modeling | Arquitectura Medallion: bronze, silver y gold | Nivel 2, láminas 7–10, 16 |
| 10 | jue 17 dic | Storage & Modeling | Batch vs streaming; Delta Lake, ACID y time travel | Nivel 2, láminas 11–15 |
| 11 | vie 18 dic | Storage & Modeling | Caso práctico: reglas de negocio para silver y reportes gold del caso | Nivel 2, láminas 17–18, planilla de reglas Medallion |
| 12 | lun 11 ene | Ingestion & Processing I · Azure Data Platform | Arquitectura Azure del laboratorio; Resource Group y Azure Key Vault (secretos) | Nivel 3, láminas 2–3, guía 01, guía 02 |
| 13 | mar 12 ene | Ingestion & Processing I · Azure Data Platform | ADLS Gen2 (contenedores y estructura de carpetas) y creación de Azure Data Factory | Nivel 3, guía 03, guía 04 |
| 14 | mié 13 ene | Ingestion & Processing I · Azure Data Platform | Ingesta con ADF: PostgreSQL/Azure SQL → ADLS, linked services y acceso a Key Vault | Nivel 3, guía 05 (1.ª parte), láminas 5–6 |
| 15 | jue 14 ene | Ingestion & Processing I · Azure Data Platform | Ingesta con ADF: MongoDB/Azure DocumentDB → ADLS, columnas de auditoría (origen, fecha de proceso, RunId) | Nivel 3, guía 05 (2.ª parte), lámina 7 |
| 16 | vie 15 ene | Ingestion & Processing I · Azure Data Platform | Caso práctico: validación de la ingesta (conteos esperados, compresión snappy) | Nivel 3, lámina 8 |
| 17 | lun 18 ene | Ingestion & Processing II · Python | Python para datos: variables, colecciones, funciones, clases y tipado | Nivel 4, láminas 2–7, 16 |
| 18 | mar 19 ene | Ingestion & Processing II · Python | pandas: lectura, filtros y transformaciones | Nivel 4, láminas 8–11 |
| 19 | mié 20 ene | Ingestion & Processing II · Python | APIs con requests y JSON; logging, configuración sin secretos en el código, estructura de un ETL | Nivel 4, láminas 12–15, 17 |
| 20 | jue 21 ene | Ingestion & Processing II · Python | Caso práctico: ETL de la API de clientes y ventas con validaciones silver | Nivel 4, lámina 18 |
| 21 | vie 22 ene | Databricks | Databricks: workspace, clusters, notebooks y conexión con ADLS (base para Apache Spark) | Material nuevo |
| 22 | lun 25 ene | Ingestion & Processing III · Apache Spark | Por qué Spark; arquitectura (driver, executors, cluster manager) y SparkSession, en Databricks | Nivel 5, láminas 2–8 |
| 23 | mar 26 ene | Ingestion & Processing III · Apache Spark | DataFrames: lectura, select, filter, withColumn, join y groupBy | Nivel 5, láminas 9–15 |
| 24 | mié 27 ene | Ingestion & Processing III · Apache Spark | Spark SQL, lazy evaluation, acciones, DAG de ejecución y Catalyst | Nivel 5, láminas 16–19, 23–26 |
| 25 | jue 28 ene | Ingestion & Processing III · Apache Spark | Performance y costo: shuffle (narrow vs wide), archivos pequeños, joins grandes, partitionBy, cache y tamaño del cómputo | Nivel 5, láminas 20–22 y material nuevo |
| 26 | vie 29 ene | Ingestion & Processing III · Apache Spark | Caso práctico: bronze → silver → gold del caso con PySpark | Nivel 5, laboratorio |
| 27 | lun 1 feb | Databricks | Unity Catalog: catálogos, esquemas, tablas managed y external, external locations y linaje | Material nuevo |
| 28 | mar 2 feb | Databricks | Delta en la práctica: MERGE, time travel, OPTIMIZE y VACUUM | Material nuevo |
| 29 | mié 3 feb | Databricks | Orquestación con ADF y Lakeflow Jobs (dependencias, reintentos, schedules); observabilidad: monitoreo y alertas | Material nuevo |
| 30 | jue 4 feb | Modeling & Reliability | Modelado dimensional: hechos, dimensiones, granularidad; ETL vs ELT | Material nuevo |
| 31 | vie 5 feb | Modeling & Reliability | Slowly Changing Dimensions (tipos 1 y 2) con MERGE | Material nuevo |
| 32 | lun 8 feb | Modeling & Reliability | Cargas incrementales con watermark y backfills | Material nuevo |
| 33 | mar 9 feb | Modeling & Reliability | Idempotencia y exactly-once: reejecutar sin duplicar | Material nuevo |
| 34 | mié 10 feb | Streaming, Quality & Governance | Streaming: fundamentos de Kafka, Structured Streaming y Auto Loader | Material nuevo |
| 35 | jue 11 feb | Streaming, Quality & Governance | CDC: leer cambios de PostgreSQL/Azure SQL y aplicarlos a silver | Material nuevo |
| 36 | vie 12 feb | Streaming, Quality & Governance | Calidad de datos (frescura, volumen, nulos, unicidad; cuarentena y alertas), schema evolution y data contracts | Material nuevo |
| 37 | lun 15 feb | Streaming, Quality & Governance | CI/CD: Git en Databricks, Declarative Automation Bundles y pipelines de Azure DevOps | Material nuevo |
| 38 | mar 16 feb | Caso integrador | Caso integrador: armado de parejas y diseño del pipeline del caso de punta a punta (incluye despliegue con CI/CD) | — |
| 39 | mié 17 feb | Caso integrador | Caso integrador: trabajo con mentoría en vivo | — |
| 40 | jue 18 feb | Caso integrador | Presentaciones del caso integrador (1.ª parte) | — |
| 41 | vie 19 feb | Caso integrador | Presentaciones del caso integrador (2.ª parte) y cierre del programa | — |
