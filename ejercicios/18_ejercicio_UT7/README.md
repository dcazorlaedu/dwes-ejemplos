# 18_ejercicio_UT7 · Página dinámica: panel actualizable e internacionalización

**UT7 · RA8 + RA9 · Nivel 2** — Páginas interactivas y aplicaciones híbridas

**RA8:** Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas.
**RA9:** Desarrolla aplicaciones web híbridas seleccionando y utilizando tecnologías, frameworks servidor y repositorios heterogéneos de información.

**Criterios trabajados:** RA8 d), RA8 f), RA8 g)

## Situación

Se construye un panel de reservas que modifica su contenido sin recargar, disponible en español e inglés.

## Enunciado

1. Crea una API de reservas (GET/POST) y un panel que actualice la lista y el total tras cada reserva modificando el DOM (crear y eliminar elementos, actualizar contadores).
2. Internacionaliza la interfaz: diccionario de textos por idioma, detección con `Accept-Language`, formateo de fechas y moneda con la extensión `intl` y plurales con `MessageFormatter`.
3. Permite cambiar el idioma desde la página y recuerda la elección (cookie o sesión).
4. Aplica estas tecnologías en una aplicación completa: protege la API con token CSRF y comprueba que un envío sin él falla.

## Entrega

Panel, API, textos traducidos y una captura de la aplicación en cada idioma.

## Criterios de aceptación (compruébalos tú)

- La lista y el total se actualizan sin recargar.
- Los números y fechas cambian de formato según el idioma.
- El plural «1 plaza / 5 plazas» es correcto en ambos idiomas.

## Pista

No concatenes frases traducidas: usa mensajes completos con marcadores.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/18_ejercicio_UT7/)
