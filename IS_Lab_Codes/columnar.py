key = input("enter the key ")
columns = [(j,i) for i ,j in enumerate(key)]
columns = sorted(columns)

pt = input("enter the plain text ")
print(pt)
col = len(key)
rows = int(len(pt)/col )

index = 0
elems = [["" for i in range(col)] for j in range(rows)]

for i in range(rows):
    for j in range(col):
        elems[i][j] = pt[index]
        index += 1
    
for row in elems:
    print(row)

ct = []
for column in columns:
    c = column[1]
    temp = []
    for i in range(rows):
        temp.append(elems[i][c])
    ct.append(temp)
print("")
for row in ct:
    print(row)
    
def decrypt(ct,row,col, columns):
    elems = [["" for i in range(col)] for j in range(rows)]
    index = 0
    for column in columns:
        c = column[1]
        for i,j in enumerate(ct[index]):
            elems[i][c] += j
        index += 1
            
    print(elems)
    return elems

decrypt(ct,rows, col, columns)