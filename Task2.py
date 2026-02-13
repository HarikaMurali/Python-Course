import numpy as np
a=np.zeros((10,10), dtype=object)
a[0][0]="B"
a[1][2]="B"
a[4][4]="B"
a[7][3]="B"
a[9][7]="B"
count=np.sum(a[2]=="B")
print("The number of seats in 3rd row=",count)

