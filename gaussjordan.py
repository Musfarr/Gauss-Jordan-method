import numpy as np

n = int(input("enter no of eq\n"))
col = []

for i in range(n):
    row = []
    for j in range(0,n+1):
        print("enter A",i,j)
        t = float(input("enter element"))
        row.append(t)
    col.append(row)

A = np.matrix(col)
print("The matrix is \n")
print(A)

for i in range(n):
    for j in range(n):
        A[i,:] = A[i,:]/A[i,i]
        if i != j:
            factor = A[j,i]/A[i,i]
            for k in range(n+1):
                A[j,k]=A[j,k]-factor*A[i,k]

print("augmented matrix\n")
print(A)

print("the values of variable are \n")
print(A[:,n])




