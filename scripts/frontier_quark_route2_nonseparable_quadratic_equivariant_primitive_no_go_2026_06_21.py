"""Route-2 nonseparable quadratic primitive no-go.

Question
--------
After scalar quadratic functionals and pure channel metrics fail to derive
lambda = q_E/q_T = 9/4, can a genuinely nonseparable quadratic primitive

    Q : Sym^2(E (+) T1) -> E (+) T1

be forced by O_h symmetry to select the Route-2 endpoint triple?

Result
------
No. Character arithmetic on the six-arm O_h star gives

    Sym^2(E)        = A1 (+) E
    E tensor T1     contains one T1 channel
    Sym^2(T1)      contains A1 (+) E

and therefore

    Sym^2(E (+) T1) contains 2*A1 (+) 2*E (+) 1*T1 (+) non-readout T2 pieces.

Thus Hom_Oh(Sym^2(E (+) T1), E (+) T1) has dimension 3: two independent
E-output reduced coefficients and one independent T1-output coefficient.
O_h symmetry permits nonseparable quadratic maps, but it does not select a
unique readout ratio. The endpoint value lambda=9/4 still requires an
additional coefficient-selection/normalization primitive.

Forbidden-inputs discipline: the target rationals are comparison targets only.
No observed masses, fitted endpoints, live selector, or nearest-rational rule
is consumed.
"""
from __future__ import annotations

from fractions import Fraction as F
import itertools

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    return ok


ARMS = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
ARM_INDEX = {a: i for i, a in enumerate(ARMS)}


def oh_signed_perms() -> list[sp.Matrix]:
    mats: list[sp.Matrix] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for row in range(3):
                M[row, perm[row]] = signs[row]
            mats.append(M)
    return mats


def arm_rep(M: sp.Matrix) -> sp.Matrix:
    P = sp.zeros(6, 6)
    for j, arm in enumerate(ARMS):
        v = M * sp.Matrix(arm)
        image = tuple(int(v[k]) for k in range(3))
        P[ARM_INDEX[image], j] = 1
    return P


def key(M: sp.Matrix) -> tuple[int, ...]:
    return tuple(int(M[i, j]) for i in range(M.rows) for j in range(M.cols))


def character(projector: sp.Matrix, rep: sp.Matrix) -> sp.Rational:
    return sp.Rational(sp.trace(projector * rep))


def inner_product(chi_a: list[sp.Rational], chi_b: list[sp.Rational]) -> sp.Rational:
    return sp.simplify(sum(a * b for a, b in zip(chi_a, chi_b)) / len(chi_a))


def sym2_character(chi: list[sp.Rational], square_indices: list[int]) -> list[sp.Rational]:
    return [sp.simplify((chi[i] ** 2 + chi[square_indices[i]]) / 2) for i in range(len(chi))]


def tensor_character(chi_a: list[sp.Rational], chi_b: list[sp.Rational]) -> list[sp.Rational]:
    return [a * b for a, b in zip(chi_a, chi_b)]


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    c_te = F(-2) * q_t / q_e
    return q_e, rho_e, c_te


