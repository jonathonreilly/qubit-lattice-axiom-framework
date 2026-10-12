"""D2 (a, supersonic): 1D TB particle eps = 1 - cos k (v_max = 1) with a slow acoustic mode
(c = 0.4 < v_max).  The one-phonon threshold th(K) = min_q [eps(K-q) + w(q)] has an exact
Lambda-kink at the face (two Cherenkov minimisers +-q* exchange there), slope s_th.
BW1 root below threshold at continuous K (q-grid N, K off-grid).  Measures vs g2 -> 0:
gap to threshold at the face, face curvature C, rounding length ell = s/C, chord slope s(d)
relative to threshold slope, Z(pi).  Also 2D (kx, 0) line through the face, BW1, c = 0.4."""
import numpy as np, sys, time
TWO_PI = 2*np.pi
def eps(k): return 1 - np.cos(k)
def w1(q, c): return 2*c*np.abs(np.sin(q/2))
def root(Ks, q, M2, c, N, epsf, wq):
    lam_out = []; Z_out = []; th_out = []
    for K in Ks:
        P = epsf(K, q) + wq
        lp = P.min(); wts = M2/N
        lo, hi = lp - 50, lp
        lam = lp - 1e-3
        for it in range(200):
            den = lam - P
            f = lam - epsf(K, None) - (wts/den).sum()
            fp = 1 + (wts/den**2).sum()
            if f < 0: lo = lam
            else: hi = lam
            new = lam - f/fp
            if not (lo < new < hi): new = 0.5*(lo+hi)
            if abs(new - lam) < 1e-15*max(1, abs(lam)): lam = new; break
            lam = new
        den = lam - P
        lam_out.append(lam); Z_out.append(1/(1 + (wts/den**2).sum())); th_out.append(lp)
    return np.array(lam_out), np.array(Z_out), np.array(th_out)

def study1d(c, g2, a, N, ds):
    q = TWO_PI*np.arange(1, N)/N
    wq = w1(q, c); M2 = g2*(2*np.abs(np.sin(q/2)))**(2*a)
    epsf = lambda K, qq: eps(K - qq) if qq is not None else eps(K)
    Ks = np.array([np.pi] + [np.pi - d for d in ds])
    E, Z, th = root(Ks, q, M2, c, N, epsf, wq)
    D = E[0] - E[1:]; Dth = th[0] - th[1:]
    return E, Z, th, D, Dth

if __name__ == '__main__':
    ds = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3]
    print("# 1D BW1 supersonic c=0.4, a=0.5.  s(d) = [E(pi)-E(pi-d)]/d ; s_th = threshold chord slope at d=0.03")
    print("# rows: g2 N | E(pi) gap(pi)=th-E Z(pi) | s_th | s(d)/s_th for d=" + ",".join(map(str, ds)) + " | ell=s_th/C, C=2D/d^2 at d=1e-4")
    for g2 in [0.3, 0.1, 0.03, 0.01, 0.003]:
        for N in [8192, 32768]:
            t = time.time()
            E, Z, th, D, Dth = study1d(0.4, g2, 0.5, N, ds)
            s_th = Dth[5]/ds[5]
            C = 2*D[0]/ds[0]**2
            print(f"g2={g2} N={N} | E={E[0]:.6f} gap={th[0]-E[0]:.3e} Z={Z[0]:.4e} | s_th={s_th:.4f} | "
                  + " ".join(f"{D[i]/ds[i]/s_th:.3f}" for i in range(len(ds))) + f" | ell={s_th/C:.3e} | t={time.time()-t:.1f}", flush=True)
    # subsonic comparison (c = 1.5): no threshold kink
    print("# subsonic comparison c=1.5, a=0.5")
    for g2 in [0.3, 0.03]:
        E, Z, th, D, Dth = study1d(1.5, g2, 0.5, 32768, ds)
        print(f"c=1.5 g2={g2} | E={E[0]:.6f} gap={th[0]-E[0]:.3e} Z={Z[0]:.4f} | s(d)=" + " ".join(f"{D[i]/ds[i]:.2e}" for i in range(len(ds))))
