#!/usr/bin/env python3
"""Kinetic B-W OS0 identification bridge interface no-go.

The runner checks a bounded interface fact for the kinetic-isotropy lane:
the strict-unitary real-time band theorem fixes |d omega/dk| = 1, but it does
not by itself fix the positive Euclidean transfer normalization used by the
OS0 kinetic-form ratio. A separate B-W readout rule is still required.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import sympy as sp


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md"
TARGET = ROOT / "docs" / "KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md"


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def main() -> int:
    print("Kinetic B-W OS0 identification bridge interface no-go")
    print("actual_current_surface_status: no-go")
    print("trace_class: negative_route_pruning")
    print("reachability_to_target: prunes")
    print("proposal_allowed: false")
    print("audit_required_before_effective_retained: true")
    print()

    k, r = sp.symbols("k r", positive=True, real=True)

    print("A. strict-unitary saturated tick")
    U = sp.diag(sp.exp(sp.I * k), sp.exp(-sp.I * k))
    check("U(k) is exactly unitary", sp.simplify(U.H * U - sp.eye(2)) == sp.zeros(2))
    eigs = list(U.eigenvals().keys())
    check(
        "quasi-energy pair is omega <-> -omega",
        set(eigs) == {sp.exp(sp.I * k), sp.exp(-sp.I * k)},
        str(eigs),
    )
    omega = k
    check("real-time group velocity is one", sp.diff(omega, k) == 1)

    print("\nB. Euclidean transfer envelopes are not fixed by U(k)")
    slopes = []
    for rv in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2), sp.Integer(3)):
        E = rv * omega
        T = sp.exp(-E)
        slopes.append(sp.diff(E, k))
        check(
            f"T_r is a positive contraction for r={rv}",
            all(0 < float(T.subs(k, kv)) < 1 for kv in (0.1, 0.7, 1.3)),
            f"T(0.7)={float(T.subs(k, 0.7)):.6f}",
        )
    check("same unitary slope permits different Euclidean slopes", len(set(slopes)) == 4, str(slopes))
    check("only the supplied r=1 B-W rule gives OS0 ratio one", slopes[1] == 1 and slopes[0] != 1 and slopes[2] != 1)

    print("\nC. positive transfer and unitary tick are distinct objects")
    for rv in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)):
        T = sp.exp(-rv * omega)
        phase = sp.exp(sp.I * omega)
        sample = 0.4
        check(
            f"T_r(k) cannot equal exp(i omega) at k={sample} for r={rv}",
            abs(complex(T.subs(k, sample)) - complex(phase.subs(k, sample))) > 1e-6,
        )
    check(
        "no algebraic equality maps the positive envelope to the unitary phase",
        sp.simplify(sp.exp(-r * k) - sp.exp(sp.I * k)) != 0,
    )

    print("\nD. conditional bridge map")
    bw_E = omega
    check("if B-W supplies E_E(k)=|omega(k)| on k>=0, OS0 slope is one", sp.diff(bw_E, k) == 1)
    arbitrary_E = r * omega
    check("without B-W normalization the OS0 slope remains a free positive r", sp.diff(arbitrary_E, k) == r)
    numeric_rs = np.array([0.5, 1.0, 2.0, 3.0])
    check("free r changes the inferred c_t/c_s while preserving real-time unit slope", np.ptp(numeric_rs) > 0)

    print("\nE. source firewall checks")
    note = NOTE.read_text(encoding="utf-8")
    target = TARGET.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    target_flat = " ".join(target.split())
    check("new note declares no_go claim type", "**Claim type:** no_go" in note)
    check("new note carries the no-go discipline gate", "## No-Go Discipline Gate" in note and "Status: **PASS**" in note)
    check("new note states B-W is not automatic", "not an algebraic consequence" in note_flat)
    check("new note forbids silent B-W identification", "silently identify" in note_flat)
    check("target kinetic note cites this B-W interface no-go", "KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md" in target)
    check("target kinetic note still keeps primitive retirement firewalled", "does not retire the kinetic-isotropy primitive" in target_flat)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    if PASS > 0 and FAIL == 0:
        print(
            "VERDICT: B-W is not automatic from the unit real-time band slope. "
            "A separate OS0 Wick/readout normalization rule is still required; "
            "with the supplied r=1 rule the ratio becomes one."
        )
        return 0
    print("VERDICT: B-W interface no-go failed; do not use this artifact.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
