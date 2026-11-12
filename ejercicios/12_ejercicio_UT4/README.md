# 12_ejercicio_UT4 · Roles, CSRF y depuración

**UT4 · RA4 · Nivel 3** — Sesiones, estado y autenticación

**RA4:** Desarrolla aplicaciones web embebidas en lenguajes de marcas analizando e incorporando funcionalidades según especificaciones.

**Criterios trabajados:** RA4 d), RA4 e), RA4 f)

## Situación

Se añaden perfiles (comercial, almacén, administrador) y hay que proteger los formularios y probar la aplicación.

## Enunciado

1. Implementa una función única de autorización (`puede($rol, $permiso)`) y úsala para ocultar enlaces **y** para impedir el acceso directo a páginas (403).
2. Protege los formularios con un token CSRF guardado en la sesión y comparado con `hash_equals`; demuestra con `curl` que una petición sin token recibe 403.
3. Limita los intentos de acceso (por ejemplo, bloqueo de 10 minutos tras 3 fallos) y demuestra el bloqueo.
4. Depura un fallo: usa `var_dump`/`error_log`, la pestaña Red y los registros del servidor para localizar un error que introduzcas deliberadamente, y escribe tres pruebas manuales o automáticas de la autorización.

## Entrega

Código, evidencias de las pruebas (capturas o salidas de `curl`) y un informe de depuración de media página.

## Criterios de aceptación (compruébalos tú)

- Un comercial recibe 403 al abrir la página de administración escribiendo la URL.
- Un POST sin token CSRF recibe 403.
- Tras 3 intentos fallidos el usuario queda bloqueado y el mensaje no revela si existe la cuenta.

## Ampliación (opcional, no evaluable)

- Sustituye el bloqueo por un límite de peticiones por IP con cabeceras `Retry-After` y `X-RateLimit-Remaining`.

## Pista

Oculta lo que el usuario no puede hacer **y** comprueba el permiso en el servidor.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/12_ejercicio_UT4/)
