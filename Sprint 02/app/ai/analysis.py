import sqlite3

from app.config import DATABASE_PATH


def analisar_consumo():

    conexao = sqlite3.connect(DATABASE_PATH)

    sessoes = conexao.execute(
        """
        SELECT kwh
        FROM sessoes
        WHERE kwh > 0
        """
    ).fetchall()

    conexao.close()

    if not sessoes:
        return {
            "total_sessoes": 0,
            "consumo_total": 0,
            "consumo_medio": 0,
            "maior_consumo": 0
        }

    consumos = [sessao[0] for sessao in sessoes]

    total_sessoes = len(consumos)
    consumo_total = sum(consumos)
    consumo_medio = consumo_total / total_sessoes
    maior_consumo = max(consumos)

    return {
        "total_sessoes": total_sessoes,
        "consumo_total": consumo_total,
        "consumo_medio": consumo_medio,
        "maior_consumo": maior_consumo
    }