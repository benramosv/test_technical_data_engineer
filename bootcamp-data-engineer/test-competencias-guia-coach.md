# Test de competencias Data Engineer · Guía para coaches

**Confidencial: contiene la clave de respuestas. No compartir con los postulantes.**

| | |
|---|---|
| Versión | 0.7 preliminar · 19-nov-2026 · el formato del test y el criterio de selección quedan abiertos |
| Aprobación | Revisión de los coaches de Data Engineer y aprobación del Workstream Lead de Technical Evolution |
| Formato | **Abierto.** La duración, las secciones, los puntajes y la modalidad (en vivo, con cámara y sin defensa oral) están pendientes de validación. Pedimos al Workstream Lead que los confirme o los ajuste |
| Selección | **Abierto.** El criterio de selección (al final de esta guía) está pendiente de validación |
| Aplicación | 25–26 o 26–27 de noviembre (fecha por confirmar) |
| Cuestionario | Esta guía acompaña al cuestionario para postulantes, que lleva el mismo número de versión, y a la carpeta de imágenes para Forms |

## Qué mide y qué no

El test mide el piso de entrada del bootcamp: lo que un participante necesita traer para seguir el primer módulo (Fundamentals & Architecture) desde la primera semana. Las cinco secciones corresponden a lo que valora la convocatoria: fundamentos técnicos, pensamiento analítico y resolución de problemas, aprendizaje autónomo y capacidad de comunicar.

| Sección | Mide | Puntos | Tipo |
|---|---|---|---|
| A · SQL | Consultas, joins, agregaciones, nulos | 36 | Opción múltiple, autocorregible. **Mínimo propuesto: 16 puntos** |
| A9 (extra) | Funciones de ventana. No suma porque el primer módulo del bootcamp las enseña. Solo sirve para desempatar | 0 | Opción múltiple |
| B · Lógica y Python | Leer código simple y predecir el resultado | 10 | Opción múltiple, autocorregible |
| C · Fundamentos de datos | Conceptos de los dos primeros módulos del bootcamp: OLTP/OLAP, tipos de datos, formatos, batch, ELT, data lake, Medallion, clave primaria, Delta | 20 | Opción múltiple, autocorregible |
| D · Caso de calidad | Detección de problemas y criterio para resolverlos | 20 | Abierta, con rúbrica |
| E · Aprende y aplica | Capacidad de aprender algo nuevo en el momento (COALESCE) y combinarlo con lo que ya sabe (LEFT JOIN) | 14 | E1 autocorregible; E2 abierta, con rúbrica |

No evalúa Spark, Databricks, ADF ni Azure. Eso es lo que enseña el bootcamp, y evaluarlo favorecería a quienes ya lo saben por encima de quienes pueden aprenderlo.

El caso de la sección D usa las mismas reglas de validación que el bootcamp aplica en la capa silver: documento de 8 dígitos, correo con @, cantidad mayor a 0, monto igual a precio por cantidad y fecha no futura.

## Logística propuesta

- Cargar las secciones A, B y C en Microsoft Forms en modo cuestionario, para que se corrijan solas. La sección D va como pregunta de texto largo.
- Las tablas y el código van como imágenes (21 PNG en la carpeta `test-imagenes`). La sección siguiente indica dónde va cada una.
- Sesión en vivo de 65 minutos con cámara encendida, liderada por los coaches.
- Distribución sugerida del tiempo: 35 minutos para A, B y C, 10 para E y 15 para D, con 5 de margen.
- Corregir las secciones D y E2 con dos coaches por respuesta. Si los puntajes difieren en más de 3 puntos, se discute y se acuerda uno.

## Imágenes para Forms

Cada imagen se agrega con el ícono de imagen de la pregunta o de la sección.

### Tablas (van en la descripción de la sección)

