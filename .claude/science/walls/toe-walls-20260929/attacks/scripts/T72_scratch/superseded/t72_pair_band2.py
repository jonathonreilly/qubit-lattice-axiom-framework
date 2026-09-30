import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
from t72_pair_band import sx,sz,I2,sz1,sz2,sx1,sx2,I4

def H_rel_sparse(K, lam, beta, m, R, e0=0.0):
    n=2*R+1
    Dm = beta/(2j)*(sz1*np.exp(-1j*K/2) - sz2*np.exp(1j*K/2))
    Dp = beta/(2j)*(-sz1*np.exp(1j*K/2) + sz2*np.exp(-1j*K/2))
    on = m*(sx1+sx2) + 2*e0*I4
    Ir = sp.identity(n,format='csr')
    lo = sp.diags([np.ones(n-1)],[-1],format='csr')   # phi(r-1) into row r
    up = sp.diags([np.ones(n-1)],[1],format='csr')
    H = sp.kron(Ir,on) + sp.kron(lo,Dm) + sp.kron(up,Dp)
    d = np.zeros(n); d[R] = -lam
    H = H + sp.kron(sp.diags(d),I4)
    return H.tocsc()

def bound_E_sparse(K,lam,beta,m,R,e0=0.0,guess=None):
    H = H_rel_sparse(K,lam,beta,m,R,e0)
    thr = 2*e0 + 2*np.sqrt(beta**2*np.sin(K/2)**2 + m**2)
    sig = thr - 0.5*lam*lam*m if guess is None else guess   # inside gap
    ev = sla.eigsh(H, k=6, sigma=thr-1e-3*m-0.3*lam**2*m, which='LM', return_eigenvectors=False)
    cand = ev[(ev<thr-1e-9)&(ev>2*e0+0.6*m)]
    return cand.min()

def W_pair_sparse(lam,beta,m,R,e0=0.0,dK=0.01):
    E0=bound_E_sparse(0.0,lam,beta,m,R,e0); Ep=bound_E_sparse(dK,lam,beta,m,R,e0); Em=bound_E_sparse(-dK,lam,beta,m,R,e0)
    d2=(Ep-2*E0+Em)/dK**2
    return E0*d2,E0,d2

if __name__=="__main__":
    print("small-m scan: W_pair-1 vs binding fraction; NR+clock-alone prediction (contact): (W-1)/(B/2m) = -4")
    for m,R in ((0.25,400),(0.1,900)):
        print(f"m={m}")
        for lam in (0.01,0.02,0.04,0.08):
            W,E0,d2=W_pair_sparse(lam,1.0,m,R)
            B=2*m-E0
            print(f"  lam={lam:5.3f} B={B:9.6f} B/2m={B/(2*m):8.5f}  W={W:9.5f}  (W-1)/(B/2m)={(W-1)/(B/(2*m)):8.3f}")
