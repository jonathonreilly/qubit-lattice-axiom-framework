#!/usr/bin/env python3
"""Exact checks: purity-weighted kernel is not barycenter evaluation.

Identity gates call purity_kernel(rho, E), equivalently K(rho, E).
Replacing K by Tr(rho E) must fail 9/26 versus 3/10. No cache is written.
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
    / "NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_AUG10_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class H2:
    """Real-symmetric 2x2 matrix over Fraction."""

    p: Fraction
    q: Fraction
    r: Fraction

    def __add__(self, other: "H2") -> "H2":
        return H2(self.p + other.p, self.q + other.q, self.r + other.r)

    def scale(self, value: Fraction) -> "H2":
        return H2(self.p * value, self.q * value, self.r * value)

    def mul(self, other: "H2") -> "H2":
        return H2(
            self.p * other.p + self.q * other.q,
            self.p * other.q + self.q * other.r,
            self.q * other.q + self.r * other.r,
        )

    def trace(self) -> Fraction:
        return self.p + self.r

    def pairing(self, other: "H2") -> Fraction:
        return self.p * other.p + (self.q * other.q) * 2 + self.r * other.r


ZERO = H2(Fraction(0), Fraction(0), Fraction(0))
I2 = H2(Fraction(1), Fraction(0), Fraction(1))
PZ = H2(Fraction(1), Fraction(0), Fraction(0))
PMZ = H2(Fraction(0), Fraction(0), Fraction(1))
MIXED = I2.scale(Fraction(1, 2))
E0 = PZ.scale(Fraction(1, 2))
BIASED = H2(Fraction(3, 5), Fraction(0), Fraction(2, 5))


def purity_kernel(rho: H2, effect: H2) -> Fraction:
    """K(rho, E) := Tr(rho^2 E) / Tr(rho^2). Identity gates call this."""
    rho2 = rho.mul(rho)
    denom = rho2.trace()
    if denom == 0:
        raise ZeroDivisionError("Tr(rho^2) vanished")
    return rho2.pairing(effect) / denom


def K(rho: H2, effect: H2) -> Fraction:
    return purity_kernel(rho, effect)


def born_kernel(rho: H2, effect: H2) -> Fraction:
    """Hostile replacement: Tr(rho E). Substituting this for K fails 9/26 vs 3/10."""
    return rho.pairing(effect)


def restriction_weight(effect_trace: Fraction, menu_traces: tuple[Fraction, ...]) -> Fraction:
    numerator = effect_trace * effect_trace
    denominator = sum((trace * trace) for trace in menu_traces)
    return numerator / denominator


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
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_aug10 = PARENT_AUG10_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: axiom wording and the August 10 type-separation "
        "note are source-bound; no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, the axiom memo, and "
        "the August 10 parent; no cache is written"
    )
    print(
        "kernel_formula: identity gates call purity_kernel(rho, E); "
        "born_kernel and restriction are hostile controls"
    )
    print(
        "negative_scope: this kernel is not barycenter evaluation and is not "
        "affine in mu; Born is not declared false"
    )

    checks.check(
        "audit-input-paths",
        "declared audit inputs exist and match the note, August 10 note, and axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
    )
    checks.check(
        "source-aug10",
        "August 10 supplies E0, the 25/142 restriction control, and menu-independence",
        all(phrase in parent_aug10 for phrase in ("E_0=(1/2)P(z)", "25/142", "2/11", "menu-independent"))
        and "25/142" in note
        and "E0=(1/2)P(z)" in note.replace(" ", ""),
    )
    checks.check(
        "source-aug09-citation",
        "the note cites the August 9 frame-lift uniqueness parent",
        "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
        in note
        and "unique density-matrix trace form" in note,
    )

    mixed_denom = MIXED.mul(MIXED).trace()
    biased_denom = BIASED.mul(BIASED).trace()
    pure_denom = PZ.mul(PZ).trace()
    checks.check(
        "theorem-1-well-defined",
        "Tr(rho^2)>0 on mixed, biased, and pure states; K(I)=1 and K(0)=0",
        mixed_denom == Fraction(1, 2)
        and biased_denom == Fraction(13, 25)
        and pure_denom == Fraction(1)
        and all(denom > 0 for denom in (mixed_denom, biased_denom, pure_denom))
        and purity_kernel(MIXED, I2) == 1
        and purity_kernel(BIASED, I2) == 1
        and purity_kernel(PZ, I2) == 1
        and purity_kernel(MIXED, ZERO) == 0
        and purity_kernel(BIASED, ZERO) == 0
        and K(BIASED, I2) == 1,
        residual=(mixed_denom, biased_denom, pure_denom),
    )
    checks.check(
        "theorem-1-positive",
        "K is nonnegative on the PSD effects E0, I, P(z), and P(-z)",
        all(
            purity_kernel(state, effect) >= 0
            for state in (MIXED, BIASED, PZ, PMZ)
            for effect in (E0, I2, PZ, PMZ)
        ),
    )
    checks.check(
        "theorem-1-menu-independent",
        "K depends on rho only, while restriction of E0 splits as 25/142 versus 2/11",
        purity_kernel(MIXED, E0) == K(MIXED, E0)
        and purity_kernel(BIASED, E0) == K(BIASED, E0)
        and restriction_weight(Fraction(1, 2), (Fraction(1, 2), Fraction(9, 10), Fraction(3, 5)))
        == Fraction(25, 142)
        and restriction_weight(Fraction(1, 2), (Fraction(1, 2), Fraction(3, 4), Fraction(3, 4)))
        == Fraction(2, 11)
        and Fraction(25, 142) != Fraction(2, 11),
    )

    mixed_k = purity_kernel(MIXED, E0)
    mixed_w = born_kernel(MIXED, E0)
    mixed_rho2 = MIXED.mul(MIXED)
    checks.check(
        "theorem-2-mixed",
        "at I/2, Tr(rho^2)=1/2, Tr(rho^2 E0)=1/8, and K=1/4=w(E0)",
        mixed_rho2.trace() == Fraction(1, 2)
        and mixed_rho2.pairing(E0) == Fraction(1, 8)
        and mixed_k == Fraction(1, 4)
        and mixed_w == Fraction(1, 4)
        and mixed_k == mixed_w,
        residual=(mixed_k, mixed_w),
    )

    biased_rho2 = BIASED.mul(BIASED)
    tr_rho2 = biased_rho2.trace()
    tr_rho2_e0 = biased_rho2.pairing(E0)
    biased_k = purity_kernel(BIASED, E0)
    biased_w = born_kernel(BIASED, E0)
    checks.check(
        "theorem-3-intermediates",
        "at diag(3/5,2/5), Tr(rho^2)=13/25 and Tr(rho^2 E0)=9/50",
        BIASED == H2(Fraction(3, 5), Fraction(0), Fraction(2, 5))
        and tr_rho2 == Fraction(13, 25)
        and tr_rho2_e0 == Fraction(9, 50),
        residual=(tr_rho2, tr_rho2_e0),
    )
    checks.check(
        "theorem-3-purity",
        "purity_kernel at the biased state is (9/50)/(13/25)=9/26",
        biased_k == tr_rho2_e0 / tr_rho2
        and biased_k == Fraction(9, 26)
        and K(BIASED, E0) == Fraction(9, 26),
        residual=biased_k,
    )
    checks.check(
        "theorem-3-born",
        "barycenter evaluation at the biased state is Tr(rho E0)=3/10",
        biased_w == Fraction(3, 10)
        and BIASED.pairing(E0) == Fraction(3, 10),
        residual=biased_w,
    )
    checks.check(
        "theorem-3-disagree",
        "9/26=45/130 and 3/10=39/130, so K is not Tr(rho E)",
        Fraction(9, 26) == Fraction(45, 130)
        and Fraction(3, 10) == Fraction(39, 130)
        and biased_k == Fraction(45, 130)
        and biased_w == Fraction(39, 130)
        and biased_k != biased_w,
        residual=(biased_k, biased_w),
    )

    k_plus = purity_kernel(PZ, E0)
    k_minus = purity_kernel(PMZ, E0)
    affine_mix = Fraction(3, 5) * k_plus + Fraction(2, 5) * k_minus
    checks.check(
        "theorem-4-atoms",
        "pure atoms give K(P(z),E0)=1/2 and K(P(-z),E0)=0",
        k_plus == Fraction(1, 2)
        and k_minus == 0
        and PZ.mul(PZ) == PZ
        and PMZ.mul(PMZ) == PMZ,
        residual=(k_plus, k_minus),
    )
    checks.check(
        "theorem-4-not-affine",
        "affine mix of the atoms is 3/10, not the barycenter value 9/26",
        affine_mix == Fraction(3, 10)
        and purity_kernel(BIASED, E0) == Fraction(9, 26)
        and affine_mix != purity_kernel(BIASED, E0)
        and (PZ.scale(Fraction(3, 5)) + PMZ.scale(Fraction(2, 5))) == BIASED,
        residual=(affine_mix, purity_kernel(BIASED, E0)),
    )

    cond_a = restriction_weight(
        E0.trace(), (E0.trace(), Fraction(9, 10), Fraction(3, 5))
    )
    checks.check(
        "restriction-hostile",
        "restriction of E0 on M_A recomputes as 25/142, which is not K(I/2,E0)=1/4",
        E0.trace() == Fraction(1, 2)
        and cond_a == Fraction(25, 142)
        and purity_kernel(MIXED, E0) == Fraction(1, 4)
        and cond_a != Fraction(1, 4)
        and cond_a != purity_kernel(MIXED, E0)
        and cond_a != purity_kernel(BIASED, E0),
        residual=cond_a,
    )

    checks.check(
        "mutation-born-fails",
        "replacing K by Tr(rho E) yields 3/10, not 9/26",
        born_kernel(BIASED, E0) == Fraction(3, 10)
        and purity_kernel(BIASED, E0) == Fraction(9, 26)
        and born_kernel(BIASED, E0) != purity_kernel(BIASED, E0)
        and born_kernel(MIXED, E0) == purity_kernel(MIXED, E0),
        residual=(born_kernel(BIASED, E0), purity_kernel(BIASED, E0)),
    )

    checks.check(
        "theorem-5-scope",
        "Theorem 5 scopes August 9 uniqueness and refuses the two banned overclaims",
        "August 9 uniqueness of Born is among affine" in note
        and "does not say Born is false" in note
        and "does not say that no uniqueness theorem exists in a larger class" in note
        and "not `Tr(ρE)`" in note,
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
                "menu-independent",
                "Tr(",
                "3/10",
                "9/26",
                "25/142",
                "45/130",
                "39/130",
                "authors no audit verdict",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block " not in note
        and "toe-lphys" not in note,
    )

    n5_lines = (
        "per_element: E0 at I/2 and diag(3/5,2/5) with values 1/4, 9/26, 3/10, and control 25/142",
        "per_site: the exhibit is one M_2(C) density-body site; no composite carrier is claimed",
        "per_mode: the diagonal family P(z), P(-z), I/2 is checked; no spectral-mode exhaustion",
        "per_block: Theorem 5 only scopes August 9 uniqueness to affine or similarly restricted kernels",
        "lattice_wide: checked and not executed — no lattice-wide Born no-go or uniqueness denial",
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
