"""
Audit companion (exact, sympy) for
CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md

Physics-loop dirac-corner-coupling, block 1 (negative-route-pruning).
The three hw=1 BZ corners carry mass matrix M = a I + b C + bbar C^2 (kinetic D=0 at the corners),
so the corner Grassmann integral gives the fermion weight det(M). Question: does this fermion
weight select the balanced Koide r=|b|^2/a^2=1/2 (Q=2/3)? The ledger flagged the corner-coupling /
fermion-determinant as the #1 OPEN dynamical lead. This runner PRUNES it: det(M) is NOT stationary,
and has no extremum, at r=1/2; its special points are at r=1, r=4, and the boundaries r->0, r->inf.

CONDITIONAL on the open staggered-Dirac realization gate. No PDG values as derivation inputs.
"""
import sympy as sp
from sympy import sqrt, Rational, symbols, cos, diff, solve, simplify

R = []
def chk(l, o): R.append((l, bool(o)))

# circulant determinant on the corners: det(M) = a^3 - 3 a |b|^2 + 2 |b|^3 cos(3 delta).
a, bmag, delta = symbols('a bmag delta', positive=True)
detM = a**3 - 3*a*bmag**2 + 2*bmag**3*cos(3*delta)

# (1) delta-extremum: d/d(delta) det = -6 |b|^3 sin(3 delta) = 0 -> sin(3 delta)=0 -> cos(3 delta)=+/-1.
chk("(1) delta-stationary at sin(3 delta)=0 -> cos(3 delta)=+/-1",
    simplify(diff(detM, delta) + 6*bmag**3*sp.sin(3*delta)) == 0)

# Fix the Frobenius scale 3a^2 + 6|b|^2 = 1; parametrize by singlet energy fraction x=3a^2 in (0,1):
#   a=sqrt(x/3), |b|=sqrt((1-x)/6), r=|b|^2/a^2=(1-x)/(2x).  x=1/2 <-> r=1/2.
x = symbols('x', positive=True)
a_x = sqrt(x/Rational(3)); b_x = sqrt((1-x)/Rational(6))
def r_of(xv): return simplify((1-xv)/(2*xv))

for sgn, name in [(1, "cos3d=+1"), (-1, "cos3d=-1")]:
    det_x = a_x**3 - 3*a_x*b_x**2 + 2*sgn*b_x**3
    dd = simplify(diff(det_x, x))
    crit = [c for c in solve(sp.Eq(dd, 0), x) if c.is_real and 0 < c < 1]
    # the stationary point(s) -> r value(s)
    rs = sorted(set(simplify(r_of(c)) for c in crit))
    chk(f"(2{name}) det stationary in shape at r in {[str(rv) for rv in rs]} (NOT 1/2)",
        all(simplify(rv - Rational(1,2)) != 0 for rv in rs) and len(rs) >= 1)
    # explicitly: derivative NONZERO at x=1/2 (r=1/2) -> r=1/2 is not a stationary point
    chk(f"(3{name}) d(det)/dx != 0 at x=1/2 (r=1/2): r=1/2 is NOT a det stationary point",
        simplify(dd.subs(x, Rational(1,2))) != 0)

# (4) the det's special points are r=1 (det=0, two masses degenerate) and r=4 (cos3d=-1 branch),
#     plus the boundaries -- none is the balanced r=1/2. r=1 check: at x=1/3, cos3d=+1, det=0.
det_13 = (a_x**3 - 3*a_x*b_x**2 + 2*b_x**3).subs(x, Rational(1,3))
chk("(4) at r=1 (x=1/3, cos3d=+1) the determinant VANISHES (two-fold mass degeneracy), not a balanced vacuum",
    simplify(det_13) == 0 and simplify(r_of(Rational(1,3)) - 1) == 0)

# (5) CONTRAST: r=1/2 IS the max-sector-entropy point (equal singlet/doublet energy, S=log2), but it is
#     NOT a det stationary point (3) -> the dynamical (det) criterion and the balanced criterion DISAGREE.
#     sector energy fractions f+ = 3a^2/(3a^2+6|b|^2) = x ; f_perp = 1-x ; binary entropy max at x=1/2.
S = -x*sp.log(x) - (1-x)*sp.log(1-x)
chk("(5) max-sector-entropy at x=1/2 (r=1/2): dS/dx=0 there and S=log2",
    simplify(diff(S, x).subs(x, Rational(1,2))) == 0 and simplify(S.subs(x, Rational(1,2)) - sp.log(2)) == 0)

