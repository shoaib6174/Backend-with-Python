import socket, threading
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
client.connect(('localhost', 8888))                             

def receive():
    while True:                                                 
        try:
            message = client.recv(1024).decode('ascii')
            
            print(message)
        except:                                                
            print("An error occured!")
            client.close()
            break
def write():
    global nickname
    while True:                                                
        message = '{}: {}'.format(nickname, input(': '))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()