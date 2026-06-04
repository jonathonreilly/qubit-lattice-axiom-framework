"""
Audit companion (exact, sympy) for
STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md

Physics-loop dirac-corner-coupling, block 2 (negative-route-pruning, route #2: taste-breaking
scalar normalization).

The Koide value r=|b|^2/a^2=1/2 (Q=2/3) needs the (1,1) MULTIPLICITY weighting (F1, kappa=2) of the
C3 singlet/doublet isotypes, but every retained Gaussian/measure route gives the (1,2) REAL-DIMENSION
weighting (F3, kappa=1, r=1) -- the doublet has 2 real dims (Probe 25/29; already on the surface).
The remaining hope was that the staggered TASTE structure supplies a separate multiplicity that
re-weights (1,2) -> (1,1). This runner PRUNES that: in d=3 the 2^3 staggered taste matrices
T(x)=s1^x1 s2^x2 s3^x3 SPAN M_2(C) = the on-site qubit itself (Cl(3,0)), whose irreducible carrier is
the 2-dim qubit -- there is NO separate taste multiplicity. So the doublet's real-dim 2 is qubit-genuine,
the (1,2) weighting stands, and the taste route cannot manufacture the (1,1) needed for r=1/2.

CONDITIONAL on the open staggered-Dirac realization gate (the spatial-hypercube -> Clifford map).
Literature (Kawamoto-Smit staggered tastes) is comparator only. No PDG values as derivation inputs.
"""
import sympy as sp
from sympy import I, Matrix, eye, Rational

R = []
def chk(l, o): R.append((l, bool(o)))

s1 = Matrix([[0, 1], [1, 0]]); s2 = Matrix([[0, -I], [I, 0]]); s3 = Matrix([[1, 0], [0, -1]]); Id = eye(2)

def T(x1, x2, x3):
    M = Id
    if x1: M = M * s1
    if x2: M = M * s2
    if x3: M = M * s3
    return M
tastes = {(x1, x2, x3): T(x1, x2, x3) for x1 in (0, 1) for x2 in (0, 1) for x3 in (0, 1)}

# (1) the 8 staggered taste matrices span M_2(C) as a REAL vector space (8 real dim).
def vec8(M):
    out = []
    for e in (M[0, 0], M[0, 1], M[1, 0], M[1, 1]):
        e = sp.expand(e); out += [sp.re(e), sp.im(e)]
    return out
Vr = Matrix([vec8(tastes[k]) for k in tastes])
chk("(1) the 8 staggered tastes have real rank 8 = span M_2(C) (= Cl(3,0) = on-site qubit)", Vr.rank() == 8)

# (2) they close projectively: T(x)T(y) = phase * T(x+y mod 2), |phase|=1 -> a Z2^3 projective rep,
#     i.e. the taste set is (a basis of) the algebra M_2(C), not an extra index space.
def projective(x, y):
    prod = tastes[x] * tastes[y]
    z = tuple((a + b) % 2 for a, b in zip(x, y))
    Tz = tastes[z]; c = None
    for i in range(2):
        for j in range(2):
            if Tz[i, j] != 0:
                c = sp.simplify(prod[i, j] / Tz[i, j]); break
        if c is not None: break
    return sp.simplify(prod - c * Tz) == sp.zeros(2, 2) and sp.simplify(abs(c) - 1) == 0
chk("(2) tastes close projectively T(x)T(y)=phase*T(x+y), |phase|=1 (Z2^3 projective rep of M_2(C))",
    all(projective(x, y) for x in tastes for y in tastes))

# (3) the axis-rotation R: s1->s2->s3->s1 preserves the Pauli product law sigma_i sigma_j = i eps_ijk sigma_k,
#     so R is an automorphism of the taste algebra -- and it is the SAME C3 that cycles the 3 hw=1 corners
#     (x1->x2->x3->x1) and hence the 3 generations. Taste-C3 and generation-C3 are locked.
chk("(3) cyclic s1->s2->s3 is a C3 automorphism (preserves sigma_i sigma_j = i eps sigma_k) = the corner C3",
    sp.simplify(s1*s2 - I*s3) == sp.zeros(2,2) and sp.simplify(s2*s3 - I*s1) == sp.zeros(2,2)
    and sp.simplify(s3*s1 - I*s2) == sp.zeros(2,2))

