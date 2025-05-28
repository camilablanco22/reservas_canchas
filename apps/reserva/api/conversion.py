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