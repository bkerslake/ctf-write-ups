import math
import hashlib
import sys
from tqdm import tqdm
import functools
from sympy import *
import numpy as np

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb78a053d258da7c42b")

#Set up matrix A
A = Matrix([[21, 301, -9549, 55692],
           [1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0]])
P, D = A.diagonalize()
P_inv = P.inv()
B = P*D*P_inv

final = pow(B, int(20000000)) * Matrix([4, 3, 2, 1])

# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = final[3]
    decrypt_flag(sol)