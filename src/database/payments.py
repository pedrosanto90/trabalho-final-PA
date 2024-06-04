import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error

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

def update_payment(payment_id, payment_date, payment_value, payment_state, payment_type):
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
                payment_value = %s,
                payment_state = %s,
                payment_type = %s
            WHERE
                payment_id = %s
            """
            record = (payment_date, payment_value, payment_state, payment_type, payment_id)

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
