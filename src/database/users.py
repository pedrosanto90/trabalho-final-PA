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


def login(user_name, user_password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute('SELECT user_password FROM users WHERE user_name = %s', (user_name,))
            result = cursor.fetchone()

            if result is not None:
                stored_password = result[0]
                if bcrypt.checkpw(user_password.encode('utf-8'), stored_password.encode('utf-8')):
                    print("Login bem-sucedido.")
                    return "Login bem-sucedido."
                else:
                    print("Username ou password incorretos")
                    return "Username ou password incorretos"
            else:
                print("Utilizador não encontrado.")
                return "Utilizador não encontrado."
            
    except Error as err:
        print(f'Erro ao criar o utilizador: {err}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

