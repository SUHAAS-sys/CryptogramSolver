# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.
# Leave in code under testing, comment out code if needed for later
# reference, or delete code that is no longer wanted.
import numpy as qw






A=('pineapple apple pi lime ')
print(A,type(A))

B=A.split()
print(B,type(B))
C=qw.array(B)
print(C,type(C))
D=sorted(C,key=len)
print(D,type(D))
print(D[2])
print(len(D[0]),len(D[2]),type(len(D[0])))
def split(G):
    return [char for char in G]
G=("suhas is in home ?")

print(split(G),type(G))

T=('suhas ms is at home ')
print(T,type(T))
Y=T.split()
print(Y,type(Y))
I=qw.array(Y)
print(I,type(I))
arr=qw.array_split(I,5)
print(arr)


original_list = ['g', 'fytc', 'y', 'bmg']
length_sorted_list = []
dictionary_memory = {}


def sort_list_by_length():
    temp_list = []
    global original_list
    for i in range(0, len(original_list)):
        temp_list.insert(i, sorted(original_list, key=len)[i])
    return temp_list


def dictionary_builder(original, compare):
    for original_element in original:
        for compare_element in compare:
            dictionary_memory[original_element] = compare_element
            compare.remove(compare_element)
            break


if __name__ == '__main__':
    print(original_list)
    length_sorted_list = sort_list_by_length().copy()
    print(length_sorted_list)
    dictionary_builder(original_list, length_sorted_list)
    # print(original_list)
    # print(length_sorted_list)
    print(str(dictionary_memory))