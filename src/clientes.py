import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
def create_client(client_id, client_name, client_address, client_nif, client_mobile, client_email, client_created)
    try:
        # Conexão com o banco de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabbalho_final',
            user='root',
            password='admin'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para inserir um novo cliente
            insert_query = """
                INSERT INTO cond_users (user_id, user_fullname, user_address, user_nif, user_mobile, user_email, user_created_at, user_updated_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
                """
            record = (client_id, client_name, client_address, client_nif, client_mobile, client_email, client_created)

            # Executar a consulta
            cursor.execute(insert_query, record)
            connection.commit()
            print("Cliente inserido com sucesso.")

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

    # Exemplo de uso da função
    create_client(1, 'Nome Completo', 'Endereço Exemplo, 123', '123456789', '912345678', 'cliente@example.com',
                  '2024-05-24')
