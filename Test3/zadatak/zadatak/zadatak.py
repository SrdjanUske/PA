
oper = ['+', '-', '*', '/']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Node:
    def __init__(self, parent = None, left = None, right = None, value = None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value

def operation(oper1, oper2, operator):
    if operator == '+':
        return oper1 + oper2
    elif operator == '-':
        return oper1 - oper2
    elif operator == '*':
        return oper1 * oper2
    elif operator == '/':
        return oper1 / oper2
    else:
        print("Unsupported operation!")
        return None


def eval_tree(tree, dictionary):
    s = 0
    if tree.left == None and tree.right == None:
        for i in range(0, len(tree.value)):
            if tree.value[i] not in nums:
                return float(dictionary[tree.value])
        return float(tree.value)
    else:
        left = eval_tree(tree.left, dictionary)
        right = eval_tree(tree.right, dictionary)
        if tree.value in oper:
            s = operation(left, right, tree.value)
            #print(s)
        return s

def make_infix(tree):
    s = ""
    if tree.left == None and tree.right == None:
        return str(tree.value)
    else:
        s += "("
        s += make_infix(tree.left)
        if tree.value in oper:
            s = s + " " + str(tree.value) + " " 
        s += make_infix(tree.right)
        s += ")"
        return s

def get_parse_tree(s):
    global oper
    l = s.split()
    print(l)
    stack = []
    for x in l:
        n = Node(value = x)
        if x in oper:
            right = stack.pop(-1)
            left = stack.pop(-1)
            n.left = left
            n.right = right
            left.parent = n
            right.parent = n
        stack.append(n)
    return stack[0]

def test(s):
    list = s[0]
    dict = s[1]
    tree = get_parse_tree(list)
    #print(tree.value)
    print("MAKE_INFIX RETURNS: " + make_infix(tree))
    print("EVAL_TREE RETURNS: " + str(eval_tree(tree, dict)))

if __name__ == "__main__":
    for s in [["23 45 67 + -", None], ["a 5 + b c 3 / - *", {'a': 34, 'b': 65, 'c': 3}], ["vel_0 time * g time * time 2 / * +", {'vel_0': -10, 'time': 20, 'g': 9.81}]]:
        test(s)