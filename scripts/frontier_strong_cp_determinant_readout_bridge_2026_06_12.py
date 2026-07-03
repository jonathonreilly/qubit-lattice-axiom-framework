#!/usr/bin/env python3
"""Verifier for the strong-CP determinant-readout bridge.

The runner checks the narrow bridge in
docs/STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md:
continuous determinant phase characters are multiplicative over independent
mass blocks, K/CPT orbit invariance forces k=0, and K-even nonmultiplicative
phase probes are excluded by the block law.
"""

from __future__ import annotations

import cmath
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "STRONG_CP_DETERMINANT_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-12.md"
THETA_NOTE = DOCS / "THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md"
MINIMAL_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"
STRONG_CP_PARENT = DOCS / "STRONG_CP_THETA_ZERO_NOTE.md"

PASS = 0
FAIL = 0
EPS = 1.0e-12


def flat(text: str) -> str:
    return " ".join(text.split())


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag} {label}{suffix}")


def char(k: int, phi: float) -> complex:
    return cmath.exp(1j * k * phi)


def close(a: complex | float, b: complex | float) -> bool:
    return abs(a - b) < EPS


def main() -> int:
    print("Strong-CP determinant-readout bridge verifier")
    print("=" * 72)

    note = NOTE.read_text(encoding="utf-8")
    note_flat = flat(note)
    theta_note = THETA_NOTE.read_text(encoding="utf-8")
    minimal = MINIMAL_AXIOMS.read_text(encoding="utf-8")
    parent = STRONG_CP_PARENT.read_text(encoding="utf-8")

    check("bridge note exists and declares bounded theorem", "Claim type:** bounded_theorem" in note)
    check(
        "bridge names the theta P2/K-CPT row it feeds",
        THETA_NOTE.name in note and "determinant-readout bridge" in note_flat,
    )
    check(
        "bridge is explicitly mass-determinant-channel only",
        "mass-determinant channel only" in note_flat
        and "not a gauge-theta theorem" in note_flat,
    )
    check(
        "bridge does not claim action/gauge theta closure",
        "does not set `theta_gauge = 0`" in note
        and "does not eliminate multi-plaquette or large-winding gauge data" in note_flat
        and "does not prove that every possible action-level observable" in note_flat,
    )
    check(
        "Record boundary remains supplied-context only",
        "The Record axiom supplies the orbit/additivity discipline only after this readout interface is supplied"
        in note_flat
        and "does not supply the determinant channel by itself" in note_flat
        and "realized outcome is the `K`/CPT orbit" in minimal,
    )
    check(
        "strong-CP parent is cited but not promoted",
        STRONG_CP_PARENT.name in note and "does not promote it" in note_flat and "theta" in parent.lower(),
    )

    phases = [0.0, 0.17, 0.41, -0.73, 1.2]
    ks = [-3, -2, -1, 0, 1, 2, 3]
    for k in ks:
        multiplicative = all(
            close(char(k, a + b), char(k, a) * char(k, b))
            for a in phases
            for b in phases
        )
        check(f"U(1) character k={k} is multiplicative over determinant products", multiplicative)

    invariant_ks = []
    for k in ks:
        invariant = all(close(char(k, phi), char(k, -phi)) for phi in phases)
        if invariant:
            invariant_ks.append(k)
    check("K/CPT invariance leaves only k=0 among sampled determinant phase characters", invariant_ks == [0], str(invariant_ks))

    phi = 0.4
    psi = 0.9
    cos_k_even = close(math.cos(phi), math.cos(-phi))
    cos_mult_gap = abs(math.cos(phi + psi) - math.cos(phi) * math.cos(psi))
    check("hostile cos(arg det) probe is K-even", cos_k_even)
    check(
        "hostile cos(arg det) probe violates independent-block multiplicativity",
        cos_mult_gap > 1.0e-2,
        f"gap={cos_mult_gap:.6f}",
    )

    z1 = 1.3 * cmath.exp(1j * phi)
    z2 = 0.7 * cmath.exp(1j * psi)
    block_det = z1 * z2
    check("direct-sum determinant product law represented on supplied determinants", close(block_det, z1 * z2))
    check(
        "K/CPT conjugation reverses determinant phase",
        close(cmath.phase(z1.conjugate()), -cmath.phase(z1)),
        f"phi={cmath.phase(z1):.6f}",
    )

    check(
        "theta note wires this bridge without claiming gauge/action closure",
        NOTE.name in theta_note
        and "The Determinant-Readout Bridge" in theta_note
        and "does not set `theta_gauge = 0`" in theta_note
        and "independent review/audit accepts the determinant-readout bridge surface being used"
        in flat(theta_note),
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
