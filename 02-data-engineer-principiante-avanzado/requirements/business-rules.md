# Reglas del negocio

1. Un cliente no debe aparecer más de una vez en Silver.
2. Un proyecto con `planned_hours < 0` debe ir a cuarentena.
3. Un registro de horas con `hours < 0` o `hours > 24` debe ir a cuarentena.
4. Un registro de horas cuyo proyecto no existe debe marcarse como inválido.
5. Un incidente resuelto debe tener `resolved_at >= opened_at`.
6. Los incidentes abiertos deben conservar `resolved_at` nulo.
7. La métrica de resolución debe calcularse solamente para incidentes resueltos.
8. El resumen de proyectos debe incluir horas trabajadas, horas planificadas y
   porcentaje de consumo.
9. El pipeline debe poder ejecutarse dos veces para la misma fecha sin duplicar
   registros válidos.

## Preguntas analíticas

- ¿Qué proyectos consumen más del 80% de sus horas planificadas?
- ¿Qué clientes tienen más incidentes abiertos?
- ¿Cuál es el tiempo promedio de resolución por severidad?
- ¿Qué porcentaje de registros fue enviado a cuarentena?