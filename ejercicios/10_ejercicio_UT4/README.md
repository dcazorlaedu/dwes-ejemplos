# 10_ejercicio_UT4 · Cookies y preferencias del usuario

**UT4 · RA4 · Nivel 1** — Sesiones, estado y autenticación

**RA4:** Desarrolla aplicaciones web embebidas en lenguajes de marcas analizando e incorporando funcionalidades según especificaciones.

**Criterios trabajados:** RA4 a), RA4 b), RA4 c)

## Situación

Los socios quieren elegir tema claro u oscuro y que la web lo recuerde. Trabajas con cookies y almacenamiento en el cliente.

## Enunciado

1. Explica qué información sobre un cliente web puede mantenerse (cookies, sesión, almacenamiento local) y en qué se diferencian en lugar de almacenamiento, duración y seguridad.
2. Crea una página que guarde la preferencia de tema en una cookie con `setcookie` (caducidad de 30 días, `SameSite=Lax`) y la use en la siguiente visita.
3. Añade un contador de visitas por sesión con `$_SESSION` y muestra cómo viaja el identificador de sesión en la cookie `PHPSESSID`.
4. Guarda un dato en el cliente con JavaScript (`localStorage`) y recupéralo al recargar; indica qué datos **no** deberían guardarse allí.

## Entrega

Páginas, capturas de la pestaña *Application/Red* con las cookies y una tabla comparativa de mecanismos.

## Criterios de aceptación (compruébalos tú)

- Al recargar, el tema elegido se mantiene.
- El contador de sesión aumenta y se reinicia al cerrar el navegador.
- La cookie tiene fecha de caducidad y `SameSite` visibles en las herramientas.

## Pista

Una cookie se envía en cada petición al sitio: no guardes en ella datos sensibles.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/10_ejercicio_UT4/)
