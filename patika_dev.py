"""

1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]

"""

input = [['selam'], 12,'3',['ada']]

output = list()

def flatten(y):
    for x in y:
        if isinstance(x,list):
            flatten(x)
        else:
            output.append(x)

flatten(input)
print(output)

"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]

"""

input = [[1, 2], [3, 4], [5, 6, 7]]


def reverse_func(input):
    for x in range(len(input)):
        input[x] = input[x][::-1]
    for x in range(0,len(input),1):
        for y in range(0,len(input)-1,1):
            if input[y] > input[y]:
                input[y+1],input[y] = input[y],input[y+1]        
    input.reverse()
    print(input)


reverse_func(input=input)