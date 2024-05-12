import random 
costOfHiring = 5
costOfInterview = 1
totalCost = 0
def hire(list1):
    global costOfHiring 
    global costOfInterview
    global totalCost 
    hired = []
    interviews = len(list1)
    while interviews != 0:
        candidate = random.randint(0,len(list1)-1)
        totalCost += costOfInterview
        print(f'interviewing {list1[candidate]} ')
        if not hired:
            print(f'hiring {list1[candidate]} as no one hired here')
            hired = list1[candidate]
            
        elif list1[candidate] > hired:
            
            print(f'hiring {list1[candidate]} as he is better than {hired}')
            hired = list1[candidate]
            totalCost += costOfHiring  
        list1.pop(candidate)
        interviews -= 1
    print(f'total cost of process is {totalCost}')
    
list1 = [1,2,3,4,5,6,7,8,9,10]
hire(list1)