<?php /* Página de prueba: ábrela en http://localhost:8080/ */ ?>
<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><title>Entorno</title></head>
<body>
<h1>Entorno listo</h1>
<p>PHP <?= PHP_VERSION ?> · <?= php_sapi_name() ?></p>
<?php require __DIR__ . "/db.php"; ?>
<p>MySQL <?= db()->getAttribute(PDO::ATTR_SERVER_VERSION) ?> · <?= db()->query("SELECT COUNT(*) FROM productos")->fetchColumn() ?> productos</p>
</body></html>
