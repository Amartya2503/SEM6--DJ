import math
def encrypt(pt, e, n):
    val = pow(pt, e)
    val = val%n
    return val

def decrypt(ct, d, n):
    val = pow(ct, d)
    val = val%n
    return val
        
def calcD(phi, e):
          #[b, mod, div]
    prev = [0, phi, None]
    curr = [1, e, int(phi/e)]
    
    while(curr[1] != 1):
        print("new")
        print(prev)
        print(curr)
        new = [0]*3
        new[0] = prev[0] - (curr[0]*curr[2])
        new[1] = prev[1]%curr[1]
        new[2] = int(curr[1]/new[1])
        prev = curr
        curr = new
    print(prev)
    print(curr)
    if curr[0] <0:
        return phi + curr[0]
    return curr[0]

def rsa():
    p = int(input("enter the value of p"))
    q = int(input("enter the value of q"))

    phi = (p-1)*(q-1)
    n = p*q
    
    #calculate e as a prime variable between 1 and phi
    e = 2
    while e<phi:
        if math.gcd(e, phi) == 1:
            break
        e+= 1
    print("e equals ",e)
    d = calcD(phi, e)
    pt = int(input('enter the plain text'))
    ct = encrypt(pt, e, n)
    print(f'ciper text is {ct}')
    dt = decrypt(ct, d, n)
    print(f'deciphered text is {dt}')
    print(pt == dt)
    return
        
rsa()
    