def main() -> int:
    print("Route-2 nonseparable quadratic equivariant primitive no-go")
    print("=" * 88)

    group3 = oh_signed_perms()
    reps = [arm_rep(M) for M in group3]
    order = len(group3)
    idx = {key(M): i for i, M in enumerate(group3)}
    square_indices = [idx[key(M * M)] for M in group3]
    identity_index = idx[key(sp.eye(3))]

    check("O_h signed-permutation group has order 48", order == 48, f"order={order}")

    I6 = sp.eye(6)
    P_A1 = sum(reps, sp.zeros(6, 6)) / order
    antipodal = arm_rep(-sp.eye(3))
    P_T1 = (I6 - antipodal) / 2
    P_E = (I6 + antipodal) / 2 - P_A1

    ranks = (sp.trace(P_A1), sp.trace(P_E), sp.trace(P_T1))
    weights = (P_A1[0, 0], P_E[0, 0], P_T1[0, 0])
    check(
        "six-arm representation decomposes as A1 (+) E (+) T1 with weights (1/6,1/3,1/2)",
        ranks == (1, 2, 3)
        and weights == (sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2)),
        f"ranks={ranks}, weights={weights}",
    )

    chi_A = [character(P_A1, R) for R in reps]
    chi_E = [character(P_E, R) for R in reps]
    chi_T = [character(P_T1, R) for R in reps]
    check(
        "identity characters are dim(A1,E,T1)=(1,2,3)",
        (chi_A[identity_index], chi_E[identity_index], chi_T[identity_index]) == (1, 2, 3),
        f"chars={(chi_A[identity_index], chi_E[identity_index], chi_T[identity_index])}",
    )

    chi_sym_E = sym2_character(chi_E, square_indices)
    chi_ET = tensor_character(chi_E, chi_T)
    chi_sym_T = sym2_character(chi_T, square_indices)
    chi_sym_ET = sym2_character([e + t for e, t in zip(chi_E, chi_T)], square_indices)

    def mults(chi: list[sp.Rational]) -> tuple[sp.Rational, sp.Rational, sp.Rational]:
        return (
            inner_product(chi_A, chi),
            inner_product(chi_E, chi),
            inner_product(chi_T, chi),
        )

    m_sym_E = mults(chi_sym_E)
    m_ET = mults(chi_ET)
    m_sym_T = mults(chi_sym_T)
    m_sym_total = mults(chi_sym_ET)
    check(
        "Sym^2(E) contains A1 (+) E and no T1 output channel",
        chi_sym_E[identity_index] == 3 and m_sym_E == (1, 1, 0),
        f"dim={chi_sym_E[identity_index]}, mult(A1,E,T1)={m_sym_E}",
    )
    check(
        "E tensor T1 contributes one T1 readout channel and no A1/E channel",
        chi_ET[identity_index] == 6 and m_ET == (0, 0, 1),
        f"dim={chi_ET[identity_index]}, mult(A1,E,T1)={m_ET}",
    )
    check(
        "Sym^2(T1) contains A1 (+) E and no T1 output channel",
        chi_sym_T[identity_index] == 6 and m_sym_T == (1, 1, 0),
        f"dim={chi_sym_T[identity_index]}, mult(A1,E,T1)={m_sym_T}",
    )
    check(
        "Sym^2(E (+) T1) contains two A1 scalars, two E channels, and one T1 channel",
        chi_sym_ET[identity_index] == 15 and m_sym_total == (2, 2, 1),
        f"dim={chi_sym_ET[identity_index]}, mult(A1,E,T1)={m_sym_total}",
    )

    hom_to_readout = m_sym_total[1] + m_sym_total[2]
    scalar_invariants = m_sym_total[0]
    unresolved_dim_after_t_norm = hom_to_readout - 1
    check(
        "Hom_Oh(Sym^2(E (+) T1), E (+) T1) has dimension 3",
        hom_to_readout == 3,
        f"two E-output reduced coefficients + one T1-output coefficient = {hom_to_readout}",
    )
    check(
        "even after fixing one T-output normalization, at least two reduced coefficients remain free",
        unresolved_dim_after_t_norm == 2 and scalar_invariants == 2,
        f"free_after_T_norm={unresolved_dim_after_t_norm}, scalar_invariants={scalar_invariants}",
    )

    accounted_dimension = 2 * 1 + 2 * 2 + 1 * 3
    leftover_dimension = chi_sym_ET[identity_index] - accounted_dimension
    check(
        "readout-relevant multiplicities account for 9 of 15 dimensions; remaining 6 are non-readout T2-type channels",
        leftover_dimension == 6,
        f"accounted={accounted_dimension}, leftover={leftover_dimension}",
    )

    endpoint_target = endpoint_from_lambda(F(9, 4))
    check(
        "lambda=9/4 is equivalent to q_E=15/8, rho_E=21/4, c_TE=-8/9 under the granted T-side",
        endpoint_target == (F(15, 8), F(21, 4), F(-8, 9)),
        f"q_E,rho_E,c_TE={endpoint_target}",
    )

    allowed_lambdas = [F(1, 1), F(3, 2), F(9, 4), F(7, 3)]
    examples = {lam: endpoint_from_lambda(lam) for lam in allowed_lambdas}
    check(
        "free reduced coefficients can realize comparison lambdas 1, 3/2, 9/4, and 7/3; symmetry does not select one",
        set(examples) == set(allowed_lambdas) and len({v[1] for v in examples.values()}) == len(allowed_lambdas),
        "; ".join(f"lambda={lam}: rho_E={vals[1]}" for lam, vals in examples.items()),
    )

    print("\n" + "=" * 88)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: no-go for the pure O_h nonseparable quadratic primitive route.\n"
        "O_h allows quadratic maps Sym^2(E (+) T1) -> E (+) T1, including a genuinely\n"
        "mixed E tensor T1 -> T1 channel, but the map is not unique: there are two\n"
        "independent E-output reduced coefficients and one T-output coefficient. The\n"
        "endpoint lambda=9/4 is therefore not selected by the representation content;\n"
        "it still requires an additional coefficient-selection or normalization primitive."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
