import sys

sys.path.insert(0, ".")

import sqlite3

from app.config import DATABASE_PATH
from app.services.billing_service import calcular_fatura


def test_calcular_fatura():

    resultado = calcular_fatura(1, "2026-10")

    assert resultado["usuario_id"] == 1
    assert resultado["mes"] == "2026-10"
    assert resultado["total_kwh"] >= 0
    assert resultado["valor_total"] >= 0

    conexao = sqlite3.connect(DATABASE_PATH)

    fatura = conexao.execute(
        """
        SELECT total_kwh, valor_total, status
        FROM faturas
        ORDER BY id DESC
        LIMIT 1
        """
    ).fetchone()

    conexao.close()

    assert fatura is not None
    assert fatura[0] == resultado["total_kwh"]
    assert fatura[1] == resultado["valor_total"]
    assert fatura[2] == "pendente"