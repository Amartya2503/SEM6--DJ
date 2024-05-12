#we have a bank account , each operation is assigned the prefix amortized cost , which is added to the bank 
#for every operation whatever is the cost we remove that from the bank
#in doing so our bank must never become negative (this depends on the amortized cost we prefix)
#whatever is left is the excessive we are left with at the end


list1 = [1,2,3,4,5,6,7,8,9,10]
bank = 0 
stipend = 3
def expand(lista):
    list2 = lista + [0]*len(lista)
    return list2    

list2 = [0]
cursize = 0
print(f'element\t  size\t  cost\t  bank')
for i , j in enumerate(list1):
    bank += stipend
    cost = 1
    if i > cursize:
        cost += len(list2)
        list2 = expand(list2)
        cursize = len(list2)-1
    list2[i] = j
    bank -= cost
    print(f'{j}\t   {cursize+1}\t   {cost}\t   {bank}')
    if bank<0:
        print(f'can not have {stipend} as amortized cost as more balance required ')
        break
    
        