<?php
// db.php: conexión a MySQL. En Docker el servidor se llama «db» (no «localhost»).
function db(): PDO {
    static $pdo = null;
    return $pdo ??= new PDO(
        'mysql:host=' . (getenv('DB_HOST') ?: 'db') . ';dbname=' . (getenv('DB_NAME') ?: 'tienda') . ';charset=utf8mb4',
        getenv('DB_USER') ?: 'dwes', getenv('DB_PASS') ?: 'dwes_dev',
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]
    );
}
function e($s): string { return htmlspecialchars((string) $s, ENT_QUOTES, 'UTF-8'); }
