# ADR-001: Estrategia de procesamiento incremental

## Estado

Por decidir por el candidato.

## Contexto

El pipeline recibe datos diarios, puede recibir eventos retrasados y debe poder
reprocesar una fecha sin duplicar registros.

## Decisión

El candidato debe elegir entre watermark, control table, Auto Loader, MERGE u otra
estrategia y explicar por qué se ajusta a las restricciones.

## Consecuencias

Documentar costo, complejidad operativa, recuperación ante fallos, evolución de
esquema y límites conocidos.