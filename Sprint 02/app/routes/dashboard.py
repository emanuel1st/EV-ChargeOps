import sqlite3
from flask import Blueprint, render_template
from app.config import DATABASE_PATH

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard")
def dashboard():

    conexao = sqlite3.connect(DATABASE_PATH)

    total_kwh = conexao.execute(
        "SELECT COALESCE(SUM(kwh), 0) FROM sessoes"
    ).fetchone()[0]

    total_sessoes = conexao.execute(
        "SELECT COUNT(*) FROM sessoes"
    ).fetchone()[0]

    total_faturamento = conexao.execute(
        "SELECT COALESCE(SUM(valor_total), 0) FROM faturas"
    ).fetchone()[0]

    total_usuarios = conexao.execute(
        "SELECT COUNT(*) FROM usuarios"
    ).fetchone()[0]

    sessoes = conexao.execute(
        """
        SELECT
            usuarios.nome,
            veiculos.modelo,
            carregadores.identificacao,
            sessoes.kwh,
            sessoes.status
        FROM sessoes
        JOIN usuarios ON usuarios.id = sessoes.usuario_id
        JOIN veiculos ON veiculos.id = sessoes.veiculo_id
        JOIN carregadores ON carregadores.id = sessoes.carregador_id
        ORDER BY sessoes.id DESC
        """
    ).fetchall()

    conexao.close()

    return render_template(
        "dashboard.html",
        total_kwh=total_kwh,
        total_sessoes=total_sessoes,
        total_faturamento=total_faturamento,
        total_usuarios=total_usuarios,
        sessoes=sessoes
    )