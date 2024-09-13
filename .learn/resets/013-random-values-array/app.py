import numpy as np
print(np.__version__)
print(np.zeros(10))
zeros=np.zeros(10) 
mem_size=zeros.itemsize * zeros.size
print(mem_size)
print(np.info(np.add))
arr = np.zeros(10)
arr[4]=1
print(arr)
arr=np.arange(10,50)
print(arr)
vector=np.arange(10)
vector_invertido=vector[::-1]
print(vector_invertido)
import numpy as np
arr=np.arange(0,9)
matriz= np.reshape(arr,(3,3))
print(matriz)
arr = np.array([1,2,0,0,4,0])
print(np.nonzero(arr))
matriz=np.eye(3,3)
print(matriz)
variable=arr
arr=np.random.random(size=None)
print(arr)