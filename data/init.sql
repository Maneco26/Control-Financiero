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
