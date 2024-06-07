# Importação dos módulos e bibliotecas
import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

# Carregamento das variáveis de ambiente
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

# Função para verificar se um cliente com um dado NIF já existe
def existe_cliente(nif):
    connection = mysql.connector.connect(
        host='localhost',
        database='trabalho_final',
        user='root',
        password=PASSWORD
    )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute('SELECT client_nif FROM clients WHERE client_nif=%s', (nif,))
        result = cursor.fetchone()
        print(result)
        if result is not None:
            return True
        else:
            return False

# Função para criar um novo cliente
def create_client(client_name, client_address, client_nif, client_mobile, client_email):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            client_created = datetime.now().strftime('%Y-%m-%d')
            insert_query = """
                INSERT INTO clients (client_name, client_address, client_nif, client_mobile, client_email, client_created)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            record = (client_name, client_address, client_nif, client_mobile, client_email, client_created)
            cursor.execute(insert_query, record)
            connection.commit()
            print("Cliente inserido com sucesso.")
    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para atualizar as informações de um cliente
def update_client(client_address, client_mobile, client_email, client_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            update_query = """
                UPDATE clients
                SET client_address = %s, client_mobile = %s, client_email = %s
                WHERE client_id = %s
            """
            record = (client_address, client_mobile, client_email, client_id)
            cursor.execute(update_query, record)
            connection.commit()
            print("Cliente atualizado com sucesso.")
    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para excluir um cliente
def delete_client(client_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("DELETE FROM services WHERE service_client_id = %s", (client_id,))
            delete_query = "DELETE FROM clients WHERE client_id = %s"
            cursor.execute(delete_query, (client_id,))
            connection.commit()
            print("Cliente excluído com sucesso.")
    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para listar todos os clientes
def list_clients():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            select_query = """SELECT client_id, client_name, client_address, client_nif, client_mobile, client_email, DATE_FORMAT(client_created, "%d/%m/%Y") FROM clients"""
            cursor.execute(select_query)
            clients = cursor.fetchall()
            return clients
    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para verificar se um cliente existe com base no ID
def verify_client(client_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute('SELECT client_id FROM clients WHERE client_id = %s', (client_id,))
            result = cursor.fetchone()
            return result is not None
    except Error as err:
        print(f'Erro ao conectar a base de dados: {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")