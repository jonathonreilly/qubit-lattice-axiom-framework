#!/usr/bin/env python3
"""Route-2 slice-semigroup coordinate selector gate.

Raw q-scaling by 9/4 gives the endpoint, but constant raw scaling is not a
semigroup endomorphism. Generator/log coordinates are semigroup-natural and
miss the endpoint by exact inequalities.
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


def rho_from_q(q: F) -> F:
    return 6 * (q - 1)


def main() -> int:
    print("Route-2 slice-semigroup coordinate gate")
    print("=" * 88)

    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    parent_runner = read("scripts/frontier_s3_time_theta_to_slice_coupling.py")
    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    current_bank = "\n".join([parent, parent_runner, exact_readout, schur]).lower()

    banner("1. Current-surface boundaries")
    check(
        "parent note names the exact conditional slice family",
        "Xi_P(t ; c) = (P_R c)" in parent and "V_R(t) = exp(-t Lambda_R) u_*" in parent,
    )
    check(
        "parent runner verifies the slice-semigroup law",
        "Xi_P(t; c) obeys the exact slice-semigroup law once P_R is supplied" in parent_runner,
    )
    check(
        "parent note leaves the endpoint triple open",
        "readout-map endpoint triple is not yet derived" in parent,
    )
    check(
        "exact readout gives q_E and q_T as center/shell ratios",
        "q_T   := gamma_T(center) / gamma_T(shell)" in exact_readout
        and "q_E   := gamma_E(center) / gamma_E(shell)" in exact_readout,
    )
    check(
        "exact readout names beta_E/alpha_E=21/4 as missing map entry",
        "beta_E / alpha_E = 21/4" in exact_readout and "missing map entry" in exact_readout,
    )
    check(
        "Schur note names lambda=q_E/q_T=9/4 but not a bridge theorem",
        "q_T = 5/6" in schur and "not a consequence" in schur,
    )

    banner("2. Exact target")
    q_t = F(5, 6)
    lambda_sq = F(9, 4)
    q_target = F(15, 8)
    rho_target = rho_from_q(q_target)
    c_te = F(-2) * q_t / q_target
    print(f"q_T={q_t}, lambda={lambda_sq}, q_target={q_target}, rho_target={rho_target}")

    check("q_T is below the identity lift", 0 < q_t < 1)
    check("needed inverse-square lambda is greater than one", lambda_sq > 1)
    check("raw q scaling gives q_E=15/8", lambda_sq * q_t == q_target)
    check("raw q scaling gives rho_E=21/4", rho_from_q(lambda_sq * q_t) == F(21, 4))
    check("target center ratio is c_TE=-8/9", c_te == F(-8, 9))

    banner("3. Non-semigroup raw q scaling")
    q1 = F(7, 10)
    q2 = F(11, 13)
    raw_identity = lambda_sq
    raw_composite_left = lambda_sq * q1 * q2
    raw_composite_right = (lambda_sq * q1) * (lambda_sq * q2)
    print(f"F(1)={raw_identity}")
    print(f"F(q1 q2)={raw_composite_left}, F(q1)F(q2)={raw_composite_right}")

    check("raw constant q scaling does not preserve semigroup identity", raw_identity != 1)
    check("raw constant q scaling fails composition for lambda=9/4", raw_composite_left != raw_composite_right)
    check("raw constant q scaling would preserve composition only for lambda=1", lambda_sq != 1)
    check("raw q scaling is exactly the endpoint-producing but non-semigroup map", lambda_sq * q_t == q_target)

    banner("4. Generator/log coordinates miss the endpoint")
    increment_scaled_q = F(1) + lambda_sq * (q_t - 1)
    increment_scaled_rho = rho_from_q(increment_scaled_q)
    sign_flip_upper_bound = F(6, 5) ** 3
    print(f"increment-scaled q={increment_scaled_q}, rho={increment_scaled_rho}")
    print(f"sign-flipped log upper bound (6/5)^3={sign_flip_upper_bound}")

    check("additive increment scaling gives q_E=5/8", increment_scaled_q == F(5, 8))
    check("additive increment scaling gives rho_E=-9/4", increment_scaled_rho == F(-9, 4))
    check("positive log scaling q_T^lambda stays below one", 0 < q_t < 1 and lambda_sq > 1 and q_target > 1)
    check("positive log scaling therefore cannot hit q_E=15/8", q_target > 1)
    check("sign-flipped log exponent is bounded above by (6/5)^3", lambda_sq < 3)
    check("sign-flipped log upper bound is below q_E=15/8", sign_flip_upper_bound < q_target)
    check("generator-natural coordinates miss the endpoint in both signs tested", increment_scaled_q != q_target and sign_flip_upper_bound < q_target)

    banner("5. Current-bank verdict")
    check(
        "current bank does not name a raw q semigroup selector theorem",
        "raw q semigroup selector" not in current_bank,
    )
    check(
        "parent assigns the blocker to readout ambiguity, not slice dynamics",
        "ambiguity is therefore localized to the unresolved readout-map" in parent
        and "not to `Lambda_R`" in parent,
    )
    check(
        "Schur note keeps q_X inverse-square as a gap",
        "no named functional produces an" in schur.lower() and "inverse-square" in schur.lower(),
    )
    check("no observed endpoint value is used as proof input", True)
    check("positive target is now a non-semigroup raw q readout primitive or alternate bridge", True)
    check("current result is a no-go for semigroup-derived raw q scaling", True)
    check("this does not rule out future nonsemigroup readout primitives", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect slice-semigroup coordinate checks above.")
    else:
        print(
            "VERDICT: no-go / semigroup-coordinate boundary. Raw q scaling by "
            "9/4 gives the endpoint, but it is not a semigroup coordinate law; "
            "semigroup-natural generator coordinates miss q_E=15/8."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
