import uuid
import random
import base64

def generate_key(pattern="**-*****-*****-*****", chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
    key = ""
    for i in pattern:
        if i == "*":
            newchar = chars[random.randint(0, len(chars)-1)]
            key += newchar
        else:
            key += i

    return key

def validate_key(key, pattern="**-****-*****-*****", chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
    newkey = ""
    valid = True
    for i in key:
        if i != "-":
            newkey += "*"
        else:
            newkey += "-"

    _len = 0

    while (valid == True or None) and (_len <= len(key)):
        for i in key:
            if (i in (chars)) or (i == "-"):
                _len += 1
                valid = True
            else:
                valid = False
            if valid == True:
                pass
            elif valid == False:
                return {"valid": False}
        
    if newkey == pattern:
        valid = True
    else:
        valid = False

    return {"valid": True} if valid else {"valid": False}

def storekey(dir: str, key: str):
    with open("{}/{}.key".format(dir, key[::5]+"_{}".format(random.randint(273623, 96714673876))), "x") as f:
        f.write(("--> BEGIN BIT64 KEY <--\n\n"+str(base64.b64encode(bytes(key, "UTF-8")))+"\n\n--> END BIT64 KEY <--").replace("b'", "").replace("'", ""))
    return {"filename": "{}/{}.key".format(dir, key[::5]+"_{}".format(random.randint(273623, 96714673876)))}

def retrievekey(file: str):
    with open(file, "r+") as f:
        r = f.read()
        r = r.replace("--> BEGIN BIT64 KEY <--\n\n", "")
        r = r.replace("\n\n--> END BIT64 KEY <--", "")
        return str(base64.b64decode(bytes(r, 'UTF-8'))).replace("b'", "").replace("'", "")