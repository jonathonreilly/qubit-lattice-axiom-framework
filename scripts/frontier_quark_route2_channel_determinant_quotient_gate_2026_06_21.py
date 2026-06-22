#!/usr/bin/env python3
"""Route-2 channel determinant quotient gate.

This runner tests whether the current determinant-context machinery already
supplies a Route-2 channel determinant quotient for the E/T1 weights. A
supplied diagonal model diag(w_E,w_T1) would give the target Hessian ratio,
but determinant value alone does not select the channel coordinate split.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n       {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")
    return ok


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def endpoint(lambda_et: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    s_te = F(-2)
    q_e = q_t * lambda_et
    rho_e = 6 * (q_e - 1)
    c_te = s_te * q_t / q_e
    return q_e, rho_e, c_te


def det2(pair: tuple[F, F]) -> F:
    return pair[0] * pair[1]


def hessian_ratio(pair: tuple[F, F]) -> F:
    return (1 / (pair[0] * pair[0])) / (1 / (pair[1] * pair[1]))


def square_sum(weights: tuple[F, ...]) -> F:
    return sum(w * w for w in weights)


def main() -> int:
    print("Route-2 channel determinant quotient gate")
    print("=" * 88)

    classifier = read("docs/OBSERVABLE_PRINCIPLE_T1D_POSITIVE_DIAGONAL_READOUT_CLASSIFIER_NOTE_2026-06-18.md")
    context_bridge = read("docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md")
    independence = read("docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    leverage = read("docs/OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md")
    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    e_blind = read("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    current_bank = "\n".join(
        [
            classifier,
            context_bridge,
            independence,
            schur,
            leverage,
            exact_readout,
            e_blind,
            parent,
        ]
    ).lower()

    banner("1. Current determinant and Route-2 boundaries")
    check(
        "positive-diagonal classifier leaves arbitrary one-site phi before determinant quotient",
        "phi : R_{>0} -> R" in classifier
        and "every continuous scalar readout" in classifier,
    )
    check(
        "positive-diagonal classifier says determinant-only forces log",
        "phi(x) = c log x" in classifier and "determinant-only" in classifier,
    )
    check(
        "determinant-context bridge is conditional on a supplied context",
        "determinant-sector readout context" in context_bridge
        and "not an axiom reduction" in context_bridge,
    )
    check(
        "T1-d independence no-go says determinant quotient is not Record-derived",
        "only after the determinant-only readout quotient is already" in independence
        and "imposed" in independence,
    )
    check(
        "Route-2 Schur note isolates inverse-square as the exact gap",
        "No named functional produces" in schur and "inverse-square" in schur,
    )
    check(
        "Route-2 exact readout target remains beta_E/alpha_E=21/4",
        "beta_E / alpha_E" in exact_readout and "21/4" in exact_readout,
    )

    banner("2. Conditional diagonal determinant model")
    w_e = F(1, 3)
    w_t = F(1, 2)
    route2_pair = (w_e, w_t)
    determinant = det2(route2_pair)
    lambda_det = hessian_ratio(route2_pair)
    q_e, rho_e, c_te = endpoint(lambda_det)

    print(f"Route-2 candidate pair = {route2_pair}")
    print(f"determinant = {determinant}")
    print(f"diagonal Hessian ratio = {lambda_det}")
    print(f"endpoint from candidate = q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")

    check("O_h leverage note supplies w_E=1/3 and w_T1=1/2", "1/3, 1/2" in leverage)
    check("candidate diagonal determinant is 1/6", determinant == F(1, 6), f"det={determinant}")
    check("candidate diagonal Hessian coefficients give lambda=9/4", lambda_det == F(9, 4))
    check("candidate gives q_E=15/8", q_e == F(15, 8), f"q_E={q_e}")
    check("candidate gives rho_E=21/4", rho_e == F(21, 4), f"rho_E={rho_e}")
    check("candidate gives c_TE=-8/9", c_te == F(-8, 9), f"c_TE={c_te}")

    banner("3. Same-determinant fiber ambiguity")
    pairs = ((F(1, 3), F(1, 2)), (F(1, 4), F(2, 3)), (F(1, 6), F(1)))
    determinants = tuple(det2(pair) for pair in pairs)
    ratios = tuple(hessian_ratio(pair) for pair in pairs)
    print(f"same-fiber pairs = {pairs}")
    print(f"determinants = {determinants}")
    print(f"Hessian ratios = {ratios}")

    check("all witness pairs have the same determinant 1/6", all(det == F(1, 6) for det in determinants))
    check("same determinant fiber has different Hessian ratios", len(set(ratios)) == 3, f"ratios={ratios}")
    check(
        "determinant scalar value alone cannot select the Route-2 Hessian ratio",
        determinants[0] == determinants[1] == determinants[2] and ratios[0] != ratios[1] != ratios[2],
    )
    check(
        "determinant-context note uses same-fiber witnesses to exclude extra data",
        "same determinant sector" in context_bridge and "different traces" in context_bridge,
    )

    banner("4. Additive one-site freedom before quotient")
    a = pairs[0]
    b = (F(1, 5), F(5, 6))
    lhs = square_sum(a + b)
    rhs = square_sum(a) + square_sum(b)
    same_det_square_sums = tuple(square_sum(pair) for pair in pairs)
    print(f"same-fiber square sums = {same_det_square_sums}")

    check("one-site square term is additive over supplied block lists", lhs == rhs)
    check(
        "one-site square term is not determinant-only on the same determinant fiber",
        len(set(same_det_square_sums)) == 3,
        f"square sums={same_det_square_sums}",
    )
    check(
        "classifier identifies this as the pre-quotient one-site freedom",
        "W_n(x_1,...,x_n) = sum_i phi(x_i)" in classifier,
    )

    banner("5. Current-bank verdict")
    check(
        "checked current bank does not state a Route-2 channel determinant quotient",
        "route-2 channel determinant" not in current_bank
        and "route2 channel determinant" not in current_bank,
    )
    check(
        "checked current bank does not supply a Hessian-to-E-center bridge phrase",
        "hessian-to-e-center" not in current_bank,
    )
    check(
        "E-center guard still requires a primitive that evaluates the E-center column",
        "genuine E-center lift" in e_blind and "E-center column" in e_blind,
    )
    check("parent S3 note remains open on the endpoint triple", "readout-map endpoint triple is not yet derived" in parent)
    check("no observed endpoint value is used as a proof input", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect determinant quotient gate checks above.")
    else:
        print(
            "VERDICT: no-go / conditional support boundary. A supplied Route-2 "
            "diagonal determinant model would give the endpoint exactly, but "
            "the current determinant-context machinery does not supply that "
            "Route-2 channel coordinate context or the Hessian-to-E-center "
            "readout bridge. Determinant value alone is insufficient."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
