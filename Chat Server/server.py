import socket, threading   
host = 'localhost'                                                      
port = 8888                                                             
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                             
server.listen()
print(f'Serving HTTP on {host}:{port} ...')

clients = []


def broadcast(message):                                                 
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:                                                           
            message = client.recv(1024)
            print(message)
            broadcast(message)

        except:   
            remove_client(client)
            broadcast('Someone has left the chat'.encode('ascii'))    
            break


def remove_client(client):                                               
    index = clients.index(client)
    clients.remove(client)
    client.close()



def serve():                                                         
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address))) 

        name = f"{address[0]}:{address[1]}"
        clients.append(client)

        broadcast("{} joined!".format(name).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

serve()