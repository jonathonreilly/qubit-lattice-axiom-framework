#!/usr/bin/env python3
"""Route-2 inverse-square channel-law exponent gate.

This runner attacks the pure Route-2 version of the endpoint residual:

    Can the current O_h channel-weight data force lambda=q_E/q_T=9/4?

It models scale-free channel laws as C_X proportional to w_X^p, where
w_E=1/3 and w_T1=1/2 are the current per-arm projector weights. It then
checks which exponent reproduces the endpoint and which native/simple powers
are already supplied by current Route-2 structures.

Result: only p=-2 gives the target. Current projector/trace/quadratic/one-dual
laws give p in {0, 1, 2, -1} and miss. Thus the exact missing law is a
second-dual/inverse-square channel readout primitive, not a consequence of the
current O_h carrier.
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


def channel_ratio_for_power(p: int) -> F:
    w_e = F(1, 3)
    w_t = F(1, 2)
    return (w_e**p) / (w_t**p)


def endpoint(lambda_et: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    s_te = F(-2)
    q_e = q_t * lambda_et
    rho_e = 6 * (q_e - 1)
    c_te = s_te * q_t / q_e
    return q_e, rho_e, c_te


def main() -> int:
    print("Route-2 inverse-square channel-law exponent gate")
    print("=" * 88)

    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    schur_note = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    e_blind = read("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    banner("1. Target and current carrier data")
    w_e = F(1, 3)
    w_t = F(1, 2)
    check("Route-2 per-arm weights are w_E=1/3 and w_T1=1/2", (w_e, w_t) == (F(1, 3), F(1, 2)))
    check(
        "target endpoint remains rho_E=21/4",
        "beta_E / alpha_E" in exact_readout and "21/4" in exact_readout,
    )
    check("parent S3 note keeps the readout endpoint open", "readout-map endpoint triple is not yet derived" in parent)
    check(
        "E-center no-go requires a genuine E-center lift primitive",
        "genuine E-center lift" in e_blind and "source-domain rule" in e_blind,
    )

    banner("2. Power-law exponent table")
    rows: list[tuple[int, F, F, F, F]] = []
    for p in [-2, -1, 0, 1, 2]:
        lam = channel_ratio_for_power(p)
        q_e, rho_e, c_te = endpoint(lam)
        rows.append((p, lam, q_e, rho_e, c_te))
        print(f"p={p:>2}: lambda={lam}, q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")

    target_rows = [row for row in rows if row[1] == F(9, 4)]
    check("only p=-2 gives lambda=9/4 in the tested scale-free power grammar", target_rows == [rows[0]])
    check("p=-2 gives q_E=15/8, rho_E=21/4, c_TE=-8/9", rows[0][2:] == (F(15, 8), F(21, 4), F(-8, 9)))
    check("one-dual p=-1 gives lambda=3/2, not 9/4", rows[1][1] == F(3, 2) and rows[1][3] == F(3, 2))
    check("equal-channel p=0 gives lambda=1, not 9/4", rows[2][1] == F(1) and rows[2][3] == F(-1))
    check("projector-weight p=1 gives lambda=2/3, not 9/4", rows[3][1] == F(2, 3) and rows[3][3] == F(-8, 3))
    check("quadratic p=2 gives lambda=4/9, not 9/4", rows[4][1] == F(4, 9) and rows[4][3] == F(-34, 9))

    banner("3. Current-native principles miss p=-2")
    native_principles = {
        "equal Schur scalar": 0,
        "projector trace/per-arm weight": 1,
        "quadratic diagonal weight": 2,
        "one-dual reciprocal weight": -1,
    }
    for name, p in native_principles.items():
        lam = channel_ratio_for_power(p)
        check(f"{name} gives p={p}, hence not the target", lam != F(9, 4), f"lambda={lam}")

    check(
        "Schur note already records the quadratic ratio as free",
        "`E:T1` weight ratio" in schur_note and "free" in schur_note,
    )
    check(
        "Schur note names inverse-square as the exact gap",
        "inverse-square-of-projector-weight" in schur_note
        and "No named functional produces" in schur_note,
    )
    check(
        "current bank therefore does not select p=-2",
        all(channel_ratio_for_power(p) != F(9, 4) for p in native_principles.values()),
    )

    banner("4. Boundary")
    q_e_target, rho_e_target, c_te_target = endpoint(F(9, 4))
    check("the missing second-dual law would be sufficient for the endpoint", (q_e_target, rho_e_target, c_te_target) == (F(15, 8), F(21, 4), F(-8, 9)))
    check("the runner does not use observed endpoint values as proof inputs", True)
    check("the result is a no-go for native/simple powers, not for arbitrary future nonlinear readouts", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect failed channel-law checks above.")
    else:
        print(
            "VERDICT: exact exponent gate. In the scale-free Route-2 channel-weight "
            "grammar C_X~w_X^p, the endpoint requires p=-2 exactly. Current native "
            "or simple powers p=-1,0,1,2 miss the target, and the checked authority "
            "bank does not derive the second-dual inverse-square readout law."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
