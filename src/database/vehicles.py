import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error

load_dotenv()
PASSWORD= os.getenv("PASSWORD")

def create_vehicle(vehicle_client_id, vehicle_registration, vehicle_brand, vehicle_model, vehicle_registration_date):
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

            # Consulta SQL para inserir um novo veículo
            insert_query = """
            INSERT INTO vehicles (vehicle_client_id, vehicle_registration, vehicle_brand, vehicle_model, vehicle_registration_date)
            VALUES (%s, %s, %s, %s, %s)
            """
            record = (vehicle_client_id, vehicle_registration, vehicle_brand, vehicle_model, vehicle_registration_date)

            # Executar a consulta
            cursor.execute(insert_query, record)
            connection.commit()
            print("Veículo inserido com sucesso.")

    except Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def update_vehicle(vehicle_id, vehicle_client_id, vehicle_registration, vehicle_brand, vehicle_model, vehicle_registration_date):
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

            # Consulta SQL para atualizar um veículo
            update_query = """
            UPDATE vehicles
            SET
                vehicle_client_id = %s,
                vehicle_registration = %s,
                vehicle_brand = %s,
                vehicle_model = %s,
                vehicle_registration_date = %s
            WHERE
                vehicle_id = %s
            """
            record = (vehicle_client_id, vehicle_registration, vehicle_brand, vehicle_model, vehicle_registration_date, vehicle_id)

            # Executar a consulta
            cursor.execute(update_query, record)
            connection.commit()
            print("Veículo atualizado com sucesso.")

    except Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def delete_vehicle(vehicle_id):
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

            # Consulta SQL para excluir um veículo
            delete_query = """
            DELETE FROM vehicles
            WHERE vehicle_id = %s
            """
            record = (vehicle_id,)

            # Executar a consulta
            cursor.execute(delete_query, record)
            connection.commit()
            print("Veículo eliminado com sucesso.")

    except Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")