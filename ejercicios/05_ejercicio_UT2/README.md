# 05_ejercicio_UT2 · Tabla dinámica de salidas con arrays, bucles y funciones

**UT2 · RA2 + RA3 · Nivel 3** — Programación PHP del lado del servidor

**RA2:** Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.
**RA3:** Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.

**Criterios trabajados:** RA3 a), RA3 b), RA3 c), RA3 d), RA3 g)

## Situación

El club guarda sus salidas en un array y quiere mostrarlas en una tabla HTML con resumen estadístico.

## Enunciado

1. Define un array de 6 salidas (ruta, km, dificultad, plazas libres) y recórrelo con `foreach` para generar una tabla; marca en rojo las completas (0 plazas) usando una condición.
2. Utiliza también `for` y `while` para otras salidas (por ejemplo, numerar filas o generar un calendario de 4 semanas) y comprueba que terminan correctamente.
3. Crea funciones con parámetros tipados y valor de retorno (`kmTotales`, `mediaKm`, `filtrarPorDificultad`) y úsalas en la página; añade comentarios `/** ... */` explicando cada una.
4. Ordena el array por kilómetros con `usort` y agrupa por dificultad. Usa funciones de array (`array_map`, `array_filter`, `array_column`).
5. Aplica una estructura de decisión múltiple (`match` o `switch`) para traducir la dificultad a un icono o etiqueta.

## Entrega

`salidas.php` con la tabla, el listado de funciones y una captura del resultado.

## Criterios de aceptación (compruébalos tú)

- La tabla tiene una fila por salida y las filas completas se distinguen visualmente.
- Las funciones tienen tipos de parámetros y de retorno.
- El orden por kilómetros es correcto (ascendente) y el agrupado por dificultad no pierde filas.

## Pista

Si la salida de una función depende de un bucle, escribe primero el caso con un solo elemento y después generaliza.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/05_ejercicio_UT2/)
