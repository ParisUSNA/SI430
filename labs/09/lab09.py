#!/bin/python3

import hashlib
import sys
import hmac

def computeHMAC(key, data):
    x = hmac.digest(key, data, 'sha256')
    return x
