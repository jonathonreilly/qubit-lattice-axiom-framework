#!/usr/bin/env python3
"""Native SU(2) one-plaquette beta=16 u0 interval certificate.

This runner computes the SU(2) one-plaquette Wilson class-angle integral
directly and cross-checks it against the Bessel closed form. It supplies a
source-side bounded-support bridge for the g_2(v) interval row's former
row-local literature u0 interval import.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import mpmath as mp
except ImportError:
    print("FAIL: mpmath required for high-precision quadrature")
    sys.exit(1)


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "SU2_U0_SINGLE_PLAQUETTE_BETA16_NATIVE_INTERVAL_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = (
    ROOT / "docs" / "G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM_NOTE_2026-05-17.md"
)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def su2_partition(beta: mp.mpf) -> mp.mpf:
    return mp.quad(lambda th: mp.sin(th) ** 2 * mp.e ** (beta * mp.cos(th)), [0, mp.pi])


def su2_plaquette_integral(beta: mp.mpf) -> mp.mpf:
    numerator = mp.quad(
        lambda th: mp.cos(th) * mp.sin(th) ** 2 * mp.e ** (beta * mp.cos(th)),
        [0, mp.pi],
    )
    return numerator / su2_partition(beta)


def main() -> int:
    mp.mp.dps = 80
    beta = mp.mpf(16)
    p_quad = su2_plaquette_integral(beta)
    p_bessel = mp.besseli(2, beta) / mp.besseli(1, beta)
    u0 = p_bessel ** mp.mpf("0.25")

    print("SU(2) beta=16 one-plaquette u0 native interval certificate")
    print(f"P_SU2(beta=16) = {mp.nstr(p_bessel, 60)}")
    print(f"u0_SU2(beta=16) = {mp.nstr(u0, 60)}")

    check("partition function is positive", su2_partition(beta) > 0)
    check("quadrature expectation lies in (-1, 1)", -1 < p_quad < 1)
    check(
        "Bessel ratio matches independent quadrature",
        abs(p_quad - p_bessel) < mp.mpf("1e-50"),
        detail=f"abs diff={mp.nstr(abs(p_quad - p_bessel), 6)}",
    )
    check("P_SU2(beta=16) lies in [0.9078, 0.9079]", mp.mpf("0.9078") < p_bessel < mp.mpf("0.9079"))
    check("u0_SU2(beta=16) lies in [0.9761, 0.9762]", mp.mpf("0.9761") < u0 < mp.mpf("0.9762"))
    check("u0_SU2(beta=16) lies in parent interval [0.96, 0.98]", mp.mpf("0.96") < u0 < mp.mpf("0.98"))
    check(
        "native tight interval is subset of parent interval",
        mp.mpf("0.96") < mp.mpf("0.9761") < u0 < mp.mpf("0.9762") < mp.mpf("0.98"),
    )

    note_text = NOTE_PATH.read_text(encoding="utf-8")
    parent_text = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    required_status_fields = [
        "**Claim type:** bounded_theorem",
        "**Type:** bounded_theorem",
        "bounded support for the native SU(2) beta=16 one-plaquette",
        "actual_current_surface_status: bounded-support",
        "trace_class: direct_blocker_closure",
        "reachability_to_target: closes",
        "proposal_allowed: false",
        "bare_retained_allowed: false",
        "[`SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md`](SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28.md)",
    ]
    check(
        "new note carries required status firewall fields",
        all(field in note_text for field in required_status_fields),
    )
    forbidden_loads = [
        "observed g_2(v)",
        "fitted selector",
        "literature numerical interval load-bearing",
    ]
    check(
        "new note excludes observed g2, fitted selector, and literature numerical interval load-bearing roles",
        all(phrase in note_text for phrase in forbidden_loads),
    )
    parent_required = [
        "SU2_U0_SINGLE_PLAQUETTE_BETA16_NATIVE_INTERVAL_BOUNDED_SUPPORT_NOTE_2026-06-18.md",
        "X1 is now supplied by the 2026-06-18 native SU(2) beta=16 single-plaquette bridge",
        "not a row-local literature admission",
    ]
    check(
        "parent note routes X1 through the native bridge",
        all(phrase in parent_text for phrase in parent_required),
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
