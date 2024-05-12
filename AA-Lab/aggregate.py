#the number of operations is the number of times we try insertion
#the cost of each operation is 1 if we have empty space in array , else the cost becomes size of previous array +1(of current insertion)

cost = 0
operations = 0

def expand(list1):
    list2 = [0]*2*len(list1)
    for i in range(len(list1)):
        list2[i] = list1[i]
    return list2

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

list2 = [0]
cursize = 0
for j,i in enumerate(list1):
    if j > cursize:
        print(f'size previously : {len(list2)}')
        cost += len(list2)
        list2 = expand(list2)
        cursize = len(list2) -1
        print(f'size after updating : {len(list2)}')
    print(f'inserting {i}\t index {j}\t remaining size {len(list2)-j} ')
    list2[j] = i
    cost += 1
    operations += 1
    
print("cost of all operations is = ", cost)
print("total number of operations is = ", operations)
print("amortized cost using aggregate method is ",cost/operations)



