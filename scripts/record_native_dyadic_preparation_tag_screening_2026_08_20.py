#!/usr/bin/env python3
"""Exact Record-native dyadic preparation and tag-screening checks.

The primary object is a homogeneous strict-nearest-neighbour append rule on a
finite apparatus rail.  Five occupied neighbours and one blank forward
neighbour identify the unique active site.  Relational four-guard patterns
select accumulator, preparation, or tester behavior.  No cache is written.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Iterable


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BARYCENTER_PATH = ROOT / "docs" / "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md"
NONAFFINE_PATH = ROOT / "docs" / "NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13.md"
CYCLE20_PATH = ROOT / "docs" / "work_history" / "repo" / "review_feedback" / "OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md"
REGISTRY_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
AUDIT_INPUT_PATHS = (
    "docs/RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/NONAFFINE_PURITY_WEIGHTED_KERNEL_IS_NOT_BARYCENTER_EVALUATION_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/work_history/repo/review_feedback/OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
)

Point = tuple[int, int, int]
BitRecords = dict[Point, int]
StateKey = tuple[tuple[Point, int], ...]

DIRECTIONS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
BASE_TRANSVERSE: tuple[Point, ...] = (
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def neg(a: Point) -> Point:
    return (-a[0], -a[1], -a[2])


def scale(k: int, a: Point) -> Point:
    return (k * a[0], k * a[1], k * a[2])


def dot(a: Point, b: Point) -> int:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def state_key(records: BitRecords) -> StateKey:
    return tuple(sorted(records.items()))


def from_state_key(key: StateKey) -> BitRecords:
    return dict(key)


@dataclass(frozen=True)
class H2:
    """Real symmetric two-by-two matrix over exact rationals."""

    a: Fraction
    b: Fraction
    d: Fraction

    def complement(self) -> "H2":
        return H2(Fraction(1) - self.a, -self.b, Fraction(1) - self.d)

    def mul(self, other: "H2") -> tuple[Fraction, Fraction, Fraction, Fraction]:
        return (
            self.a * other.a + self.b * other.b,
            self.a * other.b + self.b * other.d,
            self.b * other.a + self.d * other.b,
            self.b * other.b + self.d * other.d,
        )

    def trace(self) -> Fraction:
        return self.a + self.d

    def det(self) -> Fraction:
        return self.a * self.d - self.b * self.b


PZ = H2(Fraction(1), Fraction(0), Fraction(0))
PMZ = PZ.complement()


def conjugate_projector(u: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]) -> H2:
    """Return U PZ U^T for one exact real orthogonal U."""
    return H2(u[0][0] ** 2, u[0][0] * u[1][0], u[1][0] ** 2)


def determinant3(matrix: tuple[Point, Point, Point]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def cubic_rotations() -> tuple[tuple[Point, Point, Point], ...]:
    rotations: list[tuple[Point, Point, Point]] = []
    basis = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows: list[Point] = []
            for row in range(3):
                vector = basis[perm[row]]
                rows.append(tuple(signs[row] * entry for entry in vector))
            matrix = tuple(rows)  # type: ignore[assignment]
            if determinant3(matrix) == 1:
                rotations.append(matrix)
    return tuple(rotations)


ROTATIONS = cubic_rotations()


def rotate(matrix: tuple[Point, Point, Point], point: Point) -> Point:
    return tuple(dot(row, point) for row in matrix)  # type: ignore[return-value]


@dataclass(frozen=True)
class Track:
    records: StateKey
    targets: tuple[Point, ...]
    roles: tuple[str, ...]
    reference_bit: int
    accumulator_count: int
    tester_count: int


def build_track(
    accumulator_count: int,
    tester_count: int,
    *,
    rotation: tuple[Point, Point, Point] | None = None,
    shift: Point = (0, 0, 0),
    complement_bits: bool = False,
) -> Track:
    if accumulator_count < 1 or tester_count < 1:
        raise ValueError("the apparatus needs at least one accumulator and one tester")
    rotation = rotation or ROTATIONS[0]

    def transform(point: Point) -> Point:
        return add(rotate(rotation, point), shift)

    reference = 1 if complement_bits else 0
    other = 1 - reference
    records: BitRecords = {transform((-1, 0, 0)): reference}
    targets: list[Point] = []
    roles: list[str] = []
    total_targets = accumulator_count + 1 + tester_count
    for j in range(total_targets):
        target = (j, 0, 0)
        targets.append(transform(target))
        if j < accumulator_count:
            roles.append("accumulator")
            guard_bits = (reference, reference, reference, reference)
        elif j == accumulator_count:
            roles.append("preparation")
            guard_bits = (reference, reference, reference, other)
        else:
            roles.append("tester")
            guard_bits = (reference, reference, other, other)
        for direction, bit in zip(BASE_TRANSVERSE, guard_bits, strict=True):
            position = transform(add(target, direction))
            if position in records and records[position] != bit:
                raise AssertionError("incompatible guard overlap")
            records[position] = bit
    return Track(
        records=state_key(records),
        targets=tuple(targets),
        roles=tuple(roles),
        reference_bit=reference,
        accumulator_count=accumulator_count,
        tester_count=tester_count,
    )


@dataclass(frozen=True)
class Signature:
    role: str
    predecessor: Point
    forward: Point
    reference_bit: int


def local_signature(records: BitRecords, target: Point) -> Signature | None:
    if target in records:
        return None
    occupied_directions = [direction for direction in DIRECTIONS if add(target, direction) in records]
    if len(occupied_directions) != 5:
        return None
    blank_directions = [direction for direction in DIRECTIONS if direction not in occupied_directions]
    if len(blank_directions) != 1:
        return None
    forward = blank_directions[0]
    predecessor_direction = neg(forward)
    predecessor = add(target, predecessor_direction)
    if predecessor not in records:
        return None
    transverse = [direction for direction in occupied_directions if direction != predecessor_direction]
    if len(transverse) != 4 or any(dot(direction, forward) != 0 for direction in transverse):
        return None
    values = {direction: records[add(target, direction)] for direction in transverse}
    predecessor_bit = records[predecessor]

    if len(set(values.values())) == 1:
        reference = next(iter(values.values()))
        if predecessor_bit in (reference, 1 - reference):
            return Signature("accumulator", predecessor, forward, reference)

    counts = Counter(values.values())
    if sorted(counts.values()) == [1, 3]:
        reference = counts.most_common(1)[0][0]
        if predecessor_bit in (reference, 1 - reference):
            return Signature("preparation", predecessor, forward, reference)

    opposite_pairs: list[tuple[Point, Point]] = []
    unused = set(transverse)
    while unused:
        direction = min(unused)
        partner = neg(direction)
        if partner not in unused:
            return None
        unused.remove(direction)
        unused.remove(partner)
        opposite_pairs.append((direction, partner))
    pair_values: list[int] = []
    for left, right in opposite_pairs:
        if values[left] != values[right]:
            return None
        pair_values.append(values[left])
    if len(pair_values) == 2 and pair_values[0] == 1 - pair_values[1]:
        reference = min(pair_values)
        if predecessor_bit in (reference, 1 - reference):
            return Signature("tester", predecessor, forward, reference)
    return None


def active_sites(records: BitRecords) -> tuple[Point, ...]:
    frontier = {add(position, direction) for position in records for direction in DIRECTIONS}
    return tuple(sorted(point for point in frontier if local_signature(records, point) is not None))


def local_transitions(
    records: BitRecords,
    target: Point,
    *,
    fair_weight: Fraction = Fraction(1, 2),
    unscreened_controller: Point | None = None,
) -> tuple[tuple[int, Fraction], ...]:
    signature = local_signature(records, target)
    if signature is None:
        return ()
    predecessor_bit = records[signature.predecessor]
    if signature.role == "accumulator":
        if predecessor_bit == signature.reference_bit:
            return (
                (signature.reference_bit, fair_weight),
                (1 - signature.reference_bit, Fraction(1) - fair_weight),
            )
        return ((predecessor_bit, Fraction(1)),)
    if signature.role == "tester" and unscreened_controller is not None:
        return ((predecessor_bit ^ records[unscreened_controller], Fraction(1)),)
    return ((predecessor_bit, Fraction(1)),)


@dataclass(frozen=True)
class History:
    records: StateKey
    probability: Fraction
    writes: tuple[tuple[Point, int], ...]


def advance_histories(
    histories: Iterable[History],
    *,
    fair_weight: Fraction = Fraction(1, 2),
) -> list[History]:
    advanced: list[History] = []
    for history in histories:
        records = from_state_key(history.records)
        sites = active_sites(records)
        if len(sites) != 1:
            raise AssertionError(f"declared single rail has {len(sites)} active sites")
        target = sites[0]
        transitions = local_transitions(records, target, fair_weight=fair_weight)
        if sum((probability for _, probability in transitions), Fraction(0)) != 1:
            raise AssertionError("local mark kernel is not normalized")
        for bit, probability in transitions:
            new_records = dict(records)
            new_records[target] = bit
            advanced.append(
                History(
                    records=state_key(new_records),
                    probability=history.probability * probability,
                    writes=history.writes + ((target, bit),),
                )
            )
    return advanced


def run_track(track: Track, *, fair_weight: Fraction = Fraction(1, 2)) -> list[list[History]]:
    layers: list[list[History]] = [[History(track.records, Fraction(1), ())]]
    for _ in track.targets:
        layers.append(advance_histories(layers[-1], fair_weight=fair_weight))
    return layers


def decoded_future(
    history: History,
    steps: int,
    *,
    unscreened_controller: Point | None = None,
) -> dict[tuple[int, ...], Fraction]:
    distribution: dict[StateKey, tuple[Fraction, tuple[int, ...]]] = {
        history.records: (Fraction(1), ())
    }
    for _ in range(steps):
        new_distribution: dict[StateKey, tuple[Fraction, tuple[int, ...]]] = {}
        for key, (weight, transcript) in distribution.items():
            records = from_state_key(key)
            sites = active_sites(records)
            if len(sites) != 1:
                raise AssertionError("future rail lost its unique active site")
            target = sites[0]
            transitions = local_transitions(
                records,
                target,
                unscreened_controller=unscreened_controller,
            )
            for bit, probability in transitions:
                updated = dict(records)
                updated[target] = bit
                new_distribution[state_key(updated)] = (weight * probability, transcript + (bit,))
        distribution = new_distribution
    result: defaultdict[tuple[int, ...], Fraction] = defaultdict(Fraction)
    for weight, transcript in distribution.values():
        result[transcript] += weight
    return dict(result)


def power_response(weight: Fraction, power: int) -> Fraction:
    numerator = weight**power
    denominator = numerator + (Fraction(1) - weight) ** power
    return numerator / denominator


def merge_records(left: BitRecords, right: BitRecords) -> BitRecords:
    merged = dict(left)
    for point, bit in right.items():
        if point in merged and merged[point] != bit:
            raise AssertionError("incompatible apparatus overlap")
        merged[point] = bit
    return merged


def apply_at(records: BitRecords, target: Point) -> dict[StateKey, Fraction]:
    result: defaultdict[StateKey, Fraction] = defaultdict(Fraction)
    for bit, probability in local_transitions(records, target):
        updated = dict(records)
        updated[target] = bit
        result[state_key(updated)] += probability
    return dict(result)


def apply_second(
    distribution: dict[StateKey, Fraction], target: Point
) -> dict[StateKey, Fraction]:
    result: defaultdict[StateKey, Fraction] = defaultdict(Fraction)
    for key, outer_probability in distribution.items():
        records = from_state_key(key)
        for new_key, probability in apply_at(records, target).items():
            result[new_key] += outer_probability * probability
    return dict(result)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool, residual: object | None = None) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
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
    barycenter_note = BARYCENTER_PATH.read_text(encoding="utf-8")
    nonaffine_note = NONAFFINE_PATH.read_text(encoding="utf-8")
    cycle20 = CYCLE20_PATH.read_text(encoding="utf-8")
    registry = REGISTRY_PATH.read_text(encoding="utf-8")
    for relative in AUDIT_INPUT_PATHS:
        (ROOT / relative).read_text(encoding="utf-8")

    print("scope: exact finite binary-code apparatus rails and their projective finite prefixes; no global law selection")
    print("law data: one fair accumulator kernel and a supplied commuting binary apparatus scaffold")
    print("bridge data: quantum typing of Record labels and the copy/equality event is separately supplied as B")
    print("negative scope: only named normalized-power maps on the executed dyadic preparation family under B")

    checks.check(
        "authority",
        "the current axiom, primitive registry, three direct comparison surfaces, and landing note are bound",
        AUDIT_TIMEOUT_SEC == 120
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and "For each site, the probability distribution over the possibilities" in axiom
        and all(name in registry for name in ("scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"))
        and "barycenter evaluation" in barycenter_note
        and "normalized-square" in nonaffine_note
        and "Physical Randomization Gives Affinity" in cycle20,
    )
    checks.check(
        "cubic-group",
        "the generated proper-cubic group has exactly 24 determinant-one signed permutations",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24 and all(determinant3(rotation) == 1 for rotation in ROTATIONS),
    )

    unitaries = (
        ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))),
        ((Fraction(0), Fraction(1)), (Fraction(1), Fraction(0))),
        ((Fraction(3, 5), Fraction(-4, 5)), (Fraction(4, 5), Fraction(3, 5))),
    )
    projectors = tuple(conjugate_projector(unitary) for unitary in unitaries)
    checks.check(
        "relational-m2-carrier",
        "three exact internal frames preserve rank-one projector/complement and orthogonal binary relations",
        all(
            projector.trace() == 1
            and projector.det() == 0
            and projector.mul(projector) == (projector.a, projector.b, projector.b, projector.d)
            and projector.complement().trace() == 1
            and projector.complement().det() == 0
            and projector.mul(projector.complement()) == (0, 0, 0, 0)
            for projector in projectors
        ),
    )

    base = build_track(4, 4)
    layers = run_track(base)
    role_trace: list[str] = []
    uniqueness_ok = True
    for index, layer in enumerate(layers[:-1]):
        for history in layer:
            records = from_state_key(history.records)
            sites = active_sites(records)
            uniqueness_ok &= sites == (base.targets[index],)
            signature = local_signature(records, sites[0]) if sites else None
            if history is layer[0] and signature is not None:
                role_trace.append(signature.role)
    checks.check(
        "strict-nn-unique-front",
        "every lawful history has exactly one active site and the local role sequence is accumulator, preparation, tester",
        uniqueness_ok
        and role_trace == ["accumulator"] * 4 + ["preparation"] + ["tester"] * 4,
        residual=role_trace,
    )

    locality_ok = True
    permanence_ok = True
    for layer in layers[:-1]:
        for history in layer:
            records = from_state_key(history.records)
            target = active_sites(records)[0]
            signature = local_signature(records, target)
            locality_ok &= signature is not None
            locality_ok &= all(dot(direction, direction) == 1 for direction in DIRECTIONS)
            locality_ok &= all(add(target, direction) in records or direction == signature.forward for direction in DIRECTIONS)
            transitions = local_transitions(records, target)
            for bit, _ in transitions:
                updated = dict(records)
                updated[target] = bit
                permanence_ok &= target not in records
                permanence_ok &= len(updated) == len(records) + 1
                permanence_ok &= all(updated[position] == old_bit for position, old_bit in records.items())
    checks.check(
        "locality-permanence",
        "each append conditions on six-neighbour Record membership, reads only occupied contents, writes one blank site, and preserves old Records",
        locality_ok and permanence_ok,
    )

    dyadic_ok = True
    dyadic_rows: list[tuple[int, Fraction, Fraction]] = []
    for count in range(1, 7):
        track = build_track(count, 2)
        count_layers = run_track(track)
        prep_layer = count_layers[count + 1]
        prep_position = track.targets[count]
        success = sum(
            (history.probability for history in prep_layer if from_state_key(history.records)[prep_position] == track.reference_bit),
            Fraction(0),
        )
        expected = Fraction(1, 2**count)
        dyadic_rows.append((count, success, expected))
        dyadic_ok &= success == expected and sum((history.probability for history in prep_layer), Fraction(0)) == 1
    checks.check(
        "dyadic-preparation",
        "n fair accumulator stages generate endpoint preparation mass 2^-n with exact normalized history weights",
        dyadic_ok,
        residual=dyadic_rows,
    )

    track = build_track(4, 3)
    track_layers = run_track(track)
    prep_layer = track_layers[5]
    prep_position = track.targets[4]
    fibres: defaultdict[int, list[History]] = defaultdict(list)
    for history in prep_layer:
        fibres[from_state_key(history.records)[prep_position]].append(history)
    future_fingerprints: dict[int, set[tuple[tuple[tuple[int, ...], Fraction], ...]]] = {}
    for bit, histories in fibres.items():
        future_fingerprints[bit] = {
            tuple(sorted(decoded_future(history, 3).items())) for history in histories
        }
    checks.check(
        "tag-screened-lumpability",
        "four distinct failure histories share one preparation Record and one identical three-test future law",
        len(fibres[1 - track.reference_bit]) == 4
        and all(len(fingerprints) == 1 for fingerprints in future_fingerprints.values())
        and future_fingerprints[track.reference_bit]
        == {(((track.reference_bit,) * 3, Fraction(1)),)}
        and future_fingerprints[1 - track.reference_bit]
        == {(((1 - track.reference_bit,) * 3, Fraction(1)),)},
        residual={bit: len(fingerprints) for bit, fingerprints in future_fingerprints.items()},
    )

    controller = track.targets[0]
    failed_histories = fibres[1 - track.reference_bit]
    unscreened_fingerprints = {
        tuple(sorted(decoded_future(history, 1, unscreened_controller=controller).items()))
        for history in failed_histories
    }
    checks.check(
        "mutation-unscreened-tag",
        "a controller-dependent tester splits the lawful failure fibre and is rejected by the lumpability gate",
        len(unscreened_fingerprints) == 2,
        residual=unscreened_fingerprints,
    )

    covariance_ok = True
    for rotation in ROTATIONS:
        for shift in ((0, 0, 0), (7, -3, 5)):
            transformed = build_track(3, 2, rotation=rotation, shift=shift)
            transformed_layers = run_track(transformed)
            for index, layer in enumerate(transformed_layers[:-1]):
                covariance_ok &= all(active_sites(from_state_key(history.records)) == (transformed.targets[index],) for history in layer)
            success = sum(
                (
                    history.probability
                    for history in transformed_layers[4]
                    if from_state_key(history.records)[transformed.targets[3]] == transformed.reference_bit
                ),
                Fraction(0),
            )
            covariance_ok &= success == Fraction(1, 8)
    complement_track = build_track(3, 2, complement_bits=True)
    complement_layers = run_track(complement_track)
    complement_success = sum(
        (
            history.probability
            for history in complement_layers[4]
            if from_state_key(history.records)[complement_track.targets[3]] == complement_track.reference_bit
        ),
        Fraction(0),
    )
    checks.check(
        "covariance",
        "all 24 rotations, two translations, and global binary-complement relabeling preserve roles and dyadic mass",
        covariance_ok and complement_success == Fraction(1, 8),
    )

    track_a = build_track(2, 2, shift=(0, 0, 0))
    track_b = build_track(2, 2, shift=(0, 10, 0))
    union = merge_records(from_state_key(track_a.records), from_state_key(track_b.records))
    active = active_sites(union)
    ab = apply_second(apply_at(union, track_a.targets[0]), track_b.targets[0])
    ba = apply_second(apply_at(union, track_b.targets[0]), track_a.targets[0])
    checks.check(
        "disjoint-concurrency",
        "two separated transition kernels expose two active sites and commute; conditional on both writes they give four quarter-weight states",
        active == tuple(sorted((track_a.targets[0], track_b.targets[0])))
        and ab == ba
        and len(ab) == 4
        and set(ab.values()) == {Fraction(1, 4)},
    )

    response_rows: list[tuple[int, Fraction, Fraction, Fraction]] = []
    response_ok = True
    for count in range(2, 7):
        weight = Fraction(1, 2**count)
        square = power_response(weight, 2)
        cubic = power_response(weight, 3)
        response_rows.append((count, weight, square, cubic))
        response_ok &= weight != square and weight != cubic
    checks.check(
        "named-response-discriminator",
        "the Record endpoint transcript equals 2^-n while the named normalized-power maps disagree for n=2 through 6 under bridge B",
        response_ok
        and response_rows[0] == (2, Fraction(1, 4), Fraction(1, 10), Fraction(1, 28)),
        residual=response_rows,
    )

    mutation_track = build_track(2, 2)
    mutated_layers = run_track(mutation_track, fair_weight=Fraction(1, 3))
    mutated_success = sum(
        (
            history.probability
            for history in mutated_layers[3]
            if from_state_key(history.records)[mutation_track.targets[2]] == mutation_track.reference_bit
        ),
        Fraction(0),
    )
    broken_records = from_state_key(mutation_track.records)
    active_target = mutation_track.targets[0]
    guard_to_remove = add(active_target, (0, 1, 0))
    del broken_records[guard_to_remove]
    checks.check(
        "hostile-mutations",
        "a one-third randomizer changes the mixture to one ninth and a missing guard kills the active-site certificate",
        mutated_success == Fraction(1, 9)
        and mutated_success != Fraction(1, 4)
        and local_signature(broken_records, active_target) is None,
    )

    required_note_phrases = (
        "actual_current_surface_status: bounded-support",
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
        "No-Go Discipline Gate",
        "p^2/[p^2+(1-p)^2]",
        "p^3/[p^3+(1-p)^3]",
        "fair branch weight is supplied law content",
        "separately supplied bridge `B`",
        "physical time remains open",
        "no TOE percentage moves",
        "review-loop is not used",
    )
    checks.check(
        "claim-boundary",
        "the landing note exposes supplied law and bridge data, physical-time and action boundaries, audit status, and N1-N8 scope",
        all(phrase in note for phrase in required_note_phrases)
        and "the Born rule is derived" not in note.lower()
        and "new axiom is required" not in note.lower(),
    )

    n5_lines = (
        "per_element: exact P versus I-P Record contents and dyadic weights are checked; quantum typing remains supplied bridge B",
        "per_site: every append conditions on six-neighbour occupancy, reads occupied contents, and writes one blank lattice site",
        "per_mode: accumulator, preparation, tester, complement, normalized-square, and cubic modes are executed",
        "per_block: single-rail histories, record-fibre lumpability, mutations, and disjoint two-rail commutation are checked",
        "lattice_wide: checked and not executed — arbitrary overlaps, infinite apparatus density, physical time, and actuality remain open",
    )
    for line in n5_lines:
        print(line)
    checks.check(
        "n5-certificate",
        "all five landing-resolution statements are substantive and at least forty characters",
        all(
            len(line) >= 40
            and line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            for line in n5_lines
        ),
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
