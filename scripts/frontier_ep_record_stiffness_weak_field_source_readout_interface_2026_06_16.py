#!/usr/bin/env python3
"""EP record-stiffness weak-field source/readout interface checker.

This runner checks a narrow post-audit repair for the EP record-stiffness
conditional template:

* the normalized |psi|^2 source-readout and weak-field source coupling are
  supported by the retained-bounded weak-field source-response bridge;
* the same coefficient m appearing in the inertial gap and gravitational
  source remains a supplied shared-coupling template input.

It does not derive the continuous scalar action from Record and does not close
the equivalence principle.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "EP_RECORD_STIFFNESS_WEAK_FIELD_SOURCE_READOUT_INTERFACE_NOTE_2026-06-16.md"
PARENT = ROOT / "docs" / "EP_RECORD_STIFFNESS_CONDITIONAL_SHARED_COUPLING_TEMPLATE_NOTE_2026-06-07.md"
WEAK_FIELD = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def main() -> int:
    print("EP RECORD-STIFFNESS WEAK-FIELD SOURCE/READOUT INTERFACE")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    weak = WEAK_FIELD.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    parent_flat = " ".join(parent.split())

    check(
        "interface note is bounded-support and not WEP closure",
        "**Claim type:** bounded_theorem" in note
        and "bounded-support interface theorem" in note
        and "does not close the equivalence principle" in note_flat,
    )
    check(
        "parent note references the weak-field source/readout split",
        "2026-06-16 weak-field source/readout interface split" in parent
        and "EP-S3a" in parent
        and "EP-S3b" in parent,
    )
    check(
        "note leaves continuous action and rest-gap context open",
        "does not derive the continuous local energy/action functional" in note_flat
        and "does not derive the inertial rest-gap readout from Record" in note_flat,
    )
    check(
        "note forbids audit-status and axiom promotion",
        "adds no new axiom" in note_flat
        and "does not edit any audit verdict" in note_flat
        and "not a WEP closure" in note_flat,
    )

    check(
        "weak-field dependency contains Born-density source readout",
        "rho_psi(x) = |psi(x)|^2" in weak
        and "unique local" in weak
        and "phase-invariant" in weak
        and "normalized" in weak,
    )
    check(
        "weak-field dependency contains same-source test coupling",
        "S_test(phi; x) = L_test (1 - phi(x))" in weak
        and "U_test(phi; x) = -m phi(x)" in weak,
    )

    x, width, m, lam = sp.symbols("x width m lambda", positive=True)
    psi2 = sp.exp(-x**2 / width**2) / (width * sp.sqrt(sp.pi))
    norm = sp.simplify(sp.integrate(psi2, (x, -sp.oo, sp.oo)))
    energy_source = sp.simplify(sp.integrate(m * psi2, (x, -sp.oo, sp.oo)))
    check(
        "normalized source-readout integral is one",
        norm == 1,
        f"integral |psi|^2={norm}",
    )
    check(
        "recorded-energy source integral gives coefficient m without width dependence",
        energy_source == m and width not in energy_source.free_symbols,
        f"integral m|psi|^2={energy_source}",
    )

    p1, p2, p3, a = sp.symbols("p1 p2 p3 a", positive=True)
    e2_lattice = m**2 + (2 / a**2) * (
        (1 - sp.cos(p1 * a)) + (1 - sp.cos(p2 * a)) + (1 - sp.cos(p3 * a))
    )
    gap_squared = sp.simplify(e2_lattice.subs({p1: 0, p2: 0, p3: 0}))
    check(
        "supplied scalar dispersion has p=0 gap squared m^2",
        sp.simplify(gap_squared - m**2) == 0,
        f"E2(0)={gap_squared}",
    )

    inertial_coefficient = m
    grav_source_coefficient = energy_source
    ratio = sp.simplify(grav_source_coefficient / inertial_coefficient)
    check(
        "template ratio is one only when the shared coefficient is identified",
        ratio == 1,
        f"m_grav/m_inert={ratio}",
    )

    rescaled_source = sp.simplify(sp.integrate(lam * m * psi2, (x, -sp.oo, sp.oo)))
    rescaled_ratio = sp.simplify(rescaled_source / inertial_coefficient)
    check(
        "shared source coefficient remains a real residual",
        rescaled_ratio == lam and sp.simplify(rescaled_ratio - 1) != 0,
        f"lambda-scaled ratio={rescaled_ratio}",
    )

    check(
        "parent remains an open-gate conditional template after split",
        "open-gate conditional template" in parent_flat
        and "does not derive `V`, `m`, the mass scale" in parent,
    )

    print("=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: partial source/readout support only. The weak-field bridge "
        "supports |psi|^2 as source readout and the same-source coupling form, "
        "while the continuous action, inertial rest-gap interpretation, and "
        "shared coefficient identity remain open."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
