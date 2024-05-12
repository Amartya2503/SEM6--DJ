class TreeNode:
    def __inti__(self, val=None):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None
        self.color = 1
        return self


def checksibling(node):
    if node.parent:
        parent = node.parent
        sibling = None
        if parent.right == node:
            sibling = parent.left
        else:
            sibling = parent.right
        if not sibling:
            return False
        return node.color == sibling.color
    else:
        return False

def switchcolor(parent):
    if parent.color == 0:
            parent.color = 1
    else:
        parent.color = 1

def changecolor(node):
    if not node.parent:
        return

    parent = node.parent
    if parent.right == node:
        sibling = parent.left
    else:
        sibling = parent.right

    sibling.color = 0
    node.color = 0

    switchcolor(parent)

def rrrotation(parent, grandparent, grandParentParent):
    #this is the RR case in which parent is the average value node which becomes the grand parent and the grand parent becomes the left child of current node. the left sub tree of parent will become child of updated left child of new grandparent
    tempParentLeft = parent.left
    tempGrandParentLeft = grandparent.left
    
    if not grandParentParent:
        pass
    if grandParentParent.right == grandparent:
        grandParentParent.right = parent
    else:
        grandParentParent.left = parent
    #now we did the supergrandParent change its linkage to parent which is new grand parent
    #so as our parent is rotated , we need to make the parent link back to grandparents parent
    parent.parent = grandParentParent
    #since RR our parents left is the previous grandparent
    parent.left = grandparent
    #parents left child is now the grandParent so we also update the grandParents parent and set it to the parent
    grandparent.parent = parent
    #previously what was parents right will become grandparents new right 
    grandparent.right = tempParentLeft
    #what we just made the grandparents new right child we need to update its parent as well 
    tempParentLeft.parent = grandparent
        
def llrotation(parent, grandparent, grandParentParent):
    tempParentRight = parent.right
    if grandParentParent.right == grandparent:
        grandParentParent.right = parent
    else:
        grandParentParent.left = parent
    parent.parent = grandParentParent
    
    parent.right = grandparent
    grandparent.parent = parent
    
    grandparent.left = tempParentRight
    tempParentRight.parent = grandparent
        
def rotateTree(node, parent):
    
    grandparent = parent.parent
    if not grandparent:
        #such case must not be permitted 
        return 
    if parent.right == node:
        d1 = 'r'
    else:
        d1 = 'l'
    if grandparent.right == parent:
        d0 = 'r'
    else:
        d0 = 'l'
        
    grandParentParent = grandparent.parent
    #we know wether we have RR, RL , LL , LR rotation now 
    if d0 == 'r' and d1 == 'r':
        rrrotation(parent, grandparent, grandParentParent)
        
    if d0 == 'l' and d1 == 'l':
        llrotation(parent, grandparent, grandParentParent)
    
    if d0 == 'r' and d1 == 'l':
        #small value is the leaf node
        pass
        
    switchcolor(parent)
    switchcolor(grandparent)     
            
        
def checkconflict(node, depth):
    if node.parent and node.color == 1 and node.parent.color == 1:
        print(f'need of rotation as node having value {node.val} at depth {depth+1} has conflict with node {node.parent} at depth {depth}')
        # we witness a red red conflict
        if checksibling(node.parent):
            # sibling also red or same color
            changecolor(node.parent)
            print(f'since both sibling of parents are same color we can recolor them to parent - {node.parent.color}')
            if node.parent.parent:
                checkconflict(node.parent.parent)
        else:
            # parent and uncle not same , now we witness rotation
            pass


def rbinsertion(head, value):
    if not head:
        # root node defined and returned without traversal
        head = TreeNode(value)
        head.color = 0
        head.parent = None
        return head
    temp = head
    node = TreeNode(value)
    depth = 0
    while (temp):
        if value >= temp.val:
            print("moving right at depth ", depth)
            if temp.right:
                temp = temp.right
            else:
                print("inserting at depth ", depth+1)
                temp.right = node
                node.color = 1
                node.parent = temp
        else:
            print("moving left at depth ", depth)
            if temp.left:
                temp = temp.left
            else:
                print("inserting at depth ", depth+1)
                temp.left = node
                node.color = 1
                node.parent = temp

        depth += 1
    
    checkconflict(node, depth)
