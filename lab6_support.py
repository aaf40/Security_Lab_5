# Chat Encryption Helper - ch9_crypto_chat.py
import os, base64, json
#from Crypto.Cipher import PKCS1_OAEP, AES
#from Crypto.PublicKey import RSA, ECC
from binascii import hexlify, unhexlify
from base64 import b64encode, b64decode
 
# encryption method used by all calls
def encrypt(message, usePKI, useDH, dhSecret):
    em=cipherEncrypt(message, dhSecret, 1)
    return em
 
# decryption method used by all calls
def decrypt(message, usePKI, useDH, dhSecret):
    dm=cipherEncrypt(message, dhSecret, -1)
    return dm
 
# decrypt using RSA (for future reference, not needed for this homework)
#def decrypt_rsa(ciphertext):
#    return ciphertext
 
# encrypt using RSA (for future reference, not needed for this homework)
#def encrypt_rsa(message):
#    return message
 
# check client commands (for future reference, not needed for this homework)
def check_client_command(data):
    return 1
 
# check server commands (for future reference, not needed for this homework)
def check_server_command(data):
    return 1
    
def reversed_string(a_string):
    return a_string[::-1]

def cipherEncrypt(inputText, n, d):
    if d not in [1, -1] or n < 1:
        return "Invalid n or d value"
    
    valid_chars = [chr(i) for i in range(34, 127)]
    encryptedText = ""
    
    inputText = inputText[::-1]
    
    for char in inputText:
        if char in valid_chars:
            index = valid_chars.index(char)
            if d == 1:
                shifted_index = (index + n) % len(valid_chars)
            else:
                shifted_index = (index - n) % len(valid_chars)
            encryptedText += valid_chars[shifted_index]
        else:
            encryptedText += char
    
    return encryptedText

