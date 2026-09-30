"""T72 core (staggered one-component chain: single valley, the repo's 'staggered rest energy').
Single walker:  h = beta*S + m*Gamma + e0,  S=(T-T^dag)/2i, Gamma=(-1)^x ; eps^2 = beta^2 sin^2 k + m^2 (reduced zone).
Clock (whole generator timed): hop x<->x+1 gets sqrt(w_x w_{x+1}); on-site terms get w_x.
Pair: two distinguishable walkers + contact -lam*(w_x if timed else 1) at x1=x2."""
import numpy as np, scipy.sparse as sp, scipy.linalg as la

def h1(N, w, beta, m, e0=0.0, periodic=False, twist=0.0):
    rows=[];cols=[];vals=[]
    for x in range(N-1 if not periodic else N):
        y=(x+1)%N
        f=np.sqrt(w[x]*w[y])*beta
        ph = np.exp(1j*twist) if (periodic and y==0) else 1.0
        # (S psi)(x) = (psi(x-1)-psi(x+1))/(2i): entry S[y,x]=+1/(2i), S[x,y]=-1/(2i)
        rows += [y, x]; cols += [x, y]
        vals += [f/(2j)*np.conj(ph) if False else f/(2j)*ph, -f/(2j)*np.conj(ph)]
    H = sp.csr_matrix((vals,(rows,cols)),shape=(N,N),dtype=complex)
    gam = np.array([(-1)**x for x in range(N)],dtype=float)
    H = H + sp.diags((m*gam + e0)*w).astype(complex)
    return H.tocsr()

def band_W(beta,m,e0,k=1e-3):
    eps=lambda kk: e0+np.sqrt(beta**2*np.sin(kk)**2+m**2)
    E0=eps(0.0); d2=(eps(k)-2*E0+eps(-k))/k**2
    return E0*d2,E0,d2

def two_body(N, w, beta, m, e0, lam, timed, periodic=False):
    h=h1(N,w,beta,m,e0,periodic)
    I=sp.identity(N,format='csr',dtype=complex)
    H=sp.kron(h,I)+sp.kron(I,h)
    fac = w if timed else np.ones(N)
    V=np.zeros(N*N)
    for x in range(N): V[x*N+x] = -lam*fac[x]
    return (H+sp.diags(V.astype(complex))).tocsr()

def Xcm(N):
    xs=np.arange(N,dtype=float); I=sp.identity(N,format='csr')
    return (0.5*(sp.kron(sp.diags(xs),I)+sp.kron(I,sp.diags(xs)))).tocsr().astype(complex)

def Xone(N): return sp.diags(np.arange(N,dtype=float)).astype(complex).tocsr()

def dressed_a(Hfun, X, ev, V, idx, Ecut, g):
    """Hfun(g) -> sparse H(g); ev,V eigen of H(0); idx = state index. Returns dressed double-commutator a(g)."""
    H0=Hfun(0.0); Hg=Hfun(g); H1=(Hg-H0)/g
    psi=V[:,idx]; E=ev[idx]
    neg=np.where(ev<Ecut)[0]
    Vn=V[:,neg]
    coef=(Vn.conj().T@(H1@psi))/(E-ev[neg])
    pd=psi+g*(Vn@coef); pd/=np.linalg.norm(pd)
    A=Hg@X-X@Hg; B=Hg@A-A@Hg
    return -np.vdot(pd,B@pd).real

def W_direct(Hfun, X, ev, V, idx, Ecut, g=1e-3):
    ap=dressed_a(Hfun,X,ev,V,idx,Ecut,+g); am=dressed_a(Hfun,X,ev,V,idx,Ecut,-g)
    return -(0.5*(ap-am))/g

# ---------- pair band via translation-by-2 Bloch sectors on a large periodic ring ----------
def pair_band_E(Nring, lam, beta, m, e0, Qs, timed=True):
    """H2 on a periodic ring (uniform), reduce by simultaneous shift of both particles by 2 sites.
    Returns dict Q -> sorted eigenvalues of the sector. Q = quasi-momentum per 2-site cell; physical K = Q/2."""
    M=Nring//2
    H=two_body(Nring,np.ones(Nring),beta,m,e0,lam,timed,periodic=True).tocoo()
    N=Nring
    # orbits of (x1,x2) under (x1,x2)->(x1+2,x2+2): representative x1 in {0,1}, x2 in 0..N-1
    def idx(x1,x2): return (x1%N)*N+(x2%N)
    reps=[(a,b) for a in (0,1) for b in range(N)]
    # each basis index -> (rep number, j) with (x1,x2)=(a+2j, b+2j)
    lookup={}
    for r,(a,b) in enumerate(reps):
        for j in range(M):
            lookup[idx(a+2*j,b+2*j)]=(r,j)
    out={}
    R=len(reps)
    rr=np.array([lookup[i][0] for i in H.row]); jr=np.array([lookup[i][1] for i in H.row])
    rc=np.array([lookup[i][0] for i in H.col]); jc=np.array([lookup[i][1] for i in H.col])
    for Q in Qs:
        # Bloch states |r,Q> = M^{-1/2} sum_j e^{-iQ j} |r,j> ; H_Q[r',r] = sum_j' <r',0|H|r,j> e^{-iQ j}... compute via entries
        HQ=np.zeros((R,R),dtype=complex)
        # matrix element <r',j'|H|r,j> depends on j-j'; H_Q[r',r] = sum_{entries with row=(r',j'=0)} val * e^{-iQ (j - 0)}
        sel = (jr==0)
        np.add.at(HQ,(rr[sel],rc[sel]),H.data[sel]*np.exp(-1j*Q*jc[sel]))
        HQ=0.5*(HQ+HQ.conj().T)
        out[Q]=la.eigvalsh(HQ)
    return out
