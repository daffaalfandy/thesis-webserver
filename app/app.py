import socket
import random
import string
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
    
    response = '<h1> Client with IP Address: {} </h1>'.format(ip_addr)
    response += '</br> <h1> Have a random string: {} </h1>'.format(random_str)
    response += '</br> <strong> <h2> Served by Server {} with IP Addreess: {} </h2> </strong>'.format(hostname, server_ipaddr)
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')