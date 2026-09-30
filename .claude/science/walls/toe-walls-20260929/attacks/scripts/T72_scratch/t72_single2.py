"""T72 test 1b: single clocked walkers with an interband-dressed (Zitterbewegung-free) start state.
Also a time-evolution cross-check of the dressed double-commutator value."""
import numpy as np, scipy.sparse as sp, scipy.linalg as la, scipy.sparse.linalg as sla, sys
from t72_single import build, Xop, band_W

def dressed_accel(N, beta, m, e0, g, evecs, evals, psi, Ecut, dress=True):
    xpos = np.arange(N); xc=(N-1)/2.0
    X,_ = Xop(N)
    H0 = build(N, np.ones(N), beta, m, e0)
    Hg = build(N, np.exp(g*(xpos-xc)), beta, m, e0)
    H1 = (Hg - H0)/g   # dH/dg at first order (finite difference; exact enough for small g)
    if dress:
        neg = np.where(evals < Ecut)[0]
        Vn = evecs[:,neg]
        Eps = evals[np.argmax(np.abs(evecs.conj().T@psi))]
        coef = (Vn.conj().T@(H1@psi))/(Eps - evals[neg])
        psid = psi + g*(Vn@coef)
        psid /= np.linalg.norm(psid)
    else:
        psid = psi
    A = Hg@X - X@Hg
    B = Hg@A - A@Hg
    return -np.vdot(psid, B@psid).real, psid, Hg, X

def run(N, beta, m, e0, g=1e-3, dress=True):
    H0 = build(N, np.ones(N), beta, m, e0)
    ev, V = la.eigh(H0.toarray())
    idx = np.where(ev > e0 + 0.5*m)[0][0]
    psi = V[:,idx]
    Ecut = e0 + 0.5*m
    ap,_,_,_ = dressed_accel(N,beta,m,e0,+g,V,ev,psi,Ecut,dress)
    am,_,_,_ = dressed_accel(N,beta,m,e0,-g,V,ev,psi,Ecut,dress)
    return -(0.5*(ap-am))/g, V, ev, psi

def evolve_fit(N, beta, m, e0, g, psi, T=30.0, npts=301):
    xpos=np.arange(N); xc=(N-1)/2.0
    X,_=Xop(N)
    Hg = build(N, np.exp(g*(xpos-xc)), beta, m, e0)
    Xd = X.diagonal().real
    ts = np.linspace(0,T,npts)
    Ps = sla.expm_multiply(-1j*Hg, psi, start=0, stop=T, num=npts, endpoint=True)
    x = np.array([np.vdot(p, Xd*p).real/np.vdot(p,p).real for p in Ps])
    # fit x = c0 + c1 t + c2 t^2 on second half (ZB oscillation is small and fast)
    sel = ts>T/4
    c = np.polyfit(ts[sel], x[sel], 2)
    return 2*c[0], ts, x

if __name__ == "__main__":
    N=240
    print("# dressed (ZB-free) double commutator; W_meas = -a_odd/g")
    print("class            beta   m     e0   W_pred     W_dressed  W_undressed")
    cases = [("W1 Dirac", 1.0, 1.0, 0.0), ("W1 Dirac", 1.0, 0.5, 0.0),
             ("W1 c-mismatch", 0.8, 1.0, 0.0), ("W1 c-mismatch", 1.2, 0.5, 0.0),
             ("W2 offset", 1.0, 1.0, 0.5), ("W2 offset", 1.0, 0.5, 1.0), ("W2 offset", 0.9, 1.0, 0.3)]
    for name,b,m,e0 in cases:
        Wd, V, ev, psi = run(N,b,m,e0,dress=True)
        Wu, *_ = run(N,b,m,e0,dress=False)
        Wp,_,_ = band_W(b,m,e0)[0], None, None
        print(f"{name:16s} {b:4.2f} {m:5.2f} {e0:5.2f}  {Wp:9.5f}  {Wd:9.5f}  {Wu:9.5f}")
    print("# time-evolution cross-check (g=0.01, T=30): a_fit/(-g) vs W_pred")
    for name,b,m,e0 in [("W1 Dirac",1.0,1.0,0.0),("W2 offset",1.0,1.0,0.5),("W2 offset",1.0,0.5,1.0),("W1 c-mismatch",0.8,1.0,0.0)]:
        H0 = build(N, np.ones(N), b, m, e0)
        ev,V = la.eigh(H0.toarray()); idx=np.where(ev>e0+0.5*m)[0][0]; psi=V[:,idx]
        afit,ts,x = evolve_fit(N,b,m,e0,0.01,psi)
        Wp = band_W(b,m,e0)[0]
        print(f"{name:16s} beta={b} m={m} e0={e0}: W_pred={Wp:8.4f}  W_from_evolution={-afit/0.01:8.4f}")
