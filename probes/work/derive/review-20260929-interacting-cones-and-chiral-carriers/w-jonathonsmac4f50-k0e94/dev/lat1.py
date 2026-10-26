import numpy as np, sympy as sp
qx,qy,qz,P,mu=sp.symbols('qx qy qz P mu',real=True)
Om=sp.sqrt(mu**2+4*(sp.sin(qx/2)**2+sp.sin(qy/2)**2+sp.sin(qz/2)**2))
sk=sp.Matrix([-sp.sin(qx),-sp.sin(qy),sp.sin(P-qz)])
# p = P zhat: s(p-q): x comp sin(0-qx)
ek=sp.sqrt(sk.dot(sk))
ep=sp.sin(P)
c=sk[2]/ek
F=(1/(2*Om))*(ep-c*(ek+Om))/(ep**2-(ek+Om)**2)
dF=sp.diff(F,P).subs(P,0)
f0=sp.lambdify((qx,qy,qz,mu),sp.simplify(F.subs(P,0)),'numpy')
f1=sp.lambdify((qx,qy,qz,mu),dF,'numpy')
import pickle
def smooth(x):  # map [0,1]->[0,1]
    t=x**3*(10-15*x+6*x**2); dt=30*x**2*(1-x)**2
    return t,dt
def integrate(mu_,N):
    xg,wg=np.polynomial.legendre.leggauss(N)
    x=(xg+1)/2; w=wg/2
    t,dt=smooth(x); W=w*dt
    # q_x,q_y in [0,pi] (x4 symmetry), q_z in [-pi,pi] -> two halves
    qa=np.pi*t; Wa=np.pi*W
    tot=0.0; tot0=0.0
    QX,QY=np.meshgrid(qa,qa,indexing='ij'); WXY=np.outer(Wa,Wa)
    for sz in (1,-1):
        for iz in range(N):
            Z=sz*qa[iz]; wz=Wa[iz]
            v=f1(QX,QY,Z,mu_)
            tot+=wz*np.sum(WXY*v)
            tot0+=wz*np.sum(WXY*f0(QX,QY,Z,mu_))
    pref=4/(2*np.pi)**3
    return pref*tot, pref*tot0
if __name__=="__main__":
    import sys
    for mu_ in [1.0,0.5]:
        for N in [40,80,120]:
            print(mu_,N,integrate(mu_,N),flush=True)
