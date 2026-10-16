"""EXACT (sympy) proof of the closed-form spectra, avoiding the 8x8 symbolic determinant:
for W(x) (x_i = e^{i k_i}) show (a) q(W) = 0 for the claimed polynomial q, (b) tr W^j equals the
claimed power sums for enough j to fix multiplicities (roots of q generically distinct), plus exact
unitarity.  E1: q = (l^2+1)^2 - 2 l (l^2+1) + 4 P l^2, each root double, P = 1/8 + (1/48) sum (x^2+x^-2).
N1: eigenvalue 1 (x3), -1 (x1), and roots of l^4 + (2-4X) l^2 + 1, X = (1 + sum_{a<b} C_a C_b)/4,
C = (x + 1/x)/2."""
import sympy as sp, numpy as np, pickle
from walks import OFFS, corners
from quat import x56 as K, x62 as S1
x = sp.symbols('x1:4'); l = sp.symbols('l')
def ex(M): return M.applyfunc(lambda e: sp.expand(e))
I8 = sp.eye(8)
G = sp.diag(*[sp.Mul(*[x[j] ** int(v[j]) for j in range(3)]) for v in corners])
Gi = sp.diag(*[sp.Mul(*[x[j] ** (-int(v[j])) for j in range(3)]) for v in corners])
qA = (I8 + sp.Matrix(K.tolist())) / sp.sqrt(2); qB = (I8 + sp.Matrix(S1.tolist()) / sp.sqrt(3)) / sp.sqrt(2)
W = ex(G * qB * Gi * qA)
P = sp.Rational(1, 8) + sp.Rational(1, 48) * sum(xi ** 2 + xi ** -2 for xi in x)
W2 = ex(W * W); W3 = ex(W2 * W); W4 = ex(W3 * W)
qW = ex(W4 - 2 * W3 + (2 + 4 * P) * W2 - 2 * W + I8)
print("E1: q(W) == 0 exactly:", all(sp.simplify(e) == 0 for e in qW))
# power sums of roots of q: q = l^4 - 2 l^3 + (2+4P) l^2 - 2 l + 1 ; Newton: p1 = 2, p2 = 2^2 - 2(2+4P), p3 = ...
e1, e2, e3 = 2, 2 + 4 * P, 2
p1 = e1; p2 = e1 * p1 - 2 * e2; p3 = e1 * p2 - e2 * p1 + 3 * e3
for j, (Wj, pj) in enumerate([(W, p1), (W2, p2), (W3, p3)], 1):
    print(f"E1: tr W^{j} == 2 * p{j}(q):", sp.simplify(sp.expand(Wj.trace() - 2 * pj)) == 0)
# ---- N1
dat = pickle.load(open("nn_eqs_class0.pkl", "rb")); names, Bo = dat["names"], dat["B"].astype(int)
act = {"o00": 1, "o0i": sp.I, "oi0": -sp.I, "oii": -1, "000": 1, "0ii": 1}
WN = sp.zeros(8, 8)
for kn, v in act.items():
    Bk = Bo[names.index(kn)]
    for i, n in enumerate(OFFS):
        if np.abs(Bk[i]).max():
            WN += v * sp.Matrix(Bk[i].tolist()) * sp.Mul(*[x[j] ** int(n[j]) for j in range(3)])
WN = ex(WN / 4)
WNd = ex(WN.T.applyfunc(lambda e: sp.conjugate(e)).subs({sp.conjugate(xi): 1 / xi for xi in x}, simultaneous=True))
print("N1 unitarity exact:", all(sp.simplify(e) == 0 for e in ex(WNd * WN - I8)))
C = [(xi + 1 / xi) / 2 for xi in x]
X = (1 + C[0] * C[1] + C[1] * C[2] + C[2] * C[0]) / 4
Wp = [I8, WN]
for j in range(2, 7): Wp.append(ex(Wp[-1] * WN))
qN = ex((Wp[1] - I8) * (Wp[1] + I8) * (Wp[4] + (2 - 4 * X) * Wp[2] + I8))
print("N1: q(W) == 0 exactly:", all(sp.simplify(e) == 0 for e in qN))
# dispersive roots r: r^4 + (2-4X) r^2 + 1: power sums: odd = 0; p2 = -2(2-4X); p4 = p2^2/... use Newton with e1=0,e2=2-4X,e3=0,e4=1
# simpler: compute power sums symbolically from roots r^2 = y, y^2 + (2-4X) y + 1 = 0 -> y1+y2 = 4X-2, y1 y2 = 1
y1, y2 = sp.symbols('y1 y2')
def ps(j):  # sum over 4 roots r of r^j: odd -> 0, even 2m -> 2 (y1^m + y2^m)
    if j % 2: return 0
    m = j // 2
    expr = sp.expand(2 * (y1 ** m + y2 ** m))
    # reduce symmetric poly via elementary s = y1+y2, t = y1 y2
    s, t = sp.symbols('s t')
    from sympy.polys.polyfuncs import symmetrize
    sym = symmetrize(expr, [y1, y2], formal=True)
    val = sym[0].subs({sym[2][0][0]: 4 * X - 2, sym[2][1][0]: 1})
    return val
for j in range(1, 7):
    claim = 3 + (-1) ** j + ps(j)
    print(f"N1: tr W^{j} == 3 + (-1)^{j} + sum r^{j}:", sp.simplify(sp.expand(Wp[j].trace() - claim)) == 0)
