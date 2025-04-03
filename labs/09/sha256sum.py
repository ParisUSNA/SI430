#!/bin/python3

import sys
import hashlib

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Usage: ./sha256sum.py [args]")
        exit

    for i in range(1, len(sys.argv)):
        with open(sys.argv[i], "rb") as file:
            digest = hashlib.file_digest(file, "sha256")

            print(f"{digest.hexdigest()}  {sys.argv[i]}")
