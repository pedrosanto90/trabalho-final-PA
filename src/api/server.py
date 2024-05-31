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
            return jsonify(clients)
        
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("conexão ao mysql encerrada.")
    
    return jsonify({"error": "Unable to fetch clients"}), 500

@app.route("/norauto/api/vehicles")
def vehicles():
    try:
        # Conexão com o banco de dados
        connection = connect_db()

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM vehicles")
            vehicles = cursor.fetchall()
            return jsonify(vehicles)
        
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("conexão ao mysql encerrada.")
    
    return jsonify({"error": "Unable to fetch vehicles"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)