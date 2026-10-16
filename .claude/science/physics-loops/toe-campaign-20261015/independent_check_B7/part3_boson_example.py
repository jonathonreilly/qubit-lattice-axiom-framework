"""Part 3e: spectrum of the exact bosonic nearest-site example N1 (class 0):
amplitude 1/4 x phase on hop types  o00:1, o0i:i, oi0:-i, oii:-1, 000:1, 0ii:1  (others 0).
k=0 levels, first-order (degenerate) perturbation theory, isotropy, small-k numerics, BZ scan of
degeneracies (NUMERICAL except where stated)."""
import numpy as np, pickle, sys
from scipy.optimize import minimize
from walks import *
from part2_cone import dirs
dat = pickle.load(open("nn_eqs_class0.pkl", "rb"))
names, Bo = dat["names"], dat["B"].astype(float)
act = {"o00": 1, "o0i": 1j, "oi0": -1j, "oii": -1, "000": 1, "0ii": 1}
if len(sys.argv) > 1 and sys.argv[1] == "mirror":
    act = {"o00": 1, "o0i": -1j, "oi0": 1j, "oii": -1, "000": 1, "0ii": 1}
A = sum(v * Bo[names.index(k)] for k, v in act.items()) / 4
D = class_D(0)
print("unitarity", unitarity_defect(A), "covariance", covariance_defect(A, D), "max site disp", site_disp_max(A))
# list hops of corner 0 explicitly
print("hops from corner (0,0,0) of block 0 [displacement: amplitude]:")
for i, n in enumerate(OFFS):
    for vo in corners:
        a = A[i, idx(vo), 0]
        if abs(a) > 1e-12:
            print("   ", tuple(vo - 0 - 2 * n), np.round(a, 4))
W0 = symbol(A, np.zeros(3))
w, V = np.linalg.eig(W0)
print("W(0) eigenphases omega=-arg:", np.round(np.sort(-np.angle(w)), 6))
dW = [sum(1j * n[j] * A[i] for i, n in enumerate(OFFS)) for j in range(3)]
for lam in np.unique(np.round(w, 7)):
    P = V[:, np.abs(w - lam) < 1e-6]; P, _ = np.linalg.qr(P)
    hs = [(1j / lam) * P.conj().T @ dW[j] @ P for j in range(3)]
    sp = np.array([np.sort(np.linalg.eigvalsh((sum(nn[j] * hs[j] for j in range(3)) + sum(nn[j] * hs[j] for j in range(3)).conj().T) / 2)) for nn in dirs(300)])
    herm = max(np.abs(h - h.conj().T).max() for h in hs)
    print(f" level omega0={-np.angle(lam):+.6f} mult {P.shape[1]}: herm defect {herm:.1e}; v(100)={np.round(np.linalg.eigvalsh(hs[0]),5)}"
          f" v(111)={np.round(np.linalg.eigvalsh(sum(hs)/np.sqrt(3)),5)}; spread over dirs {np.round(sp.max(0)-sp.min(0),6)}")
    for kn in [np.array([1, 0, 0]), np.array([1, 1, 1]) / np.sqrt(3), np.array([0.3, -0.5, 0.8]) / np.linalg.norm([0.3, -0.5, 0.8])]:
        for eps in [1e-3, 1e-4]:
            ev = np.linalg.eigvals(symbol(A, eps * kn))
            near = ev[np.abs(ev - lam) < 0.05]
            print(f"     |k|={eps:g} dir {np.round(kn,3)}: (omega-omega0)/|k| = {np.round(np.sort(-np.angle(near / lam) / eps), 5)}")
def phases(k): return np.sort(np.mod(-np.angle(np.linalg.eigvals(symbol(A, k))), 2 * np.pi))
def gap2(k):
    p = phases(k); pe = np.concatenate([p, p + 2 * np.pi]); return min(pe[i + 1] - pe[i] for i in range(8))
Nk = 14
ks = np.linspace(-np.pi, np.pi, Nk, endpoint=False) + 0.1
vals = sorted([(gap2(np.array([a, b, c])), np.array([a, b, c])) for a in ks for b in ks for c in ks], key=lambda t: t[0])
found = []
for g, k in vals[:150]:
    r = minimize(gap2, k, method="Nelder-Mead", options=dict(xatol=1e-11, fatol=1e-14, maxiter=3000))
    if r.fun < 1e-6:
        kk = np.mod(r.x + np.pi, 2 * np.pi) - np.pi
        if not any(np.linalg.norm(np.mod(kk - f + np.pi, 2 * np.pi) - np.pi) < 1e-4 for f, _ in found):
            p = phases(kk); pe = np.concatenate([p, p + 2 * np.pi]); i = np.argmin([pe[i + 1] - pe[i] for i in range(8)])
            found.append((kk, pe[i]))
print(f"two-fold degeneracies found away from grid ({len(found)}):")
for kk, wq in sorted(found, key=lambda t: t[1]):
    print(f"   k={np.round(kk,4)} omega={np.mod(wq+np.pi,2*np.pi)-np.pi:+.5f}")
for name, k in [("Gamma", [0, 0, 0]), ("R", [np.pi] * 3), ("X", [np.pi, 0, 0]), ("M", [np.pi, np.pi, 0])]:
    print(f"  {name}: eigenphases {np.round(np.mod(phases(np.array(k, float)) + np.pi, 2*np.pi) - np.pi, 5)}")
