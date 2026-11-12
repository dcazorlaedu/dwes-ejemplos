# 14_ejercicio_UT5 · Tienda con Laravel: CRUD, autorización y pruebas

**UT5 · RA5 · Nivel 3** — Desarrollo con un framework (Laravel)

**RA5:** Desarrolla aplicaciones web identificando y aplicando mecanismos para separar el código de presentación de la lógica de negocio.

**Criterios trabajados:** RA5 b), RA5 d), RA5 e), RA5 f), RA5 h)

## Situación

Se reconstruye el catálogo con Laravel (Composer instalado en el equipo o en el contenedor). Se parte de un proyecto nuevo con `laravel new` o `composer create-project`.

## Enunciado

1. Crea el proyecto, define la migración y el modelo Eloquent de `Producto` y `Categoria` (relación `belongsTo`/`hasMany`) y un *seeder* con datos de prueba.
2. Implementa rutas de recurso, un controlador, vistas Blade con un layout común y un formulario generado dinámicamente con validación mediante un *Form Request*; muestra los errores y los valores antiguos (`old()`).
3. Incorpora autenticación y una Policy para que solo el rol «almacén» edite y solo «administrador» borre; protege las rutas con *middleware*.
4. Evita el problema N+1 con `with()` y demuestra el número de consultas antes y después.
5. Escribe al menos cuatro pruebas de *Feature* con `RefreshDatabase` (listado público, validación, autorización 403, creación) y documenta cómo ejecutarlas (`php artisan test`).

## Entrega

Repositorio del proyecto (sin `vendor/` ni `.env`), salida de `php artisan test` y un README con instrucciones.

## Criterios de aceptación (compruébalos tú)

- `php artisan test` termina en verde.
- Un usuario sin permiso recibe 403 al intentar editar o borrar.
- La página de listado ejecuta un número constante de consultas, no una por fila.

## Pista

El estado de la aplicación (usuario, mensajes *flash*) se mantiene con sesión; la lógica de negocio va en el modelo o en servicios, no en la vista.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/14_ejercicio_UT5/)
