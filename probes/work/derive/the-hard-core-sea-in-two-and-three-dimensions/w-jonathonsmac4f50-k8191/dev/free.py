import numpy as np
from lib import *
n,bonds=torus_bonds((4,4))
def Eneg(eps,q):
    h=np.zeros((16,16))
    for (a,b,j,t,c) in bonds:
        c2=list(c); c2[j]+=1
        al=(np.cos(np.pi/2*(q[0]*c[0]+q[1]*c[1]))+np.cos(np.pi/2*(q[0]*c2[0]+q[1]*c2[1])))/2
        w=np.exp(eps*al)
        h[a,b]+=t*w; h[b,a]+=t*w
    ev=np.linalg.eigvalsh(h)
    return 2*ev[ev<0].sum(), ev
print("free E0",Eneg(0,(1,0))[0])
for q in [(1,0),(2,0),(1,1),(2,1),(2,2)]:
    for e in (0.02,0.01,0.005):
        Ep=Eneg(e,q)[0];Em=Eneg(-e,q)[0];E0=Eneg(0,q)[0]
        print(q,e,"Pi_free=",(Ep+Em-2*E0)/(2*e*e)/16, " odd:",(Ep-Em)/(2*e))
