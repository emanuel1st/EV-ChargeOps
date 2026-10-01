import sqlite3
import sys

sys.path.insert(0, ".")

from app.config import DATABASE_PATH
from app.services.charging_service import registrar_sessao


def test_registrar_sessao():

    resultado = registrar_sessao(
        1,
        1,
        1,
        "2026-10-01T18:00:00",
        "2026-10-01T19:30:00",
        20.0,
        7.4
    )

    assert resultado["duracao_minutos"] == 90
    assert resultado["kwh"] == 20.0

    conexao = sqlite3.connect(DATABASE_PATH)

    sessao = conexao.execute(
        """
        SELECT kwh, potencia_kw, duracao_minutos
        FROM sessoes
        ORDER BY id DESC
        LIMIT 1
        """
    ).fetchone()

    conexao.close()

    assert sessao[0] == 20.0
    assert sessao[1] == 7.4
    assert sessao[2] == 90