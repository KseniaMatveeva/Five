#Почти периодический сигнал
import numpy as np
import scipy as sp
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
s =[ (np.exp(-(0.07)*t) *np.cos(0.5*t)) for t in range(0, 100)]
plt.plot(s)