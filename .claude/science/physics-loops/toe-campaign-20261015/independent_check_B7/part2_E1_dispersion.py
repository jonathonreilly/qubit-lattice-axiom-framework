"""Part 2h: closed form for the spinorial example E1: W = G qB G^dag qA, qA=(I+K)/sqrt2, qB=(I+S1/sqrt3)/sqrt2.
Numerically: each band doubly degenerate; eigenphases +-w_a, +-w_b.  Fit the symmetric functions
s1 = cos w_a + cos w_b and s2 = cos w_a cos w_b on the 27 trig monomials (degree <=1 per axis) and on
squares if needed; verify. NUMERICAL fit + verification."""
import numpy as np, itertools
from walks import *
from part2_cone import Q
qA = (np.eye(8) + Q[0]) / np.sqrt(2); qB = (np.eye(8) + Q[1]) / np.sqrt(2)
A = two_layer(qA.astype(complex), qB.astype(complex))
rng = np.random.default_rng(9); ks = rng.uniform(-np.pi, np.pi, (500, 3))
fs = [lambda t: np.ones_like(t), np.cos, np.sin, lambda t: np.cos(2 * t), lambda t: np.sin(2 * t)]
labels = ["".join(p) for p in itertools.product(["1", "c", "s", "C", "S"], repeat=3)]
def feats(k): return np.array([fs[a](k[0]) * fs[b](k[1]) * fs[c](k[2]) for a, b, c in itertools.product(range(5), repeat=3)])
S1 = []; S2 = []; F = []; degmax = 0
for k in ks:
    W = symbol(A, k)
    ev = np.linalg.eigvals(W); w = np.sort(-np.angle(ev))
    # check double degeneracy and +- symmetry
    tr = np.trace(W).real / 4         # = cos wa + cos wb  if each of +-wa,+-wb doubly degenerate
    tr2 = (np.trace(W @ W).real / 4 + 2) / 4   # (cos 2wa + cos 2wb)/2 + 1 /2 ... = (cos^2 wa + cos^2 wb)/2
    s1 = tr; s2 = (s1 ** 2 - 2 * tr2) / 2   # cos wa cos wb = (s1^2 - (cos^2 a + cos^2 b))/2
    S1.append(s1); S2.append(s2); F.append(feats(k))
F = np.array(F)
for nm, y in [("cos wa + cos wb", np.array(S1)), ("cos wa * cos wb", np.array(S2))]:
    coef, *_ = np.linalg.lstsq(F, y, rcond=None)
    print(nm, "= ", " + ".join(f"{c:+.6f}[{l}]" for c, l in zip(coef, labels) if abs(c) > 1e-8), "  max fit err", np.abs(F @ coef - y).max())
print("([abc]: f(k1)f(k2)f(k3); 1=1, c=cos k, s=sin k, C=cos 2k, S=sin 2k; k = block momentum)")
