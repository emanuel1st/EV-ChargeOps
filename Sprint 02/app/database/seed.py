from app.database.connection import get_connection

def seed_database():
    connection = get_connection()

    connection.execute(
        "INSERT OR IGNORE INTO unidades (id, identificacao) VALUES (?, ?)",
        (1, "Unidade 101")
    )

    connection.execute(
        "INSERT OR IGNORE INTO usuarios (id, nome, email, unidade_id) VALUES (?, ?, ?, ?)",
        (1, "João Silva", "joao@exemplo.com", 1)
    )

    connection.execute(
        "INSERT OR IGNORE INTO veiculos (id, usuario_id, modelo, placa) VALUES (?, ?, ?, ?)",
        (1, 1, "BYD Dolphin", "ABC1D23")
    )

    connection.execute(
        "INSERT OR IGNORE INTO carregadores (id, identificacao, localizacao, status) VALUES (?, ?, ?, ?)",
        (1, "HCA-G2-01", "Estacionamento L1", "disponivel")
    )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    seed_database()
    print("Dados de teste inseridos.")
