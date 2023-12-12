import socket
import library

# this will serve as the "client" for our implementation
def Main():
        #virtual machine IP
        #host = "192.168.100.221"
        host="127.0.0.1"
        port = 5001
        #necessary to connect to the server
        mySocket = socket.socket()
        mySocket.connect((host,port))
        
        message = input("Enter the message you want to encrypt -> ")
        UnencryptedMessage = library.text_to_bits(message)
        print("Unencrypted message = " + UnencryptedMessage)
        #encrypting the message using DES
        finalEncryptedMessage = library.encrypt(message)
        print("Encrypted message   = " + finalEncryptedMessage)

        #have the communication go on forever
        while message != 'q':

                #prints the pretty loading bar
                library.sending()

                #encrypting the message
                finalEncryptedMessage = library.encrypt(message)
                #sending the message
                mySocket.send(finalEncryptedMessage.encode())
                #receiving the response from the other user
                data = mySocket.recv(1024).decode()
                print ("Received from server      = " + data)
                #decrypting the other user's message
                decryptedMessageRaw = library.decrypt(data)
                if not data:
                        break
                print ("Decrypted Message in bits = " + str(decryptedMessageRaw))
                #Preapare decrypted text
                decryptedMessage = library.text_from_bits(decryptedMessageRaw)
                print ("Decrypted Message in text = " + decryptedMessage)
                print("\n")
                #setting up the message all over again....
                message = input("Enter the message you want to encrypt -> ")
                finalEncryptedMessage = library.encrypt(message)
                print("Encrypted message = " + finalEncryptedMessage)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
