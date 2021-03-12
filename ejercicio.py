import matplotlib.pyplot as mtp
import numpy as np

x = np.linspace(-50,50,1000000)
y = x**2
mtp.plot(x,y)
mtp.show()