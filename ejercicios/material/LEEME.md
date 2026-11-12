# Entorno de prácticas de DWES (Docker + DataGrip)

1. Instala Docker (Docker Desktop o Docker Engine con *compose*).
2. En esta carpeta ejecuta `docker compose up -d`. La primera vez se construye la imagen de PHP+Apache y se carga la base de datos `tienda`.
3. Abre `http://localhost:8080`: debe aparecer «Entorno listo» con la versión de PHP y de MySQL. **Guarda tus páginas en `src/`**.
4. DataGrip: *+ → Data Source → MySQL*; host `localhost`, puerto `3306`, usuario `dwes`, contraseña `dwes_dev`, base de datos `tienda`.
5. Desde PHP (dentro del contenedor) el servidor de base de datos es **`db`**, no `localhost` (ya está configurado en `src/db.php`).

Datos incluidos:
- `db/init/schema.sql`: TiendaTech (clientes, productos, pedidos…) para UT3, UT4 y UT5.
- `db/init/02_club.sql`: rutas y reservas del club «Sendas del Sureste» para UT6 y UT7.
- `ventas_demo.csv`: 20 000 filas ficticias para el ejercicio de grandes volúmenes (UT7).

Los scripts de `db/init` solo se ejecutan cuando el volumen está vacío. Para recargarlos: `docker compose down -v && docker compose up -d` (borra los datos).
Contraseñas de ejemplo, solo para el aula. Todos los datos son ficticios.
