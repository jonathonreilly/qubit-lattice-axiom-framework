"""EXACT (sympy) verification of the closed-form spectra of E1 (spinorial, two-layer) and N1
(bosonic, nearest-site): exact symbol W(x), x_i = e^{i k_i}; exact unitarity W^dag W = I; exact
characteristic polynomial compared with the claimed factorisation."""
import sympy as sp, numpy as np, pickle
from walks import OFFS, corners, idx, two_layer
from quat import x56 as K, x62 as S1
x = sp.symbols('x1:4'); lam = sp.symbols('lam')
def sym_W(Aint, scale):
    W = sp.zeros(8, 8)
    for i, n in enumerate(OFFS):
        if np.abs(Aint[i]).max() == 0: continue
        mon = sp.Mul(*[x[j] ** int(n[j]) for j in range(3)])
        W += sp.Matrix(Aint[i].tolist()) * mon
    return W * scale
def dag(W):  # conjugate transpose on the torus: x -> 1/x, complex-conjugate numbers
    return W.T.applyfunc(lambda e: sp.conjugate(e).subs({sp.conjugate(xi): 1 / xi for xi in x}))
# ---- E1: qA=(I+K)/sqrt2, qB=(I+S1/sqrt3)/sqrt2 ; work with exact sympy matrices directly
I8 = sp.eye(8); Km = sp.Matrix(K.tolist()); S1m = sp.Matrix(S1.tolist())
qA = (I8 + Km) / sp.sqrt(2); qB = (I8 + S1m / sp.sqrt(3)) / sp.sqrt(2)
G = sp.diag(*[sp.Mul(*[x[j] ** int(v[j]) for j in range(3)]) for v in corners])
Ginv = sp.diag(*[sp.Mul(*[x[j] ** (-int(v[j])) for j in range(3)]) for v in corners])
W = G * qB * Ginv * qA
Wd = qA.T * G * qB.T * Ginv            # real q's: W^dag = qA^T G qB^T G^-1 (G^dag = G^-1 on torus)
print("E1 unitarity exact:", sp.simplify(Wd * W - I8) == sp.zeros(8, 8))
cp = sp.expand(sp.simplify((lam * I8 - W).det(method='berkowitz')))
# claimed: prod over t in {cos wa, cos wb} (lam^2 - 2 t lam + 1)^2 with t^2 - t + P = 0
# => [ (lam^2+1)^2 - 2 lam (lam^2+1) (ta+tb) + 4 lam^2 ta tb ]^2 with ta+tb=1, ta tb = P
P = sp.Rational(1, 8) + sp.Rational(1, 48) * sum(xi ** 2 + xi ** -2 for xi in x)
claim = sp.expand(((lam ** 2 + 1) ** 2 - 2 * lam * (lam ** 2 + 1) + 4 * lam ** 2 * P) ** 2)
print("E1 charpoly matches closed form:", sp.simplify(cp - claim) == 0)
# ---- N1
dat = pickle.load(open("nn_eqs_class0.pkl", "rb")); names, Bo = dat["names"], dat["B"].astype(int)
act = {"o00": 1, "o0i": sp.I, "oi0": -sp.I, "oii": -1, "000": 1, "0ii": 1}
WN = sp.zeros(8, 8)
for kname, v in act.items():
    WN += v * sym_W(Bo[names.index(kname)], 1)
WN = WN / 4
WNd = WN.T.applyfunc(lambda e: sp.conjugate(e)).subs({sp.conjugate(xi): 1 / xi for xi in x}, simultaneous=True)
print("N1 unitarity exact:", sp.simplify(sp.expand(WNd * WN) - I8) == sp.zeros(8, 8))
cpN = sp.factor(sp.expand((lam * I8 - WN).det(method='berkowitz')))
X = sp.Rational(1, 4) * (1 + sum(((x[a] + 1 / x[a]) / 2) * ((x[b] + 1 / x[b]) / 2) for a, b in [(0, 1), (1, 2), (2, 0)]))
claimN = sp.expand((lam - 1) ** 3 * (lam + 1) * (lam ** 4 + (2 - 4 * X) * lam ** 2 + 1))
print("N1 charpoly:", cpN)
print("N1 charpoly matches (lam-1)^3 (lam+1) (lam^4 + (2-4X) lam^2 + 1):", sp.simplify(sp.expand(cpN) - claimN) == 0)
