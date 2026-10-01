import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for

from app.config import DATABASE_PATH
from app.services.charging_service import registrar_sessao


sessions_bp = Blueprint("sessions", __name__)


@sessions_bp.route("/sessao/nova", methods=["GET", "POST"])
def nova_sessao():

    conexao = sqlite3.connect(DATABASE_PATH)

    usuarios = conexao.execute(
        "SELECT id, nome FROM usuarios ORDER BY nome"
    ).fetchall()

    veiculos = conexao.execute(
        "SELECT id, modelo, placa FROM veiculos ORDER BY modelo"
    ).fetchall()

    carregadores = conexao.execute(
        "SELECT id, identificacao, localizacao FROM carregadores ORDER BY identificacao"
    ).fetchall()

    conexao.close()

    if request.method == "POST":

        usuario_id = int(request.form["usuario_id"])
        veiculo_id = int(request.form["veiculo_id"])
        carregador_id = int(request.form["carregador_id"])
        inicio = request.form["inicio"]
        fim = request.form["fim"]
        kwh = float(request.form["kwh"])
        potencia_kw = float(request.form["potencia_kw"])

        registrar_sessao(
            usuario_id,
            veiculo_id,
            carregador_id,
            inicio,
            fim,
            kwh,
            potencia_kw
        )

        return redirect(url_for("dashboard.dashboard"))

    return render_template(
        "nova_sessao.html",
        usuarios=usuarios,
        veiculos=veiculos,
        carregadores=carregadores
    )