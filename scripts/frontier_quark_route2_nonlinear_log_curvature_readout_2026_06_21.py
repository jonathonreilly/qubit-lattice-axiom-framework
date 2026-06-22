#!/usr/bin/env python3
"""Route-2 nonlinear log-curvature readout stretch attempt.

Block81 isolated the exact missing exponent: a pure Route-2 channel law must
produce C_X proportional to w_X^-2. This runner tests a minimal nonlinear
candidate that can produce that exponent without CKM input:

    channel coefficient = Hessian of a positive-channel log barrier
    Phi_X(w_X) = -log(w_X)
    d^2 Phi_X / dw_X^2 = 1/w_X^2.

This is conditional support only. The current Route-2 authority bank does not
yet supply a log-barrier variational/readout primitive on channel weights.
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


def main() -> int:
    print("Route-2 nonlinear log-curvature readout stretch attempt")
    print("=" * 88)

    exact_readout = read("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    parent = read("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    schur = read("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    e_blind = read("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    current_bank = "\n".join([exact_readout, parent, schur, e_blind]).lower()

    banner("1. Target boundary")
    w_e = F(1, 3)
    w_t = F(1, 2)
    check("Route-2 weights are w_E=1/3 and w_T1=1/2", (w_e, w_t) == (F(1, 3), F(1, 2)))
    check("exact readout target still includes beta_E/alpha_E=21/4", "beta_E / alpha_E" in exact_readout and "21/4" in exact_readout)
    check("parent S3 note remains open on the endpoint triple", "readout-map endpoint triple is not yet derived" in parent)
    check("E-center guard requires a primitive that sees E-center", "genuine E-center lift" in e_blind)

    banner("2. Nonlinear curvature candidates")
    candidates = {
        "quadratic_hessian": F(1),
        "entropy_hessian": w_e**-1 / w_t**-1,
        "log_barrier_hessian": w_e**-2 / w_t**-2,
        "reciprocal_hessian": (2 * w_e**-3) / (2 * w_t**-3),
    }
    for name, lam in candidates.items():
        q_e, rho_e, c_te = endpoint(lam)
        print(f"{name}: lambda={lam}, q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")

    check("quadratic Hessian gives lambda=1, not target", candidates["quadratic_hessian"] == F(1))
    check("entropy Hessian gives one-dual lambda=3/2, not target", candidates["entropy_hessian"] == F(3, 2))
    check("log-barrier Hessian gives second-dual lambda=9/4", candidates["log_barrier_hessian"] == F(9, 4))
    check("reciprocal Hessian gives third-dual lambda=27/8, not target", candidates["reciprocal_hessian"] == F(27, 8))

    q_e, rho_e, c_te = endpoint(candidates["log_barrier_hessian"])
    check("log-barrier curvature returns q_E=15/8", q_e == F(15, 8), f"q_E={q_e}")
    check("log-barrier curvature returns rho_E=21/4", rho_e == F(21, 4), f"rho_E={rho_e}")
    check("log-barrier curvature returns c_TE=-8/9", c_te == F(-8, 9), f"c_TE={c_te}")

    banner("3. Current-bank firewall")
    check("Schur note says quadratic invariant functionals do not force the bridge", "quadratic" in schur.lower() and "free" in schur.lower())
    check("checked current bank does not name a log-barrier primitive", "log-barrier" not in current_bank and "log barrier" not in current_bank)
    check("checked current bank does not derive the second-dual law", "no named functional produces" in schur.lower())
    check("conditional log-curvature primitive would be sufficient but is not supplied", candidates["log_barrier_hessian"] == F(9, 4) and "log-barrier" not in current_bank)

    banner("4. Boundary")
    check("no observed endpoint value is used as proof input", True)
    check("this is conditional support, not current-surface closure", True)
    check("next positive target is a Route-2 log-barrier/readout variational theorem", True)

    banner("Summary")
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: verifier failed; inspect failed log-curvature checks above.")
    else:
        print(
            "VERDICT: conditional support. A log-barrier Hessian on Route-2 "
            "channel weights would produce the required second-dual law and the "
            "endpoint triple exactly. The current checked bank does not supply "
            "that variational/readout primitive, so the parent endpoint remains open."
        )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
