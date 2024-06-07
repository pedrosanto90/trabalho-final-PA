# Importação dos módulos e bibliotecas
import mysql.connector
from dotenv import load_dotenv
import os

# Carregamento das variáveis de ambiente
load_dotenv()
PASSWORD = os.getenv('PASSWORD')


# Função para conectar à base de dados
def connect():
    mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=PASSWORD,
        database="trabalho_final"
    )
    print('Base de dados conectada!')  # Imprime uma mensagem de sucesso


# Função para criar a base de dados
def create_db():
    # Conecta ao servidor MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=PASSWORD,
    )

    mycursor = mydb.cursor()  # Cria um cursor para executar comandos SQL
    mycursor.execute('CREATE DATABASE trabalho_final')  # Cria a base de dados "trabalho_final"

    print('Base de dados criada!')  # Imprime uma mensagem de sucesso


# Função para criar as tabelas na base de dados
def create_tables():
    # Conecta à base de dados "trabalho_final"
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=PASSWORD,
        database="trabalho_final"
    )

    mycursor = mydb.cursor()  # Cria um cursor para executar comandos SQL

    # Criação da tabela "clients"
    mycursor.execute('CREATE TABLE clients (client_id INT AUTO_INCREMENT PRIMARY KEY, \
    client_name VARCHAR(256), \
    client_address VARCHAR(256), \
    client_nif VARCHAR(9), \
    client_mobile VARCHAR(9), \
    client_email VARCHAR(50), \
    client_created DATE)')

    # Criação da tabela "services"
    mycursor.execute('CREATE TABLE services (service_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_client_id INT, \
    service_type VARCHAR(50), \
    service_description VARCHAR(1024), \
    service_start_date DATE, \
    service_end_date DATE, \
    service_state VARCHAR(50), \
    FOREIGN KEY(service_client_id) REFERENCES clients(client_id))')

    # Criação da tabela "payments"
    mycursor.execute('CREATE TABLE payments (payment_id INT AUTO_INCREMENT PRIMARY KEY, \
    payment_service_id INT, \
    payment_date DATE, \
    payment_value FLOAT, \
    payment_state VARCHAR(50), \
    payment_type VARCHAR(50), \
    FOREIGN KEY(payment_service_id) REFERENCES services(service_id))')

    # Criação da tabela "users"
    mycursor.execute('CREATE TABLE users (user_id INT AUTO_INCREMENT PRIMARY KEY, \
    user_name VARCHAR(50), \
    user_fullname VARCHAR(256), \
    user_password VARCHAR(64), \
    user_role VARCHAR(50))')

    print('Tabelas criadas!')  # Imprime uma mensagem de sucesso
