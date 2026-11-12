# 11_ejercicio_UT4 · Inicio de sesión con contraseñas seguras

**UT4 · RA4 · Nivel 2** — Sesiones, estado y autenticación

**RA4:** Desarrolla aplicaciones web embebidas en lenguajes de marcas analizando e incorporando funcionalidades según especificaciones.

**Criterios trabajados:** RA4 b), RA4 d), RA4 e)

## Situación

El panel del club necesita identificar a los usuarios. Hay que implantar un login seguro.

## Enunciado

1. Crea la tabla de usuarios (correo único, hash de la contraseña, rol) y registra dos usuarios guardando la contraseña con `password_hash`.
2. Implementa `login.php`: verificación con `password_verify`, `session_regenerate_id(true)` al entrar y mensaje de error genérico («usuario o contraseña incorrectos»).
3. Protege `panel.php`: si no hay sesión, redirige al login. Implementa el cierre de sesión destruyendo la sesión y la cookie.
4. Explica los mecanismos de autenticación disponibles (formulario + sesión, HTTP básica, tokens, OAuth) y cuándo usar cada uno.

## Entrega

Aplicación (registro, login, panel, salir) y una tabla de mecanismos de autenticación.

## Criterios de aceptación (compruébalos tú)

- La base de datos no contiene contraseñas en claro.
- Acceder a `panel.php` sin sesión redirige a `login.php`.
- Tras salir, la página protegida deja de ser accesible con el botón «atrás» y recargando.

## Pista

No guardes nunca la contraseña en claro ni con MD5/SHA-1.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/11_ejercicio_UT4/)
