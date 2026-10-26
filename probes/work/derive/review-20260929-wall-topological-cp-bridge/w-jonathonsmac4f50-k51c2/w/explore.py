import numpy as np, sys
def build(L,Q):
    N=L*L
    idx=lambda x,y:(x%L)*L+(y%L)
    phi=2*np.pi*Q/L**2
    def U1(x,y): return np.exp(-1j*phi*L*y) if x==L-1 else 1.0
    def U2(x,y): return np.exp(1j*phi*x)
    T1=np.zeros((N,N),complex);T2=np.zeros((N,N),complex)
    for x in range(L):
        for y in range(L):
            T1[idx(x,y),idx(x+1,y)]=U1(x,y)   # (T psi)(x)=U psi(x+mu)
            T2[idx(x,y),idx(x,y+1)]=U2(x,y)
    eta2=np.diag([(-1)**x for x in range(L) for y in range(L)]).astype(complex)
    eps=np.diag([(-1)**(x+y) for x in range(L) for y in range(L)]).astype(complex)
    D=0.5*((T1-T1.conj().T)+eta2@(T2-T2.conj().T))
    C1=(T1+T1.conj().T)/2;C2=(T2+T2.conj().T)/2
    S=(C1@C2+C2@C1)/2
    G=1j*eta2@S
    return D,G,eps,T1,T2
for L in (4,6,8,12):
  for Q in (0,1,2,3,-1):
    D,G,eps,T1,T2=build(L,Q)
    assert np.allclose(D.conj().T,-D)
    w,v=np.linalg.eigh(1j*D)
    z=np.abs(w)<1e-9
    n0=z.sum()
    P=v[:,z]
    g=np.trace(P.conj().T@G@P).real if n0 else 0
    # plaquette flux
    print(L,Q,'n0',n0,'trGP',round(g,6),'1-g/n0', (1-g/n0) if n0 else None, 'comm',round(np.linalg.norm(G@D+D@G),4), 'eps-comm',np.linalg.norm(eps@G-G@eps))
