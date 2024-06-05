import requests
import sys
import json

# Certifique-se de que o script está sendo executado com o número correto de argumentos
if len(sys.argv) != 2:
    print("Uso: python script.py <id>")
    sys.exit(1)

# Verifique se o argumento é uma string
id = sys.argv[1]

# Envie a solicitação GET para o endpoint da API
response = requests.get('http://127.0.0.1:5005/norauto/api/payments')

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    
    # Verifique se o ID está presente nos dados
    if id in data:
        # Formate os dados em JSON antes de imprimir
        formatted_data = json.dumps(data[id], indent=4)
        print(formatted_data)
    else:
        print(f'Nenhum item encontrado com o id: {id}')
else:
    print(f'Falha ao recuperar os dados: {response.status_code}')
