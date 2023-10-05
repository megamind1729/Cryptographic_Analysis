import hashlib
import random
import sympy

def generate_semiprime(bits):
    while True:
        p = sympy.randprime(2**(bits - 1), 2**bits)
        q = sympy.randprime(2**(bits - 1), 2**bits)
        N = p * q
        if p != q and N.bit_length() == bits * 2:
            return N

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()

def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def rsa_sign(message, N, e):
    return mod_pow(int(message, 16), e, N)

if __name__ == "__main__":
    N = generate_semiprime(1024)
    e = 65537

    file_path = input("Enter file path: ")

    sha256 = calculate_sha256(file_path)

    signature = rsa_sign(sha256, N, e)
    signature_hex = hex(signature)[2:]

    print("Random semiprime N:", N)
    print("SHA-256 hash of the file:", sha256)
    print("RSA signature:", signature_hex)
