import math
import numpy as np 
dict1={1:(1,0),2:(2,0),3:(2,3),4:(5,6)}
tuple1=[(1,2),(3,4)]
n = len(dict1) 
adj_mat = [[float('inf')] * n for _ in range(n)]
def adjmat(dict1,tuple1):
    for i in range(0,len(adj_mat)):
        for j in range(0,len(adj_mat)):
            adj_mat[i][j]=math.inf
    for i in tuple1:
        x=dict1[i[0]]
        y=dict1[i[1]]
        x1=x[0]
        y1=x[1]
        x2=y[0]
        y2=y[1]
        dist=(x2-x1)**2+(y2-y1)**2
        dist_sqr=math.sqrt(dist)
        node1=i[0]
        node2=i[1]
        adj_mat[node1-1][node2-1]=dist_sqr
    return adj_mat
print(adjmat(dict1,tuple1))