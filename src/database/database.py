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

    mycursor.execute('CREATE TABLE vehicles (vehicle_id INT AUTO_INCREMENT PRIMARY KEY, \
    vehicle_client_id INT NOT NULL, \
    vehicle_registration VARCHAR(6), \
    vehicle_brand VARCHAR(50), \
    vehicle_model VARCHAR(50), \
    vehicle_registration_date DATE)')

    mycursor.execute('CREATE TABLE service_types (service_type_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_type_description VARCHAR(50))')

    mycursor.execute('CREATE TABLE states ( state_id INT AUTO_INCREMENT PRIMARY KEY, \
    state_description VARCHAR(50))')

    mycursor.execute('CREATE TABLE services (services_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_client_id INT, \
    services_vehicle_id INT, service_type INT, \
    service_description VARCHAR(1024), \
    service_start_date DATE, \
    service_end_date DATE, \
    service_state INT, \
    service_price INT, \
    FOREIGN KEY(services_vehicle_id) REFERENCES vehicles(vehicle_id), \
    FOREIGN KEY(service_type) REFERENCES service_types(service_type_id), \
    FOREIGN KEY(service_client_id) REFERENCES clients(client_id), \
    FOREIGN KEY(service_state) REFERENCES states(state_id))')

    mycursor.execute('CREATE TABLE payments (payment_id INT AUTO_INCREMENT PRIMARY KEY, \
    payment_service_id INT, payment_date DATE, payment_value INT, payment_state VARCHAR(50), \
    payment_type VARCHAR(50)')

    mycursor.execute('CREATE TABLE reports (report_id INT AUTO_INCREMENT PRIMARY KEY, \
    report_service_id INT NOT NULL, \
    report_insurance_id INT NOT NULL, \
    report_date date, \
    report_refund_value FLOAT)')

    # TODO - rever tabela
    mycursor.execute('CREATE TABLE insurances (insurance_id INT AUTO_INCREMENT PRIMARY KEY, \
    insurance_name VARCHAR(50), \
    insurance_phone VARCHAR(15), \
    insurance_email VARCHAR(50), \
    insurance_address VARCHAR(256), \
    insurance_client_id INT NOT NULL, \
    insurance_vehicle_id INT NOT NULL, \
    insurance_service_id INT NOT NULL, \
    insurance_report_id INT NOT NULL, \
    FOREIGN KEY(insurance_client_id) REFERENCES clients(client_id), \
    FOREIGN KEY(insurance_vehicle_id) REFERENCES vehicles(vehicle_id), \
    FOREIGN KEY(insurance_service_id) REFERENCES services(services_id), \
    FOREIGN KEY(insurance_report_id) REFERENCES reports(report_id))')


    mycursor.execute('CREATE TABLE users (user_id INT AUTO_INCREMENT PRIMARY KEY, \
    user_name VARCHAR(50), \
    user_fullname VARCHAR(256), \
    user_image VARCHAR(256), \
    user_password VARCHAR(64), \
    user_role VARCHAR(50))')
