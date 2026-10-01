import sqlite3
from flask import Blueprint, render_template, request, redirect, url_for

from app.config import DATABASE_PATH
from app.services.billing_service import calcular_fatura


invoices_bp = Blueprint("invoices", __name__)


@invoices_bp.route("/faturas")
def faturas():

    conexao = sqlite3.connect(DATABASE_PATH)

    faturas = conexao.execute(
        """
        SELECT
            faturas.id,
            usuarios.nome,
            faturas.mes,
            faturas.total_kwh,
            faturas.tarifa_kwh,
            faturas.taxa_fixa,
            faturas.valor_total,
            faturas.status
        FROM faturas
        JOIN usuarios ON usuarios.id = faturas.usuario_id
        ORDER BY faturas.id DESC
        """
    ).fetchall()

    usuarios = conexao.execute(
       "SELECT id, nome FROM usuarios ORDER BY nome"
    ).fetchall()

    conexao.close()

    return render_template(
    "invoices.html",
    faturas=faturas,
    usuarios=usuarios
)


@invoices_bp.route("/faturas/nova", methods=["POST"])
def nova_fatura():

    usuario_id = int(request.form["usuario_id"])
    mes = request.form["mes"]

    calcular_fatura(usuario_id, mes)

    return redirect(url_for("invoices.faturas"))