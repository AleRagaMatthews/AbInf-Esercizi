import numpy as np
import time

start = time.time()

fx = open("mat1.txt","w")

a=np.identity( n=100, dtype=None )


for i in range(len(a)):
    print('\n', file=fx)
    for j in range(len(a)):
        print(a[i][j], '', file=fx, end='')
         
fx.close()

stop = time.time()

print('Tempo', stop-start)


start = time.time()

fy=open("mat2.txt","w")

n=100
i=0
j=0

a = [range(n) for _ in range(n)]

for i in range(n):
    print('\n', file=fy)
    for j in range(n):
        print(a[i][j], '', file=fy, end='')
        
fy.close()

stop=time.time()

print('Tempo', stop-start)