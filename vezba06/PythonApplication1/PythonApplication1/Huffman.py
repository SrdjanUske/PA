import math

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None, val = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d
        if self.left != None:
            self.val = self.left.data.freq + self.right.data.freq
        else:
            self.val = 0

    def print_node(self):
        #print("Parent = ", self.parent)
        #print("Left = ", self.left)
        #print("Right = ", self.right)
        print("Data -> value = " , self.data.value)
        print("freq = ", self.data.freq)

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.value = val1
        self.freq = val2
    

def MakeNewElem(value, freq):
    return Data(value, freq)

def putElem(freq = None, data = None, parent = None, before = None, end = None):
    return Node(l = end, r = before, val = freq, p = parent, d = data)
    
def RemoveElem(list, position):
    list[position] = None

def GetMinFreqElem(tree):
    min = math.inf
    index = -1
    for i in range(0, len(tree)):
        
        if (tree[i] != None):
            if (tree[i].left != None and tree[i].right != None):
                if (tree[i].val < min):
                    min = tree[i].val
                    index = i
            else:
                if (tree[i].data.freq < min):
                    min = tree[i].data.freq
                    index = i
    return index

def get_histogram(dict, input):
    for i in range(0, len(input)):
        if input[i] in dict:
            dict[input[i]] += 1
        else:
            dict[input[i]] = 1

def Huffman(tree):
    
    freq_end1 = GetMinFreqElem(tree)
    RemoveElem(tree, freq_end1)
    
    freq_bef_end1 = GetMinFreqElem(tree)
    RemoveElem(tree, freq_bef_end1)

    sum = tree[freq_end1].data.freq + tree[freq_bef_end1].data.freq
    nodeNew = putElem(sum, tree[freq_bef_end1], tree[freq_end1])
    tree.append(nodeNew)
        

if __name__ == "__main__":
    

    # 1)
    input1 = ['a', 'b']
    dict1 = {}
    get_histogram(dict1, input1)
    print(dict1)

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    dict2 = {}
    get_histogram(dict2, input2)
    print(dict2)

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    dict3 = {}
    get_histogram(dict3, input3)
    print(dict3)

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    dict4 = {}
    get_histogram(dict4, input4)
    print(dict4)

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    dict5 = {}
    get_histogram(dict5, input5)
    print(dict5)

    #2)
    list_nodes1 = []
    for value, freq in dict1.items():
        data = MakeNewElem(value, freq)
        list_nodes1.append(putElem(data))

    #for i in range(0, len(list_nodes1)):
      #  list_nodes1[i].print_node()
    
    list_nodes2 = []
    for value, freq in dict2.items():
        data = MakeNewElem(value, freq)
        list_nodes2.append(putElem(data))

   #for i in range(0, len(list_nodes2)):
     #   list_nodes2[i].print_node()
    
    list_nodes3 = []
    for value, freq in dict3.items():
        data = MakeNewElem(value, freq)
        list_nodes3.append(putElem(data))

    #for i in range(0, len(list_nodes3)):
        #list_nodes3[i].print_node()
    
    list_nodes4 = []
    for value, freq in dict4.items():
        data = MakeNewElem(value, freq)
        list_nodes4.append(putElem(data))

    #for i in range(0, len(list_nodes4)):
       #list_nodes4[i].print_node()
    
    list_nodes5 = []
    for value, freq in dict5.items():
        data = MakeNewElem(value, freq)
        list_nodes5.append(putElem(data))

    #for i in range(0, len(list_nodes5)):
       # list_nodes5[i].print_node()

    while len(list_nodes1) != 1:
        Huffman(list_nodes1)
    
    
    
    
     