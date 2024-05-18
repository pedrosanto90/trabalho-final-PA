import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

def connect():
    try:
        mydb = mysql.connector.connect( 
            host="localhost",
            user="root",
            passwd=PASSWORD,
            database="trabalho_final"
        )
        print('Database connected!')
    except:
        create_db()
        

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

    # create tables
    mycursor.execute('CREATE TABLE clients (client_id INT AUTO_INCREMENT PRIMARY KEY, \
    client_name VARCHAR(255), client_address VARCHAR(255), client_nif INT(9), \
    client_phone INT(9), client_email VARCHAR(50), client_registration_date DATE)')

    mycursor.execute('CREATE TABLE vehicles (vehicle_id INT AUTO_INCREMENT PRIMARY KEY, \
    vehicle_client_id INT, vehicle_registration VARCHAR(8), vehicle_brand VARCHAR(50), \
    vehicle_model VARCHAR(50), FOREIGN KEY(vehicle_client_id) REFERENCES clients(client_id))')

    mycursor.execute('CREATE TABLE service_types (service_type_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_type_description VARCHAR(50))')

    mycursor.execute('CREATE TABLE states ( state_id INT AUTO_INCREMENT PRIMARY KEY, \
    state_description VARCHAR(50))')

    mycursor.execute('CREATE TABLE services (services_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_client_id INT, \
    services_vehicle_id INT, service_type INT, service_description VARCHAR(1024), \
    service_start_date DATE, service_end_date DATE, service_state INT, service_price INT, \
    FOREIGN KEY(services_vehicle_id) REFERENCES vehicles(vehicle_id), \
    FOREIGN KEY(service_type) REFERENCES service_types(service_type_id), \
    FOREIGN KEY(service_client_id) REFERENCES clients(client_id), \
    FOREIGN KEY(service_state) REFERENCES states(state_id))')

    mycursor.execute('CREATE TABLE payment_states (payment_state_id INT AUTO_INCREMENT PRIMARY KEY, \
    payment_state_description VARCHAR(50))')

    mycursor.execute('CREATE TABLE payments (payment_id INT AUTO_INCREMENT PRIMARY KEY, \
    payment_service_id INT, payment_date DATE, payment_value INT, payment_state INT, \
    FOREIGN KEY(payment_service_id) REFERENCES services(services_id), \
    FOREIGN KEY(payment_state) REFERENCES payment_states(payment_state_id))')

    # TODO - rever tabela
    mycursor.execute('CREATE TABLE insurances (insurance_id INT AUTO_INCREMENT PRIMARY KEY, \
    insurance_description VARCHAR(50))')

    mycursor.execute('CREATE TABLE reports (report_id INT AUTO_INCREMENT PRIMARY KEY, \
    service_id INT, insurance_id INT, report_date DATE, refund_value INT, \
    FOREIGN KEY(service_id) REFERENCES services(services_id), \
    FOREIGN KEY(insurance_id) REFERENCES insurances(insurance_id))')
    

def main():
    connect()
    create_tables()
