import numpy as np

a=np.array([1, 2, 3, 4])
b=np.array([10,8, 32, 9])

somma=a+b
print(somma)

molt=a*b
print(molt)

scalprod=np.dot(a, b)
print(scalprod)

m1=np.matrix(a)
m2=np.matrix(b[:,np.newaxis])

moltmatrx=m1*m2
print(moltmatrx)

#Indicizzazione e slicing

a=np.array([[2,4,6],[8,10,12],[14,16,18]])

print(a[0][1], a[2][2], a[1][0])
print(a[:,1])
print(a[0:2, 0:2])
print(a[2, :1])

#Copy by reference

a=np.array([1, 2, 3, 4])
b=a
print(b)

#Copy by value

b=np.zeros_like(a)
b[:] = a[:]

print(b)