#my potential is the number of ones in the counter
#cost of channging the count is 1
def countones(a):
    b = a
    count = 0
    while b:
        if b&1:
            count+= 1
        b = b>>1
    return count

def lisbin(a):
    b = a
    ls = []
    while b:
        ls.append(b&1)
        b = b>>1
    ls = ls[::-1]
    ls = [0]*(4-len(ls)) +ls
    return ls

def diff(list1, list2):
    cost = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            cost += 1
    return cost

a = int(input("enter the value till which you want to count"))
print(f'counter\t\t value\t\t actualcost\tpotentialDiff\t totalcost')
pastlis = [0]*4
for i in range(1,a):
    curpotential = countones(i)
    prevpotential = countones(i-1)
    potentialDiff = curpotential - prevpotential
    val = lisbin(i)
    actual = diff(val, pastlis)
    print(f'{i}\t  {val}\t\t  {actual}\t\t  {potentialDiff}\t\t  {actual + potentialDiff}')
    pastlis = val