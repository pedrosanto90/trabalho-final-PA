import mysql.connector
import bcrypt
from main import *
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD= os.getenv("PASSWORD")

def create_user(user_name, user_fullname, user_password, user_role):
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
            insert_query = 'INSERT INTO users (user_name, user_fullname, user_password, user_role) \
                VALUES (%s, %s, %s, %s)'
            
            # TODO: adicionar bcrypt para guardar as passwords
            hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
            record = (user_name, user_fullname, hashed_password, user_role)

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


def delete_user(user_name):
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

            # Consulta SQL para excluir um utilizador
            delete_query = """
            DELETE FROM users
            WHERE user_name = %s
            """
            record = (user_name,)

            # Executar a consulta
            cursor.execute(delete_query, record)
            connection.commit()

            image_path = os.path.join("images/", f"{user_name}.jpg")
            if os.path.isfile(image_path):
                os.remove(image_path)

            print("Utilizador eliminado com sucesso.")

    except Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
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
                    return True
                else:
                    print("Username ou password incorretos")
                    return False
            else:
                print("Utilizador não encontrado.")
                return False
            
    except Error as err:
        print(f'Erro ao conectar a base de dados: {err}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def update_password(user_name, user_password):
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
            UPDATE users
            SET
                user_password = %s
            WHERE
                user_name = %s
            """
            record = (user_password, user_name)

            # Execute the query
            cursor.execute(update_query, record)
            connection.commit()
            print("Utilizador atualizado com sucesso.")
            return cursor.rowcount

    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

def verify_user(user_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute('SELECT user_name FROM users WHERE user_name = %s', (user_name,))
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

def verify_login(user_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            cursor.execute('SELECT user_name FROM users WHERE user_name = %s AND user_role = "Operador"', (user_name,))
            result = cursor.fetchone()

            if result is not None:
                return "Operador"
            else:
                return "Contabilidade"

    except Error as err:
        print(f'Erro ao conectar a base de dados: {err}')

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")