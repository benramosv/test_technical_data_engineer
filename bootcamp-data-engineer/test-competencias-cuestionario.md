# Test de competencias · Data Engineer

**AI & Data Summer Bootcamp · Technical Evolution · Versión 0.7 preliminar**

## Instrucciones

- Tienes **65 minutos**.
- Son 5 secciones y 29 preguntas. Suman 100 puntos; la pregunta A9 es extra y no suma.
- Las secciones A, B y C son de opción múltiple y tienen una sola respuesta correcta cada pregunta.
- La sección D es un caso breve con respuesta escrita. En la sección E vas a aprender algo nuevo y aplicarlo.
- Responde por tu cuenta, sin herramientas de IA ni búsquedas en internet. Buscamos conocer tu punto de partida, y está bien no saber alguna respuesta.

## Datos para las secciones A y D

Una tienda guarda sus clientes y sus ventas en dos tablas.

**Tabla `clientes`**

| document_number | first_name | city |
|---|---|---|
| 10000001 | Ana | Lima |
| 10000002 | Luis | Arequipa |
| 10000003 | Rosa | Lima |
| 10000004 | Jorge | Cusco |

**Tabla `ventas`**

| id_venta | document_number | category | quantity | unit_price | sale_date |
|---|---|---|---|---|---|
| 1 | 10000001 | Laptops | 1 | 3000 | 2026-10-01 |
| 2 | 10000001 | Accesorios | 2 | 50 | 2026-10-03 |
| 3 | 10000002 | Laptops | 1 | 2800 | 2026-10-05 |
| 4 | 10000003 | Accesorios | 3 | 40 | 2026-10-05 |
| 5 | 10000002 | Monitores | 2 | 700 | 2026-11-02 |
| 6 | 10000005 | Accesorios | 1 | 60 | 2026-11-03 |

---

## Sección A · SQL (36 puntos, 4 por pregunta; la A9 es extra)

**A1.** ¿Qué devuelve esta consulta?

```sql
SELECT COUNT(*) FROM ventas WHERE category = 'Accesorios';
```

- a) 2
- b) 4
- c) 3
- d) 6

**A2.** ¿Cuántas filas devuelve esta consulta?

```sql
SELECT v.id_venta, c.first_name
FROM ventas v
INNER JOIN clientes c ON v.document_number = c.document_number;
```

- a) 5
- b) 4
- c) 6
- d) 7

**A3.** ¿Qué devuelve esta consulta?

```sql
SELECT c.first_name, COUNT(v.id_venta) AS compras
FROM clientes c
LEFT JOIN ventas v ON c.document_number = v.document_number
GROUP BY c.first_name;
```

- a) 3 filas; Jorge no aparece
- b) 4 filas; Jorge aparece con 0 compras
- c) 4 filas; Jorge aparece con 1 compra
- d) 5 filas; aparece también la venta 6

**A4.** Con esta consulta, ¿qué ciudad vende más y cuánto?

```sql
SELECT c.city, SUM(v.quantity * v.unit_price) AS total
FROM ventas v
INNER JOIN clientes c ON v.document_number = c.document_number
GROUP BY c.city;
```

- a) Lima, 3220
- b) Lima, 3280
- c) Arequipa, 2800
- d) Arequipa, 4200

**A5.** ¿Qué consulta devuelve las categorías con más de 2 ventas?

- a) `SELECT category, COUNT(*) FROM ventas WHERE COUNT(*) > 2 GROUP BY category;`
- b) `SELECT category, COUNT(*) FROM ventas GROUP BY category WHERE COUNT(*) > 2;`
- c) `SELECT category, COUNT(*) FROM ventas GROUP BY category HAVING COUNT(*) > 2;`
- d) `SELECT category FROM ventas HAVING category > 2;`

**A6.** ¿Qué consulta devuelve los clientes que no tienen ninguna compra?

- a) `SELECT c.* FROM clientes c LEFT JOIN ventas v ON c.document_number = v.document_number WHERE v.id_venta IS NULL;`
- b) `SELECT c.* FROM clientes c INNER JOIN ventas v ON c.document_number = v.document_number WHERE v.id_venta IS NULL;`
- c) `SELECT c.* FROM clientes c LEFT JOIN ventas v ON c.document_number = v.document_number WHERE v.id_venta = NULL;`
- d) `SELECT * FROM ventas WHERE document_number IS NULL;`

