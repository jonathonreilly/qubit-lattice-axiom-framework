#!/usr/bin/env python3
"""Exact checks: C1 J type does not enforce Record admissibility.

Reconstructs J:W→{0}∪M on W={x,y} with labels {A,B,C} and declared
μ(A)=3/5, μ(B)=2/5, μ(C)=0. Unit-count I is 1 on J_ok=(A,0) and
J_bad=(C,0). Displayed J splits them. The leftover constraint is
im(J)\\{0} ⊆ supp(μ). C1 is not adopted. No pairing on J. No Tr.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/J_TYPE_DOES_NOT_ENFORCE_ADMISSIBILITY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

AUDIT_INPUT_PATHS = (
    "docs/J_TYPE_DOES_NOT_ENFORCE_ADMISSIBILITY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

X = "x"
Y = "y"
W = (X, Y)
ZERO = 0
A = "A"
B = "B"
C = "C"
M = (A, B, C)
CODEMAIN = (ZERO,) + M

MU = {
    A: Fraction(3, 5),
    B: Fraction(2, 5),
    C: Fraction(0),
}

J_OK = (A, ZERO)
J_BAD = (C, ZERO)


def J_of(lock_field: tuple[object, ...]) -> tuple[object, ...]:
    return lock_field


def I_of(lock_field: tuple[object, ...]) -> int:
    return sum(1 for lock in lock_field if lock != ZERO)


def mu_A() -> Fraction:
    return MU[A]


def mu_C() -> Fraction:
    return MU[C]


def supp_mu() -> frozenset[str]:
    return frozenset(label for label, mass in MU.items() if mass != 0)


def image_nonzero(lock_field: tuple[object, ...]) -> frozenset[object]:
    return frozenset(lock for lock in lock_field if lock != ZERO)


def well_typed(lock_field: tuple[object, ...]) -> bool:
    return len(lock_field) == len(W) and all(lock in CODEMAIN for lock in lock_field)


def legal(lock_field: tuple[object, ...]) -> bool:
    return image_nonzero(lock_field) <= supp_mu()


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


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_norm = normalize(note)

    print("external_scientific_inputs: axiom memo Record wording only; C1 J arithmetic is reconstructed")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: leftover image constraint; C1 not adopted; no pairing on J; no Tr")

    checks.check(
        "audit-input-paths",
        "declared inputs are the new note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/J_TYPE_DOES_NOT_ENFORCE_ADMISSIBILITY_HYPOTHETICAL_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "record-quote",
        "current Record locks exactly one admissible local possibility",
        "locks exactly one admissible local possibility" in axiom,
    )

    i_ok = I_of(J_OK)
    i_bad = I_of(J_BAD)
    checks.check(
        "identity-I_of-J_ok",
        "I_of(J_ok) is unit-count 1",
        i_ok == 1 and isinstance(i_ok, int),
    )
    checks.check(
        "identity-I_of-J_bad",
        "I_of(J_bad) is unit-count 1",
        i_bad == 1 and isinstance(i_bad, int),
    )
    checks.check(
        "theorem1-I-does-not-split",
        "I(J_ok) equals I(J_bad)",
        i_ok == i_bad,
    )

    j_ok = J_of(J_OK)
    j_bad = J_of(J_BAD)
    checks.check(
        "identity-J_of-J_ok",
        "J_of on J_ok returns (A, 0)",
        j_ok == (A, ZERO),
    )
    checks.check(
        "identity-J_of-J_bad",
        "J_of on J_bad returns (C, 0)",
        j_bad == (C, ZERO),
    )
    checks.check(
        "theorem2-J-splits",
        "displayed J_ok is not J_bad",
        j_ok != j_bad,
    )

    mass_c = mu_C()
    mass_a = mu_A()
    checks.check(
        "identity-mu_C",
        "mu_C() is 0",
        mass_c == 0 and isinstance(mass_c, Fraction),
    )
    checks.check(
        "identity-mu_A",
        "mu_A() is 3/5",
        mass_a == Fraction(3, 5) and isinstance(mass_a, Fraction),
    )
    checks.check(
        "declared-support",
        "supp(mu) is {A, B}",
        supp_mu() == frozenset({A, B}),
    )
    checks.check(
        "theorem3-both-well-typed",
        "J_ok and J_bad are values of W→{0}∪M",
        well_typed(j_ok) is True and well_typed(j_bad) is True,
    )
    checks.check(
        "theorem3-legal-versus-illegal",
        "J_ok meets im(J)\\{0} ⊆ supp(mu); J_bad does not",
        legal(j_ok) is True
        and legal(j_bad) is False
        and image_nonzero(j_ok) == frozenset({A})
        and image_nonzero(j_bad) == frozenset({C}),
    )
    checks.check(
        "mutation-I-splits",
        "predicate I splits J_ok from J_bad fails",
        (i_ok != i_bad) is False,
    )
    checks.check(
        "mutation-J-equal",
        "predicate J_ok=J_bad fails",
        (j_ok == j_bad) is False,
    )
    checks.check(
        "mutation-mu-C-nonzero",
        "predicate mu(C)!=0 fails",
        (mass_c != 0) is False,
    )
    checks.check(
        "machine-status-contract",
        "required hypothetical and surface-status strings are present",
        'hypothetical_axiom_status: "C1 follow-on: J type does not force lock in supp(mu); admissibility stays a constraint on im J; not adopted"'
        in note
        and "actual_current_surface_status: bounded-support" in note,
    )
    checks.check(
        "note-no-adoption",
        "note does not adopt C1, r=1/2, L_phys, pairing, or Tr",
        "Do not adopt C1" in note_norm
        and "Do not force `r=1/2`" in note_norm
        and "Do not adopt `L_phys`" in note_norm
        and "Do not put a pairing on `J`" in note_norm
        and "Do not import a Born compiler (no `Tr`)" in note_norm,
    )
    checks.check(
        "note-unit-and-model",
        "unit-count I=1 is a convention; declared mu is a model",
        "Unit-count `I=1` is a convention" in note_norm
        and "Record additivity does not force the unit" in note_norm
        and "declared `μ` is a model" in note_norm,
    )

    print("per_element: J_ok=(A,0) and J_bad=(C,0); labels {A,B,C}")
    print("per_site: window {x,y}; one occupied site on each lock")
    print("per_mode: unit-count I versus displayed J; leftover image constraint")
    print("per_block: C1 type versus Record admissible; mu declared not derived")
    print("lattice_wide: checked and not executed — two-site window only")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
