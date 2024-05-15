pt = "geeksforgeeks"
key = "ayush"

def keyRegen(key, pt):
    while len(key) < len(pt):
        key += key
    key = key[:len(pt)]
    print(key)
    return key

key = keyRegen(key, pt)

def encrypt(key, pt):
    ct = ""
    for i in range(len(key)):
        a = key[i]
        b = pt[i]
        val = ord(a) - ord('a') + ord(b) - ord('a')
        val %= 26
        val += ord('a')
        ch = chr(val)
        ct += ch
    print(ct)
    return ct
        
def decrypt(key, ct):
    pt = ""
    for i in range(len(key)):
        b = key[i]
        a = ct[i]
        val = (ord(a)- ord('a')) - (ord(b) - ord('a'))
        val %= 26
        val += ord('a')
        pt += chr(val)
    print(pt)
    return pt

        
ct = encrypt(key, pt)
decrypt(key, ct)