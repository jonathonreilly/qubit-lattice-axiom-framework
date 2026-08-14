#!/usr/bin/env python3
"""Finite content-support and formation-extension type separation.

The paired note is
docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md.

The finite menu, probability vector, and two-label extension fiber are declared
test objects. No full-lattice history, formation process, or rate is modeled.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_SUPPORT_CONSTRAINS_CONTENT_NOT_FORMATION_SITE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

MENU = frozenset({"A", "B", "C"})
LABELS = frozenset({"x", "y"})
MU = {"A": Fraction(1, 3), "B": Fraction(2, 3), "C": Fraction(0)}


def normalize(text: str) -> str:
    return " ".join(text.split())


def is_probability(measure: dict[str, Fraction]) -> bool:
    return (
        set(measure) == MENU
        and all(mass >= 0 for mass in measure.values())
        and sum(measure.values(), Fraction(0)) == 1
    )


def support_of(measure: dict[str, Fraction]) -> frozenset[str]:
    return frozenset(label for label, mass in measure.items() if mass > 0)


@dataclass(frozen=True)
class FormationExtension:
    """A finite extension over a held-fixed conditional content law."""

    formed: frozenset[str]
    locks: tuple[tuple[str, str], ...]

    def lock_map(self) -> dict[str, str]:
        return dict(self.locks)

    def is_well_typed(self, measure: dict[str, Fraction]) -> bool:
        lock_map = self.lock_map()
        return (
            bool(self.formed)
            and self.formed <= LABELS
            and len(lock_map) == len(self.locks)
            and frozenset(lock_map) == self.formed
            and all(content in support_of(measure) for content in lock_map.values())
        )

    def multiplicity(self) -> int:
        return len(self.formed)


E_X = FormationExtension(frozenset({"x"}), (("x", "A"),))
E_Y = FormationExtension(frozenset({"y"}), (("y", "A"),))
E_XY = FormationExtension(
    frozenset({"x", "y"}), (("x", "A"), ("y", "B"))
)


def content_projection(
    extension: FormationExtension, measure: dict[str, Fraction]
) -> tuple[tuple[str, Fraction], ...]:
    """Forget the extension data and retain only the supplied content law."""
    if not extension.is_well_typed(measure):
        raise ValueError("projection requires a well-typed formation extension")
    return tuple(sorted(measure.items()))


def enumerate_extensions(
    measure: dict[str, Fraction],
) -> tuple[FormationExtension, ...]:
    """Enumerate the complete nonempty extension fiber on the two labels."""
    allowed = tuple(sorted(support_of(measure)))
    extensions: list[FormationExtension] = []
    for size in range(1, len(LABELS) + 1):
        for sites in combinations(sorted(LABELS), size):
            for contents in product(allowed, repeat=size):
                extensions.append(
                    FormationExtension(
                        frozenset(sites), tuple(zip(sites, contents, strict=True))
                    )
                )
    return tuple(extensions)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    normalized_note = normalize(note)
    normalized_axiom = normalize(axiom)

    print("Finite conditional-content / formation-extension separation")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: supplied finite menu and abstract two-label extension fiber; "
        "no full Z^3 history and no rate object"
    )

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-unique-normalized",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(not Path(path).is_absolute() and ".." not in Path(path).parts for path in AUDIT_INPUT_PATHS),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)

    distribution_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    lock_sentence = (
        "When present, a record locks exactly one admissible local possibility."
    )
    checks.check(
        "source-distribution-sentence-current",
        distribution_sentence in normalized_axiom,
    )
    checks.check(
        "source-occurrence-sentence-current",
        "Records form." in axiom,
    )
    checks.check(
        "source-lock-sentence-current",
        lock_sentence in normalized_axiom,
    )
    checks.check(
        "source-conditional-content-typing-current",
        "conditional on formation at that site" in normalized_axiom
        and "it does not supply the formation site, probability, or rate"
        in normalized_axiom,
    )
    checks.check(
        "source-finite-support-reading-current",
        "on finite menus, exactly the possibilities of nonzero probability"
        in normalized_axiom,
    )

    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split(
        "## Qualification", 1
    )[0]
    checks.check(
        "post-reset-record-has-unreadable-absence",
        "A site with no record cannot be read." in normalize(record_section),
    )
    checks.check(
        "post-reset-record-has-no-scalar-or-additivity-clause",
        "I(empty)" not in record_section
        and "scalar readout" not in record_section
        and "additive" not in record_section,
    )

    checks.check("finite-law-normalized", is_probability(MU))
    checks.check(
        "finite-law-exact-masses",
        MU == {
            "A": Fraction(1, 3),
            "B": Fraction(2, 3),
            "C": Fraction(0),
        },
    )
    support = support_of(MU)
    checks.check("theorem1-support-is-a-b", support == frozenset({"A", "B"}))
    checks.check("theorem1-c-is-not-lockable", "C" not in support)
    checks.check("theorem1-a-and-b-are-lockable", {"A", "B"} <= support)

    positive_c_mutation = {
        "A": Fraction(1, 3),
        "B": Fraction(1, 3),
        "C": Fraction(1, 3),
    }
    checks.check(
        "mutation-positive-c-defeats-exclusion",
        is_probability(positive_c_mutation)
        and "C" in support_of(positive_c_mutation),
    )
    zero_a_mutation = {
        "A": Fraction(0),
        "B": Fraction(2, 3),
        "C": Fraction(1, 3),
    }
    checks.check(
        "mutation-zero-a-removes-a-from-support",
        is_probability(zero_a_mutation)
        and "A" not in support_of(zero_a_mutation),
    )

    checks.check("extension-x-well-typed", E_X.is_well_typed(MU))
    checks.check("extension-y-well-typed", E_Y.is_well_typed(MU))
    checks.check("extension-xy-well-typed", E_XY.is_well_typed(MU))
    projection_x = content_projection(E_X, MU)
    projection_y = content_projection(E_Y, MU)
    projection_xy = content_projection(E_XY, MU)
    checks.check(
        "theorem2-site-distinct-extensions",
        E_X != E_Y and E_X.formed == {"x"} and E_Y.formed == {"y"},
    )
    checks.check(
        "theorem2-same-content-projection",
        projection_x == projection_y == tuple(sorted(MU.items())),
    )
    checks.check(
        "theorem3-multiplicity-distinct-extensions",
        E_X.multiplicity() == 1
        and E_XY.multiplicity() == 2
        and E_X.multiplicity() != E_XY.multiplicity(),
    )
    checks.check(
        "theorem3-same-content-projection",
        projection_x == projection_xy == tuple(sorted(MU.items())),
    )
    complete_fiber = enumerate_extensions(MU)
    checks.check(
        "complete-fiber-has-eight-extensions",
        len(complete_fiber) == 8
        and len(set(complete_fiber)) == 8
        and all(extension.is_well_typed(MU) for extension in complete_fiber),
    )
    checks.check(
        "complete-fiber-site-sets-and-multiplicities",
        {extension.formed for extension in complete_fiber}
        == {frozenset({"x"}), frozenset({"y"}), frozenset({"x", "y"})}
        and {extension.multiplicity() for extension in complete_fiber} == {1, 2},
    )

    empty_extension = FormationExtension(frozenset(), ())
    illicit_c_extension = FormationExtension(
        frozenset({"x"}), (("x", "C"),)
    )
    mismatched_lock_extension = FormationExtension(
        frozenset({"x"}), (("y", "A"),)
    )
    duplicate_lock_extension = FormationExtension(
        frozenset({"x"}), (("x", "A"), ("x", "B"))
    )
    checks.check(
        "mutation-empty-extension-rejected",
        not empty_extension.is_well_typed(MU),
    )
    checks.check(
        "mutation-zero-mass-lock-rejected",
        not illicit_c_extension.is_well_typed(MU),
    )
    checks.check(
        "mutation-lock-domain-mismatch-rejected",
        not mismatched_lock_extension.is_well_typed(MU),
    )
    checks.check(
        "mutation-duplicate-site-lock-rejected",
        not duplicate_lock_extension.is_well_typed(MU),
    )

    machine_markers = (
        "actual_current_surface_status: bounded-support",
        "target_claim_type: bounded_theorem",
        "claim_type_reason:",
        "trace_class: negative_route_pruning",
        "target_claim_id: record_formation_site_and_multiplicity_rule",
        "target_blocker_text:",
        "source_of_blocker_text: handoff",
        "reachability_to_target: prunes",
        "artifact_role: theorem",
        "next_trace_action:",
        "conditional_surface_status:",
        "hypothetical_axiom_status: no edit",
        "admitted_observation_status: null",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    checks.check(
        "note-machine-status-complete",
        all(marker in note for marker in machine_markers),
    )
    checks.check(
        "note-one-hop-dependency-current",
        "upstream_dependencies:\n  - minimal_axioms" in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note,
    )
    checks.check(
        "note-does-not-claim-two-vertex-z3-fragment",
        "do not form an induced physical fragment of `Z^3`" in normalized_note
        and "every site has six nearest neighbors" in normalized_note,
    )
    checks.check(
        "note-distinguishes-multiplicity-from-rate",
        "Multiplicity is a cardinality, not a rate." in note
        and "Distinct extension cardinalities do not constitute distinct rates."
        in note,
    )
    checks.check(
        "note-post-reset-absence-boundary",
        "is never passed to a readout map" in normalized_note
        and "is not assigned a scalar" in normalized_note
        and "Absence is unread and receives no scalar value." in normalized_note,
    )
    checks.check(
        "note-no-go-n1-through-n8",
        all(f"### N{index}" in note for index in range(1, 9)),
    )
    checks.check(
        "note-no-go-route-enumeration",
        note.count("**ATTEMPTED**") >= 5
        and "Hamiltonian, stochastic kernel" in note
        and "clocked counting process" in note,
    )
    checks.check(
        "note-steelman-accepts-full-rule-route",
        "The strongest objection" in normalized_note
        and "Correct: the finite witness cannot exclude that." in normalized_note,
    )
    checks.check(
        "note-live-partial-closure-routes",
        "Every such route remains live" in normalized_note,
    )

    n5_lines = (
        "per-element: executed — support and every displayed lock are checked",
        "per-site: executed — the two abstract labels x and y are enumerated",
        "per-mode: not applicable — no modal or spectral decomposition is used",
        "per-block: executed — only the declared two-label extension fiber is checked",
        "lattice-wide: not executed — no Z^3 history or formation process is claimed",
    )
    checks.check(
        "note-n5-five-line-certificate",
        all(line in note for line in n5_lines),
    )
    print("N5_CERTIFICATE:")
    for line in n5_lines:
        print(line)

    checks.check(
        "note-explicit-nonclaims",
        "It supplies no site selector, formation probability, process, time, or"
        in note
        and "No axiom, primitive, registry, or audit verdict is edited." in note,
    )
    checks.check(
        "note-does-not-upgrade-finite-scope",
        "This is a deliberately typed finite construction, not the definition of a framework state."
        in normalized_note
        and "no full Z^3 or rate closure" in normalized_note,
    )
    return 0 if checks.finish() == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
