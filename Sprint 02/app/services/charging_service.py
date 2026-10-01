import sqlite3
from datetime import datetime
from app.config import DATABASE_PATH


def registrar_sessao(
    usuario_id,
    veiculo_id,
    carregador_id,
    inicio,
    fim,
    kwh,
    potencia_kw
):
    inicio_dt = datetime.fromisoformat(inicio)
    fim_dt = datetime.fromisoformat(fim)

    duracao = int((fim_dt - inicio_dt).total_seconds() / 60)

    conexao = sqlite3.connect(DATABASE_PATH)

    conexao.execute(
        """
        INSERT INTO sessoes (
            usuario_id,
            veiculo_id,
            carregador_id,
            inicio,
            fim,
            duracao_minutos,
            kwh,
            potencia_kw,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            usuario_id,
            veiculo_id,
            carregador_id,
            inicio,
            fim,
            duracao,
            kwh,
            potencia_kw,
            "concluida"
        )
    )

    conexao.commit()
    conexao.close()

    return {
        "mensagem": "Sessão registrada com sucesso!",
        "duracao_minutos": duracao,
        "kwh": kwh
    }