# 09_ejercicio_UT3 · Pedido transaccional, pruebas y documentación

**UT3 · RA6 · Nivel 3** — Acceso a bases de datos desde PHP

**RA6:** Desarrolla aplicaciones web de acceso a almacenes de datos, aplicando medidas para mantener la seguridad y la integridad de la información.

**Criterios trabajados:** RA6 b), RA6 f), RA6 g)

## Situación

Al confirmar un pedido deben insertarse la cabecera y las líneas y descontarse el stock; si algo falla no debe quedar nada a medias.

## Enunciado

1. Diseña el flujo de «confirmar pedido» (cliente, líneas con producto y cantidad) y escríbelo con una transacción PDO (`beginTransaction`, `commit`, `rollBack`).
2. Comprueba el stock con `SELECT ... FOR UPDATE` dentro de la transacción y rechaza el pedido si no hay unidades suficientes, sin dejar datos parciales.
3. Prueba tres casos con peticiones reales (formulario o `curl`): pedido correcto, stock insuficiente y producto inexistente; registra el estado de las tablas antes y después de cada caso.
4. Explica qué pasaría con dos pedidos simultáneos del mismo producto y cómo lo previene el bloqueo de la fila.
5. Documenta la aplicación: README con requisitos, instalación en Docker, esquema de tablas, decisiones de seguridad y lista de pruebas realizadas.

## Entrega

Código, registro de pruebas (antes/después de cada caso), README de la aplicación y breve análisis de concurrencia.

## Criterios de aceptación (compruébalos tú)

- En el caso de stock insuficiente no existe cabecera de pedido ni líneas.
- En el caso correcto el stock baja exactamente la cantidad pedida.
- El README permite a otra persona ponerlo en marcha.

## Pista

El orden importa: comprobar y bloquear primero, insertar y descontar después, confirmar al final.

## Material

Entorno Docker y datos en [`../material/`](../material/LEEME.md). Guarda tus páginas en `src/` y ábrelas en `http://localhost:8080`; consulta la base de datos con DataGrip (`localhost:3306`, usuario `dwes`).

[Ver en el sitio web](https://dcazorlaedu.github.io/dwes-ejemplos/ejercicios/09_ejercicio_UT3/)
