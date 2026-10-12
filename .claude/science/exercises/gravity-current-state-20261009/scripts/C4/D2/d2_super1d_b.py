"""D2 (a, supersonic, degenerate Cherenkov minimisers): band eps = (1 - cos k)^2 (flat
bottom, v_max = 2.6; a nearest-neighbour-network band of trig degree 2) with c = 0.4 or 1.0.
At K = pi the one-phonon threshold min_k [eps(k) + 2c|cos(k/2)|] has two minimisers +-k* != 0,
so th(K) has an exact Lambda-kink at the face.  Does the dressed (BW1) bound state inherit it?
Measures as in d2_super1d.py; plus a SLAC fit (E^2 = m0^2 + beta k^2 on [pi-w, pi]) of the
threshold curve and of the dressed band."""
import numpy as np, time
from d2_super1d import root
TWO_PI = 2*np.pi
def eps(k): return (1 - np.cos(k))**2
def slacfit(k, E):
    A = np.vstack([np.ones_like(k), k**2]).T
    (m02, b), *_ = np.linalg.lstsq(A, E**2, rcond=None)
    Ef = np.sqrt(np.clip(m02 + b*k**2, 0, None))
    return m02, b, np.max(np.abs(Ef - E))/(E.max() - E.min())
ds = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3]
print("# eps=(1-cos k)^2, a=0.5, BW1, q-grid N=32768.  s(d) = [E(pi)-E(pi-d)]/d ; s_th from threshold at d=0.01")
for c in [0.4, 1.0]:
    kk = np.linspace(-np.pi, np.pi, 200001); g = eps(kk) + 2*c*np.abs(np.cos(kk/2))
    i = np.argmin(g); print(f"c={c}: K=pi threshold minimiser k*={kk[i]:.4f}, th(pi)={g[i]:.5f}, kink slope |eps'(k*)|={abs(2*(1-np.cos(kk[i]))*np.sin(kk[i])):.4f}")
    N = 32768; q = TWO_PI*np.arange(1, N)/N; wq = 2*c*np.abs(np.sin(q/2))
    epsf = lambda K, qq: eps(K - qq) if qq is not None else eps(K)
    for g2 in [0.3, 0.1, 0.03, 0.01, 0.003]:
        M2 = g2*(2*np.abs(np.sin(q/2)))
        Ks = np.array([np.pi] + [np.pi - d for d in ds])
        E, Z, th = root(Ks, q, M2, c, N, epsf, wq)
        D = E[0] - E[1:]; Dth = th[0] - th[1:]
        s_th = Dth[4]/ds[4]
        print(f"c={c} g2={g2} | E(pi)={E[0]:.6f} gap={th[0]-E[0]:.3e} Z(pi)={Z[0]:.3e} | s_th={s_th:.4f} | s(d)/s_th="
              + " ".join(f"{D[i]/ds[i]/s_th:.3f}" for i in range(len(ds))) + f" | ell=s_th/C={s_th/(2*D[0]/ds[0]**2):.2e}", flush=True)
    # SLAC fits on windows including the face, dressed vs threshold, g2=0.03
    Kw = np.linspace(np.pi/2, np.pi, 401)
    E, Z, th = root(Kw, q, 0.03*(2*np.abs(np.sin(q/2))), c, N, epsf, wq)
    for w in [np.pi/8, np.pi/4, np.pi/2]:
        sel = Kw >= np.pi - w - 1e-12
        print(f"c={c} g2=0.03 window w={w:.3f}: SLAC dev/bw dressed={slacfit(Kw[sel], E[sel])[2]:.4f} threshold={slacfit(Kw[sel], th[sel])[2]:.4f}; Z range on window {Z[sel].min():.2e}..{Z[sel].max():.2e}")
