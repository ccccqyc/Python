from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while True:
    # Establish the connection
    print"Ready to server..."
    connectionSocket, addr = serverSocket.accept()
    print 'connected to port', serverPort

    try:
        message = connectionSocket.recv(1024)

        filename = message.split()[1]
        f = open(filename[1:])

        outputdata = f.open(filename[1:])

        # send one http header line into socket2
        # fill in start
        connectionSocket.send("HTTP/1.0 200 OK\r\n")

        # send the content if the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata)
            connectionSocket.close()
    except IOError:
        #send response message for line not found
        print "404 Error : File Not Found."

    connectionSocket.close()