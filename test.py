# import modules # noqa
import numpy as np
import matplotlib.pyplot as plt


N = 50
p = 0.5
h = np.ones(N)
for i in range(0, int(np.floor(p*(N))/2)):
    h[i] = h[i]*0.5*(1 - np.cos(2*np.pi*(i+1)/(np.floor(p*N)+1)))

for i in range(N - int(np.floor(p*(N))/2), N):
    h[i] = h[i]*0.5*(1 - np.cos(2*np.pi*(N-i)/(np.floor(p*N)+1)))

# calculate the sum of the h[i] when C = 1
sum_h = 0
for i in range(N):
    sum_h += h[i]**2

# find the value of C such that the squared sum is 1
C = 1/np.sqrt(sum_h)

# update the sum
#h = h*C

sum_k = 0
for i in range(N):
    if h[i] == 1:
        sum_k += 1

t = np.linspace(0, N, N)
print(h)
print(sum_k)
#plt.plot(t, h)
plt.show()