**A7.** ¿Qué devuelve esta consulta?

```sql
SELECT COUNT(DISTINCT document_number) FROM ventas;
```

- a) 3
- b) 6
- c) 5
- d) 4

**A8.** Una tabla de ventas recibió filas repetidas con el mismo `id_venta`. ¿Qué consulta muestra los `id_venta` repetidos?

- a) `SELECT DISTINCT id_venta FROM ventas;`
- b) `SELECT id_venta FROM ventas WHERE COUNT(id_venta) > 1;`
- c) `SELECT id_venta, COUNT(*) FROM ventas GROUP BY id_venta HAVING COUNT(*) > 1;`
- d) `SELECT id_venta FROM ventas ORDER BY id_venta;`

**A9 (extra, no suma puntos).** ¿En qué ventas la columna `rn` vale 1?

```sql
SELECT id_venta, document_number,
       ROW_NUMBER() OVER (PARTITION BY document_number ORDER BY sale_date DESC) AS rn
FROM ventas;
```

- a) 1, 3, 4 y 6
- b) 2, 4, 5 y 6
- c) Solo 5 y 6
- d) Solo 1

**A10.** ¿Cuántas ventas hubo en octubre de 2026?

```sql
SELECT COUNT(*) FROM ventas
WHERE sale_date >= '2026-10-01' AND sale_date < '2026-11-01';
```

- a) 4
- b) 3
- c) 5
- d) 6

---

## Sección B · Lógica y Python básico (10 puntos, 2 por pregunta)

**B1.** ¿Qué imprime este código?

```python
precios = [3000, 50, 2800, 40]
total = 0
for p in precios:
    if p > 100:
        total += p
print(total)
```

- a) 5890
- b) 3000
- c) 2
- d) 5800

**B2.** ¿Qué imprime este código?

```python
cliente = {"nombre": "Ana", "ciudad": "Lima"}
cliente["pais"] = "Peru"
print(len(cliente))
```

- a) 3
- b) 2
- c) 4
- d) Da error

**B3.** ¿Qué imprime este código?

```python
def monto(cantidad, precio):
    return cantidad * precio

ventas = [(1, 3000), (2, 50), (3, 40)]
print(sum(monto(c, p) for c, p in ventas))
```

- a) 3090
- b) 3
- c) 3220
- d) Da error

**B4.** ¿Qué imprime este código?

```python
nombres = ["ana", "luis", "ana", "rosa"]
print(len(set(nombres)))
```

- a) 4
- b) Da error
- c) 2
- d) 3

**B5.** ¿Qué imprime este código?

```python
emails = ["ana@mail.com", "luis.mail.com", "", "rosa@mail.com"]
validos = [e for e in emails if "@" in e]
print(validos)
```

- a) `['ana@mail.com', 'rosa@mail.com']`
- b) `['ana@mail.com', 'luis.mail.com', 'rosa@mail.com']`
- c) `['luis.mail.com', '']`
- d) `2`

---

## Sección C · Fundamentos de datos (20 puntos, 2 por pregunta)

**C1.** El sistema que registra miles de ventas por minuto en las cajas de una tienda es principalmente:

- a) Un sistema OLAP
- b) Un sistema OLTP
- c) Un data lake
- d) Un data mart

**C2.** ¿Cuál es un ejemplo de dato semiestructurado?

- a) Una tabla relacional de clientes
- b) Un video de una cámara de seguridad
- c) Una imagen JPG
- d) Un archivo JSON donde algunos registros tienen campos que otros no tienen

**C3.** ¿Por qué un archivo Parquet suele leerse más rápido que un CSV en consultas analíticas?

- a) Porque guarda los datos por columnas y permite leer solo las columnas que la consulta necesita
- b) Porque es texto plano y se lee línea por línea
- c) Porque no tiene esquema
- d) Porque solo admite datos numéricos

**C4.** El área comercial revisa cada mañana un reporte con las ventas del día anterior. ¿Qué tipo de procesamiento conviene?

- a) Streaming en tiempo real
- b) Ninguno: el reporte se puede armar a mano
- c) Un proceso batch que corra de noche
- d) Consultar directamente la base transaccional en horario de atención

**C5.** En una arquitectura Medallion, ¿en qué capa se guardan los datos tal como llegan de la fuente?

