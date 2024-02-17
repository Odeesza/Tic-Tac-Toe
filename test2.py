import numpy as np

arr = np.arange(42).reshape((6,7))
print(arr,"\n")

arr2 = np.fliplr(arr).diagonal(1)#de -2 à 3

print(arr2)

d1 = np.diag(arr,3) #de -2 à 3
print(d1)