"""Independent referee for delay-of-the-rate-field-with-the-curvature-member a2.

Rebuilds the 7x7 pencil from R1, R2 and the kinetic term, and the continuum kernels.
Does not call the author's script. The 96^3 box is not rebuilt.
"""
import sys

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

FAILS = []
R = sp.Rational


def want(label, ok):
    if not ok:
        FAILS.append(label)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def hmat(v):
    return sp.Matrix([[v[0], v[3], v[4]], [v[3], v[1], v[5]], [v[4], v[5], v[2]]])


def member(p, H):
    p2 = (p.T * p)[0]
    tr = H.trace()
    R1 = -((p.T * H * p)[0] - p2 * tr)
    ph = H * p
    R2 = (
        -R(1, 4) * p2 * sum(H[i, j] ** 2 for i in range(3) for j in range(3))
        + R(1, 2) * (ph.T * ph)[0]
        - R(1, 2) * (p.T * H * p)[0] * tr
        + R(1, 4) * p2 * tr ** 2
    )
    return R1, R2, p2


def pencil(pv, al, be, K, w, hs, u):
    p = sp.Matrix(pv)
    H = hmat(hs)
    R1, R2, p2 = member(p, H)
    F2 = -K * w * (u * R1 + R2)
    xs = list(hs) + [u]
    dv = sp.symbols("d0:6")
    Hd = hmat(dv)
    T = (al * sum(Hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * Hd.trace() ** 2) / w
    M = sp.zeros(7)
    for a in range(6):
        for b in range(6):
            M[a, b] = sp.diff(T, dv[a], dv[b])
    V = sp.Matrix(7, 7, lambda i, j: sp.diff(F2, xs[i], xs[j]))
    return M, V, p2


s = sp.Symbol("s")
hs = sp.symbols("h11 h22 h33 h12 h13 h23")
u = sp.Symbol("u")

# ---------------------------------------------------------------- transfer function
ok = True
n = 0
cases = [
    ([0, 0, 1], (R(1), R(1, 2), R(1), R(1))),
    ([1, 2, 2], (R(2), R(-1, 3), R(3), R(1, 2))),
    ([R(1, 3), 1, 2], (R(1, 4), R(1, 5), R(7, 3), R(2))),
    ([R(2, 5), R(-1, 2), R(3, 4)], (R(1), R(1, 2), R(1), R(1))),
]
for pv, (al, be, K, w) in cases:
    M, V, p2 = pencil(pv, al, be, K, w, hs, u)
    b = sp.zeros(7, 1)
    b[6] = -1
    dom = QQ.frac_field(s)
    x = DomainMatrix.from_Matrix(s ** 2 * M + V).convert_to(dom).lu_solve(
        DomainMatrix.from_Matrix(b).convert_to(dom)
    )
    Hs = sp.cancel(dom.to_sympy(x[6, 0].element))
    target = -1 / (4 * K * w * p2) + al * (al + 3 * be) * s ** 2 / (K ** 2 * w ** 3 * (al + be) * p2 ** 2)
    denom = sp.denom(sp.together(Hs))
    ok = ok and sp.simplify(Hs - target) == 0 and denom.free_symbols == set()
    n += 1

alS, beS, KS, wS, PS = sp.symbols("alpha beta K wbar P", nonzero=True)
M, V, p2 = pencil([0, 0, PS], alS, beS, KS, wS, hs, u)
b = sp.zeros(7, 1)
b[6] = -1
dom = QQ.frac_field(s, alS, beS, KS, wS, PS)
x = DomainMatrix.from_Matrix(s ** 2 * M + V).convert_to(dom).lu_solve(
    DomainMatrix.from_Matrix(b).convert_to(dom)
)
Hs = sp.cancel(dom.to_sympy(x[6, 0].element))
target = -1 / (4 * KS * wS * p2) + alS * (alS + 3 * beS) * s ** 2 / (KS ** 2 * wS ** 3 * (alS + beS) * p2 ** 2)
ok = ok and sp.simplify(Hs - target) == 0
ok = ok and sp.degree(sp.together(Hs), s) == 2
want(f"T1 the 7x7 pencil gives u/e = -1/(4K wbar p^2) + C s^2/p^4 with no pole in s ({n} rational points and the symbolic axis)", ok)

# ---------------------------------------------------------------- rotation
a, b_, c = R(1, 3), R(-1, 2), R(1, 5)
Aa = sp.Matrix([[0, -c, b_], [c, 0, -a], [-b_, a, 0]])
Q = (sp.eye(3) - Aa) * (sp.eye(3) + Aa).inv()
ok = sp.simplify(Q.T * Q - sp.eye(3)) == sp.zeros(3) and sp.simplify(Q.det() - 1) == 0
p = sp.Matrix(sp.symbols("p1:4"))
H = hmat(hs)
R1, R2, _ = member(p, H)
R1r, R2r, _ = member(Q * p, Q * H * Q.T)
ok = ok and sp.expand(R1 - R1r) == 0 and sp.expand(R2 - R2r) == 0
Hd = hmat(sp.symbols("d0:6"))
kin = lambda X: sum(X[i, j] ** 2 for i in range(3) for j in range(3))
trc = lambda X: X.trace() ** 2
ok = ok and sp.expand(kin(Hd) - kin(Q * Hd * Q.T)) == 0 and sp.expand(trc(Hd) - trc(Q * Hd * Q.T)) == 0
want("T1 R1, R2 and the kinetic invariants are unchanged by a rational rotation, so H depends on p only through p^2", ok)

# ---------------------------------------------------------------- kernels
x, y, z = sp.symbols("x y z", real=True, positive=True)
r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
G = 1 / (4 * sp.pi * r)
B = -r / (8 * sp.pi)
ok = sp.simplify(lap(G)) == 0 and sp.simplify(lap(B) + G) == 0
Dx, Dy, Dz = sp.symbols("Dx Dy Dz")
D = sp.Matrix([Dx, Dy, Dz])
X = sp.Matrix([x, y, z])
grad = lambda f: sp.Matrix([sp.diff(f, v) for v in (x, y, z)])
dipB = -(D.T * grad(B))[0]
ok = ok and sp.simplify(dipB - (D.T * X)[0] / (8 * sp.pi * r)) == 0
hess = sp.Matrix(3, 3, lambda i, j: sp.diff(B, (x, y, z)[i], (x, y, z)[j]))
ok = ok and sp.simplify(hess + (sp.eye(3) - X * X.T / r ** 2) / (8 * sp.pi * r)) == sp.zeros(3)
mem = grad(dipB)
want_m = (D - X * (D.T * X)[0] / r ** 2) / (8 * sp.pi * r)
ok = ok and sp.simplify(mem - want_m) == sp.zeros(3, 1)
dipG = -(D.T * grad(G))[0]
ok = ok and sp.simplify(dipG - (D.T * X)[0] / (4 * sp.pi * r ** 3)) == 0
# Poisson clock: u = -1/(4 K wbar) * (G * e), so a dipole gives -(D.rhat)/(16 pi K wbar r^2)
Ks, ws = sp.symbols("K wbar", nonzero=True)
uP = -1 / (4 * Ks * ws) * dipG
ok = ok and sp.simplify(uP + (D.T * X)[0] / (16 * sp.pi * Ks * ws * r ** 3)) == 0
want("T2 continuum kernels: dipole Poisson clock -(D.rhat)/(16 pi K wbar r^2); B-part force and memory fall as 1/r", ok)

print(f"TOTAL FAIL={len(FAILS)}")
if FAILS:
    print("SUMMARY: fails at " + FAILS[0])
    sys.exit(1)
print(
    "HIT: confirmed - the clock transfer function is u/e = -1/(4K wbar p^2) + C s^2/p^4 with "
    "C = alpha(alpha+3 beta)/(K^2 wbar^3 (alpha+beta)), a polynomial in s, so the clock is not retarded. "
    "A ledger-kept dipole jump moves a distant packet at once by a dipole force and leaves a transverse 1/r memory from the C term."
)
print(
    "SUMMARY: confirmed the partial result for ledger-kept formation events. "
    "The 7x7 pencil and the continuum kernels were recomputed. The 96^3 lattice control was not rebuilt. "
    "Second order, moving bodies, and the branch alpha+beta=0 stay outside the claim."
)
