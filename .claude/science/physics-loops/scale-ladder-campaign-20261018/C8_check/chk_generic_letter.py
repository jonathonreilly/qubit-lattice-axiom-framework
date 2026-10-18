"""C8 check (e) supplement: does ANY O-symmetric translation-invariant letter act as a scalar on D+- at k*, with compressed
derivative proportional to S's (so it can only rescale the isotropic k* speed)?  Random group-averaged range-2 letters."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mymodel import *
from scipy.linalg import expm
rng = np.random.default_rng(8805); kst = np.array([1, -1, 1]) * np.pi / 2
def sym_avg(X):
    acc = {}
    for g in PROPER:
        for a, B in conjG(g, X).items(): acc[a] = acc.get(a, 0) + B / 24
    return acc
def rand_letter():
    X = {}
    for a in itertools.product((-2, -1, 0, 1, 2), repeat=3):
        if sum(abs(x) for x in a) <= 2 and rng.random() < 0.5: X[a] = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
    H = sym_avg(X); Hh = {}
    for a, B in H.items(): Hh[a] = Hh.get(a, 0) + B / 2
    for a, B in dag(H).items(): Hh[a] = Hh.get(a, 0) + B / 2
    return Hh                                         # O-symmetric Hermitian; the letter is U(k) = exp(i H(k))
def comp(Uf, k, D, h=1e-6):
    U = Uf(k); UD = D.conj().T @ U @ D; pres = np.allclose(U @ D, D @ UD, atol=1e-8); sc = np.allclose(UD, UD[0, 0] * np.eye(2), atol=1e-8)
    hs = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h; G = (Uf(k + dk) - Uf(k - dk)) / (2 * h); hs.append(-1j * D.conj().T @ U.conj().T @ G @ D)
    return pres and sc, [(x + x.conj().T) / 2 for x in hs]
_, hS = comp(lambda k: Sk(k, 1), kst, DP); _, hSm = comp(lambda k: Sk(k, 1), kst, DM)
okall = True; cs = []
for t in range(12):
    H = rand_letter(); Uf = lambda k: expm(1j * bloch(H, k))
    for D, href in ((DP, hS), (DM, hSm)):
        sc, h = comp(Uf, kst, D)
        num = sum(np.vdot(a.flatten(), b.flatten()) for a, b in zip(href, h)).real; den = sum(np.vdot(a.flatten(), a.flatten()).real for a in href)
        c = num / den; res = max(np.abs(b - c * a).max() for a, b in zip(href, h))
        okall &= sc and res < 1e-6; cs.append(round(c, 4))
print("[%s] 12 random O-symmetric range-2 letters exp(iH): scalar on D+ and D- at k*, compressed derivative = c * (S's), c real" % ('PASS' if okall else 'FAIL'))
print("   sample coefficients c:", cs[:12])
