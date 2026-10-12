# Supervisor check, done in momentum space on the 2^d unit cell.
# H = sum_mu eta_mu(x) (i/2)(psi_x^dag psi_{x+mu} - h.c.); unit cell = hypercube {0,1}^d.
import numpy as np, itertools
def cell_ops(d):
    C=list(itertools.product((0,1),repeat=d)); ci={c:i for i,c in enumerate(C)}; n=len(C)
    def eta(mu,x): return (-1)**sum(x[:mu])
    def Hk(k):
        H=np.zeros((n,n),complex)
        for c in C:
            for mu in range(d):
                y=list(c); y[mu]+=1; wrap=y[mu]//2; y[mu]%=2
                amp=0.5j*eta(mu,c)*np.exp(2j*k[mu]*wrap)   # cell = 2 sites, Bloch phase per cell crossing
                H[ci[c],ci[tuple(y)]]+=amp; H[ci[tuple(y)],ci[c]]+=np.conj(amp)
        return H
    def Tk(mu,k):  # unit shift x->x+mu with frame zeta_mu(x)=(-1)^{x_{mu+1}+..}
        T=np.zeros((n,n),complex)
        for c in C:
            y=list(c); y[mu]+=1; wrap=y[mu]//2; y[mu]%=2
            T[ci[tuple(y)],ci[c]]=(-1)**sum(c[mu+1:])*np.exp(-2j*k[mu]*wrap)
        return T
    return n,Hk,Tk
for d in (3,4):
    n,Hk,Tk=cell_ops(d); k0=np.zeros(d); h=1e-6
    H0=Hk(k0); print(f"d={d}: |H(0)|={np.abs(H0).max():.1e}, cell dim {n}")
    G=[(Hk(np.eye(d)[m]*h)-Hk(-np.eye(d)[m]*h))/(2*h) for m in range(d)]
    sq=max(np.abs(g@g-np.eye(n)*np.trace(g@g).real/n).max() for g in G)
    an=max(np.abs(G[a]@G[b]+G[b]@G[a]).max() for a in range(d) for b in range(a+1,d))
    T=[Tk(m,k0) for m in range(d)]
    cm=max(np.abs(t@g-g@t).max() for t in T for g in G)
    print(f"  Gamma^2~1 resid {sq:.1e}, anticomm resid {an:.1e}, [T,Gamma] resid {cm:.1e}")
    if d==3:
        X=G[0]@G[1]@G[2]; X=X/np.sqrt(np.abs(np.linalg.eigvals(X@X)).mean()); X=1j*X if np.allclose(X,-X.conj().T) else X
        print("  chirality X eigs:",np.round(np.linalg.eigvalsh((X+X.conj().T)/2),3))
        Z=T[0]@T[1]@T[2]; ph=np.exp(-1j*np.angle(np.linalg.eigvals(Z)[0]))
        for s in (1,-1): print(f"  ||ph*Z - ({s})X|| = {np.abs(ph*Z-s*X).max():.2e}; [Z,X]={np.abs(Z@X-X@Z).max():.1e}")
    else:
        # 4D Euclidean: H is the Dirac operator; chirality gamma5 ~ G1G2G3G4; shifts T1T2T3 vs T4
        X=G[0]@G[1]@G[2]@G[3]; X=X/np.sqrt(np.abs(np.linalg.eigvals(X@X)).mean())
        Z=T[0]@T[1]@T[2]
        print(f"  [T1T2T3, gamma5] = {np.abs(Z@X-X@Z).max():.2e} ; {{T1T2T3, gamma5}} = {np.abs(Z@X+X@Z).max():.2e}")

# 4D: is T1T2T3 proportional to gamma5, or does it take both signs inside each chirality block?
n,Hk,Tk=cell_ops(4); h=1e-6
G=[(Hk(np.eye(4)[m]*h)-Hk(-np.eye(4)[m]*h))/(2*h) for m in range(4)]
g5=G[0]@G[1]@G[2]@G[3]; g5=g5/np.sqrt(np.abs(np.linalg.eigvals(g5@g5)).mean())
g5=(g5+g5.conj().T)/2
w,v=np.linalg.eigh(g5); Z=Tk(0,np.zeros(4))@Tk(1,np.zeros(4))@Tk(2,np.zeros(4))
for s in (1,-1):
    P=v[:,np.isclose(w,s)]; zb=P.conj().T@Z@P
    print(f"4D gamma5={s:+d} block: T1T2T3 eigenvalues", np.round(np.linalg.eigvals(zb),3))
