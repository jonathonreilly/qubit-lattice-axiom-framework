#!/usr/bin/env python3
"""Exact integer checks: M_3(C) does not embed in one-site M_2(C).

Identity gates call dim_m2() and dim_m3(). The mutation predicate
dim M_3 <= dim M_2 must fail (9 ≰ 4). Parents: axiom memo only.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "M3_DOES_NOT_EMBED_IN_ONE_SITE_M2_COLOR_ALGEBRA_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/M3_DOES_NOT_EMBED_IN_ONE_SITE_M2_COLOR_ALGEBRA_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def dim_matrix_algebra(n: int) -> int:
    """Exact complex dimension of M_n(C): n^2."""
    return n * n


def dim_m2() -> int:
    return dim_matrix_algebra(2)


def dim_m3() -> int:
    return dim_matrix_algebra(3)


def dim_m3_leq_dim_m2() -> bool:
    """Mutation predicate: dim M_3 <= dim M_2. Must fail (9 ≰ 4)."""
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
    note_n = normalize(note)
    axiom_n = normalize(axiom)

    print("external_scientific_inputs: none; exact integer dimensions only")
    print("package_local_integrity_reads: new note and current axiom memo")
    print("negative_scope: one-site injection only; multi-site tensors remain open")

    # Identity gates MUST call dim_m2() and dim_m3().
    checks.check(
        "identity-dim-m2",
        "dim_C(M_2(C)) = 4 via dim_m2()",
        dim_m2() == 4,
    )
    checks.check(
        "identity-dim-m3",
        "dim_C(M_3(C)) = 9 via dim_m3()",
        dim_m3() == 9,
    )
    checks.check(
        "exact-integers",
        "both dimensions are exact Python ints",
        isinstance(dim_m2(), int) and isinstance(dim_m3(), int),
    )
    checks.check(
        "theorem-1-strict",
        "9 > 4 so no injective C-linear map A3 → A2",
        dim_m3() > dim_m2(),
    )
    checks.check(
        "mutation-dim-m3-leq-dim-m2-fails",
        "predicate dim M_3 <= dim M_2 fails (9 ≰ 4)",
        dim_m3_leq_dim_m2() is False,
    )
    checks.check(
        "no-injective-star-hom",
        "an injective *-hom would be an injective C-linear map, already impossible",
        not dim_m3_leq_dim_m2(),
    )

    qubit_sentence = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    checks.check(
        "theorem-2-qubit-quote",
        "axiom memo names the one-site algebra as M_2(C)",
        qubit_sentence in axiom,
    )
    checks.check(
        "theorem-2-no-m3",
        "axiom memo does not name M_3(C)",
        "M_3(C)" not in axiom and "M_3(\\mathrm{C})" not in axiom,
    )
    checks.check(
        "theorem-2-no-su3",
        "axiom memo does not name SU(3)",
        "SU(3)" not in axiom and "SU3" not in axiom,
    )

    checks.check(
        "theorem-3-display-a3",
        "note displays A3 = M_3(C) as an extra object",
        "A3 = M_3(C)" in note or "A3 := M_3(C)" in note,
    )
    checks.check(
        "theorem-3-no-color-axiom",
        "note does not adopt a color axiom",
        "does not adopt a color axiom" in note_n.lower(),
    )
    checks.check(
        "theorem-3-not-qcd",
        "note does not identify A3 with QCD",
        "does not identify" in note_n.lower() and "QCD" in note,
    )
    checks.check(
        "theorem-3-min-dim-or-c3",
        "extra object is at least 9-dimensional or a C^3 Hilbert space",
        "nine-dimensional" in note_n.lower() and "C^3" in note,
    )

    checks.check(
        "theorem-4-june-10-not-retired",
        "note does not retire June 10",
        "does not retire June 10" in note,
    )
    checks.check(
        "theorem-4-np-not-lnzl",
        "N_p and ln Z_L are different objects",
        "N_p" in note and "ln Z_L" in note and "different" in note_n,
    )
    checks.check(
        "theorem-4-no-05934",
        "0.5934 is not imported",
        "0.5934" not in axiom
        and "`0.5934` is not used, not imported" in note
        and "`0.5934` is not imported" in note_n,
    )

    checks.check(
        "theorem-5-no-r-half",
        "note does not force r=1/2",
        "does not force" in note_n and "r = 1/2" in note,
    )
    checks.check(
        "theorem-5-no-multisite-impossibility",
        "note does not claim color is impossible later on a multi-site tensor",
        "does not claim" in note_n and "multi-site tensor" in note,
    )

    checks.check(
        "audit-inputs-axiom-and-note-only",
        "declared audit inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/M3_DOES_NOT_EMBED_IN_ONE_SITE_M2_COLOR_ALGEBRA_IS_EXTRA_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "no-unmerged-pr-citation",
        "note does not cite unmerged PR numbers or c8carrier/phycomp",
        "c8carrier" not in note_n.lower()
        and "phycomp" not in note_n.lower()
        and "PR #" not in note
        and "#6198" not in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