| Imagen | Dónde va |
|---|---|
| `T1_tabla_clientes.png` | Descripción de la sección A. Repetir en la sección E (E2 la usa) |
| `T2_tabla_ventas.png` | Descripción de la sección A |
| `T3_tabla_extracto_D.png` | Descripción de la sección D, junto con el texto del caso |
| `T4_tabla_contactos.png` | Descripción de la sección E, debajo de la explicación de COALESCE |

### Código del enunciado (van en la pregunta)

| Imagen | Pregunta |
|---|---|
| `A1_codigo.png` | A1 |
| `A2_codigo.png` | A2 |
| `A3_codigo.png` | A3 |
| `A4_codigo.png` | A4 |
| `A7_codigo.png` | A7 |
| `A9_codigo.png` | A9 (extra) |
| `A10_codigo.png` | A10 |
| `B1_codigo.png` a `B5_codigo.png` | B1 a B5 |
| `E1_codigo.png` | E1 |

### Opciones con código (van en la pregunta; las opciones de Forms quedan como "a", "b", "c", "d")

| Imagen | Pregunta |
|---|---|
| `A5_opciones.png` | A5 |
| `A6_opciones.png` | A6 |
| `A8_opciones.png` | A8 |
| `B5_opciones.png` | B5 (va junto con `B5_codigo.png`) |

### Al cargar en Forms

- **No activar "orden aleatorio de opciones"** en A5, A6, A8 y B5: las letras están dentro de la imagen y se desordenarían. En el resto de las preguntas sí se puede activar.
- La explicación de COALESCE de la sección E y los textos de las preguntas van como texto normal.
- E2 y D1/D2 son preguntas de texto largo. La respuesta de E2 conviene pedirla en una caja de texto amplia, porque es una consulta SQL.

## Clave de respuestas

| Pregunta | Respuesta | Por qué |
|---|---|---|
| A1 | c) 3 | Ventas 2, 4 y 6 |
| A2 | a) 5 | La venta 6 (documento 10000005) no tiene cliente y el INNER JOIN la descarta |
| A3 | b) 4 filas; Jorge con 0 | LEFT JOIN conserva a Jorge. COUNT(v.id_venta) no cuenta nulos, por eso da 0. Con COUNT(*) daría 1, que es la trampa de la opción c |
| A4 | d) Arequipa, 4200 | Arequipa: 2800 + 1400. Lima: 3000 + 100 + 120 = 3220. La opción b suma por error la venta 6, que no tiene cliente |
| A5 | c) | Los filtros sobre agregaciones van en HAVING, no en WHERE |
| A6 | a) | Devuelve a Jorge. La opción c falla porque `= NULL` nunca es verdadero |
| A7 | d) 4 | 10000001, 10000002, 10000003 y 10000005 |
| A8 | c) | GROUP BY con HAVING COUNT(*) > 1 |
| A9 (extra) | b) 2, 4, 5 y 6 | Con ORDER BY sale_date DESC, rn = 1 es la venta más reciente de cada cliente. La opción a sería el orden ascendente |
| A10 | a) 4 | Ventas 1, 2, 3 y 4 |
| B1 | d) 5800 | 3000 + 2800 |
| B2 | a) 3 | El diccionario pasa a tener 3 claves |
| B3 | c) 3220 | 3000 + 100 + 120 |
| B4 | d) 3 | El set elimina el "ana" repetido |
| B5 | a) | Solo los dos correos que contienen @ |
| C1 | b) OLTP | Muchas transacciones cortas y concurrentes |
| C2 | d) JSON con campos variables | Tiene estructura, pero no fija |
| C3 | a) Formato columnar | Lee solo las columnas necesarias y comprime mejor |
| C4 | c) Batch nocturno | El dato se necesita una vez al día |
| C5 | b) Bronze | Bronze guarda el dato crudo, sin cambios |
| C6 | b) Extraer, cargar, transformar | En ELT se carga primero y se transforma dentro de la plataforma de destino |
| C7 | b) Datos en formato original, bajo costo | La opción a describe un data warehouse |
| C8 | c) Limpiar, deduplicar, validar | Los reportes van en gold; bronze conserva el original |
| C9 | d) Identificar cada fila de forma única | Base de las relaciones entre tablas |
| C10 | a) Time travel | Delta guarda versiones de la tabla y permite consultar una anterior |
| E1 | b) luis@mail.com y sin contacto | 10000002 no tiene teléfono y cae al email. 10000003 no tiene ninguno y cae al valor por defecto. La opción c es el error de quien cree que COALESCE se detiene en el segundo valor |

