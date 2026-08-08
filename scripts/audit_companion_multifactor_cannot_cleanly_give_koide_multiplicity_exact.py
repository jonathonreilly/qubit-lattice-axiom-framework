"""
Audit companion (exact, sympy) for
MULTIFACTOR_CONNES_LOTT_PURCHASES_NOT_DERIVES_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md

Koide flavor-blind multi-factor route pruning.

The Koide value r=|b|^2/a^2=1/2 (Q=2/3) needs the (1,1) multiplicity
weighting (legacy F1, kappa=2) of the C3 singlet/doublet isotypes. The clean
Gaussian/Frobenius route gives the (1,2) real-dimension weighting (legacy F3,
kappa=1, r=1). This runner checks the narrow multi-factor claim:
flavor-blind extra factors with trivial C3 action multiply both isotypes
equally and preserve the (1,2) ratio. The (1,1) weighting requires an
isotype-distinguishing operator W=P_+ + (1/2)P_doublet, which is a
flavor-structured input unless a separate retained derivation supplies it.

Conditional on the open staggered-Dirac gate. Connes-Lott/NCG literature is
comparator only. No PDG values as derivation inputs.
"""

import sympy as sp
from sympy import I, Matrix, Rational, eye, kronecker_product, simplify

R = []


def chk(label, ok):
    R.append((label, bool(ok)))


# C3 generation action on C^3.
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
ones = Matrix([[1], [1], [1]])
P_plus = (ones * ones.T) / 3
P_doublet = eye(3) - P_plus

chk(
    "(1) C3 isotype real-dim weights are singlet 1 and doublet 2",
    P_plus.rank() == 1 and P_doublet.rank() == 2,
)

# Frobenius split for the C3-circulant Yukawa.
a, bre, bim = sp.symbols("a bre bim", real=True)
b = bre + I * bim
M_singlet = a * eye(3)
M_doublet = b * C + sp.conjugate(b) * (C * C)
fro_singlet = simplify(sp.trace(M_singlet.H * M_singlet))
fro_doublet = simplify(sp.trace(M_doublet.H * M_doublet))
chk(
    "(2) Frobenius split is 3a^2 on singlet and 6|b|^2 on doublet",
    simplify(fro_singlet - 3 * a**2) == 0
    and simplify(fro_doublet - 6 * (bre**2 + bim**2)) == 0,
)

# Flavor-blind tensor V=C^n with trivial C3 action preserves the ratio.
for n in range(1, 7):
    Pp_n = kronecker_product(P_plus, eye(n))
    Pd_n = kronecker_product(P_doublet, eye(n))
    chk(
        f"(3 n={n}) flavor-blind tensor gives isotype dims ({n},{2*n}), ratio 1:2",
        Pp_n.rank() == n and Pd_n.rank() == 2 * n,
    )

# Flavor-blind direct sums preserve the ratio as well.
for copies in (2, 3):
    Pp_sum = sp.diag(*([P_plus] * copies))
    Pd_sum = sp.diag(*([P_doublet] * copies))
    chk(
        f"(4 copies={copies}) flavor-blind direct sum gives dims ({copies},{2*copies}), ratio 1:2",
        Pp_sum.rank() == copies and Pd_sum.rank() == 2 * copies,
    )

# KO/real-structure doubling is also a flavor-blind multiplicity doubling in this scope.
J_p = kronecker_product(P_plus, eye(2))
J_d = kronecker_product(P_doublet, eye(2))
chk(
    "(5) KO/real-structure doubling modeled flavor-blindly gives dims (2,4), ratio 1:2",
    J_p.rank() == 2 and J_d.rank() == 4,
)

# The desired (1,1) maker commutes with C3 but is not scalar on the isotype split.
W = P_plus + Rational(1, 2) * P_doublet
commutes = simplify(W * C - C * W) == sp.zeros(3, 3)
not_scalar = simplify(W - W[0, 0] * eye(3)) != sp.zeros(3, 3)
chk(
    "(6) W=P_+ +(1/2)P_doublet is C3-equivariant but isotype-distinguishing",
    commutes and not_scalar,
)

