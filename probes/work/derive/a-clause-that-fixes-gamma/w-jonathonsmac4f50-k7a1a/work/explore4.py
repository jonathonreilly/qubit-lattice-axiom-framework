import numpy as np
M=64
ks=(np.arange(M)+0.5)*2*np.pi/M
K=np.stack(np.meshgrid(ks,ks,ks,indexing='ij'),-1).reshape(-1,3)
d1=np.sin(K); r1=np.linalg.norm(d1,axis=1); n1=d1/r1[:,None]
rbar=r1.mean(); print("rbar",rbar, "kappa",rbar/12, "gamma",12/rbar)
def parts(q):
    d2=np.sin(K+q); r2=np.linalg.norm(d2,axis=1); n2=d2/r2[:,None]
    a=(d1+d2)/2
    t1=0.25*(-(n1*d2).sum(1)-r1)
    num=0.5*((a*a).sum(1)*(1+(n1*n2).sum(1))-2*(a*n1).sum(1)*(a*n2).sum(1))
    t2=-num/(r1+r2)
    Rint=(r2-r1)**2*(1-(n1*n2).sum(1))/(4*(r1+r2))
    h=2*(t1+t2).mean()
    L=(2*(1-np.cos(q))).sum()
    return h, -rbar*(1-L/12), 2*t2.mean(), -2*Rint.mean()*0.5*2/2, L   # placeholders
rng=np.random.default_rng(1)
worst=1e9
for q in [np.array(x)*np.pi/8 for x in [(1,0,0),(2,0,0),(4,0,0),(8,0,0),(4,4,0),(8,8,0),(8,8,8),(3,5,7),(1,1,1),(8,4,2),(6,6,6)]]:
    d2=np.sin(K+q); r2=np.linalg.norm(d2,axis=1); n2=d2/r2[:,None]
    a=(d1+d2)/2
    t1=0.25*(-(n1*d2).sum(1)-r1)
    num=0.5*((a*a).sum(1)*(1+(n1*n2).sum(1))-2*(a*n1).sum(1)*(a*n2).sum(1))
    t2=-num/(r1+r2)
    Rint=(r2-r1)**2*(1-(n1*n2).sum(1))/(8*(r1+r2))   # t2 should equal -this
    L=(2*(1-np.cos(q))).sum()
    h=2*(t1+t2).mean(); T1=-rbar*(1-L/12); R=2*Rint.mean()
    print((q/np.pi*8).astype(int), "h",round(h,6),"T1",round(T1,6),"t2 err",np.abs(t2+Rint).max(),"R",round(R,6),"hNO",round(h+rbar,6),"kL",round(rbar*L/12,6), "ratio", round((h+rbar)/(rbar*L/12),5))
