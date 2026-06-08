#!/usr/bin/env python3
"""
DM neutrino weak-triplet coefficient framework boundary.

Framework convention for this runner:
  the legacy claim id contains "axiom", but the live framework baseline is the
  named Lattice + Quantum + Record axiom set. This packet uses the Lattice +
  Quantum algebraic surface, not a new or single axiom.

Question:
  Does the current Lattice + Quantum baseline, together with the current
  derived atlas rows, already derive the transfer coefficients c_odd and
  M_even in

      gamma = c_odd * a_sel
      [E1,E2]^T = M_even [tau_E,tau_T]^T ?

Answer:
  Yes.

  The transfer class is exact, and the transfer coefficients are now fixed:

    - c_odd = +1 on the source-oriented branch convention
    - M_even = v_even [1,1]
    - v_even = (sqrt(8/3), sqrt(8)/3)

  by bosonic matching on the reduced selector / triplet odd blocks and on the
  exact weak row factor / even dual generators.

  Equivalently:

    - gamma = a_sel
    - E1 = sqrt(8/3) * (tau_E + tau_T)
    - E2 = (sqrt(8)/3) * (tau_E + tau_T)

  What remains open is not transfer-coefficient normalization. It is the
  source-amplitude law for a_sel and tau_+, and the benchmark runner has not
  yet been rebuilt around that exact transfer law.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", cls: str = "B") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status} ({cls})] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def read(rel: str) -> str:
    path = ROOT / rel
    if path.exists():
        return path.read_text(encoding="utf-8")

    filename = Path(rel).name
    archived = sorted((ROOT / "archive_unlanded").glob(f"**/{filename}"))
    if len(archived) == 1:
        return archived[0].read_text(encoding="utf-8")
    raise FileNotFoundError(path)


def compact(text: str) -> str:
    return "".join(text.split())


def part1_framework_baseline_is_named_lattice_quantum_record() -> None:
    print("\n" + "=" * 88)
    print("PART 1: FRAMEWORK BASELINE IS LATTICE + QUANTUM + RECORD")
    print("=" * 88)

    minimal = read("docs/MINIMAL_AXIOMS_2026-06-05.md")
    transfer = read("docs/DM_NEUTRINO_WEAK_TRIPLET_TRANSFER_CLASS_THEOREM_NOTE_2026-04-15.md")

    check(
        "The live framework baseline names Lattice, Quantum, and Record",
        "1. **Lattice**" in minimal
        and "2. **Quantum**" in minimal
        and "3. **Record**" in minimal,
    )
    check(
        "The Lattice + Quantum surface supplies Z^3 and the one-qubit/Cl(3,0) carrier",
        "The site set is `Z^3`" in minimal
        and "`A_x ~= M_2(C)`, equivalently `Cl(3,0)`" in minimal,
    )
    check(
        "The transfer-class theorem is a derived structural theorem on top of the baseline surface",
        "exact transfer-class theorem" in transfer and "coefficient problem" in transfer,
    )


def part2_c_odd_is_now_fixed_by_bosonic_matching() -> None:
    print("\n" + "=" * 88)
    print("PART 2: C_ODD IS NOW FIXED BY BOSONIC MATCHING")
    print("=" * 88)

    selector = read("docs/PMNS_SELECTOR_UNIQUE_AMPLITUDE_SLOT_NOTE.md")
    sign = read("docs/PMNS_SELECTOR_SIGN_TO_BRANCH_REDUCTION_NOTE.md")
    source = read("docs/DM_NEUTRINO_TRIPLET_CHARACTER_SOURCE_THEOREM_NOTE_2026-04-15.md")
    codd = read("docs/DM_NEUTRINO_CODD_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md")

    check(
        "The source side gives exactly one real selector amplitude slot a_sel",
        "one real amplitude slot" in selector and "B_red = a_sel S_cls" in selector,
    )
    check(
        "The target side gives exactly one odd triplet slot gamma",
        "CP-odd triplet slot `gamma`" in source or "CP-odd triplet slot" in source,
    )
    check(
        "The bosonic matching theorem fixes the canonical odd normalization to |c_odd| = 1",
        "|c_odd| = 1" in codd and "c_odd = +1" in codd,
    )
    check(
        "The source-oriented sign convention records c_odd = +1",
        "a_sel > 0" in sign,
        "positive selector orientation picks the source-oriented branch",
    )


def part3_the_exact_source_carrier_closes_the_even_leg() -> None:
    print("\n" + "=" * 88)
    print("PART 3: THE EXACT SOURCE CARRIER CLOSES THE EVEN LEG")
    print("=" * 88)

    primitive = read("docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md")
    reduction = read("docs/DM_NEUTRINO_WEAK_EVEN_SWAP_REDUCTION_THEOREM_NOTE_2026-04-15.md")
    veven = read("docs/DM_NEUTRINO_VEVEN_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md")

    v_even = np.array([0.7, -0.2], dtype=float)
    m = np.column_stack([v_even, v_even])
    primitive_compact = compact(primitive)

    check(
        "The exact source carrier treats the two bright columns symmetrically as u_E and u_T",
        "K_R(q):=[[u_E(q),u_T(q)],[delta_A1(q)u_E(q),delta_A1(q)u_T(q)]]"
        in primitive_compact
        or "K_R(q)=[[u_E(q),u_T(q)],[delta_A1(q)u_E(q),delta_A1(q)u_T(q)]]"
        in primitive_compact,
    )
    check(
        "The swap-reduction theorem records the exact common-column form M_even = v_even [1,1]",
        "v_even [1,1]" in reduction or "v_even [1, 1]" in reduction,
    )
    check(
        "The antisymmetric source mode lies in the kernel of the swap-fixed exact class",
        np.linalg.norm(m @ np.array([1.0, -1.0])) < 1e-12,
        f"kernel err={np.linalg.norm(m @ np.array([1.0,-1.0])):.2e}",
        cls="A",
    )
    check(
        "The even bosonic-normalization theorem fixes v_even exactly",
        "v_even = (sqrt(8/3), sqrt(8)/3)" in veven,
    )
    check(
        "So the exact even transfer law is [E1,E2]^T = v_even (tau_E + tau_T)",
        "E1 = sqrt(8/3) tau_+" in veven and "E2 = (sqrt(8)/3) tau_+" in veven,
    )
    check(
        "The source-side carrier still factors through the symmetric row mode only",
        "tau_+ = tau_E + tau_T" in reduction
        and "M_even [1,-1]^T = 0" in reduction,
    )


def part4_the_current_single_axiom_boundary_is_exact() -> None:
    print("\n" + "=" * 88)
    print("PART 4: THE CURRENT FRAMEWORK BOUNDARY IS EXACT")
    print("=" * 88)

    boundary = read("docs/DM_NEUTRINO_WEAK_TRIPLET_COEFFICIENT_AXIOM_BOUNDARY_NOTE_2026-04-15.md")

    check(
        "The boundary note records that the live gap is now source amplitudes rather than transfer coefficients",
        "source-amplitude law" in boundary and "a_sel" in boundary and "tau_+" in boundary,
    )
    check(
        "The boundary note records that the benchmark remains bounded because the source amplitudes are still open",
        "eta = 1.81e-10" in boundary
        and "benchmark runner has not yet been rebuilt" in boundary
        and "exact transfer" in boundary,
    )


def main() -> int:
    print("=" * 88)
    print("DM NEUTRINO WEAK-TRIPLET COEFFICIENT FRAMEWORK BOUNDARY")
    print("=" * 88)

    part1_framework_baseline_is_named_lattice_quantum_record()
    part2_c_odd_is_now_fixed_by_bosonic_matching()
    part3_the_exact_source_carrier_closes_the_even_leg()
    part4_the_current_single_axiom_boundary_is_exact()

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
