# pt = "oak"
pt = "RAMSWARUPK"
# key = "son"
key = "RANCHOBABA"
ct = ""
for i in range(len(pt)):
    vala = ord(pt[i]) - ord('a')
    valb = ord(key[i]) - ord('a')
    valc = (vala^valb)%26
    ct += chr(valc+ord('a'))
print(ct)
dt = ""
for i in range(len(key)):
    vala = ord(key[i]) - ord('a') 
    valb = ord(ct[i]) - ord('a')
    valc = (vala^valb)%26
    dt += chr(valc+ord('a')) 
print(dt)