import sqlite3

from flask import Blueprint, render_template

from app.config import DATABASE_PATH


users_bp = Blueprint("users", __name__)


@users_bp.route("/usuarios")
def usuarios():

    conexao = sqlite3.connect(DATABASE_PATH)

    usuarios = conexao.execute(
        """
        SELECT
            usuarios.id,
            usuarios.nome,
            usuarios.email,
            unidades.identificacao
        FROM usuarios
        LEFT JOIN unidades
            ON unidades.id = usuarios.unidade_id
        ORDER BY usuarios.nome
        """
    ).fetchall()

    conexao.close()

    return render_template(
        "users.html",
        usuarios=usuarios
    )