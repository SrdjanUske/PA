import math

class Node:
 
    def __init__(self, l = None, r = None, freq = None):
        self.left = l
        self.right = r
        self.freq = freq

class Data:
    
    def __init__(self, parent, ch, freq):
        self.parent = parent
        self.value = ch
        self.freq = freq
    

def MakeNewElem(left, right, freq):
    node = Node(left, right, freq)
    left.parent = node
    right.parent = node
    return node

def putElem(characters, elem):
    characters.append(elem)

def RemoveElem(characters, elem):
    characters.remove(elem)

def GetMinFreqElem(tree):
    minimum = tree[0]
    for i in range(1, len(tree)):
        if (tree[i].freq < minimum.freq):
            minimum = tree[i]
    return minimum

def get_histogram(input):
    dict = {}
    characters = []
    for i in range(0, len(input)):
        if input[i] in dict:
            dict[input[i]] += 1
        else:
            dict[input[i]] = 1
    
    for letter in dict:
        data = Data(None, letter, dict[letter])
        characters.append(data)

    return characters

def GetEncVal(chars, characters):
    enc = ""
    while not chars in characters:
        if chars.parent.left == chars:
            enc += '0'
        elif chars.parent.right == chars:
            enc += '1'
        chars = chars.parent
    return enc[::-1]


def Huffman(tree):
    
    indx1 = GetMinFreqElem(tree)
    RemoveElem(tree, indx1)
    
    indx2 = GetMinFreqElem(tree)
    RemoveElem(tree, indx2)

    node = MakeNewElem(indx1, indx2, indx1.freq + indx2.freq)
    putElem(tree, node)
        
def test(s):

    # 1)
    print(s)
    characters = get_histogram(s)
    chars = characters[:]

    # 2)
    while len(characters) > 1:
        Huffman(characters)

    # 3)
    for i in chars:
        print(i.value + " -> " + GetEncVal(i, characters))

    print("\n")

if __name__ == "__main__":
    
    input = [['a', 'b'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd'], ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']]
    
    for parts in input:
        test(parts)
   