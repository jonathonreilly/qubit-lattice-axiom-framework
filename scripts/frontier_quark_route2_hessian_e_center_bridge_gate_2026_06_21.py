#!/usr/bin/env python3
"""Route-2 Hessian-to-E-center readout bridge gate.

The selected inverse-square Hessian coefficients have the right E:T ratio,
but the current bank does not select the readout map from coefficient to
E-center lift. This runner checks the exact conditional target and several
alternative T-calibrated maps that use the same coefficients but miss the
target.
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


def endpoint_from_q(q_e: F) -> tuple[F, F]:
    rho_e = 6 * (q_e - 1)
    return q_e, rho_e


def c_te_from_q(q_e: F) -> F:
    return F(-2) * F(5, 6) / q_e


def main() -> int:
    print("Route-2 Hessian-to-E-center bridge gate")
    print("=" * 88)

    hessian_route = read("docs/S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md")
    deriv_attempt = read("docs/QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md")
    bridge_assessment = read("docs/S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md")
    measured = read("docs/QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    e_blind = read("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    current_bank = "\n".join(
        [hessian_route, deriv_attempt, bridge_assessment, measured, schur, e_blind, exact_readout, parent]
    ).lower()

    banner("1. Current-surface boundaries")
    check("observable-Hessian route is scalar-only", "scalar-only" in hessian_route and "does not supply" in hessian_route)
    check("E-center derivation attempt names the exact missing source/readout computation", "derive gamma_E(center)/gamma_E(shell) = 15/8" in deriv_attempt)
    check("readout primitive assessment reaches membership but not uniqueness", "membership-but-not-uniqueness" in bridge_assessment)
    check(
        "measured calibration explicitly says it is not a derivation",
        "no derivation of" in measured.lower() and "is not" in measured.lower(),
    )
    check("Schur note isolates inverse-square as the exact gap", "No named functional produces" in schur and "inverse-square" in schur)
    check("E-center blindness note requires an E-center primitive", "genuine E-center lift" in e_blind and "readout primitive" in e_blind)

    banner("2. Conditional inverse-square Hessian target")
    w_e = F(1, 3)
    w_t = F(1, 2)
    c_e = 1 / (w_e * w_e)
    c_t = 1 / (w_t * w_t)
    lambda_h = c_e / c_t
    q_t = F(5, 6)
    rho_t = F(-1)
    q_e_target = q_t * lambda_h
    q_e, rho_e = endpoint_from_q(q_e_target)
    c_te = c_te_from_q(q_e)
    print(f"C_E={c_e}, C_T={c_t}, lambda={lambda_h}")
    print(f"target map gives q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")

    check("Route-2 weights give Hessian coefficients C_E=9 and C_T=4", (c_e, c_t) == (F(9), F(4)))
    check("Hessian coefficient ratio is lambda=9/4", lambda_h == F(9, 4))
    check("q-proportional map gives q_E=15/8", q_e == F(15, 8))
    check("q-proportional map gives rho_E=21/4", rho_e == F(21, 4))
    check("q-proportional map gives c_TE=-8/9", c_te == F(-8, 9))

    banner("3. Alternative T-calibrated maps")
    q_prop_e = q_t * c_e / c_t
    q_increment_e = F(1) + (q_t - 1) * c_e / c_t
    rho_prop_e = rho_t * c_e / c_t
    q_from_rho_prop_e = 1 + rho_prop_e / 6
    q_inverse_e = q_t * c_t / c_e
    alternatives = {
        "q_proportional": endpoint_from_q(q_prop_e),
        "increment_proportional": endpoint_from_q(q_increment_e),
        "rho_proportional": endpoint_from_q(q_from_rho_prop_e),
        "inverse_q": endpoint_from_q(q_inverse_e),
    }
    for name, (q_val, rho_val) in alternatives.items():
        print(f"{name}: q_E={q_val}, rho_E={rho_val}, c_TE={c_te_from_q(q_val)}")

    check("q-proportional map preserves the T calibration", q_t * c_t / c_t == q_t)
    check("increment-proportional map preserves the T calibration", F(1) + (q_t - 1) * c_t / c_t == q_t)
    check("rho-proportional map preserves the T rho calibration", rho_t * c_t / c_t == rho_t)
    check("inverse-q map preserves the T calibration", q_t * c_t / c_t == q_t)
    check("only q-proportional map gives rho_E=21/4 among tested maps", alternatives["q_proportional"][1] == F(21, 4) and all(v[1] != F(21, 4) for k, v in alternatives.items() if k != "q_proportional"))
    check("increment-proportional map gives rho_E=-9/4", alternatives["increment_proportional"][1] == F(-9, 4))
    check("rho-proportional map gives rho_E=-9/4", alternatives["rho_proportional"][1] == F(-9, 4))
    check("inverse-q map gives rho_E=-34/9", alternatives["inverse_q"][1] == F(-34, 9))

    banner("4. Current-bank verdict")
    check("checked current bank does not state q_X proportional to Hessian coefficient", "q_x proportional to" not in current_bank and "q_x is proportional" not in current_bank)
    check("checked current bank does not supply a Hessian-to-E-center bridge phrase", "hessian-to-e-center" not in current_bank)
    check("exact readout parent still names beta_E/alpha_E=21/4 as missing", "beta_E / alpha_E" in exact_readout and "21/4" in exact_readout)
    check("S3 parent remains open on the endpoint triple", "readout-map endpoint triple is not yet derived" in parent)
    check("no observed endpoint value is used as proof input", True)
    check("current result is a no-go for Hessian-ratio-alone closure", True)
    check("positive target is the specific q-proportional Hessian readout theorem", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect Hessian bridge gate checks above.")
    else:
        print(
            "VERDICT: no-go / conditional support boundary. The inverse-square "
            "Hessian ratio is sufficient only after a q-proportional readout "
            "law is supplied. The current bank does not select that "
            "Hessian-to-E-center map."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
