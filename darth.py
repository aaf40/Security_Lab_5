# Message Receiver - crypto_chat_server.py
import hashlib, random, os, time
from binascii import hexlify
from socket import *
import lab6_support as ct 
import dh

#P and G are agreed upon by both Bob and Alice to be 13 and 9 respectively. They are not shared over a network connection, so Darth does not know about it.
P = 13; # A prime number P is taken 
G = 7;  # A primitive root for P, G is taken
d = 6   #Darth's private key
 
def get_dh_sharedsecret(sharedKey):
    x = dh.dh_generateSecretKey(sharedKey, d, P)
    return x
 
def get_dh_sharedkey():
    x = dh.dh_generatePublicKey(P,G,d)
    return x
 
def decrypt(ciphertext, usePKI, useDH, serverSecret):
    #msg = ct.decrypt(ciphertext, usePKI, useDH, serverSecret)
    try:
        msg = ct.decrypt(ciphertext, usePKI, useDH, serverSecret)
    except:
        msg = ciphertext
    return msg
 
def main(): 
    # set variables used to determine scheme
    useClientPKI = False;
    useDHKey = True;
    serverSecret = 0
 
    # set the variables used for the server components
    key = ""
    host = "192.168.1.233"
    port = 8080
    buf = 1024 * 2
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # UDPSock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1) # for running on linux

# Enable broadcasting mode
    # UDPSock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1) # for running on linux
    UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    UDPSock.bind(addr)
    
    print ("Waiting to received shared key from Alice...")
    (data, addr) = UDPSock.recvfrom(buf)
    
    sharedKey = int(str(data, 'utf-8'))
    #print("Shared key between Bob and Alice is", sharedKey)
    sharedSecret = get_dh_sharedsecret(sharedKey)
    
    print("Shared secret between Bob and Alice as calculated by Darth is", sharedSecret)
 
    # welcome to the server message
    print ("Waiting to receive messages...")
 
    # listening loop
    while True:
        # read the data sent from the client
        (data, addr) = UDPSock.recvfrom(buf)
        #print("Data in server", data)
        #print("Received addr", addr)
 
        # check to see if the user typed a special command such as addPKI or addDH
        #result = ct.check_server_command(plaintext)
       
        #if result == 10: # encryption has been disabled so no message
        #    plaintext = b'PKI Encryption disabled!'
        #elif result == 11: # encryption enabled
        #    plaintext = b'PKI Encryption enabled!'
        #elif result == 20: # dh enabled
        #    clientKey = plaintext
        #    plaintext = b'Diffie-Hellman disabled!'
        #elif result == 21: # encryption enabled
        #    plaintext = b'Diffie-Hellman enabled!'
 
        # messages are received encoded so you must decode the message for processing
        msg = str(data, 'utf-8')
        
        # process any client special commands
        #if result == 0:
        #    # no encryption
        #    break
 
        # if any encryption is used, change the message to 'secure' message
        if useClientPKI == True or useDHKey == True:
            # send the data packet for decryption
            plaintext = decrypt(msg, useClientPKI, useDHKey, sharedSecret)
            print ("Received wrong message: " + plaintext)
        else:
            print ("Received message: " + msg)
        
 
    UDPSock.close()
    os._exit(0) 
 
if __name__ == '__main__': 
    main() 
