#runge-kutta
import math
import matplotlib.pyplot as plt

def trans(t, xx, q, r, ind):
    p = [0.0 for _ in range(5)]
    i = 0
    if ind==4:
        i = 4
        
    for j in range(1, 5):
        p[j] = xx[i+j] - q[j]
        xx[j+4] = xx[j+4-i]
    
    xx[1] = math.sqrt(abs(r+p[1]) / 2.0)
    xx[2] = math.sqrt(abs(r-p[1]) / 2.0)
    if p[2]<0.0:
        xx[2] = -xx[2]
    xx[3] = (xx[1]*p[3] + xx[2]*p[4]) / 2.0
    xx[4] = (xx[1]*p[4] - xx[2]*p[3]) / 2.0
    xx[9] = t

def invers(xx, yy, r, ind):
    p = [0.0 for _ in range(5)]
    pro_q = [0.0 for _ in range(5)]
        
    p[1] = xx[1]*xx[1] - xx[2]*xx[2]
    p[2] = 2*xx[1]*xx[2]
    p[3] = 2 * (xx[1]*xx[3] - xx[2]*xx[4]) / r
    p[4] = 2 * (xx[2]*xx[3] + xx[1]*xx[4]) / r
    if ind==3:
        i = 0
        si = 3.0
        sj = 4.0
    else:
        i = 4
        si = 4.0
        sj = 3.0
    for j in range(1, 5):
        pro_q[j] = -(sj*xx[4+j] + si*p[j]) / (si+5)
    for  j in range(1, 5):
        yy[j+4-i] = xx[j+4]
        yy[i+j] = p[j] + pro_q[j]
    yy[9] = xx[9]
    
def extra(n, h, a, xx, ind):
    y = [[0.0 for _ in range(10)] for _ in range(4)]
    x = [0.0 for _ in range(10)]
    f = [0.0 for _ in range(10)]
    for i in range(1, 8):
        ns = 2**i
        hs = h/ns
        for k in range(1, n+1):
            y[2][k] = xx[k]
            x[k] = xx[k]    
        dfeq(n, x, f, ind)
        for k in range(1, n+1):
            y[3][k] = y[2][k] + f[k] * hs
        for j in range(1, ns+1):
            for k in range(1, n+1):
                y[1][k] = y[2][k]
                y[2][k] = y[3][k]
                x[k] = y[3][k]
            dfeq(n, x, f, ind)
            for k in range(1, n+1):
                y[3][k] = y[1][k] + 2 * hs * f[k]
        for k in range(1, n+1):
            a[i][1][k] = (y[1][k]+2*y[2][k]+y[3][k]) / 4.0
            #euler
            #a[i][1][k] = y[1][k]

def nevil(n, a, xx):
    for k in range(1, n+1):
        for i in range(2, 8):
            for j in range(2, i+1):
                j1 = j-1
                a[i][j][k] = a[i][j1][k] + (a[i][j1][k] - a[i-1][j1][k]) / (4**(j1)-1)
    for k in range(1, n+1):
        xx[k] = a[7][7][k]
    
