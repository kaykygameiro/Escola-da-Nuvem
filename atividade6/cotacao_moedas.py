import requests
from datetime import datetime

moeda = input("Digite a moeda (ex: USD, EUR): ").upper()

try:
    response = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda}-BRL")
    dados = response.json()
    chave = f"{moeda}BRL"
    
    if chave in dados:
        cotacao = dados[chave]
        timestamp = int(cotacao['timestamp'])
        data = datetime.fromtimestamp(timestamp)
        
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Máxima: R$ {cotacao['high']}")
        print(f"Mínima: R$ {cotacao['low']}")
        print(f"Última atualização: {data.strftime('%d/%m/%Y %H:%M:%S')}")
    else:
        print("Moeda não encontrada")
        
except:
    print("Erro na requisição")