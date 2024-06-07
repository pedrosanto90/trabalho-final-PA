# Trabalho Final - Programação Avançada

## Desenvolvido por:
<p>Pedro Espirito Santo</p>
<p>João Pinheiro Ferreira</p>
<p>João Bagueixo Ferreira</p>
<p>Rodrigo Lucindo</p>

<br>
<h3>Versao do python: 3.12.2</h3>
<br>

## Executar o projeto:
Criar o ficheiro *.env* na raiz do projecto e colocar as seguintes variaveis de ambiente:

```bash
PASSWORD=<password>
```
Necessario criar diretorio *images* na raiz do projecto.

Ao rodar o ficheiro app.py pela primeira vez, a base de dados e gerada automaticamente e o utilizador *admin* 
e criado com a passoword *admin*.

A base de dados vem vazia, para entroduzir os dados basta executar o ficheiro *insert_test_data.py*
apos iniciar o programa a primeira vez (*app.py*)

<br>

## Executar a API:

python src/api/server.py
main endpont: http://127.0.0.1:5005/

