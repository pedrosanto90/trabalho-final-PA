import requests
import sys
import json

# Verifica se o script foi executado com um argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <id>")
    sys.exit(1)

# Verifica se o argumento é uma string
id = sys.argv[1]

# Envia a solicitação GET para o endpoint da API
response = requests.get('http://127.0.0.1:5005/norauto/api/services')

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    
    # Verifica se o ID está presente nos dados
    if id in data:
        # Formata os dados em JSON antes de imprimir
        formatted_data = json.dumps(data[id], indent=4)
        print(formatted_data)
    else:
        print(f'Nenhum item encontrado com o id: {id}')
else:
    print(f'Falha ao obter dados: {response.status_code}')