- a) Gold
- b) Bronze
- c) Silver
- d) Data mart

**C6.** En un proceso ELT, ¿en qué orden ocurren las etapas?

- a) Extraer, transformar, cargar
- b) Extraer, cargar, transformar
- c) Cargar, extraer, transformar
- d) Transformar, extraer, cargar

**C7.** ¿Qué describe mejor a un data lake?

- a) Un repositorio que solo acepta datos ya limpios y modelados en estrella
- b) Un repositorio de bajo costo que guarda los datos en su formato original, estructurados o no
- c) Una base transaccional para registrar ventas
- d) Un reporte de BI

**C8.** En una arquitectura Medallion, ¿qué se hace normalmente al pasar los datos de bronze a silver?

- a) Construir los reportes finales para el negocio
- b) Copiar el archivo sin ningún cambio
- c) Limpiar, quitar duplicados y validar reglas
- d) Borrar los datos originales

**C9.** ¿Para qué sirve la clave primaria de una tabla?

- a) Para ordenar la tabla alfabéticamente
- b) Para cifrar los datos
- c) Para enlazar la tabla con un reporte
- d) Para identificar de forma única cada fila

**C10.** Ayer alguien borró por error registros de una tabla Delta Lake. ¿Qué característica permite consultar cómo estaba la tabla antes del borrado?

- a) Time travel
- b) Particionamiento
- c) Compresión snappy
- d) Un índice B-Tree

---

## Sección D · Caso: calidad de datos (20 puntos)

Todos los días llega un archivo de ventas que alimenta un reporte para el área comercial. Este es un extracto de un archivo reciente:

| id_venta | document_number | email | quantity | unit_price | amount | sale_date |
|---|---|---|---|---|---|---|
| 101 | 10000001 | ana@mail.com | 2 | 50 | 100 | 2026-11-10 |
| 102 | 1000002 | luis@mail.com | 1 | 2800 | 2800 | 2026-11-11 |
| 103 | 10000003 | rosa.mail.com | 3 | 40 | 120 | 2026-11-12 |
| 103 | 10000003 | rosa.mail.com | 3 | 40 | 120 | 2026-11-12 |
| 104 | 10000004 | jorge@mail.com | -1 | 700 | -700 | 2026-11-12 |
| 105 | 10000005 | eva@mail.com | 2 | 60 | 100 | 2027-03-01 |

El `document_number` válido tiene 8 dígitos. `amount` debería ser igual a `quantity × unit_price`.

**D1 (10 puntos).** Identifica todos los problemas de calidad que encuentres. Para cada uno, indica la fila (`id_venta`) y qué está mal.

**D2 (10 puntos).** En 5 a 8 líneas, explica qué harías con las filas que tienen problemas antes de que lleguen al reporte, y por qué.

---

## Sección E · Aprende y aplica (14 puntos)

Lee esta explicación. No necesitas conocer la función de antes.

> `COALESCE(valor1, valor2, ...)` revisa los valores en orden y devuelve el primero que no sea `NULL`. Si todos son `NULL`, devuelve `NULL`.
>
> - `COALESCE(NULL, 'sin dato')` devuelve `'sin dato'`.
> - `COALESCE('Lima', 'sin dato')` devuelve `'Lima'`.
> - `COALESCE(NULL, NULL, 'x')` devuelve `'x'`.

Usa también la tabla `clientes` del inicio y esta nueva tabla:

**Tabla `contactos`**

| document_number | phone | email |
|---|---|---|
| 10000001 | 999111222 | ana@mail.com |
| 10000002 | NULL | luis@mail.com |
| 10000003 | NULL | NULL |

**E1 (7 puntos).** ¿Qué valor de `contacto` devuelve esta consulta para los clientes 10000002 y 10000003?

```sql
SELECT document_number, COALESCE(phone, email, 'sin contacto') AS contacto
FROM contactos;
```

- a) NULL y NULL
- b) luis@mail.com y sin contacto
- c) luis@mail.com y NULL
- d) sin contacto y sin contacto

**E2 (7 puntos).** Escribe una consulta que muestre el `first_name` de **todos** los clientes de la tabla `clientes` y su teléfono. Si un cliente no tiene teléfono, o no aparece en la tabla `contactos`, debe mostrar `'sin teléfono'`.
