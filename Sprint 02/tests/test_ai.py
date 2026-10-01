import sys

sys.path.insert(0, ".")

from app.ai.analysis import analisar_consumo
from app.ai.prediction import prever_demanda
from app.ai.anomaly import detectar_anomalias


def test_analise_consumo():

    resultado = analisar_consumo()

    assert "total_sessoes" in resultado
    assert "consumo_total" in resultado
    assert "consumo_medio" in resultado
    assert "maior_consumo" in resultado


def test_previsao_demanda():

    resultado = prever_demanda()

    assert "historico_sessoes" in resultado
    assert "consumo_medio" in resultado
    assert "previsao_proxima_sessao" in resultado


def test_deteccao_anomalias():

    resultado = detectar_anomalias()

    assert "total_anomalias" in resultado
    assert "anomalias" in resultado