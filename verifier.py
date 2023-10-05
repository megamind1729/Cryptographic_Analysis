from sign import *

file_path = input("Enter file path: ")
N = int(input("Enter N: "))  
e = int(input("Enter e: "))
signature_hex = input("Enter signature(in hex, does not start with 0x): ")
if (signature_hex[0:2] == "0x"):
    signature_hex = signature_hex[2:]

signature = int(signature_hex, 16)

sha256 = calculate_sha256(file_path)
expected_signature = rsa_sign(sha256, N, e)

if signature == expected_signature:
    print("accept")
else:
    print("reject")
