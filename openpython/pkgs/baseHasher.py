import base64
import os

def encode(data):
    key = base64.b64decode(bytes(data, 'utf-8'))
    return key

def decode(key):
    data = base64.b64decode(key.decode('utf-8'))
    return data