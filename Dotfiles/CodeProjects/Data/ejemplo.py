import numpy as np 

l = np.sqrt(25)

a = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10]
b = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10]
print(type(a))

print(type(np.array(a)))

p = np.array([a, b])
print(p)
print(p.shape)