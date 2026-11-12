# 16_ejercicio_UT6 · Prueba, documenta, asegura y consume la API

**UT6 · RA7 · Nivel 2** — Servicios web y API REST

**RA7:** Desarrolla servicios web reutilizables y accesibles mediante protocolos web, verificando su funcionamiento.

**Criterios trabajados:** RA7 e), RA7 f), RA7 g), RA7 h)

## Situación

La API de rutas debe verificarse, documentarse y ser consumida por otra aplicación de forma robusta.

## Enunciado

1. Escribe una batería de pruebas HTTP (script PHP, PHPUnit o colección Postman/Bruno) con al menos ocho casos que cubran códigos 200, 201, 404, 405 y 422 y la paginación.
2. Añade autenticación por token (`Authorization: Bearer`) y comprueba el 401 sin token y el 403 con permisos insuficientes.
3. Documenta la API con un fichero OpenAPI (`openapi.yaml`) con rutas, parámetros, cuerpos y respuestas, y valídalo con una herramienta (Swagger Editor/Redocly).
4. Crea un cliente PHP con cURL que consuma la API con tiempos máximos, control de errores y reintentos para fallos temporales; pruébalo contra una ruta que falla a propósito.

## Entrega

Pruebas y resultado, `openapi.yaml`, cliente PHP y evidencias de las llamadas.

## Criterios de aceptación (compruébalos tú)

- Las pruebas fallan si se rompe un código de estado.
- Sin token la API devuelve 401.
- El cliente reintenta un 503 y no reintenta un 404.

## Ampliación (opcional, no evaluable)

- Añade ETag y respuestas `304 Not Modified`, y un límite de peticiones con `429` y `Retry-After`.

## Pista

Un cliente debe tratar de forma distinta los errores 4xx (no reintentar) y 5xx (reintentar con espera creciente).

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/16_ejercicio_UT6/)
