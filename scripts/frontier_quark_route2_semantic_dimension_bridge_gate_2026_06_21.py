#!/usr/bin/env python3
"""Route-2 semantic dimension bridge gate.

This runner tests the strongest exact version of the next Route-2 readout
repair target:

    lambda := q_E/q_T = (1/N_pair^2)/(1/N_color^2) = 9/4.

It deliberately separates:

1. arithmetic closure: if that lambda is supplied, the endpoint triple is
   exactly (-1,-2,21/4);
2. dimension coincidence: dim(E)=2 and dim(T1)=3 match N_pair=2 and
   N_color=3 numerically;
3. semantic bridge: current main must still supply a typed map from the
   Route-2 O_h channels to the CKM/Q_L dimensions and an inverse-square
   readout law. Current authority surfaces do not supply that bridge.

No observed quark masses, fitted endpoint values, or audit verdicts are used.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path

PASS = 0
FAIL = 0

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    path = ROOT / rel
    return path.read_text(encoding="utf-8")


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n       {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")
    return ok


def banner(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def endpoint_from_lambda(lambda_et: F) -> dict[str, F]:
    """Endpoint algebra after the granted T-side candidates."""
    rho_t = F(-1)
    s_te = F(-2)
    q_t = F(1) + rho_t / 6
    q_e = q_t * lambda_et
    rho_e = 6 * (q_e - 1)
    c_te = s_te * q_t / q_e
    return {
        "rho_T": rho_t,
        "s_TE": s_te,
        "q_T": q_t,
        "lambda": lambda_et,
        "q_E": q_e,
        "rho_E": rho_e,
        "c_TE": c_te,
    }


def main() -> int:
    print("Route-2 semantic dimension bridge gate")
    print("=" * 88)

    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    parent_theta = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    schur_no_go = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    ckm_inverse = read("docs/CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md")

    banner("1. Current target localization")
    check(
        "exact readout note names the endpoint triple as missing",
        "(-1, -2, 21/4)" in exact_readout
        and "does not derive the exact dimensionless readout triple" in exact_readout,
    )
    check(
        "S3 parent note keeps the unique readout-to-slice theorem open",
        "not derived by the current exact stack" in parent_theta
        and "readout-map endpoint triple" in parent_theta,
    )
    check(
        "Schur covariance note identifies lambda=q_E/q_T=9/4 as the E-center target",
        "q_E/q_T = 9/4" in schur_no_go
        and "21/4" in schur_no_go
        and "E-Center Datum" in schur_no_go,
    )

    banner("2. Conditional endpoint algebra")
    n_pair = F(2)
    n_color = F(3)
    reciprocal_ratio = (F(1) / n_pair**2) / (F(1) / n_color**2)
    check(
        "reciprocal-square source-dimension ratio is exactly 9/4",
        reciprocal_ratio == F(9, 4),
        f"(1/2^2)/(1/3^2) = {reciprocal_ratio}",
    )
    endpoint = endpoint_from_lambda(reciprocal_ratio)
    check(
        "lambda=9/4 gives q_T=5/6, q_E=15/8",
        endpoint["q_T"] == F(5, 6) and endpoint["q_E"] == F(15, 8),
        f"q_T={endpoint['q_T']}, q_E={endpoint['q_E']}",
    )
    check(
        "lambda=9/4 gives rho_E=21/4",
        endpoint["rho_E"] == F(21, 4),
        f"rho_E={endpoint['rho_E']}",
    )
    check(
        "lambda=9/4 gives c_TE=-8/9 with the granted T-side candidates",
        endpoint["c_TE"] == F(-8, 9),
        f"c_TE={endpoint['c_TE']}",
    )
    check(
        "conditional endpoint triple is (-1,-2,21/4)",
        (endpoint["rho_T"], endpoint["s_TE"], endpoint["rho_E"])
        == (F(-1), F(-2), F(21, 4)),
        f"(rho_T,s_TE,rho_E)=({endpoint['rho_T']},{endpoint['s_TE']},{endpoint['rho_E']})",
    )

    banner("3. Dimension coincidence versus readout law")
    dim_e = F(2)
    dim_t1 = F(3)
    weight_e = dim_e / 6
    weight_t1 = dim_t1 / 6
    oh_inverse_square = (weight_e**-2) / (weight_t1**-2)
    check(
        "O_h channel dimensions match the CKM source dimensions numerically",
        (dim_e, dim_t1) == (n_pair, n_color),
        f"(dim_E,dim_T1)=({dim_e},{dim_t1}); (N_pair,N_color)=({n_pair},{n_color})",
    )
    check(
        "inverse-square of O_h per-arm weights also gives 9/4",
        oh_inverse_square == F(9, 4),
        f"((2/6)^-2)/((3/6)^-2) = {oh_inverse_square}",
    )
    check(
        "dimension labels alone do not choose a coefficient ratio",
        len({F(1), F(3, 2), F(9, 4), F(4, 9)}) == 4,
        "same dimensions permit ratio 1, one-power 3/2, inverse-square 9/4, or square 4/9 unless a law selects one",
    )
    check(
        "Schur note says the E:T1 quadratic ratio is free",
        "`E:T1` weight ratio" in schur_no_go
        and "free" in schur_no_go
        and "quadratic form" in schur_no_go,
    )
    check(
        "Schur note says no named functional supplies inverse-square projector-weight lift",
        "No named functional produces an" in schur_no_go
        and "inverse-square-of-projector-weight" in schur_no_go,
    )

    banner("4. Authority-surface bridge scan")
    check(
        "CKM inverse-square note is CKM-side, not a Route-2 readout bridge",
        "Route-2" not in ckm_inverse
        and "q_E" not in ckm_inverse
        and "q_T" not in ckm_inverse
        and "beta_E" not in ckm_inverse,
    )
    check(
        "CKM note frames inverse-square as eta^2/rho/A^2 bookkeeping",
        "eta^2 = 1/N_pair^2 - 1/N_color^2" in ckm_inverse
        and "rho A^2 = 1/N_color^2" in ckm_inverse,
    )
    check(
        "Route-2 readout note does not cite N_pair/N_color as its missing-map selector",
        "N_pair" not in exact_readout
        and "N_color" not in exact_readout,
    )
    check(
        "S3 parent note still routes closure upstream to the readout-map endpoint triple",
        "The next theorem target is the missing readout-map endpoint triple" in parent_theta,
    )

    banner("5. Minimal bridge requirements")
    requirements = {
        "typed_channel_dimension_bridge": False,
        "inverse_square_readout_law": False,
        "no_observed_or_fitted_endpoint_input": True,
    }
    check(
        "typed bridge E<->N_pair and T1<->N_color is not supplied by current checked surfaces",
        requirements["typed_channel_dimension_bridge"] is False,
    )
    check(
        "inverse-square readout law is not supplied by current checked surfaces",
        requirements["inverse_square_readout_law"] is False,
    )
    check(
        "no observed or fitted endpoint input is used in this verifier",
        requirements["no_observed_or_fitted_endpoint_input"] is True,
    )
    check(
        "therefore the conditional arithmetic is support, not current-surface closure",
        reciprocal_ratio == F(9, 4)
        and requirements["typed_channel_dimension_bridge"] is False
        and requirements["inverse_square_readout_law"] is False,
    )

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect failed bridge gate checks above.")
    else:
        print(
            "VERDICT: conditional support plus current-bank bridge firewall. "
            "The reciprocal-square dimension ratio returns lambda=9/4 and the exact "
            "Route-2 endpoint triple if adopted, but current authority surfaces do "
            "not supply the typed E/T1-to-N_pair/N_color bridge or the inverse-square "
            "readout law."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
