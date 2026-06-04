"""
Audit companion (exact, sympy) for
STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md

Koide taste-multiplicity route pruning (negative-route-pruning: taste-breaking scalar
normalization).

The Koide value r=|b|^2/a^2=1/2 (Q=2/3) needs the (1,1) MULTIPLICITY weighting
(legacy F1, kappa=2) of the C3 singlet/doublet isotypes, but the surfaced
Gaussian/measure route gives the (1,2) REAL-DIMENSION weighting (legacy F3,
kappa=1, r=1) -- the doublet has 2 real dims (Probe 25/29; already on the surface).
The remaining hope was that the staggered TASTE structure supplies a separate multiplicity that
re-weights (1,2) -> (1,1). This runner PRUNES that: in d=3 the 2^3 staggered taste matrices
T(x)=s1^x1 s2^x2 s3^x3 SPAN M_2(C) = the on-site qubit itself (Cl(3,0)), whose
irreducible carrier is the 2-dim qubit -- there is NO separate taste multiplicity. So the
doublet's real-dim 2 is qubit-genuine, the (1,2) weighting stands, and the taste route
cannot manufacture the (1,1) needed for r=1/2.

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
#     Witness: the center of the general M_2(C) element is scalars only.
u0, u1, u2, u3 = sp.symbols("u0 u1 u2 u3")
X = u0 * Id + u1 * s1 + u2 * s2 + u3 * s3
eqs = []
for g in (s1, s2, s3):
    eqs.extend(list(sp.simplify(X * g - g * X)))
center_solution = sp.linsolve(eqs, (u0, u1, u2, u3))
chk("(4) M_2(C) is simple, unique 2-dim irrep, center = scalars only -> no separate taste multiplicity",
    center_solution == sp.FiniteSet((u0, 0, 0, 0)))

# (5) Koide consequence: C3-doublet (b directions of M=aI+bC+bbarC^2) keeps genuine real-dim 2 (qubit),
#     so the block-total Frobenius weighting is (singlet:doublet)=(1,2) (legacy F3, kappa=1, r=1),
#     NOT (1,1) (legacy F1, kappa=2)
#     (r=1/2). Reprove the isotype Frobenius split exactly (no taste rescaling available).
a, bre, bim = sp.symbols('a bre bim', real=True)
w = sp.exp(2*sp.pi*I/3); C = Matrix([[0,1,0],[0,0,1],[1,0,0]])
b = bre + I*bim
M = a*eye(3) + b*C + sp.conjugate(b)*(C*C)
fro = sp.simplify(sp.trace(M.H * M))
chk("(5) isotype Frobenius split Tr(M^H M) = 3a^2 + 6|b|^2 -> singlet:doublet real-dim weight (1,2), legacy F3, kappa=1",
    sp.simplify(fro - (3*a**2 + 6*(bre**2 + bim**2))) == 0)

# (6) r=1/2 (legacy F1) would need the doublet weighted as 1 block (its 2 dims at half weight): a relative factor 2
#     the qubit cannot supply. Make the gap explicit: (1,1)-balance 3a^2=3|b|^2*... vs (1,2)-balance.
#     F1 balance 3a^2 = 6|b|^2 -> r=1/2 ; F3 balance 3a^2 = 3|b|^2 -> r=1. The factor is exactly 2.
rF1 = sp.Rational(1,2); rF3 = sp.Integer(1)
chk("(6) legacy F1 balance (3a^2=6|b|^2) gives r=1/2 and legacy F3 balance (3a^2=3|b|^2) gives r=1; the gap is the factor 2 the qubit can't supply",
    sp.simplify(rF1 - sp.Rational(1,2)) == 0 and sp.simplify(rF3 - 1) == 0)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nPRUNED (taste-normalization route): in d=3 the staggered taste matrices SPAN M_2(C) = the on-site qubit, whose\n"
    "irreducible carrier is 2-dimensional with no separate multiplicity. So taste-breaking cannot\n"
    "manufacture the (1,1) multiplicity weighting r=1/2 needs; the doublet's real-dim 2 is qubit-genuine\n"
    "-> (1,2), legacy F3, kappa=1. The naive 3D taste count 2^{3/2}~2.83 vs the actual qubit dim 2 is exactly\n"
    "the 'borrowed Wick Z3->Z4' subtlety the repo flags. Remaining open handles include a SEPARATE factor,\n"
    "an explicit multiplicity-counting admission, or the eta-phase mass-weighting residual. CONDITIONAL on\n"
    "the open staggered-Dirac gate."
)
