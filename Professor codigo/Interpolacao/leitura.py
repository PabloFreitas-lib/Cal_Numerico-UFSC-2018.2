import numpy as np

nome="dados.txt"

M = np.loadtxt(nome, dtype='float', comments='#')
print(M)

x,z = np.loadtxt(nome, dtype='float', comments='#', usecols=(0, 2), unpack=True)
print(x)
print(z)

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
