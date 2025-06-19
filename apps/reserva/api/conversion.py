import requests
from decimal import Decimal
from django.conf import settings

def convertir_moneda(monto, moneda_destino):
    # DEBO USAR VARIABLES DE ENTORNO
    url = f"https://v6.exchangerate-api.com/v6/{settings.EXCHANGE_API_KEY}/latest/ARS"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    tasa = data['conversion_rates'].get(moneda_destino)

    if tasa is None:
        raise Exception(f"Tasa de cambio no encontrada para {moneda_destino}")

    return round(monto * Decimal(str(tasa)), 2)

def calcular_duracion_en_horas(turno):
    inicio = turno.hora_inicio
    fin = turno.hora_fin

    # Convertir a segundos desde medianoche
    inicio_seg = inicio.hour * 3600 + inicio.minute * 60 + inicio.second
    fin_seg = fin.hour * 3600 + fin.minute * 60 + fin.second

    # Calcular duración en horas como Decimal
    segundos = fin_seg - inicio_seg
    return Decimal(segundos) / Decimal(3600)