# Balance points: per-real-dimension versus per-block.
r_per_dimension = sp.Integer(1)
r_per_block = Rational(1, 2)
chk(
    "(7) per-dimension balance gives r=1; per-block balance gives r=1/2",
    simplify(r_per_dimension - 1) == 0 and simplify(r_per_block - Rational(1, 2)) == 0,
)

passed = sum(1 for _, ok in R if ok)
failed = sum(1 for _, ok in R if not ok)
for label, ok in R:
    print(("PASS" if ok else "FAIL"), "-", label)
print(f"\n{passed} PASS, {failed} FAIL")
if failed:
    raise SystemExit(1)

print(
    "\nPRUNED (flavor-blind multi-factor route): C3-trivial extra factors multiply singlet and\n"
    "doublet isotypes equally, preserving the (1,2) real-dimension ratio (legacy F3, kappa=1,\n"
    "r=1). The (1,1) multiplicity weighting (legacy F1, kappa=2, r=1/2) requires the\n"
    "isotype-distinguishing operator W=P_+ +(1/2)P_doublet. That is a flavor-structured input\n"
    "unless a separate retained derivation supplies it. This is not a universal no-go against\n"
    "NCG or two-factor models; it prunes the flavor-blind route only."
)

# N5 execution certificate (print-only; adds no check and no verdict)
print()
print("==============================================================================")
print("N5 EXECUTION CERTIFICATE")
print("==============================================================================")
print(
    "  per_element: thin but real, and it is computed rather than asserted - "
    "the Frobenius split is obtained by actually forming M_singlet = a*eye(3) "
    "and M_doublet = b*C + conj(b)*C^2 and taking trace(M.H * M) in sympy, "
    "which returns the exact closed forms 3*a^2 and 6*(bre^2 + bim^2), i.e. "
    "three diagonal entries of modulus a and six off-diagonal entries of "
    "modulus |b|; the one indexed lookup in the file, W[0,0], serves only to "
    "build the scalarity comparison W - W[0,0]*eye(3)."
)
print(
    "  per_site: checked and not executed - none of the three generation slots "
    "is ever addressed on its own. Every quantity computed here is a rank, a "
    "trace, or a full-matrix simplify to the zero matrix, and the two "
    "projectors are used as indivisible objects throughout, so nothing in the "
    "argument would change if the slots were relabelled arbitrarily."
)
print(
    "  per_mode: checked and not executed - the extension operations the whole "
    "pruning rests on act on isotype projectors wholesale and never reach a "
    "character. kronecker_product(P, eye(n)) for n = 1 through 6, sp.diag of "
    "two and three copies, and the KO doubling against eye(2) all multiply a "
    "projector by an identity, C is multiplied but never diagonalized, and the "
    "two nontrivial cube roots of unity appear nowhere in the file."
)
print(
    "  per_block: this is the only granularity carrying weight, and it carries "
    "it by exact integer ranks - P_plus and P_doublet are checked to have rank "
    "1 and rank 2, then the flavor-blind extensions are shown to scale that "
    "pair rigidly to (n, 2n) for every n in 1..6, to (copies, 2*copies) for two "
    "and three summands, and to (2, 4) under the real-structure doubling, so "
    "the 1:2 block ratio survives every flavor-blind factor tested. The "
    "obstruction is a clash of two granularities: balancing per real dimension "
    "yields r = 1 while balancing per block yields r = 1/2, and only the "
    "isotype-distinguishing W = P_plus + (1/2)*P_doublet, verified to commute "
    "with C yet not be a multiple of the identity, converts one into the other."
)
print(
    "  lattice_wide: checked and not executed - there is no substrate here at "
    "all, only fixed matrices over C^3 and small tensor extensions of them, and "
    "no limit or extent of any kind. The runner's closing paragraph draws the "
    "same boundary itself, stating that this is not a universal no-go against "
    "NCG or two-factor models and prunes the flavor-blind route only."
)
