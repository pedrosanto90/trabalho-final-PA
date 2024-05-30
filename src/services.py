import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
from datetime import datetime

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

def create_service(service_vehicle_id, service_type_id, service_state_id, service_description, \
                   service_start, service_end, service_state, service_price, service_price_material):
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
                insert into services (service_vehicle_id, service_type_id, service_state_id, service_description, \
                service_start, service_end, service_state, service_price, service_price_material, service_created)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            record = (service_vehicle_id, service_type_id, service_state_id, service_description, \
                      service_start, service_end, service_state, service_price, service_price_material, \
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

create_service(1, 1, 1, 'teste', '2022-01-01', '2022-01-01', 1, 1, 1)
