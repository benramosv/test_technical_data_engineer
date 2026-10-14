# Hoja de evaluación — Data Engineer Competente

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
| Arquitectura | Diseño Medallion, contratos y diagrama | 30 | | |
| Arquitectura | Ambientes, seguridad y costos | 25 | | |
| Arquitectura | Decisiones y trade-offs documentados | 25 | | |
| Arquitectura | Claridad operacional | 20 | | |
| **Subtotal** | **Arquitectura** | **100** | | |
| Incrementalidad | Idempotencia y control de procesamiento | 30 | | |
| Incrementalidad | Late-arriving data y reprocesamiento | 25 | | |
| Incrementalidad | Delta MERGE y evolución de esquema | 25 | | |
| Incrementalidad | Recuperación ante fallos parciales | 20 | | |
| **Subtotal** | **Incrementalidad y Delta** | **100** | | |
| Silver/Gold | SCD Tipo 2 correcto | 35 | | |
| Silver/Gold | Métricas y consultas SQL de negocio | 35 | | |
| Silver/Gold | Modelo mantenible y validado | 30 | | |
| **Subtotal** | **Silver/Gold** | **100** | | |
| Rendimiento | Particiones, shuffle y skew | 35 | | |
| Rendimiento | Small files, filtros y joins | 30 | | |
| Rendimiento | Evidencia o razonamiento reproducible | 35 | | |
| **Subtotal** | **Rendimiento** | **100** | | |
| Calidad/observabilidad | Reglas y severidad | 30 | | |
| Calidad/observabilidad | Métricas, freshness y auditoría | 35 | | |
| Calidad/observabilidad | Alertas y diagnóstico | 35 | | |
| **Subtotal** | **Calidad y observabilidad** | **100** | | |
| Workflow | Parámetros, dependencias y resiliencia | 50 | | |
| Workflow | Evidencia de éxito y fallo/reproceso | 30 | | |
| Workflow | Configuración portable entre ambientes | 20 | | |
| **Subtotal** | **Workflow** | **100** | | |
| CI/CD y operación | PR checks, tests y configuración como código | 30 | | |
| CI/CD y operación | Runbook y rollback lógico | 30 | | |
| CI/CD y operación | ADR y documentación reproducible | 25 | | |
| CI/CD y operación | Gestión segura de secretos | 15 | | |
| **Subtotal** | **CI/CD y operación** | **100** | | |

## Resultado ponderado

| Sección | Peso | Puntaje | Aporte |
|---|---:|---:|---:|
| Arquitectura | 20% | | |
| Incrementalidad y Delta | 20% | | |
| Silver/Gold | 20% | | |
| Rendimiento | 15% | | |
| Calidad y observabilidad | 15% | | |
| Workflow | 5% | | |
| CI/CD y operación | 5% | | |
| **TOTAL** | **100%** | | **___ / 100** |

### Nivel alcanzado

- [ ] No aprobado — menor de 50
- [ ] En desarrollo — 50 a 69
- [ ] Aprobado — 70 a 89
- [ ] Sobresaliente — 90 a 100

### Condiciones de aprobación Competente

- [ ] Demuestra incrementalidad e idempotencia.
- [ ] Explica controles de calidad y manejo de fallos.
- [ ] Puede justificar decisiones de rendimiento.
- [ ] Puede operar o reprocesar la solución.

## Preguntas de revisión

| Pregunta | Evidencia / respuesta | Puntaje cualitativo |
|---|---|---|
| ¿Cómo manejarías late-arriving data? | | |
| ¿Cómo implementarías SCD Tipo 2? | | |
| ¿Dónde esperas shuffles o skew? | | |
| ¿Cómo promoverías entre ambientes? | | |
| ¿Cómo recuperarías un fallo parcial? | | |

## Observaciones y recomendación

```text

```

- [ ] Apto para Data Engineer Competente
- [ ] Apto con plan de desarrollo
- [ ] Repetir evaluación
- [ ] No apto para el rol