## Rúbrica de la sección D

**D1 (10 puntos).** Hay 6 problemas:

| id_venta | Problema |
|---|---|
| 102 | `document_number` con 7 dígitos |
| 103 | Email sin @ |
| 103 | Fila duplicada |
| 104 | Cantidad negativa (y monto negativo) |
| 105 | `amount` no coincide: 2 × 60 = 120, no 100 |
| 105 | Fecha de venta en el futuro (marzo 2027) |

| Problemas correctos | Puntos |
|---|---|
| 6 | 10 |
| 5 | 8 |
| 4 | 6 |
| 3 | 4 |
| 1–2 | 2 |
| 0 | 0 |

Si el postulante marca como problema algo que no lo es (por ejemplo, el documento 10000005 por no estar en la tabla `clientes`, que no forma parte de este extracto), no se resta ni se suma.

**D2 (10 puntos).**

| Criterio | Puntos |
|---|---|
| Separa las filas con problemas en lugar de borrarlas sin dejar registro (cuarentena, tabla de rechazos o similar) | 3 |
| Elimina los duplicados con un criterio explícito (por ejemplo, quedarse con una fila por `id_venta`) | 2 |
| Conserva el archivo original sin modificar, para poder reprocesar o auditar | 2 |
| Avisa al responsable de la fuente o deja una alerta para que el error se corrija en origen | 2 |
| Se explica con claridad y orden | 1 |

Una respuesta que proponga "corregir los datos a mano" sin dejar registro suma como máximo 3 puntos, solo por la claridad y por los criterios que sí cumpla.

## Rúbrica de la sección E2

Respuesta esperada (son válidas otras equivalentes):

```sql
SELECT c.first_name, COALESCE(ct.phone, 'sin teléfono') AS telefono
FROM clientes c
LEFT JOIN contactos ct ON c.document_number = ct.document_number;
```

Resultado: Ana 999111222; Luis, Rosa y Jorge sin teléfono. Jorge no está en `contactos`, por eso hace falta el LEFT JOIN.

| Criterio | Puntos |
|---|---|
| Parte de `clientes` con LEFT JOIN, de modo que Jorge aparece | 3 |
| Usa COALESCE sobre el teléfono con `'sin teléfono'` como valor por defecto | 3 |
| La consulta es correcta en lo demás: columnas, condición del JOIN y sintaxis razonable | 1 |

Con INNER JOIN, Jorge desaparece: máximo 4 puntos. Los errores menores de sintaxis no restan si la lógica es correcta.

## Criterio de selección (abierto)

Este criterio está pendiente de validación. Pedimos al Workstream Lead que lo confirme o lo ajuste antes de corregir el test.

1. **Mínimo para ser elegible:** 50 de 100 puntos en total **y** 16 de 36 en la sección A (SQL).
2. **Orden:** de mayor a menor puntaje total.
3. **Desempate:** primero el puntaje de la sección E, después el de la D, después la pregunta extra A9 y, por último, las evidencias que el postulante subió en el formulario.
4. **Requisitos del formulario:** aval del gerente y disponibilidad de 7 horas semanales.
5. **Si menos de 10 postulantes superan el mínimo:** lo decide el Workstream Lead. La recomendación es no completar los cupos con quienes no alcanzaron el mínimo.
