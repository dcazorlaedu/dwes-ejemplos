# 04_ejercicio_UT2 · Variables, operadores, ámbito y directivas

**UT2 · RA2 + RA3 · Nivel 2** — Programación PHP del lado del servidor

**RA2:** Escribe sentencias ejecutables por un servidor web reconociendo y aplicando procedimientos de integración del código en lenguajes de marcas.
**RA3:** Escribe bloques de sentencias embebidos en lenguajes de marcas, seleccionando y utilizando las estructuras de programación.

**Criterios trabajados:** RA2 f), RA2 g), RA2 h), RA3 a)

## Situación

La tienda del club calcula el precio de las inscripciones con descuentos. Debes practicar tipos, operadores y ámbitos.

## Enunciado

1. Declara variables de los cuatro tipos escalares y de un array; muestra con `var_dump` sus tipos y realiza conversiones (`(int)`, `intval`, `settype`) y comparaciones con `==` y `===` explicando las diferencias.
2. Calcula el precio final de una inscripción con operadores aritméticos, de asignación compuesta, lógicos y de coalescencia nula (`??`).
3. Demuestra el ámbito de variables: una variable global no visible en una función, `global`, `static` y parámetros. Explica cuándo cada opción es adecuada.
4. Usa al menos dos directivas que cambien el comportamiento por defecto (`declare(strict_types=1)`, `ini_set` o `error_reporting`) y muestra el efecto antes y después.
5. Define constantes con `const` y `define()` y explica en qué se diferencian de las variables.

## Entrega

Un fichero `tipos.php` por apartado (o uno con secciones) y una tabla con el resultado esperado frente al observado.

## Criterios de aceptación (compruébalos tú)

- `var_dump` muestra tipos correctos para cada variable.
- La función no puede leer la variable global sin `global` o parámetro.
- La directiva elegida produce un cambio observable en la salida.

## Pista

Con `strict_types=1` una llamada con un tipo distinto al declarado lanza un `TypeError`.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/04_ejercicio_UT2/)
