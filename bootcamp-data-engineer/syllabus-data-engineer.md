# Syllabus Data Engineer

**AI & Data Summer Bootcamp · Ola 0 · Technical Evolution**

| | |
|---|---|
| Versión | 0.11 preliminar · 19-nov-2026 · para revisión de los coaches de Data Engineer y aprobación del Workstream Lead |
| Vertical | Data Engineer (10 participantes) |
| Duración | 1-dic-2026 al 19-feb-2027 · 41 sesiones de 1 h |
| Horario | Lunes a viernes, 17:00–18:00, más 2 h semanales de autoestudio |
| Stack | Azure Data Factory, ADLS Gen2, Azure Key Vault, Azure Databricks, Azure DevOps |
| Resultado | Principiantes aptos al 1-mar-2027, asignables a Digital Lab, DEC (Digital Enablement Center) o Delivery Consult |

## 1. Para quién es y qué se espera al final

El programa está pensado para profesionales de Kyndryl con base técnica que quieren pasar a ingeniería de datos. No hace falta haber trabajado como Data Engineer ni dominar las tecnologías del perfil. Se espera SQL básico y ganas de aprender de forma autónoma. El ingreso se define con un test de competencias.

Al terminar, cada participante podrá:

- Explicar los conceptos base de la ingeniería de datos: OLTP vs OLAP, warehouse vs lake vs lakehouse, Medallion, batch vs streaming, formatos de archivo y Delta Lake.
- Escribir SQL analítico con JOINs, CTE y funciones de ventana.
- Ingerir datos desde PostgreSQL/Azure SQL, MongoDB/Azure DocumentDB y APIs hacia ADLS Gen2 con Data Factory y Python, con los secretos guardados en Key Vault.
- Transformar datos con PySpark en Databricks a lo largo de las capas bronze, silver y gold.
- Hacer que un pipeline sea confiable: cargas incrementales, reejecuciones sin duplicados, historia con SCD tipo 2 y controles de calidad.
- Versionar y desplegar el pipeline con Git, Declarative Automation Bundles (antes llamados Databricks Asset Bundles) y Azure DevOps.
- Presentar y defender un pipeline completo frente a un equipo técnico.

El nivel es inicial y no hay examen de certificación al final. La meta es que el participante llegue a su primer proyecto entendiendo qué hace y por qué.

## 2. Cómo funciona

- **Clases:** 5 sesiones de 1 h por semana, con explicación y práctica guiada.
- **Caso práctico:** todos los laboratorios trabajan sobre un mismo caso de negocio. Módulo a módulo, el participante va armando su pipeline de punta a punta, y cada módulo cierra con un laboratorio que agrega una pieza.
- **Autoestudio:** 2 h por semana para terminar el caso práctico y repasar.
- **Mentoría:** un punto de control con el coach al cierre de cada módulo.

## 3. Calendario

| Módulo | Material base | Sesiones | Fechas |
|---|---|---|---|
| Fundamentals & Architecture | Nivel 1 · Fundamentos de Datos | 4 | 1–4 dic |
| *Break* | | — | 7–9 dic |
| Fundamentals & Architecture (continúa) | Nivel 1 · Fundamentos de Datos | 3 | 10–11 dic, 14 dic |
| Storage & Modeling | Nivel 2 · Arquitectura Moderna de Datos | 4 | 15–18 dic |
| *Break* | | — | 21 dic – 8 ene |
| Ingestion & Processing I · Azure Data Platform | Nivel 3 · Azure Data Platform | 5 | 11–15 ene |
| Ingestion & Processing II · Python | Nivel 4 · Python para Ingeniería de Datos | 4 | 18–21 ene |
| Databricks (parte 1) | — (material nuevo) | 1 | 22 ene |
| Ingestion & Processing III · Apache Spark | Nivel 5 · Apache Spark y PySpark | 5 | 25–29 ene |
| Databricks (parte 2) | — (material nuevo) | 3 | 1–3 feb |
| Modeling & Reliability | — (material nuevo) | 4 | 4–5 feb, 8–9 feb |
| Streaming, Quality & Governance | — (material nuevo) | 4 | 10–12 feb, 15 feb |
| Caso integrador | — (material nuevo) | 4 | 16–19 feb |

