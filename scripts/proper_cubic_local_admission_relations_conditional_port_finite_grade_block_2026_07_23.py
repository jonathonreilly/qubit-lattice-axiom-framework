#!/usr/bin/env python3
"""Dependency-clean finite admission/port/grade substrate certificate.

This runner reconstructs, without campaign-module imports, the exact finite
content needed for three deliberately narrow statements:

1. five displayed radius-one, proper-cubic-invariant Boolean relations on a
   six-direction word are total, nonconstant, and pairwise extensionally
   distinct;
2. unique quorum feeds one explicit conditional port, followed by a supplied
   finite lock/readout preservation algebra;
3. one supplied endpoint-to-unary calibration feeds a finite denominator-64
   grade block.

The runner derives no actuality or framework-Record identification.  The
finite grade and its complete-block count identity supply no probability,
Born-calibration, corpus, or realized-history bridge.  Physical M2 compilation
and formation-law selection are outside the proved finite scope.

The implementation is Python-standard-library only.  It does not invoke git,
subprocesses, a network, archived objects, or another runner.
"""

from __future__ import annotations

import ast
from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-07-23"
AUTHORITY = "none"
AUDIT = "unset"
CLAIM_TYPE = "bounded_theorem"
NOTE = ROOT / "docs" / (
    "PROPER_CUBIC_LOCAL_ADMISSION_RELATIONS_CONDITIONAL_PORT_FINITE_"
    "GRADE_BLOCK_BOUNDED_THEOREM_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs" / (
    "proper_cubic_local_admission_relations_conditional_port_finite_"
    "grade_block_receipt_2026_07_23.json"
)
CACHE = ROOT / "logs" / "runner-cache" / (
    "proper_cubic_local_admission_relations_conditional_port_finite_"
    "grade_block_2026_07_23.txt"
)
AUDIT_INPUT_PATHS = (
    "docs/PROPER_CUBIC_LOCAL_ADMISSION_RELATIONS_CONDITIONAL_PORT_FINITE_"
    "GRADE_BLOCK_BOUNDED_THEOREM_NOTE_2026-07-23.md",
)

PASS = 0
FAIL = 0
CHECKS: list[dict[str, object]] = []


def check(label: str, condition: object, detail: object = "") -> bool:
    """Record and print one deterministic check row."""
    global PASS, FAIL
    accepted = bool(condition)
    PASS += int(accepted)
    FAIL += int(not accepted)
    CHECKS.append({"label": label, "pass": accepted, "detail": detail})
    print("PASS" if accepted else "FAIL", label, "::", detail)
    return accepted


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# Proper-cubic action on the six directed nearest-neighbor labels.
# ---------------------------------------------------------------------------
Vector = tuple[int, int, int]
Matrix = tuple[Vector, Vector, Vector]
DIRECTIONS: tuple[Vector, ...] = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
AXES: tuple[Vector, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def determinant(matrix: Matrix) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_frames() -> tuple[Matrix, ...]:
    frames: list[Matrix] = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix: Matrix = tuple(  # type: ignore[assignment]
                tuple(signs[row] if column == permutation[row] else 0
                      for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                frames.append(matrix)
    return tuple(frames)


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(  # type: ignore[return-value]
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(  # type: ignore[return-value]
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )


def rotate_six(word: tuple[int, ...], frame: Matrix) -> tuple[int, ...]:
    validate_six_word(word)
    output = [0] * 6
    for old_direction, bit in enumerate(word):
        new_direction = DIRECTIONS.index(matvec(frame, DIRECTIONS[old_direction]))
        output[new_direction] = bit
    return tuple(output)


def axis_permutation(frame: Matrix) -> tuple[int, int, int]:
    return tuple(
        next(index for index, component in enumerate(matvec(frame, axis)) if component)
        for axis in AXES
    )  # type: ignore[return-value]


def rotate_axis_word(word: tuple[int, int, int], frame: Matrix) -> tuple[int, int, int]:
    output = [0, 0, 0]
    for old_axis, new_axis in enumerate(axis_permutation(frame)):
        output[new_axis] = word[old_axis]
    return tuple(output)  # type: ignore[return-value]


def frame_certificate() -> dict[str, object]:
    frames = proper_cubic_frames()
    unique = len(set(frames)) == 24
    image_failures = sum(
        set(matvec(frame, direction) for direction in DIRECTIONS) != set(DIRECTIONS)
        for frame in frames
    )
    group_failures = 0
    for left, right in product(frames, repeat=2):
        group_failures += int(matmul(left, right) not in frames)
    result = {
        "proper_cubic_frames": len(frames),
        "unique": unique,
        "direction_image_failures": image_failures,
        "ordered_frame_products": len(frames) ** 2,
        "group_closure_failures": group_failures,
        "pass": unique and image_failures == group_failures == 0,
    }
    check("24 proper-cubic frames form a closed action", result["pass"], result)
    return result


# ---------------------------------------------------------------------------
# Five explicit local admission relations and exact model separation.
# ---------------------------------------------------------------------------
RULES: dict[str, frozenset[int]] = {
    "unique_quorum": frozenset((1,)),
    "odd_shells": frozenset((1, 3, 5)),
    "nonempty": frozenset((1, 2, 3, 4, 5, 6)),
    "low_density": frozenset((1, 2)),
    "even_nonzero": frozenset((2, 4, 6)),
}

SUPPLIED_STRUCTURE = (
    "six directed nearest-neighbor labels and their opposite pairing",
    "five static accepted-shell sets defining five candidate relations",
    "freshness Boolean and uniform tiling convention",
    "unique-quorum choice for the conditional candidate port",
    "lane-zero member/receipt adapter, blank output fields, and ready token",
    "LOCK genesis, transient/readout rails, and finite generator list",
    "trivial proper-cubic action on scalar payload and readout lanes",
    "endpoint-to-count calibration count=2*(endpoint_plus+endpoint_minus)",
    "equally weighted 4x4x4 address chart and eight-label convention",
    "complete-block rule and unsigned-axis/sign-trivial auxiliary frame action",
    "original endpoint word retained for controlled uncompute",
    "finite noiseless Boolean operations",
)
EXPECTED_CENSUS = {
    "unique_quorum": (6, 6, 0),
    "odd_shells": (32, 26, 6),
    "nonempty": (63, 41, 22),
    "low_density": (21, 21, 0),
    "even_nonzero": (31, 15, 16),
}


def validate_six_word(word: tuple[int, ...]) -> None:
    if len(word) != 6 or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("six binary direction fields required")


def relation_answer(shells: frozenset[int], word: tuple[int, ...], *, fresh: bool = True) -> int:
    validate_six_word(word)
    if type(fresh) is not bool:
        raise ValueError("freshness must be Boolean")
    return int(fresh and sum(word) in shells)


def relation_certificate() -> dict[str, object]:
    frames = proper_cubic_frames()
    words = tuple(product((0, 1), repeat=6))
    train = tuple(word for word in words if sum(word) <= 3)
    held = tuple(word for word in words if sum(word) >= 4)
    rows: dict[str, object] = {}
    covariance_failures = totality_failures = freshness_failures = 0

    for name, shells in RULES.items():
        truth = tuple(relation_answer(shells, word) for word in words)
        totality_failures += int(len(truth) != 64 or bool(set(truth) - {0, 1}))
        freshness_failures += sum(relation_answer(shells, word, fresh=False) != 0 for word in words)
        for word, frame in product(words, frames):
            covariance_failures += int(
                relation_answer(shells, rotate_six(word, frame))
                != relation_answer(shells, word)
            )
        census = (
            sum(truth),
            sum(relation_answer(shells, word) for word in train),
            sum(relation_answer(shells, word) for word in held),
        )
        rows[name] = {
            "accepted_shells": sorted(shells),
            "accepted_truth_rows": census[0],
            "train_accepts_weight_0_through_3": census[1],
            "held_accepts_weight_4_through_6": census[2],
            "expected_census": EXPECTED_CENSUS[name],
            "census_match": census == EXPECTED_CENSUS[name],
            "total": True,
            "nonconstant": len(set(truth)) == 2,
            "static_shell_set_is_supplied_rule": True,
        }

    separators = []
    for left, right in combinations(RULES, 2):
        witnesses = tuple(
            word for word in words
            if relation_answer(RULES[left], word) != relation_answer(RULES[right], word)
        )
        train_count = sum(sum(word) <= 3 for word in witnesses)
        separators.append({
            "left": left,
            "right": right,
            "witness": "".join(map(str, witnesses[0])) if witnesses else None,
            "train_separators": train_count,
            "held_separators": len(witnesses) - train_count,
            "total_separators": len(witnesses),
        })

    malformed_rows = []
    for label, operation in (
        ("short_word", lambda: relation_answer(RULES["unique_quorum"], (0,) * 5)),
        ("nonbinary_word", lambda: relation_answer(RULES["unique_quorum"], (0, 0, 0, 0, 0, 2))),
        ("nonboolean_freshness", lambda: relation_answer(RULES["unique_quorum"], (0,) * 6, fresh=1)),
    ):
        rejected = False
        try:
            operation()
        except ValueError:
            rejected = True
        malformed_rows.append({"case": label, "rejected": rejected})

    passed = (
        covariance_failures == totality_failures == freshness_failures == 0
        and all(row["census_match"] and row["nonconstant"] for row in rows.values())
        and len(separators) == 10
        and all(row["total_separators"] > 0 for row in separators)
        and all(row["rejected"] for row in malformed_rows)
    )
    result = {
        "neighborhood_words": len(words),
        "train_words": len(train),
        "held_words": len(held),
        "relations": rows,
        "covariance_tests": len(RULES) * len(words) * len(frames),
        "covariance_failures": covariance_failures,
        "totality_failures": totality_failures,
        "freshness_zero_failures": freshness_failures,
        "pairwise_separators": separators,
        "malformed_rows": malformed_rows,
        "all_five_extensionally_distinct": all(row["total_separators"] > 0 for row in separators),
        "positive_model_theorem": (
            "the declared finite schema has at least five displayed extensionally distinct models"
        ),
        "physical_selection_in_theorem_scope": False,
        "pass": passed,
    }
    check("five local relations are total, covariant, and extensionally distinct", passed,
          {"relations": len(rows), "separators": len(separators)})
    return result


# ---------------------------------------------------------------------------
# Unique-quorum conditional port.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ConditionalPort:
    archive6: tuple[int, ...]
    losers6: tuple[int, ...]
    ready: int
    spent: int
    edge: int
    member5: tuple[int, ...]
    receipt5: tuple[int, ...]
    snapshot12: tuple[int, ...]


def unique_quorum_port(word: tuple[int, ...]) -> ConditionalPort:
    validate_six_word(word)
    occurrence = int(sum(word) == 1)
    winner = word.index(1) if occurrence else None
    losers = tuple(bit ^ int(index == winner) for index, bit in enumerate(word))
    lane_zero = (occurrence, 0, 0, 0, 0)
    snapshot = (occurrence, occurrence, occurrence, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    return ConditionalPort(
        archive6=word,
        losers6=losers,
        ready=1 - occurrence,
        spent=occurrence,
        edge=occurrence,
        member5=lane_zero,
        receipt5=lane_zero,
        snapshot12=snapshot,
    )


def validate_port(port: ConditionalPort) -> None:
    validate_six_word(port.archive6)
    validate_six_word(port.losers6)
    scalar_fields = (port.ready, port.spent, port.edge, *port.member5,
                     *port.receipt5, *port.snapshot12)
    if any(type(bit) is not int or bit not in (0, 1) for bit in scalar_fields):
        raise ValueError("conditional port leaves its binary code")
    if len(port.member5) != 5 or len(port.receipt5) != 5 or len(port.snapshot12) != 12:
        raise ValueError("conditional port arity mismatch")
    if port != unique_quorum_port(port.archive6):
        raise ValueError("conditional port provenance mismatch")


def reverse_port(port: ConditionalPort) -> tuple[int, ...]:
    validate_port(port)
    return port.archive6


def rotate_port(port: ConditionalPort, frame: Matrix) -> ConditionalPort:
    return ConditionalPort(
        archive6=rotate_six(port.archive6, frame),
        losers6=rotate_six(port.losers6, frame),
        ready=port.ready,
        spent=port.spent,
        edge=port.edge,
        member5=port.member5,
        receipt5=port.receipt5,
        snapshot12=port.snapshot12,
    )


def port_payload(port: ConditionalPort) -> tuple[int, ...]:
    """The scalar emitted tuple protected by the finite lock construction."""
    return (port.edge, *port.member5, *port.receipt5, *port.snapshot12)


def conditional_port_certificate() -> dict[str, object]:
    frames = proper_cubic_frames()
    words = tuple(product((0, 1), repeat=6))
    equation_failures = inverse_failures = covariance_failures = 0
    class_rows = {"no_hit": 0, "unique": 0, "collision": 0}
    for word in words:
        port = unique_quorum_port(word)
        validate_port(port)
        occurrence = port.edge & port.member5[0] & port.receipt5[0]
        expected = int(sum(word) == 1)
        equation_failures += int(
            occurrence != expected
            or port.snapshot12[:3] != (occurrence,) * 3
            or port.snapshot12[3:] != (0,) * 9
            or port.ready + port.spent != 1
            or port.spent != occurrence
            or port.member5 != port.receipt5
            or port.losers6 != tuple(
                bit ^ int(expected and index == word.index(1))
                for index, bit in enumerate(word)
            )
        )
        inverse_failures += int(reverse_port(port) != word)
        for frame in frames:
            covariance_failures += int(
                rotate_port(port, frame) != unique_quorum_port(rotate_six(word, frame))
            )
        class_rows[
            "no_hit" if sum(word) == 0 else "unique" if sum(word) == 1 else "collision"
        ] += 1

    witness = unique_quorum_port((1, 0, 0, 0, 0, 0))
    collision = unique_quorum_port((1, 1, 0, 0, 0, 0))
    field_presence_witnesses = {
        "edge": port_payload(witness) != (0, *port_payload(witness)[1:]),
        "member": witness.member5 != (0,) * 5,
        "receipt": witness.receipt5 != (0,) * 5,
        "snapshot": witness.snapshot12 != (0,) * 12,
        "ready_spent": (witness.ready, witness.spent) != (1, 0),
        "collision_loser_copy": collision.losers6 != (0,) * 6,
    }

    malformed = []
    bad = asdict(witness)
    bad["snapshot12"] = (1,) * 12
    for label, operation in (
        ("bad_provenance", lambda: validate_port(ConditionalPort(**bad))),
        ("short_archive", lambda: unique_quorum_port((0,) * 5)),
        ("nonbinary_archive", lambda: unique_quorum_port((0, 0, 0, 0, 0, 2))),
    ):
        rejected = False
        try:
            operation()
        except ValueError:
            rejected = True
        malformed.append({"case": label, "rejected": rejected})

    passed = (
        equation_failures == inverse_failures == covariance_failures == 0
        and class_rows == {"no_hit": 1, "unique": 6, "collision": 57}
        and all(field_presence_witnesses.values())
        and all(row["rejected"] for row in malformed)
    )
    result = {
        "words": len(words),
        "classification_census": class_rows,
        "conditional_equation_failures": equation_failures,
        "inverse_failures": inverse_failures,
        "covariance_tests": len(words) * len(frames),
        "covariance_failures": covariance_failures,
        "field_presence_witnesses": field_presence_witnesses,
        "malformed_rows": malformed,
        "archive_makes_map_injective": inverse_failures == 0,
        "lane_zero_binding_is_supplied": True,
        "formation_or_admission_selection_derived": False,
        "actuality_derived": False,
        "framework_Record_identification_derived": False,
        "pass": passed,
    }
    check("unique quorum reaches the exact finite conditional port equations", passed,
          {"words": len(words), "covariance_tests": result["covariance_tests"]})
    return result


# ---------------------------------------------------------------------------
# Supplied finite lock/readout algebra.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class LockedPortState:
    payload: tuple[int, ...]
    readout: tuple[int, ...]
    matter6: tuple[int, ...]
    lock: int
    transient: int


@dataclass(frozen=True)
class PortGenerator:
    family: str
    index: int


def port_generators(payload_width: int) -> tuple[PortGenerator, ...]:
    return tuple(
        [PortGenerator("read", index) for index in range(payload_width)]
        + [PortGenerator("negative_lock_prewrite", index) for index in range(payload_width)]
        + [PortGenerator("matter_flip", index) for index in range(6)]
    )


def apply_port_generator(state: LockedPortState, generator: PortGenerator) -> LockedPortState:
    payload = list(state.payload)
    readout = list(state.readout)
    matter = list(state.matter6)
    if generator.family == "read":
        readout[generator.index] ^= payload[generator.index]
    elif generator.family == "negative_lock_prewrite":
        payload[generator.index] ^= (1 - state.lock) & state.transient
    elif generator.family == "matter_flip":
        matter[generator.index] ^= 1
    else:
        raise ValueError("unknown finite port generator")
    return LockedPortState(tuple(payload), tuple(readout), tuple(matter), state.lock, state.transient)


def finite_preservation_certificate() -> dict[str, object]:
    formed_ports = tuple(unique_quorum_port(tuple(int(index == direction) for index in range(6)))
                         for direction in range(6))
    width = len(port_payload(formed_ports[0]))
    generators = port_generators(width)
    generator_failures = pair_failures = inverse_failures = 0
    read_nontrivial = matter_nontrivial = 0
    for port, transient in product(formed_ports, (0, 1)):
        initial = LockedPortState(port_payload(port), (0,) * width, (0,) * 6, 1, transient)
        for generator in generators:
            output = apply_port_generator(initial, generator)
            generator_failures += int(output.payload != initial.payload or output.lock != 1)
            inverse_failures += int(apply_port_generator(output, generator) != initial)
            read_nontrivial += int(generator.family == "read" and output.readout != initial.readout)
            matter_nontrivial += int(generator.family == "matter_flip" and output.matter6 != initial.matter6)
        for first, second in product(generators, repeat=2):
            output = apply_port_generator(apply_port_generator(initial, first), second)
            pair_failures += int(output.payload != initial.payload or output.lock != 1)

    prewrite_active = 0
    preformation = LockedPortState((0,) * width, (0,) * width, (0,) * 6, 0, 1)
    for generator in generators:
        output = apply_port_generator(preformation, generator)
        prewrite_active += int(
            generator.family == "negative_lock_prewrite" and output.payload != preformation.payload
        )

    frames = proper_cubic_frames()
    family_closure_failures = 0
    names = {(generator.family, generator.index) for generator in generators}
    for frame, generator in product(frames, generators):
        moved_index = generator.index
        if generator.family == "matter_flip":
            moved_index = DIRECTIONS.index(matvec(frame, DIRECTIONS[generator.index]))
        family_closure_failures += int((generator.family, moved_index) not in names)

    expected_read_nontrivial = sum(sum(port_payload(port)) for port in formed_ports) * 2
    expected_matter_nontrivial = len(formed_ports) * 2 * 6
    passed = (
        generator_failures == pair_failures == inverse_failures == family_closure_failures == 0
        and prewrite_active == width
        and read_nontrivial == expected_read_nontrivial
        and matter_nontrivial == expected_matter_nontrivial
    )
    result = {
        "payload_width": width,
        "formed_unique_ports": len(formed_ports),
        "generator_count": len(generators),
        "generator_families": {
            family: sum(generator.family == family for generator in generators)
            for family in ("read", "negative_lock_prewrite", "matter_flip")
        },
        "generator_tests": len(formed_ports) * 2 * len(generators),
        "ordered_pair_controls": len(formed_ports) * 2 * len(generators) ** 2,
        "generator_payload_failures_at_lock1": generator_failures,
        "ordered_pair_payload_failures_at_lock1": pair_failures,
        "generator_inverse_failures": inverse_failures,
        "negative_lock_prewrite_nontrivial_at_lock0": prewrite_active,
        "read_nontrivial_count": read_nontrivial,
        "matter_nontrivial_count": matter_nontrivial,
        "all24_generator_family_closure_tests": len(frames) * len(generators),
        "all24_generator_family_closure_failures": family_closure_failures,
        "finite_composition_proof": (
            "each declared generator fixes every payload coordinate and LOCK at LOCK=1; "
            "induction therefore fixes them under every finite word in this supplied generator monoid"
        ),
        "lock_genesis_is_supplied": True,
        "physical_future_operation_class_derived": False,
        "all_future_permanence_derived": False,
        "framework_Record_identification_derived": False,
        "pass": passed,
    }
    check("supplied finite lock/readout algebra preserves the conditional payload", passed,
          {"generators": len(generators), "pair_controls": result["ordered_pair_controls"]})
    return result


# ---------------------------------------------------------------------------
# Endpoint-derived denominator-64 finite grade block.
# ---------------------------------------------------------------------------
def axis_occupancies(word: tuple[int, ...]) -> tuple[int, int, int]:
    validate_six_word(word)
    return word[0] + word[1], word[2] + word[3], word[4] + word[5]


def parameter_counts(word: tuple[int, ...]) -> tuple[int, int, int]:
    return tuple(2 * occupancy for occupancy in axis_occupancies(word))  # type: ignore[return-value]


def validate_parameter_counts(counts: tuple[int, int, int]) -> None:
    if len(counts) != 3 or any(type(value) is not int or value not in (0, 2, 4) for value in counts):
        raise ValueError("counts leave the state-derived even-count code")


def address_triple(address: int) -> tuple[int, int, int]:
    if type(address) is not int or address not in range(64):
        raise ValueError("address leaves the finite 4x4x4 block")
    return address // 16, (address // 4) % 4, address % 4


def address_number(triple: tuple[int, int, int]) -> int:
    if len(triple) != 3 or any(type(value) is not int or value not in range(4) for value in triple):
        raise ValueError("address triple leaves the finite 4x4x4 block")
    return 16 * triple[0] + 4 * triple[1] + triple[2]


def label_for_address(counts: tuple[int, int, int], address: int) -> int:
    validate_parameter_counts(counts)
    left, middle, right = address_triple(address)
    return (
        4 * int(middle >= counts[1])
        + 2 * int(left >= counts[0])
        + int(right >= counts[2])
    )


def mask_bits(counts: tuple[int, int, int]) -> tuple[int, ...]:
    validate_parameter_counts(counts)
    return tuple(
        int(label_for_address(counts, address) == label)
        for label in range(8)
        for address in range(64)
    )


def mask_count_vector(counts: tuple[int, int, int]) -> tuple[int, ...]:
    validate_parameter_counts(counts)
    return tuple(
        sum(label_for_address(counts, address) == label for address in range(64))
        for label in range(8)
    )


def grade_vector(counts: tuple[int, int, int]) -> tuple[Fraction, ...]:
    return tuple(Fraction(value, 64) for value in mask_count_vector(counts))


def exact_product_grade(counts: tuple[int, int, int]) -> tuple[Fraction, ...]:
    validate_parameter_counts(counts)
    left, middle, right = (Fraction(value, 4) for value in counts)
    return tuple(
        (1 - middle if middle_negative else middle)
        * (1 - left if left_one else left)
        * (1 - right if right_one else right)
        for middle_negative, left_one, right_one in product((0, 1), repeat=3)
    )


def label_bits(label: int) -> tuple[int, int, int]:
    if type(label) is not int or label not in range(8):
        raise ValueError("label leaves the eight-label code")
    return label >> 1 & 1, label >> 2 & 1, label & 1


def bits_label(bits: tuple[int, int, int]) -> int:
    if len(bits) != 3 or any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("label bits leave the three-bit code")
    return 2 * bits[0] + 4 * bits[1] + bits[2]


def rotate_label(label: int, frame: Matrix) -> int:
    return bits_label(rotate_axis_word(label_bits(label), frame))


def rotate_address(address: int, frame: Matrix) -> int:
    return address_number(rotate_axis_word(address_triple(address), frame))


def grade_forward(word: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    counts = parameter_counts(word)
    unary = tuple(int(index < count) for count in counts for index in range(4))
    return unary, mask_bits(counts)


def grade_controlled_uncompute(
    retained_word: tuple[int, ...],
    unary: tuple[int, ...],
    mask: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Clear derived rails after verifying them against the retained endpoint word."""
    expected = grade_forward(retained_word)
    if (unary, mask) != expected:
        raise ValueError("finite grade controlled-uncompute provenance mismatch")
    return (0,) * 12, (0,) * 512


def complete_block_frequency(counts: tuple[int, int, int], size: int) -> tuple[Fraction, ...]:
    validate_parameter_counts(counts)
    if type(size) is not int or size <= 0 or size % 64:
        raise ValueError("unordered finite block accepts complete 64-address multiples only")
    return grade_vector(counts)


def l1(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum((abs(a - b) for a, b in zip(left, right)), Fraction(0))


def finite_grade_certificate() -> dict[str, object]:
    frames = proper_cubic_frames()
    words = tuple(product((0, 1), repeat=6))
    forward_failures = controlled_uncompute_failures = grade_failures = covariance_failures = 0
    count_grid = set()
    for word in words:
        counts = parameter_counts(word)
        count_grid.add(counts)
        unary, mask = grade_forward(word)
        expected_unary = tuple(int(index < count) for count in counts for index in range(4))
        forward_failures += int(unary != expected_unary or mask != mask_bits(counts))
        controlled_uncompute_failures += int(
            grade_controlled_uncompute(word, unary, mask) != ((0,) * 12, (0,) * 512)
        )
        grade_failures += int(
            sum(mask) != 64
            or sum(grade_vector(counts), Fraction(0)) != 1
            or grade_vector(counts) != exact_product_grade(counts)
            or complete_block_frequency(counts, 64) != grade_vector(counts)
        )
        for frame in frames:
            moved_word = rotate_six(word, frame)
            moved_counts = parameter_counts(moved_word)
            covariance_failures += int(moved_counts != rotate_axis_word(counts, frame))
            for address in range(64):
                covariance_failures += int(
                    label_for_address(moved_counts, rotate_address(address, frame))
                    != rotate_label(label_for_address(counts, address), frame)
                )

    group_failures = 0
    for left, right in product(frames, repeat=2):
        composed = matmul(left, right)
        for axis_word in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 0)):
            group_failures += int(
                rotate_axis_word(rotate_axis_word(axis_word, right), left)
                != rotate_axis_word(axis_word, composed)
            )

    deletion_word = (1, 0, 1, 0, 1, 0)
    deleted_word = (0, 0, 1, 0, 1, 0)
    endpoint_deletion = l1(
        grade_vector(parameter_counts(deletion_word)),
        grade_vector(parameter_counts(deleted_word)),
    )
    alternative_calibration = axis_occupancies(deletion_word)
    # The alternative is deliberately evaluated as a generic denominator-four
    # table, not admitted into the even-count state-derived code.
    alternative_grade = tuple(
        Fraction(sum(
            (4 * int(address_triple(address)[1] >= alternative_calibration[1])
             + 2 * int(address_triple(address)[0] >= alternative_calibration[0])
             + int(address_triple(address)[2] >= alternative_calibration[2])) == label
            for address in range(64)
        ), 64)
        for label in range(8)
    )
    calibration_deletion = l1(grade_vector(parameter_counts(deletion_word)), alternative_grade)

    permutation_counts = parameter_counts((1, 0, 1, 0, 0, 0))
    direct = tuple(label_for_address(permutation_counts, address) for address in range(64))
    reverse = tuple(label_for_address(permutation_counts, 63 - address) for address in range(64))
    direct_grade = tuple(Fraction(direct.count(label), 64) for label in range(8))
    reverse_grade = tuple(Fraction(reverse.count(label), 64) for label in range(8))
    order_separator = sum(left != right for left, right in zip(direct, reverse))

    malformed = []
    for label, operation in (
        ("short_endpoint", lambda: grade_forward((0,) * 5)),
        ("nonbinary_endpoint", lambda: grade_forward((0, 0, 0, 0, 0, 2))),
        ("odd_external_counts", lambda: validate_parameter_counts((3, 2, 2))),
        ("held_size_137", lambda: complete_block_frequency((2, 2, 2), 137)),
        ("held_size_211", lambda: complete_block_frequency((2, 2, 2), 211)),
        (
            "wrong_controlled_uncompute_mask",
            lambda: grade_controlled_uncompute((0,) * 6, (0,) * 12, (0,) * 512),
        ),
    ):
        rejected = False
        try:
            operation()
        except ValueError:
            rejected = True
        malformed.append({"case": label, "rejected": rejected})

    passed = (
        forward_failures == controlled_uncompute_failures == grade_failures
        == covariance_failures == group_failures == 0
        and len(count_grid) == 27
        and endpoint_deletion == 1
        and calibration_deletion == Fraction(11, 16)
        and direct_grade == reverse_grade
        and order_separator == 64
        and all(row["rejected"] for row in malformed)
    )
    result = {
        "endpoint_words": len(words),
        "reachable_count_grid_size": len(count_grid),
        "reachable_counts_per_axis": (0, 2, 4),
        "unary_width": 12,
        "mask_width": 512,
        "one_hot_mask_bits_per_block": 64,
        "forward_failures": forward_failures,
        "held_input_controlled_uncompute_failures": controlled_uncompute_failures,
        "grade_or_normalization_failures": grade_failures,
        "covariance_tests": len(words) * len(frames) * 65,
        "covariance_failures": covariance_failures,
        "ordered_frame_products": len(frames) ** 2,
        "group_tests": len(frames) ** 2 * 4,
        "group_failures": group_failures,
        "endpoint_deletion_grade_L1": str(endpoint_deletion),
        "alternative_calibration_witness": deletion_word,
        "declared_calibration_counts_on_witness": parameter_counts(deletion_word),
        "counterfactual_calibration_counts_on_witness": alternative_calibration,
        "alternative_calibration_grade_L1": str(calibration_deletion),
        "address_reversal_witness": (1, 0, 1, 0, 0, 0),
        "address_reversal_counts_on_witness": permutation_counts,
        "address_reversal_grade_L1": str(l1(direct_grade, reverse_grade)),
        "address_reversal_order_separator": order_separator,
        "malformed_and_held_rows": malformed,
        "equally_weighted_addresses": 64,
        "auxiliary_frame_action": (
            "unsigned axis permutation; frame sign flips act trivially on address coordinates"
        ),
        "retained_endpoint_word_required_for_controlled_uncompute": True,
        "calibration": "count_axis=2*(endpoint_plus+endpoint_minus); p_axis=count_axis/4",
        "calibration_is_supplied_candidate_structure": True,
        "realized_history_identification_derived": False,
        "Born_probability_or_calibration_derived": False,
        "framework_Record_identification_derived": False,
        "pass": passed,
    }
    check("finite denominator-64 grade block is exact on its declared code", passed,
          {"words": len(words), "count_grid": len(count_grid), "covariance_tests": result["covariance_tests"]})
    return result


# ---------------------------------------------------------------------------
# Clean-clone/dependency and source-note controls.
# ---------------------------------------------------------------------------
def dependency_closure_certificate() -> dict[str, object]:
    source = Path(__file__).read_text()
    tree = ast.parse(source)
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add((node.module or "").split(".")[0])
    allowed = {
        "__future__", "ast", "dataclasses", "fractions", "hashlib",
        "itertools", "json", "pathlib",
    }
    forbidden_import_roots = {"subprocess", "requests", "urllib", "socket", "importlib"}
    dynamic_call_names = {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
        and node.func.id in {"eval", "exec", "__import__"}
    }
    note_text = NOTE.read_text() if NOTE.exists() else ""
    links = {
        "runner": "../scripts/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_2026_07_23.py",
        "receipt": "../outputs/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_receipt_2026_07_23.json",
        "cache": "../logs/runner-cache/proper_cubic_local_admission_relations_conditional_port_finite_grade_block_2026_07_23.txt",
    }
    metadata = {
        "claim_type": "**Claim type:** bounded_theorem" in note_text,
        "authority": "**Authority:** none" in note_text,
        "audit": "**Audit:** unset" in note_text,
        "record_boundary": "framework-Record identification" in note_text,
        "born_boundary": "supplies no probability or Born" in note_text,
        "actuality_boundary": "derives neither actuality" in note_text,
    }
    passed = (
        imported <= allowed
        and not (imported & forbidden_import_roots)
        and not dynamic_call_names
        and NOTE.is_file()
        and all(target in note_text for target in links.values())
        and all(metadata.values())
    )
    result = {
        "stdlib_import_roots": sorted(imported),
        "allowed_stdlib_import_roots": sorted(allowed),
        "nonstdlib_imports": sorted(imported - allowed),
        "forbidden_import_roots_present": sorted(imported & forbidden_import_roots),
        "dynamic_import_or_eval_calls_present": sorted(dynamic_call_names),
        "external_runner_imports": 0,
        "archived_object_reads": 0,
        "network_calls": 0,
        "subprocess_calls": 0,
        "note_exists": NOTE.is_file(),
        "canonical_links": links,
        "note_metadata_and_boundaries": metadata,
        "clean_clone_requirement": "the four new package files atop origin/main; runner executes with Python stdlib only",
        "pass": passed,
    }
    check("dependency closure is self-contained on current main plus this package", passed,
          {"imports": sorted(imported), "nonstdlib": sorted(imported - allowed)})
    return result


def main() -> int:
    print("FINITE ADMISSION / CONDITIONAL PORT / GRADE SUBSTRATE CERTIFICATE")
    print("authority", AUTHORITY, "audit", AUDIT, "claim_type", CLAIM_TYPE)
    frames = frame_certificate()
    relations = relation_certificate()
    port = conditional_port_certificate()
    preservation = finite_preservation_certificate()
    grade = finite_grade_certificate()
    dependencies = dependency_closure_certificate()

    package_pass = all(row["pass"] for row in (
        frames, relations, port, preservation, grade, dependencies
    )) and FAIL == 0
    receipt = {
        "date": DATE,
        "claim_type": CLAIM_TYPE,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "package_scope": (
            "self-contained finite model separation plus candidate conditional port, "
            "finite declared preservation algebra, and finite grade block"
        ),
        "frame_certificate": frames,
        "relation_certificate": relations,
        "conditional_port_certificate": port,
        "finite_preservation_certificate": preservation,
        "finite_grade_certificate": grade,
        "dependency_closure": dependencies,
        "interpretation_boundaries": {
            "formation_or_admission_selection_derived": False,
            "actuality_derived": False,
            "framework_Record_identification_derived": False,
            "physical_future_operation_class_derived": False,
            "probability_or_Born_calibration_derived": False,
            "objective_corpus_or_realized_history_identification_derived": False,
            "physical_M2_compiler_derived": False,
        },
        "supplied_structure": SUPPLIED_STRUCTURE,
        "not_derived": [
            "physical formation/admission selection law",
            "objective actuality and packet-to-framework-Record identification",
            "derivation of the LOCK genesis and physical future-operation class",
            "derivation of the endpoint-to-grade calibration",
            "objective corpus, probability interpretation, Born calibration, independence, and convergence",
            "physical M2 compiler, noise, renewal, scaling, and infinite-volume control",
        ],
        "runner_sha256": digest(Path(__file__)),
        "note_sha256": digest(NOTE),
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "checks": CHECKS,
        "pass": package_pass,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print("RECEIPT", RECEIPT.relative_to(ROOT))
    print("SCORE", f"PASS={PASS}", f"FAIL={FAIL}")
    print("DISPOSITION", "PASS" if package_pass else "FAIL")
    return 0 if package_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
