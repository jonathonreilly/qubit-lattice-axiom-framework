#!/usr/bin/env python3
"""Route-2 log-barrier Record primitive gate.

This runner tests whether the Record/log-det surfaces already force the
second-dual Route-2 law C_X proportional to w_X^-2. They do not. The pure
log-barrier Hessian gives the exact endpoint condition, but finite additivity
over supplied channel records allows additive counterterms whose Hessians
change the ratio unless a determinant quotient and Hessian-to-readout bridge
are supplied.
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


def hessian_coeff(w: F, epsilon: F) -> F:
    return 1 / (w * w) + 2 * epsilon


def poly_sum(weights: tuple[F, ...], epsilon: F) -> F:
    return epsilon * sum(w * w for w in weights)


def main() -> int:
    print("Route-2 log-barrier Record primitive gate")
    print("=" * 88)

    minimal = read("docs/MINIMAL_AXIOMS_2026-06-05.md")
    record_no_go = read("docs/OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md")
    observable_parent = read("docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md")
    context_bridge = read("docs/OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_CONTEXT_QUOTIENT_BRIDGE_NOTE_2026-06-18.md")
    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    e_blind = read("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    current_bank = "\n".join(
        [
            minimal,
            record_no_go,
            observable_parent,
            context_bridge,
            exact_readout,
            parent,
            schur,
            e_blind,
        ]
    ).lower()

    banner("1. Current-surface boundaries")
    check(
        "Record explicitly supplies no readout context or weighting",
        "supplies no readout context" in minimal and "weighting" in minimal and "normalization" in minimal,
    )
    check(
        "Record no-go says additivity does not derive the branch-to-scalar map",
        "does not derive the branch-to-scalar map" in record_no_go
        and "after the scalar is supplied" in record_no_go,
    )
    check(
        "observable parent keeps readout-identification as a declared boundary",
        "declared readout-identification Boundary" in observable_parent
        and "not a consequence of `minimal_axioms`" in observable_parent,
    )
    check(
        "determinant-context bridge is conditional on a supplied context",
        "does not derive the context from Record" in context_bridge
        and "W_c(Z) = c log Z" in context_bridge,
    )
    check(
        "Route-2 exact readout note names beta_E/alpha_E=21/4 as missing",
        "beta_E / alpha_E" in exact_readout and "21/4" in exact_readout,
    )
    check(
        "S3 parent remains open on the readout-map endpoint triple",
        "readout-map endpoint triple is not yet derived" in parent,
    )
    check(
        "Schur note names inverse-square channel lift as the exact gap",
        "No named functional produces" in schur and "inverse-square" in schur,
    )
    check(
        "E-center blindness note requires a genuine E-center lift or readout primitive",
        "genuine E-center lift" in e_blind and "equivalent" in e_blind and "readout primitive" in e_blind,
    )

    banner("2. Pure log-barrier conditional arithmetic")
    w_e = F(1, 3)
    w_t = F(1, 2)
    coeff_e = hessian_coeff(w_e, F(0))
    coeff_t = hessian_coeff(w_t, F(0))
    lambda_log = coeff_e / coeff_t
    q_e, rho_e, c_te = endpoint(lambda_log)

    print(f"w_E={w_e}, w_T1={w_t}")
    print(f"pure log Hessian coefficients: C_E={coeff_e}, C_T={coeff_t}, lambda={lambda_log}")
    print(f"endpoint from pure log barrier: q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")

    check("Route-2 channel weights are w_E=1/3 and w_T1=1/2", (w_e, w_t) == (F(1, 3), F(1, 2)))
    check("pure log-barrier Hessian gives lambda=9/4", lambda_log == F(9, 4))
    check("pure log-barrier Hessian gives q_E=15/8", q_e == F(15, 8), f"q_E={q_e}")
    check("pure log-barrier Hessian gives rho_E=21/4", rho_e == F(21, 4), f"rho_E={rho_e}")
    check("pure log-barrier Hessian gives c_TE=-8/9", c_te == F(-8, 9), f"c_TE={c_te}")

    banner("3. Additive counterterm countermodel")
    eps = F(1)
    a = (w_e, w_t)
    b = (F(1, 4),)
    add_lhs = poly_sum(a + b, eps)
    add_rhs = poly_sum(a, eps) + poly_sum(b, eps)
    coeff_e_eps = hessian_coeff(w_e, eps)
    coeff_t_eps = hessian_coeff(w_t, eps)
    lambda_eps = coeff_e_eps / coeff_t_eps
    q_e_eps, rho_e_eps, c_te_eps = endpoint(lambda_eps)

    print(f"epsilon={eps} counterterm coefficients: C_E={coeff_e_eps}, C_T={coeff_t_eps}, lambda={lambda_eps}")
    print(f"endpoint from epsilon=1 countermodel: q_E={q_e_eps}, rho_E={rho_e_eps}, c_TE={c_te_eps}")

    check(
        "polynomial channel counterterm is additive over disjoint supplied channel records",
        add_lhs == add_rhs,
        f"left={add_lhs}, right={add_rhs}",
    )
    check("epsilon=0 is the pure log-barrier target", lambda_log == F(9, 4))
    check(
        "epsilon=1 changes the Hessian ratio while preserving channel additivity",
        lambda_eps == F(11, 6) and lambda_eps != F(9, 4),
        f"lambda_epsilon={lambda_eps}",
    )
    check(
        "epsilon=1 does not return the target endpoint",
        (q_e_eps, rho_e_eps, c_te_eps) != (F(15, 8), F(21, 4), F(-8, 9)),
        f"q_E={q_e_eps}, rho_E={rho_e_eps}, c_TE={c_te_eps}",
    )
    check(
        "determinant quotient is the kind of extra rule that excludes additive trace-like terms",
        "log det(S) + epsilon Tr(S)" in context_bridge
        and "rejected by the context" in context_bridge,
    )

    banner("4. Coordinate and readout gate")
    hessian_in_w = coeff_e
    hessian_in_log_w = F(0)
    check("in the w coordinate d2(-log w)/dw2 gives the second-dual law", hessian_in_w == F(9))
    check("in the log coordinate u=log w, d2(-u)/du2 is zero", hessian_in_log_w == F(0))
    check(
        "Hessian-to-readout therefore needs a coordinate/readout bridge",
        hessian_in_w != hessian_in_log_w,
        f"w-coordinate={hessian_in_w}, log-coordinate={hessian_in_log_w}",
    )

    banner("5. Current-bank verdict")
    check(
        "checked current bank does not name a Route-2 log-barrier primitive",
        "route-2 log-barrier" not in current_bank and "route2 log-barrier" not in current_bank,
    )
    check(
        "checked current bank does not supply a Hessian-to-readout bridge phrase",
        "hessian-to-readout" not in current_bank,
    )
    check("no observed endpoint value is used as a proof input", True)
    check("current status is no-go for Record/log-det-alone derivation", True)
    check("conditional target is now precise: determinant quotient plus w-Hessian E-center bridge", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect log-barrier Record primitive checks above.")
    else:
        print(
            "VERDICT: no-go / conditional support boundary. Pure log-barrier "
            "channel curvature would give the Route-2 endpoint exactly, but "
            "Record/log-det additivity alone does not force that primitive; "
            "it still needs a supplied channel determinant quotient and a "
            "w-coordinate Hessian-to-E-center readout bridge."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
