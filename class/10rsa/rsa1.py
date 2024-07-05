#! /usr/bin/env python3
import random
from sympy import isprime, mod_inverse

def generate_keypair(bits):
    # 選擇兩個大質數 p 和 q
    p = random_prime(bits)
    q = random_prime(bits)
    while p == q:
        q = random_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)

    # 選擇公開指數 e
    e = 65537  # 常用公開指數
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def random_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

def encrypt(public_key, plaintext):
    e, n = public_key
    plaintext_int = int.from_bytes(plaintext.encode('utf-8'), 'big')
    cipher_int = pow(plaintext_int, e, n)
    return cipher_int

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext_int = pow(ciphertext, d, n)
    plaintext = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return plaintext

# 測試RSA加密演算法
if __name__ == "__main__":
    bits = 512  # 密鑰長度
    public_key, private_key = generate_keypair(bits)

    message = "Hello, RSA!"
    ciphertext = encrypt(public_key, message)
    print(f"加密後的密文: {ciphertext}")

    decrypted_message = decrypt(private_key, ciphertext)
    print(f"解密後的明文: {decrypted_message}")

    bits = 2048  # 使用更長的密鑰
    public_key, private_key = generate_keypair(bits)

    message = "Hello, RSA with 2048-bit key!"
    ciphertext = encrypt(public_key, message)
    print(f"加密後的密文: {ciphertext}")

    decrypted_message = decrypt(private_key, ciphertext)
    print(f"解密後的明文: {decrypted_message}")