Los nombres de los módulos siguen los bloques de la infografía "Data Engineer Interview Prep", que usamos como referencia de los conceptos que necesita un Data Engineer. El curso reutiliza el material del Upskilling Program de junio 2026, organizado en cinco niveles. La columna "Material base" indica qué nivel se usa en cada módulo. Los módulos marcados como material nuevo se preparan para este programa.

---

## Fundamentals & Architecture

*Material base: Nivel 1 · Fundamentos de Datos*

**Objetivo.** Entender qué hace un Data Engineer, reconocer los tipos de datos y sus formatos, y escribir SQL analítico.

**Conceptos.** Ciclo de vida del dato (generación, ingesta, almacenamiento, transformación, consumo). OLTP vs OLAP. Datos estructurados, semiestructurados y no estructurados. Formatos CSV, JSON, XML, Parquet, Avro y Delta Lake. Bases relacionales y NoSQL. Data warehouse, data mart, data lake y lakehouse.

**Sesiones.**
1. Qué es Data Engineering. Ciclo de vida del dato. OLTP vs OLAP. Tipos de datos.
2. Formatos de archivo: de CSV y JSON a Parquet, Avro y Delta Lake.
3. Bases relacionales y NoSQL. Warehouse, data mart, data lake y lakehouse.
4. SQL: JOINs, CTE, GROUP BY y funciones de fecha.
5. SQL: funciones de ventana (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD).
6. Práctica guiada de SQL: errores comunes con NULL, LEFT vs INNER JOIN y WHERE vs HAVING.
7. Caso práctico y revisión.

**Caso práctico.** Siete ejercicios SQL sobre el modelo de ventas, que terminan en un reporte con cliente, ciudad, cantidad de compras, total gastado y ranking.

**Autoestudio (2 h).** Terminar los ejercicios.

**Evidencia.** Script SQL con los 7 ejercicios resueltos.

**Mentoría.** Revisión del reporte final y de las dudas sobre funciones de ventana.

---

## Storage & Modeling

*Material base: Nivel 2 · Arquitectura Moderna de Datos*

**Objetivo.** Entender por qué evolucionaron las arquitecturas de datos y diseñar las capas Medallion para un caso real.

**Conceptos.** Del warehouse al lakehouse. Arquitectura Medallion: bronze (el dato tal como llega), silver (limpio y validado) y gold (listo para el negocio). Batch vs streaming. Delta Lake: ACID, versiones y time travel.

**Sesiones.**
1. Por qué evolucionaron las arquitecturas. Warehouse, lake y lakehouse.
2. Medallion: qué va en cada capa y qué no se hace en cada una.
3. Batch vs streaming. Delta Lake, ACID y time travel.
4. Caso práctico.

**Caso práctico.** Definir las reglas de negocio de la capa silver del caso (validaciones de monto, cantidad, documento, correo y fechas) y elegir los reportes gold que necesita el negocio.

**Autoestudio (2 h).** Completar el diagrama Medallion del caso. Antes del break, cada participante confirma por correo con su coach que tiene acceso al tenant Azure, porque Ingestion & Processing I · Azure Data Platform arranca el 11 de enero con laboratorios.

**Evidencia.** Diagrama Medallion y la lista de reglas silver y reportes gold.

**Mentoría.** ¿Cada regla tiene un motivo de negocio claro?

---

## Ingestion & Processing I · Azure Data Platform

*Material base: Nivel 3 · Azure Data Platform*

**Objetivo.** Montar en Azure la base del pipeline e ingerir las fuentes del caso en la capa bronze.

**Conceptos.** Resource groups. Secretos en Key Vault. ADLS Gen2: contenedores y estructura de carpetas. Data Factory: linked services, datasets, pipelines y copy. Columnas de auditoría para rastrear cada carga.