# ---- Cycle 2: the FULL one-loop effective potential, not just the bare determinant ----
# Fermion one-loop Coleman-Weinberg on the 3 corner modes: V_ferm = -Tr log M. On
# a fixed nonzero determinant-sign branch this is read as -log|det(M)|, so its
# shape-stationary points equal det's -> still r=1, r=4, boundaries; still NOT r=1/2.
det_plus = a_x**3 - 3*a_x*b_x**2 + 2*b_x**3
det_minus = a_x**3 - 3*a_x*b_x**2 - 2*b_x**3
V_ferm_plus = -sp.log(det_plus)
V_ferm_minus = -sp.log(-det_minus)
chk("(6) CW fermion potential V_ferm=-log|det(M)| branchwise: d/dx != 0 at x=1/2 on both branches",
    simplify(diff(V_ferm_plus, x).subs(x, Rational(1,2))) != 0
    and simplify(diff(V_ferm_minus, x).subs(x, Rational(1,2))) != 0)

# (7) any scalar potential depending ONLY on the Frobenius scale invariant s=3a^2+6|b|^2 is CONSTANT on the
#     fixed-scale slice (s=1), so it adds 0 to d/dx and CANNOT move the shape-stationary point onto r=1/2.
g2, g3 = symbols('g2 g3', real=True)
s_inv = 3*a_x**2 + 6*b_x**2                 # = 1 identically on the slice
V_scalar_inv = g2*s_inv**2 + g3*s_inv**3
chk("(7) any scale-only scalar potential is x-flat on the fixed-scale slice -> cannot create an r=1/2 vacuum",
    simplify(diff(V_scalar_inv, x)) == 0)

# (7b) hence the combined one-loop V_eff = V_scalar(scale) + V_ferm has the SAME shape-stationary points
#      as V_ferm alone: NOT r=1/2. This upgrades Cycle 1 (bare det) to the full effective potential.
V_eff_plus = V_scalar_inv + V_ferm_plus
V_eff_minus = V_scalar_inv + V_ferm_minus
chk("(7b) combined V_eff = scale-scalar + CW-fermion: d/dx != 0 at x=1/2 on both branches",
    simplify(diff(V_eff_plus, x).subs(x, Rational(1,2))) != 0
    and simplify(diff(V_eff_minus, x).subs(x, Rational(1,2))) != 0)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nPRUNED: the corner fermion-determinant det(M) does NOT select the balanced Koide r=1/2. Its\n"
    "stationary/special points at fixed Frobenius scale are r=1 (det=0, degenerate) and r=4, plus the\n"
    "boundaries -- the balanced max-sector-entropy point r=1/2 is NOT among them. With the measure routes\n"
    "(kappa=1) and the framework's own scalar-potential concession (V_eff min != physical point), the\n"
    "leading corner-sector dynamics do not rescue r=1/2. Residual (untested): taste-breaking scalar\n"
    "normalization; multi-factor Connes-Lott. CONDITIONAL on the open staggered-Dirac realization gate."
)

# ---- N5 execution certificate (print-only: adds no chk(), no verdict) ----
print("\nN5 EXECUTION CERTIFICATE")
print(
    "per_element: resolution reaches the three independent circulant entries and stops "
    "there - a, |b| and the phase delta are carried as sympy symbols and every statement "
    "above is a symbolic identity in them, but no 3x3 array is ever instantiated and no "
    "individual (i,j) position is evaluated on its own, because the determinant a^3 - 3 a "
    "|b|^2 + 2 |b|^3 cos(3 delta) is entered as a closed form rather than expanded from "
    "entries"
)
print(
    "per_site: checked and not executed - the three hw=1 objects this runner works over are "
    "Brillouin-zone corners, that is momentum labels, and no position-space site, spacing "
    "or hopping ever appears; the corner Grassmann integral is taken as already performed, "
    "so the site sum that would have produced it is upstream of the first line of code"
)
print(
    "per_mode: checked and not executed - only the product of the three corner masses is "
    "ever formed, since det(M) is the sole spectral object used; the individual corner "
    "eigenvalues are never written down, and the two-fold mass degeneracy asserted where "
    "the determinant vanishes is inferred from det = 0 alone rather than from any computed "
    "eigenvalue list"
)
print(
    "per_block: the C_3 singlet and the two-dimensional perpendicular doublet are tracked "
    "as separate energy reservoirs, with fractions x and 1 - x on the fixed Frobenius "
    "slice, and the binary entropy S = -x log x - (1 - x) log(1 - x) built on exactly that "
    "two-block split is shown to be stationary at x = 1/2 with the exact value log 2, which "
    "is what makes the balanced point a sector-symmetry statement rather than a dynamical "
    "one"
)
print(
    "lattice_wide: checked and not executed - the only global object in the file is the "
    "single fixed-scale slice 3 a^2 + 6 |b|^2 = 1, and on that slice a scale-only scalar "
    "potential is shown to have identically vanishing x-derivative; no volume, no particle "
    "number and no extent of any kind is defined, so the whole-system content is one "
    "constrained three-corner sector and no limit is taken in any direction"
)
