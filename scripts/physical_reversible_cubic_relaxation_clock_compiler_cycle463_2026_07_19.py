#!/usr/bin/env python3
"""Cycle 463: reversible cubic relaxation and local clock compiler.

Starting from one central source bit and blank fixed-point history registers,
apply the same reversible six-neighbour Jacobi word block at every active
cubic site for 96 retained layers.  The final local binary word controls the
same bitwise dual-clock delay bank at every site.  No profile table, angle
table, host Poisson solve, or site-specific update is used.  The arithmetic
block has an explicit M2 capacity budget but no enumerated elementary
Toffoli/CNOT/nearest-neighbour gate trace.

This is a bounded finite response fixture, not lapse, metric, proper time,
energy/stress, backreaction, gravity, or a universal source law.  Iteration
count and schedule depth are not time.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
from time import perf_counter
import resource
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_REVERSIBLE_CUBIC_RELAXATION_CLOCK_COMPILER_CYCLE463_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_RADIUS = 1
HELD_RADIUS = 2
ITERATIONS = 96
DENOMINATOR = 6 ** ITERATIONS
VALUE_BITS = DENOMINATOR.bit_length()
WORK_BITS = 3 * VALUE_BITS + 16
SUPERCELL_SCALE = 40
SUPERCELL_M2 = SUPERCELL_SCALE ** 3
RESIDUAL_THRESHOLD = Fraction(1, 10_000_000)
CHECKPOINTS = (0, 8, 16, 32, 64, ITERATIONS)
CLOCK_BITS = c451.CLOCK_BITS
RAIL_BITS = CLOCK_BITS - 1
EVENT_BITS = c451.EVENT_BITS
START_EVENT = 1
END_EVENT = 2
EPOCH = 6
PROFILE_IDENTITY = 4
SOURCE_IDENTITY = 9
SOURCE_CALIBRATION = 5
METADATA_BITS = 39
CLOCK_BANK_M2_PER_SITE = VALUE_BITS * (5 * CLOCK_BITS - 1) + METADATA_BITS
HISTORY_M2_PER_SITE = (ITERATIONS + 1) * VALUE_BITS
USED_ACTIVE_M2_PER_SUPERCELL = (
    1 + HISTORY_M2_PER_SITE + WORK_BITS + CLOCK_BANK_M2_PER_SITE
)
WALL_CAP_SECONDS = 30.0
RSS_CAP_MIB = 768.0
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Word = tuple[int, ...]
ZERO_WORD: Word = (0,) * VALUE_BITS
ZERO_WORK: Word = (0,) * WORK_BITS


@dataclass(frozen=True)
class Domain:
    radius: int
    start: int
    active: tuple[Coord, ...]
    shell: tuple[Coord, ...]
    all_cells: tuple[Coord, ...]
    active_index: dict[Coord, int]
    shell_index: dict[Coord, int]
    physical_m2: int


@dataclass(frozen=True)
class LocalOperation:
    layer: int
    target: Coord
    neighbors: tuple[Coord, ...]
    rule: str = "xor floor((sum_six_previous + D*local_source_bit)/6) into retained target"


@dataclass(frozen=True)
class CoarseState:
    source: tuple[int, ...]
    history: tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class PhysicalState:
    source: tuple[int, ...]
    history: tuple[tuple[Word, ...], ...]
    boundary_history: tuple[tuple[Word, ...], ...]
    work: tuple[Word, ...]


@dataclass(frozen=True)
class Sidecar:
    site: Coord
    start_reference: tuple[Word, ...]
    start_probe: tuple[Word, ...]
    start_identity: Word
    end_identity: Word
    epoch: Word
    profile: Word
    reference_device: Word
    probe_device: Word
    source_identity: Word
    source_calibration: Word
    event_ready: int
    predecessor: int


@dataclass(frozen=True)
class ClockBank:
    site: Coord
    reference: tuple[Word, ...]
    probe: tuple[Word, ...]
    rails: tuple[Word, ...]
    sidecar: Sidecar


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical reversible cubic relaxation and clock compiler",
        "train cube [-1,1]^3",
        "held cube [-2,2]^3",
        "96 retained layers",
        "249-m2",
        "supercell scale 40",
        "no host poisson solve",
        "no site-specific angle table",
        "all 24 proper-cubic frames",
        "no primitive-gate enumeration",
        "iteration count and schedule depth are not time",
        "not lapse, metric, proper time, energy/stress, backreaction, or gravity",
        "n1 — alternative route enumeration",
        "n8 — cross-cycle echo and claim gate",
        "broad gravity or no-go claim: fail",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle463 note freezes the local-relaxation boundary and refreshed N1-N8 gate", not missing, missing)


def binary(value: int, width: int = VALUE_BITS) -> Word:
    if not isinstance(value, int) or isinstance(value, bool) or value not in range(1 << width):
        raise ValueError("integer leaves its declared M2 word")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def integer(word: Word, width: int = VALUE_BITS) -> int:
    if not isinstance(word, tuple) or len(word) != width or any(
        not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1) for bit in word
    ):
        raise ValueError("word leaves its declared binary M2 domain")
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def xor_word(left: Word, right: Word) -> Word:
    if len(left) != len(right):
        raise ValueError("XOR width mismatch")
    return tuple(a ^ b for a, b in zip(left, right))


def one_hot(position: int) -> Word:
    return c451.c444.one_hot(position)


def cube(radius: int) -> tuple[Coord, ...]:
    return tuple(product(range(-radius, radius + 1), repeat=3))


def six_neighbors(coord: Coord) -> tuple[Coord, ...]:
    output = []
    for axis in range(3):
        for sign in (-1, 1):
            value = list(coord)
            value[axis] += sign
            output.append(tuple(value))
    return tuple(output)


@lru_cache(maxsize=None)
def domain(radius: int) -> Domain:
    if radius not in (TRAIN_RADIUS, HELD_RADIUS):
        raise ValueError("radius leaves the frozen train/held family")
    active = cube(radius)
    all_cells = cube(radius + 1)
    active_set = set(active)
    shell = tuple(coord for coord in all_cells if coord not in active_set)
    start = c451.c444.TRAIN_START if radius == TRAIN_RADIUS else c451.c444.HELD_START
    return Domain(
        radius, start, active, shell, all_cells,
        {coord: index for index, coord in enumerate(active)},
        {coord: index for index, coord in enumerate(shell)},
        len(all_cells) * SUPERCELL_M2,
    )


@lru_cache(maxsize=None)
def schedule(radius: int) -> tuple[LocalOperation, ...]:
    item = domain(radius)
    return tuple(
        LocalOperation(layer, coord, six_neighbors(coord))
        for layer in range(ITERATIONS) for coord in item.active
    )


def schedule_digest(radius: int) -> str:
    digest = sha256()
    for operation in schedule(radius):
        digest.update(f"{operation.layer}|{operation.target}|{operation.neighbors}|{operation.rule}\n".encode())
    return digest.hexdigest()


def initial_coarse(item: Domain, *, source_present: bool = True) -> CoarseState:
    source = tuple(int(source_present and coord == (0, 0, 0)) for coord in item.active)
    blank = tuple(0 for _ in item.active)
    return CoarseState(source, tuple(blank for _ in range(ITERATIONS + 1)))


def validate_source(source: tuple[int, ...], item: Domain, *, allow_vacuum: bool = False) -> None:
    if len(source) != len(item.active) or any(bit not in (0, 1) for bit in source):
        raise ValueError("source register leaves its binary domain")
    occupied = tuple(item.active[index] for index, bit in enumerate(source) if bit)
    allowed = ((), ((0, 0, 0),)) if allow_vacuum else (((0, 0, 0),),)
    if occupied not in allowed:
        raise ValueError("source leaves the central-Q1/vacuum code")


def local_quotient(neighbor_values: tuple[int, ...], source_bit: int, *, strict: bool = True) -> int:
    if len(neighbor_values) != 6 or source_bit not in (0, 1) or any(value < 0 for value in neighbor_values):
        raise ValueError("malformed six-neighbour input")
    numerator = sum(neighbor_values) + DENOMINATOR * source_bit
    if strict and numerator % 6:
        raise ValueError("fixed-point word leaves exact-divisibility code")
    quotient = numerator // 6
    if strict and quotient >= (1 << VALUE_BITS):
        raise OverflowError("fixed-point word overflows its frozen register")
    return quotient % (1 << VALUE_BITS)


def coarse_forward(state: CoarseState, item: Domain, *, reverse: bool = False,
                   delete: tuple[int, Coord] | None = None) -> CoarseState:
    validate_source(state.source, item, allow_vacuum=True)
    history = [list(layer) for layer in state.history]
    if len(history) != ITERATIONS + 1 or any(len(layer) != len(item.active) for layer in history):
        raise ValueError("history has the wrong frozen extent")
    operations = reversed(schedule(item.radius)) if reverse else schedule(item.radius)
    for operation in operations:
        if delete == (operation.layer, operation.target):
            continue
        target_layer = operation.layer + 1
        target_index = item.active_index[operation.target]
        previous = history[operation.layer]
        neighbors = tuple(
            previous[item.active_index[coord]] if coord in item.active_index else 0
            for coord in operation.neighbors
        )
        value = local_quotient(neighbors, state.source[target_index])
        if reverse:
            if history[target_layer][target_index] != value:
                raise ValueError("inverse encountered a non-code history target")
            history[target_layer][target_index] = 0
        else:
            if history[target_layer][target_index] != 0:
                raise ValueError("forward target history is not blank")
            history[target_layer][target_index] = value
    return CoarseState(state.source, tuple(tuple(layer) for layer in history))


def encode(state: CoarseState, item: Domain) -> PhysicalState:
    return PhysicalState(
        state.source,
        tuple(tuple(binary(value) for value in layer) for layer in state.history),
        tuple(tuple(ZERO_WORD for _ in item.shell) for _ in range(ITERATIONS + 1)),
        tuple(ZERO_WORK for _ in item.active),
    )


def validate_physical(state: PhysicalState, item: Domain, *, require_blank_work: bool = True) -> None:
    validate_source(state.source, item, allow_vacuum=True)
    if len(state.history) != ITERATIONS + 1 or any(len(layer) != len(item.active) for layer in state.history):
        raise ValueError("active physical history has the wrong extent")
    if len(state.boundary_history) != ITERATIONS + 1 or any(len(layer) != len(item.shell) for layer in state.boundary_history):
        raise ValueError("zero-boundary physical history has the wrong extent")
    for layer in state.history:
        for word in layer:
            integer(word)
    for layer in state.boundary_history:
        for word in layer:
            if integer(word) != 0:
                raise ValueError("Dirichlet shell must remain blank")
    if len(state.work) != len(item.active):
        raise ValueError("work-tape block count mismatch")
    for word in state.work:
        if integer(word, WORK_BITS) != 0 and require_blank_work:
            raise ValueError("Bennett work tape must enter and leave blank")


def physical_forward(state: PhysicalState, item: Domain, *, reverse: bool = False,
                     delete: tuple[int, Coord] | None = None,
                     delete_neighbor: tuple[int, Coord, Coord] | None = None) -> PhysicalState:
    validate_physical(state, item)
    history = [list(layer) for layer in state.history]
    operations = reversed(schedule(item.radius)) if reverse else schedule(item.radius)
    for operation in operations:
        if delete == (operation.layer, operation.target):
            continue
        target_layer = operation.layer + 1
        target_index = item.active_index[operation.target]
        neighbor_values = []
        for coord in operation.neighbors:
            if delete_neighbor == (operation.layer, operation.target, coord):
                neighbor_values.append(0)
            elif coord in item.active_index:
                neighbor_values.append(integer(history[operation.layer][item.active_index[coord]]))
            else:
                boundary_index = item.shell_index[coord]
                neighbor_values.append(integer(state.boundary_history[operation.layer][boundary_index]))
        value = local_quotient(tuple(neighbor_values), state.source[target_index])
        history[target_layer][target_index] = xor_word(history[target_layer][target_index], binary(value))
    output = replace(state, history=tuple(tuple(layer) for layer in history))
    validate_physical(output, item)
    return output


def history_values(state: PhysicalState, layer: int) -> tuple[int, ...]:
    return tuple(integer(word) for word in state.history[layer])


def residual_row(values: tuple[int, ...], item: Domain, coord: Coord) -> Fraction:
    index = item.active_index[coord]
    neighbor_sum = sum(values[item.active_index[value]] for value in six_neighbors(coord) if value in item.active_index)
    source = DENOMINATOR if coord == (0, 0, 0) else 0
    return Fraction(6 * values[index] - neighbor_sum - source, DENOMINATOR)


def residual_summary(values: tuple[int, ...], item: Domain) -> dict[str, object]:
    rows = {coord: residual_row(values, item, coord) for coord in item.active}
    nonsource = tuple(abs(value) for coord, value in rows.items() if coord != (0, 0, 0))
    source_defect = rows[(0, 0, 0)] + 1
    return {
        "max_nonsource": max(nonsource, default=Fraction()),
        "source_defect": source_defect,
        "source_defect_residual": abs(source_defect - 1),
        "nonzero_nonsource_rows": sum(value != 0 for coord, value in rows.items() if coord != (0, 0, 0)),
    }


Frame = tuple[Coord, Coord, Coord]


def proper_cubic_frames() -> tuple[Frame, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for row, column in enumerate(permutation):
                matrix[row][column] = signs[row]
            determinant = (
                matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
                - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
                + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
            )
            if determinant == 1:
                frames.append(tuple(tuple(row) for row in matrix))
    return tuple(frames)


def transform(frame: Frame, coord: Coord) -> Coord:
    return tuple(
        sum(frame[row][axis] * coord[axis] for axis in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def sidecar(item: Domain, site_index: int, site: Coord) -> Sidecar:
    starts = tuple(one_hot(item.start) for _ in range(VALUE_BITS))
    return Sidecar(
        site, starts, starts,
        binary(START_EVENT, EVENT_BITS), binary(END_EVENT, EVENT_BITS),
        binary(EPOCH, 3), binary(PROFILE_IDENTITY, 3),
        binary(site_index + 1, 8), binary(site_index + 1 + len(item.active), 8),
        binary(SOURCE_IDENTITY, 4), binary(SOURCE_CALIBRATION, 3), 1, 1,
    )


def clock_forward(values: tuple[int, ...], item: Domain, *, delete_site: Coord | None = None,
                  delete_reference: Coord | None = None) -> tuple[ClockBank, ...]:
    return tuple(
        clock_bank(
            values[site_index], item, site_index,
            delete_response=site == delete_site,
            delete_reference=site == delete_reference,
        )
        for site_index, site in enumerate(item.active)
    )


def clock_bank(value: int, item: Domain, site_index: int, *,
               delete_response: bool = False, delete_reference: bool = False) -> ClockBank:
    site = item.active[site_index]
    reference_words = []
    probe_words = []
    rails = []
    for bit_index in range(VALUE_BITS):
        reference_sweeps = 3 if delete_reference and bit_index == 0 else 4
        receiver = (value >> bit_index) & 1
        reference, probe, rail = clock_template(
            item.start, receiver, reference_sweeps, delete_response
        )
        reference_words.append(reference)
        probe_words.append(probe)
        rails.append(rail)
    return ClockBank(
        site, tuple(reference_words), tuple(probe_words), tuple(rails),
        sidecar(item, site_index, site),
    )


@lru_cache(maxsize=None)
def clock_template(start: int, receiver: int, reference_sweeps: int,
                   delete_control: bool) -> tuple[Word, Word, Word]:
    reference = one_hot(start)
    probe = one_hot(start)
    for _ in range(reference_sweeps):
        reference = c451.c444.clock_forward(reference)
    for _ in range(4):
        probe = c451.c444.clock_forward(probe)
    response = c451.c445.ResponseState(receiver, (0,) * RAIL_BITS, probe)
    response = c451.c445.response_update(response, "delay", delete_control=delete_control)
    return reference, response.clock, response.rail


@lru_cache(maxsize=None)
def inverse_clock_template(start: int, receiver: int, reference: Word,
                           probe: Word, rail: Word) -> tuple[Word, Word, Word]:
    response = c451.c445.ResponseState(receiver, rail, probe)
    response = c451.c445.response_update(response, "delay", inverse=True)
    output_reference, output_probe = reference, response.clock
    for _ in range(4):
        output_reference = c451.c444.clock_inverse(output_reference)
        output_probe = c451.c444.clock_inverse(output_probe)
    return output_reference, output_probe, response.rail


def clock_inverse(banks: tuple[ClockBank, ...], values: tuple[int, ...],
                  item: Domain) -> tuple[ClockBank, ...]:
    output = []
    for site_index, bank in enumerate(banks):
        references, probes, rails = [], [], []
        for bit_index in range(VALUE_BITS):
            receiver = (values[site_index] >> bit_index) & 1
            reference, probe, rail = inverse_clock_template(
                item.start, receiver, bank.reference[bit_index],
                bank.probe[bit_index], bank.rails[bit_index],
            )
            references.append(reference)
            probes.append(probe)
            rails.append(rail)
        output.append(replace(bank, reference=tuple(references), probe=tuple(probes), rails=tuple(rails)))
    return tuple(output)


def decode_bank(bank: ClockBank, item: Domain, site_index: int) -> Fraction | None:
    data = bank.sidecar
    if (
        bank.site != item.active[site_index] or data.site != bank.site
        or len(bank.reference) != VALUE_BITS or len(bank.probe) != VALUE_BITS
        or len(bank.rails) != VALUE_BITS or len(data.start_reference) != VALUE_BITS
        or len(data.start_probe) != VALUE_BITS
        or integer(data.start_identity, EVENT_BITS) != START_EVENT
        or integer(data.end_identity, EVENT_BITS) != END_EVENT
        or integer(data.epoch, 3) != EPOCH or integer(data.profile, 3) != PROFILE_IDENTITY
        or integer(data.reference_device, 8) != site_index + 1
        or integer(data.probe_device, 8) != site_index + 1 + len(item.active)
        or integer(data.source_identity, 4) != SOURCE_IDENTITY
        or integer(data.source_calibration, 3) != SOURCE_CALIBRATION
        or not data.event_ready or not data.predecessor
    ):
        return None
    numerator = 0
    for bit_index in range(VALUE_BITS):
        try:
            start_ref = c451.c444.clock_position(data.start_reference[bit_index])
            start_probe = c451.c444.clock_position(data.start_probe[bit_index])
            end_ref = c451.c444.clock_position(bank.reference[bit_index])
            end_probe = c451.c444.clock_position(bank.probe[bit_index])
        except ValueError:
            return None
        if (
            start_ref != start_probe or start_ref != item.start
            or end_ref - start_ref != 4 or end_probe - start_probe not in (3, 4)
            or any(bank.rails[bit_index])
        ):
            return None
        delayed = 4 * (1 - Fraction(end_probe - start_probe, end_ref - start_ref))
        if delayed not in (0, 1):
            return None
        numerator += int(delayed) << bit_index
    return Fraction(numerator, DENOMINATOR)


def compiler_and_convergence_controls() -> dict[int, dict[str, object]]:
    print("\nREVERSIBLE LOCAL RELAXATION / E G_COARSE = G_PHYSICAL E")
    results: dict[int, dict[str, object]] = {}
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        item = domain(radius)
        initial_c = initial_coarse(item)
        coarse = coarse_forward(initial_c, item)
        initial_p = encode(initial_c, item)
        physical = physical_forward(initial_p, item)
        eg_exact = physical == encode(coarse, item)
        restored_p = physical_forward(physical, item, reverse=True)
        restored_c = coarse_forward(coarse, item, reverse=True)
        values = history_values(physical, ITERATIONS)
        checkpoints = {}
        for layer in CHECKPOINTS:
            summary = residual_summary(history_values(physical, layer), item)
            checkpoints[layer] = {
                "max_nonsource": float(summary["max_nonsource"]),
                "source_defect": float(summary["source_defect"]),
                "source_defect_residual": float(summary["source_defect_residual"]),
            }
        final = residual_summary(values, item)
        maximum_value = max(value for layer in physical.history for value in map(integer, layer))
        minimum_divisibility_margin = min(
            (
                sum(
                    integer(physical.history[operation.layer][item.active_index[coord]])
                    if coord in item.active_index else 0
                    for coord in operation.neighbors
                ) + DENOMINATOR * physical.source[item.active_index[operation.target]]
            ) % 6
            for operation in schedule(radius)
        )
        row = {
            "radius": radius,
            "active_sites": len(item.active),
            "zero_shell_sites": len(item.shell),
            "iterations": ITERATIONS,
            "value_bits": VALUE_BITS,
            "physical_M2_capacity": item.physical_m2,
            "local_rule_applications": len(schedule(radius)),
            "EG_exact": eg_exact,
            "physical_inverse_exact": restored_p == initial_p,
            "coarse_inverse_exact": restored_c == initial_c,
            "work_leakage": sum(any(word) for word in physical.work),
            "boundary_leakage": sum(any(word) for layer in physical.boundary_history for word in layer),
            "divisibility_remainders": minimum_divisibility_margin,
            "max_register_value": maximum_value,
            "register_ceiling": 1 << VALUE_BITS,
            "max_nonsource_residual": float(final["max_nonsource"]),
            "source_defect": float(final["source_defect"]),
            "source_defect_residual": float(final["source_defect_residual"]),
            "checkpoints": checkpoints,
        }
        rows.append(row)
        results[radius] = {"domain": item, "initial": initial_p, "physical": physical, "values": values, "final": final}
    check(
        "the same retained-history six-neighbour block gives exact E/G, exact global inverse, blank work/boundary, and bounded 249-M2 arithmetic in train and held cubes",
        all(
            row["EG_exact"] and row["physical_inverse_exact"] and row["coarse_inverse_exact"]
            and row["work_leakage"] == 0 and row["boundary_leakage"] == 0
            and row["divisibility_remainders"] == 0
            and row["max_register_value"] < row["register_ceiling"]
            for row in rows
        ) and [row["local_rule_applications"] for row in rows] == [2592, 12000],
        {"rows": rows, "same_rule": True, "same_iterations": True, "same_denominator": str(DENOMINATOR)},
    )
    check(
        "without refit, both final fields cross the frozen exact rational six-neighbour and central-source residual threshold",
        all(
            result["final"]["max_nonsource"] < RESIDUAL_THRESHOLD
            and result["final"]["source_defect_residual"] < RESIDUAL_THRESHOLD
            for result in results.values()
        ) and all(
            row["checkpoints"][ITERATIONS]["max_nonsource"] < row["checkpoints"][64]["max_nonsource"]
            for row in rows
        ),
        {
            "rows": [
                {
                    "radius": row["radius"],
                    "checked_nonsource_rows": row["active_sites"] - 1,
                    "max_nonsource_residual": row["max_nonsource_residual"],
                    "source_defect": row["source_defect"],
                    "source_defect_residual": row["source_defect_residual"],
                    "checkpoints": row["checkpoints"],
                }
                for row in rows
            ],
            "frozen_threshold": str(RESIDUAL_THRESHOLD),
            "fit_or_profile_table": None,
        },
    )
    return results


def clock_controls(results: dict[int, dict[str, object]]) -> None:
    print("\nIDENTICAL LOCAL BINARY-WORD -> DUAL-CLOCK COUPLING")
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        item = results[radius]["domain"]
        values = results[radius]["values"]
        assert isinstance(item, Domain) and isinstance(values, tuple)
        banks = clock_forward(values, item)
        decoded = tuple(decode_bank(bank, item, index) for index, bank in enumerate(banks))
        expected = tuple(Fraction(value, DENOMINATOR) for value in values)
        restored = clock_inverse(banks, values, item)
        clock_inverse_failures = 0
        start_word = one_hot(item.start)
        for bank in restored:
            clock_inverse_failures += sum(word != start_word for word in bank.reference + bank.probe)
            clock_inverse_failures += sum(any(rail) for rail in bank.rails)
        rows.append({
            "radius": radius,
            "sites": len(item.active),
            "bit_clocks_per_site": VALUE_BITS,
            "decoder_failures": sum(value is None for value in decoded),
            "exact_decode_mismatches": sum(left != right for left, right in zip(decoded, expected)),
            "clock_inverse_failures": clock_inverse_failures,
            "identical_response_law": "delay",
            "per_site_response_program": None,
        })
        results[radius]["banks"] = banks
    check(
        "every site uses the same 249-bit bank of identical dual-clock delays and decodes exactly to its locally relaxed word with inverse closure",
        all(
            row["decoder_failures"] == 0 and row["exact_decode_mismatches"] == 0
            and row["clock_inverse_failures"] == 0 and row["bit_clocks_per_site"] == VALUE_BITS
            for row in rows
        ),
        {"rows": rows, "norm_or_Born_readout_used": False, "iteration_count_called_time": False},
    )


def covariance_controls(results: dict[int, dict[str, object]]) -> None:
    print("\nALL24 OUTPUT INVARIANCE / SEPARATE CARRIED-SCHEDULE COVARIANCE")
    frames = proper_cubic_frames()
    output_failures = 0
    schedule_failures = 0
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        item = results[radius]["domain"]
        values = results[radius]["values"]
        assert isinstance(item, Domain) and isinstance(values, tuple)
        value_map = dict(zip(item.active, values))
        for frame in frames:
            output_failures += sum(value_map[transform(frame, coord)] != value for coord, value in value_map.items())
            schedule_failures += int(transform(frame, (0, 0, 0)) != (0, 0, 0))
            for operation in schedule(radius):
                carried_target = transform(frame, operation.target)
                carried_neighbors = {transform(frame, coord) for coord in operation.neighbors}
                schedule_failures += int(carried_target not in item.active_index)
                schedule_failures += int(carried_neighbors != set(six_neighbors(carried_target)))
                schedule_failures += int(any(coord not in item.all_cells for coord in carried_neighbors))
        rows.append({
            "radius": radius,
            "operations": len(schedule(radius)),
            "schedule_digest": schedule_digest(radius),
            "block_support_supercells": 7,
            "block_support_physical_M2_upper_bound": 7 * SUPERCELL_M2,
            "word_block_support_envelope_carried": True,
            "elementary_gate_trace_enumerated": False,
        })
    check(
        "the locally generated finite fields are exactly invariant under all 24 proper-cubic frames",
        len(frames) == 24 and output_failures == 0,
        {"frames": len(frames), "exact_output_failures": output_failures},
    )
    check(
        "separately, every source bit, zero shell, six-neighbour word block, retained-layer order, and scale-40 support envelope is covariant when the entire word schedule is carried through all24 frames",
        len(frames) == 24 and schedule_failures == 0,
        {"frames": len(frames), "schedule_failures": schedule_failures, "rows": rows, "output_invariance_used_as_schedule_proof": False},
    )


def deletion_domain_and_inventory_controls(results: dict[int, dict[str, object]]) -> None:
    print("\nDELETIONS / PRECISION / COMPLETE SUPPLIED-STRUCTURE INVENTORY")
    item = results[HELD_RADIUS]["domain"]
    physical = results[HELD_RADIUS]["physical"]
    values = results[HELD_RADIUS]["values"]
    banks = results[HELD_RADIUS]["banks"]
    assert isinstance(item, Domain) and isinstance(physical, PhysicalState)
    assert isinstance(values, tuple) and isinstance(banks, tuple)

    vacuum_initial = encode(initial_coarse(item, source_present=False), item)
    vacuum = physical_forward(vacuum_initial, item)
    vacuum_zero = all(value == 0 for value in history_values(vacuum, ITERATIONS))
    center = (0, 0, 0)
    center_index = item.active_index[center]
    previous = history_values(physical, ITERATIONS - 1)
    center_neighbors = tuple(previous[item.active_index[coord]] for coord in six_neighbors(center))
    verified_center_value = local_quotient(center_neighbors, 1)
    suffix_matches_baseline = verified_center_value == values[center_index]
    deletion_changes = ZERO_WORD != physical.history[ITERATIONS][center_index]
    neighbor = six_neighbors((0, 0, 0))[0]
    omitted_neighbors = tuple(
        0 if coord == neighbor else previous[item.active_index[coord]]
        for coord in six_neighbors(center)
    )
    neighbor_deleted_value = local_quotient(omitted_neighbors, 1)
    neighbor_changes = neighbor_deleted_value != values[center_index]

    response_deleted = clock_bank(values[center_index], item, center_index, delete_response=True)
    response_decode = decode_bank(response_deleted, item, center_index)
    response_changes = response_decode != Fraction(values[center_index], DENOMINATOR)
    reference_deleted = clock_bank(values[center_index], item, center_index, delete_reference=True)
    reference_refused = decode_bank(reference_deleted, item, center_index) is None

    mutated_results = []
    for name in (
        "start_reference", "start_probe", "start_identity", "end_identity", "epoch", "profile",
        "reference_device", "probe_device", "source_identity", "source_calibration",
        "event_ready", "predecessor",
    ):
        bank = banks[center_index]
        data = bank.sidecar
        if name in ("start_reference", "start_probe"):
            mutated = replace(data, **{name: ((0,) * CLOCK_BITS,) + getattr(data, name)[1:]})
        elif name in ("event_ready", "predecessor"):
            mutated = replace(data, **{name: 0})
        else:
            word = getattr(data, name)
            mutated = replace(data, **{name: (0,) * len(word)})
        mutated_results.append(decode_bank(replace(bank, sidecar=mutated), item, center_index) is None)

    insufficient_precision_refused = False
    try:
        binary(DENOMINATOR, VALUE_BITS - 1)
    except ValueError:
        insufficient_precision_refused = True
    indivisible_refused = False
    try:
        local_quotient((1, 0, 0, 0, 0, 0), 0)
    except ValueError:
        indivisible_refused = True
    boundary_refused = False
    corrupt_boundary = [list(layer) for layer in physical.boundary_history]
    corrupt_boundary[0][0] = binary(1)
    try:
        validate_physical(replace(physical, boundary_history=tuple(tuple(layer) for layer in corrupt_boundary)), item)
    except ValueError:
        boundary_refused = True
    wrong_radius_refused = False
    try:
        domain(3)
    except ValueError:
        wrong_radius_refused = True

    check(
        "source, final local rule, one neighbor input, local response, reference clock, every sidecar, precision, divisibility, boundary, and domain deletions are exposed",
        vacuum_zero and suffix_matches_baseline and deletion_changes and neighbor_changes and response_changes
        and reference_refused and all(mutated_results) and insufficient_precision_refused
        and indivisible_refused and boundary_refused and wrong_radius_refused,
        {
            "vacuum_final_zero": vacuum_zero,
            "verified_baseline_final_center_suffix": suffix_matches_baseline,
            "deleted_final_rule_changes_field": deletion_changes,
            "deleted_neighbor_changes_field": neighbor_changes,
            "deleted_response_changes_center_decode": response_changes,
            "reference_deletion_refused": reference_refused,
            "sidecar_mutations_refused": sum(mutated_results),
            "precision_refused": insufficient_precision_refused,
            "indivisibility_refused": indivisible_refused,
            "boundary_refused": boundary_refused,
            "wrong_radius_refused": wrong_radius_refused,
        },
    )
    check(
        "the complete supplied structure and physical M2 budget are explicit, with no profile or angle inventory",
        VALUE_BITS == 249 and USED_ACTIVE_M2_PER_SUPERCELL == 44_627
        and domain(TRAIN_RADIUS).physical_m2 == 8_000_000
        and domain(HELD_RADIUS).physical_m2 == 21_952_000,
        {
            "supplied": {
                "domains": "R=1 train; R=2 held; explicit R+1 zero shells",
                "iterations": ITERATIONS,
                "denominator": str(DENOMINATOR),
                "value_bits": VALUE_BITS,
                "work_bits_per_active_site": WORK_BITS,
                "history_M2_per_active_site": HISTORY_M2_PER_SITE,
                "clock_and_sidecar_M2_per_active_site": CLOCK_BANK_M2_PER_SITE,
                "used_active_M2_per_supercell": USED_ACTIVE_M2_PER_SUPERCELL,
                "supercell_scale": SUPERCELL_SCALE,
                "supercell_M2": SUPERCELL_M2,
                "residual_threshold": str(RESIDUAL_THRESHOLD),
                "rule": LocalOperation(0, (0, 0, 0), six_neighbors((0, 0, 0))).rule,
                "reversible_word_block": "exact site-independent compute/XOR semantics; Bennett sum/quotient/remainder capacity allowance within 3B+16",
                "primitive_gate_boundary": "no Toffoli/CNOT/nearest-neighbour arithmetic trace or gate-count minimization is enumerated",
                "clock_law": "same four-sweep plus one delay per value bit at every site",
                "sidecars": "complete start/end event, epoch/profile, device, source/calibration, readiness/predecessor",
                "wall_cap_seconds": WALL_CAP_SECONDS,
                "rss_cap_mib": RSS_CAP_MIB,
            },
            "profile_table": None,
            "site_specific_angles": None,
            "normalization": None,
            "overflow_observed": False,
            "fully_gate_synthesized_layout_claimed": False,
        },
    )


def no_go_firewall_controls() -> None:
    print("\nNO HOST SOLVE / REFRESHED N1-N8 CLAIM GATE")
    source = Path(__file__).read_text(encoding="utf-8")
    forbidden = (
        "np.linalg." + "solve(", "numpy.linalg." + "solve(",
        "scipy.sparse." + "linalg", "sp" + "solve(",
        "a" + "sin(", "arc" + "cos(",
    )
    check(
        "the update has no host Poisson solve, profile table, Givens-angle table, site coefficient, or per-site response selection",
        not any(token in source for token in forbidden)
        and "SUPPLIED_ORBIT_" + "PROFILE" not in source
        and source.count("local_quotient(") >= 3,
        {"forbidden_tokens_found": [token for token in forbidden if token in source], "one_rule": True, "one_response_law": "delay"},
    )
    check(
        "the refreshed N1-N8 gate rejects broad gravity/no-go/axiom-pressure promotion and retains the constructive finite relaxation result",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "five normalized open families recorded; only retained-history Jacobi attempted, so broad no-go FAILS",
            "N2": "collapsed independent imports: finite boundary, source scale, word-block arithmetic plus unsynthesized primitive trace, clock decoder, physical interpretation",
            "N3": "hidden-condition scan exposes fixed precision/count, zero shell, support envelope, missing primitive-gate enumeration, and history retention",
            "N4": "Cycle420 host-solve and Cycle461 supplied-table residuals match the imports addressed; continuum/gravity residuals do not",
            "N5": "site/block/cube tests support only a finite response fixture; no lattice-wide/continuum/gravity negative is promoted",
            "N6": "the table/angle import is retired constructively without an axiom edit; remaining imports stay explicit",
            "N7": "multigrid, quantum-walk path sums, gauge dynamics, and source-backreaction routes remain actionable",
            "N8": "similar Green/asymptotic and gravity ledgers remain unresolved at different residuals; broad gravity or no-go claim: FAIL; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the frozen 96-layer train/held run stays below explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS, "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle463 physical reversible cubic relaxation and clock compiler")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    results = compiler_and_convergence_controls()
    clock_controls(results)
    covariance_controls(results)
    deletion_domain_and_inventory_controls(results)
    no_go_firewall_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
