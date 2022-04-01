import numpy as np

a = np.loadtxt('mat.txt', usecols=range(0,10))

x = np.arange(10)/2.0

for i in range(10):
    for j in range(10):
        a[i,j] = 2.0 + float(i+1)/float(j+i+1)
        
b = np.dot(a, x)
y = np.linalg.solve(a, b)
autoval = np.linalg.eigvals(a)
autovett= np.linalg.eig(a)

print(autoval)
print(autovett)