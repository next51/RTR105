import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

import sys
import matplotlib.pyplot as plt
import numpy as np

from numpy import *
x = linspace(0, 7, 70)
y = cos(x)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $cos(x)$')
plt.plot(x, y)
plt(show)
