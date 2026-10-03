"""A41 d2: scan the family angle theta in [0, pi/2] (theta -> theta + pi and theta -> -theta give the same spectra up to
a momentum shift; the scale t only rescales energies). For zero flux (H0, 3 bands) and pi flux (H6, 6 bands; the
minimal-cell 12-band spectrum is spec H6 + spec(-H6)):
  zf: does det H0 change sign (a band crosses E = 0 on a surface)?  min over k of the 2nd smallest |E| (two bands at
      E = 0), refined by Nelder-Mead from the 3 best grid points (2 for the other quantities);  smallest gap between adjacent bands (refined) and
      the energy where it sits.
  pf: does det H6 change sign (zero-energy surface; a crossing of the H6 and -H6 sectors)?  min |E| of H6 (refined).
Then theta = pi/2 (real symmetric hop) zero flux: the E = 0 triple points and their slopes."""
import os, signal
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from scipy.optimize import minimize
from common import *
rng = np.random.default_rng(7)
G = grid(28)

def refine(f, starts):
    best = (np.inf, None)
    for k in starts:
        r = minimize(f, k, method="Nelder-Mead", options=dict(xatol=1e-11, fatol=1e-14, maxiter=1200))
        r = minimize(f, r.x, method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-15, maxiter=1200))
        if r.fun < best[0]: best = (r.fun, r.x)
    return best

def starts_of(vals, n=6):
    idx = np.argsort(vals)[:n]; return [G[i] for i in idx]

print("theta/pi | zero flux: det sign change, min 2nd-smallest|E| (grid -> refined), min adjacent gap (refined) at E "
      "| pi flux: det H6 sign change, min|E(H6)| (grid -> refined), min 2nd-smallest|E(H6)| refined")
for th in np.linspace(0, np.pi / 2, 9):
    M = M_family(th)
    H = H0(G, M); E = np.linalg.eigvalsh(H); dt = np.linalg.det(H).real
    flat = np.abs(E[:, 1]).max() < 1e-12
    sc = "flat band" if flat else f"{np.mean(dt > 1e-9):.2f}+/{np.mean(dt < -1e-9):.2f}-"
    a = np.sort(np.abs(E), 1)
    z2g = a[:, 1].min()
    f2 = lambda k: np.sort(np.abs(np.linalg.eigvalsh(H0(k, M))))[1]
    z2r, kz = refine(f2, starts_of(a[:, 1], 3))
    gaps = np.diff(E, axis=1); gm = gaps.min(0)
    out = []
    for n in range(2):
        fg = lambda k, n=n: np.diff(np.linalg.eigvalsh(H0(k, M)))[n]
        gr, kg = refine(fg, starts_of(gaps[:, n], 2))
        out.append(f"g{n}{n+1} {gr:.1e} at E={np.linalg.eigvalsh(H0(kg, M))[n]:+.3f}")
    H6g = H6(G, M); E6 = np.linalg.eigvalsh(H6g); d6 = np.linalg.det(H6g).real; del H6g
    a6 = np.sort(np.abs(E6), 1)
    f61 = lambda k: np.abs(np.linalg.eigvalsh(H6(k, M))).min()
    z61, k61 = refine(f61, starts_of(a6[:, 0], 2))
    f62 = lambda k: np.sort(np.abs(np.linalg.eigvalsh(H6(k, M))))[1]
    z62, k62 = refine(f62, starts_of(a6[:, 1], 2))
    print(f"{th/np.pi:.4f} | zf: {sc}; z2 {z2g:.2e} -> {z2r:.1e}; {'; '.join(out)} "
          f"| pf: {np.mean(d6 > 1e-9):.2f}+/{np.mean(d6 < -1e-9):.2f}-; z1 {a6[:,0].min():.2e} -> {z61:.1e}; z2 -> {z62:.1e}")

# theta = pi/2 (real symmetric H0 = sqrt2 (V + V^T)): E = 0 triple points where s_x = c_y, s_y = c_z, s_z = c_x
M = M_family(np.pi / 2)
q4 = np.pi / 4
import itertools
cands = [np.array(p) * q4 for p in itertools.product(range(-3, 5), repeat=3)]
trip = [k for k in cands if np.abs(H0(k, M)).max() < 1e-12]
print(f"theta=pi/2 zero flux: H0(k) = 0 exactly at {len(trip)} of the 512 points k in (pi/4)Z^3 mod 2pi")
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
for k in trip[:8]:
    sl = np.array([np.linalg.eigvalsh(H0(k + 1e-5 * d, M)) / 1e-5 for d in dirs])
    sl2 = np.array([np.linalg.eigvalsh(H0(k + 1e-3 * d, M)) / 1e-3 for d in dirs])
    print(f"   k/(pi/4) = {np.round(k / q4).astype(int)}: slopes over 300 dirs: low {sl[:,0].min():.3f}..{sl[:,0].max():.3f}, "
          f"mid {sl[:,1].min():.3f}..{sl[:,1].max():.3f}, up {sl[:,2].min():.3f}..{sl[:,2].max():.3f}; "
          f"q=1e-3 vs 1e-5 max diff {np.abs(sl-sl2).max():.1e}")
# same points at pi flux, theta = pi/2: H6 = 0 there too (all h_a vanish?) -> 6-fold zero
print("   same points, pi flux: max |H6| =", f"{max(np.abs(H6(k, M)).max() for k in trip):.1e}",
      "; per-direction blocks never vanish (eigenvalues 0, +-sqrt2 for every k): checked",
      f"{max(abs(np.sort(np.linalg.eigvalsh(blocks(rng.uniform(-3,3,3), M)[a])) - np.array([-np.sqrt(2),0,np.sqrt(2)])).max() for a in range(3) for _ in range(50)):.1e}")
