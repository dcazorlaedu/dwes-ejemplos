# 01_ejercicio_UT1 · Del archivo HTML a la página dinámica

**UT1 · RA1 · Nivel 1** — Introducción al desarrollo de aplicaciones web

**RA1:** Selecciona las arquitecturas y tecnologías de programación web en entorno servidor, analizando sus capacidades y características propias.

**Criterios trabajados:** RA1 a), RA1 b), RA1 c), RA1 f)

## Situación

El club «Sendas del Sureste» tiene una web estática y quiere mostrar la fecha de la próxima salida y el nombre de quien visita la página. Trabajas con el entorno Docker del material (servidor web en `http://localhost:8080`).

## Enunciado

1. Crea `estatica.html` y `dinamica.php` con el mismo aspecto. Explica, con lo que ves en el navegador y en la pestaña *Red* (F12), qué se ejecuta en el servidor y qué en el cliente.
2. Haz que `dinamica.php` muestre la fecha y la hora del servidor y un saludo con el nombre recibido por la URL (`?nombre=...`). Compara el HTML recibido con el código fuente del fichero `.php`.
3. Describe qué mecanismo usa el servidor para ejecutar PHP en tu entorno (módulo de Apache o PHP-FPM) y cómo decide qué ficheros procesa por extensión.
4. Identifica en tu página dónde se integran el lenguaje de marcas y el lenguaje de programación (etiquetas de apertura/cierre, `<?= ?>`) y qué ventajas aporta la generación dinámica frente a la página estática.

## Entrega

Los dos ficheros, una captura de la pestaña Red con la respuesta de cada uno y una tabla breve «servidor / cliente» (qué se ejecuta y dónde).

## Criterios de aceptación (compruébalos tú)

- `dinamica.php` muestra una hora distinta al recargar y `estatica.html` no.
- El código fuente recibido en el navegador no contiene etiquetas `<?php`.
- El nombre recibido por la URL se muestra escapado (`htmlspecialchars`).

## Ampliación (opcional, no evaluable)

- Observa en la pestaña Red las cabeceras y el código de estado de una petición `GET` y de otra a una ruta inexistente (404). Fíjate en `Content-Type`, `Cache-Control` y `Set-Cookie`.

## Pista

El navegador nunca recibe código PHP: solo HTML. Comprueba con «Ver código fuente» y con la cabecera `Content-Type`.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/01_ejercicio_UT1/)
