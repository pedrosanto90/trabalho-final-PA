import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

def create_service(service_type_id, service_description,
                   service_start, service_end, service_state, service_price):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # obter a data e hora atuais
            service_created = datetime.now().strftime('%y-%m-%d')

            # consulta sql para inserir um novo cliente
            insert_query = """
                insert into services (service_type_id, service_description, \
                service_start, service_end, service_state, service_price, service_created)
                values (%s, %s, %s, %s, %s, %s, %s)
                """
            record = (service_type_id, service_description, \
                      service_start, service_end, service_state, service_price,\
                      service_created)

            # executar a consulta
            cursor.execute(insert_query, record)
            connection.commit()
            print("serviço inserido com sucesso.")

    except Error as err:
        print("erro ao conectar ao mysql:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("conexão ao mysql encerrada.")

def update_service(service_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Obter a data e hora atuais para atualização
            service_updated = datetime.now().strftime('%Y-%m-%d')

            # Consulta SQL para atualizar um serviço
            update_query = """
                UPDATE services
                SET service_type_id = %s,
                    service_description = %s,
                    service_start = %s,
                    service_end = %s,
                    service_state = %s,
                    service_price = %s,
                    service_updated = %s
                WHERE service_id = %s
                """
            record = (service_type_id, service_description, \
                      service_start, service_end, service_state, service_price, service_id)

            # Executar a consulta
            cursor.execute(update_query, record)
            connection.commit()
            print("Serviço atualizado com sucesso.")

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def delete_service(service_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para excluir um serviço
            delete_query = """
                DELETE FROM services
                WHERE service_id = %s
                """
            record = (service_id,)

            # Executar a consulta
            cursor.execute(delete_query, record)
            connection.commit()
            print("Serviço excluído com sucesso.")

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")