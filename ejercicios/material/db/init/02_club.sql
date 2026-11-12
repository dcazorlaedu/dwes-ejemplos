-- Datos ficticios del club «Sendas del Sureste» para los ejercicios de UT6 y UT7.
USE tienda;
DROP TABLE IF EXISTS reservas, rutas;
CREATE TABLE rutas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(80) NOT NULL UNIQUE, km DECIMAL(4,1) NOT NULL CHECK (km > 0),
  dificultad ENUM('baja','media','alta') NOT NULL, plazas SMALLINT NOT NULL CHECK (plazas > 0), fecha DATE NOT NULL) ENGINE=InnoDB;
CREATE TABLE reservas (id INT AUTO_INCREMENT PRIMARY KEY, id_ruta INT NOT NULL, nombre VARCHAR(60) NOT NULL, personas TINYINT NOT NULL CHECK (personas BETWEEN 1 AND 12),
  creada DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (id_ruta) REFERENCES rutas(id)) ENGINE=InnoDB;
INSERT INTO rutas (nombre, km, dificultad, plazas, fecha) VALUES
 ('Sierra Espuña',12.0,'media',15,'2026-11-21'),('Cabo Cope',9.0,'baja',20,'2026-11-28'),('Sierra de la Pila',16.0,'alta',12,'2026-12-05'),
 ('Calblanque',14.0,'media',25,'2026-12-12'),('Peña del Águila',11.0,'media',18,'2026-12-19'),('Barrancos de Gebas',8.5,'baja',22,'2027-01-09');
INSERT INTO reservas (id_ruta, nombre, personas) VALUES (1,'Ana López',2),(1,'Luis Martínez',4),(2,'Carmen Sánchez',3),(3,'Pedro Navarro',1),(4,'Lucía Navarro',5);
