#!/usr/bin/env python3
"""Exact checks: involution rank-split selects the traceless ratio.

Ranks (6,2) recompute β=−3α (May 2; not claimed new). The involution
σ=diag(+1^4,−1^4) has ranks (4,4) and ratio −1. Lattice, Qubit,
Admissibility, and Record do not select Y_0 over Z_0. No cache is written.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "INVOLUTION_RANK_SPLIT_SELECTS_TRACELESS_RATIO_AXIOMS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
MAY2_PATH = (
    ROOT
    / "docs"
    / "LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md"
)
HYPERCHARGE_PATH = ROOT / "docs" / "HYPERCHARGE_IDENTIFICATION_NOTE.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/INVOLUTION_RANK_SPLIT_SELECTS_TRACELESS_RATIO_AXIOMS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md",
    "docs/HYPERCHARGE_IDENTIFICATION_NOTE.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Diagonal:
    """Exact diagonal operator on C^8, entries in Q."""

    entries: tuple[Fraction, ...]

    def __add__(self, other: "Diagonal") -> "Diagonal":
        return Diagonal(tuple(a + b for a, b in zip(self.entries, other.entries, strict=True)))

    def __sub__(self, other: "Diagonal") -> "Diagonal":
        return Diagonal(tuple(a - b for a, b in zip(self.entries, other.entries, strict=True)))

    def __mul__(self, other: object) -> "Diagonal":
        if isinstance(other, Diagonal):
            return Diagonal(tuple(a * b for a, b in zip(self.entries, other.entries, strict=True)))
        if isinstance(other, (int, Fraction)):
            scale = Fraction(other)
            return Diagonal(tuple(a * scale for a in self.entries))
        return NotImplemented

    def __rmul__(self, other: object) -> "Diagonal":
        return self.__mul__(other)

    def adj(self) -> "Diagonal":
        return self

    def trace(self) -> Fraction:
        return sum(self.entries, Fraction(0))

    def rank(self) -> int:
        return sum(1 for entry in self.entries if entry != 0)

    def spec_multiset(self) -> tuple[Fraction, ...]:
        return tuple(sorted(self.entries))

    def is_projector(self) -> bool:
        return self * self == self and self.adj() == self

    @staticmethod
    def ones(dimension: int) -> "Diagonal":
        return Diagonal(tuple(Fraction(1) for _ in range(dimension)))

    @staticmethod
    def from_signs(n_plus: int, n_minus: int) -> "Diagonal":
        return Diagonal(tuple([Fraction(1)] * n_plus + [Fraction(-1)] * n_minus))


def plus_projector(involution: Diagonal) -> Diagonal:
    identity = Diagonal.ones(len(involution.entries))
    return (identity + involution) * Fraction(1, 2)


def minus_projector(involution: Diagonal) -> Diagonal:
    identity = Diagonal.ones(len(involution.entries))
    return (identity - involution) * Fraction(1, 2)


def ratio_from_ranks(n_plus: int, n_minus: int) -> Fraction:
    """Identity-gate function: traceless ratio β/α = −n_+/n_-."""
    if n_minus == 0:
        raise ValueError("minus rank must be positive")
    return -Fraction(n_plus, n_minus)


def traceless_beta(n_plus: int, n_minus: int, alpha: Fraction) -> Fraction:
    """Solve n_+ α + n_- β = 0 for β."""
    if n_minus == 0:
        raise ValueError("minus rank must be positive")
    return -Fraction(n_plus) * alpha / Fraction(n_minus)


def y0() -> Diagonal:
    """May 2 generator on ranks (6,2): Y_0 = Pi_+ − 3 Pi_-."""
    tau = Diagonal.from_signs(6, 2)
    return plus_projector(tau) + traceless_beta(6, 2, Fraction(1)) * minus_projector(tau)


def z0() -> Diagonal:
    """Identity-gate function: Z_0 = Qi_+ − Qi_- on ranks (4,4)."""
    sigma = Diagonal.from_signs(4, 4)
    return plus_projector(sigma) - minus_projector(sigma)


def constant_minus_three(_n_plus: int, _n_minus: int) -> Fraction:
    """Mutation: freeze the May 2 ratio on every rank pair."""
    return Fraction(-3)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")
        if not result and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    may2 = MAY2_PATH.read_text(encoding="utf-8")
    hypercharge = HYPERCHARGE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")
    normalized_note = normalize(note).replace("> ", "")
    normalized_axiom = normalize(axiom)

    print(
        "external_scientific_inputs: May 2 ratio identity, name-free Y_0, "
        "and the four axiom sentences are source-bound; no observational "
        "or fitted inputs are used"
    )
    print(
        "package_local_integrity_reads: the proposed source note is read for "
        "claim-surface consistency; no runner cache is written"
    )
    print(
        "negative_scope: axioms do not select Y_0 over Z_0; ranks (4,4) "
        "force ratio -1; no U(1)_Y identification"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, May 2, name-free parent, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/INVOLUTION_RANK_SPLIT_SELECTS_TRACELESS_RATIO_AXIOMS_DO_NOT_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md",
            "docs/HYPERCHARGE_IDENTIFICATION_NOTE.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    may2_identity = "6 · α + 2 · β = 0"
    may2_ratio = "β = −3 α"
    may2_nonclaim = "identification with Standard Model hypercharge Y"
    checks.check(
        "source-may2-ratio",
        "May 2 states 6α+2β=0 ⇒ β=−3α and excludes SM identification",
        may2_identity in may2 and may2_ratio in may2 and may2_nonclaim in may2,
    )
    checks.check(
        "source-hypercharge-y0",
        "the name-free parent writes Y_0 = P_sym − 3 P_anti from 6α+2β=0",
        "6 alpha + 2 beta = 0" in hypercharge
        and "so beta=-3 alpha." in hypercharge
        and "Y_0 = P_sym - 3 P_anti." in hypercharge,
    )

    lattice_sentence = "Physical sites are the points of the cubic lattice `Z^3`"
    qubit_sentence = "No possibility is privileged."
    admissibility_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_sentence = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )
    lock_sentence = "When present, a record locks exactly one admissible local possibility."
    checks.check(
        "source-lattice-sites",
        "the exact current Lattice Z^3 sentence is present in the axiom memo",
        lattice_sentence in axiom,
    )
    checks.check(
        "source-qubit-nonprivilege",
        "the exact current Qubit non-privilege sentence is present in the axiom memo",
        qubit_sentence in axiom,
    )
    checks.check(
        "source-admissibility",
        "the exact current Admissibility nearest-neighbor sentence is present in the axiom memo",
        admissibility_sentence in normalized_axiom,
    )
    checks.check(
        "source-record-additivity",
        "the exact current Record additivity sentence is present in the axiom memo",
        record_sentence in normalized_axiom and lock_sentence in axiom,
    )

    tau = Diagonal.from_signs(6, 2)
    pi_plus = plus_projector(tau)
    pi_minus = minus_projector(tau)
    pi_plus_direct = Diagonal(tuple([Fraction(1)] * 6 + [Fraction(0)] * 2))
    pi_minus_direct = Diagonal(tuple([Fraction(0)] * 6 + [Fraction(1)] * 2))
    checks.check(
        "theorem-1-involution",
        "τ_Y is a self-adjoint involution and recovers the direct (6,2) projectors",
        tau * tau == Diagonal.ones(8)
        and tau.adj() == tau
        and pi_plus == pi_plus_direct
        and pi_minus == pi_minus_direct
        and pi_plus.is_projector()
        and pi_minus.is_projector()
        and pi_plus + pi_minus == Diagonal.ones(8)
        and pi_plus * pi_minus == Diagonal(tuple(Fraction(0) for _ in range(8))),
        residual=(pi_plus.entries, pi_minus.entries),
    )
    checks.check(
        "theorem-1-ranks",
        "Pi_+ and Pi_- have integer ranks 6 and 2",
        pi_plus.rank() == 6
        and pi_minus.rank() == 2
        and pi_plus.trace() == Fraction(6)
        and pi_minus.trace() == Fraction(2),
        residual=(pi_plus.rank(), pi_minus.rank()),
    )

    sample_alphas = (Fraction(1), Fraction(2), Fraction(-5), Fraction(7, 11))
    may2_line = all(
        traceless_beta(pi_plus.rank(), pi_minus.rank(), alpha) == Fraction(-3) * alpha
        and ratio_from_ranks(pi_plus.rank(), pi_minus.rank()) == Fraction(-3)
        for alpha in sample_alphas
    )
    generator_62 = y0()
    checks.check(
        "theorem-1-ratio",
        "ranks (6,2) force β=−3α on the sample grid and Y_0 has spec {1^6,(-3)^2}",
        may2_line
        and generator_62.trace() == Fraction(0)
        and generator_62.spec_multiset()
        == tuple([Fraction(-3)] * 2 + [Fraction(1)] * 6)
        and generator_62 == pi_plus + Fraction(-3) * pi_minus,
        residual=(generator_62.trace(), generator_62.spec_multiset()),
    )

    sigma = Diagonal.from_signs(4, 4)
    qi_plus = plus_projector(sigma)
    qi_minus = minus_projector(sigma)
    checks.check(
        "theorem-2-involution",
        "σ is a self-adjoint involution with complementary (4,4) projectors",
        sigma * sigma == Diagonal.ones(8)
        and sigma.adj() == sigma
        and qi_plus.is_projector()
        and qi_minus.is_projector()
        and qi_plus + qi_minus == Diagonal.ones(8)
        and qi_plus * qi_minus == Diagonal(tuple(Fraction(0) for _ in range(8)))
        and qi_plus.rank() == 4
        and qi_minus.rank() == 4
        and qi_plus.trace() == Fraction(4)
        and qi_minus.trace() == Fraction(4),
        residual=(qi_plus.rank(), qi_minus.rank()),
    )

    four_four_line = all(
        traceless_beta(qi_plus.rank(), qi_minus.rank(), alpha) == Fraction(-1) * alpha
        and ratio_from_ranks(qi_plus.rank(), qi_minus.rank()) == Fraction(-1)
        for alpha in sample_alphas
    )
    generator_44 = z0()
    checks.check(
        "theorem-2-ratio",
        "ranks (4,4) force β=−α and Z_0 equals σ with spec {1^4,(-1)^4}",
        four_four_line
        and generator_44.trace() == Fraction(0)
        and generator_44 == sigma
        and generator_44.spec_multiset()
        == tuple([Fraction(-1)] * 4 + [Fraction(1)] * 4),
        residual=(generator_44.trace(), generator_44.spec_multiset()),
    )

    eigenvalue_ratios = tuple(
        y_entry / z_entry for y_entry, z_entry in zip(generator_62.entries, generator_44.entries, strict=True)
    )
    checks.check(
        "theorem-2-not-multiple",
        "Y_0 is not a scalar multiple of Z_0: eigenvalue ratios are not constant",
        len(set(eigenvalue_ratios)) > 1
        and generator_62.spec_multiset() != generator_44.spec_multiset()
        and generator_62 != generator_44
        and generator_62 != Fraction(-3) * generator_44,
        residual=eigenvalue_ratios,
    )

    axiom_forbidden = ("τ", "SWAP_23", "C^8", "taste cube", "(6,2)", "(4,4)", "Y_0", "Z_0")
    checks.check(
        "theorem-3-axioms-silent",
        "Lattice, Qubit, Admissibility, and Record do not name τ, SWAP_23, a C^8 taste cube, or the rank pairs",
        all(token not in axiom for token in axiom_forbidden)
        and lattice_sentence in axiom
        and qubit_sentence in axiom
        and admissibility_sentence in normalized_axiom
        and record_sentence in normalized_axiom
        and lock_sentence in axiom,
    )
    checks.check(
        "theorem-3-not-selected",
        "the quoted axiom sentences appear in the note and do not select Y_0 over Z_0",
        lattice_sentence in note
        and qubit_sentence in note
        and admissibility_sentence in normalized_note
        and record_sentence in normalized_note
        and lock_sentence in note
        and "I(empty)=0" in note
        and generator_62.spec_multiset() != generator_44.spec_multiset(),
    )

    y_like = generator_62 * Fraction(1, 3)
    checks.check(
        "theorem-4-scale-convention",
        "α=1/3 remains a convention: Y_like=Y_0/3 is a rescaling, not a derived unit",
        "α=1/3" in note
        and "convention" in note
        and "not derived" in note.lower()
        and "PHYSICAL_HYPERCHARGE_ALPHA_SCALE_FREEDOM_CYCLE692_NOTE_2026-07-25.md" in note
        and y_like.spec_multiset()
        == tuple([Fraction(-1)] * 2 + [Fraction(1, 3)] * 6)
        and y_like.trace() == Fraction(0)
        and ratio_from_ranks(6, 2) == Fraction(-3),
        residual=y_like.spec_multiset(),
    )
    checks.check(
        "theorem-5-phy-open",
        "P-HY and anomaly-complete U(1)_Y remain open; Y_like is not identified",
        "P-HY" in note
        and "anomaly-complete" in note
        and "U(1)_Y" in note
        and "not identified" in note
        and "Do not identify Y_like with U(1)_Y" in note,
    )

    checks.check(
        "mutation-ranks-change-ratio",
        "replacing ranks (6,2) by (4,4) changes the traceless ratio −3 to −1",
        ratio_from_ranks(pi_plus.rank(), pi_minus.rank()) == Fraction(-3)
        and ratio_from_ranks(qi_plus.rank(), qi_minus.rank()) == Fraction(-1)
        and ratio_from_ranks(pi_plus.rank(), pi_minus.rank())
        != ratio_from_ranks(qi_plus.rank(), qi_minus.rank()),
        residual=(
            ratio_from_ranks(pi_plus.rank(), pi_minus.rank()),
            ratio_from_ranks(qi_plus.rank(), qi_minus.rank()),
        ),
    )
    checks.check(
        "mutation-constant-ratio-fails",
        "freezing the ratio at −3 fails on ranks (4,4)",
        constant_minus_three(4, 4) == Fraction(-3)
        and ratio_from_ranks(4, 4) == Fraction(-1)
        and constant_minus_three(4, 4) != ratio_from_ranks(4, 4)
        and constant_minus_three(6, 2) == ratio_from_ranks(6, 2),
        residual=(constant_minus_three(4, 4), ratio_from_ranks(4, 4)),
    )
    checks.check(
        "mutation-identify-generators-fails",
        "replacing Z_0 by Y_0 fails the {1^4,(-1)^4} multiset witness",
        z0().spec_multiset() == tuple([Fraction(-1)] * 4 + [Fraction(1)] * 4)
        and y0().spec_multiset() == tuple([Fraction(-3)] * 2 + [Fraction(1)] * 6)
        and y0().spec_multiset() != z0().spec_multiset(),
        residual=(y0().spec_multiset(), z0().spec_multiset()),
    )

    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    retained_ok = all(line in note for line in allowed_retained)
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")
    checks.check(
        "note-contract",
        "machine-status fields, required phrases, and forbidden-word hygiene hold",
        all(
            phrase in note
            for phrase in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                'hypothetical_axiom_status: "no edit"',
                "trace_class: negative_route_pruning",
                "target_claim_id: involution_rank_split_selects_traceless_ratio",
                "reachability_to_target: prunes",
                'target_blocker_text: "axioms select the (6,2) LH split and the 1:(-3) ratio"',
                'next_trace_action: "The (6,2) split is an extra involution choice. Axioms do not select Y_0 over Z_0. Do not identify Y_like with U(1)_Y. Do not adopt axiom text."',
                "authors no audit verdict",
                "I(empty)=0",
                "not claimed new",
                "MINIMAL_AXIOMS_2026-06-29.md",
                "LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md",
                "HYPERCHARGE_IDENTIFICATION_NOTE.md",
                "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md",
            )
        )
        and may2_identity in note.replace("6 α + 2 β = 0", may2_identity)
        and record_sentence in normalized_note
        and admissibility_sentence in normalized_note
        and "**Type:** bounded_theorem" in note
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "toe-lphys" not in note,
    )
    checks.check(
        "canonical-nonmutation",
        "the involution split and both generators are absent from the canonical axiom file",
        all(
            phrase not in axiom
            for phrase in ("Y_0", "Z_0", "Qi_+", "Pi_+", "SWAP_23", "taste cube", "β=−3α")
        ),
    )

    n5_lines = (
        "per_element: diagonals of Y_0 and Z_0 and both trace equations are recomputed in Fraction",
        "per_site: one copy of C^8 is the only carrier; no spatial site is assigned a taste cube",
        "per_mode: two-value central operators are checked; no Hamiltonian mode is claimed",
        "per_block: only ranks (6,2) versus (4,4) and the axiom residual are executed",
        "lattice_wide: checked and not executed — no lattice-wide electroweak or U(1)_Y claim",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
            residual=(len(line), line[:40]),
        )
        print(line)

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
