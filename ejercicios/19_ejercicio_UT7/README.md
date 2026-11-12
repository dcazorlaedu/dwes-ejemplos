# 19_ejercicio_UT7 · Aplicación híbrida con un repositorio externo y otro propio

**UT7 · RA8 + RA9 · Nivel 3** — Páginas interactivas y aplicaciones híbridas

**RA8:** Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas.
**RA9:** Desarrolla aplicaciones web híbridas seleccionando y utilizando tecnologías, frameworks servidor y repositorios heterogéneos de información.

**Criterios trabajados:** RA9 a), RA9 b), RA9 c), RA9 d), RA9 f)

## Situación

La web del club mostrará datos del tiempo de una API pública y publicará su propio repositorio de rutas en formato abierto.

## Enunciado

1. Analiza las ventajas de reutilizar información y código existentes (APIs públicas, bibliotecas) y los riesgos (disponibilidad, licencias, privacidad).
2. Consume una API pública (por ejemplo Open-Meteo, sin clave) desde PHP con cURL y caché local de 10 minutos, y muestra la información procesada (media, máximo, aviso) en una página.
3. Crea un repositorio propio: exporta las rutas de la base de datos a un fichero JSON/CSV versionado y a una API de solo lectura que otros puedan consumir.
4. Integra código de terceros mediante Composer (por ejemplo `nesbot/carbon` o `league/csv`) y explica cómo gestionas versiones y licencias.
5. Gestiona el fallo del servicio externo (tiempo agotado, respuesta inválida) mostrando datos en caché o un mensaje y registrando el incidente.

## Entrega

Aplicación, ficheros exportados, `composer.json` y evidencias de los casos de fallo.

## Criterios de aceptación (compruébalos tú)

- Con el servicio caído la página sigue funcionando.
- El repositorio propio puede leerse con `curl` en JSON.
- Las dependencias se instalan con `composer install`.

## Pista

Nunca muestres al usuario un error técnico del servicio externo.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/19_ejercicio_UT7/)
