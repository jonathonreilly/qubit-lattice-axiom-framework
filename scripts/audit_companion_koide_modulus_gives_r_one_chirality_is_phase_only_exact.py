#!/usr/bin/env python3
"""
Audit companion (exact/numeric, sympy+numpy) for
KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md

Physics-loop dirac-corner-coupling, block 6 (route-specific correction:
the tested determinant-modulus route does not supply the block-4/block-5
"chiral -> r=1/2" mechanism).

The load-bearing repo computation is the circulant primitive
M = aI + bC + bbar C^2.  The runner checks that the tested modulus
diagnostic is non-holomorphic in (Re b, Im b), has a rank-2 doublet
Hessian, and has the tested fixed-scale determinant stationary ratio r=1
rather than r=1/2.  Literature mentioned in the source note is comparator
context only, not a proof input.
"""
import numpy as np
import sympy as sp
from sympy import I, simplify, symbols, sqrt, Matrix, eye, conjugate

R = []
def chk(l, o): R.append((l, bool(o)))

# (1) M = aI + bC + bbar C^2 is HERMITIAN -> a vector-type mass has a REAL determinant.
a = symbols('a', real=True, positive=True); bre, bim = symbols('bre bim', real=True)
b = bre + I*bim; C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]]); M = a*eye(3) + b*C + conjugate(b)*(C*C)
chk("(1) M = aI+bC+bbar C^2 is Hermitian (vector mass -> determinant real)", simplify(M - M.H) == sp.zeros(3, 3))

# modulus effective potential V_mod = Tr log(M^dag M) = 2 sum_k log|lambda_k|, lambda_k = a+2|b|cos(theta+2pi k/3)
def Vmod(a_, br, bi):
    beta = np.hypot(br, bi); th = np.arctan2(bi, br)
    return sum(2*np.log(abs(a_ + 2*beta*np.cos(th + 2*np.pi*k/3))) for k in range(3))

# (2) V_mod depends on BOTH Re b and Im b, and the doublet Hessian has RANK 2 -> two genuine real modes
#     (NON-holomorphic). Holomorphic would be rank 1 (b counted once).
a0, br0, bi0, h = 2.0, 0.5, 0.3, 1e-5
dbr = (Vmod(a0, br0+h, bi0) - Vmod(a0, br0-h, bi0))/(2*h)
dbi = (Vmod(a0, br0, bi0+h) - Vmod(a0, br0, bi0-h))/(2*h)
Hrr = (Vmod(a0, br0+h, bi0) - 2*Vmod(a0, br0, bi0) + Vmod(a0, br0-h, bi0))/h**2
Hii = (Vmod(a0, br0, bi0+h) - 2*Vmod(a0, br0, bi0) + Vmod(a0, br0, bi0-h))/h**2
Hri = (Vmod(a0, br0+h, bi0+h) - Vmod(a0, br0+h, bi0-h) - Vmod(a0, br0-h, bi0+h) + Vmod(a0, br0-h, bi0-h))/(4*h**2)
rank = np.linalg.matrix_rank(np.array([[Hrr, Hri], [Hri, Hii]]), tol=1e-6)
chk("(2) modulus doublet Hessian on (Re b, Im b) has RANK 2 -> two real modes (non-holomorphic) -> (1,2) weighting",
    abs(dbr) > 1e-6 and abs(dbi) > 1e-6 and rank == 2)

# (3) the fixed-scale determinant branch is stationary in the shape at r=1 (not 1/2).
x = symbols('x', positive=True); ax = sqrt(x/3); bx = sqrt((1-x)/6)
detM = (ax + 2*bx)*(ax - bx)**2                                   # theta=0 eigenvalues a+2|b|, a-|b|, a-|b|
crit = [c for c in sp.solve(sp.Eq(simplify(sp.diff(detM, x)), 0), x) if c.is_real and 0 < c < 1]
rs = sorted(set(simplify((1 - c)/(2*c)) for c in crit))
chk("(3) fixed-scale determinant branch has stationary ratio r=1 (not 1/2)",
    rs == [sp.Integer(1)])

# (4) Hermitian (vector) M has REAL det. A phase/eta direction would be a separate
#     non-Hermitian/chiral computation, not this modulus ratio.
detval = complex(np.linalg.det(np.array(M.subs({a: a0, bre: br0, bim: bi0})).astype(complex)))
chk("(4) Hermitian M: det is real (im part ~0); phase/eta is separate from this modulus ratio",
    abs(detval.imag) < 1e-9)

# (5) holomorphy (b counted ONCE -> r=1/2) would require dV/d(bbar)=0. The modulus has rank-2 Hessian (2),
#     so it is NOT holomorphic; a rank-1 count is a different conditional structure.
chk("(5) rank-1 holomorphic counting is not supplied by the tested rank-2 modulus",
    rank == 2)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nROUTE-SPECIFIC CORRECTION: the tested fluctuation-determinant modulus is an\n"
    "|b|^2-type function with a rank-2 doublet Hessian, so this modulus route counts\n"
    "two real doublet modes and does not supply the prior chiral/holomorphic r=1/2\n"
    "mechanism. The tested fixed-scale determinant branch has stationary ratio r=1,\n"
    "not r=1/2. A phase/eta or holomorphic determinant construction would be a\n"
    "separate open route, not established by this runner."
)
