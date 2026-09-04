"""
T314 - audit the LAST unaudited flagship number: EH = 1.00000 +- 0.00003.

R196 found tau0 wrong by 5%; R197 found R157's 6.5e-5 error bar ~10x too tight.
R132/R135 claim the induced Einstein-Hilbert coefficient at 1.00000 +- 0.00003.
R189 already confirms the TARGET analytically (b1 = (d-1)/(3d) = 1/4 at d=4,
matching R132's independently measured value). What has never been checked is
the achievable PRECISION of the lattice measurement.

Exact Bloch in d=4 (metric depends on x0 only, so the three transverse momenta
are good quantum numbers: L^3 matrices of size L, no stochastic noise), then
T271's validated 1/s extrapolation. The question is not "is b1 = 1/4" -- that is
settled -- but "how tightly can this measurement pin it", i.e. is +-3e-5 real.
"""
import numpy as np, time
from numpy.polynomial.legendre import leggauss
XS,WS=leggauss(24)
def integ(f,lo,hi):
    lo=np.asarray(lo,float); hi=np.asarray(hi,float)
    q=0.5*(lo+hi)[:,None]+0.5*(hi-lo)[:,None]*XS[None,:]
    return 0.5*(hi-lo)*np.sum(WS[None,:]*f(q),axis=1)
def heat4(L,eps,svals):
    """exact Tr e^{-sB} in d=4 by Bloch decomposition over (q1,q2,q3)"""
    kap=2*np.pi/L; t=np.arange(L,dtype=float)
    W  =lambda x:(1.0+eps*np.cos(kap*x))**1.0      # f^{d/2-1}, d=4
    Rho=lambda x:(1.0+eps*np.cos(kap*x))**2.0      # f^{d/2},   d=4
    w=integ(W,t,t+1.0); v=integ(W,t-0.5,t+0.5); m=integ(Rho,t-0.5,t+0.5)
    idx=np.arange(L); isq=1.0/np.sqrt(m)
    K0=np.zeros((L,L)); K0[idx,idx]=w+np.roll(w,1)
    jp=(idx+1)%L; K0[idx,jp]-=w; K0[jp,idx]-=w
    q=2*np.pi*np.arange(L)/L; c2=2*(1-np.cos(q))
    tot=np.zeros(len(svals))
    for a in range(L):
        for b in range(L):
            for c in range(L):
                K=K0.copy(); K[idx,idx]+=(c2[a]+c2[b]+c2[c])*v
                ev=np.linalg.eigvalsh(K*isq[:,None]*isq[None,:])
                tot+=np.array([np.sum(np.exp(-sv*ev)) for sv in svals])
    return tot, m.sum()*L**3
def R_of(L,xs,h=0.05):
    kap=2*np.pi/L; s=xs/kap**2
    Ks={};Vs={}
    for e in (-2,-1,0,1,2): Ks[e],Vs[e]=heat4(L,e*h,s)
    d2=lambda D:0.5*(-D[2]+16*D[1]-30*D[0]+16*D[-1]-D[-2])/(12*h*h)
    return (4*np.pi*s)**2.0*d2(Ks)/d2(Vs)          # (4 pi s)^{d/2}, d=4
xs=np.array([0.10,0.20,0.35,0.50])
print("d=4 exact Bloch.   target R(x) = 1 + (1/4)x + O(x^2)   [R189: b1=(d-1)/(3d)]\n")
data={}
for L in (16,20,24,32,40):
    t0=time.time(); data[L]=R_of(L,xs)
    print(f"  L={L:3d}  R = "+" ".join(f"{v:9.6f}" for v in data[L])
          +f"   [{time.time()-t0:.0f}s]")
np.save("t314.npy",np.array([data[L] for L in (16,20,24,32,40)]))
print("\n1/s extrapolation at fixed x (T271's validated procedure), by window:")
Ls=[16,20,24,32,40]
for win in ((16,20,24),(20,24,32),(24,32,40)):
    A=[]
    for i,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in win]); rv=np.array([data[L][i] for L in win])
        A.append(np.polyfit(1.0/sv,rv,1)[1])
    A=np.array(A)
    b1=np.polyfit(xs,A-1.0,1)[0]
    print(f"  window {str(win):16s} R_extrap = "+" ".join(f"{v:9.6f}" for v in A))
print("\n  spread across windows at each x  =  the real uncertainty:")
allA=[]
for win in ((16,20,24),(20,24,32),(24,32,40)):
    A=[]
    for i,x in enumerate(xs):
        sv=np.array([x/(2*np.pi/L)**2 for L in win]); rv=np.array([data[L][i] for L in win])
        A.append(np.polyfit(1.0/sv,rv,1)[1])
    allA.append(A)
allA=np.array(allA)
for i,x in enumerate(xs):
    sp=allA[:,i].max()-allA[:,i].min()
    print(f"    x={x:.2f}   spread = {sp:.2e}   relative {sp/allA[:,i].mean():.2e}")
print(f"\n  R132/R135 claim: 1.00000 +- 0.00003  (3e-5)")
