import math
import matplotlib.pyplot as plt

m1 = 0.7
m2 = 0.3

dt = 0.1
tmax = 100.0

x1 = 0.5
y1 = 0.0
x2 = 0.0
y2 = 1.0


k0 = [0.0 for _ in range(4)]
k1 = [0.0 for _ in range(4)]
k2 = [0.0 for _ in range(4)]
k3 = [0.0 for _ in range(4)]

def f1(x1, y1, x2, y2):
    a = x2
    return a
def f2(x1, y1, x2, y2):
    a = y2
    return a
def f3(x1, y1, x2, y2):
    a = 2*y2+x1+(-m1*(x1-m2)/((pow((x1-m2)*(x1-m2)+y1*y1,1.5)))-m2*(x1+m1)/(pow((x1+m1)*(x1+m1)+y1*y1,1.5)))
    return a
def f4(x1, y1, x2, y2):
    a = -2*x2+y1+(-m1*y1/(pow((x1-m2)*(x1-m2)+y1*y1,1.5))-m2*y1/(pow((x1+m1)*(x1+m1)+y1*y1,1.5)))
    return a

px1 = []
py1 = []
px2 = []
py2 = []

#ƒ‹ƒ“ƒQƒNƒbƒ^
t = 0.0
while True:
    k0[0]=dt*f1(x1,y1,x2,y2)
    k0[1]=dt*f2(x1,y1,x2,y2)
    k0[2]=dt*f3(x1,y1,x2,y2)
    k0[3]=dt*f4(x1,y1,x2,y2)

    k1[0]=dt*f1(x1+k0[0]/2.0,y1+k0[1]/2.0,x2+k0[2]/2.0,y2+k0[3]/2.0)
    k1[1]=dt*f2(x1+k0[0]/2.0,y1+k0[1]/2.0,x2+k0[2]/2.0,y2+k0[3]/2.0)
    k1[2]=dt*f3(x1+k0[0]/2.0,y1+k0[1]/2.0,x2+k0[2]/2.0,y2+k0[3]/2.0)
    k1[3]=dt*f4(x1+k0[0]/2.0,y1+k0[1]/2.0,x2+k0[2]/2.0,y2+k0[3]/2.0)

    k2[0]=dt*f1(x1+k1[0]/2.0,y1+k1[1]/2.0,x2+k1[2]/2.0,y2+k1[3]/2.0)
    k2[1]=dt*f2(x1+k1[0]/2.0,y1+k1[1]/2.0,x2+k1[2]/2.0,y2+k1[3]/2.0)
    k2[2]=dt*f3(x1+k1[0]/2.0,y1+k1[1]/2.0,x2+k1[2]/2.0,y2+k1[3]/2.0)
    k2[3]=dt*f4(x1+k1[0]/2.0,y1+k1[1]/2.0,x2+k1[2]/2.0,y2+k1[3]/2.0)

    k3[0]=dt*f1(x1+k2[0],y1+k2[1],x2+k2[2],y2+k2[3])
    k3[1]=dt*f2(x1+k2[0],y1+k2[1],x2+k2[2],y2+k2[3])
    k3[2]=dt*f3(x1+k2[0],y1+k2[1],x2+k2[2],y2+k2[3])
    k3[3]=dt*f4(x1+k2[0],y1+k2[1],x2+k2[2],y2+k2[3])

    x1=x1+(k0[0]+2.0*k1[0]+2.0*k2[0]+k3[0])/6.0
    y1=y1+(k0[1]+2.0*k1[1]+2.0*k2[1]+k3[1])/6.0
    x2=x2+(k0[2]+2.0*k1[2]+2.0*k2[2]+k3[2])/6.0
    y2=y2+(k0[3]+2.0*k1[3]+2.0*k2[3]+k3[3])/6.0
    px1.append(x1)
    py1.append(y1)
    px2.append(x2)
    py2.append(y2)
    t += dt
    if t > tmax:
        break
        
plt.plot(px1, py1, px2, py2)

plt.show()