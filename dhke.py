import argparse                                                               #To parse the arguments given to the script
from Crypto.Cipher import AES                                                 #To implement encryption
from Crypto.Util.Padding import pad, unpad

def calculate_shared_key(g_e: int, g_c: int, N_e: int, N_c: int, x: int, gy_modN: int) -> int:
    
    g = (2 ** g_e) - g_c
    N = (2 ** N_e) - N_c
    
    key = pow(gy_modN, x, N)                                                  #Calculate the shared key
    return key;

def encrypt(plaintext: str, key: int, IV: bytes) -> bytes:

    key_bytes = key.to_bytes(32, byteorder='little')                          #Convert the integer key to bytes
    #print(key_bytes, IV)
 
    cipher = AES.new(key_bytes, AES.MODE_CBC, IV)                             #Create a new AES cipher in CBC mode (since we have an initialization 
    #print(cipher)                                                            #vector
    
    ciphertext = cipher.encrypt(pad(plaintext.encode('UTF-8'), AES.block_size)) #Encrypt using AES after encoding the plaintext in UTF-8
    return ciphertext;
  
def decrypt(ciphertext: bytes, key: int, IV: bytes) -> str:
    
    key_bytes = key.to_bytes(32, byteorder='little')                          #Convert the integer key to bytes
     
    dtxt = AES.new(key_bytes, AES.MODE_CBC, IV)                               #Create a new cipher
    plaintext = unpad(dtxt.decrypt(ciphertext), AES.block_size)               #Decrypt the encrypted ciphertext

    return plaintext;


parser = argparse.ArgumentParser(description="Diffie-Hellman Encryption")     #parse the given arguments
parser.add_argument("--iv", required=True)
parser.add_argument("--g_e", required=True, type=int)
parser.add_argument("--g_c", required=True, type=int)
parser.add_argument("--N_e", required=True, type=int)
parser.add_argument("--N_c", required=True, type=int)
parser.add_argument("--x", required=True, type=int)
parser.add_argument("--gy_modN", required=True, type=int)
parser.add_argument("--ciphertext", required=True)
parser.add_argument("--plaintext", required=True)


args = parser.parse_args()
# 
# print("init vector: ", args.iv)
# print("g_e: ", args.g_e)
# print("g_c: ", args.g_c)
# print("N_e: ", args.N_e)
# print("N_c: ", args.N_c)
# print("x: ", args.x)
# print("gy_modN: ", args.gy_modN)
# print("encrypted message: ", args.ciphertext)
# print("plaintext: ", args.plaintext)
# 
key = calculate_shared_key(args.g_e, args.g_c, args.N_e, args.N_c, args.x, args.gy_modN)
# print(key)

ivstring = "".join((args.iv).split())                                         #Remove all the whitespace from the initialization vector given
# print(ivstring)

ivbytes = bytes.fromhex(ivstring)                                             #Convert the initialization vector to hex bytes
#print(ivbytes)

ctxt = encrypt(args.plaintext, key, ivbytes)                                         

c = "".join((args.ciphertext).split())                                        

ciphertext = bytes.fromhex(c)
dtxt = decrypt(ciphertext, key, ivbytes)

#print(dtxt.decode('UTF-8'))
#print(ctxt.hex().upper())

l = ctxt.hex().upper()

k = ' '.join(l[i:i+2] for i in range(0, len(l), 2))                          #Add whitespace after every 2 characters

print(f"{dtxt.decode('UTF-8')}, {k}")                                        #Print decoded and encrypted





