import mysql.connector
from dotenv import load_dotenv
import os
from mysql.connector import Error
import bcrypt

load_dotenv()
PASSWORD= os.getenv("PASSWORD")

def create_user(user_name, user_fullname, user_password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para inserir um novo cliente
            insert_query = 'INSERT INTO users (user_name, user_fullname, user_password) \
                VALUES (%s, %s, %s)'
            
            # TODO: adicionar bcrypt para guardar as passwords
            hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
            record = (user_name, user_fullname, hashed_password)

            cursor.execute(insert_query, record)
            connection.commit()
            print("Utilizador inserido com sucesso.")
    except Error as err:
        print(f'Erro ao criar o utilizador: {err}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

create_user('pedroesanto', 'Pedro Espirito Santo', 'Pedro915624607')
