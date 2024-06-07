# Importação dos módulos e bibliotecas
import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime


# Carregamento das variáveis de ambiente
load_dotenv()
PASSWORD = os.getenv("PASSWORD")


# Função para criar um novo serviço
def create_service(service_client_id, service_type, service_description, service_price):
    try:
        # Estabelecer conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query para inserir um novo serviço na tabela services
            insert_query = """
                INSERT INTO services (service_client_id, service_type, service_description,
                service_start_date, service_state)
                VALUES (%s, %s, %s, %s, %s)
            """
            # Valores a serem inseridos na tabela services
            record = (service_client_id, service_type, service_description,
                      datetime.now().strftime('%Y-%m-%d'), "Começado")

            # Query para inserir um pagamento associado ao serviço na tabela payments
            insert_query_2 = """
                INSERT INTO payments (payment_service_id, payment_value, payment_state)
                VALUES ((SELECT service_id FROM services ORDER BY service_id DESC LIMIT 1), %s, %s)
            """
            # Valores a serem inseridos na tabela payments
            record_2 = (service_price, "Por pagar")

            # Executar as queries com os valores fornecidos
            cursor.execute(insert_query, record)
            cursor.execute(insert_query_2, record_2)
            connection.commit()
            print("Serviço inserido com sucesso.")

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para atualizar um serviço existente
def update_service(service_id):
    try:
        # Estabelecer conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query para atualizar um serviço específico
            update_query = """
                UPDATE services
                SET service_end_date = %s,
                    service_state = %s
                WHERE service_id = %s
            """
            # Valores a serem atualizados
            record = (datetime.now().strftime('%Y-%m-%d'), "Terminado", service_id)

            # Executar a query com os valores fornecidos
            cursor.execute(update_query, record)
            connection.commit()
            print("Serviço atualizado com sucesso.")
            return cursor.rowcount  # Retornar o número de linhas afetadas

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return 0

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para eliminar um serviço
def delete_service(service_id):
    try:
        # Estabelecer conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Query para eliminar um serviço específico
            delete_query = """
                DELETE FROM services
                WHERE service_id = %s
            """
            # Valor do ID do serviço a ser eliminado
            record = (service_id,)

            # Executar a query com o valor fornecido
            cursor.execute(delete_query, record)
            connection.commit()
            print("Serviço excluído com sucesso.")
            return cursor.rowcount  # Retornar o número de linhas afetadas

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return 0

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para listar todos os serviços
def list_services():
    try:
        # Estabelecer conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Query para selecionar todos os serviços
            query = """
            SELECT service_id, service_client_id, service_type, service_description, 
                   DATE_FORMAT(service_start_date, "%d/%m/%Y"), 
                   DATE_FORMAT(service_end_date, "%d/%m/%Y"), service_state 
            FROM services
            """
            # Executar a query
            cursor.execute(query)
            # Obter todas as linhas do resultado da consulta
            services = cursor.fetchall()
            return services  # Retornar a lista de serviços

    except mysql.connector.Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return []

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para listar serviços por data de início
def list_services_by_date(date):
    try:
        # Estabelecer conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Query para selecionar serviços com base na data de início
            query = """
            SELECT service_id, service_client_id, service_type, service_description, 
                   DATE_FORMAT(service_start_date, "%d/%m/%Y"), 
                   DATE_FORMAT(service_end_date, "%d/%m/%Y"), service_state 
            FROM services
            WHERE DATE(service_start_date) = %s
            """
            # Executar a query com a data fornecida
            cursor.execute(query, (date,))
            # Obter todas as linhas do resultado da consulta
            services = cursor.fetchall()
            return services  # Retornar a lista de serviços filtrados pela data

    except mysql.connector.Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return []

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