**Sesiones.**
1. Arquitectura Azure del laboratorio. Resource group y Key Vault.
2. ADLS Gen2 y creación de Data Factory.
3. Ingesta desde PostgreSQL/Azure SQL hacia ADLS, con credenciales en Key Vault.
4. Ingesta desde MongoDB/Azure DocumentDB. Columnas de auditoría: origen, fecha de proceso e identificador de ejecución.
5. Caso práctico.

**Caso práctico.** Ingerir clientes y ventas de PostgreSQL/Azure SQL y MongoDB/Azure DocumentDB en bronze y validar la carga contra los conteos esperados.

**Autoestudio (2 h).** Repetir la ingesta parametrizando la fecha de proceso.

**Evidencia.** Pipelines de Data Factory exportados y los conteos de la validación.

**Mentoría.** ¿Qué pasa si una fuente no responde a mitad de la carga?

---

## Ingestion & Processing II · Python

*Material base: Nivel 4 · Python para Ingeniería de Datos*

**Objetivo.** Escribir un ETL en Python con buenas prácticas.

**Conceptos.** Tipos, colecciones, funciones y clases. pandas para explorar y transformar. Consumo de APIs con requests y JSON. Logging en lugar de print. Configuración sin secretos en el código. Tipado. Estructura de un ETL: extract, transform, load, config y logs.

**Sesiones.**
1. Python para datos: variables, colecciones, funciones, clases y tipado.
2. pandas: lectura, filtros y transformaciones.
3. APIs con requests y JSON. Logging, configuración y estructura de un ETL.
4. Caso práctico.

**Caso práctico.** ETL que consume una API del caso y aplica las reglas silver definidas en Storage & Modeling.

**Autoestudio (2 h).** Agregar logging y manejo de errores al ETL.

**Evidencia.** Código del ETL con su archivo de configuración y un log de ejecución.

**Mentoría.** Revisión del código: ¿se entiende sin explicarlo?

---

## Databricks

Este módulo se dicta en dos partes. La primera prepara el entorno para Ingestion & Processing III · Apache Spark; la segunda viene después y lleva el pipeline a Unity Catalog, Delta y orquestación.

**Objetivo.** Trabajar en Databricks como plataforma del lakehouse: cómputo, gobierno de tablas, Delta en la práctica y orquestación.

**Conceptos.** Workspace, clusters y notebooks. Unity Catalog: catálogos, esquemas, tablas managed y external, y acceso a ADLS. Delta: MERGE, time travel, OPTIMIZE y VACUUM. Linaje en Unity Catalog. Orquestación: dependencias, reintentos y schedules. Observabilidad: monitoreo de jobs y alertas.

**Sesiones.**
1. *(22 ene)* Workspace, clusters, notebooks y conexión con ADLS.
2. *(1 feb)* Unity Catalog: catálogos, esquemas y tablas; external locations; linaje.
3. *(2 feb)* Delta en la práctica: MERGE, time travel, OPTIMIZE y VACUUM.
4. *(3 feb)* Orquestación con Data Factory y Lakeflow Jobs. Observabilidad: historial de ejecuciones, monitoreo y alertas.

**Caso práctico.** Registrar las tablas bronze, silver y gold del caso en Unity Catalog, actualizar silver con MERGE y orquestar el pipeline completo desde Data Factory.

**Autoestudio (2 h).** Configurar reintentos, un schedule diario y una alerta de fallo.

**Evidencia.** Tablas en Unity Catalog y una corrida exitosa del pipeline orquestado.

**Mentoría.** ¿Cuándo conviene orquestar desde Data Factory y cuándo con Lakeflow Jobs?

---

## Ingestion & Processing III · Apache Spark

*Material base: Nivel 5 · Apache Spark y PySpark*

**Objetivo.** Procesar datos a escala con PySpark en Databricks y entender cómo Spark ejecuta un trabajo.

