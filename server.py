import socket
import library

#this will serve as the "server" for our implementation

def Main():
    #virtual machine IP
    #host = "192.168.100.221"
    host="127.0.0.1"
    port = 5001
    #necessary to initiate the server
    mySocket = socket.socket()
    mySocket.bind((host,port))

    print("Waiting for connection.....")
    #listens for a user to connect
    mySocket.listen(2)
    #getting the user's connection info
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    while True:
            #receiving the response from the other user
            data = conn.recv(1024).decode()
            print ("Received from client      = " + data)
            #decrypting the other user's message
            decryptedMessageRaw = library.decrypt(data)
            decryptedMessage = library.text_from_bits(decryptedMessageRaw)
            if not data:
                    break
            print ("Decrypted Message in bits = " + decryptedMessageRaw)
            print ("Decrypted Message in text = " + str(decryptedMessage))
            print("\n")
            message = input("Enter the message you want to encrypt -> ")
            #encrypting the message using DES
            finalEncryptedMessageRaw = library.encrypt(message)
            #prepare the unencrypted message
            UnencryptedMessage = library.text_to_bits(message)
            print("Encrypted message   = " + finalEncryptedMessageRaw)
            print("Unencrypted message = " + UnencryptedMessage)
            #prints the pretty loading bar
            library.sending()
            #sending the message
            conn.send(finalEncryptedMessageRaw.encode())
 
    conn.close()
     
if __name__ == '__main__':
    Main()





