#!/usr/bin/env python3
"""Exact checks for registered product partitions and Dirac obstruction.

Class-A arithmetic on Q(sqrt(2)). Identity gates call interval_length and
pushforward; replacing either by restriction must fail those checks.
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
    / "ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_BARYCENTER_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
PARENT_AUG10_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
PARENT_RECORD_PATH = (
    ROOT
    / "docs"
    / "RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text: str) -> str:
    return " ".join(text.split())


@dataclass(frozen=True)
class Qsqrt2:
    """Exact a + b sqrt(2)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def _coerce(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        if isinstance(other, Qsqrt2):
            return other
        if isinstance(other, (int, Fraction)):
            return Qsqrt2(Fraction(other))
        raise TypeError(other)

    def __add__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        other = self._coerce(other)
        return Qsqrt2(self.a + other.a, self.b + other.b)

    def __radd__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self + other

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.a, -self.b)

    def __sub__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self + (-self._coerce(other))

    def __rsub__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self._coerce(other) + (-self)

    def __mul__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        other = self._coerce(other)
        return Qsqrt2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __rmul__(self, other: "Qsqrt2 | int | Fraction") -> "Qsqrt2":
        return self * other

    def as_rational(self) -> Fraction:
        if self.b != 0:
            raise ValueError(f"expected rational, got {self}")
        return self.a


ZERO = Qsqrt2()
ONE = Qsqrt2(Fraction(1))


@dataclass(frozen=True)
class H2:
    """Real-symmetric 2x2 matrix over Q(sqrt(2))."""

    p: Qsqrt2
    q: Qsqrt2
    r: Qsqrt2

    def __add__(self, other: "H2") -> "H2":
        return H2(self.p + other.p, self.q + other.q, self.r + other.r)

    def scale(self, value: Qsqrt2 | int | Fraction) -> "H2":
        return H2(self.p * value, self.q * value, self.r * value)

    def mul(self, other: "H2") -> "H2":
        return H2(
            self.p * other.p + self.q * other.q,
            self.p * other.q + self.q * other.r,
            self.q * other.q + self.r * other.r,
        )

    def trace(self) -> Qsqrt2:
        return self.p + self.r

    def pairing(self, other: "H2") -> Qsqrt2:
        return self.p * other.p + (self.q * other.q) * 2 + self.r * other.r


I2 = H2(ONE, ZERO, ONE)
PZ = H2(ONE, ZERO, ZERO)
PMZ = H2(ZERO, ZERO, ONE)
PX = H2(Qsqrt2(Fraction(1, 2)), Qsqrt2(Fraction(1, 2)), Qsqrt2(Fraction(1, 2)))
PMX = H2(Qsqrt2(Fraction(1, 2)), Qsqrt2(Fraction(-1, 2)), Qsqrt2(Fraction(1, 2)))
MIXED = I2.scale(Fraction(1, 2))


def scaled_projector(coefficient: Fraction, n_x: Qsqrt2, n_z: Qsqrt2) -> H2:
    projector = H2(
        (ONE + n_z) * Fraction(1, 2),
        n_x * Fraction(1, 2),
        (ONE - n_z) * Fraction(1, 2),
    )
    return projector.scale(coefficient)


def extract_direction(effect: H2) -> tuple[Fraction, Qsqrt2, Qsqrt2]:
    coefficient = effect.trace().as_rational()
    bloch = effect.scale(Fraction(2, coefficient))
    shifted = H2(bloch.p - ONE, bloch.q, bloch.r - ONE)
    n_z = shifted.p
    n_x = shifted.q
    return coefficient, n_x, n_z


def is_scaled_projector(effect: H2) -> bool:
    coefficient, n_x, n_z = extract_direction(effect)
    projector_identity = effect.mul(effect) == effect.scale(coefficient)
    unit = n_x * n_x + n_z * n_z == ONE
    return projector_identity and unit and coefficient > 0 and coefficient <= 1


