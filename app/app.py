import socket
import random
import string
import json
from flask import Flask, request
import mysql.connector

class DBManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user='root',
            password='root',
            host='db',
            database='thesis',
        )
        self.cursor = self.connection.cursor()
        
    def insert_ip_addr(self, ip_addr, random_str):
        self.cursor.execute("INSERT INTO client_access (ip_address, random_str) VALUES ('{}', '{}');".format(ip_addr, random_str))
        self.connection.commit()
    

def eratosthenes(n):
    all = []
    prime = 1
    i = 3
    while (i <= n):
        if  i not in all:
            prime += 1
            j = i
            while (j <= (n / i)):
                all.append(i * j)
                j += 1
        i += 2

app = Flask(__name__)
conn = None

@app.route('/')
def home():
    hostname=socket.gethostname()
    server_ipaddr=socket.gethostbyname(hostname)
    ip_addr = request.remote_addr
    random_str = "".join((random.choice(string.ascii_uppercase) for x in range(90)))
    
    global conn
    if not conn:
        conn = DBManager()
    
    conn.insert_ip_addr(ip_addr, random_str)
    
    eratosthenes(100)

    data = {
        "client_ipaddr": ip_addr,
        "random_str": random_str,
        "served_by": hostname,
        "server_ipaddr": server_ipaddr
    }

    response = app.response_class(
        response = json.dumps(data),
        status = 200,
        mimetype = 'application/json'
    )
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')