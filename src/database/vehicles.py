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
