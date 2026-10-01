from app.ai.analysis import analisar_consumo
from app.ai.prediction import prever_demanda
from app.ai.anomaly import detectar_anomalias


def gerar_analise_completa():

    analise = analisar_consumo()
    previsao = prever_demanda()
    anomalias = detectar_anomalias()

    return {
        "analise": analise,
        "previsao": previsao,
        "anomalias": anomalias
    }