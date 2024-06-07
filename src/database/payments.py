# Importação dos módulos e bibliotecas
import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

# Carregamento das variáveis de ambiente
load_dotenv()
PASSWORD = os.getenv("PASSWORD")


# Função para criar um novo pagamento
def create_payment(payment_date, payment_value, payment_state, payment_type):
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

            # Query para inserir um novo pagamento na tabela payments
            insert_query = """
            INSERT INTO payments (payment_date, payment_value, payment_state, payment_type)
            VALUES (%s, %s, %s, %s)
            """
            # Valores a serem inseridos
            record = (payment_date, payment_value, payment_state, payment_type)

            # Executar a query com os valores fornecidos
            cursor.execute(insert_query, record)
            connection.commit()
            print("Pagamento inserido com sucesso.")
            return cursor.rowcount  # Retornar o número de linhas afetadas

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para atualizar um pagamento existente
def update_payment(payment_service_id, payment_type):
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

            # Query para atualizar um pagamento específico
            update_query = """
            UPDATE payments
            SET
                payment_date = %s,
                payment_state = %s,
                payment_type = %s
            WHERE
                payment_service_id = %s
            """
            # Valores a serem atualizados
            record = (datetime.now().strftime('%Y-%m-%d'), "Pago", payment_type, payment_service_id)

            # Executar a query com os valores fornecidos
            cursor.execute(update_query, record)
            connection.commit()
            print("Pagamento atualizado com sucesso.")
            return cursor.rowcount  # Retornar o número de linhas afetadas

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para eliminar um pagamento
def delete_payment(payment_id):
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

            # Query para eliminar um pagamento específico
            delete_query = """
            DELETE FROM payments
            WHERE payment_id = %s
            """
            # Valor do ID do pagamento a ser eliminado
            record = (payment_id,)

            # Executar a query com o valor fornecido
            cursor.execute(delete_query, record)
            connection.commit()
            print("Pagamento eliminado com sucesso.")
            return cursor.rowcount  # Retornar o número de linhas afetadas

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para listar todos os pagamentos
def list_payments():
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

            # Query para selecionar todos os pagamentos
            select_query = """SELECT payment_service_id, DATE_FORMAT(payment_date, "%d/%m/%Y"), payment_value, 
                            payment_state, payment_type FROM payments"""

            # Executar a query
            cursor.execute(select_query)

            # Obter todas as linhas do resultado da consulta
            payments = cursor.fetchall()

            return payments  # Retornar a lista de pagamentos

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para verificar se um pagamento existe
def verify_payment(payment_service_id):
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

            # Query para verificar se um pagamento existe
            cursor.execute('SELECT payment_service_id FROM payments WHERE payment_service_id = %s',
                           (payment_service_id,))
            result = cursor.fetchone()

            if result is not None:
                return True  # Retornar True se o pagamento existir
            else:
                return False  # Retornar False se o pagamento não existir

    except Error as err:
        print(f'Erro ao conectar a base de dados: {err}')

    finally:
        # Fechar o cursor e a conexão
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")
