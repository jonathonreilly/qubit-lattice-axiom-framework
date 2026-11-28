# GUIDE only (row 1086 check). Monte Carlo / quadrature spot checks of
# DEC2, its U(1) analogue, DEC6, NA1, NA4, P4-LIFT. Not a proof.
import os
os.environ["OPENBLAS_NUM_THREADS"]="1"; os.environ["OMP_NUM_THREADS"]="1"
import numpy as np
from scipy.special import iv
rng=np.random.default_rng(1086)
def haar(n):
    x=rng.standard_normal((n,4)); return x/np.linalg.norm(x,axis=1,keepdims=True)
def qmul(p,q):
    a1,b1,c1,d1=p[...,0],p[...,1],p[...,2],p[...,3]
    a2,b2,c2,d2=q[...,0],q[...,1],q[...,2],q[...,3]
    return np.stack([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2],axis=-1)
def qinv(q): return q*np.array([1,-1,-1,-1])
def omega(s): s=np.asarray(s,float); return np.where(s>1e-12, 2*iv(1,s)/np.maximum(s,1e-300), 1.0)
print("DEC2: MC of int exp(b v.(rho+rho')) dv vs omega(b sqrt(2+2t))")
for b in (0.5,2.0,2.5):
    r=haar(1)[0]; rp=haar(1)[0]; t=r@rp
    acc=0.0; n=0; 
    for _ in range(10):
        v=haar(400000); acc+=np.exp(b*v@(r+rp)).sum(); n+=400000
    print(f"  b={b} t={t:+.4f} MC={acc/n:.5f} omega={float(omega(b*np.sqrt(2+2*t))):.5f}")
print("U(1) analogue: circle average of exp(b v.(rho+rho')) vs I0(2b|cos(d/2)|)")
th=np.linspace(0,2*np.pi,200001)[:-1]
for b,d in ((1.0,0.7),(3.0,2.5)):
    r=np.array([1.0,0.0]); rp=np.array([np.cos(d),np.sin(d)])
    val=np.exp(b*(np.cos(th)*(r[0]+rp[0])+np.sin(th)*(r[1]+rp[1]))).mean()
    print(f"  b={b} d={d} quad={val:.8f} I0={iv(0,2*b*abs(np.cos(d/2))):.8f}")
print("DEC6: V''(-1) by finite differences vs -b^4/48")
for b in (0.7,2.0):
    V=lambda t: np.log(omega(b*np.sqrt(np.maximum(2+2*t,0))))
    h=1e-3; t0=-1+2*h
    # one-sided second difference at t0, then compare near -1
    d2=(V(t0+h)-2*V(t0)+V(t0-h))/h**2
    print(f"  b={b} V''(-1+2e-3)~{float(d2):.6f}  -b^4/48={-b**4/48:.6f}")
print("NA1/NA4: E[y1y2y3y4] and Cov(F,G) under exp(k Re(q1 q2 q3^-1 q4^-1))")
e=np.array([0,1,0,0.0])
def y(q):  # e . R(q) e with R(q)x = q x q^-1, e = i
    a,b_,c,d=q[...,0],q[...,1],q[...,2],q[...,3]
    return a*a+b_*b_-c*c-d*d
for k in (1.0,2.0,4.0):
    W=0.0; S4=0.0; S2=0.0; S3=0.0; SFG=0.0; SF=0.0; SG=0.0
    for _ in range(20):
        N=200000; q=[haar(N) for _ in range(4)]
        H=qmul(qmul(qmul(q[0],q[1]),qinv(q[2])),qinv(q[3]))
        w=np.exp(k*H[:,0]); ys=[y(qq) for qq in q]
        Fv=ys[0]+ys[1]-ys[0]*ys[1]; Gv=ys[2]+ys[3]+ys[2]*ys[3]
        W+=w.sum(); S4+=(w*ys[0]*ys[1]*ys[2]*ys[3]).sum(); S2+=(w*ys[0]*ys[2]).sum()
        S3+=(w*ys[0]*ys[1]*ys[2]).sum(); SFG+=(w*Fv*Gv).sum(); SF+=(w*Fv).sum(); SG+=(w*Gv).sum()
    M=iv(3,k)/(27*iv(1,k))
    cov=SFG/W-(SF/W)*(SG/W)
    print(f"  k={k} MC E[y1y2y3y4]={S4/W:.5f} exact {M:.5f}; E[y1y3]={S2/W:+.5f} E[y1y2y3]={S3/W:+.5f}; Cov(F,G)={cov:+.5f}")
# y check: y(q)=cos(2 alpha) with |z|=cos alpha; also y(q^-1)=y(q)
q=haar(5); print("  y(q)-y(q^-1) max:",float(np.abs(y(q)-y(qinv(q))).max()))
# R(q)e first component equals y: compute q i q^-1
qi=qmul(qmul(q,np.tile(e,(5,1))),qinv(q)); print("  (q i q^-1)_i - y max:",float(np.abs(qi[:,1]-y(q)).max()))
print("P4-LIFT: Re(q1 q2 q3^-1 q4^-1) at (1,i,j,k) and after common left mult by i")
one=np.array([1,0,0,0.]); I=np.array([0,1,0,0.]); J=np.array([0,0,1,0.]); K=np.array([0,0,0,1.])
def re4(a,b_,c,d): return qmul(qmul(qmul(a,b_),qinv(c)),qinv(d))[0]
print("  ", re4(one,I,J,K), re4(qmul(I,one),qmul(I,I),qmul(I,J),qmul(I,K)))
