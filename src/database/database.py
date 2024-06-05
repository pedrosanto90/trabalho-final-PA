import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

def connect():
    mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd=PASSWORD,
        database="trabalho_final"
    )
    print('Database connected!')

def create_db():
        mydb = mysql.connector.connect( 
            host="localhost",
            user="root",
            passwd=PASSWORD,
        )

        mycursor = mydb.cursor()
        mycursor.execute('CREATE DATABASE trabalho_final')

        print('Database created!')

def create_tables():
    mydb = mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd=PASSWORD,
        database="trabalho_final"
    )

    mycursor = mydb.cursor()

    # creating tables

    mycursor.execute('CREATE TABLE clients (client_id INT AUTO_INCREMENT PRIMARY KEY, \
    client_name VARCHAR(256), \
    client_address VARCHAR(256), \
    client_nif INT(9), \
    client_mobile VARCHAR(15), \
    client_email VARCHAR(50), \
    client_created DATE)')

    mycursor.execute('CREATE TABLE services (services_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_client_id INT, \
    service_description VARCHAR(1024), \
    service_start_date DATE, \
    service_end_date DATE, \
    service_state INT, \
    service_price INT, \
    FOREIGN KEY(service_client_id) REFERENCES clients(client_id))')

    mycursor.execute('CREATE TABLE payments (payment_id INT AUTO_INCREMENT PRIMARY KEY, \
    payment_service_id INT, \
    payment_date DATE, \
    payment_value FLOAT, \
    payment_state VARCHAR(50), \
    payment_type VARCHAR(50))')

    mycursor.execute('CREATE TABLE users (user_id INT AUTO_INCREMENT PRIMARY KEY, \
    user_name VARCHAR(50), \
    user_fullname VARCHAR(256), \
    user_password VARCHAR(64), \
    user_role VARCHAR(50))')
