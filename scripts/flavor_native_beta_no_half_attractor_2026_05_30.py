#!/usr/bin/env python3
"""Supplied tanh^4 transit check for the flavor native-beta provenance note.

This runner does not derive a framework-native beta function and does not
exclude generic-r fixed points for all C3-symmetric flows. It checks only the
algebraic facts for the supplied path

    r(t) = tanh(t)^4.

The repaired source note uses this runner as a bounded diagnostic: r=1/2 is a
transit value, not a fixed point, for this path.
"""

from __future__ import annotations

import math

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def r_of_t(t: float) -> float:
    return math.tanh(t) ** 4


def beta_of_t(t: float) -> float:
    th = math.tanh(t)
    return 4.0 * th**3 * (1.0 - th**2)


def main() -> int:
    print("=" * 76)
    print("Flavor supplied tanh^4 flow transit check")
    print("=" * 76)
    print("Claim boundary: supplied r(t)=tanh^4(t) path only; no native-beta exhaustion.")
    print()

    t_star = math.atanh(2.0 ** (-0.25))
    beta_star_closed = 4.0 * 2.0 ** (-0.75) * (1.0 - 2.0 ** (-0.5))

    check("r(0) = 0", abs(r_of_t(0.0)) < 1e-14, detail=f"r(0)={r_of_t(0.0):.12f}")
    check("r(t) approaches 1 at large t", abs(r_of_t(20.0) - 1.0) < 1e-12, detail=f"r(20)={r_of_t(20.0):.12f}")
    check("beta_r(t)>0 at sample finite t=0.5", beta_of_t(0.5) > 0, detail=f"beta={beta_of_t(0.5):.12f}")
    check("beta_r(t)>0 at sample finite t=2.5", beta_of_t(2.5) > 0, detail=f"beta={beta_of_t(2.5):.12f}")
    check("t_star solves r(t_star)=1/2", abs(r_of_t(t_star) - 0.5) < 1e-14, detail=f"t_star={t_star:.12f}")
    check(
        "beta_r(t_star)>0, so r=1/2 is transit not fixed",
        beta_of_t(t_star) > 0 and abs(beta_of_t(t_star) - beta_star_closed) < 1e-14,
        detail=f"beta_star={beta_of_t(t_star):.12f}",
    )

    print()
    print("=" * 76)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 76)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
