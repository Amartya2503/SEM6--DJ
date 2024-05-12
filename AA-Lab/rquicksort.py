import random
c = 0
def rquicksort(arr):
    if len(arr)<=1 :
        return arr
    global c
    left = []
    right = []
    pivotIndex = random.randint(0, len(arr)-1)
    # pivotIndex = 0
    for i in range(len(arr)):
        if i != pivotIndex:
            c += 1
            if arr[i] > arr[pivotIndex]:
                right.append(arr[i])
            else: 
                left.append(arr[i])
    
    return rquicksort(left) + [arr[pivotIndex]] + rquicksort(right)

arr = [1,2,3,4,5,6,7,8,9,10]
sortedar = rquicksort(arr)
for i in sortedar:
    print(i)
print("the cost after random quick sort is ", c)