def encrypt(pt):
    ct = ""
    for i in pt:
        ct += chr((((ord(i) - ord('a')) + 3)%26)+ord('a'))
    return ct

def decrypt(ct):
    pt = ""
    for i in ct:
        val = ord(i) - ord('a')
        val -= 3
        if val <0:
            val = 26 +val
        val += ord('a')
        pt += chr(val)
    
    return pt

pt = "xyzabc"
ct = encrypt(pt)
print(f'encrypted text is {ct}')
dt = decrypt(ct)
print(f'decrypted text is {dt}')
print(pt == dt)

