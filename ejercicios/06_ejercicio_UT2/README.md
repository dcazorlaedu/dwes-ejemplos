# 06_ejercicio_UT2 · Formulario de inscripción con validación y patrón PRG

**UT2 · RA2 + RA3 · Nivel 4** — Programación PHP del lado del servidor

**RA2:** Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.
**RA3:** Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.

**Criterios trabajados:** RA2 e), RA3 d), RA3 e), RA3 f)

## Situación

Los socios se inscriben en salidas mediante un formulario. Debes recoger los datos, validarlos en el servidor y confirmar sin duplicar envíos.

## Enunciado

1. Crea `inscripcion.php` con un formulario (nombre, correo, edad, salida, aceptación) enviado por `POST` y etiquetas `label` asociadas a cada campo.
2. Recupera los datos con `$_POST`, valida cada campo (longitud, formato de correo con `filter_var`, rango de edad, valor de la lista) y muestra los errores junto a cada campo conservando lo escrito.
3. Si todo es válido, guarda la inscripción en un fichero (CSV o JSON), redirige con el patrón *Post/Redirect/Get* y muestra un mensaje de confirmación en la página de destino.
4. Demuestra que la salida está escapada con `htmlspecialchars` enviando un nombre con etiquetas HTML y explica por qué la validación del navegador (HTML5) no basta.
5. Explica la diferencia entre `GET` y `POST` y entre `$_GET`, `$_POST` y `$_REQUEST`; justifica tu elección para este formulario.

## Entrega

La aplicación (página, fichero de datos), capturas del formulario con errores y con confirmación, y un párrafo sobre seguridad.

## Criterios de aceptación (compruébalos tú)

- Un envío con datos inválidos muestra errores y conserva los valores.
- Un envío válido guarda una fila y redirige (código 302/303).
- Recargar la página de confirmación no crea otra fila.
- Una etiqueta `<b>` en el nombre se muestra como texto.

## Ampliación (opcional, no evaluable)

- Añade validación de subida de un fichero (foto de perfil): comprueba tamaño, tipo real con `finfo` y guárdalo con un nombre aleatorio fuera de la raíz web.

## Pista

Tras guardar, redirige con `header('Location: ...')` y `exit`; al recargar la página de confirmación no debe duplicarse la inscripción.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/06_ejercicio_UT2/)
