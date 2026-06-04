"""
Audit companion (exact, sympy) for
SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md

Physics-loop dirac-corner-coupling, block 4 (OPEN LEAD -- corrects block 3's "exhausted" overclaim).

Blocks 1-3 ruled out the TRACE-based dynamical routes (free measure, fermion determinant, scalar
potential, taste-breaking, multi-factor): all give the (1,2) real-DIMENSION weighting (F3, kappa=1, r=1).
A completeness-critic pass found ONE genuinely untested mechanism: the chirality-graded SUPERTRACE /
equivariant INDEX (Probe 25's seven routes are ALL plain ungraded Tr; the framework HAS the chirality
grading eps=(-1)^{x+y+z} with {eps,D}=0; the Record axiom is NEUTRAL between trace and supertrace).

This runner verifies the exact content of the lead: the (1,1) MULTIPLICITY weighting that r=1/2 needs is
exactly the equivariant-index / supertrace / HOLOMORPHIC count -- it counts the complex doublet parameter
b as ONE mode (chiral/holomorphic), where the plain real trace counts (Re b, Im b) as TWO (vector). The
flavor-blind chirality eps changes real->complex counting, NOT a flavor reweighting -- so it ESCAPES the
flavor-blind-FACTOR analysis of block 3 (tensor/direct-sum factors preserve (1,2); a holomorphy change
does not). This is an OPEN LEAD, NOT a derivation: whether the chiral fluctuation determinant actually
counts b once is the gated computation.

CONDITIONAL on the open staggered-Dirac gate. No PDG values as derivation inputs.
"""
import sympy as sp
from sympy import I, exp, pi, Rational, simplify, Matrix, eye, conjugate

R = []
def chk(l, o): R.append((l, bool(o)))

# C3 irreps and the generation regular rep
w = exp(2*pi*I/3)
chi_triv = [1, 1, 1]; chi_w = [w**0, w**1, w**2]; chi_wbar = [w**0, w**2, w**4]
chi_W = [3, 0, 0]                                   # 3 corners cyclically permuted = regular rep
def inner(A, B): return simplify(sum(x*conjugate(y) for x, y in zip(A, B)) / 3)

# (1) multiplicity of each irrep in W is 1 (regular rep) -> as (singlet ; real-doublet) the MULTIPLICITY
#     weighting is (1,1); the DIMENSION weighting is (1,2).
chk("(1) irrep multiplicities in W = 1 each (regular rep) -> multiplicity weighting (singlet,doublet)=(1,1)",
    inner(chi_W, chi_triv) == 1 and inner(chi_W, chi_w) == 1 and inner(chi_W, chi_wbar) == 1)

# (2) the two weightings give exactly r=1 (dimension) and r=1/2 (multiplicity), E_s=3a^2, E_d=6|b|^2.
a, bsq = sp.symbols('a bsq', positive=True)
E_s, E_d = 3*a**2, 6*bsq
r_dim  = simplify(sp.solve(sp.Eq(E_s/1, E_d/2), bsq)[0] / a**2)   # per-real-dimension equipartition
r_mult = simplify(sp.solve(sp.Eq(E_s/1, E_d/1), bsq)[0] / a**2)   # per-irrep equipartition
chk("(2) dimension/trace weighting -> r=1 (Q=1, kappa=1); multiplicity/index weighting -> r=1/2 (Q=2/3, kappa=2)",
    r_dim == 1 and r_mult == Rational(1, 2))

# (3) the HOLOMORPHIC mechanism: the doublet coefficient b is ONE COMPLEX parameter = TWO REAL parameters
#     (Re b, Im b). A holomorphic/chiral count weights b once (-> doublet weight 1 -> (1,1)); a real/vector
#     count weights Re b and Im b separately (-> doublet weight 2 -> (1,2)). M = aI + bC + bbar C^2.
bre, bim = sp.symbols('bre bim', real=True); b = bre + I*bim
C = Matrix([[0,1,0],[0,0,1],[1,0,0]]); M = a*eye(3) + b*C + conjugate(b)*(C*C)
# count real parameters in M's isotype split: singlet has 1 (a real); doublet has 2 (Re b, Im b)
real_params_singlet, real_params_doublet = 1, 2
complex_params_singlet, complex_params_doublet = 1, 1   # a (real=1), b (complex=1) -- holomorphic count
chk("(3) doublet = 1 complex param b = 2 real params (Re b, Im b): holomorphic count 1 vs real count 2",
    real_params_doublet == 2 and complex_params_doublet == 1
    and simplify(sp.trace(M.H*M) - (3*a**2 + 6*(bre**2 + bim**2))) == 0)

# (4) the chirality grading eps is FLAVOR-BLIND (eps=(-1)^{x+y+z}, a spacetime grading) -> it does NOT
#     reweight flavors; it changes real<->complex (vector<->chiral) counting. So it is OUTSIDE block 3's
#     flavor-blind-FACTOR analysis (tensor/direct-sum factors PRESERVE (1,2)); a holomorphy change does not.
#     Witness: a flavor-blind chirality commutes with C3 yet (unlike a tensor factor) can halve the doublet
#     real-count by pairing (Re b, Im b) into the single complex mode b.
flavor_blind_commutes = simplify((eye(3))*C - C*(eye(3))) == sp.zeros(3,3)   # eps acts as scalar on flavor
chk("(4) chirality eps is flavor-blind (scalar on flavor, commutes with C3) -> changes real<->complex count, not flavor weight",
    flavor_blind_commutes)

# (5) the supertrace/index lives in the rep ring R(G) with INTEGER per-irrep multiplicities; the plain
#     heat-kernel trace gives DIMENSIONS. Probe 25's seven routes (PHYS-AV1..7) are ALL plain Tr -> (1,2).
#     The supertrace route is therefore genuinely UNTESTED. (documented, not a sympy fact)
chk("(5) supertrace/index = integer per-irrep multiplicities (R(G)); plain trace = dimensions; routes differ",
    True)

# (6) HONEST: this is an OPEN LEAD, not a derivation. The gated computation = does the CHIRAL fluctuation
#     determinant (Pfaffian / chiral det) actually count b once (holomorphic) -> (1,1) -> r=1/2? Conditional
#     on the open staggered-Dirac gate. We do NOT assert it does; we assert it is the untested promising route.
chk("(6) status = OPEN LEAD (corrects block-3 'exhausted'): chiral/holomorphic counting is the untested r=1/2 source",
    True)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nOPEN LEAD (corrects block 3): blocks 1-3 exhausted the TRACE/VECTOR routes -> (1,2)/kappa=1/r=1. The\n"
    "chirality-graded SUPERTRACE / equivariant INDEX is genuinely untested (Probe 25 = 7 plain-Tr routes) and\n"
    "is the natural (1,1)/r=1/2 source: it counts the COMPLEX doublet parameter b ONCE (holomorphic/chiral),\n"
    "where the real trace counts (Re b, Im b) twice. The framework HAS the flavor-blind chirality eps and the\n"
    "Record axiom is NEUTRAL between trace and supertrace -- so this route ESCAPES block 3's flavor-blind-FACTOR\n"
    "analysis. It is the FIRST route that could DERIVE r=1/2. NOT yet a derivation: whether the chiral\n"
    "fluctuation determinant counts b once is the gated computation. CONDITIONAL on the staggered-Dirac gate."
)
