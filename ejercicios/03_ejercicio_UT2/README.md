# 03_ejercicio_UT2 · Primera página PHP embebida en HTML

**UT2 · RA2 + RA3 · Nivel 1** — Programación PHP del lado del servidor

**RA2:** Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.
**RA3:** Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.

**Criterios trabajados:** RA2 a), RA2 b), RA2 c), RA2 d), RA2 e), RA3 g)

## Situación

Necesitas una página de presentación del club que mezcle HTML y PHP. Se ejecuta en el entorno Docker (`http://localhost:8080`).

## Enunciado

1. Crea `club.php` con HTML válido y bloques `<?php ... ?>` y `<?= ... ?>` que muestren el nombre del club, el año actual y una lista de tres salidas guardadas en variables.
2. Explica con tus palabras cómo se genera la página (qué recibe el navegador) y qué tecnologías alternativas existen (ASP.NET, JSP, Python, Node.js).
3. Escribe sentencias simples (`echo`, concatenación, `date()`) y comprueba su efecto en el documento resultante. Añade comentarios de línea, de bloque y HTML, y explica cuáles llegan al navegador.
4. Introduce un error de sintaxis deliberado, localiza el mensaje y corrígelo. Explica por qué el error se ve (o no) según la configuración de `display_errors`.

## Entrega

`club.php`, una captura de la página y un párrafo explicando los comentarios y el error provocado.

## Criterios de aceptación (compruébalos tú)

- La página es HTML válido y la lista se genera desde variables PHP.
- Los comentarios de PHP no aparecen en el código fuente recibido, los de HTML sí.
- El error de sintaxis produce un mensaje con fichero y línea (en desarrollo).

## Pista

Los comentarios de PHP no llegan al navegador; los de HTML sí.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/03_ejercicio_UT2/)