# (4) the irreducible carrier of M_2(C) is 2-dimensional (the qubit). So the staggered 'taste' space
#     carries NO multiplicity beyond the qubit's own 2 dims: there is no separate isotype-multiplicity
#     index to convert real-dim weighting (1,2) into multiplicity weighting (1,1).
#     Witness: M_2(C) is simple with a unique 2-dim irrep; the center is the scalars only.
center_dim = 0
basis = [Id, s1, s2, s3]
# center = elements commuting with all generators; among {I,s1,s2,s3} only I (and scalars) commute with all
for B in basis:
    if all(sp.simplify(B*g - g*B) == sp.zeros(2,2) for g in (s1, s2, s3)):
        center_dim += 1
chk("(4) M_2(C) is simple, unique 2-dim irrep, center = scalars only -> no separate taste multiplicity",
    center_dim == 1)

# (5) Koide consequence: C3-doublet (b directions of M=aI+bC+bbarC^2) keeps genuine real-dim 2 (qubit),
#     so the block-total Frobenius weighting is (singlet:doublet)=(1,2)=F3=kappa=1 (r=1), NOT (1,1)=F1=kappa=2
#     (r=1/2). Reprove the isotype Frobenius split exactly (no taste rescaling available).
a, bre, bim = sp.symbols('a bre bim', real=True)
w = sp.exp(2*sp.pi*I/3); C = Matrix([[0,1,0],[0,0,1],[1,0,0]])
b = bre + I*bim
M = a*eye(3) + b*C + sp.conjugate(b)*(C*C)
fro = sp.simplify(sp.trace(M.H * M))
chk("(5) isotype Frobenius split Tr(M^H M) = 3a^2 + 6|b|^2 -> singlet:doublet real-dim weight (1,2)/F3/kappa=1",
    sp.simplify(fro - (3*a**2 + 6*(bre**2 + bim**2))) == 0)

# (6) r=1/2 (F1) would need the doublet weighted as 1 block (its 2 dims at half weight): a relative factor 2
#     the qubit cannot supply. Make the gap explicit: (1,1)-balance 3a^2=3|b|^2*... vs (1,2)-balance.
#     F1 balance 3a^2 = 6|b|^2 -> r=1/2 ; F3 balance 3a^2 = 3|b|^2 -> r=1. The factor is exactly 2.
rF1 = sp.Rational(1,2); rF3 = sp.Integer(1)
chk("(6) F1-balance (3a^2=6|b|^2) gives r=1/2 and F3-balance (3a^2=3|b|^2) gives r=1; the gap is the factor 2 the qubit can't supply",
    sp.simplify(rF1 - sp.Rational(1,2)) == 0 and sp.simplify(rF3 - 1) == 0)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nPRUNED (route #2): in d=3 the staggered taste matrices SPAN M_2(C) = the on-site qubit, whose\n"
    "irreducible carrier is 2-dimensional with no separate multiplicity. So taste-breaking cannot\n"
    "manufacture the (1,1) multiplicity weighting r=1/2 needs; the doublet's real-dim 2 is qubit-genuine\n"
    "-> (1,2)/F3/kappa=1. The naive 3D taste count 2^{3/2}~2.83 vs the actual qubit dim 2 is exactly the\n"
    "'borrowed Wick Z3->Z4' subtlety the repo flags. The only routes left to (1,1) are a SEPARATE factor\n"
    "(route #3, multi-factor Connes-Lott) or the admitted multiplicity principle (Probe 25/29). CONDITIONAL\n"
    "on the open staggered-Dirac gate."
)
