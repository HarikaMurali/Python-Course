import numpy as np
'''a=np.zeros((2,2))
print(a)
b=np.ones((3,3))
print(b)'''

a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a.shape)
print(a[0])
print(a[1])
print(a[1][2])
a[1][2]=25
print(a[1][2])
print(np.count_nonzero(a))
