import base64
import random
import os

def encode(data):
    randEnc = random.randint(50, 100)
    key = base64.b64encode(bytes(data, 'utf-8'))
    return key

def decode(key):
    data = base64.b64decode(key.decode('utf-8'))
    return data