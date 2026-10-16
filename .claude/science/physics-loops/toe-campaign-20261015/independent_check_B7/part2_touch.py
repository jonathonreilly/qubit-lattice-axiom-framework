"""Part 2g: band touchings of spinorial two-layer examples (NUMERICAL: grid + Nelder-Mead refinement).
mode E1: qA = (I+K)/sqrt2, qB = (I+S1/sqrt3)/sqrt2  (bands found doubly degenerate everywhere -> look
         for points where two doublets meet: gap measure over windows of 4 eigenphases)
mode E2: qA,qB = given quaternion coefficients (generic or tuned): windows of 2.
Reports degeneracy points (mod symmetry duplicates) with quasienergy relative to the k=0 node(s),
and whether the node quasienergy omega0 is attained by any band elsewhere (Fermi surface)."""
import numpy as np, sys, json
from scipy.optimize import minimize
from walks import *
from part2_cone import Q, quat, eff_h

mode = sys.argv[1]
Nk = int(sys.argv[2]) if len(sys.argv) > 2 else 20
if mode == "E1":
    qA = (np.eye(8) + Q[0]) / np.sqrt(2); qB = (np.eye(8) + Q[1]) / np.sqrt(2); m = 4
else:
    co = json.loads(sys.argv[3]); qA = quat(co[:4]); qB = quat(co[4:]); m = 2
A = two_layer(qA.astype(complex), qB.astype(complex))
w0s = sorted(-np.angle(np.linalg.eigvals(qB @ qA)))
w0s = sorted(set(np.round(w0s, 8)))
print("mode", mode, "node quasienergies at k=0:", w0s, " unitarity", unitarity_defect(A))

def phases(k):
    return np.sort(np.mod(-np.angle(np.linalg.eigvals(symbol(A, k))), 2 * np.pi))
def gapm(k):
    p = phases(k); pe = np.concatenate([p, p + 2 * np.pi])
    return min(pe[i + m - 1] - pe[i] for i in range(8))
def where(k):
    p = phases(k); pe = np.concatenate([p, p + 2 * np.pi])
    i = int(np.argmin([pe[i + m - 1] - pe[i] for i in range(8)]))
    return np.mod(pe[i:i + m].mean(), 2 * np.pi)

ks = np.linspace(-np.pi, np.pi, Nk, endpoint=False) + np.pi / Nk * 0.5
grid = [np.array([a, b, c]) for a in ks for b in ks for c in ks]
vals = [(gapm(k), k) for k in grid]
vals.sort(key=lambda t: t[0])
found = []
for g, k in vals[:300]:
    r = minimize(gapm, k, method="Nelder-Mead", options=dict(xatol=1e-11, fatol=1e-14, maxiter=4000))
    if r.fun < 1e-6:
        kk = np.mod(r.x + np.pi, 2 * np.pi) - np.pi
        if not any(np.linalg.norm(np.mod(kk - f + np.pi, 2 * np.pi) - np.pi) < 1e-4 for f, _ in found):
            found.append((kk, where(kk)))
# include high-symmetry points explicitly
for name, k in [("Gamma", [0, 0, 0]), ("R", [np.pi] * 3), ("X", [np.pi, 0, 0]), ("M", [np.pi, np.pi, 0])]:
    p = phases(np.array(k, float))
    print(f"  {name}: eigenphases {np.round(p, 5)}")
print(f"{m}-fold degeneracy points found ({len(found)}), quasienergy omega (mod 2pi) and relative to nodes:")
for kk, w in sorted(found, key=lambda t: (t[1], tuple(np.round(np.abs(t[0]), 3)))):
    rel = [np.round(np.mod(w - w0 + np.pi, 2 * np.pi) - np.pi, 5) for w0 in w0s]
    print(f"  k={np.round(kk, 5)}  omega={w:.6f}  omega-omega0 = {rel}")
# Fermi surface test at each node quasienergy: min over k of distance of spectrum to omega0, away from Gamma
for w0 in w0s:
    dmin = 1e9; karg = None
    for k in grid:
        if np.linalg.norm(k) < 0.3: continue
        p = phases(k)
        d = np.min(np.abs(np.mod(p - w0 + np.pi, 2 * np.pi) - np.pi))
        if d < dmin: dmin, karg = d, k
    print(f"  node omega0={w0:+.5f}: min distance of spectrum to omega0 on grid away from Gamma: {dmin:.4f} at k={np.round(karg,3)}")
