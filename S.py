
# Отобразите полигармонический сигнал на графике
import scipy as sp
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import math
from math import cos
A=2
B=1
w=0.1
C=3
# c шагом
s =[(A*cos(w*t)+B*cos(2*w*t+2)+C*cos(4*w*t+4)) for t in range(0, 200)]
plt.plot(s)

