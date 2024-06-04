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

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def update_client(client_address, client_mobile, client_email, client_id):
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

            # Consulta SQL para atualizar um cliente
            update_query = """
                UPDATE clients
                SET client_address = %s, client_mobile = %s, client_email = %s
                WHERE client_id = %s
                """
            record = (client_address, client_mobile, client_email, client_id)

            # Executar a consulta
            cursor.execute(update_query, record)
            connection.commit()
            print("Cliente atualizado com sucesso.")
    
    except Error as err:
        print("Erro ao conectar ao MySQL:", err)


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def delete_client(client_id):
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

            # Consulta SQL para deletar um cliente
            delete_query = """
                DELETE FROM clients
                WHERE client_id = %s
                """
            record = (client_id,)

            # Executar a consulta
            cursor.execute(delete_query, record)
            connection.commit()
            print("Cliente excluído com sucesso.")

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")