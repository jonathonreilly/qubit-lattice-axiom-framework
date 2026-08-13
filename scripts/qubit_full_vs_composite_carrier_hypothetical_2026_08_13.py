#!/usr/bin/env python3
"""Exact dimension checks for the Qubit full-versus-composite reading.

The runner counts complex dimensions of M_2(C), M_3(C), C^8, and one-site
C^2 from standard bases, checks that 9>4 and 8>2, and checks that current
sentence S and displayed counterfactual S' agree on dim A2. No QCD, no
0.5934, no forced r=1/2. S' is not adopted.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "QUBIT_FULL_VS_COMPOSITE_CARRIER_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/QUBIT_FULL_VS_COMPOSITE_CARRIER_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

S = "The full one-site possibility domain has algebraic presentation `M_2(C)`."
S_PRIME = (
    "The local possibility algebra at a site is `M_2(C)`; a physical object "
    "may be a declared finite composite of sites or a declared larger carrier."
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def standard_matrix_units(n: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    units = []
    for row in range(n):
        for column in range(n):
            matrix = [[0] * n for _ in range(n)]
            matrix[row][column] = 1
            units.append(tuple(tuple(entry) for entry in matrix))
    return tuple(units)


def standard_basis(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(1 if index == axis else 0 for index in range(n)) for axis in range(n))


def dim_mn(n: int) -> int:
    units = standard_matrix_units(n)
    if len(set(units)) != len(units):
        raise ValueError("standard matrix units are not distinct")
    return len(units)


def dim_m2() -> int:
    return dim_mn(2)


def dim_m3() -> int:
    return dim_mn(3)


def dim_c8() -> int:
    basis = standard_basis(8)
    if len(set(basis)) != len(basis):
        raise ValueError("standard basis of C^8 is not distinct")
    return len(basis)


def dim_one_site_hilbert() -> int:
    basis = standard_basis(2)
    if len(set(basis)) != len(basis):
        raise ValueError("standard basis of C^2 is not distinct")
    return len(basis)


def exists_injective_c_linear(dim_src: int, dim_tgt: int) -> bool:
    return dim_src <= dim_tgt


def dim_a2_named_by(sentence: str) -> int:
    if "M_2(C)" not in sentence and "M_2(C)" not in sentence.replace(" ", ""):
        raise ValueError("sentence does not name A2")
    if "M_2" not in sentence:
        raise ValueError("sentence does not name A2")
    return dim_m2()


def predicate_dim_m3_le_dim_m2() -> bool:
    return dim_m3() <= dim_m2()


def predicate_s_and_sprime_disagree_dim_a2() -> bool:
    return dim_a2_named_by(S) != dim_a2_named_by(S_PRIME)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "dimensions are counted from standard bases; no observational or "
        "fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; unmerged color3/phycomp/ranksplit surfaces "
        "are not imported"
    )
    print(
        "negative_scope: only the reading that nothing physical is larger "
        "than one-site A2 is separated from the 9>4 and 8>2 facts; S' is "
        "displayed and not adopted"
    )

    d2 = dim_m2()
    d3 = dim_m3()
    d8 = dim_c8()
    d_site = dim_one_site_hilbert()

    checks.check(
        "identity-dim-m2",
        f"the identity gate dim_m2() equals {d2} by counting 2-by-2 matrix units",
        d2 == 2 * 2 and d2 == len(standard_matrix_units(2)),
    )
    checks.check(
        "identity-dim-m3",
        f"the identity gate dim_m3() equals {d3} by counting 3-by-3 matrix units",
        d3 == 3 * 3 and d3 == len(standard_matrix_units(3)),
    )
    checks.check(
        "identity-dim-c8",
        f"the identity gate dim_c8() equals {d8} by counting the standard basis of C^8",
        d8 == 8 and d8 == len(standard_basis(8)),
    )
    checks.check(
        "one-site-hilbert",
        "the one-site Hilbert space of A2 is C^2 with dimension 2",
        d_site == 2 and d_site == len(standard_basis(2)),
    )
    checks.check(
        "theorem1-no-injective",
        "9>4 so no injective C-linear map A3→A2 exists",
        d3 > d2 and not exists_injective_c_linear(d3, d2),
    )
    checks.check(
        "theorem1-c8-not-one-site",
        "8>2 so C^8 is not the one-site Hilbert space",
        d8 > d_site and not exists_injective_c_linear(d8, d_site),
    )
    checks.check(
        "mutation-dim-m3-le-dim-m2",
        "the predicate dim M_3 ≤ dim M_2 fails",
        not predicate_dim_m3_le_dim_m2() and d3 > d2,
    )
    checks.check(
        "theorem2-agree-dim-a2",
        "S and S' both name A2 and both assign dim_C A2 = 4",
        dim_a2_named_by(S) == d2 and dim_a2_named_by(S_PRIME) == d2,
    )
    checks.check(
        "mutation-s-sprime-disagree-dim-a2",
        "the predicate that S and S' disagree about dim A2 fails",
        not predicate_s_and_sprime_disagree_dim_a2(),
    )
    checks.check(
        "source-qubit-sentence",
        "the current axiom memo and the note both carry sentence S",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the note displays S' and refuses adoption and a Qubit rewrite",
        all(
            phrase in normalized_note
            for phrase in (
                normalize(S_PRIME),
                "displayed, not adopted",
                "Display `S′`. Do not adopt it.",
                "This note does not rewrite the Qubit axiom.",
            )
        )
        and S_PRIME not in axiom
        and "declared finite composite of sites" not in axiom,
    )
    checks.check(
        "theorem3-wall-is-reading",
        "the note locates the color/P-HY wall in a reading of S, not in the dimensions",
        all(
            phrase in note
            for phrase in (
                "extras *to the axiom*",
                "extras *to one site*",
                "The TOE wall “color/`P-HY` cannot exist unless we add an axiom” is a",
                "reading of `S`, not of the dimension facts.",
            )
        ),
    )
    checks.check(
        "theorem4-boundary",
        "the note refuses QCD, generation, U(1)_Y, 0.5934, and r=1/2 identifications",
        all(
            phrase in note
            for phrase in (
                "This note does not identify `A3` with QCD.",
                "This note does not identify `C^8` with generations",
                "This note does not identify `Y` with `U(1)_Y`.",
                "This note does not import `0.5934`.",
                "This note does not force `r=1/2`.",
            )
        )
        and "0.5934" not in axiom,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required C2 counterfactual and bounded-support fields",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "C2 counterfactual: M_2 is the local possibility algebra; physical carriers may be composites; not adopted"',
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "no-unmerged-citation",
        "the note does not cite unmerged color3, phycomp, or ranksplit surfaces",
        all(
            needle not in note.lower()
            for needle in (
                "color3",
                "phycomp",
                "ranksplit",
                "unmerged pr",
                "pull/6",
            )
        ),
    )

    print("per_element: identity gates call dim_m2(), dim_m3(), and dim_c8(); injectivity is the dimension comparison")
    print("per_site: A2 and C^2 are one-site objects; A3 and C^8 are extras to one site")
    print("per_mode: no spectral-mode exhaustion is claimed")
    print("per_block: the S-versus-S' reading of the Qubit sentence is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide compiler or QCD claim is made")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
