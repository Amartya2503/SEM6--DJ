present = []
matrix = [["" for i in range(5)] for j in range(5)]
key = "monarchy"
pt = "instruments"
# pt = "helloe"
i = 0
while(True):
    if i >= len(pt)-1:
        break
    if pt[i] == pt[i+1]:
        print(pt[i])
        prev = pt[:i+1]
        next = pt[i+1:]
        pt = prev + "x" + next
        print(f'after edition pt is {pt}')
    i += 2
if len(pt)%2 != 0:
    pt += "z"
print(pt)
#nwo pt is ready , we need to make the matrix
def encrypt(matrix, pt):
    ct = []
    for i in range(0,len(pt),2):
        c1 = pt[i]
        c2 = pt[i+1]
        c1r, c1c = 0,0
        c2r , c2c = 0,0
        for j in range(len(matrix)):
            if c1 in matrix[j]:
                c1r = j
                c1c = matrix[j].index(c1)
            if c2 in matrix[j]:
                c2r = j
                c2c = matrix[j].index(c2)
        pair = ""
        if c1r == c2r:
           pair += matrix[c1r][(c1c+1)%5] + matrix[c1r][(c2c+1)%5]
        elif c1c == c2c:
            pair += matrix[(c1r+1)%5][c1c] + matrix[(c2r+1)%5][c2c]
        else:
            pair += matrix[c1r][c2c] + matrix[c2r][c1c]
        print(pair)
        ct.append(pair)
    return ct

def decrypt(matrix, ct):
    pt = []
    for i in ct:
        c1 = i[0]
        c2 = i[1]
        c1r,c1c = 0,0
        c2r,c2c = 0,0
        for j in range(len(matrix)):
            if c1 in matrix[j]:
                c1r = j
                c1c = matrix[j].index(c1)
            if c2 in matrix[j]:
                c2r = j
                c2c = matrix[j].index(c2)
        pair = ""
        if c1r == c2r:
            pair += matrix[c1r][(c1c-1)%5] + matrix[c2r][(c2c-1)%5]
        elif c1c == c2c:
            pair += matrix[(c1r-1)%5][c1c] + matrix[(c2r-1)%5][c1c]
        else:
            pair = matrix[c1r][c2c] + matrix[c2r][c1c]
        print(pair)
        pt.append(pair)
    return pt
#rule of matrix : j will not appear, all letters of key will be only filled once , rest of remaining letters fill 5x5 matrix
m = []
[m.append(el) for el in key if el not in m]
[m.append(chr(val)) for val in range(97, 123) if chr(val) not in m and chr(val) != "j" and len(m )< 25 ]
matrix = [m[i:i+5] for i in range(0, len(m), 5)]
print (matrix)

ct = encrypt(matrix , pt)
print(f'cipher text is {ct}')

dt = decrypt(matrix, ct)
print(f'decrypted message is {dt}')