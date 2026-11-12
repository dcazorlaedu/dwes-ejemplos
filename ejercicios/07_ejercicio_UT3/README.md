# 07_ejercicio_UT3 · Conecta con MySQL y publica el catálogo

**UT3 · RA6 · Nivel 1** — Acceso a bases de datos desde PHP

**RA6:** Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información.

**Criterios trabajados:** RA6 a), RA6 b), RA6 c), RA6 d), RA6 e)

## Situación

La tienda del club (`tienda`, base de datos del entorno Docker) debe mostrar su catálogo en una página web. Conéctate también con DataGrip (`localhost:3306`, usuario `dwes`).

## Enunciado

1. Compara MySQLi y PDO (tabla de ventajas) y elige una tecnología de acceso para el proyecto; justifica la elección.
2. Escribe `db.php` con una función de conexión reutilizable (PDO, excepciones, `utf8mb4`) que lea el servidor de variables de entorno (`db` dentro de Docker).
3. Crea `catalogo.php` que recupere productos con su categoría mediante una consulta con `JOIN` y los publique en una tabla HTML con el precio formateado.
4. Guarda el resultado en un array de resultados (`fetchAll`) y recórrelo con `foreach`; explica la diferencia entre `fetch`, `fetchAll` y recorrer el `PDOStatement`.
5. Verifica en DataGrip que la consulta devuelve las mismas filas que la página.

## Entrega

`db.php`, `catalogo.php`, captura de la página y de DataGrip con la misma consulta.

## Criterios de aceptación (compruébalos tú)

- La página muestra todos los productos con su categoría.
- El mensaje de error de conexión no revela credenciales.
- Los importes se muestran con dos decimales.

## Pista

La conexión se crea una sola vez por petición; guarda las credenciales fuera del código si es posible.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/07_ejercicio_UT3/)
