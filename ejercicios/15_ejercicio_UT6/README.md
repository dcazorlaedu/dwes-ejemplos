# 15_ejercicio_UT6 · Diseña y programa una API REST de rutas

**UT6 · RA7 · Nivel 1** — Servicios web y API REST

**RA7:** Desarrolla servicios web reutilizables y accesibles mediante protocolos web, verificando su funcionamiento.

**Criterios trabajados:** RA7 a), RA7 b), RA7 c), RA7 d), RA7 e)

## Situación

El club quiere ofrecer sus rutas a otras aplicaciones mediante una API. Se parte de la base de datos `tienda` o de una tabla propia `rutas`.

## Enunciado

1. Explica qué es un servicio web, su ámbito (integración entre sistemas, apps móviles, terceros) y las ventajas de exponer la lógica como servicio.
2. Describe los protocolos y estándares implicados (HTTP, REST, JSON, SOAP/WSDL, OpenAPI) y compara REST con SOAP.
3. Diseña los recursos y verbos de la API (`GET/POST/PUT/DELETE /rutas`) con los códigos de estado que devolverá cada caso (200, 201, 204, 404, 422, 405).
4. Programa la API en PHP (un controlador frontal, respuestas JSON, validación y códigos correctos, cabecera `Location` al crear).

## Entrega

Tabla de recursos y códigos, código de la API y salidas de `curl` de al menos un caso por código.

## Criterios de aceptación (compruébalos tú)

- `POST /rutas` válido devuelve 201 y `Location`.
- Un cuerpo inválido devuelve 422 con los errores por campo.
- `DELETE /rutas` (colección) devuelve 405 con `Allow`.

## Pista

Nombres de recurso en plural y en minúsculas; el verbo expresa la acción, no la URL.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/15_ejercicio_UT6/)
