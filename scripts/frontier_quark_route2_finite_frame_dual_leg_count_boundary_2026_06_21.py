"""Route-2 finite-frame/Riesz dual leg-count boundary.

Question
--------
Can finite-frame/Riesz duality on the six-arm O_h star derive the Route-2
endpoint factor lambda = q_E/q_T = 9/4?

Result
------
Not on the current surface. The exact frame facts are:

* unnormalized projected arm frames are Parseval on each channel, so they give
  no reciprocal projector-weight factor (lambda = 1);
* unit-normalized projected arm analysis has one reciprocal frame-bound factor,
  giving lambda = (1/w_E)/(1/w_T) = 3/2;
* two independent unit-frame analysis legs give lambda = 9/4.

The target is therefore conditionally reproduced by a two-analysis-leg
primitive, but the current exact Route-2 readout map observes only the product
lambda and contains no theorem selecting leg_count = 2 or a source/readout
split. Canonical Riesz reconstruction itself cancels the frame bound rather
than producing an endpoint lift.
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
        image = M * sp.Matrix(arm)
        P[ARM_INDEX[tuple(int(image[k]) for k in range(3))], j] = 1
    return P


def projected_frame_operator(P: sp.Matrix, unit_normalized: bool) -> sp.Matrix:
    """Sum |f_a><f_a| for f_a=P e_a, optionally divided by sqrt(w)."""
    w = sp.Rational(P[0, 0])
    S = sp.zeros(6, 6)
    for a in range(6):
        e = sp.zeros(6, 1)
        e[a, 0] = 1
        f = P * e
        S += f * f.T
    if unit_normalized:
        S = sp.simplify(S / w)
    return sp.simplify(S)


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    c_te = F(-2) * q_t / q_e
    return q_e, rho_e, c_te


def main() -> int:
    print("Route-2 finite-frame/Riesz dual leg-count boundary")
    print("=" * 88)

    reps = [arm_rep(M) for M in oh_signed_perms()]
    order = len(reps)
    I6 = sp.eye(6)
    P_A1 = sum(reps, sp.zeros(6, 6)) / order
    antipodal = arm_rep(-sp.eye(3))
    P_T1 = (I6 - antipodal) / 2
    P_E = (I6 + antipodal) / 2 - P_A1

    ranks = (sp.trace(P_A1), sp.trace(P_E), sp.trace(P_T1))
    w_e = sp.Rational(P_E[0, 0])
    w_t = sp.Rational(P_T1[0, 0])
    check(
        "six-arm O_h decomposition gives ranks (A1,E,T1)=(1,2,3) and weights w_E=1/3, w_T=1/2",
        order == 48 and ranks == (1, 2, 3) and (w_e, w_t) == (sp.Rational(1, 3), sp.Rational(1, 2)),
        f"order={order}, ranks={ranks}, w_E={w_e}, w_T={w_t}",
    )

    S_E_un = projected_frame_operator(P_E, unit_normalized=False)
    S_T_un = projected_frame_operator(P_T1, unit_normalized=False)
    check(
        "unnormalized projected arm frames are Parseval: sum |P_X e_a><P_X e_a| = P_X",
        S_E_un == P_E and S_T_un == P_T1,
        "E and T1 unnormalized frame operators equal their projectors",
    )

    S_E_unit = projected_frame_operator(P_E, unit_normalized=True)
    S_T_unit = projected_frame_operator(P_T1, unit_normalized=True)
    check(
        "unit-normalized projected arm analysis has frame bounds 1/w_E=3 and 1/w_T=2",
        S_E_unit == 3 * P_E and S_T_unit == 2 * P_T1,
        f"S_E_unit factor={1/w_e}, S_T_unit factor={1/w_t}",
    )

    dual_E_unit = w_e * S_E_unit
    dual_T_unit = w_t * S_T_unit
    check(
        "canonical Riesz dual reconstruction cancels the unit-frame bound on each channel",
        dual_E_unit == P_E and dual_T_unit == P_T1,
        "S_X^{-1} S_X = P_X on each irreducible channel",
    )

    lambda_0 = F(1, 1)
    lambda_1 = F(1, int(w_e.denominator))  # overwritten below for clarity
    lambda_1 = F(1, 1) / F(w_e) / (F(1, 1) / F(w_t))
    lambda_2 = lambda_1 * lambda_1
    check(
        "leg-count ladder is exact: n=0 -> lambda=1, n=1 -> 3/2, n=2 -> 9/4",
        (lambda_0, lambda_1, lambda_2) == (F(1, 1), F(3, 2), F(9, 4)),
        f"lambda_n={(lambda_0, lambda_1, lambda_2)}",
    )

    consequences = {n: endpoint_from_lambda(lam) for n, lam in [(0, lambda_0), (1, lambda_1), (2, lambda_2)]}
    check(
        "only two reciprocal analysis legs reproduce rho_E=21/4 under the granted T-side algebra",
        consequences[0] == (F(5, 6), F(-1, 1), F(-2, 1))
        and consequences[1] == (F(5, 4), F(3, 2), F(-4, 3))
        and consequences[2] == (F(15, 8), F(21, 4), F(-8, 9)),
        f"consequences={consequences}",
    )

    split_examples = [
        (F(1, 1), F(9, 4)),
        (F(3, 2), F(3, 2)),
        (F(9, 4), F(1, 1)),
        (F(27, 16), F(4, 3)),
    ]
    product_fixed = all(a * b == F(9, 4) for a, b in split_examples)
    check(
        "source/readout leg split is product-gauge under the endpoint algebra: many splits give lambda=9/4",
        product_fixed,
        f"splits={split_examples}",
    )

    readout_product_only = []
    for a, b in split_examples:
        q_e, rho_e, c_te = endpoint_from_lambda(a * b)
        readout_product_only.append((rho_e, c_te))
    check(
        "the reduced readout endpoint observes only the product lambda, not the split into two legs",
        len(set(readout_product_only)) == 1 and readout_product_only[0] == (F(21, 4), F(-8, 9)),
        f"observed={(readout_product_only[0])}",
    )

    wrong_leg_counts = {
        "parseval_or_reconstruction": endpoint_from_lambda(lambda_0),
        "single_analysis_leg": endpoint_from_lambda(lambda_1),
    }
    check(
        "canonical reconstruction and one-leg analysis are exact falsifiers for endpoint-lift claims",
        wrong_leg_counts["parseval_or_reconstruction"][1] == F(-1, 1)
        and wrong_leg_counts["single_analysis_leg"][1] == F(3, 2),
        f"rho values={wrong_leg_counts}",
    )

    print("\n" + "=" * 88)
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "\nVERDICT: conditional-support / no-go boundary. Finite-frame analysis explains\n"
        "where the target 9/4 can come from: two reciprocal unit-frame analysis legs.\n"
        "But canonical Riesz reconstruction cancels the frame bound, one analysis leg\n"
        "gives only 3/2, and the current exact readout map observes only the product\n"
        "rather than a derived source/readout split. Therefore a two-leg primitive is\n"
        "extra theorem content, not a current derivation of rho_E=21/4."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
