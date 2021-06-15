class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.me = val


def Insert(x, tree):
    if len(tree) < 1:
        tree.append(Node(x))
    else:
        Insert2(x, tree[0])
        
def Insert2(x, node):
    if x < node.me:
        if node.left != None:
            Insert2(x, node.left)
        else:
            node.left = Node(x)
    else:
        if node.right != None:
            Insert2(x, node.right)
        else:
            node.right = Node(x)
      
            
def PrintTree():
    if tree[0] != None:
        print(str(tree[0].me))
        count = 0
        PrintTree2(tree[0], count)
    
def PrintTree2(node, count):
    if node != None:
        count += 1
        
        if node.left != None:
            temp = "| "
            
            i = 1
            while i < count:
                temp += "| "
                i += 1
                
            temp += str(node.left.me)
            print(temp)
            PrintTree2(node.left, count)
            
        if node.right != None:
            temp = "| "
            
            i = 1
            while i < count:
                temp += "| "
                i += 1
                
            temp += str(node.right.me)
            print(temp)
            PrintTree2(node.right, count)
    
    
def PrintInorder(node):
    s = ""
    if node != None:
        s += PrintInorder(node.left)
        s += str(node.me)
        s += " "
        s += PrintInorder(node.right)
    return s
         
def PrintPostorder(node):
    s = ""
    if node != None:
        s += PrintPostorder(node.left)
        s += PrintPostorder(node.right)
        s += str(node.me)
        s += " "
    return s

def PrintPreorder(node):
    s = ""
    if node != None:
        s += str(node.me)
        s += " "
        s += PrintPreorder(node.left)
        s += PrintPreorder(node.right)
    return s

        
into = [50,75,25,15,60,35,90,42,20,27,5,55,95,80,70]
into2 = [5,4,9,7,6]

tree = []

for i in into:
    Insert(i, tree)
    
PrintTree()
print(" ")
print("pre-order:  " + PrintPreorder(tree[0]))
print("in-order:   " + PrintInorder(tree[0]))
print("post-order: " + PrintPostorder(tree[0]))







