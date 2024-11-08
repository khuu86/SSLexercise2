from socket import *
import ssl

serverName = 'localhost'
serverPort = 12000

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
clientSocket = socket(AF_INET, SOCK_STREAM)
secureSocket = context.wrap_socket(clientSocket)
secureSocket.connect((serverName, serverPort))
connected = True
while connected:
    sentence = input('Input lowercase sentence:')
    secureSocket.send(sentence.encode())
    modifiedSentence = secureSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())
    if modifiedSentence == 'STOP':
        connected = False
        secureSocket.close()