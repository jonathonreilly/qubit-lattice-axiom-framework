"""T72 test 1: single clocked walkers. W_meas from direct double commutator vs W_pred from the band."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla, scipy.linalg as la, sys

sx = sp.csr_matrix(np.array([[0,1],[1,0]],dtype=complex))
sz = sp.csr_matrix(np.array([[1,0],[0,-1]],dtype=complex))
I2 = sp.identity(2, dtype=complex, format='csr')

def hop_matrix(N, w):
    """S with bond factors sqrt(w_x w_{x+1}):  (S psi)(x) = (psi(x-1)-psi(x+1))/(2i), open chain."""
    rows=[];cols=[];vals=[]
    for x in range(N-1):
        f=np.sqrt(w[x]*w[x+1])
        # (S)[x+1, x] = +1/(2i)*f  (psi(x) enters at x+1 with +)  ; (S)[x, x+1] = -1/(2i)*f
        rows += [x+1, x]; cols += [x, x+1]; vals += [f/(2j), -f/(2j)]
    return sp.csr_matrix((vals,(rows,cols)),shape=(N,N),dtype=complex)

def build(N, w, beta, m, e0=0.0):
    S = hop_matrix(N, w)
    D = sp.diags(w.astype(complex))
    H = beta*sp.kron(S, sz) + m*sp.kron(D, sx) + e0*sp.kron(D, I2)
    return H.tocsr()

def Xop(N):
    x = np.repeat(np.arange(N,dtype=float),2)
    return sp.diags(x.astype(complex)), x

def accel(H, X, psi):
    A = H@X - X@H
    B = H@A - A@H
    return -np.vdot(psi, B@psi).real   # d^2<X>/dt^2

def lowest_pos_state(N, beta, m, e0):
    H0 = build(N, np.ones(N), beta, m, e0)
    ev, V = la.eigh(H0.toarray())
    # lowest positive-energy above e0 (band bottom at e0+m)
    idx = np.where(ev > e0 + 0.5*m)[0][0]
    return ev[idx], V[:,idx], H0

def band_W(beta, m, e0, k=1e-3):
    eps = lambda kk: e0 + np.sqrt(beta**2*np.sin(kk)**2 + m**2)
    E0 = eps(0.0)
    d2 = (eps(k) - 2*eps(0.0) + eps(-k))/k**2
    return E0*d2, E0, d2

def run(N, beta, m, e0, g=1e-3):
    E, psi, H0 = lowest_pos_state(N, beta, m, e0)
    xc = (N-1)/2.0
    X, xs = Xop(N)
    xpos = np.arange(N)
    out=[]
    for gg in (+g, -g):
        w = np.exp(gg*(xpos - xc))
        H = build(N, w, beta, m, e0)
        out.append(accel(H, X, psi))
    a_odd = 0.5*(out[0]-out[1])
    Wmeas = -a_odd/g
    Wp, E0, d2 = band_W(beta, m, e0)
    return Wmeas, Wp, E, E0, d2, psi, H0

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 240
    print(f"# single clocked walker, open chain N={N}; W_meas from -<[H_w,[H_w,X]]>/g (odd part in g=+-1e-3)")
    print("class            beta   m     e0   W_pred     W_meas     rel.err")
    cases = [("W1 Dirac", 1.0, 1.0, 0.0), ("W1 Dirac", 1.0, 0.5, 0.0), ("W1 Dirac", 1.0, 0.25, 0.0),
             ("W1 c-mismatch", 0.8, 1.0, 0.0), ("W1 c-mismatch", 1.2, 0.5, 0.0), ("W1 c-mismatch", 0.5, 1.0, 0.0),
             ("W2 offset", 1.0, 1.0, 0.5), ("W2 offset", 1.0, 0.5, 1.0), ("W2 offset", 0.9, 1.0, 0.3)]
    for name,b,m,e0 in cases:
        Wm, Wp, E, E0, d2, psi, H0 = run(N,b,m,e0)
        print(f"{name:16s} {b:4.2f} {m:5.2f} {e0:5.2f}  {Wp:9.5f}  {Wm:9.5f}  {abs(Wm-Wp)/max(abs(Wp),0.1):8.2e}")
