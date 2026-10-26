import numpy as np
def A(q,M,off=0.5):
    ks=(np.arange(M)+off)*2*np.pi/M
    K=np.stack(np.meshgrid(ks,ks,ks,indexing='ij'),-1).reshape(-1,3)
    d1=np.sin(K); d2=np.sin(K+q)
    r1=np.linalg.norm(d1,axis=1); r2=np.linalg.norm(d2,axis=1)
    n1=d1/r1[:,None]; n2=d2/r2[:,None]
    a=(d1+d2)/2
    t1=0.25*(-(n1*d2).sum(1)-r1)
    num=0.5*((a*a).sum(1)*(1+(n1*n2).sum(1))-2*(a*n1).sum(1)*(a*n2).sum(1))
    t2=-num/(r1+r2)
    return (t1+t2).mean()
for M in [48,96,144]:
    h0=2*A(np.zeros(3),M)
    print(M,"e0",h0)
M=96
h0=2*A(np.zeros(3),M)
for qs in [0.05,0.1,0.2,0.4,0.8,1.6,3.14159265]:
    q=np.array([qs,0,0]); hq=2*A(q,M)
    L=2*(1-np.cos(qs))
    print(qs,hq,hq-h0,(hq-h0)/L)
q=np.array([1,1,1])*np.pi
print("Q",2*A(q,M))
