# import random
# c = 0
# def quicks(list1):
#     global c
#     if len(list1) <= 1:
#         return list1
#     # pivot = random.randint(0,len(list1)-1)
#     pivot = 0
#     pivotel = list1[pivot]
#     left = []
#     right = []
#     for i, j in enumerate(list1):
#         c+= 1
#         if i != pivot:
#             if j  > pivotel:
#                 right.append(j)
#             else:
#                 left.append(j)
#     return quicks(left) + [pivotel] + quicks(right)

# list1 = [10,9,8,7,6,5,4,3,2,1]
# list1 = quicks(list1)
# print(f'after sorting list is {list1}')
# print(f'the cost is {c}')


############################################################################
                #KD Tree#
############################################################################

# class TreeNode:
#     def __init__(self,val = None):
#         self.val = val
#         self.right = None
#         self.left = None
    
# def insertion(head,k):
#     print("enter the elements of node")
#     val = [0]*k
#     for i in range(k):
#         val[i] = int(input())
        
#     newNode = TreeNode(val)
#     temp = head
#     if not temp:
#         head = newNode
#         return head
#     depth = 0
#     while(temp):
#         compindex = depth%k
#         if val[compindex] >= temp.val[compindex] :
#             print("moving right at depth ", depth)
#             if temp.right:
#                 temp = temp.right
#             else:
#                 print(f'inserting at depth {depth+1}')
#                 temp.right = newNode
#                 return newNode
#         else:
#             print("moving left at depth ", depth)
#             if temp.left:
#                 temp = temp.left
#             else:
#                 print(f'inserting at depth {depth+1}')
#                 temp.left = newNode
#                 return newNode
#         depth += 1
# def kdTree():
#     head = None
#     option = 0
#     k = int(input('enter the number of dimensions '))
#     while(option != -1):
#         option = int(input("enter the option "))
#         if option == 1:
#             if not head:
#                 head = insertion(head,k)
#             else :
#                 insertion(head, k)
        
# kdTree()


###############################################################################
                            #grahams scan
###############################################################################

##Steps of grahams scan algo :
# 1. find the starting point which is min in coordinates
# 2. sort the points in polar angles basis using atan2(points[0] -start[0], points[1]-start[1])
# 3. define a function to find direction , same , clock or anticlock orientation is calculated using cross product(p,q,r)
# 4. now get a stack in which insert the first 2 elements for all the following elements while the size of stack is greater than 2 and the incoming point is not making an anticlock movement keep popping the top of stack
# 5. at the end we are left with the elements present in the grahams scan algo
# def grahams(points):
    
                






















