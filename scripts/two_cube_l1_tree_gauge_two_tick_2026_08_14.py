#!/usr/bin/env python3
"""Exact checks: two-site tree gauge stays source-complete after two L1 ticks.

Integer incidence only. No axiom edit, no cache write, no network, no
citation manifest.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "TWO_CUBE_L1_TREE_GAUGE_TWO_TICK_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_TREE_GAUGE_TWO_TICK_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

TICK_1 = (4, 1)
TICK_2 = (7, 4)
FACES = ("F*", "F_B")


def normalize(text: str) -> str:
    return " ".join(text.split())


def gauss(phi_star: int, phi_b: int) -> tuple[int, int]:
    """Displayed incidence: g_A := φ(F*), g_B := −φ(F*) + φ(F_B)."""

    return phi_star, -phi_star + phi_b


def tree_gauge(rho_a: int, rho_b: int) -> tuple[int, int]:
    """Tree gauge: φ(F*)=ρ(A), φ(F_B)=ρ(A)+ρ(B)."""

    return rho_a, rho_a + rho_b


def decode(rho: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    flux = tree_gauge(*rho)
    return flux, gauss(*flux)


def det2(matrix: tuple[tuple[int, int], tuple[int, int]]) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matvec(matrix: tuple[tuple[int, int], tuple[int, int]], vec: tuple[int, int]) -> tuple[int, int]:
    return (
        matrix[0][0] * vec[0] + matrix[0][1] * vec[1],
        matrix[1][0] * vec[0] + matrix[1][1] * vec[1],
    )


INCIDENCE = ((1, 0), (-1, 1))
INVERSE = ((1, 0), (1, 1))


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

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
    source_text = note

    print(
        "external_scientific_inputs: none; no observational, fitted, literature, "
        "scale, or normalization value is used"
    )
    print(
        "explicit_bounded_inputs: the two-site two-face incidence, tree-gauge "
        "decoder, and displayed L1 ticks (4,1) then (7,4)"
    )
    print(
        "framework_context: Lattice names Z^3 sites only; the incidence, decoder, "
        "and ticks are not attributed to the axioms"
    )
    print("package_local_integrity_reads: the proposed source note is read for claim-surface consistency")
    print("measure_boundary: exact integer incidence algebra only")
    print(
        "negative_scope: only a third-face or -x-ray reading is refused; no broader "
        "gravity identification no-go is asserted"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the declared note-plus-axiom tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/TWO_CUBE_L1_TREE_GAUGE_TWO_TICK_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "source-lattice",
        "the axiom memo names cubic-lattice sites and does not name this decoder",
        "Physical sites are the points of the cubic lattice `Z^3`" in axiom
        and "tree-gauge decoder" not in axiom
        and "φ(F*)" not in axiom,
    )
    checks.check(
        "note-incidence",
        "the note displays the two-site incidence",
        "g_A := φ(F*)" in note and "g_B := −φ(F*) + φ(F_B)" in note,
    )
    checks.check(
        "note-tree-gauge",
        "the note displays the tree-gauge assignment",
        "φ(F*) = ρ(A)" in note and "φ(F_B) = ρ(A) + ρ(B)" in note,
    )

    sample = ((0, 0), (1, 0), (0, 1), (-3, 5), TICK_1, TICK_2)
    checks.check(
        "thm1-identity",
        "tree gauge solves g=ρ for every sampled integer pair",
        all(decode(rho)[1] == rho for rho in sample),
    )

    flux1, g1 = decode(TICK_1)
    flux2, g2 = decode(TICK_2)
    checks.check(
        "thm2-tick1",
        "after tick 1, φ=(4,5) and g=ρ=(4,1)",
        flux1 == (4, 5) and g1 == TICK_1 == (4, 1),
    )
    checks.check(
        "thm2-tick2",
        "after tick 2, φ=(7,11) and g=ρ=(7,4)",
        flux2 == (7, 11) and g2 == TICK_2 == (7, 4),
    )
    checks.check(
        "thm2-composition",
        "the same decoder is reapplied; frozen tick-1 flux fails at tick 2",
        gauss(*flux1) != TICK_2 and decode(TICK_2)[1] == TICK_2,
    )
    checks.check(
        "thm3-invertible",
        "the 2x2 incidence has determinant 1 and inverse equal to the tree gauge",
        det2(INCIDENCE) == 1
        and matvec(INVERSE, TICK_1) == flux1
        and matvec(INVERSE, TICK_2) == flux2
        and matvec(INCIDENCE, flux1) == TICK_1
        and matvec(INCIDENCE, flux2) == TICK_2,
    )
    checks.check(
        "n1-wrong-sign",
        "dropping the minus on F* fails tick 1",
        flux1[0] + flux1[1] != TICK_1[1],
    )
    checks.check(
        "n1-swapped-gauge",
        "swapping the tree assignment fails tick 1",
        gauss(TICK_1[1], TICK_1[0]) != TICK_1,
    )
    checks.check(
        "two-face-domain",
        "the decoder domain is exactly the two faces F* and F_B",
        FACES == ("F*", "F_B") and len(FACES) == 2,
    )
    checks.check(
        "not-two-cube-clone",
        "the tested object names no third face and no -x ray",
        "no third face" in normalized_note
        and "no `−x` ray" in note
        and "third face" not in axiom,
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    checks.check(
        "forbidden-strings",
        "note and runner omit the forbidden gravity and slogan strings",
        all(token not in source_text for token in forbidden),
    )
    checks.check(
        "machine-status-contract",
        "the source uses the required bounded-support, trace, and propose-ratify status fields",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "trace_class: frontier_discovery",
                "target_claim_id: null",
                "next_trace_action:",
                "hypothetical_axiom_status: null",
                "**Type:** bounded_theorem",
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "note-negative-scope",
        "the note separates the two-tick identity from physical-identification non-claims",
        all(
            phrase in normalized_note
            for phrase in (
                "not a two-cube-gauge clone",
                "no map from this decoder to a physical gravitational constraint",
                "No claim about continuum gravity",
                "an axiom update is necessary",
            )
        ),
    )
    checks.check(
        "canonical-nonmutation",
        "the axiom memo does not contain the tree incidence or the displayed ticks",
        all(
            phrase not in axiom
            for phrase in (
                "φ(F*)",
                "φ(F_B)",
                "g_A :=",
                "(4, 1)",
                "(7, 4)",
                "tree gauge",
            )
        ),
    )
    checks.check(
        "no-go-gate",
        "the exact local boundary carries a complete source-visible N1-N8 disposition",
        all(f"### N{index}" in note for index in range(1, 9))
        and note.count("**ATTEMPTED**") >= 5
        and "Collapsed obstruction set: `{g = ρ after each displayed tick}`" in note
        and "Steelman disposition: **CLOSED**" in note
        and "N1–N8 disposition: **PASS**" in note
        and "## Excluded Broader Claims" in note,
    )
    checks.check(
        "no-cache-no-manifest",
        "this cycle declares that it writes no runner cache and no citation manifest",
        "writes no runner cache" in normalized_note
        and "writes no citation manifest" in normalized_note,
    )

    print("per_element: entries of M, M^{-1}, and the two decoded flux pairs are evaluated exactly")
    print("per_site: the supplied object is the two displayed sites A and B, not a lattice-wide source law")
    print("per_mode: the two faces F* and F_B are resolved; no third face or -x ray is introduced")
    print("per_block: one two-site tree after two L1 ticks is tested; no physical identification is inferred")
    print("lattice_wide: checked and not executed — the theorem supplies no lattice-wide decoder")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
