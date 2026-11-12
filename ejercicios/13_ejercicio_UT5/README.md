# 13_ejercicio_UT5 · De la página a un MVC mínimo

**UT5 · RA5 · Nivel 2** — Desarrollo con un framework (Laravel)

**RA5:** Desarrolla aplicaciones web identificando y aplicando mecanismos para separar el código de presentación de la lógica de negocio.

**Criterios trabajados:** RA5 a), RA5 b), RA5 c), RA5 e), RA5 g)

## Situación

La página de administración del almacén mezcla HTML, SQL y reglas de negocio. Debes separarlas sin usar todavía un framework.

## Enunciado

1. Analiza el código de una página que mezcla presentación y lógica y enumera los problemas (mantenimiento, pruebas, seguridad, reutilización).
2. Reorganiza la aplicación en tres capas: modelo (clases `Producto` y `ProductoRepositorio`), vista (plantillas con solo HTML y `<?= ?>`) y controlador (`ProductoControlador`) con un enrutador sencillo (`index.php?accion=...`).
3. Aplica principios de POO: interfaz del repositorio, inyección de dependencias en el controlador y propiedades `readonly`.
4. Mueve la configuración (conexión, entorno) a un fichero propio y lee los parámetros de variables de entorno.
5. Explica qué ganas con esta separación y qué frameworks (Laravel, Symfony) la ofrecen ya resuelta.

## Entrega

Estructura de carpetas, código de las tres capas y una explicación de una página sobre la separación de responsabilidades.

## Criterios de aceptación (compruébalos tú)

- Las plantillas no contienen SQL.
- El controlador depende de una interfaz de repositorio, no de PDO directamente.
- Cambiar el título de la página solo exige tocar la vista.

## Pista

Una vista no debería contener consultas SQL ni decisiones de negocio.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/13_ejercicio_UT5/)
