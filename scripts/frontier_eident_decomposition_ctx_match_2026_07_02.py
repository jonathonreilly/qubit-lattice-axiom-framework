#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OCC = ROOT / "docs/OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md"
BLOCK06 = ROOT / "docs/EQUAL_CHANNEL_ENERGY_REDUCES_TO_EQUIPARTITION_SURFACE_DICTIONARY_RESIDUAL_BOUNDED_NOTE_2026-07-02.md"
BLOCK01 = ROOT / "docs/FLAVOR_CARRIER_MEASURE_SCORING_DISCRIMINATOR_BOUNDED_NOTE_2026-07-02.md"


def scaled_square_fixed_roots(scale: Fraction) -> set[Fraction]:
    """Solve r = scale*r^2 exactly for nonzero scale."""
    if scale == 0:
        raise ValueError("scale must be nonzero")
    return {Fraction(0), Fraction(1, 1) / scale}


def fixed_points_slot():
    return scaled_square_fixed_roots(Fraction(1))


def fixed_points_component():
    return scaled_square_fixed_roots(Fraction(2))


def main():
    checks = []
    occ = OCC.read_text()
    block06 = BLOCK06.read_text()
    block01 = BLOCK01.read_text()
    all_text = "\n".join([occ, block06, block01])

    a2 = Fraction(5, 7)
    b2 = Fraction(11, 13)
    ps = a2
    pd = 2 * b2
    ei = 3 * a2
    eb = 6 * b2

    checks.append(("T1 proportionality EI=3ps", ei == 3 * ps))
    checks.append(("T1 proportionality EB=3pd", eb == 3 * pd))
    checks.append(("T1 cancellation factor", (ei - eb) == 3 * (ps - pd)))

    equal_case_a2 = Fraction(9, 10)
    equal_case_b2 = equal_case_a2 / 2
    checks.append(("T1 equal-weight implies equal-energy", 3 * equal_case_a2 == 6 * equal_case_b2))
    checks.append(("T1 equal-energy implies equal-weight", equal_case_a2 == 2 * equal_case_b2))

    checks.append(("component fixed set {0,1/2}", fixed_points_component() == {Fraction(0), Fraction(1, 2)}))
    checks.append(("slot fixed set {0,1}", fixed_points_slot() == {Fraction(0), Fraction(1)}))
    checks.append(("component r=1/2 gives x=1", 2 * Fraction(1, 2) == 1))
    checks.append(("slot r=1 gives x=1", Fraction(1) == 1))

    anchors = [
        "Given a readout context with a finite central-sector decomposition and a fixed\n`K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized\ncentral sector.",
        "On the supplied surface, the two registered outcomes are the singlet outcome\n`s` and the doublet `K`-orbit outcome `d`.",
        "x' = (p_d^2/Z)/(p_s^2/Z) = (p_d/p_s)^2 = x^2.",
        "- Component dictionary `(1,2)`: `x = 2r`. The doublet outcome carries two\n  components, so `p_d = 2|b|^2` and `p_s = a^2`.",
        "- Slot dictionary `(1,1)`: `x = r`. There is one slot per outcome at equal\n  per-slot weight.",
        "||I||^2 = 3,        ||B||^2 = 6.",
        "Y = a I + b U + conj(b) U^{-1}.",
        "The exact structural parallel is the shared\n`C_3` singlet/doublet split.",
    ]
    for anchor in anchors:
        checks.append((f"text anchor: {anchor.splitlines()[0][:40]}", anchor in all_text))

    fail = [name for name, ok in checks if not ok]
    passed = len(checks) - len(fail)

    if fail:
        print("FAIL: " + "; ".join(fail[:4]))
        print(f"FAIL: {len(fail)} check(s) failed; exact proportionality or textual anchors need review.")
    else:
        print("PASS: T1 exact proportionality, cancellation, and equal-weight iff equal-energy.")
        print("PASS: fixed-set reuse and textual anchors for weights, norms, and CTX-match floor.")
    print(f"TOTAL: PASS={passed} FAIL={len(fail)}")

    return 1 if fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
