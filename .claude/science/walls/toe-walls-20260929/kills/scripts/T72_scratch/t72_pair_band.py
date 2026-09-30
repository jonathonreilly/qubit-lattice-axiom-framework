"""T72 test 2a: pair band. Relative-coordinate two-body problem at total wave number K (uniform, w=1).
Validated against a brute-force periodic ring."""
import numpy as np, scipy.linalg as la, scipy.sparse as sp

sx=np.array([[0,1],[1,0]],dtype=complex); sz=np.diag([1,-1]).astype(complex); I2=np.eye(2,dtype=complex)
sz1=np.kron(sz,I2); sz2=np.kron(I2,sz); sx1=np.kron(sx,I2); sx2=np.kron(I2,sx); I4=np.eye(4,dtype=complex)

def H_rel(K, lam, beta=1.0, m=1.0, R=60, e0=0.0):
    n=2*R+1
    H=np.zeros((4*n,4*n),dtype=complex)
    Dm = beta/(2j)*(sz1*np.exp(-1j*K/2) - sz2*np.exp(1j*K/2))   # coefficient of phi(r-1) in row r
    Dp = beta/(2j)*(-sz1*np.exp(1j*K/2) + sz2*np.exp(-1j*K/2)) # coefficient of phi(r+1)
    on = m*(sx1+sx2) + 2*e0*I4
    for i in range(n):
        H[4*i:4*i+4,4*i:4*i+4] = on
        if i>0:   H[4*i:4*i+4,4*(i-1):4*(i-1)+4] = Dm
        if i<n-1: H[4*i:4*i+4,4*(i+1):4*(i+1)+4] = Dp
    c=R  # r=0 index
    H[4*c:4*c+4,4*c:4*c+4] -= lam*I4
    return H

def pair_levels(K, lam, beta=1.0, m=1.0, R=60, e0=0.0, target=None):
    ev = la.eigvalsh(H_rel(K,lam,beta,m,R,e0))
    return ev

def bound_E(K, lam, beta=1.0, m=1.0, R=60, e0=0.0):
    """bound level: the lowest eigenvalue in the positive sector clearly below the 2-particle continuum 2*(e0+eps(K/2))"""
    ev = pair_levels(K,lam,beta,m,R,e0)
    thr = 2*e0 + 2*np.sqrt(beta**2*np.sin(K/2)**2 + m**2)   # (+,+) continuum lower edge at this K, roughly
    cand = ev[(ev>2*e0+0.6*m) & (ev<thr-1e-6)]
    return cand.min() if len(cand) else np.nan

def W_pair(lam, beta=1.0, m=1.0, R=60, e0=0.0, dK=0.02):
    E0 = bound_E(0.0,lam,beta,m,R,e0); Ep=bound_E(dK,lam,beta,m,R,e0); Em=bound_E(-dK,lam,beta,m,R,e0)
    d2 = (Ep-2*E0+Em)/dK**2
    return E0*d2, E0, d2

def ring_bruteforce(N, lam, beta=1.0, m=1.0, e0=0.0):
    # single-particle periodic ring
    S=np.zeros((N,N),dtype=complex)
    for x in range(N):
        S[(x+1)%N,x]+=1/(2j); S[x,(x+1)%N]+=-1/(2j)
    h1 = beta*np.kron(S,sz) + m*np.kron(np.eye(N),sx) + e0*np.eye(2*N)
    H2 = np.kron(h1,np.eye(2*N)) + np.kron(np.eye(2*N),h1)
    # contact: -lam when x1==x2, identity in spin
    diag=np.zeros((2*N,2*N))
    idx = lambda x,s: 2*x+s
    V=np.zeros(4*N*N)
    for x in range(N):
        for s1 in range(2):
            for s2 in range(2):
                V[idx(x,s1)*2*N+idx(x,s2)] = -lam
    H2 = H2 + np.diag(V)
    return la.eigvalsh(H2)

if __name__=="__main__":
    lam=1.0
    print("validation: relative-coordinate vs brute-force ring N=18, lam=1, beta=m=1")
    ev=ring_bruteforce(18,lam)
    for K in (0.0, 2*np.pi/18, 2*np.pi*2/18):
        Er=bound_E(K,lam,R=40)
        near=ev[np.argmin(abs(ev-Er))]
        print(f"K={K:.4f}  E_rel={Er:.8f}  nearest ring eigenvalue={near:.8f}  diff={abs(near-Er):.2e}")
    print("\nW_pair vs lam (beta=m=1, e0=0):  W = E0 * d2E/dK2 at K=0")
    print(" lam     E0        B=2m-E0   M_pair^-1=E''   W_pair    W_pair-1     (W-1)/(B/2m)")
    for lam in (0.05,0.1,0.2,0.4,0.8,1.2):
        W,E0,d2=W_pair(lam)
        B=2.0-E0
        print(f"{lam:5.2f}  {E0:9.5f}  {B:8.5f}  {d2:9.5f}  {W:9.5f}  {W-1:9.5f}  {(W-1)/(B/2) if B>1e-9 else float('nan'):9.4f}")
