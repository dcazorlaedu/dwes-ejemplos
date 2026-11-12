# 17_ejercicio_UT7 · Buscador interactivo con AJAX y validación

**UT7 · RA8 + RA9 · Nivel 1** — Páginas interactivas y aplicaciones híbridas

**RA8:** Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas.
**RA9:** Desarrolla aplicaciones web híbridas seleccionando y utilizando tecnologías, frameworks servidor y repositorios heterogéneos de información.

**Criterios trabajados:** RA8 a), RA8 b), RA8 c), RA8 d), RA8 e)

## Situación

La tienda quiere un buscador que se actualice mientras se escribe y un formulario de reserva que valide sin recargar la página.

## Enunciado

1. Explica las diferencias entre código del servidor y del cliente y las ventajas de combinar PHP y JavaScript en una aplicación (interactividad, menos recargas, reutilización de la API).
2. Crea un endpoint PHP que devuelva productos en JSON según `?q=` y una página con `fetch` que muestre los resultados mientras se escribe, con retardo (*debounce*) de 300 ms.
3. Gestiona los estados de la interfaz: cargando, sin resultados, error de red y error del servidor (4xx/5xx); recuerda que `fetch` no rechaza los códigos HTTP de error.
4. Añade un formulario de reserva con verificación en el cliente (JavaScript) y en el servidor (códigos 422), mostrando los errores junto a cada campo.
5. Identifica las tecnologías y frameworks que podrías usar para este caso (Fetch API, Axios, Alpine.js, htmx, Vue, Livewire…) y elige una con argumentos.

## Entrega

Código del endpoint y de la página, capturas de los estados y una tabla de tecnologías.

## Criterios de aceptación (compruébalos tú)

- Escribir en el cuadro actualiza la lista sin recargar y con una sola petición por pausa.
- Se distinguen visualmente los estados cargando/vacío/error.
- Un dato malicioso en un producto no ejecuta código en la página.

## Pista

El texto recibido del servidor se inserta con `textContent`, no con `innerHTML`.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/17_ejercicio_UT7/)
