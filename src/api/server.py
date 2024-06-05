from flask import Flask, jsonify
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()
PASSWORD = os.getenv("PASSWORD")

if not PASSWORD:
    raise ValueError("No PASSWORD environment variable set")

app = Flask(__name__)

def connect_db():
    connection = mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd=PASSWORD,
        database="trabalho_final"
    )
    print('Database connected!')
    return connection

@app.route("/")
def home():
    routes ={
        "clients": "/norauto/api/clients",
        "payments": "/norauto/api/payments",
        "services": "/norauto/api/services"
    }
    return jsonify(routes)

@app.route("/norauto/api/clients")
def get_clients():
    try:
        # Conexão com o banco de dados
        connection = connect_db()

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # TODO: alterar query para mostrar nome do cliente em vez do ID
            #       nao mostrar ID do vehiculo
        
            cursor.execute("SELECT * FROM clients")
            clients = cursor.fetchall()

            clients_dict = {client['client_id']: {
                "client_address": client['client_address'],
                "client_created": client['client_created'],
                "client_email": client['client_email'],
                "client_mobile": client['client_mobile'],
                "client_name": client['client_name'],
                "client_nif": client['client_nif']
            } for client in clients}
            return jsonify(clients_dict)
        
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("conexão ao mysql encerrada.")
    
    return jsonify({"error": "Unable to fetch clients"}), 500

@app.route("/norauto/api/payments")
def payments():
    try:
        # Conexão com o banco de dados
        connection = connect_db()

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM payments")
            payments = cursor.fetchall()
            payments_dict = {payment['payment_id']: {
                "payment_date": payment['payment_date'],
                "payment_value": payment['payment_value'],
                "payment_state": payment['payment_state'],
                "payment_type": payment['payment_type']
            } for payment in payments}
            return jsonify(payments_dict)
        
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("conexão ao mysql encerrada.")
    
    return jsonify({"error": "Unable to fetch payments"}), 500


@app.route("/norauto/api/services")
def services():
    try:
        # Conexão com o banco de dados
        connection = connect_db()

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            cursor.execute("SELECT * FROM services")
            services = cursor.fetchall()
    # mycursor.execute('CREATE TABLE services (service_id INT AUTO_INCREMENT PRIMARY KEY, \
    # service_client_id INT, \
    # service_type VARCHAR(50), \
    # service_description VARCHAR(1024), \
    # service_start_date DATE, \
    # service_end_date DATE, \
    # service_state INT, \
    # service_price INT, \
    # service_created DATE, \
    # service_updated DATE, \
    # FOREIGN KEY(service_client_id) REFERENCES clients(client_id))')
            services_dict = {service['service_id']: {
                "service_client_id": service['service_client_id'],
                "service_created": service['service_created'],
                "service_description": service['service_description'],
                "service_end_date": service['service_end_date'],
                "service_price": service['service_price'],
                "service_start_date": service['service_start_date'],
                "service_state": service['service_state'],
                "service_type": service['service_type'],
                "service_updated": service['service_updated']
            } for service in services}
            return jsonify(services_dict)
        
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("conexão ao mysql encerrada.")
    
    return jsonify({"error": "Unable to fetch services"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
