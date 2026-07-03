#!/usr/bin/env python3
"""Finite quadratic-mode gluing derivation for the universal-GR sign lane.

This runner derives the normal-mode relation used by the degenerate
supermetric sign diagnostic from a finite-dimensional quadratic channel:

    L = (1/2) G qdot^2 - (1/2) V q^2
    Euler-Lagrange: G qddot + V q = 0
    q(t) = exp(i omega t) -> omega^2 = V / G

The result is only the finite quadratic-mode gluing law. It does not derive
the Regge/Lichnerowicz comparator signs, the Einstein-Hilbert action, or a
physical Newton constant.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [PASS] {name}")
    else:
        FAIL_COUNT += 1
        print(f"  [FAIL] {name}")
    if detail:
        print(f"         {detail}")


def mode_frequency_squared(kinetic_coefficient, curvature_coefficient):
    """Return omega^2 for a diagonal finite quadratic mode.

    The input convention is L = 1/2 G qdot^2 - 1/2 V q^2, so
    omega^2 = V/G when G is nonzero.
    """
    if kinetic_coefficient == 0:
        raise ZeroDivisionError("quadratic mode gluing requires nonzero G")
    return curvature_coefficient / kinetic_coefficient


def gluing_product_sign(
    g_trace,
    g_tt,
    v_trace,
    v_tt,
) -> int:
    """Sign of omega_trace^2 * omega_TT^2 for diagonal channels."""
    product = mode_frequency_squared(g_trace, v_trace) * mode_frequency_squared(g_tt, v_tt)
    return 1 if product > 0 else -1 if product < 0 else 0


def main() -> int:
    print("=" * 88)
    print("UNIVERSAL GR QUADRATIC MODE GLUING DERIVATION")
    print("=" * 88)

    t, omega = sp.symbols("t omega")
    G, V = sp.symbols("G V", nonzero=True)
    q = sp.exp(sp.I * omega * t)
    euler_lagrange_on_mode = sp.simplify(G * sp.diff(q, t, 2) + V * q)
    dispersion_polynomial = sp.simplify(euler_lagrange_on_mode / q)
    check(
        "Euler-Lagrange equation gives V - G*omega^2 on a normal mode",
        dispersion_polynomial == V - G * omega**2,
        f"dispersion={dispersion_polynomial}",
    )
    check(
        "normal-mode root is omega^2 = V/G",
        sp.simplify((V / G) - omega**2).subs(omega**2, V / G) == 0,
        "L = 1/2 G qdot^2 - 1/2 V q^2, G != 0",
    )

    exact_channels = [
        (Fraction(3, 2), Fraction(7, 4), Fraction(7, 6)),
        (Fraction(5, 3), Fraction(-11, 6), Fraction(-11, 10)),
    ]
    exact_ok = all(mode_frequency_squared(g, v) == expected for g, v, expected in exact_channels)
    check(
        "finite diagonal channel gluing is exact over rational coefficients",
        exact_ok,
        ", ".join(
            f"G={g}, V={v}, omega2={mode_frequency_squared(g, v)}"
            for g, v, _ in exact_channels
        ),
    )

    g0 = Fraction(-7, 5)
    v_trace = Fraction(-1, 2)
    v_tt = Fraction(1, 2)
    product_signs = []
    for eps in (Fraction(1), Fraction(-1)):
        product_signs.append(gluing_product_sign(eps * g0, eps * g0, v_trace, v_tt))
    check(
        "degenerate equal-channel G makes the sign product depend only on V_trace*V_TT",
        product_signs == [-1, -1],
        f"overall-sign product signs={product_signs}",
    )

    b2 = Fraction(49, 100)
    k2 = Fraction(1, 1)
    gr_trace = Fraction(-2, 1) / b2
    gr_tt = Fraction(1, 1) / b2
    wt = mode_frequency_squared(gr_trace, -k2 / 2)
    ws = mode_frequency_squared(gr_tt, k2 / 2)
    check(
        "GR lambda=1 control has both quadratic-mode signs positive for the comparator pair",
        wt > 0 and ws > 0,
        f"omega_trace^2={wt}, omega_TT^2={ws}",
    )

    note_path = Path(
        "docs/UNIVERSAL_GR_QUADRATIC_MODE_GLUING_DERIVATION_NARROW_THEOREM_NOTE_2026-06-09.md"
    )
    note_text = note_path.read_text(encoding="utf-8")
    check(
        "source note keeps comparator signs and physical GR action outside scope",
        "does not derive the Regge/Lichnerowicz comparator signs" in note_text
        and "does not identify the full Einstein-Hilbert action" in note_text,
    )
    check(
        "source note states no new axiom or Tier-A admission",
        "no new axiom" in note_text and "no Tier-A admission" in note_text,
    )

    print()
    print("BOUNDARY")
    print("  Derived: finite quadratic-mode gluing law omega^2 = V/G for diagonal channels.")
    print("  Still open: comparator signs, full geometric action, continuum coefficient, G_Newton.")
    print()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
