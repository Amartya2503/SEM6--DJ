#my potential is the number of ones in the counter
#cost of channging the count is 1
def countones(a):
    b = a
    count = 0
    while b:
        if b&1:
            count+= 1
        b = b>>1
    # print(f'the number of ones in {a} is {count}')
    return count

a = int(input("enter the value till which you want to count"))
cost=0
print(f'counter\t cost\t potential\t prevPotential\t totalcost')
for i in range(1,a):
    curpotential = countones(i)
    prevpotential = countones(i-1)
    cost += 1+(curpotential - prevpotential)
    print(f'{i}\t  {1}\t  {curpotential}\t\t  {prevpotential}\t\t  {cost}')
