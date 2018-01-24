# Отобразите апериодический сигнал на графике
import scipy as sp
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import math
from math import  exp
a=15
b=100
c=17
d=100
# c шагом
s=[exp((-(a/b))*t) - exp(-((c/d))*t)for t in range(0,100)]
plt.plot(s)



