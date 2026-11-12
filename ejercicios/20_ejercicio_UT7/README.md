# 20_ejercicio_UT7 · Informe con librerías, pruebas y documentación

**UT7 · RA8 + RA9 · Nivel 4** — Páginas interactivas y aplicaciones híbridas

**RA8:** Genera páginas web dinámicas analizando y utilizando tecnologías y frameworks del servidor web que añadan código al lenguaje de marcas.
**RA9:** Desarrolla aplicaciones web híbridas seleccionando y utilizando tecnologías, frameworks servidor y repositorios heterogéneos de información.

**Criterios trabajados:** RA8 g), RA9 e), RA9 g), RA9 h)

## Situación

La dirección pide un informe mensual de reservas con gráficos y exportación a Excel/PDF, con calidad verificable.

## Enunciado

1. Calcula estadísticas con una biblioteca (por ejemplo `league/csv` + funciones de agregación) sobre un CSV grande usando generadores y mide la memoria usada.
2. Genera un informe en PDF (Dompdf) y una hoja de cálculo (PhpSpreadsheet) y un gráfico simple en la página con una biblioteca de JavaScript.
3. Desarrolla con TDD una clase de cálculo (por ejemplo `CalculoOcupacion`): escribe primero las pruebas con PHPUnit (rojo), implementa (verde) y refactoriza.
4. Depura un fallo con registro (Monolog) y herramientas del navegador, y documenta la aplicación con un README y comentarios de documentación.
5. Reflexiona sobre cuándo los datos justifican herramientas de Big Data o de inteligencia de negocios y qué librerías usarías.

## Entrega

Proyecto con `composer.json`, pruebas en verde, informes generados y documentación.

## Criterios de aceptación (compruébalos tú)

- `vendor/bin/phpunit` termina en verde.
- El PDF y el XLSX se generan desde la aplicación.
- La memoria máxima no crece con el tamaño del fichero.

## Pista

Un generador (`yield`) procesa un fichero enorme con memoria casi constante.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/20_ejercicio_UT7/)
