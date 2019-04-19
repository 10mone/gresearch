import math
import matplotlib.pyplot as plt

ff = [[0.0 for _ in range(6)] for _ in range(6)]

n = 4
ti = 0.0
tf = 20000
h = 0.2
xx = [1.0989720, 0.0, 0.0, 0.02048855]

tt = ti

x = [0.0 for _ in range(n)]
f = [0.0 for _ in range(n)]
fm = [0.0 for _ in range(10)]

# output
px = []
py = []
  
def dfeq(f):
    gs = 0.000295912208
    r = math.sqrt(x[0]*x[0] + x[1]*x[1])
    f[0] = x[2]
    f[1] = x[3]
    f[2] = -gs * x[0] / r**3
    f[3] = -gs * x[1] / r**3

def runge_kutta(n, x, ff):
    for j in range(4):
        hh = (j/2) * h/2
        t = tt + hh
        for i in range(n):
            x[i] = xx[i] + f[i]*hh
        dfeq(f)
        for i in range(n):
            ff[i][j] = f[i]
    for i in range(n):
            fm[i] = (ff[i][0] + 2*ff[i][1] + 2*ff[i][2] + ff[i][4]) / 6.0
            #euler
            #fm[i] = ff[i][0]
        
while True:
    if tt > tf:
        break
    
    px.append(xx[0])
    py.append(xx[1])

    runge_kutta(n, x, ff)
    for i in range(n):
        xx[i] = xx[i] + fm[i]*h
    tt = tt + h


plt.figure(figsize=(15, 15), dpi=100)
ax=plt.subplot()
ax.plot(px, py)
ax.set_xlim(-6.0, 4.0)
ax.set_ylim(-5.0, 5.0)
plt.show()