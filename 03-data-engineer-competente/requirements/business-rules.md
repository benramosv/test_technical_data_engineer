# Reglas y restricciones

1. El pipeline debe ser idempotente para una misma fecha de proceso.
2. Los datos retrasados deben poder incorporarse sin duplicados.
3. Los cambios de atributos de clientes o proyectos deben conservar historial.
4. Registros inválidos deben quedar auditables en cuarentena.
5. Una ejecución debe producir métricas de volumen, calidad y freshness.
6. Un error crítico de calidad debe impedir la promoción a Gold.
7. El pipeline debe soportar reprocesamiento selectivo de una fecha.
8. Las rutas, catálogos, credenciales y parámetros no deben estar hardcodeados.

## Preguntas analíticas

- ¿Qué proyectos superan el 80% de horas planificadas?
- ¿Qué clientes tienen mayor volumen de incidentes abiertos?
- ¿Cuál es el tiempo promedio de resolución por severidad y mes?
- ¿Cuál es la tasa de registros rechazados por fuente?
- ¿Qué cambios históricos ocurrieron en clientes o proyectos?