import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# The public key in PEM format
public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA09NxQBBY8W3El6h7v7r8
GlMHbcu1zrgM8Ib5UUbS+GarKKjR/+nHl/QR6Nv2E9z3qF2cdFhs//GS7gLn/6mh
vAYpznyzYNMmEizfUGVfdOfkohz/4nmy1B/2IriLrcSWGEfR5ZXfbzb2hcYxLfUP
lx6phgWx0aYO5PdOdNhgnaaeJhkH40VpG1I23s28R1lsSfsvbKrGJ9a55JHzXm/M
a7KirP/MMjmohvKjCXfETL/Uwd4AItBtOzWrbx6s6IWQpjEDesOoMdoDfB9Bz8zJ
m18Wb2zT8qkwudl0S780ufRONL8WcNOCCLs2Fkb3koOi620wJXUqrKvKv2VHV5Fv
vDhe1BMnsQbDutnfB7m1S2xW+L5weyxJlnYBkRNKQu+HVfOXowPiFQxIaUcth1/W
YN2U9kgSarom1N50Xm0oM8x5DyqXna+eQ7BKfRMpETwzWejLS/ZIuljpZzJsgcLP
b3k2xxwDq19IUcMOIEErpHaI+85Z8bSq7F4NlF2mRqe8WhlpUpQvu3IAAhJkZJZQ
yrfheZg2MJmOFpCwX5ACMvid5w8LawdOLfORFwcCvyaoys+3mZruQ+QHgf9ez3er
ptd2jHZX8WVOg1a+5hnipGDfYlUXyPhbAV6orMpsCyLGVqEzLVYyTHh2OjvOvRBk
3ZAQWVTtyLuT1X5pQr4+MGUCAwEAAQ==
-----END PUBLIC KEY-----
"""

# Decode the PEM format to get DER encoded data
public_key_der = base64.b64decode(''.join(public_key_pem.strip().splitlines()[1:-1]))

# Parse the DER encoded data to extract the components
public_key = serialization.load_der_public_key(public_key_der, backend=default_backend())
modulus = public_key.public_numbers().n
exponent = public_key.public_numbers().e

print("Modulus (n):", modulus)
print("Exponent (e):", exponent)

print("Modulus (n):", base64.encode(modulus))

