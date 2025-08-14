-- Tabla de Tarjetas
CREATE TABLE IF NOT EXISTS tarjetas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    emisor TEXT,
    tipo TEXT CHECK(tipo IN ('Crédito', 'Débito')) NOT NULL,
    limite REAL DEFAULT 0,
    saldo_actual REAL DEFAULT 0,
    fecha_corte TEXT,
    fecha_pago TEXT,
    notas TEXT
);

-- Tabla de Servicios recurrentes
CREATE TABLE IF NOT EXISTS servicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    monto_defecto REAL NOT NULL,
    periodicidad TEXT CHECK(periodicidad IN ('Mensual', 'Semanal', 'Anual')) NOT NULL,
    proveedor TEXT,
    categoria TEXT,
    estado TEXT CHECK(estado IN ('Activo', 'Inactivo')) DEFAULT 'Activo',
    notas TEXT
);
