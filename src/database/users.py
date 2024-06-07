# Importação dos módulos e bibliotecas
import mysql.connector
import bcrypt
from main import *
from dotenv import load_dotenv
import os

# Carregamento das variáveis de ambiente
load_dotenv()
PASSWORD = os.getenv("PASSWORD")

# Função para criar um novo utilizador
def create_user(user_name, user_fullname, user_password, user_role):
    try:
        # Conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para inserir um novo utilizador
            insert_query = 'INSERT INTO users (user_name, user_fullname, user_password, user_role) \
                VALUES (%s, %s, %s, %s)'

            # Hash da password utilizando bcrypt
            hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
            record = (user_name, user_fullname, hashed_password.decode('utf-8'), user_role)

            cursor.execute(insert_query, record)
            connection.commit()
            print("Utilizador inserido com sucesso.")
    except mysql.connector.Error as err:
        print(f'Erro ao criar o utilizador: {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para remover um utilizador
def delete_user(user_name):
    try:
        # Conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para excluir um utilizador
            delete_query = 'DELETE FROM users WHERE user_name = %s'
            record = (user_name,)

            # Executar a consulta
            cursor.execute(delete_query, record)
            connection.commit()

            # Remover a imagem do utilizador se existir
            image_path = os.path.join("images/", f"{user_name}.jpg")
            if os.path.isfile(image_path):
                os.remove(image_path)

            print("Utilizador eliminado com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para atualizar a password de um utilizador
def update_password(user_name, user_password):
    try:
        # Conexão com a base de dados
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Hash da nova password utilizando bcrypt
            hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
            update_query = 'UPDATE users SET user_password = %s WHERE user_name = %s'
            record = (hashed_password.decode('utf-8'), user_name)

            # Executar a consulta
            cursor.execute(update_query, record)
            connection.commit()
            print("Utilizador atualizado com sucesso.")
            return cursor.rowcount
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para verificar a existência de um utilizador
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

            # Consulta SQL para verificar a existência de um utilizador
            cursor.execute('SELECT user_name FROM users WHERE user_name = %s', (user_name,))
            result = cursor.fetchone()

            return result is not None
    except mysql.connector.Error as err:
        print(f'Erro ao conectar à base de dados: {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para verificar o login de um utilizador
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

            # Consulta SQL para obter a password do utilizador
            cursor.execute('SELECT user_password FROM users WHERE user_name = %s', (user_name,))
            result = cursor.fetchone()

            if result is not None:
                stored_password = result[0]
                # Verificação da password com bcrypt
                if bcrypt.checkpw(user_password.encode('utf-8'), stored_password.encode('utf-8')):
                    print("Login bem-sucedido.")
                    return True
                else:
                    print("Username ou password incorretos")
                    return False
            else:
                print("Utilizador não encontrado.")
                return False
    except mysql.connector.Error as err:
        print(f'Erro ao conectar à base de dados: {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")

# Função para verificar o cargo de um utilizador (Operador ou Contabilidade)
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

            # Consulta SQL para verificar o cargo do utilizador
            cursor.execute('SELECT user_name FROM users WHERE user_name = %s AND user_role = "Operador"', (user_name,))
            result = cursor.fetchone()

            return "Operador" if result is not None else "Contabilidade"
    except mysql.connector.Error as err:
        print(f'Erro ao conectar à base de dados: {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")


# Função para obter o nome completo de um utilizador
def login_fullname(user_name):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='trabalho_final',
            user='root',
            password=PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para obter o nome completo do utilizador
            cursor.execute('SELECT user_fullname FROM users WHERE user_name = %s', (user_name,))
            result = cursor.fetchone()

            return result[0] if result else None
    except mysql.connector.Error as err:
        print(f'Erro ao conectar à base de dados: {err}')
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão ao MySQL encerrada.")