**Conceptos.** Por qué hace falta procesamiento distribuido. Driver, executors y cluster manager. DataFrames. Spark SQL. Lazy evaluation y acciones. Plan de ejecución: DAG, Catalyst, stages y tasks. Performance y costo: shuffle (operaciones narrow vs wide), archivos pequeños, joins grandes, particiones, cache y tamaño del cómputo.

**Sesiones.**
1. Por qué Spark. Arquitectura y SparkSession.
2. DataFrames: lectura, select, filter, withColumn, join y groupBy.
3. Spark SQL, lazy evaluation, acciones y plan de ejecución.
4. Performance y costo: shuffle, archivos pequeños, partitionBy, cache y tamaño del cómputo.
5. Caso práctico.

**Caso práctico.** Transformar los datos del caso de bronze a silver (aplicando las reglas definidas en Storage & Modeling) y de silver a gold (los reportes elegidos), en notebooks de Databricks.

**Autoestudio (2 h).** Comparar el plan de ejecución antes y después de particionar.

**Evidencia.** Notebooks bronze → silver → gold y las tablas gold resultantes.

**Mentoría.** Lectura conjunta de la Spark UI de un job del caso.

---

## Modeling & Reliability

*Material nuevo*

**Objetivo.** Modelar la capa gold con historia y hacer que el pipeline cargue solo lo nuevo y se pueda reejecutar sin duplicar ni perder datos.

**Conceptos.** ETL vs ELT. Modelo estrella: hechos, dimensiones y granularidad. Slowly Changing Dimensions. Cargas incrementales con watermark y backfills. Idempotencia y exactly-once.

**Sesiones.**
1. Modelado dimensional: hechos, dimensiones y granularidad. ETL vs ELT.
2. Slowly Changing Dimensions tipo 1 y tipo 2 con MERGE.
3. Cargas incrementales con watermark y backfills.
4. Idempotencia: reejecutar un pipeline sin duplicar ni perder datos.

**Caso práctico.** Construir el modelo estrella gold del caso con una dimensión SCD tipo 2, pasar la carga de ventas a incremental por watermark y demostrar con una reejecución que el pipeline no duplica.

**Autoestudio (2 h).** Ejecutar un backfill de una semana y verificar los resultados.

**Evidencia.** Diagrama del modelo estrella, tablas gold y la evidencia de la reejecución sin duplicados.

**Mentoría.** ¿Qué pasa si el job falla a mitad de una carga incremental?

---

## Streaming, Quality & Governance

*Material nuevo*

**Objetivo.** Incorporar datos que llegan de forma continua y cambios de la fuente, controlar la calidad del pipeline y desplegarlo de forma automatizada.

**Conceptos.** Fundamentos de Kafka y streaming. Change Data Capture. Calidad de datos: frescura, volumen, nulos y unicidad; cuarentena y alertas. Schema evolution y data contracts. CI/CD: Git, Declarative Automation Bundles y pipelines de Azure DevOps.

**Sesiones.**
1. Streaming: fundamentos de Kafka, Structured Streaming y Auto Loader.
2. CDC: leer los cambios de PostgreSQL/Azure SQL y aplicarlos a silver.
3. Calidad de datos (frescura, volumen, nulos y unicidad; cuarentena y alertas), schema evolution y data contracts.
4. CI/CD: Git en Databricks, Declarative Automation Bundles y pipelines de Azure DevOps para desplegar entre entornos.

**Caso práctico.** Ingerir de forma continua los archivos nuevos del caso con Auto Loader, aplicar a silver los cambios de la fuente relacional con CDC, agregar quality gates con cuarentena y una alerta de frescura, y desplegar el pipeline con un Declarative Automation Bundles desde Azure DevOps.

**Autoestudio (2 h).** Simular un cambio de esquema en la fuente y documentar cómo lo absorbe el pipeline.

**Evidencia.** Stream en ejecución con su checkpoint, tabla silver con los cambios aplicados, el registro de filas en cuarentena y una corrida exitosa del pipeline de despliegue en Azure DevOps.

