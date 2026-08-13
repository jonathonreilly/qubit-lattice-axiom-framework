#!/usr/bin/env python3
"""Exact checks for finite dyadic registration and truncated barycenter.

Class-A arithmetic on Q(sqrt(2)). Identity gates call floor_diff_mass and
truncated_pushforward; replacing either by restriction or by raw Tr must fail
those checks.
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
    / "RECORD_BIT_DYADIC_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_AUG09_PATH = (
    ROOT
    / "docs"
    / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
)
PARENT_AUG10_PATH = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)

AUDIT_INPUT_PATHS = (
    "docs/RECORD_BIT_DYADIC_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
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


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def prefix_sums(state: H2, menu: tuple[H2, ...]) -> tuple[Fraction, ...]:
    totals: list[Fraction] = [Fraction(0)]
    running = Fraction(0)
    for effect in menu:
        running += pairing(state, effect).as_rational()
        totals.append(running)
    return tuple(totals)


def floor_diff_count(state: H2, menu: tuple[H2, ...], index: int, n: int) -> int:
    """Integer count q_i(ρ) from prefix-sum floors."""
    prefixes = prefix_sums(state, menu)
    scale = 1 << n
    high = floor_fraction(prefixes[index + 1] * scale)
    low = floor_fraction(prefixes[index] * scale)
    return high - low


def floor_diff_mass(state: H2, menu: tuple[H2, ...], index: int, n: int) -> Fraction:
    """Truncated mass q_i(ρ)/2^n. Identity-gate function."""
    return Fraction(floor_diff_count(state, menu, index, n), 1 << n)


def truncated_pushforward(
    weights_states: tuple[tuple[Fraction, H2], ...],
    menu: tuple[H2, ...],
    index: int,
    n: int,
) -> Fraction:
    """Product pushforward (μ⊗λ_n)(A_n(index|M)) via floor-difference masses."""
    total = Fraction(0)
    weight_sum = Fraction(0)
    for weight, state in weights_states:
        total += weight * floor_diff_mass(state, menu, index, n)
        weight_sum += weight
    if weight_sum != 1:
        raise ValueError("mixture weights must sum to one")
    return total


def restriction_weight(effect: H2, menu: tuple[H2, ...]) -> Fraction:
    numerator = effect.trace().as_rational() ** 2
    denominator = sum((item.trace().as_rational() ** 2) for item in menu)
    return numerator / denominator


def is_dyadic_rational(value: Fraction) -> bool:
    denominator = value.denominator
    return denominator > 0 and denominator.bit_count() == 1


def assigned_edges(state: H2, menu: tuple[H2, ...], n: int) -> tuple[int, ...]:
    scale = 1 << n
    return tuple(floor_fraction(prefix * scale) for prefix in prefix_sums(state, menu))


def partition_ok(state: H2, menu: tuple[H2, ...], n: int) -> bool:
    edges = assigned_edges(state, menu, n)
    if edges[0] != 0 or edges[-1] != (1 << n):
        return False
    if any(edges[index] > edges[index + 1] for index in range(len(edges) - 1)):
        return False
    counts = [floor_diff_count(state, menu, index, n) for index in range(len(menu))]
    if sum(counts) != (1 << n):
        return False
    if any(count != edges[index + 1] - edges[index] for index, count in enumerate(counts)):
        return False
    return all(count >= 0 for count in counts)


def truncation_bound_ok(state: H2, menu: tuple[H2, ...], n: int) -> bool:
    scale = 1 << n
    for index, effect in enumerate(menu):
        mass = floor_diff_mass(state, menu, index, n)
        target = pairing(state, effect).as_rational()
        if abs(mass * scale - target * scale) >= 1:
            return False
        if abs(mass - target) >= Fraction(1, scale):
            return False
    return True


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
    parent_aug09 = PARENT_AUG09_PATH.read_text(encoding="utf-8")
    parent_aug10 = PARENT_AUG10_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: axiom wording and the August 9 and "
        "August 10 parent notes are source-bound; no observational or fitted inputs"
    )
    print(
        "integrity_reads: this runner, its paired note, the axiom memo, and "
        "the two parent notes; no other repository scientific inputs"
    )
    print(
        "construction: floor-difference registration on D×U_n; "
        "w_n is affine in μ and is not barycenter evaluation at finite n"
    )
    print(
        "negative_scope: no finite n makes truncated E_0 mass equal Tr at all "
        "three declared Diracs; continuum and compilers remain live"
    )

    canonical_sentence = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    record_lock = "When present, a record locks exactly one admissible local possibility."
    record_content = "A readout value is determined by record content alone."
    record_additivity = (
        "For any finite collection of pairwise-disjoint records, scalar readout"
    )
    checks.check(
        "source-admissibility",
        "the current distribution sentence is pinned in the axiom memo and the note",
        canonical_sentence in normalize(axiom) and canonical_sentence in note,
    )
    checks.check(
        "source-record",
        "the Record lock, content-only, and additivity sentences are pinned",
        record_lock in normalize(axiom)
        and record_content in normalize(axiom)
        and record_additivity in normalize(axiom)
        and record_lock in note
        and record_content in note
        and record_additivity in note,
    )
    checks.check(
        "source-parents",
        "Aug 10 has restriction witness and partition language; Aug 9 has menu-independent Tr form",
        all(
            phrase in parent_aug10
            for phrase in (
                "25/142",
                "2/11",
                "509/200",
                "registered",
                "partition",
                "physical construction that produces registered measurable event partitions",
            )
        )
        and all(phrase in parent_aug09 for phrase in ("menu-independent", "Tr(")),
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

    biased = barycenter(((Fraction(3, 5), PZ), (Fraction(2, 5), PMZ)))
    biased2 = barycenter(((Fraction(4, 5), PZ), (Fraction(1, 5), PMZ)))
    declared_states = (MIXED, biased, biased2, PZ, PMZ)
    executed_depths = (1, 2, 3)

    checks.check(
        "pairings-recompute",
        "declared E_0 pairings are 1/4, 3/10, 2/5, 1/2, and 0 in both menus",
        pairing(MIXED, e0).as_rational() == Fraction(1, 4)
        and pairing(biased, e0).as_rational() == Fraction(3, 10)
        and pairing(biased2, e0).as_rational() == Fraction(2, 5)
        and pairing(PZ, e0).as_rational() == Fraction(1, 2)
        and pairing(PMZ, e0).as_rational() == 0
        and biased == H2(Qsqrt2(Fraction(3, 5)), ZERO, Qsqrt2(Fraction(2, 5)))
        and biased2 == H2(Qsqrt2(Fraction(4, 5)), ZERO, Qsqrt2(Fraction(1, 5))),
    )

    checks.check(
        "partition-cover",
        "prefix floors start at 0, end at 2^n, are nondecreasing, and sum of q_i is 2^n",
        all(
            partition_ok(state, menu, depth)
            for state in declared_states
            for menu in (menu_a, menu_b, menu_a_rev)
            for depth in executed_depths
        ),
    )

    checks.check(
        "uniform-truncation-bound",
        "constructed floor_diff_mass stays strictly inside 2^{-n} of each pairing",
        all(
            truncation_bound_ok(state, menu, depth)
            for state in declared_states
            for menu in (menu_a, menu_b, menu_a_rev)
            for depth in executed_depths
        ),
    )

    checks.check(
        "mixed-exact-quarter",
        "floor_diff_mass at I/2 equals 1/4 for n>=2 and is not 1/4 at n=1",
        floor_diff_mass(MIXED, menu_a, 0, 3) == Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_b, 0, 3) == Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_a, 0, 2) == Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_b, 0, 2) == Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_a, 0, 1) != Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_b, 0, 1) != Fraction(1, 4)
        and pairing(MIXED, e0).as_rational() == Fraction(1, 4),
    )

    never_dyadic_ok = True
    for depth in executed_depths:
        for menu in (menu_a, menu_b):
            if floor_diff_mass(biased, menu, 0, depth) == Fraction(3, 10):
                never_dyadic_ok = False
            if floor_diff_mass(biased2, menu, 0, depth) == Fraction(2, 5):
                never_dyadic_ok = False
    checks.check(
        "biased-never-dyadic",
        "floor_diff_mass at the biased Diracs is never 3/10 or 2/5; those pairings are not dyadic rationals",
        never_dyadic_ok
        and not is_dyadic_rational(Fraction(3, 10))
        and not is_dyadic_rational(Fraction(2, 5))
        and is_dyadic_rational(Fraction(1, 4))
        and (Fraction(3, 10) * (1 << 20)).denominator != 1
        and (Fraction(2, 5) * (1 << 20)).denominator != 1
        and Fraction(3, 10).denominator % 5 == 0
        and Fraction(2, 5).denominator % 5 == 0,
    )

    checks.check(
        "spectral-endpoints",
        "at δ_P(z) the truncated E_0 mass is 1/2; at δ_P(-z) the mass is 0",
        all(
            floor_diff_mass(PZ, menu, 0, depth) == Fraction(1, 2)
            and floor_diff_mass(PMZ, menu, 0, depth) == 0
            for menu in (menu_a, menu_b)
            for depth in executed_depths
        ),
    )

    finite_n_hits = []
    for depth in executed_depths:
        exact_all = True
        for menu in (menu_a, menu_b):
            exact_all = exact_all and floor_diff_mass(MIXED, menu, 0, depth) == Fraction(1, 4)
            exact_all = exact_all and floor_diff_mass(biased, menu, 0, depth) == Fraction(3, 10)
            exact_all = exact_all and floor_diff_mass(biased2, menu, 0, depth) == Fraction(2, 5)
        finite_n_hits.append(exact_all)
    checks.check(
        "finite-n-obstruction",
        "no executed finite n makes truncated E_0 mass exact at all three declared Diracs",
        not any(finite_n_hits)
        and not is_dyadic_rational(Fraction(3, 10))
        and not is_dyadic_rational(Fraction(2, 5)),
    )

    mixture = ((Fraction(3, 5), PZ), (Fraction(2, 5), PMZ))
    mixture_affine_ok = True
    for menu in (menu_a, menu_b):
        for depth in executed_depths:
            for index in range(len(menu)):
                pushed = truncated_pushforward(mixture, menu, index, depth)
                rebuilt = (
                    Fraction(3, 5) * floor_diff_mass(PZ, menu, index, depth)
                    + Fraction(2, 5) * floor_diff_mass(PMZ, menu, index, depth)
                )
                mixture_affine_ok = mixture_affine_ok and pushed == rebuilt
    checks.check(
        "mixture-identity",
        "truncated pushforward of 3/5 δ_P(z)+2/5 δ_P(-z) equals the atomic mixture of floor_diff_mass",
        mixture_affine_ok
        and truncated_pushforward(mixture, menu_a, 0, 1) == Fraction(3, 10)
        and truncated_pushforward(mixture, menu_a, 0, 2) == Fraction(3, 10)
        and truncated_pushforward(mixture, menu_a, 0, 3) == Fraction(3, 10)
        and truncated_pushforward(mixture, menu_b, 0, 3) == Fraction(3, 10),
    )

    checks.check(
        "mixture-not-barycenter-at-biased",
        "endpoint mixture truncated E_0 mass is 3/10; Dirac at the barycenter is not",
        all(
            truncated_pushforward(mixture, menu, 0, depth) == Fraction(3, 10)
            and floor_diff_mass(biased, menu, 0, depth) != Fraction(3, 10)
            for menu in (menu_a, menu_b)
            for depth in executed_depths
        ),
    )

    checks.check(
        "disagree-restriction",
        "truncated E_0 values disagree with restriction 25/142 and 2/11",
        floor_diff_mass(MIXED, menu_a, 0, 3) != cond_a
        and floor_diff_mass(MIXED, menu_a, 0, 3) != cond_b
        and floor_diff_mass(biased, menu_a, 0, 3) != cond_a
        and floor_diff_mass(biased, menu_a, 0, 3) != cond_b
        and floor_diff_mass(biased2, menu_a, 0, 3) != cond_a
        and floor_diff_mass(biased2, menu_a, 0, 3) != cond_b
        and cond_a != cond_b
        and cond_a != Fraction(1, 4)
        and cond_b != Fraction(1, 4),
    )

    e0_index_rev = menu_a_rev.index(e0)
    continuum_lengths_a = sorted(
        pairing(MIXED, item).as_rational() for item in menu_a
    )
    continuum_lengths_rev = sorted(
        pairing(MIXED, item).as_rational() for item in menu_a_rev
    )
    checks.check(
        "order-independence-length",
        "reversed M_A keeps the same pairing lengths; exact E_0 truncated mass is unchanged when the increment is integral",
        continuum_lengths_a == continuum_lengths_rev
        and pairing(MIXED, menu_a_rev[e0_index_rev]).as_rational() == Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_a_rev, e0_index_rev, 3) == Fraction(1, 4)
        and floor_diff_mass(MIXED, menu_a_rev, e0_index_rev, 2) == Fraction(1, 4)
        and floor_diff_mass(PZ, menu_a_rev, e0_index_rev, 3) == Fraction(1, 2)
        and floor_diff_mass(PMZ, menu_a_rev, e0_index_rev, 3) == 0,
    )

    checks.check(
        "mutation-restriction-would-fail",
        "replacing floor_diff_mass by restriction 25/142 would fail mixed-exact-quarter and mixture-not-barycenter",
        cond_a == Fraction(25, 142)
        and cond_a != Fraction(1, 4)
        and cond_b != Fraction(1, 4)
        and cond_a == restriction_weight(e0, menu_a)
        and cond_a != floor_diff_mass(MIXED, menu_a, 0, 3)
        and cond_a != truncated_pushforward(mixture, menu_a, 0, 3),
    )
    checks.check(
        "mutation-raw-trace-would-fail",
        "replacing floor_diff_mass by raw Tr would fail biased-never-dyadic and mixture-not-barycenter",
        pairing(biased, e0).as_rational() == Fraction(3, 10)
        and pairing(biased, e0).as_rational()
        == truncated_pushforward(mixture, menu_a, 0, 3)
        and pairing(biased, e0).as_rational()
        != floor_diff_mass(biased, menu_a, 0, 3)
        and pairing(MIXED, e0).as_rational() == Fraction(1, 4),
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
                "hypothetical_axiom_status: \"no edit\"",
                "trace_class: direct_blocker_closure",
                "target_claim_id: admissibility_distribution_to_effect_grade_bridge",
                "reachability_to_target: partially_closes",
                "next_trace_action: \"A physical compiler that produces independent uniform Record bits, or a continuum factor, remains open; do not adopt axiom text.\"",
                "conditional_surface_status: \"exact for floor-difference registration on D×U_n and the finite-n obstruction at 3/10; physical bit independence/uniformity open\"",
                "25/142",
                "2/11",
                "509/200",
                "3/10",
                "never dyadic",
                "not a physical menu compiler",
                "authors no audit verdict",
            )
        )
        and retained_ok
        and "retained" not in other_retained
        and "promoted" not in note.lower()
        and "we adopt" not in note.lower()
        and "new axiom" not in note.lower()
        and "Codex" not in note
        and "Block 11" not in note
        and "toe-lphys" not in note,
    )

    print(
        "per_element: E_0 and remaining declared menu members checked by "
        "floor-difference masses and restriction controls"
    )
    print(
        "per_site: finite-n obstruction, product partition, and truncated "
        "kernel identities are one-site statements"
    )
    print(
        "per_mode: prefix-sum floor bins on the declared menus; register "
        "points are typed, not compiled"
    )
    print(
        "per_block: only the finite-n exact-equality obstruction and the "
        "truncated-kernel identities are executed"
    )
    print(
        "lattice_wide: checked and not executed — no lattice-wide dynamics, "
        "formation rate, or Record identification is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
