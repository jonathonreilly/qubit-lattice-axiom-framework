"""T72 test 1c: honest time-evolution check with a free Gaussian packet (not a whole-chain standing wave)."""
import numpy as np, scipy.linalg as la, scipy.sparse.linalg as sla
from t72_single import build, Xop, band_W

def packet(N, beta, m, e0, sigma=22.0):
    H0 = build(N, np.ones(N), beta, m, e0)
    ev, V = la.eigh(H0.toarray())
    x = np.arange(N); xc=(N-1)/2
    env = np.exp(-(x-xc)**2/(4*sigma**2))
    # spinor at k=0 in the upper band: eigenvector of m*sx (+): (1,1)/sqrt2 ; then project to upper band of H0
    g0 = np.kron(env, np.array([1,1])/np.sqrt(2)).astype(complex)
    up = np.where(ev > e0 + 0.5*m)[0]
    c = V[:,up].conj().T@g0
    psi = V[:,up]@c
    return psi/np.linalg.norm(psi)

def run(N,beta,m,e0,g,T=40.0,npts=161):
    psi = packet(N,beta,m,e0)
    xpos=np.arange(N); xc=(N-1)/2
    Hg = build(N, np.exp(g*(xpos-xc)), beta, m, e0)
    X,_ = Xop(N); Xd = X.diagonal().real
    Ps = sla.expm_multiply(-1j*Hg, psi, start=0, stop=T, num=npts, endpoint=True)
    ts = np.linspace(0,T,npts)
    x = np.array([np.vdot(p, Xd*p).real for p in Ps])
    sel = ts > T/5
    c = np.polyfit(ts[sel], x[sel], 2)
    return -2*c[0]/g, ts, x

if __name__=="__main__":
    N=700
    print("# free Gaussian packet (sigma=22), positive band, evolved in w=exp(g(x-xc)), g=0.003, T=40")
    for name,b,m,e0 in [("W1 Dirac",1.0,1.0,0.0),("W1 Dirac",1.0,0.5,0.0),("W1 c-mismatch",0.8,1.0,0.0),
                        ("W2 offset",1.0,1.0,0.5),("W2 offset",1.0,0.5,1.0)]:
        Wm,ts,x = run(N,b,m,e0,0.003)
        Wp = band_W(b,m,e0)[0]
        print(f"{name:14s} beta={b} m={m} e0={e0}: W_pred={Wp:7.4f}  W_from_evolution={Wm:7.4f}  rel.err={(Wm-Wp)/Wp:+.3f}")