**Mentoría.** ¿Qué parte del pipeline se rompería primero en producción y por qué?

---

## Caso integrador

*Material nuevo*

**Objetivo.** Demostrar, en parejas, que el participante está listo para su primer proyecto.

**Conceptos.** Integra todo lo visto en el programa.

**Sesiones.**
1. Armado de parejas y diseño del pipeline del caso de punta a punta.
2. Trabajo con mentoría en vivo.
3. Presentaciones (1.ª parte).
4. Presentaciones (2.ª parte) y cierre del programa.

**Caso práctico.** Pipeline completo del caso: ingesta desde PostgreSQL/Azure SQL, MongoDB/Azure DocumentDB y la API hacia bronze; transformaciones silver y gold en Databricks con Unity Catalog; carga incremental con una dimensión SCD tipo 2; quality gates; orquestación; y despliegue con un Declarative Automation Bundles desde un pipeline de Azure DevOps.

**Autoestudio (2 h).** Preparar la presentación y el README del pipeline.

**Evidencia.** Repositorio en Azure DevOps con el código, el bundle y el pipeline de CI/CD; una corrida exitosa del despliegue; el README; y una presentación de unos 20 minutos con preguntas del coach sobre los conceptos del programa.

**Mentoría.** Feedback individual sobre fortalezas y brechas para el primer proyecto.

---

## 4. Criterio de "principiante apto" (abierto)

Este criterio está pendiente de validación con la coordinación de Technical Evolution. Pedimos al Workstream Lead que lo confirme o lo ajuste.

Propuesta: un participante es apto si:

1. Entrega al menos 7 de los 8 casos prácticos (los cinco módulos con material base, Databricks, Modeling & Reliability y Streaming, Quality & Governance).
2. Aprueba el caso integrador.
3. Asiste al menos al 80 % de las sesiones.

## 5. Fuera del alcance

- Preparación de certificaciones.
- Otras nubes (AWS, GCP) y Microsoft Fabric.
- Airflow y dbt. La orquestación se enseña con Data Factory y Lakeflow Jobs, y las transformaciones con Spark y SQL en Databricks.
- Apache Iceberg. De los formatos de tabla abiertos, el curso enseña Delta Lake.
- Laboratorios de Kafka. Kafka se ve como concepto.
- Contenido de las verticales AI Engineer y AI Platform Engineer.

## Anexo: origen de cada módulo y conceptos que cubre

La infografía "Data Engineer Interview Prep" lista 20 conceptos. El programa cubre los 20; en formatos de tabla abiertos solo se enseña Delta Lake.

| Módulo | Origen | Conceptos de la infografía |
|---|---|---|
| Fundamentals & Architecture | Upskilling Program, Nivel 1 | OLTP vs OLAP; warehouse vs lake vs lakehouse; formatos de archivo |
| Storage & Modeling | Upskilling Program, Nivel 2 y su planilla de reglas Medallion | Batch vs streaming; arquitectura Medallion; formatos de tabla abiertos (Delta) |
| Ingestion & Processing I · Azure Data Platform | Upskilling Program, Nivel 3 | Linaje y observabilidad (columnas de auditoría) |
| Ingestion & Processing II · Python | Upskilling Program, Nivel 4 | Ninguno: Python y el consumo de APIs no están en la infografía, pero el perfil de Data Engineer los pide |
| Ingestion & Processing III · Apache Spark | Upskilling Program, Nivel 5 | Modelo de ejecución de Spark; shuffle y particionamiento; costo y performance |
| Databricks | Material nuevo | Formatos de tabla abiertos (Delta); orquestación de pipelines; linaje y observabilidad |
| Modeling & Reliability | Material nuevo | ETL vs ELT; modelo estrella; Slowly Changing Dimensions; idempotencia y exactly-once; cargas incrementales y backfills |
| Streaming, Quality & Governance | Material nuevo | Change Data Capture; fundamentos de Kafka; controles de calidad de datos; schema evolution y data contracts |
| Caso integrador | Material nuevo | Todos |
