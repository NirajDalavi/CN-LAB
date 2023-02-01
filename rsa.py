import random
import math

def multiplicative_inverse(e, phi):
    d = 0
    k = 1
    while True:
        d = (phi * k + 1) / e
        if d.is_integer():
            return int(d)
        k += 1

# def generate_keypair(p, q):
#     n = p * q
#     phi = (p-1) * (q-1)
#     e = random.randint(1, phi)
#     g = math.gcd(e, phi)
#     while g != 1:
#         e = random.randrange(1, phi)
#         g = math.gcd(e, phi)
#     d = multiplicative_inverse(e, phi)
#     return ((e, n), (d, n))
        
        
        
def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = 2
    
    g = math.gcd(e, phi)
    while g != 1:
        e +=1
        g = math.gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext] #Calculated (char^key)%n for each char of PT
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public, message)
    print(f"Encrypted message: {encrypted_msg}")
    print(f"Decrypted message: {decrypt(private, encrypted_msg)}")
