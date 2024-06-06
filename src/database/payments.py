import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

# Load environment variables
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

def create_payment(payment_date, payment_value, payment_state, payment_type):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to insert a new payment
            insert_query = """
            INSERT INTO payments (payment_date, payment_value, payment_state, payment_type)
            VALUES (%s, %s, %s, %s)
            """
            record = (payment_date, payment_value, payment_state, payment_type)

            # Execute the query
            cursor.execute(insert_query, record)
            connection.commit()
            print("Pagamento inserido com sucesso.")
            return cursor.rowcount

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def update_payment(payment_service_id, payment_type):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to update a payment
            update_query = """
            UPDATE payments
            SET
                payment_date = %s,
                payment_state = %s,
                payment_type = %s
            WHERE
                payment_service_id = %s
            """
            record = (datetime.now().strftime('%Y-%m-%d'), "Pago", payment_type, payment_service_id)

            # Execute the query
            cursor.execute(update_query, record)
            connection.commit()
            print("Pagamento atualizado com sucesso.")
            return cursor.rowcount

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def delete_payment(payment_id):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to delete a payment
            delete_query = """
            DELETE FROM payments
            WHERE payment_id = %s
            """
            record = (payment_id,)

            # Execute the query
            cursor.execute(delete_query, record)
            connection.commit()
            print("Pagamento eliminado com sucesso.")
            return cursor.rowcount

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def list_payments():
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to select all payments
            select_query = """SELECT payment_service_id, DATE_FORMAT(payment_date, "%d/%m/%Y"), payment_value, payment_state, payment_type FROM payments"""

            # Execute the query
            cursor.execute(select_query)

            # Fetch all rows
            payments = cursor.fetchall()

            return payments

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def verify_payment(payment_service_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute('SELECT payment_service_id FROM payments WHERE payment_service_id = %s', (payment_service_id,))
            result = cursor.fetchone()

            if result is not None:
                return True
            else:
                return False

    except Error as err:
        print(f'Erro ao conectar a base de dados: {err}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")
