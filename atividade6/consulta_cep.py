import requests

cep = input("Digite o CEP: ").replace("-", "")

try:
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    dados = response.json()
    
    if 'erro' not in dados:
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    else:
        print("CEP não encontrado")
        
except:
    print("Falha na requisição")