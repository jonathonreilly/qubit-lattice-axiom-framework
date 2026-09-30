"""T72 test 2b: two distinguishable clocked walkers with a contact attraction on an open chain, direct dressed
double-commutator acceleration in a clock gradient, vs the band prediction W_pair = E0 E''(K=0).
timed=True: binding term multiplied by the site clock (like every other term); timed=False: binding constant."""
import numpy as np, scipy.sparse as sp, scipy.linalg as la, sys, time
from t72_single import build
from t72_pair_band import W_pair

def two_body(N, w, beta, m, e0, lam, timed):
    h = build(N, w, beta, m, e0)
    I = sp.identity(2*N, format='csr', dtype=complex)
    H = sp.kron(h, I) + sp.kron(I, h)
    fac = w if timed else np.ones(N)
    V = np.zeros((2*N)**2)
    for x in range(N):
        for s1 in range(2):
            for s2 in range(2):
                V[(2*x+s1)*2*N + (2*x+s2)] = -lam*fac[x]
    return (H + sp.diags(V.astype(complex))).tocsr()

def Xcm(N):
    xs = np.repeat(np.arange(N,dtype=float),2)
    Xs = sp.diags(xs.astype(complex)); I = sp.identity(2*N, format='csr', dtype=complex)
    return 0.5*(sp.kron(Xs,I)+sp.kron(I,Xs)).tocsr()

def measure(N, beta, m, e0, lam, timed, g=1e-3, Ecut=None, verbose=False):
    xpos=np.arange(N); xc=(N-1)/2
    H0 = two_body(N, np.ones(N), beta, m, e0, lam, timed)
    t0=time.time()
    ev, V = la.eigh(H0.toarray())
    if verbose: print(f"   eigh done {time.time()-t0:.0f}s", flush=True)
    if Ecut is None: Ecut = 2*e0 + 1.0*m
    idx = np.where(ev > Ecut)[0][0]           # lowest state of the (+,+) sector = lowest bound COM level
    psi = V[:,idx]; E = ev[idx]
    X = Xcm(N)
    res={}
    for sgn in (+1,-1):
        gg = sgn*g
        Hg = two_body(N, np.exp(gg*(xpos-xc)), beta, m, e0, lam, timed)
        H1 = (Hg-H0)/gg
        neg = np.where(ev < Ecut)[0]
        Vn = V[:,neg]
        coef = (Vn.conj().T@(H1@psi))/(E-ev[neg])
        pd = psi + gg*(Vn@coef); pd/=np.linalg.norm(pd)
        A = Hg@X - X@Hg
        B = Hg@A - A@Hg
        res[sgn] = -np.vdot(pd, B@pd).real
    a_odd = 0.5*(res[+1]-res[-1])
    # also the kinetic expectation for the Hellmann-Feynman prediction (untimed binding)
    return -a_odd/g, E, psi, H0, ev, V

if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 24
    beta=1.0; m=1.0; e0=0.0
    print(f"# open chain N={N}; W_direct = -a_odd/g (dressed double commutator); W_band from relative problem")
    print(" lam  timed   E_standing  W_direct   W_band(timed)   W_direct/W_band")
    for lam in (0.2,0.4,0.8):
        Wb,E0b,d2b = W_pair(lam,beta,m,R=60,e0=e0)
        for timed in (True,):
            Wd,E,psi,H0,ev,V = measure(N,beta,m,e0,lam,timed,verbose=False)
            print(f"{lam:4.1f}  {str(timed):5s}  {E:9.5f}  {Wd:9.5f}   {Wb:9.5f}   {Wd/Wb:8.4f}", flush=True)
