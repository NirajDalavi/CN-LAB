# RSA Encryption/Decryption Program
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q
    phi = (p-1) * (q-1)
    e = 343
    g = gcd(e, phi)
    while g != 1:
        e+=1
        g = gcd(e, phi)
    d = modinv(e, phi)
    return ((e, n), (d,n),phi,e)

def encrypt(pk, plaintext):
    key, n = pk
    cipher = (plaintext ** key) % n 
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = (ciphertext ** key) % n 
    return (plain)

if __name__ == '__main__':
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private,phi,e = generate_keypair(p, q)
    print("Value of phi is",phi)
    print("Value of e is",e)
    print("Your public key is ", public ," and your private key is ", private)
    message = int(input("Enter a message to encrypt with your public key: "))
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print( encrypted_msg)
    print("Decrypting message with private key ", private ," . . .")
    print("Your message is:")
    print(decrypt(private, encrypted_msg))