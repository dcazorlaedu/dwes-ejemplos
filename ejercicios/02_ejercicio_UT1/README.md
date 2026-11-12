# 02_ejercicio_UT1 · Arquitectura y herramientas para una aplicación de reservas

**UT1 · RA1 · Nivel 2** — Introducción al desarrollo de aplicaciones web

**RA1:** Selecciona las arquitecturas y tecnologías de programación web en entorno servidor, analizando sus capacidades y características propias.

**Criterios trabajados:** RA1 c), RA1 d), RA1 e), RA1 f), RA1 g)

## Situación

Una asociación quiere una aplicación de reservas de salidas con listado público, panel de gestión y una app móvil en el futuro. Debes proponer la arquitectura y las herramientas sin escribir todavía el código.

## Enunciado

1. Dibuja un diagrama con navegador, servidor web, intérprete de PHP y base de datos y explica el recorrido de una petición «ver el listado de salidas».
2. Compara tres opciones: PHP «puro» con páginas, un framework (Laravel) y una API + aplicación de una sola página. Indica ventajas, inconvenientes y cuándo elegirías cada una.
3. Enumera los lenguajes y tecnologías de servidor más habituales (PHP, Node.js, Python, Java, .NET…) y razona por qué PHP + MySQL encaja aquí.
4. Explica el papel de un servidor de aplicaciones o *runtime* frente a un servidor web, y qué herramientas (Composer, Git, Docker, depurador) usarías en el equipo.
5. Describe cómo integrarías HTML/CSS/JavaScript con PHP en esta aplicación y qué parte correspondería a cada tecnología.

## Entrega

Diagrama, tabla comparativa y una recomendación argumentada de una página.

## Criterios de aceptación (compruébalos tú)

- El diagrama muestra el sentido de la petición y de la respuesta.
- La tabla compara al menos tres criterios (curva de aprendizaje, rendimiento, mantenimiento…).
- La recomendación menciona herramientas concretas (Composer, Docker, Git) y su función.

## Pista

Una buena recomendación justifica la elección con los requisitos (equipo, plazos, escalabilidad, mantenimiento), no con preferencias.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/02_ejercicio_UT1/)
