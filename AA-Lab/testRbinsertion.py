
class TreeNode():
    def __init__(self, val =None):
        self.val = val
        self.color = 1
        self.right = None
        self.left = None
        self.parent = None

def switchcolor(node):
    if node.parent:
        if node.color == 1:
            print(f'changing node {node.val} from red to black')
            node.color= 0
        else:
            print(f'changing node {node.val} from black to red')
            node.color == 1
    return

def resolverotation(node):
    
def checkconflict(node):
    if not node.parent:
        return False
    parent = node.parent
    if not parent.parent:
        return False
    grandparent = parent.parent
    if node.color == 1 and parent.color == 1:
        print(f"conflict at {node.val} and its parent {parent.val}")
        if grandparent.left == parent : 
            unclenode = grandparent.right
        else :
            unclenode = grandparent.left
        if not unclenode:
            print("there is need for rotation ")
            resolverotation(node)
            return False
        if unclenode.color == parent.color:
            switchcolor(unclenode)
            switchcolor(parent)
            switchcolor(grandparent)
            
            return checkconflict(grandparent)
    else:
        return False
        
        

def insertion(head, val):
    print("inserting ",val)
    node = TreeNode(val)
    if not head :
        print('creating head ')
        head = node
        head.color = 0
        head.parent = None
        return head
    
    temp = head
    depth = 0
    while(temp):
        if val >= temp.val:
            print(f'moving right at depth {depth}')
            if temp.right:
                temp = temp.right
            else:
                print(f'inserting {val} at depth {depth+1} ')
                temp.right = node
                node.parent = temp
                checkconflict(node) 
                return node
        else:
            print(f'moving left at depth {depth}')
            if temp.left :
                temp = temp.left
            else:
                print(f'inserting {val} at depth {depth+1}')
                temp.left = node
                node.parent  = temp
                checkconflict(node) 
                return node
    
    
    
head = insertion(None, 55)
insertion(head, 66)
insertion(head, 27)
insertion(head, 19)
insertion(head, 51)
insertion(head, 83)
insertion(head, 57)
insertion(head, 72)
insertion(head, 68)