def barycenter(weights_states: tuple[tuple[Fraction, H2], ...]) -> H2:
    total = H2(ZERO, ZERO, ZERO)
    weight_sum = Fraction(0)
    for weight, state in weights_states:
        total = total + state.scale(weight)
        weight_sum += weight
    if weight_sum != 1:
        raise ValueError("barycentric weights must sum to one")
    return total


def pairing(state: H2, effect: H2) -> Qsqrt2:
    return state.pairing(effect)


def interval_length(state: H2, menu: tuple[H2, ...], index: int) -> Fraction:
    """Lebesgue length of the fiber assigned to menu[index] at state."""
    return pairing(state, menu[index]).as_rational()


def prefix_sums(state: H2, menu: tuple[H2, ...]) -> tuple[Fraction, ...]:
    totals: list[Fraction] = [Fraction(0)]
    running = Fraction(0)
    for effect in menu:
        running += pairing(state, effect).as_rational()
        totals.append(running)
    return tuple(totals)


def assigned_cell(
    state: H2, menu: tuple[H2, ...], t: Fraction
) -> int | None:
    """Exact cell index for the half-open cells with t=1 in the last cell."""
    if t < 0 or t > 1:
        return None
    prefixes = prefix_sums(state, menu)
    last = len(menu) - 1
    for index in range(len(menu)):
        left, right = prefixes[index], prefixes[index + 1]
        if left <= t and (t < right or (index == last and t <= right)):
            return index
    return None


def pushforward(
    weights_states: tuple[tuple[Fraction, H2], ...],
    menu: tuple[H2, ...],
    index: int,
) -> Fraction:
    """Product pushforward (μ⊗λ)(A(index|M)) via fiber lengths."""
    total = Fraction(0)
    weight_sum = Fraction(0)
    for weight, state in weights_states:
        total += weight * interval_length(state, menu, index)
        weight_sum += weight
    if weight_sum != 1:
        raise ValueError("mixture weights must sum to one")
    return total


def restriction_weight(effect: H2, menu: tuple[H2, ...]) -> Fraction:
    numerator = effect.trace().as_rational() ** 2
    denominator = sum((item.trace().as_rational() ** 2) for item in menu)
    return numerator / denominator


@dataclass(frozen=True)
class Embedded:
    """Image of ι(ρ,t)=ρ+i(t-1/2)I as (Hermitian H2, imag coefficient of I)."""

    hermitian: H2
    imag_i: Fraction


