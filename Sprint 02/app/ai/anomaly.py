import sqlite3

from app.config import DATABASE_PATH


def detectar_anomalias():

    conexao = sqlite3.connect(DATABASE_PATH)

    sessoes = conexao.execute(
        """
        SELECT
            id,
            usuario_id,
            kwh,
            inicio
        FROM sessoes
        WHERE kwh > 0
        ORDER BY id DESC
        """
    ).fetchall()

    conexao.close()

    if not sessoes:
        return {
            "total_anomalias": 0,
            "anomalias": []
        }

    consumos = [sessao[2] for sessao in sessoes]

    media = sum(consumos) / len(consumos)

    limite = media * 1.5

    anomalias = []

    for sessao in sessoes:

        if sessao[2] > limite:

            anomalias.append({
                "id": sessao[0],
                "usuario_id": sessao[1],
                "kwh": sessao[2],
                "inicio": sessao[3]
            })

    return {
        "total_anomalias": len(anomalias),
        "media": media,
        "limite": limite,
        "anomalias": anomalias
    }