"""R19-24: convergence checks for r1924_sunset.py (imports its function unchanged):
(1) tau-quadrature: 20 vs 32 Gauss-Legendre nodes per panel; (2) the m -> 0 trend (m = 0.2, 0.1) of the two-loop LV speed shift,
to see whether it has a finite massless limit (UV-localized) or an IR log. Units: delta c^2 / lam^2; x (16 pi^2)^2 = per (lam/16pi^2)^2."""
import time, numpy as np, r1924_sunset as R
t0 = time.time(); c = (16*np.pi**2)**2
orig = R.panels
def panels32(tmax):
    edges = [0.0, 0.25, 0.5, 1.0]
    while edges[-1] < tmax: edges.append(edges[-1]*1.6)
    xg, wg = np.polynomial.legendre.leggauss(32); T, W = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        T.append(0.5*(b-a)*xg + 0.5*(b+a)); W.append(0.5*(b-a)*wg)
    return np.concatenate(T), np.concatenate(W)
for name, e2 in (('NN', R.nn), ('G(2.526)', R.gbox)):
    R.panels = orig; a = R.sunset_speed(32, 0.3, e2)[:2]
    R.panels = panels32; b = R.sunset_speed(32, 0.3, e2)[:2]
    print('%-9s m=0.3 L=32: GL20 (%+.6e, %+.6e)  GL32 (%+.6e, %+.6e)' % (name, a[0], a[1], b[0], b[1]), flush=True)
R.panels = orig
for name, e2 in (('NN', R.nn), ('G(2.526)', R.gbox)):
    for m, Ls in ((0.2, (48, 64)), (0.1, (64, 96))):
        for L in Ls:
            dE, dos, p, w, tl = R.sunset_speed(L, m, e2)
            print('%-9s m=%.2f L=%d | dc2/lam2 Eucl %+.4e (x(16pi^2)^2 = %+.4f) | on-shell %+.4e (%+.4f) | d_p2 %+.4e d_w2 %+.4e (%.0fs)'
                  % (name, m, L, dE, dE*c, dos, dos*c, p, w, time.time()-t0), flush=True)
print('elapsed %.0fs' % (time.time()-t0))
