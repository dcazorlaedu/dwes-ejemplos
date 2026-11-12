# 08_ejercicio_UT3 · CRUD de productos con consultas preparadas

**UT3 · RA6 · Nivel 2** — Acceso a bases de datos desde PHP

**RA6:** Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información.

**Criterios trabajados:** RA6 c), RA6 d), RA6 f), RA6 g)

## Situación

El almacén necesita añadir, modificar y borrar productos desde una página de administración, sin riesgo de inyección SQL.

## Enunciado

1. Implementa un listado con búsqueda por nombre y paginación (`LIMIT`/`OFFSET`, con parámetros enteros).
2. Crea el formulario de alta y la inserción con consulta preparada (nombre, categoría, precio, stock) validando los datos antes de enviarlos.
3. Implementa la edición y el borrado (este último con `POST` y confirmación) y muestra mensajes de resultado con el patrón *Post/Redirect/Get*.
4. Demuestra, con una búsqueda del tipo `x' OR '1'='1`, que tu aplicación no es vulnerable y explica por qué una consulta construida concatenando texto sí lo sería.
5. Controla los errores: clave ajena inexistente, nombre duplicado y borrado de un producto con pedidos; muestra un mensaje claro sin revelar detalles internos.

## Entrega

Aplicación (listado, alta, edición, borrado) y capturas de la prueba de inyección y de los errores controlados.

## Criterios de aceptación (compruébalos tú)

- La búsqueda con `x' OR '1'='1` no devuelve todos los productos.
- Cada operación muestra un mensaje de confirmación.
- Un borrado imposible por clave ajena muestra un error controlado.

## Ampliación (opcional, no evaluable)

- Aísla el SQL de productos en una clase repositorio y compara el diseño antes y después.

## Pista

Los marcadores `:nombre` o `?` solo sustituyen **valores**, nunca nombres de tablas o columnas.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/08_ejercicio_UT3/)
