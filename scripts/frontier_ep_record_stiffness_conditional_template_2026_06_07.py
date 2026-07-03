#!/usr/bin/env python3
"""Conditional EP/record-stiffness salvage runner.

The runner checks only algebra inside a supplied continuous energy/action
context. It does not derive that context from the Record axiom.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


RESULTS: list[tuple[str, bool, str]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((label, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    print("EP record-stiffness conditional shared-coupling template")
    print("=" * 72)

    phi, phi0, eps, m, sigma = sp.symbols("phi phi0 epsilon m sigma", positive=True)
    p1, p2, p3, a = sp.symbols("p1 p2 p3 a", positive=True)

    potential = sp.Rational(1, 2) * m**2 * (phi - phi0) ** 2
    stiffness = sp.diff(potential, phi, 2).subs(phi, phi0)
    cost = sp.simplify(potential.subs(phi, phi0 + eps) - potential.subs(phi, phi0))
    check(
        "supplied local energy curvature gives stiffness V''(phi0)=m^2",
        sp.simplify(stiffness - m**2) == 0 and sigma not in stiffness.free_symbols,
        f"displacement cost={cost}",
    )

    packet_dispersion_response = 1 / (m * sigma)
    check(
        "failed packet-dispersion route is width-dependent",
        sigma in packet_dispersion_response.free_symbols,
        f"response={packet_dispersion_response}",
    )

    e2_lattice = m**2 + (2 / a**2) * (
        (1 - sp.cos(p1 * a)) + (1 - sp.cos(p2 * a)) + (1 - sp.cos(p3 * a))
    )
    gap = sp.simplify(e2_lattice.subs({p1: 0, p2: 0, p3: 0}))
    small_p = sp.series(e2_lattice.subs({p2: 0, p3: 0}), p1, 0, 4).removeO()
    check(
        "lattice rest gap is the supplied stiffness exactly",
        sp.simplify(gap - m**2) == 0,
        f"E2(p=0)={gap}; small-p={small_p}",
    )

    x, width = sp.symbols("x width", positive=True)
    psi2 = sp.exp(-x**2 / width**2) / (width * sp.sqrt(sp.pi))
    norm = sp.simplify(sp.integrate(psi2, (x, -sp.oo, sp.oo)))
    recorded_energy = sp.simplify(sp.integrate(m * psi2, (x, -sp.oo, sp.oo)))
    check(
        "recorded-energy source integral gives the same m and no packet-width dependence",
        norm == 1 and recorded_energy == m and width not in recorded_energy.free_symbols,
        f"integral |psi|^2={norm}; integral m|psi|^2={recorded_energy}",
    )

    inertial_mass = m
    gravitational_mass = recorded_energy
    ratio = sp.simplify(gravitational_mass / inertial_mass)
    check(
        "conditional shared-coupling template gives ratio one",
        ratio == 1 and sigma not in ratio.free_symbols and width not in ratio.free_symbols,
        f"m_grav/m_inert={ratio}",
    )

    note = Path(__file__).resolve().parent.parent / "docs" / (
        "EP_RECORD_STIFFNESS_CONDITIONAL_SHARED_COUPLING_TEMPLATE_NOTE_2026-06-07.md"
    )
    text = note.read_text()
    required = [
        "**Claim type:** open_gate",
        "2026-06-12 audit firewall: continuous-energy context supplied",
        "supplied",
        "conditional",
        "not a WEP closure",
        "does not derive",
        "packet-width",
        "No new\naxiom, Tier-A admission, WEP closure, or audit-status change",
        "2026-06-16 weak-field source/readout interface split",
        "EP-S3a",
        "EP-S3b",
    ]
    check(
        "source note keeps the open-gate conditional boundary",
        all(token in text for token in required),
        "no Record-alone mass derivation is asserted",
    )

    passed = sum(1 for _, ok, _ in RESULTS if ok)
    failed = len(RESULTS) - passed
    print("=" * 72)
    print(f"TOTAL: {passed} PASS / {failed} FAIL")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
