import numpy as np

MAX_SIZE = 1000

a = np.random.randint(100, size=MAX_SIZE)
number_lst = []

for i in range(MAX_SIZE):
        number_lst.append(i)

for i in range(MAX_SIZE):
    if a[i] % 2 == 0:
        number_lst.append(i)
