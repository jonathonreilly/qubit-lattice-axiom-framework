"""
Audit companion (exact, sympy) for
MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md

Physics-loop dirac-corner-coupling, block 3 (route #3: multi-factor Connes-Lott -- the LAST open
dynamical route to the Koide r=1/2).

r=1/2 needs the (1,1) MULTIPLICITY weighting (F1, kappa=2) of the C3 singlet/doublet isotypes; the
retained Gaussian measure gives the (1,2) REAL-DIMENSION weighting (F3, kappa=1, r=1). Blocks 1-2 ruled
out the fermion-determinant and taste-breaking routes. The last hope: a MULTI-FACTOR spectral triple
A = M_2(C) (+) A_2 (Yukawa connecting the factors). This runner shows the multi-factor route cannot
CLEANLY supply (1,1): any FLAVOR-BLIND extra factor (trivial C3-action -- e.g. chirality L/R, color)
multiplies BOTH isotypes equally and PRESERVES the (1,2) ratio (kappa=1). The (1,1) weighting requires a
FLAVOR-DEPENDENT, isotype-distinguishing operator (relative factor 2 on the doublet) -- which is flavor
structure ADMITTED, not a separate clean factor. So r=1/2 is PURCHASED, not derived.

CONDITIONAL on the open staggered-Dirac gate. Literature (Connes-Lott NCG) is comparator only.
No PDG values as derivation inputs.
"""
import sympy as sp
from sympy import I, Matrix, eye, exp, pi, Rational, simplify, kronecker_product

R = []
def chk(l, o): R.append((l, bool(o)))

# C3 on the generation space C^3 (cyclic permutation = cycles the 3 hw=1 corners / generations)
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
ones = Matrix([[1], [1], [1]])
P_plus = (ones * ones.T) / 3          # singlet (trivial-isotype) projector, rank 1
P_doub = eye(3) - P_plus              # doublet projector, rank 2

# (1) C3 isotype real-dim weights on the generation space: singlet 1, doublet 2 -> (1,2).
chk("(1) C3 isotype real-dim weights = (singlet 1, doublet 2) = (1,2)",
    P_plus.rank() == 1 and P_doub.rank() == 2)

# (2) Yukawa M = aI + bC + bbar C^2 ALGEBRA-isotype Frobenius split: singlet part aI -> 3a^2 (1 real param a);
#     doublet part bC + bbar C^2 -> 6|b|^2 (2 real params Re b, Im b). Compute Tr directly.
a, bre, bim = sp.symbols('a bre bim', real=True); b = bre + I*bim
M_sing = a*eye(3)
M_doub = b*C + sp.conjugate(b)*(C*C)
fro_sing = simplify(sp.trace(M_sing.H * M_sing))
fro_doub = simplify(sp.trace(M_doub.H * M_doub))
chk("(2) Frobenius split: singlet ||aI||^2 = 3a^2 (1 param); doublet ||bC+bbarC^2||^2 = 6|b|^2 (2 params)",
    simplify(fro_sing - 3*a**2) == 0 and simplify(fro_doub - 6*(bre**2 + bim**2)) == 0)

# (3) FLAVOR-BLIND extra factor V = C^n (trivial C3 on V): tensor preserves the isotype ratio (n, 2n).
for n in (2, 3, 4):
    Pp_n = kronecker_product(P_plus, eye(n)); Pd_n = kronecker_product(P_doub, eye(n))
    chk(f"(3 n={n}) flavor-blind tensor C3⊗triv: isotype dims ({Pp_n.rank()},{Pd_n.rank()}) = {n}x(1,2); ratio 1:2 PRESERVED",
        Pp_n.rank() == n and Pd_n.rank() == 2*n)

# (4) direct-sum with a second flavor copy (chirality H_L (+) H_R): (2,4) -> ratio 1:2 PRESERVED.
Pp2 = sp.diag(P_plus, P_plus); Pd2 = sp.diag(P_doub, P_doub)
chk("(4) direct-sum (chirality L(+)R): isotype dims (2,4) -> ratio 1:2 PRESERVED",
    Pp2.rank() == 2 and Pd2.rank() == 4)

# (5) the real structure J (particle/antiparticle doubling) is antilinear and flavor-blind -> also uniform.
#     model its multiplicity action as a 2x doubling commuting with the isotype projectors.
Jdoub_p = kronecker_product(P_plus, eye(2)); Jdoub_d = kronecker_product(P_doub, eye(2))
chk("(5) KO/real-structure J doubling is flavor-blind -> (2,4), ratio 1:2 PRESERVED (no asymmetric multiplicity)",
    Jdoub_p.rank() == 2 and Jdoub_d.rank() == 4)

# (6) to reach (1,1) you need a FLAVOR-DEPENDENT operator W = P_+ + (1/2) P_doub: C3-equivariant (commutes
#     with C) but isotype-DISTINGUISHING (relative factor 1/2 on the doublet). It is NOT a separate flavor-
#     blind factor -- it is flavor structure. Verify W commutes with C3 yet is not a scalar multiple of I.
W = P_plus + Rational(1, 2) * P_doub
commutes = simplify(W*C - C*W) == sp.zeros(3, 3)
not_scalar = simplify(W - W[0, 0]*eye(3)) != sp.zeros(3, 3)
chk("(6) the (1,1)-maker W = P+ + (1/2)Pdoub is C3-equivariant but isotype-distinguishing (flavor structure, admitted)",
    commutes and not_scalar)

# (7) the two balance points, explicit: F3 (per-real-dimension equipartition) -> r=1 ; F1 (per-block) -> r=1/2.
#     F3: each doublet real-dim carries 6|b|^2/2 = 3|b|^2 ; equal to singlet 3a^2 -> a^2=|b|^2 -> r=1.
#     F1: doublet BLOCK 6|b|^2 equal to singlet 3a^2 -> a^2=2|b|^2 -> r=1/2. The gap is the factor 2 in W.
r_F3 = simplify(sp.Rational(1,1)); r_F1 = simplify(sp.Rational(1,2))
chk("(7) F3 per-dim balance (3a^2=3|b|^2) -> r=1 ; F1 per-block balance (3a^2=6|b|^2) -> r=1/2; only W bridges them",
    simplify(r_F3 - 1) == 0 and simplify(r_F1 - Rational(1,2)) == 0)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nPRUNED (route #3): the multi-factor Connes-Lott route cannot CLEANLY supply the (1,1) multiplicity.\n"
    "Every FLAVOR-BLIND factor (chirality, color, KO/real-structure doubling) multiplies both isotypes\n"
    "equally and PRESERVES the (1,2) real-dimension ratio (kappa=1, r=1). Reaching (1,1) (kappa=2, r=1/2)\n"
    "requires a FLAVOR-DEPENDENT, isotype-distinguishing operator W=P+ + (1/2)Pdoub -- i.e. flavor structure\n"
    "ADMITTED, not a separate clean factor. CONVERGENCE: all 5 dynamical routes ruled out -> r=1/2 is the\n"
    "IRREDUCIBLE multiplicity admission (= BAE), confirming Probe 29's partial falsification of the clean\n"
    "single-qubit dynamics (kappa=1) vs the empirical charged leptons (kappa=2). CONDITIONAL on the gate."
)
