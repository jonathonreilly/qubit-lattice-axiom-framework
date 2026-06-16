#!/usr/bin/env python3
"""Gate B weak-field source/action interface checker.

This runner checks a narrow post-audit repair:

* the linear test-action form used by the Gate B source packet,
  S = L(1 - phi), has a retained-bounded weak-field interface;
* the Gate B runner's regularized scalar phi = strength/(r + epsilon),
  normalization, propagation/readout semantics, and generated connectivity
  remain supplied ingredients.

It does not promote Gate B dynamics or physical gravity closure.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md"
PARENT = ROOT / "docs" / "GATE_B_DYNAMICS_NOTE.md"
WEAK_FIELD = ROOT / "docs" / "GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md"
VALLEY_SYNTHESIS = ROOT / "docs" / "VALLEY_LINEAR_CONTINUUM_SYNTHESIS_NOTE.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> bool:
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
    return ok


def gate_b_phi(strength: float, r: float, epsilon: float) -> float:
    return strength / (r + epsilon)


def gate_b_action(length: float, strength: float, r: float, epsilon: float) -> float:
    return length * (1.0 - gate_b_phi(strength, r, epsilon))


def main() -> int:
    print("GATE B WEAK-FIELD SOURCE/ACTION INTERFACE")
    print("=" * 78)

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    weak = WEAK_FIELD.read_text(encoding="utf-8")
    valley = VALLEY_SYNTHESIS.read_text(encoding="utf-8")

    note_flat = " ".join(note.split())
    parent_flat = " ".join(parent.split())
    parent_flat_lower = parent_flat.lower()

    check(
        "interface note is bounded-support and not Gate B closure",
        "**Claim type:** bounded_theorem" in note
        and "bounded-support interface theorem" in note
        and "does not close Gate B" in note_flat,
    )
    check(
        "parent Gate B note references the weak-field interface split",
        "2026-06-16 weak-field source/action interface split" in parent
        and "GB-S1a" in parent
        and "GB-S1b" in parent,
    )
    check(
        "note keeps GB-S2 and GB-S3 open",
        "does not discharge `GB-S2`" in note
        and "does not discharge `GB-S3`" in note
        and "generated connectivity" in note_flat,
    )
    check(
        "note forbids audit-status and axiom promotion",
        "adds no new axiom" in note_flat
        and "does not edit any audit verdict" in note_flat
        and "not a retained physical-gravity theorem" in note_flat,
    )

    check(
        "weak-field dependency contains S_test = L_test (1 - phi(x))",
        "S_test(phi; x) = L_test (1 - phi(x))" in weak,
    )
    check(
        "weak-field dependency contains Born-density source readout",
        "rho_psi(x) = |psi(x)|^2" in weak
        and "unique local" in weak
        and "phase-invariant" in weak
        and "normalized" in weak,
    )
    check(
        "valley synthesis derives the straight-ray 1/b continuum bridge for S=L(1-f)",
        "S = L(1-f)" in valley
        and "d(delta Phi)/db -> 2 k s / b" in valley,
    )

    for length in (0.5, 1.0, math.sqrt(5.0)):
        for r in (3.0, 4.0, 7.5):
            strength = 5.0e-5
            epsilon = 0.1
            phi = gate_b_phi(strength, r, epsilon)
            lhs = gate_b_action(length, strength, r, epsilon)
            rhs = length * (1.0 - phi)
            check(
                f"S=L(1-phi) identity length={length:.6g} r={r:.1f}",
                abs(lhs - rhs) < 1.0e-15,
                f"diff={abs(lhs-rhs):.3e}",
            )

    for r in (3.0, 5.0, 10.0):
        length = 1.25
        eps = 0.1
        s1 = 1.0e-5
        s2 = 4.0e-5
        delta_1 = gate_b_action(length, s1, r, eps) - length
        delta_2 = gate_b_action(length, s2, r, eps) - length
        delta_12 = gate_b_action(length, s1 + s2, r, eps) - length
        check(
            f"source perturbation is additive at r={r:.1f}",
            abs(delta_12 - (delta_1 + delta_2)) < 1.0e-15,
            f"residual={delta_12 - (delta_1 + delta_2):+.3e}",
        )

    r = 4.0
    eps = 0.1
    length = math.sqrt(2.0)
    base = length * (1.0 - 1.0 * gate_b_phi(5.0e-5, r, eps))
    rescaled = length * (1.0 - 2.0 * gate_b_phi(2.5e-5, r, eps))
    check(
        "source/action coefficient normalization remains degenerate",
        abs(base - rescaled) < 1.0e-15,
        f"base={base:.15e} rescaled={rescaled:.15e}",
    )

    for r in (3.0, 4.0, 5.0, 10.0):
        eps = 0.1
        regularized = 1.0 / (r + eps)
        continuum_shape = 1.0 / r
        rel = abs(regularized - continuum_shape) / continuum_shape
        check(
            f"regularized 1/(r+eps) is far-field close but not identical at r={r:.1f}",
            rel > 0.0 and rel <= eps / (r + eps) + 1.0e-15,
            f"relative_gap={rel:.6f}",
        )

    check(
        "parent still states I_GateB remains conditional after split",
        "parent gate b row remains an open gate" in parent_flat_lower
        and "does not derive a Gate B dynamics theorem" in parent_flat,
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: partial GB-S1 support only. The weak-field interface supports "
        "the linear test-action form S=L(1-phi), while the Gate B regularized "
        "scalar, normalization, propagation/readout, and generated-connectivity "
        "rules remain supplied."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
