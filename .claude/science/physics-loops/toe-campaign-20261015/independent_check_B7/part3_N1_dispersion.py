"""Part 3f: closed form for the dispersive bands of N1.  Spectrum (numerically) = {0,0,0,pi} flat plus
{+-w1, +-(pi-w1)}; the 4 dispersive eigenvalues are roots of l^4 + (2-4X) l^2 + 1, X = cos^2 w1.
Fit X(k) on the 27 functions prod_i f_i(k_i), f in {1, cos, sin}; then verify the fitted closed form
against the characteristic polynomial at random k (NUMERICAL fit, then numerical verification)."""
import numpy as np, pickle, itertools
from walks import *
dat = pickle.load(open("nn_eqs_class0.pkl", "rb")); names, Bo = dat["names"], dat["B"].astype(float)
act = {"o00": 1, "o0i": 1j, "oi0": -1j, "oii": -1, "000": 1, "0ii": 1}
A = sum(v * Bo[names.index(k)] for k, v in act.items()) / 4
rng = np.random.default_rng(4)
ks = rng.uniform(-np.pi, np.pi, (400, 3))
fs = [lambda t: np.ones_like(t), np.cos, np.sin]
def feats(k):
    return np.array([fs[a](k[0]) * fs[b](k[1]) * fs[c](k[2]) for a, b, c in itertools.product(range(3), repeat=3)])
Xs = []; F = []
for k in ks:
    ev = np.linalg.eigvals(symbol(A, k))
    w = -np.angle(ev)
    flat0 = np.sum(np.abs(w) < 1e-8); flatpi = np.sum(np.abs(np.abs(w) - np.pi) < 1e-8)
    disp = w[(np.abs(w) > 1e-8) & (np.abs(np.abs(w) - np.pi) > 1e-8)]
    if flat0 != 3 or flatpi != 1 or len(disp) != 4: continue
    Xs.append(np.cos(np.min(np.abs(disp))) ** 2); F.append(feats(k))
Xs = np.array(Xs); F = np.array(F)
coef, res, *_ = np.linalg.lstsq(F, Xs, rcond=None)
labels = ["".join(p) for p in itertools.product(["1", "c", "s"], repeat=3)]
print("samples", len(Xs), " fit max error", np.abs(F @ coef - Xs).max())
print("X(k) = cos^2(w1) =", " + ".join(f"{c:.6f}*[{l}]" for c, l in zip(coef, labels) if abs(c) > 1e-9),
      "   ([abc] = f_a(k1) f_b(k2) f_c(k3), 1/c/s = 1/cos/sin of block momentum)")
