import numpy as np
import matplotlib.pyplot as plt

R = 8.314
Tc = 304.2
pc = 73.83 * (10^5)
b = (R*Tc)/(8 * pc)
a = (27/64)*(((np.power(R, 2))*np.power(Tc, 2))/pc)
T = 278.15

V = np.arange(1.5, 100, 0.1)
p = (R*T)/(V - b) - a/(V * V)

plt.plot(V, p)
plt.ylabel('Pressao (Pa)')
plt.xlabel('Volume (M^3)')
plt.show()