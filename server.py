import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ''
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))

    print("Connection Closed")
    conn.close()

    while True:
        conn, addr = s.accept()
        print("Connected to: ", addr)

        start_new_thread(threaded_client, (conn,))