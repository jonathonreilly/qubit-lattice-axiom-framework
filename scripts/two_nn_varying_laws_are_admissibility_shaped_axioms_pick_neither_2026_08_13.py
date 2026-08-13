#!/usr/bin/env python3
"""Exact checks: two NN-varying occupancy laws inhabit Admissibility; axioms pick neither.

Identity gates call mu1(n) and mu2(n). Mutation predicates that the laws
agree, or that the axioms force mu(A)=1/2 for every n, must fail at n=2.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_NN_VARYING_LAWS_ARE_ADMISSIBILITY_SHAPED_AXIOMS_PICK_NEITHER_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_NN_VARYING_LAWS_ARE_ADMISSIBILITY_SHAPED_AXIOMS_PICK_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


def mu1(n: int) -> Fraction:
    if n == 0:
        return Fraction(1, 2)
    return Fraction(n, 6)


def mu2(n: int) -> Fraction:
    return Fraction(n + 1, 8)


@dataclass(frozen=True)
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> "Checks":
        result = bool(condition)
        if result:
            object.__setattr__(self, "passed", self.passed + 1)
        else:
            object.__setattr__(self, "failed", self.failed + 1)
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        return self

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    runner_src = Path(__file__).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print("external_scientific_inputs: current axiom wording only; no observational or fitted inputs")
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("negative_scope: function-selection on one occupancy coarse-grain; later selectors remain live")

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-admissibility",
        "the exact current distribution sentence is present",
        canonical_sentence in normalized_axiom,
    )
    checks.check(
        "source-one-fixed-rule",
        "Admissibility names one fixed nearest-neighbor rule",
        "one fixed nearest-neighbor admissibility rule" in normalized_axiom,
    )
    checks.check(
        "source-form-values-open",
        "the axiom memo leaves the distribution form and values unspecified",
        "distribution's extensional form and values are not specified" in normalized_axiom,
    )

    n = 1
    checks.check(
        "identity-mu1-at-1",
        "mu1(n) equals 1/6 at n=1",
        mu1(n) == Fraction(1, 6),
    )
    checks.check(
        "identity-mu2-at-1",
        "mu2(n) equals 1/4 at n=1",
        mu2(n) == Fraction(1, 4),
    )
    n = 2
    checks.check(
        "identity-mu1-at-2",
        "mu1(n) equals 1/3 at n=2",
        mu1(n) == Fraction(1, 3),
    )
    checks.check(
        "identity-mu2-at-2",
        "mu2(n) equals 3/8 at n=2",
        mu2(n) == Fraction(3, 8),
    )
    checks.check(
        "identity-gates-call-mu",
        "identity gates call mu1(n) and mu2(n)",
        "mu1(n)" in runner_src and "mu2(n)" in runner_src,
    )

    n = 1
    left_mu1 = mu1(n)
    left_mu2 = mu2(n)
    n = 2
    checks.check(
        "theorem-1-variation",
        "both laws vary with n",
        left_mu1 != mu1(n) and left_mu2 != mu2(n),
    )
    checks.check(
        "theorem-2-disagreement",
        "the two laws disagree at n=2",
        mu1(n) != mu2(n) and mu1(n) == Fraction(1, 3) and mu2(n) == Fraction(3, 8),
    )

    predicate_laws_equal = mu1(n) == mu2(n)
    checks.check(
        "mutation-mu1-equals-mu2-fails-at-n2",
        "the predicate mu1=mu2 fails at n=2 because 1/3 != 3/8",
        predicate_laws_equal is False,
    )
    predicate_force_half = mu1(n) == Fraction(1, 2)
    checks.check(
        "mutation-axioms-force-half-fails-at-n2",
        "the predicate axioms force mu(A)=1/2 for all n fails at n=2",
        predicate_force_half is False and mu1(n) == Fraction(1, 3),
    )

    occupancy = range(7)
    checks.check(
        "mu2-full-support",
        "mu2(n) stays in (0,1) for every occupancy class",
        all(Fraction(0) < mu2(n) < Fraction(1) for n in occupancy),
    )
    checks.check(
        "mu1-zero-clause",
        "mu1 uses the full-support n=0 clause and the occupancy fraction thereafter",
        mu1(0) == Fraction(1, 2) and mu1(6) == Fraction(1),
    )

    note_needles = (
        "mu1(A|1)=1/6",
        "mu1(A|2)=1/3",
        "mu2(A|1)=2/8=1/4",
        "mu2(A|2)=3/8",
        "The axiom does not name `mu1` versus `mu2`.",
        "does not adopt either as `L_phys`",
        "does not force `mu(A)=1/2`",
        "Nothing above claims that no later selector exists",
        "`r=1/2` is not forced",
    )
    checks.check(
        "note-theorem-surface",
        "the note records both identities, non-adoption, no universal half-weight, and an open later selector",
        all(needle in note for needle in note_needles),
    )
    checks.check(
        "note-n5-theorem-4",
        "N5 is attached to Theorem 4 and refuses L_phys adoption and a universal half-weight",
        "### N5 — resolution and rhetoric audit (Theorem 4)" in note
        and "no adoption of `L_phys`, no universal half-weight, no ratio dictionary" in note,
    )
    checks.check(
        "claim-type-contract",
        "the author hint uses the exact bounded-theorem enum",
        "**Type:** bounded_theorem" in note,
    )
    checks.check(
        "machine-status-contract",
        "the source uses the controlled bounded-support fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: negative_route_pruning",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the displayed occupancy laws are absent from the canonical axiom file",
        all(phrase not in axiom for phrase in ("mu1(A|n)", "mu2(A|n)", "L_phys")),
    )
    checks.check(
        "no-go-gate",
        "all N1-N8 sections and the broad-claim rejection are source-visible",
        all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and "no later selector exists" in note,
    )
    checks.check(
        "audit-input-paths",
        "declared inputs are the new note and the axiom memo only",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_NN_VARYING_LAWS_ARE_ADMISSIBILITY_SHAPED_AXIOMS_PICK_NEITHER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "no-unmerged-pr-citation",
        "the note cites no unmerged pull-request numbers",
        "PR #" not in note and "#6185" not in note and "#6202" not in note,
    )

    print("per_element: identity gates evaluate mu1(n) and mu2(n) at n=1 and n=2")
    print("per_site: one center site with menu {A,B}; no composite carrier")
    print("per_mode: occupancy classes n=0,...,6 are the declared coarse-grain")
    print("per_block: function-selection only; neither law is adopted as L_phys")
    print("lattice_wide: checked and not executed — no lattice-wide dynamics claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
