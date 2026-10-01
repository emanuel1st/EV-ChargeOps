from flask import Blueprint, render_template

from app.services.ai_service import gerar_analise_completa


ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/ia")
def analise_ia():

    resultado = gerar_analise_completa()

    return render_template(
        "ai.html",
        analise=resultado["analise"],
        previsao=resultado["previsao"],
        anomalias=resultado["anomalias"]
    )