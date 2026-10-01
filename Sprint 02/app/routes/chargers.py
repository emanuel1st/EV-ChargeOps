import sqlite3

from flask import Blueprint, render_template

from app.config import DATABASE_PATH


chargers_bp = Blueprint("chargers", __name__)


@chargers_bp.route("/carregadores")
def carregadores():

    conexao = sqlite3.connect(DATABASE_PATH)

    carregadores = conexao.execute(
        """
        SELECT
            id,
            identificacao,
            localizacao,
            status
        FROM carregadores
        ORDER BY identificacao
        """
    ).fetchall()

    conexao.close()

    return render_template(
        "chargers.html",
        carregadores=carregadores
    )