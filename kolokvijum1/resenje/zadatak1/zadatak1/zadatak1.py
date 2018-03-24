
import sys

def GetHistogram(lista):
    dict = {}

    for j in range(0, len(lista)):
        if lista[j] in dict:
            dict[lista[j]] += 1
        else:
            dict[lista[j]] = 1
    
    return dict

if __name__ == "__main__":

    input1 = ['a', 'b']
    print("\n" + str(input1))
    dict1 = GetHistogram(input1)
    print(dict1)

    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    print("\n" + str(input2))
    dict2 = GetHistogram(input2)
    print(dict2)

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    print("\n" + str(input3))
    dict3 = GetHistogram(input3)
    print(dict3)

    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    print("\n" + str(input4))
    dict4 = GetHistogram(input4)
    print(dict4)

    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    print("\n" + str(input5))
    dict5 = GetHistogram(input5)
    print(dict5)
    print("\n")
