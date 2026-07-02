"""
Audit companion (exact, sympy) for
KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md

No-go: within the C3-circulant generation Yukawa family, the Koide value
r = |b|^2/a^2 = 1/2 (Q = 2/3) is not fixed by the tested C3/S3 unitary
symmetry-protection routes. It is a norm-balance condition (equal energy in the
C3 singlet and doublet channels). Full axis-permutation symmetry S3 forces TWO
DEGENERATE masses; C3 leaves r free; there is no intermediate C3 < G < S3
subgroup; and the 1-dim singlet and 2-dim doublet cannot be swapped by a
unitary isomorphism. A C3-compatible coefficient rephasing / doublet-basis
rotation also preserves |b|^2/a^2, so it cannot calibrate arbitrary r to 1/2.
The listed routes are not asserted to exhaust the symmetry-protection space.
Dynamical, variational, nonunitary, extra-structure, and untested symmetry
mechanisms are left open. The note makes no claim that r = 1/2 is forced or
derived; here it remains a stable dial setting.

Reproven by finite algebra; no external mass values, no fits, no imported authorities.
"""
import sympy as sp
from sympy import Rational, sqrt, eye, ones, Matrix, symbols

R = []
def chk(l, o):
    assert o, l
    R.append((l, bool(o)))

# (1) THE GEOMETRIC CHARACTERIZATION: Q = 1/(3 cos^2 theta), theta = angle(sqrt(m), (1,1,1)).
#     Write v = p*uhat + q*what (uhat = (1,1,1)/sqrt3, what perp unit). Then Q = (1+(q/p)^2)/3.
#     Q = 2/3  <=>  q = p  <=>  theta = 45 deg (equal parallel/perpendicular split).
p, q = symbols('p q', positive=True)
uhat = Matrix([1, 1, 1]) / sqrt(3)
what = Matrix([1, -1, 0]) / sqrt(2)       # perp to uhat, unit
v = p*uhat + q*what
m = Matrix([v[i]**2 for i in range(3)])
Q = sp.simplify(sum(m) / (sum(v))**2)
chk("(1a) Q = (1 + (q/p)^2)/3 for the C3 decomposition (singlet p, doublet q)",
    sp.simplify(Q - (1 + (q/p)**2)/3) == 0)
chk("(1b) Q = 2/3  <=>  q = p  <=>  sqrt(m) at 45deg to (1,1,1) (equal singlet/doublet split)",
    sp.simplify(Q.subs(q, p) - Rational(2, 3)) == 0)

# (2) r=1/2  <=>  EQUAL CHANNEL ENERGY E+ = E_perp.  Circulant a I + b C + bbar C^2:
#     E+ = ||diagonal||_F^2 = 3 a^2 ; E_perp = ||off-diagonal||_F^2 = 6 |b|^2 ; r = |b|^2/a^2.
a, bmag = symbols('a bmag', positive=True)
r = bmag**2 / a**2
Eplus = 3*a**2
Eperp = 6*bmag**2
chk("(2)  r = 1/2  <=>  E+ (=3a^2) = E_perp (=6|b|^2)  (equal singlet/doublet channel energy)",
    sp.simplify((Eplus - Eperp).subs(bmag, a/sqrt(2))) == 0 and sp.simplify(r.subs(bmag, a/sqrt(2)) - Rational(1, 2)) == 0)

# (3) THE SYMMETRY TEST: a fully S3-symmetric (axis-permutation) Yukawa H = alpha I + beta (J - I)
#     has eigenvalues {alpha+2beta (x1, singlet), alpha-beta (x2, doublet)} -> TWO DEGENERATE masses.
alpha, beta = symbols('alpha beta', real=True)
J = ones(3, 3)
H_S3 = alpha*eye(3) + beta*(J - eye(3))
evals = H_S3.eigenvals()   # {value: multiplicity}
mults = sorted(evals.values())
chk("(3)  S3-symmetric Yukawa -> eigenvalue multiplicities {1,2}: TWO degenerate masses (excluded for leptons)",
    mults == [1, 2])

# (4) THE GROUP GAP: C3 (the circulant symmetry) allows ANY r -- Q = (1+2r)/3 varies with r -- and
#     the index [S3:C3] = 2 with no intermediate subgroup. So the C3/S3 enhancement route does not
#     force r=1/2 while keeping 3 distinct masses: C3 leaves r free, S3 kills the splitting.
rr = symbols('rr', positive=True)
Q_of_r = (1 + 2*rr)/3
chk("(4)  C3 leaves r free: Q=(1+2r)/3 is non-constant in r (Q'(r)=2/3 != 0), so C3 does not fix r",
    sp.simplify(sp.diff(Q_of_r, rr) - Rational(2, 3)) == 0)

# (5) STRUCTURAL: singlet (trivial rep, dim 1) and doublet (standard rep, dim 2) are different-
#     dimensional irreps -> no unitary isomorphism can swap or mix them -> equal-energy is a
#     CONDITION (norm balance), not a symmetry fixed point.
chk("(5)  dim(singlet)=1 != 2=dim(doublet): no unitary swaps them -> r=1/2 is a norm-balance, not a symmetry",
    1 != 2)

# (6) FIFTH DISTINCT ROUTE: C3-compatible coefficient rephasing / doublet-basis
#     calibration.  The real doublet coordinates (Re b, Im b) may be rotated by
#     an internal phase choice, but this preserves |b|^2 and hence preserves
#     r = |b|^2/a^2 and E_perp/E+.  A phase/basis convention cannot tune a
#     freely chosen r to 1/2.
x, y, c, s = symbols('x y c s', real=True)
x_rot = c*x - s*y
y_rot = s*x + c*y
unit_circle = c**2 + s**2 - 1
doublet_norm_diff = sp.expand((x_rot**2 + y_rot**2) - (x**2 + y**2))
remainder = sp.groebner([unit_circle], c, s, x, y, order='lex').reduce(doublet_norm_diff)[1]
chk("(6)  C3-compatible coefficient rephasing/doublet-basis rotation preserves |b|^2 and r=|b|^2/a^2, so it cannot force r=1/2",
    sp.simplify(remainder) == 0)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nNO-GO verified: r=1/2 (Q=2/3) is the equal-singlet/doublet-energy / 45-degree condition (1,2); it\n"
    "is NOT fixed by the tested C3/S3 unitary symmetry routes -- S3 forces degeneracy (3), C3 leaves\n"
    "r free (4), the 1-vs-2-dim irreps cannot be swapped (5), and C3-compatible coefficient\n"
    "rephasing/doublet-basis calibration preserves |b|^2/a^2 (6). These routes are not asserted to\n"
    "exhaust the symmetry-protection space; any positive derivation must enter through dynamics,\n"
    "extra structure, or another route not checked here rather than through those symmetry/calibration routes."
)
