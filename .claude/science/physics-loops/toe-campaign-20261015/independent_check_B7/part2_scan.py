"""Part 2d: explicit spinorial example  W(k) = G(k) qB G(k)^dag qA,
   qA = cos(a) I + sin(a) K,  qB = cos(b) I + sin(b) S1/sqrt3   (real orthogonal 8x8)
Scan the Brillouin zone for band degeneracies (NUMERICAL: grid + local refinement), report their
quasienergies, and check whether the k=0 node quasienergies are reached elsewhere."""
import numpy as np, sys
from scipy.optimize import minimize
from walks import *
from part2_cone import Q, eff_h, Wk
a = float(sys.argv[1]) if len(sys.argv) > 1 else np.pi / 4
b = float(sys.argv[2]) if len(sys.argv) > 2 else np.pi / 4
Nk = int(sys.argv[3]) if len(sys.argv) > 3 else 24
qA = np.cos(a) * np.eye(8) + np.sin(a) * Q[0]
qB = np.cos(b) * np.eye(8) + np.sin(b) * Q[1]
A = two_layer(qA.astype(complex), qB.astype(complex))
print(f"a={a:.4f} b={b:.4f}: covariance {covariance_defect(A, class_D(3)):.1e}  unitarity {unitarity_defect(A):.1e}"
      f"  max site displacement {site_disp_max(A)}")
nz = [(tuple(n), np.round(np.abs(A[i]).max(), 4)) for i, n in enumerate(OFFS) if np.abs(A[i]).max() > 1e-12]
print("nonzero offsets:", len(nz))
W0 = qB @ qA
print("W(0) eigenphases (omega = -arg):", np.round(np.sort(-np.angle(np.linalg.eigvals(W0))), 6))
for lam, P, hs in eff_h(qA, qB):
    print(f" node omega0={-np.angle(lam):+.6f}: v(100)={np.round(np.linalg.eigvalsh(hs[0]),5)}"
          f" v(110)={np.round(np.linalg.eigvalsh((hs[0]+hs[1])/np.sqrt(2)),5)} v(111)={np.round(np.linalg.eigvalsh(sum(hs)/np.sqrt(3)),5)}")

def phases(k):
    return np.sort(np.mod(-np.angle(np.linalg.eigvals(symbol(A, k))), 2 * np.pi))
def mingap(k):
    p = phases(k)
    g = np.diff(np.concatenate([p, [p[0] + 2 * np.pi]]))
    return g.min()
# grid
ks = np.linspace(-np.pi, np.pi, Nk, endpoint=False)
cands = []
allp = []
for kx in ks:
    for ky in ks:
        for kz in ks:
            k = np.array([kx, ky, kz])
            p = phases(k); allp.append(p)
            g = np.diff(np.concatenate([p, [p[0] + 2 * np.pi]]))
            cands.append((g.min(), k))
allp = np.array(allp)
cands.sort(key=lambda t: t[0])
found = []
for g, k in cands[:400]:
    r = minimize(lambda x: mingap(x), k, method="Nelder-Mead", options=dict(xatol=1e-10, fatol=1e-13, maxiter=3000))
    if r.fun < 1e-6:
        kk = np.mod(r.x + np.pi, 2 * np.pi) - np.pi
        if not any(np.linalg.norm(np.mod(kk - f + np.pi, 2 * np.pi) - np.pi) < 1e-4 for f, _ in found):
            p = phases(kk); gg = np.diff(np.concatenate([p, [p[0] + 2 * np.pi]]))
            i = np.argmin(gg)
            found.append((kk, p[i]))
print(f"degeneracy points found (refined from {Nk}^3 grid; NUMERICAL):", len(found))
for kk, w in sorted(found, key=lambda t: t[1]):
    p = phases(kk)
    mult = np.sum(np.abs(np.mod(p - w + np.pi, 2 * np.pi) - np.pi) < 1e-4)
    print(f"  k = {np.round(kk, 5)}  omega = {w:.6f} ({np.mod(w+np.pi,2*np.pi)-np.pi:+.6f})  multiplicity {mult}")
# band ranges
print("band ranges (omega in [0,2pi), sorted bands):")
for j in range(8):
    print(f"  band {j}: [{allp[:, j].min():.4f}, {allp[:, j].max():.4f}]")
