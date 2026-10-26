import numpy as np, time
def F(qx,qy,qz,P,mu):
    Om=np.sqrt(mu**2+4*(np.sin(qx/2)**2+np.sin(qy/2)**2+np.sin(qz/2)**2))
    sx=-np.sin(qx); sy=-np.sin(qy); sz=np.sin(P-qz)
    ek=np.sqrt(sx*sx+sy*sy+sz*sz)
    c=sz/ek
    ep=np.sin(P)
    return (1/(2*Om))*(ep-c*(ek+Om))/(ep**2-(ek+Om)**2)
def smooth(x):
    return x**3*(10-15*x+6*x**2), 30*x**2*(1-x)**2
def dE(P,mu,N):
    xg,wg=np.polynomial.legendre.leggauss(N); x=(xg+1)/2; w=wg/2
    t,dt=smooth(x); qa=np.pi*t; Wa=np.pi*w*dt
    QX,QY=np.meshgrid(qa,qa,indexing='ij'); W=np.outer(Wa,Wa)
    tot=0.0
    for s in (1,-1):
        for iz in range(N):
            tot+=Wa[iz]*np.sum(W*F(QX,QY,s*qa[iz],P,mu))
    return 4*tot/(2*np.pi)**3
if __name__=="__main__":
    for P in [0.4,0.2,0.1]:
        for N in [100,200,300]:
            t0=time.time(); v=dE(P,0.0,N)/np.sin(P); print(P,N,v,round(time.time()-t0,1),flush=True)
