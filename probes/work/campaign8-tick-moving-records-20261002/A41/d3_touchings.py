"""A41 d3: classify the touchings that d2 found.
 (A) zero flux, 0 < theta < pi/2: the band touchings at E = +-E_d (off zero): where, how many, dispersion in 300
     directions at two step sizes (linear in every direction? isotropic?).
 (B) pi flux, theta = pi/2: zeros of H6 although det H6 <= 0 everywhere: collect them by many refinements, cluster,
     test point vs line (count of distinct zeros vs number of starts; local shape), zero-mode multiplicity, slopes
     of the 12-band structure (spec H6 + spec(-H6)) around them.
 (C) pi flux, theta = pi/4: zero-energy set is a surface (det H6 changes sign): normal and tangent slopes."""
import os, signal
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(38)
import numpy as np
from scipy.optimize import minimize, brentq
from common import *
rng = np.random.default_rng(11)
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
NM = dict(xatol=1e-12, fatol=1e-15, maxiter=1500)
def wrap(k): return (k + np.pi) % (2 * np.pi) - np.pi
def cluster(pts, tol=1e-4):
    out = []
    for p in pts:
        if all(np.linalg.norm(wrap(p - q)) > tol for q in out): out.append(wrap(p))
    return out

# (A)
for th in (np.pi / 16, np.pi / 4):
    M = M_family(th); G = grid(20)
    E = np.linalg.eigvalsh(H0(G, M)); gap = E[:, 1] - E[:, 0]
    sols = []
    for i in np.argsort(gap)[:40]:
        f = lambda k: np.diff(np.linalg.eigvalsh(H0(k, M)))[0]
        r = minimize(f, G[i], method="Nelder-Mead", options=NM)
        if r.fun < 1e-9: sols.append(r.x)
    pts = cluster(sols)
    print(f"(A) zero flux theta={th/np.pi:.4f} pi: lower-pair touchings found from 40 starts: {len(pts)} distinct")
    for k in pts[:4]:
        e0 = np.linalg.eigvalsh(H0(k, M))
        rows = []
        for q in (1e-5, 1e-3):
            d = np.array([np.linalg.eigvalsh(H0(k + q * u, M))[:2] - e0[0] for u in dirs]) / q
            rows.append(d)
        sl = rows[0]; mn = np.abs(sl).min(0)
        print(f"    k/pi = {np.round(k/np.pi, 5)} E = {e0[0]:+.6f} (third band {e0[2]:+.4f}): slopes q=1e-5 band0 "
              f"{sl[:,0].min():.4f}..{sl[:,0].max():.4f}, band1 {sl[:,1].min():.4f}..{sl[:,1].max():.4f}; "
              f"smallest |slope| {mn.min():.2e}; slope(q=1e-3) - slope(q=1e-5) max {np.abs(rows[1]-rows[0]).max():.1e}")
        # direction of softest slope and its scaling: is E - E0 ~ q^2 there?
        j = np.argmin(np.abs(sl[:, 1] - sl[:, 0])); u = dirs[j]
        sp = [np.diff(np.linalg.eigvalsh(H0(k + q * u, M))[:2])[0] for q in (1e-4, 1e-3, 1e-2)]
        print(f"      splitting along the softest of 300 directions at q=1e-4,1e-3,1e-2: {[f'{x:.2e}' for x in sp]}")
        # exact soft direction: the eigvec analysis -- splitting along the node's fast axis (body diagonal) and perpendicular
        for name, u in (("[111]", np.ones(3) / np.sqrt(3)), ("[1-10]", np.array([1, -1, 0]) / np.sqrt(2)),
                        ("[11-2]", np.array([1, 1, -2]) / np.sqrt(6))):
            sp = [np.diff(np.linalg.eigvalsh(H0(k + q * u, M))[:2])[0] for q in (1e-4, 1e-3, 1e-2)]
            print(f"      splitting along {name}: {[f'{x:.2e}' for x in sp]}")

# (B)
M = M_family(np.pi / 2); G = grid(24)
E6 = np.linalg.eigvalsh(H6(G, M)); a1 = np.abs(E6).min(1)
print(f"(B) pi flux theta=pi/2: det H6 max on grid {np.linalg.det(H6(G, M)).real.max():.2e} (never positive); "
      f"min|E| on grid {a1.min():.2e}")
sols = []
f = lambda k: np.abs(np.linalg.eigvalsh(H6(k, M))).min()
for i in np.argsort(a1)[:60]:
    r = minimize(f, G[i], method="Nelder-Mead", options=NM)
    if r.fun < 1e-9: sols.append(r.x)
pts = cluster(sols)
print(f"    zeros from 60 starts: {len(sols)} converged, {len(pts)} distinct (mod 2pi)")
for k in pts[:6]:
    e = np.linalg.eigvalsh(H6(k, M)); nz = int(np.sum(np.abs(e) < 1e-7))
    sl = []
    for q in (1e-5, 1e-3):
        s = []
        for u in dirs:
            e6 = np.linalg.eigvalsh(H6(k + q * u, M)); e12 = np.sort(np.concatenate([e6, -e6]))
            s.append(e12[6 - nz:6 + nz] / q)
        sl.append(np.array(s))
    print(f"    k/pi = {np.round(k/np.pi, 5)}: zero modes of H6 {nz} (so {2*nz} of the 12 bands at E=0); "
          f"other |E| min {np.sort(np.abs(e))[nz]:.4f}; slopes of the {2*nz} bands: per band min..max "
          f"{'; '.join(f'{sl[0][:,j].min():.3f}..{sl[0][:,j].max():.3f}' for j in range(2*nz))}; "
          f"q=1e-3 vs 1e-5 max diff {np.abs(sl[1]-sl[0]).max():.1e}")
# line test: from a found zero, does the zero continue along some direction? minimize f on spheres of radius r
if pts:
    k0 = pts[0]
    for r in (1e-3, 1e-2, 5e-2):
        best = min(f(k0 + r * u) for u in dirs)
        print(f"    around the first zero: min over 300 directions of min|E| at radius {r:.0e}: {best:.2e} "
              f"(linear point ~ r*slope_min; a line through it would give ~0)")

# (C)
M = M_family(np.pi / 4); res = []
for _ in range(300):
    k = rng.uniform(-np.pi, np.pi, 3); u = rng.normal(size=3); u /= np.linalg.norm(u)
    g = lambda s: np.linalg.det(H6(k + s * u, M)).real
    ss = np.linspace(-1, 1, 21); gv = [g(s) for s in ss]
    for i in range(20):
        if gv[i] * gv[i + 1] < 0:
            s0 = brentq(g, ss[i], ss[i + 1], xtol=1e-14); k0 = k + s0 * u
            e = np.linalg.eigvalsh(H6(k0, M)); j = np.argmin(np.abs(e))
            gr = np.array([(np.linalg.eigvalsh(H6(k0 + 1e-6 * E3[c], M))[j] - np.linalg.eigvalsh(H6(k0 - 1e-6 * E3[c], M))[j]) / 2e-6 for c in range(3)])
            res.append((abs(e[j]), np.linalg.norm(gr), np.sort(np.abs(e))[1])); break
res = np.array(res)
print(f"(C) pi flux theta=pi/4: {len(res)} points on the zero set: |E| max {res[:,0].max():.1e}; |grad E| of the zero band "
      f"{res[:,1].min():.3f}..{res[:,1].max():.3f} (normal slope; tangent slopes vanish by construction); "
      f"next |E| min {res[:,2].min():.3f}")