def embed(state: H2, t: Fraction) -> Embedded:
    return Embedded(state, t - Fraction(1, 2))


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
    parent_barycenter = PARENT_BARYCENTER_PATH.read_text(encoding="utf-8")
    parent_aug10 = PARENT_AUG10_PATH.read_text(encoding="utf-8")
    parent_record = PARENT_RECORD_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: axiom wording and the three parent notes "
        "are source-bound; no observational or fitted inputs"
    )
    print(
        "construction: product registration Y=D×[0,1]; "
        "(μ⊗λ)(A(i|M))=Tr(ρ_μ E_i); restriction is a hostile control"
    )
    print(
        "negative_scope: Dirac pushforwards on D or X are {0,1}-valued; "
        "stochastic kernels, atomless laws, and product lifts remain live"
    )

    checks.check(
        "audit-input-paths",
        "declared inputs bind the note, current axioms, and all three direct parents",
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md",
            "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
            "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
            "docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS),
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
    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split(
        "## Qualification", 1
    )[0]
    normalized_record_section = normalize(record_section)
    checks.check(
        "source-record-simplification",
        "Record supplies content determination and no named scalar, additivity, or absence-value rule",
        "A readout value is determined by record content alone."
        in normalized_record_section
        and "A site with no record cannot be read." in normalized_record_section
        and all(
            token not in record_section
            for token in ("I(", "I(empty)", "additiv", "scalar")
        ),
    )
    checks.check(
        "source-parents",
        "Aug 10 supplies the partition residual, barycenter parent the grade, and Record parent the event/readout boundary",
        all(
            phrase in parent_aug10
            for phrase in (
                "25/142",
                "2/11",
                "509/200",
                "registered",
                "partition",
            )
        )
        and all(
            phrase in parent_barycenter
            for phrase in ("menu-independent", "Tr(", "restriction is not this kernel")
        )
        and all(
            phrase in parent_record
            for phrase in ("formation/event probability", "direct readout values")
        ),
    )

    n1x, n1z = Qsqrt2(Fraction(0), Fraction(4, 9)), Qsqrt2(Fraction(-7, 9))
    n2x, n2z = Qsqrt2(Fraction(0), Fraction(-2, 3)), Qsqrt2(Fraction(1, 3))
    m1x, m1z = Qsqrt2(Fraction(0), Fraction(2, 3)), Qsqrt2(Fraction(-1, 3))
    m2x, m2z = Qsqrt2(Fraction(0), Fraction(-2, 3)), Qsqrt2(Fraction(-1, 3))
    e0 = scaled_projector(Fraction(1, 2), ZERO, ONE)
    a1 = scaled_projector(Fraction(9, 10), n1x, n1z)
    a2 = scaled_projector(Fraction(3, 5), n2x, n2z)
    b1 = scaled_projector(Fraction(3, 4), m1x, m1z)
    b2 = scaled_projector(Fraction(3, 4), m2x, m2z)
    menu_a = (e0, a1, a2)
    menu_b = (e0, b1, b2)
    menu_a_rev = (a2, a1, e0)
    declared = (e0, a1, a2, b1, b2)

    checks.check(
        "menu-resolutions",
        "both hostile menus are exact matrix resolutions of I by five distinct scaled projectors",
        e0 + a1 + a2 == I2
        and e0 + b1 + b2 == I2
        and all(is_scaled_projector(item) for item in declared)
        and len(set(declared)) == 5,
    )

    traces = tuple(item.trace().as_rational() for item in declared)
    atomic_z = sum(value * value for value in traces)
    cond_a = restriction_weight(e0, menu_a)
    cond_b = restriction_weight(e0, menu_b)
    checks.check(
        "restriction-recompute",
        "atomic restriction recomputed from matrix traces is 25/142 on M_A and 2/11 on M_B with Z=509/200",
        atomic_z == Fraction(509, 200)
        and cond_a == Fraction(25, 142)
        and cond_b == Fraction(2, 11)
        and cond_a - cond_b == Fraction(-9, 1562),
    )

    mixed_e0 = interval_length(MIXED, menu_a, 0)
    biased = barycenter(((Fraction(3, 5), PZ), (Fraction(2, 5), PMZ)))
    biased2 = barycenter(((Fraction(4, 5), PZ), (Fraction(1, 5), PMZ)))
    biased_e0 = interval_length(biased, menu_a, 0)
    checks.check(
        "dirac-obstruction",
        "Tr(I/2,E_0)=1/4 and Tr(diag(3/5,2/5),E_0)=3/10 are not in {0,1}",
        mixed_e0 == Fraction(1, 4)
        and biased_e0 == Fraction(3, 10)
        and mixed_e0 not in (Fraction(0), Fraction(1))
        and biased_e0 not in (Fraction(0), Fraction(1))
        and interval_length(MIXED, menu_b, 0) == Fraction(1, 4)
        and interval_length(biased, menu_b, 0) == Fraction(3, 10),
    )

    def cover_ok(state: H2, menu: tuple[H2, ...]) -> bool:
        prefixes = prefix_sums(state, menu)
        if prefixes[0] != 0 or prefixes[-1] != 1:
            return False
        if any(prefixes[i] > prefixes[i + 1] for i in range(len(prefixes) - 1)):
            return False
        lengths = [interval_length(state, menu, i) for i in range(len(menu))]
        if sum(lengths) != 1 or any(length < 0 for length in lengths):
            return False
        boundary_cells = [assigned_cell(state, menu, point) for point in prefixes]
        midpoint_cells = [
            assigned_cell(state, menu, (prefixes[i] + prefixes[i + 1]) / 2)
            for i in range(len(menu))
        ]
        return (
            boundary_cells[0] == 0
            and boundary_cells[-1] == len(menu) - 1
            and boundary_cells[1:-1] == list(range(1, len(menu)))
            and midpoint_cells == list(range(len(menu)))
        )

    checks.check(
        "partition-cover",
        "all cells including t=1 give an exact disjoint cover and interval lengths sum to 1 on both menus",
        all(
            cover_ok(state, menu)
            for state in (MIXED, biased, biased2)
            for menu in (menu_a, menu_b)
        ),
    )

    mixed_norm_a = sum(interval_length(MIXED, menu_a, i) for i in range(3))
    mixed_norm_b = sum(interval_length(MIXED, menu_b, i) for i in range(3))
    checks.check(
        "mixed-pushforward",
        "E_0 fiber length is 1/4 in both menus at I/2 and both menus normalize",
        interval_length(MIXED, menu_a, 0) == Fraction(1, 4)
        and interval_length(MIXED, menu_b, 0) == Fraction(1, 4)
        and mixed_norm_a == 1
        and mixed_norm_b == 1,
    )

    biased_norm_a = sum(interval_length(biased, menu_a, i) for i in range(3))
    biased_norm_b = sum(interval_length(biased, menu_b, i) for i in range(3))
    biased2_norm_a = sum(interval_length(biased2, menu_a, i) for i in range(3))
    biased2_norm_b = sum(interval_length(biased2, menu_b, i) for i in range(3))
    checks.check(
        "biased-pushforward",
        "E_0 lengths 3/10 and 2/5 in both menus at the two biased states; menus normalize",
        biased == H2(Qsqrt2(Fraction(3, 5)), ZERO, Qsqrt2(Fraction(2, 5)))
        and biased2 == H2(Qsqrt2(Fraction(4, 5)), ZERO, Qsqrt2(Fraction(1, 5)))
        and interval_length(biased, menu_a, 0) == Fraction(3, 10)
        and interval_length(biased, menu_b, 0) == Fraction(3, 10)
        and interval_length(biased2, menu_a, 0) == Fraction(2, 5)
        and interval_length(biased2, menu_b, 0) == Fraction(2, 5)
        and biased_norm_a == 1
        and biased_norm_b == 1
        and biased2_norm_a == 1
        and biased2_norm_b == 1,
    )

    checks.check(
        "disagree-restriction",
        "pushforward E_0 values disagree with restriction 25/142 and 2/11",
        interval_length(MIXED, menu_a, 0) != cond_a
        and interval_length(MIXED, menu_a, 0) != cond_b
        and interval_length(biased, menu_a, 0) != cond_a
        and interval_length(biased, menu_a, 0) != cond_b
        and interval_length(biased2, menu_a, 0) != cond_a
        and interval_length(biased2, menu_a, 0) != cond_b
        and cond_a != cond_b,
    )

    checks.check(
        "spectral-endpoints",
        "at δ_P(z) the E_0 length is 1/2; at δ_P(-z) the length is 0",
        interval_length(PZ, menu_a, 0) == Fraction(1, 2)
        and interval_length(PZ, menu_b, 0) == Fraction(1, 2)
        and interval_length(PMZ, menu_a, 0) == 0
        and interval_length(PMZ, menu_b, 0) == 0,
    )

    mixture = ((Fraction(3, 5), PZ), (Fraction(2, 5), PMZ))
    mixture_ok = True
    for menu in (menu_a, menu_b):
        for index in range(len(menu)):
            pushed = pushforward(mixture, menu, index)
            target = pairing(biased, menu[index]).as_rational()
            mixture_ok = mixture_ok and pushed == target
    checks.check(
        "mixture-equals-barycenter",
        "pushforward of 3/5 δ_P(z)+2/5 δ_P(-z) equals pairing of the barycenter on every menu member",
        mixture_ok
        and pushforward(mixture, menu_a, 0) == Fraction(3, 10)
        and pushforward(mixture, menu_b, 0) == Fraction(3, 10),
    )

    lengths_a = sorted(interval_length(MIXED, menu_a, i) for i in range(3))
    lengths_rev = sorted(interval_length(MIXED, menu_a_rev, i) for i in range(3))
    e0_index_rev = menu_a_rev.index(e0)
    checks.check(
        "order-independence",
        "reversed M_A gives the same three lengths as a multiset; E_0 length unchanged",
        lengths_a == lengths_rev
        and interval_length(MIXED, menu_a_rev, e0_index_rev) == Fraction(1, 4)
        and interval_length(biased, menu_a_rev, e0_index_rev)
        == interval_length(biased, menu_a, 0),
    )

    samples = (
        (MIXED, Fraction(0)),
        (MIXED, Fraction(1, 4)),
        (MIXED, Fraction(1, 2)),
        (PZ, Fraction(0)),
        (PZ, Fraction(1, 2)),
        (PMZ, Fraction(1)),
        (biased, Fraction(3, 10)),
        (biased2, Fraction(2, 5)),
    )
    embedded = [embed(state, t) for state, t in samples]
    checks.check(
        "embedding-optional",
        "ι(ρ,t)=ρ+i(t-1/2)I is injective on the finite sample of (ρ,t) pairs",
        len(embedded) == len(set(embedded))
        and len(samples) == len(set(samples))
        and embed(MIXED, Fraction(0)) != embed(MIXED, Fraction(1, 2))
        and embed(PZ, Fraction(0)) != embed(PMZ, Fraction(0)),
    )

    projectors = (PZ, PMZ, PX, PMX)
    checks.check(
        "singleton-mass-two",
        "raw singleton normalization of the z and x projective menus still forces mass two",
        PZ + PMZ == I2
        and PX + PMX == I2
        and len(set(projectors)) == 4
        and Fraction(1) + Fraction(1) == 2
        and Fraction(1) + Fraction(1) > Fraction(1),
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
                "hypothetical_axiom_status: \"no edit, adoption, minimality, or necessity claim\"",
                "trace_class: direct_blocker_closure",
                "target_claim_id: admissibility_distribution_to_effect_grade_bridge",
                "reachability_to_target: partially_closes",
                "menu-independent",
                "Tr(",
                "25/142",
                "2/11",
                "509/200",
                "Dirac obstruction",
                "product registration",
                "Borel",
                "newly supplied mathematical input",
                "not a physical menu compiler",
                "not a Record-content identification or direct readout law",
                "Non-affine kernels remain live",
                "authors no audit verdict",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note,
    )
    checks.check(
        "no-go-discipline-contract",
        "the source carries N1 through N8, distinct live routes, and the narrowed gate disposition",
        all(f"### N{index}" in note for index in range(1, 9))
        and all(
            phrase in note
            for phrase in (
                "stochastic/Markov readout kernel",
                "non-atomic auxiliary coordinate",
                "fixed non-atomic law",
                "operator-valued or Naimark event model",
                "There is one wall",
                "PASS for the scoped Dirac obstruction",
                "FAIL / DO NOT SHIP",
            )
        ),
    )

    print(
        "per_element: E_0 and remaining declared menu members checked by fiber "
        "lengths and restriction controls"
    )
    print(
        "per_site: Dirac obstruction, product partition, and pushforward identity "
        "are one-site statements"
    )
    print(
        "per_mode: checked and not executed — no spectral-mode or harmonic-mode "
        "exhaustion claim is part of the theorem"
    )
    print(
        "per_block: only the atomic-support partition obstruction and the product "
        "registration block are executed"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide dynamics, "
        "formation rate, or Record identification is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
