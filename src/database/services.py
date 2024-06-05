import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

def create_service(service_client_id, service_type, service_description,
                   service_start_date, service_end_date, service_state, service_price):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            service_created = datetime.now().strftime('%Y-%m-%d')

            insert_query = """
                INSERT INTO services (service_client_id, service_type, service_description,
                service_start_date, service_end_date, service_state, service_price, service_created)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            record = (service_client_id, service_type, service_description,
                      service_start_date, service_end_date, service_state, service_price, service_created)

            cursor.execute(insert_query, record)
            connection.commit()
            print("Serviço inserido com sucesso.")

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def update_service(service_id, service_type, service_description, service_start_date, service_end_date, service_state, service_price):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            service_updated = datetime.now().strftime('%Y-%m-%d')

            update_query = """
                UPDATE services
                SET service_type = %s,
                    service_description = %s,
                    service_start_date = %s,
                    service_end_date = %s,
                    service_state = %s,
                    service_price = %s,
                    service_updated = %s
                WHERE service_id = %s
            """
            record = (service_type, service_description,
                      service_start_date, service_end_date, service_state, service_price, service_updated, service_id)

            cursor.execute(update_query, record)
            connection.commit()
            print("Serviço atualizado com sucesso.")
            return cursor.rowcount  # Return the number of affected rows

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return 0

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

            delete_query = """
                DELETE FROM services
                WHERE service_id = %s
            """
            record = (service_id,)

            cursor.execute(delete_query, record)
            connection.commit()
            print("Serviço excluído com sucesso.")
            return cursor.rowcount  # Return the number of affected rows

    except Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return 0

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def get_services_by_date(date):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = """
            SELECT * FROM services
            WHERE DATE(service_start_date) = %s
            """
            cursor.execute(query, (date,))
            services = cursor.fetchall()
            return services

    except mysql.connector.Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def get_service_by_id(service_id):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM services WHERE service_id = %s"
            cursor.execute(query, (service_id,))
            service = cursor.fetchone()
            return service

    except mysql.connector.Error as err:
        print("Erro ao conectar ao MySQL:", err)
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")