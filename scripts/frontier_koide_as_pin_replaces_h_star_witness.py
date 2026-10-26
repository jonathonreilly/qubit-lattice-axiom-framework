#!/usr/bin/env python3
"""Supplied phase-target versus historical ratio-comparator calculation.
No AS/APS physical phase theorem, derived target or unique physical parameter is claimed.
"""

import math
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ("docs/KOIDE_SUPPLIED_PHASE_RATIO_COMPARATOR_NOTE_2026-10-24.md",)

PASSES: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = ""):
    PASSES.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}")
    if detail:
        for line in detail.split("\n"):
            print(f"       {line}")


def section(title: str):
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


# =============================================================================
# Explicit supplied Hermitian chart; this implementation is self-contained.
# =============================================================================
GAMMA = 0.5
E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
SELECTOR = math.sqrt(6.0) / 3.0

H_BASE = np.array(
    [
        [0, E1, -E1 - 1j * GAMMA],
        [E1, 0, -E2],
        [-E1 + 1j * GAMMA, -E2, 0],
    ],
    dtype=complex,
)
T_M = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
T_DELTA = np.array([[0, -1, 1], [-1, 1, 0], [1, 0, -1]], dtype=complex)
T_Q = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=complex)


def H_selected(m: float) -> np.ndarray:
    return H_BASE + m * T_M + SELECTOR * T_DELTA + SELECTOR * T_Q


def selected_line_slots(m: float) -> tuple[float, float, float]:
    X = expm(H_selected(m))
    v = float(np.real(X[2, 2]))
    w = float(np.real(X[1, 1]))
    rad = math.sqrt(3.0 * (v * v + 4.0 * v * w + w * w))
    u = 2.0 * (v + w) - rad
    return u, v, w


OMEGA = complex(math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3))


def b_std(u: float, v: float, w: float) -> complex:
    return (w + np.conj(OMEGA) * u + OMEGA * v) / 3.0


def brannen_phase(m: float) -> float:
    u, v, w = selected_line_slots(m)
    bs = b_std(u, v, w)
    return math.atan2(bs.imag, bs.real)


def wv_ratio(m: float) -> float:
    """Supplied diagonal ratio r(m)=w/v; historical comparator is separate."""
    _, v, w = selected_line_slots(m)
    return w / v


def main() -> int:
    section("Supplied phase target and historical ratio comparator")
    print("INFO: chart/readout/cone and radian target2/9 are supplied, not physical derivations.")
    # Historical calibration comparator, preserved exactly; not fitted again here.
    r_star_retained = 4.100904169382

    print(f"  Historical ratio comparator r_* = {r_star_retained}")
    # Supplied bracket; no monotonicity, exhaustive roots or uniqueness claim.
    f = lambda m: wv_ratio(m) - r_star_retained
    m_first = brentq(f, -1.3, -0.8, xtol=1e-12)
    r_at_m_first = wv_ratio(m_first)

    print(f"  Reconstructed m_first (solving r(m) = r_*):")
    print(f"    m_first = {m_first:.10f}")
    print(f"    r(m_first) = {r_at_m_first:.10f}  (target {r_star_retained})")

    record(
        "A.1 Historical ratio bracket candidate lies within the stated m window",
        -1.17 < m_first < -1.15,
        f"m_first = {m_first:.10f} (historical reference -1.16046947)",
    )

    section("Part B — supplied radian target")
    target_delta = 2.0 / 9.0

    print(f"  Supplied target delta = {target_delta}")
    g = lambda m: brannen_phase(m) - target_delta
    m_AS = brentq(g, -1.3, -0.8, xtol=1e-12)
    delta_at_m_AS = brannen_phase(m_AS)

    print(f"  Supplied-target bracket candidate m_AS (legacy variable name):")
    print(f"    m_AS = {m_AS:.10f}")
    print(f"    δ(m_AS) = {delta_at_m_AS:.10f}  (target {target_delta:.10f})")

    record(
        "B.1 Bracket candidate meets the supplied phase residual threshold",
        abs(delta_at_m_AS - target_delta) < 1e-10,
        f"m_AS = {m_AS:.10f} (supplied phase target; no physical derivation)",
    )

    # Part C — the two pins agree
    section("Part C — finite comparison of two supplied prescriptions")

    dev = abs(m_first - m_AS) / abs(m_first) * 100
    print(f"  m_first (historical ratio comparator):  {m_first:.10f}")
    print(f"  m_AS    (supplied phase target):    {m_AS:.10f}")
    print(f"  Deviation: {dev:.6f}%")
    print()
    print(f"  The checked comparison threshold below is0.01%; equality/uniqueness is not claimed.")
    print(f"  The phase target and historical ratio are distinct supplied inputs.")

    record(
        "C.1 The two detected m candidates differ by less than0.01%",
        dev < 0.01,
        f"|m_first - m_AS| / |m_first| = {dev:.4f}%\n"
        "This is a finite relative-deviation comparison.",
    )

    # Cross-check: at m_AS, what's r(m_AS)? Does it match r_*?
    r_at_m_AS = wv_ratio(m_AS)
    r_dev = abs(r_at_m_AS - r_star_retained) / r_star_retained * 100
    print(f"\n  Cross-check: at m_AS, the supplied diagonal ratio r(m_AS) = {r_at_m_AS:.10f}")
    print(f"  Historical r_* = {r_star_retained}")
    print(f"  Deviation: {r_dev:.6f}%")

    record(
        "C.2 At the phase-target candidate the ratio differs from the historical comparator by less than0.01%",
        r_dev < 0.01,
        f"r(m_AS) = {r_at_m_AS:.6f} vs r_* = {r_star_retained:.6f} ({r_dev:.4f}%)",
    )

    section("Part D — scope")
    print("INFO: four finite comparisons only. The historical AS-named path is retained for provenance.")
    print("INFO: target, phase convention, generation ordering and physical applicability remain supplied/open.")

    # Summary
    section("SUMMARY")
    n_pass = sum(1 for _, ok, _ in PASSES if ok)
    n_total = len(PASSES)
    print(f"PASSED: {n_pass}/{n_total}")
    for name, ok, _ in PASSES:
        status = "PASS" if ok else "FAIL"
        print(f"  [{status}] {name}")

    print()
    all_pass = n_pass == n_total
    print("Finite comparison checks completed; no physical or audit verdict is inferred.")

    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
