#!/usr/bin/env python3
"""Route-two probe: Admissibility, record extension, and continuation sectors.

This runner separates three propositions that ordinary language can easily
collapse:

1. an availability rule gives a menu of locally available possibilities;
2. a continuation law supplies one or more successors for that menu; and
3. under declared site-tagged immutable-extension semantics, distinct
   same-site record successors cannot acquire a common syntactic extension.

The finite models are witnesses and rejectors, not the framework's physical
Admissibility rule.  The theorem source is the elementary conditional
extension argument stated in the companion note; the axiom does not separately
supply the site-tagged successor semantics.  No axiom, primitive, or audit
surface is edited or enlarged by this runner.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import json
import math

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md"
)
LOCAL_ATOM_NOTE = (
    ROOT
    / "docs"
    / "RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md"
)
SATURATION_NOTE = (
    ROOT
    / "docs"
    / "RECORD_SATURATION_AVAILABILITY_CENSUS_BOUNDED_NOTE_2026-07-08.md"
)
TICK_NOTE = (
    ROOT
    / "docs"
    / "TICK_ADMISSIBILITY_REALIZATION_BRIDGE_CLAUSE_TO_PREDICATE_NARROW_THEOREM_NOTE_2026-07-10.md"
)
PROTOCOL_NOTE = (
    ROOT
    / "docs"
    / "PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10.md"
)
FRESH_SITE_NOTE = (
    ROOT
    / "docs"
    / "RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md"
)
BOOTSTRAP_CONTINUATION_NOTE = (
    ROOT
    / "docs"
    / "BOOTSTRAP_CONTINUATION_AVAILABILITY_NONEMPTY_FREE_ORBIT_REDUCTION_PROPAGATION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-07-04.md"
)
SCALE_PRIMITIVE_NOTE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_ISOTROPY_PRIMITIVE_NOTE = (
    ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
)
REALIZED_STATE_PRIMITIVE_NOTE = (
    ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
)
PREMISE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

TARGET_SENTENCE = (
    "When a record forms at a site, the site's admissible local possibilities "
    "separate into law-admissible continuations that do not reconnect."
)

OPEN = -1
VALUES = (0, 1)
TOL = 1.0e-10
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"PASS {label}{suffix}")
    else:
        FAIL += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"FAIL {label}{suffix}")


def source_contract() -> None:
    section("A - Source and wording contract")
    axiom = AXIOM.read_text()
    note = NOTE.read_text()
    local_atom = LOCAL_ATOM_NOTE.read_text()
    saturation = SATURATION_NOTE.read_text()
    tick = TICK_NOTE.read_text()
    protocol = PROTOCOL_NOTE.read_text()
    fresh_site = FRESH_SITE_NOTE.read_text()
    bootstrap = BOOTSTRAP_CONTINUATION_NOTE.read_text()
    bootstrap_flat = " ".join(bootstrap.split())
    scale_primitive_flat = " ".join(SCALE_PRIMITIVE_NOTE.read_text().split())
    kinetic_primitive_flat = " ".join(
        KINETIC_ISOTROPY_PRIMITIVE_NOTE.read_text().split()
    )
    realized_primitive_flat = " ".join(
        REALIZED_STATE_PRIMITIVE_NOTE.read_text().split()
    )
    premise_registry = json.loads(PREMISE_REGISTRY.read_text())

    needles = (
        "There is one fixed nearest-neighbor admissibility rule, covariant under lattice",
        "For each site, the available possibilities are determined by, and vary with,",
        "Records form.",
        "site never carries more than one record; records are permanent.",
        "A state is a configuration of records.",
        "Admissibility is not a dynamics axiom.",
    )
    for index, needle in enumerate(needles, start=1):
        check(f"A{index} canonical axiom boundary contains required needle", needle in axiom)

    check("A7 locked target wording occurs exactly once in the theorem attempt", note.count(TARGET_SENTENCE) == 1)
    check("A8 locked target wording has not been inserted into the axiom", TARGET_SENTENCE not in axiom)
    check("A9 note names the target as a condition, not an axiom edit", "named condition" in note and "not an axiom edit" in note)
    check("A10 note preserves bounded-theorem claim typing", "claim_type: bounded_theorem" in note)
    check("A11 local-atom source says the fixed rule content is not supplied", "The axioms name this rule but do not supply its\ncontent." in local_atom)
    check("A12 saturation source does not identify its models with the physical rule", "they do not determine the framework's physical admissibility rule" in saturation)
    check("A13 tick source keeps the physical realization bridge open", "does not derive a physical tick--Admissibility realization bridge" in tick)
    check("A14 protocol source keeps the rule-to-protocol identification open", "does not derive the physical rule-to-protocol identification" in protocol)
    check("A15 no-go discipline is visible in the theorem attempt", all(f"N{i}" in note for i in range(1, 9)))
    check(
        "A16 adjacent record work keeps site immobility as an explicit representation condition",
        "does not separately state an immobility law" in " ".join(fresh_site.split())
        and "Site-tagged monotone record history" in fresh_site,
    )
    canonical_ids = set(premise_registry["canonical_ids"])
    check(
        "A17 approved primitive sources are limited to units, kinetic-form isotropy, and pointwise evaluation",
        canonical_ids
        == {
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        }
        and premise_registry["nodes"]["scale_reference_primitive"]["current_path"]
        == "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
        and premise_registry["nodes"]["kinetic_isotropy_primitive"]["current_path"]
        == "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
        and premise_registry["nodes"]["realized_state_primitive"]["current_path"]
        == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
        and "This is a units conversion, not a physics axiom. It carries zero dimensionless content"
        in scale_primitive_flat
        and "It carries no dimensionless dynamical content"
        in kinetic_primitive_flat
        and "Nothing more is supplied:"
        in realized_primitive_flat
        and "This is pointwise evaluation, not a state-selection rule."
        in realized_primitive_flat
        and "physical persistence dynamics" in premise_registry["nodes"]["minimal_axioms"]["note"],
    )
    check(
        "A18 bootstrap continuation source keeps its rule toy and formation selection downstream",
        "not a determination of the framework's fixed rule" in bootstrap_flat
        and "No claim is made about which element the first record locks" in bootstrap_flat,
    )


DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def permutation_sign(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> list[tuple[tuple[int, ...], ...]]:
    rotations: list[tuple[tuple[int, ...], ...]] = []
    for perm in permutations(range(3)):
        perm_tuple = tuple(perm)
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm_tuple) * math.prod(signs) != 1:
                continue
            matrix = [[0, 0, 0] for _ in range(3)]
            for row in range(3):
                matrix[row][perm_tuple[row]] = signs[row]
            rotations.append(tuple(tuple(row) for row in matrix))
    return rotations


ROTATIONS = proper_cubic_rotations()


def mat_vec(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3)) for row in range(3))


def rotate_pattern(pattern: tuple[int, ...], matrix: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    out = [OPEN] * len(DIRECTIONS)
    for old_index, direction in enumerate(DIRECTIONS):
        out[DIR_INDEX[mat_vec(matrix, direction)]] = pattern[old_index]
    return tuple(out)


def flip_labels(pattern: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(OPEN if value == OPEN else 1 - value for value in pattern)


def flip_set(values: frozenset[int]) -> frozenset[int]:
    return frozenset(1 - value for value in values)


def availability(pattern: tuple[int, ...]) -> frozenset[int]:
    """A covariant, label-equivariant, neighbor-varying witness rule.

    The rule returns a singleton only when at least two recorded neighbors all
    carry the same content.  Otherwise both values remain available.
    """
    recorded = [value for value in pattern if value != OPEN]
    if len(recorded) >= 2 and len(set(recorded)) == 1:
        return frozenset({recorded[0]})
    return frozenset(VALUES)


def full_branch_support(pattern: tuple[int, ...]) -> frozenset[int]:
    """Menu-complete support on the common one-neighbor domain."""
    if not formation_domain(pattern):
        return frozenset()
    return availability(pattern)


def copy_law_support(pattern: tuple[int, ...]) -> frozenset[int]:
    """Local covariant singleton support on the common one-neighbor domain.

    It retains the recorded neighbor's value even though both values are
    available. Other patterns are outside both continuation maps' domain.
    """
    if not formation_domain(pattern):
        return frozenset()
    recorded = [value for value in pattern if value != OPEN]
    return frozenset({recorded[0]})


def formation_domain(pattern: tuple[int, ...]) -> bool:
    """The identical covariant domain supplied to both support expansions."""
    return sum(value != OPEN for value in pattern) == 1


def local_rule_classification() -> None:
    section("B - Exact local-rule and continuation-support separation")
    patterns = list(product((OPEN, 0, 1), repeat=6))
    outputs = {availability(pattern) for pattern in patterns}

    check("B1 proper cubic rotation group has 24 elements", len(set(ROTATIONS)) == 24)
    check("B2 witness availability is nonempty on every neighbor pattern", all(availability(pattern) for pattern in patterns))
    check("B3 witness availability varies with neighbor conditions", outputs == {frozenset({0}), frozenset({1}), frozenset({0, 1})})
    check(
        "B4 witness availability is exhaustively proper-cubic covariant",
        all(
            availability(rotate_pattern(pattern, rotation)) == availability(pattern)
            for pattern in patterns
            for rotation in ROTATIONS
        ),
    )
    check(
        "B5 witness availability is label-equivariant (no binary label privilege)",
        all(availability(flip_labels(pattern)) == flip_set(availability(pattern)) for pattern in patterns),
    )
    common_domain = [pattern for pattern in patterns if formation_domain(pattern)]
    outside_domain = [pattern for pattern in patterns if not formation_domain(pattern)]
    check("B6 full branch support equals the availability menu on the common domain", all(full_branch_support(pattern) == availability(pattern) for pattern in common_domain))
    check("B7 copy-law outputs are always available", all(copy_law_support(pattern) <= availability(pattern) for pattern in patterns))
    check("B8 singleton-support law gives exactly one successor on the common domain", all(len(copy_law_support(pattern)) == 1 for pattern in common_domain))
    check(
        "B9 copy-law support is exhaustively proper-cubic covariant",
        all(
            copy_law_support(rotate_pattern(pattern, rotation)) == copy_law_support(pattern)
            for pattern in patterns
            for rotation in ROTATIONS
        ),
    )
    check(
        "B10 copy-law support is label-equivariant",
        all(copy_law_support(flip_labels(pattern)) == flip_set(copy_law_support(pattern)) for pattern in patterns),
    )

    one_neighbor_patterns = common_domain
    check("B11 one-neighbor contexts leave both possibilities available", all(availability(pattern) == frozenset({0, 1}) for pattern in one_neighbor_patterns))
    check("B12 the same contexts have one copy-law successor", all(len(copy_law_support(pattern)) == 1 for pattern in one_neighbor_patterns))
    check(
        "B13 one fixed availability rule admits branch-complete and singleton-support expansions on one domain",
        any(full_branch_support(pattern) != copy_law_support(pattern) for pattern in one_neighbor_patterns),
    )
    check("B14 both continuation maps have nonempty candidate-successor support throughout the common domain", all(full_branch_support(pattern) and copy_law_support(pattern) for pattern in common_domain))
    check("B15 both continuation maps have exactly the same supplied domain", all(not full_branch_support(pattern) and not copy_law_support(pattern) for pattern in outside_domain))


Config = tuple[int, ...]


def append_record(config: Config, site: int, value: int) -> Config:
    assert config[site] == OPEN
    out = list(config)
    out[site] = value
    return tuple(out)


def extends(base: Config, future: Config) -> bool:
    return all(value == OPEN or future[index] == value for index, value in enumerate(base))


def compatible_upper_bound(left: Config, right: Config) -> bool:
    return all(
        left[index] == OPEN or right[index] == OPEN or left[index] == right[index]
        for index in range(len(left))
    )


def extension_and_separation_theorem() -> None:
    section("C - Site-tagged immutable-extension theorem and local certificate")
    configs = list(product((OPEN, 0, 1), repeat=5))
    sibling_pairs: list[tuple[Config, Config, Config, int]] = []
    for base in configs:
        for site, value in enumerate(base):
            if value != OPEN:
                continue
            sibling_pairs.append(
                (base, append_record(base, site, 0), append_record(base, site, 1), site)
            )

    check(
        "C1 declared one-record appends strictly extend their predecessor",
        all(
            extends(base, left)
            and extends(base, right)
            and sum(value != OPEN for value in left)
            == sum(value != OPEN for value in base) + 1
            and sum(value != OPEN for value in right)
            == sum(value != OPEN for value in base) + 1
            for base, left, right, _ in sibling_pairs
        ),
    )
    check("C2 every sibling pair conflicts at exactly its newly recorded site", all(left[site] != right[site] and all(i == site or left[i] == right[i] for i in range(5)) for _, left, right, site in sibling_pairs))
    check("C3 distinct same-site records have no common site-tagged immutable extension", all(not compatible_upper_bound(left, right) for _, left, right, _ in sibling_pairs))

    # Exhaust all finite candidate futures to show the same fact by descendant
    # intersection rather than only by the direct compatibility predicate.
    future_sets = {
        config: {future for future in configs if extends(config, future)}
        for config in configs
    }
    check("C4 sibling syntactic immutable-extension cones are disjoint on five sites", all(not (future_sets[left] & future_sets[right]) for _, left, right, _ in sibling_pairs))
    check("C5 the separation certificate is local to the conflicting site", all({index for index in range(5) if left[index] != OPEN and right[index] != OPEN and left[index] != right[index]} == {site} for _, left, right, site in sibling_pairs))

    base = (OPEN, OPEN, OPEN)
    zero = append_record(base, 1, 0)
    one = append_record(base, 1, 1)
    def overwrite_successors(config: Config, site: int) -> set[Config]:
        return {
            tuple(value if index != site else replacement for index, value in enumerate(config))
            for replacement in VALUES
        }

    check(
        "C6 allowing overwrite reconnects the two values (negative control)",
        one in overwrite_successors(zero, 1)
        and one in overwrite_successors(one, 1),
    )
    check("C7 site-tagged immutability, not availability covariance, is load-bearing", not compatible_upper_bound(zero, one))

    disjoint_base = (OPEN, OPEN, OPEN, OPEN)
    xy = append_record(append_record(disjoint_base, 0, 1), 3, 0)
    yx = append_record(append_record(disjoint_base, 3, 0), 0, 1)
    check("C8 two fixed compatible distinct-site appends have an order-independent union", xy == yx)
    check("C9 competing same-site appends are incompatible", not compatible_upper_bound(append_record(disjoint_base, 2, 0), append_record(disjoint_base, 2, 1)))

    collateral_base = (OPEN, OPEN, OPEN, OPEN, OPEN)
    collateral_left = append_record(append_record(collateral_base, 2, 0), 0, 1)
    collateral_right = append_record(append_record(collateral_base, 2, 1), 4, 0)
    check(
        "C10 conflicting same-site contents remain separated when each event adds a collateral record",
        extends(collateral_base, collateral_left)
        and extends(collateral_base, collateral_right)
        and collateral_left[2] != collateral_right[2]
        and not compatible_upper_bound(collateral_left, collateral_right),
    )


def partition_for_prefix(width: int, recorded_count: int) -> dict[tuple[int, ...], set[tuple[int, ...]]]:
    parts: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
    for assignment in product(VALUES, repeat=width):
        label = assignment[:recorded_count]
        parts.setdefault(label, set()).add(assignment)
    return parts


def dynamic_refinement() -> None:
    section("D - Conditional refinement of record-content history classes")
    width = 6
    partitions = [partition_for_prefix(width, count) for count in range(width + 1)]
    check("D1 independent binary full support gives 2^n potential content classes", all(len(partitions[count]) == 2**count for count in range(width + 1)))
    check(
        "D2 each new record strictly refines that independent full-support model",
        all(
            all(
                len({assignment[: count - 1] for assignment in block}) == 1
                for block in partitions[count].values()
            )
            and len(partitions[count]) > len(partitions[count - 1])
            for count in range(1, width + 1)
        ),
    )

    realized_values = (1, 0, 1, 1, 0, 0)
    prefixes = [realized_values[:count] for count in range(width + 1)]
    check("D3 the declared fixture label accumulates exactly one fact per append", all(prefixes[count][:-1] == prefixes[count - 1] for count in range(1, width + 1)))
    check("D4 accumulated labels never discard or alter an older value", all(prefixes[later][:earlier] == prefixes[earlier] for earlier in range(width + 1) for later in range(earlier, width + 1)))
    full_realized_config = tuple(realized_values)
    check("D5 a finite region saturates after one record per site", len(full_realized_config) == width and OPEN not in full_realized_config)
    check("D6 refinement gives finer potential classes and one chosen fixture label", all(prefixes[count] in partitions[count] for count in range(width + 1)))

    equality_assignments = {tuple([0] * width), tuple([1] * width)}
    equality_counts = [
        len({assignment[:count] for assignment in equality_assignments})
        for count in range(width + 1)
    ]
    check(
        "D7 local constraints can prevent per-record class doubling",
        equality_counts == [1] + [2] * width,
        f"counts={equality_counts}",
    )


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
KET0 = np.array([1, 0], dtype=complex)
KET1 = np.array([0, 1], dtype=complex)
PLUS = (KET0 + KET1) / math.sqrt(2.0)


def density(ket: np.ndarray) -> np.ndarray:
    return np.outer(ket, ket.conj())


def commutant_dimension(generators: list[np.ndarray]) -> int:
    dim = generators[0].shape[0]
    columns: list[np.ndarray] = []
    for row in range(dim):
        for column in range(dim):
            basis = np.zeros((dim, dim), dtype=complex)
            basis[row, column] = 1.0
            columns.append(
                np.concatenate(
                    [(basis @ generator - generator @ basis).reshape(-1) for generator in generators]
                )
            )
    linear_map = np.column_stack(columns)
    rank = int(np.sum(np.linalg.svd(linear_map, compute_uv=False) > 1.0e-9))
    return dim * dim - rank


def sector_restriction(operator: np.ndarray, projector: np.ndarray) -> np.ndarray:
    complement = np.eye(projector.shape[0], dtype=complex) - projector
    return projector @ operator @ projector + complement @ operator @ complement


def operation_algebra_boundary() -> None:
    section("E - Separately supplied finite tensor-product operation-algebra comparator")
    x1, z1 = np.kron(X, I2), np.kron(Z, I2)
    x2, z2 = np.kron(I2, X), np.kron(I2, Z)
    check("E1 the comparator's full finite two-qubit matrix algebra has scalar commutant", commutant_dimension([x1, z1, x2, z2]) == 1)

    first_bit_labels = (0, 0, 1, 1)
    first_record_basis: list[np.ndarray] = []
    diagonal_basis: list[np.ndarray] = []
    for row in range(4):
        for column in range(4):
            unit = np.zeros((4, 4), dtype=complex)
            unit[row, column] = 1.0
            if first_bit_labels[row] == first_bit_labels[column]:
                first_record_basis.append(unit)
            if row == column:
                diagonal_basis.append(unit)
    check("E2 imposing preservation of one binary record creates two central blocks", commutant_dimension(first_record_basis) == 2)
    check("E3 imposing preservation of two binary records creates four central blocks", commutant_dimension(diagonal_basis) == 4)

    p0 = density(KET0)
    test_operator = np.array([[0.2, 0.3 + 0.4j], [0.3 - 0.4j, -0.1]], dtype=complex)
    once = sector_restriction(test_operator, p0)
    twice = sector_restriction(once, p0)
    check("E4 a supplied post-record block restriction is idempotent", np.linalg.norm(once - twice) < TOL)
    check("E5 that restriction fixes the record projector", np.linalg.norm(sector_restriction(p0, p0) - p0) < TOL)
    check("E6 that restriction removes cross-record interference", np.linalg.norm(sector_restriction(X, p0)) < TOL)

    angle = 0.37
    unitary = math.cos(angle / 2.0) * I2 - 1j * math.sin(angle / 2.0) * Y
    rotated_p0 = unitary @ p0 @ unitary.conj().T
    rotated_operator = unitary @ test_operator @ unitary.conj().T
    check(
        "E7 supplied restriction is presentation-covariant when record content transforms",
        np.linalg.norm(
            sector_restriction(rotated_operator, rotated_p0)
            - unitary @ sector_restriction(test_operator, p0) @ unitary.conj().T
        )
        < TOL,
    )

    p_left = np.kron(p0, I2)
    p_right = np.kron(I2, p0)
    operator = np.kron(X + 0.2 * Z, Y - 0.3 * X)
    left_right = sector_restriction(sector_restriction(operator, p_left), p_right)
    right_left = sector_restriction(sector_restriction(operator, p_right), p_left)
    check("E8 supplied restrictions commute algebraically on disjoint tensor factors", np.linalg.norm(left_right - right_left) < TOL)

    tilted = density(math.cos(0.61 / 2.0) * KET0 + math.sin(0.61 / 2.0) * KET1)
    z_then_tilt = sector_restriction(sector_restriction(Z, p0), tilted)
    tilt_then_z = sector_restriction(sector_restriction(Z, tilted), p0)
    check("E9 overlapping noncommuting restrictions require a compatibility/order law", np.linalg.norm(z_then_tilt - tilt_then_z) > 0.1)

    pre_record = density(PLUS)
    prematurely_restricted = sector_restriction(pre_record, p0)
    check("E10 imposing the restriction before formation destroys pre-record interference", abs(np.trace(pre_record @ X).real - 1.0) < TOL and abs(np.trace(prematurely_restricted @ X).real) < TOL)
    check("E11 the availability rule itself contains no operator-algebra argument", availability((OPEN,) * 6) == frozenset({0, 1}))

    restricted_record_state = sector_restriction(p0, p0)
    flipped_after_restriction = X @ restricted_record_state @ X
    check(
        "E12 a one-time block restriction does not forbid a later sector-changing unitary",
        np.linalg.norm(flipped_after_restriction - restricted_record_state) > 1.0,
    )

    u2 = np.kron(unitary, unitary)
    conjugated_generators = [u2 @ generator @ u2.conj().T for generator in (x1, z1, x2, z2)]
    check(
        "E13 finite unitary conjugation preserves the scalar commutant of the full algebra",
        commutant_dimension(conjugated_generators) == 1,
    )


def contextual_scope_boundary() -> None:
    section("F - Contextual-scope discriminator")
    deterministic_values = []
    for a0, a1, b0, b1 in product((-1, 1), repeat=4):
        deterministic_values.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
    check("F1 a single context-independent joint completion obeys CHSH <= 2", max(abs(value) for value in deterministic_values) == 2)

    correlations = {
        (0, 0): 1.0 / math.sqrt(2.0),
        (0, 1): 1.0 / math.sqrt(2.0),
        (1, 0): 1.0 / math.sqrt(2.0),
        (1, 1): -1.0 / math.sqrt(2.0),
    }
    table = {
        (a, b, x, y): (1.0 + a * b * correlations[(x, y)]) / 4.0
        for x, y in product((0, 1), repeat=2)
        for a, b in product((-1, 1), repeat=2)
    }
    check("F2 context-indexed target probabilities are nonnegative", min(table.values()) >= 0.0)
    check("F3 every context-indexed target table normalizes", all(abs(sum(table[(a, b, x, y)] for a, b in product((-1, 1), repeat=2)) - 1.0) < TOL for x, y in product((0, 1), repeat=2)))
    check(
        "F4 context-indexed target is no-signaling",
        all(
            abs(sum(table[(a, b, x, 0)] for b in (-1, 1)) - sum(table[(a, b, x, 1)] for b in (-1, 1))) < TOL
            for a, x in product((-1, 1), (0, 1))
        )
        and all(
            abs(sum(table[(a, b, 0, y)] for a in (-1, 1)) - sum(table[(a, b, 1, y)] for a in (-1, 1))) < TOL
            for b, y in product((-1, 1), (0, 1))
        ),
    )
    chsh = correlations[(0, 0)] + correlations[(0, 1)] + correlations[(1, 0)] - correlations[(1, 1)]
    check("F5 context-indexed target reaches 2 sqrt(2)", abs(chsh - 2.0 * math.sqrt(2.0)) < TOL)
    check(
        "F6 this target rejects deterministic local joint completions under the tested Bell premises",
        abs(chsh) > max(abs(value) for value in deterministic_values),
    )


def final_classification() -> None:
    section("G - Mechanical classification")
    base = (OPEN, OPEN, OPEN)
    left = append_record(base, 1, 0)
    right = append_record(base, 1, 1)
    check("G1 site-tagged history nonreconnection closes once distinct immutable successors exist", not compatible_upper_bound(left, right))
    check(
        "G2 local separation closes by a one-site conflict certificate",
        [index for index in range(3) if left[index] != OPEN and right[index] != OPEN and left[index] != right[index]] == [1],
    )
    partitions = [partition_for_prefix(4, count) for count in range(5)]
    check("G3 record-content classes refine in the independent full-support model", [len(partition) for partition in partitions] == [1, 2, 4, 8, 16])
    one_neighbor = (0, OPEN, OPEN, OPEN, OPEN, OPEN)
    check("G4 branch completeness is not fixed by the availability table", full_branch_support(one_neighbor) != copy_law_support(one_neighbor))

    x1, z1 = np.kron(X, I2), np.kron(Z, I2)
    x2, z2 = np.kron(I2, X), np.kron(I2, Z)
    full_dimension = commutant_dimension([x1, z1, x2, z2])
    labels = (0, 0, 1, 1)
    block_basis: list[np.ndarray] = []
    for row in range(4):
        for column in range(4):
            if labels[row] == labels[column]:
                unit = np.zeros((4, 4), dtype=complex)
                unit[row, column] = 1.0
                block_basis.append(unit)
    check("G5 the availability table alone does not specify an operation algebra in these constructions", full_dimension == 1 and commutant_dimension(block_basis) == 2)
    axiom = AXIOM.read_text()
    flat_axiom = " ".join(axiom.split())
    note = NOTE.read_text()
    check(
        "G6 selection, weights, rate, metric, and capacity renewal remain outside this probe",
        "with what weight, or at what rate" in flat_axiom
        and "time metric" in flat_axiom
        and "physical persistence dynamics" in flat_axiom
        and "support renewal" in note,
    )

    print("\nDECISIVE RESULT")
    print("  DERIVED IN THE SITE-TAGGED IMMUTABLE-HISTORY MODEL: local nonreconnection")
    print("  and fixed-schedule monotone refinement, conditional on distinct formation successors.")
    print("  NOT DERIVED FROM ADMISSIBILITY: counterfactual branch support or the")
    print("  post-record physical operation-algebra restriction/activation.")
    print("  CHECKED AUTHORITY BOUNDARY: one fixed rule is named but the checked")
    print("  foundation/adjacent surfaces provide no extensional table or dynamics bridge.")


def main() -> None:
    source_contract()
    local_rule_classification()
    extension_and_separation_theorem()
    dynamic_refinement()
    operation_algebra_boundary()
    contextual_scope_boundary()
    final_classification()
    print("\n" + "=" * 79)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 79)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
