"""Route-2 channel-metric no-go: an O_h-invariant metric on E (+) T1 has
a Schur-free E:T1 ratio, so it does not derive the endpoint factor
lambda = q_E/q_T = 9/4.

Context
-------
The exact Route-2 readout reduction compresses the endpoint target to

    (beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).

After granting the two T-side entries, the remaining datum is
rho_E = beta_E/alpha_E = 21/4, equivalently

    q_T = 5/6, q_E = 15/8, lambda := q_E/q_T = 9/4.

Prior no-go packets showed that O_h equivariance and quadratic invariant
functionals do not force this lambda. This runner attacks the strongest
nearby "channel metric" steelman: perhaps a positive O_h-invariant channel
metric on E (+) T1 canonically fixes the E:T1 normalization ratio.

Result
------
No. On the six-arm O_h star, the symmetric invariant metrics restricted to
E (+) T1 form the two-parameter cone

    G(c_E,c_T) = c_E P_E + c_T P_T1,     c_E,c_T > 0.

The ratio c_E/c_T is a Schur free parameter. Ambient Euclidean normalization
gives lambda=1. A one-reciprocal projector/dimension normalization gives
lambda=3/2. The endpoint lambda=9/4 appears only when the inverse-square
normalization c_X proportional to w_X^-2 is inserted. Therefore the channel
metric route is a no-go unless a new primitive derives that inverse-square
law.

Forbidden-inputs discipline: no observed masses, fitted endpoint value,
nearest-rational selector, or live endpoint fit is consumed. The target
rationals are used only as comparison targets already named by the exact
readout map.
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
    """The 48 signed permutation matrices, i.e. O_h acting on R^3."""
    mats: list[sp.Matrix] = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for row in range(3):
                M[row, perm[row]] = signs[row]
            mats.append(M)
    return mats


def arm_rep(M: sp.Matrix) -> sp.Matrix:
    """Permutation representation induced by M on the six oriented arms."""
    P = sp.zeros(6, 6)
    for j, arm in enumerate(ARMS):
        v = M * sp.Matrix(arm)
        image = tuple(int(v[k]) for k in range(3))
        P[ARM_INDEX[image], j] = 1
    return P


def reynolds_metric(S: sp.Matrix, reps: list[sp.Matrix]) -> sp.Matrix:
    """Reynolds projection for symmetric bilinear forms: S -> <R^T S R>."""
    acc = sp.zeros(6, 6)
    for R in reps:
        acc += R.T * S * R
    return sp.simplify(acc / len(reps))


def flat(M: sp.Matrix) -> list[sp.Rational]:
    return [sp.Rational(M[i, j]) for i in range(M.rows) for j in range(M.cols)]


def symmetric_basis(n: int) -> list[sp.Matrix]:
    out: list[sp.Matrix] = []
    for i in range(n):
        for j in range(i, n):
            M = sp.zeros(n, n)
            M[i, j] = 1
            M[j, i] = 1
            out.append(M)
    return out


def invariant_span_rank(forms: list[sp.Matrix]) -> int:
    return sp.Matrix([flat(M) for M in forms]).rank()


def is_zero(M: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in M)


def commutes_with_all(G: sp.Matrix, reps: list[sp.Matrix]) -> bool:
    return all(is_zero(R.T * G * R - G) for R in reps)


def ratio_endpoint(lambda_ratio: F) -> tuple[F, F, F]:
    """If a channel-metric ratio is used as lambda=q_E/q_T, return
    (q_E, rho_E, c_TE) under the granted T-side q_T=5/6 and s_TE=-2.
    """
    q_t = F(5, 6)
    q_e = lambda_ratio * q_t
    rho_e = 6 * (q_e - 1)
    c_te = F(-2) * q_t / q_e
    return q_e, rho_e, c_te


def main() -> int:
    print("Route-2 channel metric Schur-free-parameter no-go")
    print("=" * 88)

    group3 = oh_signed_perms()
    reps = [arm_rep(M) for M in group3]
    order = len(group3)
    I6 = sp.eye(6)

    check("O_h signed-permutation group has order 48", order == 48, f"order={order}")

    P_A1 = sum(reps, sp.zeros(6, 6)) / order
    antipodal = arm_rep(-sp.eye(3))
    P_T1 = (I6 - antipodal) / 2
    P_E = (I6 + antipodal) / 2 - P_A1
    P_ET = P_E + P_T1

    projector_ok = (
        P_A1 * P_A1 == P_A1
        and P_E * P_E == P_E
        and P_T1 * P_T1 == P_T1
        and P_A1 * P_E == sp.zeros(6, 6)
        and P_A1 * P_T1 == sp.zeros(6, 6)
        and P_E * P_T1 == sp.zeros(6, 6)
        and P_A1 + P_E + P_T1 == I6
    )
    ranks = (sp.trace(P_A1), sp.trace(P_E), sp.trace(P_T1))
    check(
        "six-arm projectors decompose as A1 (+) E (+) T1 with ranks (1,2,3)",
        projector_ok and ranks == (1, 2, 3),
        f"ranks={ranks}",
    )

    w_a, w_e, w_t = (P_A1[0, 0], P_E[0, 0], P_T1[0, 0])
    kappa = F(w_t) / F(w_e)
    check(
        "per-arm weights are (1/6, 1/3, 1/2), so kappa=w_T/w_E=3/2",
        (w_a, w_e, w_t, sp.Rational(kappa.numerator, kappa.denominator))
        == (sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(3, 2)),
        f"weights={(w_a, w_e, w_t)}, kappa={kappa}",
    )

    invariant_forms = [reynolds_metric(B, reps) for B in symmetric_basis(6)]
    rank_full = invariant_span_rank(invariant_forms)
    restricted_forms = [sp.simplify(P_ET * S * P_ET) for S in invariant_forms]
    rank_et = invariant_span_rank(restricted_forms)
    check(
        "symmetric invariant metrics have dimension 3 on arms and dimension 2 on E (+) T1",
        rank_full == 3 and rank_et == 2,
        f"rank_full={rank_full}, rank_ET={rank_et}",
    )

    seed = sp.Matrix(
        [
            [2, 1, 0, 3, -1, 4],
            [1, 5, 2, -2, 0, 1],
            [0, 2, 7, 1, 3, -1],
            [3, -2, 1, 11, 2, 0],
            [-1, 0, 3, 2, 13, 5],
            [4, 1, -1, 0, 5, 17],
        ]
    )
    S = reynolds_metric(seed, reps)
    cross_zero = is_zero(P_E * S * P_T1) and is_zero(P_T1 * S * P_E)
    a_e = sp.simplify(sp.trace(P_E * S * P_E) / sp.trace(P_E))
    a_t = sp.simplify(sp.trace(P_T1 * S * P_T1) / sp.trace(P_T1))
    scalar_blocks = is_zero(P_E * S * P_E - a_e * P_E) and is_zero(P_T1 * S * P_T1 - a_t * P_T1)
    check(
        "Reynolds-projected metric has no E/T1 cross block and scalar Schur blocks",
        cross_zero and scalar_blocks,
        f"a_E={a_e}, a_T={a_t}, cross_zero={cross_zero}",
    )

    G_ambient = P_E + P_T1
    G_one_recip = sp.Rational(1, 1) / w_e * P_E + sp.Rational(1, 1) / w_t * P_T1
    G_inv_square = sp.Rational(1, 1) / (w_e**2) * P_E + sp.Rational(1, 1) / (w_t**2) * P_T1
    check(
        "ambient, one-reciprocal, and inverse-square channel metrics are all O_h-invariant",
        all(commutes_with_all(G, reps) for G in (G_ambient, G_one_recip, G_inv_square)),
        "all three commute under R^T G R = G",
    )

    ratios = {
        "ambient": F(1, 1),
        "one_reciprocal": F(w_t) / F(w_e),
        "inverse_square": (F(w_t) / F(w_e)) ** 2,
    }
    check(
        "the invariant metric cone permits lambda ratios 1, 3/2, and 9/4",
        ratios == {"ambient": F(1, 1), "one_reciprocal": F(3, 2), "inverse_square": F(9, 4)},
        f"ratios={ratios}",
    )

    q_e_ambient, rho_ambient, cte_ambient = ratio_endpoint(F(1, 1))
    check(
        "ambient Euclidean metric would give lambda=1, rho_E=-1, c_TE=-2, not the endpoint target",
        (q_e_ambient, rho_ambient, cte_ambient) == (F(5, 6), F(-1, 1), F(-2, 1)),
        f"q_E={q_e_ambient}, rho_E={rho_ambient}, c_TE={cte_ambient}",
    )

    q_e_one, rho_one, cte_one = ratio_endpoint(F(3, 2))
    check(
        "one reciprocal projector/dimension normalization gives lambda=3/2, rho_E=3/2, c_TE=-4/3",
        (q_e_one, rho_one, cte_one) == (F(5, 4), F(3, 2), F(-4, 3)),
        f"q_E={q_e_one}, rho_E={rho_one}, c_TE={cte_one}",
    )

    q_e_target, rho_target, cte_target = ratio_endpoint(F(9, 4))
    check(
        "inverse-square normalization gives the target, but only by choosing c_E/c_T=9/4",
        (q_e_target, rho_target, cte_target) == (F(15, 8), F(21, 4), F(-8, 9)),
        f"q_E={q_e_target}, rho_E={rho_target}, c_TE={cte_target}",
    )

    direct_power = (F(w_e) / F(w_t))
    square_power = direct_power**2
    reciprocal_square = direct_power ** -2
    check(
        "projector-weight powers distinguish the gap: w gives 2/3, w^2 gives 4/9, w^-1 gives 3/2, w^-2 gives 9/4",
        (direct_power, square_power, direct_power**-1, reciprocal_square)
        == (F(2, 3), F(4, 9), F(3, 2), F(9, 4)),
        f"powers={(direct_power, square_power, direct_power**-1, reciprocal_square)}",
    )

    endpoint_triple = (F(-1, 1), F(-2, 1), rho_target)
    check(
        "exact readout target triple is recovered only at inverse-square lambda",
        endpoint_triple == (F(-1, 1), F(-2, 1), F(21, 4)),
        f"(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E)={endpoint_triple}",
    )

    free_ratio_examples = [F(1, 5), F(1, 1), F(3, 2), F(9, 4), F(7, 1)]
    all_invariant = True
    for r in free_ratio_examples:
        G = sp.Rational(r.numerator, r.denominator) * P_E + P_T1
        all_invariant = all_invariant and commutes_with_all(G, reps)
    check(
        "Schur leaves c_E/c_T free across a continuum of positive invariant channel metrics",
        all_invariant,
        f"checked ratios={free_ratio_examples}",
    )

    print("\n" + "=" * 88)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: no-go for the pure O_h channel-metric route. The allowed positive\n"
        "channel metrics on E (+) T1 are G(c_E,c_T)=c_E P_E + c_T P_T1 with c_E/c_T\n"
        "free. Symmetry alone permits ambient lambda=1, one-reciprocal lambda=3/2,\n"
        "and inverse-square lambda=9/4. The endpoint value is therefore not derived\n"
        "by declaring a channel metric; it is obtained only by supplying the inverse-\n"
        "square normalization law as an extra primitive."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
