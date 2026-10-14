# Diccionario de datos

| Fuente | Campo | Tipo esperado | Regla |
|---|---|---|---|
| customers | `customer_id` | string | Obligatorio y único |
| customers | `signup_date` | date | Puede ser nulo, pero debe registrarse |
| projects | `project_id` | string | Obligatorio y único |
| projects | `planned_hours` | decimal | Debe ser mayor o igual a cero |
| work_logs | `work_log_id` | string | Obligatorio y único |
| work_logs | `hours` | decimal | Debe estar entre 0 y 24 |
| incidents | `incident_id` | string | Obligatorio y único |
| incidents | `resolved_at` | timestamp | Debe ser posterior a `opened_at` |

El candidato debe documentar contratos adicionales y cómo gestionaría su evolución.