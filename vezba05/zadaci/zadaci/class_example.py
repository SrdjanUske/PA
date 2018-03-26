import random

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

    # 1. ZADATAK
    def print_node(self):
        #print("Parent = ", self.parent)
        #print("Left = ", self.left)
        #print("Right = ", self.right)
        print("Data -> num = " , self.data.num)
        #print("char = ", self.data.char)

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.num = val1
        self.char = val2

# 1. ZADATAK
def addNode(root, node):
    if node.data.num >= root.data.num:
        node.parent = root
        root.right = node
    
    else:
        node.parent = root
        root.left = node


# 2.ZADATAK
def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.data.num)
        inorder_tree_walk(x.right)  


# 3. ZADATAK
def tree_search(x, k):
    if x == None or k == x.data.num:
        return x
    
    if k < x.data.num:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def Iterative_Tree_Search(n,k):
   
    while (n != None and k != n.data.num):
        if k < n.data.num:
            n = n.left
        else: n = n.right
    return n


# 4. ZADATAK
def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x

def tree_successor(x):
    if (x.right != None):
        return tree_minimum(x.right)
    y = x.parent
    while (y != None and x == y.right):
        x = y
        y = y.parent
    return y



# 5. ZADATAK
def tree_insert(root, z):
    y = None
    x = root
    
    while x != None:
        y = x
        if z.data.num < x.data.num:
            x = x.left
        else:
            x = x.right
    z.parent = y

    if y == None:
        root = z
    elif z.data.num < y.data.num:
        y.left = z
    else:
        y.right = z

def tree_delete(root,z):
    
    if z.left == None:
        Transplant(root,z,z.right)
    elif z.right == None:
        Transplant(root,z,z.left)
    else:
        y = tree_minimum(z.right)
        if y.parent != z:
            Transplant(root,y,y.right)
            y.right = z.right
            y.right.parent = y 
        Transplant(root,z,y)
        y.left = z.left
        y.left.parent = y

def Transplant(root,u,v):
    
    if u.parent == None:
        root = v
    elif u == u.parent.left:
        u.parent.left == v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent


# VI ZADATAK
def new_inorder_tree_walk(x, lista):
    if x != None:
        new_inorder_tree_walk(x.left, lista)
        lista.append(x.data.num)
        new_inorder_tree_walk(x.right, lista)  

if __name__ == "__main__":


    # 1. ZADATAK
    d2 = Data(2, chr(2))
    d4 = Data(4, chr(4))
    d5 = Data(5, chr(5))
    d6 = Data(6, chr(6))
    d8 = Data(8, chr(8))

    n2 = Node(d = d2)
    n4 = Node(d = d4)
    n5 = Node(d = d5)
    n6 = Node(d = d6)
    n8 = Node(d = d8)

    addNode(n6, n2)
    addNode(n6, n8)
   
    n2.print_node()
    n4.print_node()
    n5.print_node()
    n6.print_node()
    n8.print_node()

    # 2. ZADATAK
    print("")
    inorder_tree_walk(n6)

    # 3. ZADATAK
    print("")
    print(tree_search(n6, 5))
    print(Iterative_Tree_Search(n6, 2))
    print("")

    # 4. ZADATAK
    print("Minimum = ", tree_minimum(n6).data.num)
    print("")
    print("Maksimum = ", tree_maximum(n6).data.num)
    print("")
    print("After 2 is ", tree_successor(n2).data.num)
    print("")

    # 5. ZADATAK
    tree_insert(n6, n4)
    inorder_tree_walk(n6)
    print("")
    tree_insert(n6, n5)
    inorder_tree_walk(n6)
    print("")
    tree_delete(n6, n5)
    inorder_tree_walk(n6)


    # 6. ZADATAK    
    lista = random.sample(range(1, 20), 10)
    sort_lista = []
    
    data = Data(lista[5], chr(lista[5]))
    root = Node(d = data)

    for i in range(0, len(lista)):
        if i != 5:
            data = Data(lista[i], chr(lista[i]))
            node = Node(d = data)
            tree_insert(root, node)

    print("")
    inorder_tree_walk(root)
    print("")
    new_inorder_tree_walk(root, sort_lista)
    print(sort_lista)

    