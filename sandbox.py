# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.
# Leave in code under testing, comment out code if needed for later
# reference, or delete code that is no longer wanted.
import numpy as qw






A=('pineapple apple rat kk arti ')
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
G=("suhas is in home")

print(split(G),type(G))




T=('suhas ms is at home ')
print(T,type(T))

Y=T.split()
print(Y,type(Y))

I=qw.array(Y)
print(I,type(I))

arr=qw.array_split(I,5)

print(arr)