def dfeq(n, x, f, ind):
    if ind<0:
        r12 = math.sqrt((x[1]-x[5])**2 + (x[2]-x[6])**2)
        r13 = math.sqrt((8*x[1]+4*x[5])**2 + (8*x[2]+4*x[6])**2) / 5.0
        r23 = math.sqrt((3*x[1]+9*x[5])**2 + (3*x[2]+9*x[6])**2) / 5.0
        f[1] = x[3]
        f[2] = x[4]
        f[3] = -4 * (x[1]-x[5]) / r12**3 - (8*x[1]+4*x[5]) / r13**3
        f[4] = -4 * (x[2]-x[6]) / r12**3 - (8*x[2]+4*x[6]) / r13**3
        f[5] = x[7]
        f[6] = x[8]
        f[7] = 3 * (x[1]-x[5]) / r12**3 - (3*x[1]+9*x[5]) / r23**3
        f[8] = 3 * (x[2]-x[6]) / r12**3 - (3*x[2]+9*x[6]) / r23**3
        return
        
    elif ind==3:
        si = 3.0
        sj = 4.0
    else:
        si = 4.0
        sj = 3.0

    s = si+5
    xr = x[1]*x[1] - x[2]*x[2]
    yr = 2*x[1]*x[2]
    xij = (12*x[5]-5*xr) / s
    yij = (12*x[6]-5*yr) / s
    xjk = (12*x[5]+si*xr) / s
    yjk = (12*x[6]+si*yr) / s
    r = x[1]*x[1] + x[2]*x[2]
    rij = math.sqrt(xij*xij + yij*yij)
    rjk = math.sqrt(xjk*xjk + yjk*yjk)
    e0 = s * (-76.9/6 - 6*sj*(x[7]*x[7]+x[8]*x[8])/s + si*sj/rij+5*sj/rjk) / (10*si)
    e1 = 6*sj*r*(1/rij**3 - 1/rjk**3)/s
    e2 = sj*r*r*(5/rij**3 + si/rjk**3) / (2*s)
    e3 = 12*(si/rij**3 + 5/rjk**3) / s
    e4 = 5*si*(1/rij**3 - 1/rjk**3) / s
    f[1] = x[3]
    f[2] = x[4]
    f[3] = e0*x[1]+e1*(x[1]*x[5]+x[2]*x[6])-e2*x[1]
    f[4] = e0*x[2]+e1*(x[1]*x[6]-x[2]*x[5])-e2*x[2]
    f[5] = x[7] * r
    f[6] = x[8] * r
    f[7] = (-e3*x[5]+e4*xr)*r
    f[8] = (-e3*x[6]+e4*yr)*r
    f[9] = r
    

#-------------‚±‚±‚©‚çmain-------------#

n = 8
ti = 0.0
tf = 70.5
hh = 1.0/32

xx = [0.0, 1.0, 3.0, 0.0, 0.0, -2.0, -1.0, 0.0, 0.0, 0.0]
yy = [0.0 for _ in range(10)]
q = [0.0 for _ in range(5)]
a = [[[0.0 for _ in range(10)] for _ in range(8)] for _ in range(8)]

rr = 0.4
t = ti
h = hh
ind = -5
r = 0.0    

px1 = []    
py1 = []
px2 = []
py2 = []
px3 = []
py3 = []
    
while t<=tf:
    for i in range(1,5):
        q[i]=-(3*xx[i] + 4*xx[i+4])/5
        
    #print("\"%f\"" % xx[9],":",{ 'm1':{'x': "%f" % xx[1], 'y': "%f" % xx[2]},'m2':{'x': "%f" % xx[5], 'y': "%f" % xx[6]},'m3':{'x':"%f" % q[1], 'y':"%f" % q[2]}},",")
    px1.append(xx[1])
    py1.append(xx[2])
    px2.append(xx[5])
    py2.append(xx[6])
    px3.append(q[1])
    py3.append(q[2])
        
    r3=math.sqrt((xx[1]-q[1])**2+(xx[2]-q[2])**2)
    r4=math.sqrt((xx[5]-q[1])**2+(xx[6]-q[2])**2)

    if r3>rr or r4>rr:
        n=n+1
        if r4>r3:
            r = r3
            ind = 3
        else:
            r = r4
            ind = 4
        trans(t,xx,q,r,ind)
        h=hh*2
        while r<rr:
            extra(n,h,a,xx,ind)
            nevil(n,a,xx)
            r=xx[1]*xx[1]+xx[2]*xx[2]
            invers(xx,yy,r,ind)
            for i in range(1,5):
                q[i]=-(3*yy[i]+4*yy[i+4])/5
                
            #print("\"%f\"" % yy[9],":",{ 'm1':{'x': "%f" % yy[1], 'y': "%f" % yy[2]},'m2':{'x': "%f" % yy[5], 'y': "%f" % yy[6]},'m3':{'x':"%f" % q[1], 'y':"%f" % q[2]}},",")
            px1.append(yy[1])
            py1.append(yy[2])
            px2.append(yy[5])
            py2.append(yy[6])
            px3.append(q[1])
            py3.append(q[2])
                
        else:
            invers(xx,yy,r,ind)
        for i in range(1,10):
            xx[i] = yy[i]
        t = yy[9]
        h = hh
        ind = -5
        n = n-1
    extra(n,h,a,xx,ind)
    nevil(n,a,xx)
    t=t+h
      

plt.figure(figsize=(10, 10), dpi=100)
ax=plt.subplot()
ax.plot(px1, py1, px2, py2, px3, py3)
ax.set_xlim(-4.0, 4.0)
ax.set_ylim(-3.0, 5.0)
plt.show()
