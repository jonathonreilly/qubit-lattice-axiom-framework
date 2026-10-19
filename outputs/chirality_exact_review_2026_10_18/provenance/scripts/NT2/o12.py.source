"""NT-2 O12 (secondary): open 1x2 strip slice (2 plaquettes sharing one link; 7 links; no holonomies).
K(phi, phi') = h(phi - phi'), h(F1, F2) = int_{-d}^{d} de T3(F1 - e) T3(F2 + e), T3 = 3-fold convolution of B_{2d}
(density of the sum of 3 uniform links; constant factors dropped). Exact: Gauss-Legendre (3 pts, degree-4 exact) on
every breakpoint piece. Independent: composite Simpson on a uniform grid (n = 4000 and 8000).
Usage: python o12.py MODE NPTS  (MODE: grid = admissible square |phi_p| <= d - 0.05 ; unres = full torus grid (R1))"""
import sys, itertools, math, time, resource, numpy as np
mode = sys.argv[1]; n = int(sys.argv[2]); d = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
w = 2 * d
def box3(x):
    x = np.asarray(x, float); tot = np.zeros_like(x)
    for eps in itertools.product((1, -1), repeat=3):
        s = x + 0.5 * w * sum(eps); tot += np.prod(eps) * np.where(s > 0, s, 0.0) ** 2
    return tot / 2.0
gx, gw = np.polynomial.legendre.leggauss(3)
def h_exact(F1, F2):
    bp = [-d, d] + [F1 + c for c in (-3 * d, -d, d, 3 * d)] + [-F2 + c for c in (-3 * d, -d, d, 3 * d)]
    bp = np.unique(np.clip(bp, -d, d)); tot = 0.0
    for lo, hi in zip(bp[:-1], bp[1:]):
        if hi - lo < 1e-15: continue
        e = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
        tot += 0.5 * (hi - lo) * np.dot(gw, box3(F1 - e) * box3(F2 + e))
    return tot
def h_simpson(F1, F2, m):
    e = np.linspace(-d, d, m + 1); wt = np.ones(m + 1); wt[1:-1:2] = 4; wt[2:-1:2] = 2
    return (2 * d / m / 3) * np.dot(wt, box3(F1 - e) * box3(F2 + e))
t0 = time.time()
if mode == 'grid':
    ax = np.linspace(-(d - 0.05), d - 0.05, n); step = ax[1] - ax[0]; wrapit = False
else:
    ax = -np.pi + 2 * np.pi * np.arange(n) / n; step = 2 * np.pi / n; wrapit = True
P = np.array([(x, y) for x in ax for y in ax])
# difference table on the integer offsets (translation invariance)
offs = np.arange(-(n - 1), n)
H = np.zeros((len(offs), len(offs))); Hs = np.zeros_like(H)
for i, a in enumerate(offs):
    for j, b in enumerate(offs):
        F1, F2 = a * step, b * step
        if wrapit:
            F1 = (F1 + np.pi) % (2 * np.pi) - np.pi; F2 = (F2 + np.pi) % (2 * np.pi) - np.pi
        if abs(F1) >= 4 * d or abs(F2) >= 4 * d: continue
        H[i, j] = h_exact(F1, F2)
        Hs[i, j] = h_simpson(F1, F2, 4000)
idx = np.array([(i, j) for i in range(n) for j in range(n)])
I1 = idx[:, 0][:, None] - idx[:, 0][None, :] + n - 1; I2 = idx[:, 1][:, None] - idx[:, 1][None, :] + n - 1
K = H[I1, I2]; Ks = Hs[I1, I2]
ev = np.linalg.eigvalsh(K); evs = np.linalg.eigvalsh(Ks)
k = len(P); E = k * np.abs(K - Ks).max() + k * 1e-15 * np.abs(K).max()
print(f"RESULT O12 mode={mode} n={n} ({k} pts) delta={d}: lam_min {ev[0]:+.4e} lam_max {ev[-1]:.4e} rel {ev[0]/ev[-1]:+.3e} | simpson lam_min {evs[0]:+.4e} | "
      f"E {E:.1e} | neg-converged {ev[0] < -10*E and ev[0]/ev[-1] < -1e-9} | max|phi| {np.abs(P).max():.3f} | {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
