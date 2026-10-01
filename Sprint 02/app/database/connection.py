import sqlite3
from pathlib import Path
from app.config import DATABASE_PATH

def get_connection():
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_connection()

    connection.executescript("""
    CREATE TABLE IF NOT EXISTS unidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        identificacao TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        unidade_id INTEGER,
        FOREIGN KEY (unidade_id) REFERENCES unidades(id)
    );

    CREATE TABLE IF NOT EXISTS veiculos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        modelo TEXT NOT NULL,
        placa TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );

    CREATE TABLE IF NOT EXISTS carregadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        identificacao TEXT NOT NULL UNIQUE,
        localizacao TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'disponivel'
    );

    CREATE TABLE IF NOT EXISTS sessoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        veiculo_id INTEGER NOT NULL,
        carregador_id INTEGER NOT NULL,
        inicio TEXT NOT NULL,
        fim TEXT,
        duracao_minutos REAL,
        kwh REAL NOT NULL,
        potencia_kw REAL,
        status TEXT NOT NULL DEFAULT 'concluida',
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (veiculo_id) REFERENCES veiculos(id),
        FOREIGN KEY (carregador_id) REFERENCES carregadores(id)
    );

    CREATE TABLE IF NOT EXISTS faturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        mes TEXT NOT NULL,
        total_kwh REAL NOT NULL,
        tarifa_kwh REAL NOT NULL,
        taxa_fixa REAL NOT NULL DEFAULT 0,
        valor_total REAL NOT NULL,
        status TEXT NOT NULL DEFAULT 'aberta',
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
    """)

    connection.commit()
    connection.close()
