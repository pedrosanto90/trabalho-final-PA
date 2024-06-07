import mysql.connector
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import random

load_dotenv()

PASSWORD = os.getenv('PASSWORD')

def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=PASSWORD,
        database="trabalho_final"
    )
    print('Database connected!')
    return mydb

# gera uma data aleatoria
def generate_random_date(start, end):
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime('%Y-%m-%d')

def insert_data():
    mydb = connect()
    mycursor = mydb.cursor()

    start_date = datetime.strptime('2023-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2023-12-31', '%Y-%m-%d')

    # Gera dados para os clientes
    clients = [
        (f"Client {i}", f"{i} Main St", random.randint(100000000, 999999999), f"555-12{i:02d}", f"client{i}@example.com", generate_random_date(start_date, end_date))
        for i in range(1, 11)
    ]

    client_sql = "INSERT INTO clients (client_name, client_address, client_nif, client_mobile, client_email, client_created) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.executemany(client_sql, clients)
    mydb.commit()

    # Gera dados para os servicos
    services = [
        (random.randint(1, 10), f"Service Type {i}", f"Service description {i}", generate_random_date(start_date, end_date), generate_random_date(start_date, end_date), random.randint(0, 2), random.randint(100, 10000), generate_random_date(start_date, end_date), generate_random_date(start_date, end_date))
        for i in range(1, 11)
    ]

    # service_sql = "INSERT INTO services (service_client_id, service_type, service_description, service_start_date, service_end_date, service_state, service_price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # mycursor.executemany(service_sql, services)
    # mydb.commit()

    # Generate data for payments
    payments = [
        (random.randint(1, 10), generate_random_date(start_date, end_date), random.uniform(100.0, 10000.0), random.choice(["Completed", "Pending", "Failed"]), random.choice(["Credit Card", "Bank Transfer", "Cash"]))
        for i in range(1, 11)
    ]

    payment_sql = "INSERT INTO payments (payment_service_id, payment_date, payment_value, payment_state, payment_type) VALUES (%s, %s, %s, %s, %s)"
    mycursor.executemany(payment_sql, payments)
    mydb.commit()

    # Generate data for users
    users = [
        (f"user{i}", f"User Fullname {i}", f"password{i}", random.choice(["admin", "user"]))
        for i in range(1, 11)
    ]

    user_sql = "INSERT INTO users (user_name, user_fullname, user_password, user_role) VALUES (%s, %s, %s, %s)"
    mycursor.executemany(user_sql, users)
    mydb.commit()

    print('Data inserted!')

insert_data()
