import numpy as np
print(np.__version__)
print(np.zeros(10))
zeros=np.zeros(10) 
mem_size=zeros.itemsize * zeros.size
print(mem_size)
print(np.info(np.add))
arr = np.zeros(10)
arr(5)=1

