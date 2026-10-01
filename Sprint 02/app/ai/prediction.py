import sqlite3

from app.config import DATABASE_PATH


def prever_demanda():

    conexao = sqlite3.connect(DATABASE_PATH)

    resultado = conexao.execute(
        """
        SELECT
            AVG(kwh),
            COUNT(*)
        FROM sessoes
        WHERE kwh > 0
        """
    ).fetchone()

    conexao.close()

    consumo_medio = resultado[0] or 0
    total_sessoes = resultado[1] or 0

    if total_sessoes == 0:
        previsao = 0
    else:
        previsao = consumo_medio

    return {
        "historico_sessoes": total_sessoes,
        "consumo_medio": consumo_medio,
        "previsao_proxima_sessao": previsao
    }