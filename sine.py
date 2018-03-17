# -*- coding: utf-8 -*-
"""
Spyder Editor

plot sine wave [-pi, pi] with pyqtgraph
"""
import pyqtgraph as pg
import numpy as np
from numpy import fft
x = np.linspace(-np.pi, np.pi, 201)
y = np.sin(x)
fy = fft.fft(y)
pg.plot(x,y,pen='g')
"pg.plot(x,fy,pen='g')"
