from socket import *
import threading
import ssl

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

def handleClient(connectionSocket, addr):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper().strip()
        connectionSocket.send(capitalizedSentence.encode())

        print(capitalizedSentence)
        if (capitalizedSentence == 'STOP'):
            print(1)
            connected = False
            connectionSocket.close()

certificatesDirectory = 'C:/certificates/'
privateKeyPath = certificatesDirectory + 'key.pem'
certificatePath = certificatesDirectory + 'certificate.pem'
privateKeyPassword = '1234'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=certificatePath, keyfile=privateKeyPath, password=privateKeyPassword)
secureSocket = context.wrap_socket(serverSocket, server_side=True)

while True:
    connectionSocket, addr = secureSocket.accept()
    client_thread = threading.Thread(target=handleClient, args=(connectionSocket, addr))
    client_thread.start()
