import sqlite3
from app.config import DATABASE_PATH, TARIFA_KWH, TAXA_FIXA


def calcular_fatura(usuario_id, mes):
    conexao = sqlite3.connect(DATABASE_PATH)

    resultado = conexao.execute(
        """
        SELECT COALESCE(SUM(kwh), 0)
        FROM sessoes
        WHERE usuario_id = ?
        AND strftime('%Y-%m', inicio) = ?
        """,
        (usuario_id, mes)
    ).fetchone()

    total_kwh = resultado[0]

    valor_consumo = total_kwh * TARIFA_KWH
    valor_total = valor_consumo + TAXA_FIXA

    conexao.execute(
        """
        INSERT INTO faturas (
            usuario_id,
            mes,
            total_kwh,
            tarifa_kwh,
            taxa_fixa,
            valor_total,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            usuario_id,
            mes,
            total_kwh,
            TARIFA_KWH,
            TAXA_FIXA,
            valor_total,
            "pendente"
        )
    )

    conexao.commit()
    conexao.close()

    return {
        "usuario_id": usuario_id,
        "mes": mes,
        "total_kwh": total_kwh,
        "tarifa_kwh": TARIFA_KWH,
        "taxa_fixa": TAXA_FIXA,
        "valor_total": valor_total
    }