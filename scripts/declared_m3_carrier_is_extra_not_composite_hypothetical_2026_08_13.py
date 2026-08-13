#!/usr/bin/env python3
"""Exact leftover-type checks: declared M_3 is extra, not a composite.

Counts dim M_2 and dim M_3 from standard matrix units, reconstructs that
class C (finite tensor/sum of M_2) has no unital M_3 because 3 never
divides 2^k and simplicity factors a unital map through one summand,
and checks that displayed S'' is a declaration, not a theorem of
Lattice+Qubit+S'. S' and S'' are not adopted. No QCD. No fifth axiom.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "DECLARED_M3_CARRIER_IS_EXTRA_NOT_COMPOSITE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/DECLARED_M3_CARRIER_IS_EXTRA_NOT_COMPOSITE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

S = "The full one-site possibility domain has algebraic presentation `M_2(C)`."
S_PRIME = (
    "The local algebra is `M_2`; a physical object may be a declared finite "
    "composite in the tensor/sum class `C` of `M_2`."
)
S_DOUBLE_PRIME = "There is also a declared one-object algebra `M_3(C)`."


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


def dim_mn(n: int) -> int:
    units = standard_matrix_units(n)
    if len(set(units)) != len(units):
        raise ValueError("standard matrix units are not distinct")
    return len(units)


def dim_m2() -> int:
    return dim_mn(2)


def dim_m3() -> int:
    return dim_mn(3)


def power_of_two(k: int) -> int:
    if k < 1:
        raise ValueError("k must be >= 1")
    return 2**k


def three_divides_power_of_two(k: int) -> bool:
    return power_of_two(k) % 3 == 0


def unital_hom_exists(source_size: int, target_size: int) -> bool:
    return target_size % source_size == 0


def class_c_witness_summand_sizes() -> tuple[tuple[int, ...], ...]:
    # M_2, M_2⊗M_2 ≅ M_4, M_2⊕M_2, M_4⊕M_2
    return ((2,), (4,), (2, 2), (4, 2))


def hosts_unital_m3(summand_sizes: tuple[int, ...]) -> bool:
    # Simplicity: a unital *-hom into a finite sum factors through one summand.
    return any(unital_hom_exists(3, size) for size in summand_sizes)


def predicate_memo_names_m3(axiom_text: str) -> bool:
    return "M_3(C)" in axiom_text


def predicate_nine_le_four() -> bool:
    return dim_m3() <= dim_m2()


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
    self_source = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")

    print(
        "external_scientific_inputs: current axiom wording is source-bound; "
        "dimensions are counted from standard bases; class-C exclusion is "
        "exact integer remainder; no observational or fitted inputs"
    )
    print(
        "package_local_integrity_reads: the proposed source note and live "
        "axiom memo only"
    )
    print(
        "negative_scope: declared M_3 is typed as extra, not as a composite "
        "in C; S' and S'' are displayed and not adopted"
    )

    d2 = dim_m2()
    d3 = dim_m3()

    checks.check(
        "identity-dim-m2",
        "dim_m2() counts the four standard 2-by-2 matrix units",
        d2 == 2 * 2 and d2 == len(standard_matrix_units(2)),
    )
    checks.check(
        "identity-dim-m3",
        "dim_m3() counts the nine standard 3-by-3 matrix units",
        d3 == 3 * 3 and d3 == len(standard_matrix_units(3)),
    )
    checks.check(
        "theorem1-nine-gt-four",
        "9>4 so dim M_3 exceeds dim M_2",
        d3 > d2,
    )
    checks.check(
        "theorem1-s-does-not-name-m3",
        "sentence S names M_2(C) and does not name M_3",
        "M_2(C)" in S and "M_3" not in S and S in axiom and S in note,
    )
    remainders = tuple(power_of_two(k) % 3 for k in range(1, 9))
    checks.check(
        "theorem2-three-never-divides",
        "3 does not divide 2^k for each k in 1..8",
        remainders == (2, 1, 2, 1, 2, 1, 2, 1)
        and all(not three_divides_power_of_two(k) for k in range(1, 9)),
    )
    checks.check(
        "theorem2-no-unital-into-power-of-two",
        "no unital *-hom M_3 -> M_{2^k} for k=1..8",
        all(not unital_hom_exists(3, power_of_two(k)) for k in range(1, 9)),
    )
    witnesses = class_c_witness_summand_sizes()
    checks.check(
        "theorem2-simple-factor-witnesses",
        "unital M_3 is absent from the four class-C witnesses by simple factoring",
        witnesses == ((2,), (4,), (2, 2), (4, 2))
        and all(not hosts_unital_m3(sizes) for sizes in witnesses),
    )
    checks.check(
        "theorem2-sprime-does-not-supply-m3",
        "S' plus class C does not supply M_3",
        normalize(S_PRIME) in normalized_note
        and "Sentence `S′` therefore does not supply `M_3`." in note
        and "So class `C` contains no unital copy of `M_3`." in note,
    )
    checks.check(
        "mutation-memo-names-m3",
        "the predicate that the axiom memo names M_3(C) fails",
        not predicate_memo_names_m3(axiom),
    )
    checks.check(
        "mutation-nine-le-four",
        "the predicate 9≤4 fails",
        not predicate_nine_le_four() and d3 > d2,
    )
    checks.check(
        "theorem3-sdoubleprime-is-declaration",
        "S'' names M_3 by declaration and is displayed as extra, not adopted",
        S_DOUBLE_PRIME in note
        and all(
            phrase in note
            for phrase in (
                "That is an extra object — a second carrier type — not a theorem of",
                "Lattice + Qubit + `S′`.",
                "Display `S′′`. Do not adopt it. Do not call it QCD.",
            )
        )
        and S_DOUBLE_PRIME not in axiom
        and S_PRIME not in axiom,
    )
    checks.check(
        "theorem4-wall-slogan-not-extra",
        "C2 as a reading removes a wall slogan, not the extra object",
        all(
            phrase in note
            for phrase in (
                "removes a *wall slogan*",
                "It does not produce `M_3`.",
                "Color remains extra unless some other construction",
                "not in `C`, and",
                "not a silent declaration",
            )
        ),
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required leftover status and bounded-support fields",
        all(
            phrase in note
            for phrase in (
                'hypothetical_axiom_status: "C2 leftover: declaring M_3 as a carrier is an extra object; not adopted"',
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "live-qubit-nonmutation",
        "live axiom memo still states one-site M_2(C); leftover sentences are not adopted",
        S in axiom
        and "Do not adopt a fifth axiom." in note
        and "Do not adopt them." in note
        and "Neither `S′` nor `S′′` is written into the axiom memo." in note
        and "declared one-object algebra" not in axiom,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/DECLARED_M3_CARRIER_IS_EXTRA_NOT_COMPOSITE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and (
            "AUDIT_INPUT_PATHS = (\n"
            '    "docs/DECLARED_M3_CARRIER_IS_EXTRA_NOT_COMPOSITE_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",\n'
            '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
            ")"
        )
        in self_source,
    )
    qcd_module_load = "from " + "qcd"
    checks.check(
        "no-qcd-no-fifth-axiom",
        "note refuses QCD identification and a fifth axiom; runner loads no QCD module",
        all(
            phrase in note
            for phrase in (
                "Do not call it QCD.",
                "Do not adopt a fifth axiom.",
                "`A3` is QCD",
                "not adopted",
            )
        )
        and qcd_module_load not in self_source.lower()
        and qcd_module_load not in note.lower()
        and "**Type:** bounded_theorem" in note,
    )

    print("per_element: identity gates call dim_m2() and dim_m3(); 3 ∤ 2^k is integer remainder")
    print("per_site: A2 is the one-site algebra named by S; A3 is a comparison algebra only")
    print("per_block: leftover type after class C is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide color or QCD claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
