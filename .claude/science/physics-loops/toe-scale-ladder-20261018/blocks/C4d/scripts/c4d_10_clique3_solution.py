"""C4d-10: k=3, G=T: extract an explicit numerical solution of the full W_3-only constraint system
(unitarity + spectator isometries, given P(2) = Theorem P1) with prescribed weight mu on
COM-moving (or off-diagonal) amplitudes, then compute the clique-walk Bloch bands W_3(K) on a
K-grid and report the band width (dispersion => candidate triple transport at the W-only level).
Evidence only; the residual is reported."""
import sys, runpy
import numpy as np
mode = sys.argv[1] if len(sys.argv) > 1 else "moving"
mu = float(sys.argv[2]) if len(sys.argv) > 2 else 0.1
NTR = int(sys.argv[3]) if len(sys.argv) > 3 else 6
NFEV = int(sys.argv[4]) if len(sys.argv) > 4 else 500
sys.argv = ["c4d_08_clique_numeric.py", "3"]
src = open("c4d_08_clique_numeric.py").read()
src = src.split("rng = np.random.default_rng(11)")[0]   # reuse system construction only
ns = {}
exec(compile(src, "c4d_08_clique_numeric.py", "exec"), ns)
from scipy.optimize import least_squares
from c4d_common import check, total
import c4d_common
c4d_common.PASS = c4d_common.FAIL = 0
live, n, make, offdiag, moving = ns["live"], ns["n"], ns["make"], ns["offdiag"], ns["moving"]
classes, Wcol, zero, K = ns["classes"], ns["Wcol"], ns["zero"], ns["K"]
mask = moving if mode == "moving" else offdiag
rng = np.random.default_rng(23)
best = None
for trial in range(NTR):
    fun, jac = make(mu, mask)
    s = least_squares(fun, rng.normal(size=2 * n) * 0.3, jac=jac, method="trf", max_nfev=NFEV,
                      xtol=1e-15, ftol=1e-15, gtol=1e-15)
    c = float(np.sum(s.fun ** 2))
    if best is None or c < best[0]:
        best = (c, s.x)
cost, z = best
x = z[:n] + 1j * z[n:]
print(f"mode={mode} mu={mu}: best residual cost {cost:.3e}")
val = {kk: x[i] for i, kk in enumerate(live)}
# Bloch matrix over translation classes; anchor = lexmin site
pos = {Y: a for a, Y in enumerate(classes)}


def anchor_class(Yp):
    m = min(Yp)
    return frozenset(tuple(q - w for q, w in zip(s, m)) for s in Yp), m


def bloch(Kv):
    M = np.zeros((len(classes), len(classes)), complex)
    for b, Y in enumerate(classes):
        for Yp, (kk, f) in Wcol(Y, False).items():
            if kk in zero:
                continue
            cls, m = anchor_class(Yp)
            M[pos[cls], b] += val[kk] * np.exp(-1j * np.dot(Kv, m))
    return M


Ks = [np.array(k) * 2 * np.pi / 6 for k in np.ndindex(6, 6, 6)]
ph = []
unit_err = 0
for Kv in Ks:
    M = bloch(Kv)
    unit_err = max(unit_err, np.max(np.abs(M.conj().T @ M - np.eye(len(classes)))))
    ph.append(np.sort(np.angle(np.linalg.eigvals(M))))
ph = np.array(ph)
# band width: compare sorted eigenphase sets across K (phase-wrap safe via spectrum distance)
def specdist(a, b):
    return max(min(abs(np.exp(1j * u) - np.exp(1j * v)) for v in b) for u in a)
width = max(specdist(ph[0], p) for p in ph)
mvw = sum(abs(val[kk]) ** 2 for kk, mflag in zip(live, mask) if mflag)
print(f"max |W(K)^dag W(K) - 1| over grid = {unit_err:.2e}; moving/offdiag weight in solution = {mvw:.3f}")
print(f"spectral variation over 6^3 K-grid (max over K of Hausdorff distance on the unit circle) = {width:.3e}")
check("solution satisfies the W_3-only system to 1e-10", cost < 1e-10, f"{cost:.2e}")
check("W_3(K) unitary on grid to 1e-5", unit_err < 1e-5)
print("DISPERSIVE" if width > 1e-4 else "FLAT", "bands for this solution")
total()
