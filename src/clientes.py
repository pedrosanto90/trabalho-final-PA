import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

load_dotenv()
PASSWORD= os.getenv("PASSWORD")

def create_client(client_name, client_address, client_nif, client_mobile, client_email):
    try:
        # Conexão com o banco de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Obter a data e hora atuais
            client_created = datetime.now().strftime('%Y-%m-%d')

            # Consulta SQL para inserir um novo cliente
            insert_query = """
                INSERT INTO clients (client_name, client_address, client_nif, client_mobile, client_email, client_created)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
            record = (client_name, client_address, client_nif, client_mobile, client_email, client_created)

            # Executar a consulta
            cursor.execute(insert_query, record)
            connection.commit()
            print("Cliente inserido com sucesso.")

    except Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

create_client('Nome Completo', 'Endereço Exemplo, 123', '123456789', '912345678', 'cliente@example.com')

