#!/usr/bin/env python3
"""Cycle595: TI innovation-bath and off-grid held-history tournament."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import re
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_2026_07_22 as c592

c587 = c592.c587
c577 = c592.c577
c552 = c592.c552
Gate = c587.Gate

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_TI_INNOVATION_BATH_OFFGRID_HISTORY_TOURNAMENT_CYCLE595_NOTE_2026-07-22.md"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-11
WALL_CAP_SECONDS = 360.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0
Word = tuple[int, ...]

FROZEN_PATHS = {
    "Cycle552 runner": ROOT / "scripts/physical_autonomous_local_member_law_cell_cycle552_2026_07_21.py",
    "Cycle552 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_LOCAL_MEMBER_LAW_CELL_CYCLE552_NOTE_2026-07-21.md",
    "Cycle552 receipt": ROOT / "outputs/physical_autonomous_local_member_law_cell_cycle552_receipt_2026_07_21.json",
    "Cycle565 runner": ROOT / "scripts/physical_born_menu_compiler_occurrence_interface_cycle565_2026_07_21.py",
    "Cycle565 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BORN_MENU_COMPILER_OCCURRENCE_INTERFACE_CYCLE565_NOTE_2026-07-21.md",
    "Cycle565 receipt": ROOT / "outputs/physical_born_menu_compiler_occurrence_interface_cycle565_receipt_2026_07_21.json",
    "Cycle571 runner": ROOT / "scripts/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.py",
    "Cycle571 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md",
    "Cycle571 receipt": ROOT / "outputs/physical_renewable_first_hit_record_admission_tournament_cycle571_receipt_2026_07_22.json",
    "Cycle571 cold": ROOT / "outputs/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.txt",
    "Cycle577 runner": ROOT / "scripts/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.py",
    "Cycle577 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_PROJECTOR_INSTRUMENT_COMPILER_TOURNAMENT_CYCLE577_NOTE_2026-07-22.md",
    "Cycle577 receipt": ROOT / "outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_receipt_2026_07_22.json",
    "Cycle577 cold": ROOT / "outputs/physical_l41_projector_instrument_compiler_tournament_cycle577_2026_07_22.txt",
    "Cycle580 runner": ROOT / "scripts/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.py",
    "Cycle580 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_ELEMENTARY_GATE_LAYOUT_COMPILER_CYCLE580_NOTE_2026-07-22.md",
    "Cycle580 receipt": ROOT / "outputs/physical_l41_elementary_gate_layout_compiler_cycle580_receipt_2026_07_22.json",
    "Cycle580 cold": ROOT / "outputs/physical_l41_elementary_gate_layout_compiler_cycle580_2026_07_22.txt",
    "Cycle582 runner": ROOT / "scripts/physical_l41_autonomous_recurrence_resource_tournament_cycle582_2026_07_22.py",
    "Cycle582 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_AUTONOMOUS_RECURRENCE_RESOURCE_TOURNAMENT_CYCLE582_NOTE_2026-07-22.md",
    "Cycle582 receipt": ROOT / "outputs/physical_l41_autonomous_recurrence_resource_tournament_cycle582_receipt_2026_07_22.json",
    "Cycle582 cold": ROOT / "outputs/physical_l41_autonomous_recurrence_resource_tournament_cycle582_2026_07_22.txt",
    "Cycle584 runner": ROOT / "scripts/physical_l41_local_streaming_reuse_tournament_cycle584_2026_07_22.py",
    "Cycle584 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_L41_LOCAL_STREAMING_REUSE_TOURNAMENT_CYCLE584_NOTE_2026-07-22.md",
    "Cycle584 receipt": ROOT / "outputs/physical_l41_local_streaming_reuse_tournament_cycle584_receipt_2026_07_22.json",
    "Cycle584 cold": ROOT / "outputs/physical_l41_local_streaming_reuse_tournament_cycle584_2026_07_22.txt",
    "Cycle587 runner": ROOT / "scripts/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_2026_07_22.py",
    "Cycle587 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_OCCURRENCE_BORN_HISTORY_BRIDGE_TOURNAMENT_CYCLE587_NOTE_2026-07-22.md",
    "Cycle587 receipt": ROOT / "outputs/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_receipt_2026_07_22.json",
    "Cycle587 cold": ROOT / "outputs/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_cold_2026_07_22.txt",
    "Cycle592 runner": ROOT / "scripts/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_2026_07_22.py",
    "Cycle592 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_PREREGISTERED_INNOVATION_RECORD_FREQUENCY_BRIDGE_TOURNAMENT_CYCLE592_NOTE_2026-07-22.md",
    "Cycle592 receipt": ROOT / "outputs/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_receipt_2026_07_22.json",
    "Cycle592 cold": ROOT / "outputs/physical_preregistered_innovation_record_frequency_bridge_tournament_cycle592_cold_2026_07_22.txt",
    "Cycle41 runner": ROOT / "scripts/complete_candidate_lstar_assembly_cycle41_2026_07_14.py",
}
FROZEN = {
    "Cycle552 runner": "123c9fe8a7a3802af2627e21dd1cee5a8dadfbe0b82b7862e64c7024be6adc7f",
    "Cycle552 note": "cc5cee11501bcf541faf54e0ca69a5d931037a126d1bac9e02c41c131e752400",
    "Cycle552 receipt": "cf70de5c6034567637e96fab75bc5e8383630c82bf0b2e0e009049bf1a63415f",
    "Cycle565 runner": "f31d207540efbf1541343c53552c947c77f2c984e705818786ac3c5f6d06eba2",
    "Cycle565 note": "f29702462974b922e23624df57fb0b6107f5051e95c43d7b51a10953db829bbb",
    "Cycle565 receipt": "a1b30e2fe268b270720f01ab426af5736cdc23189f94c641a428dc0369ccca9a",
    "Cycle571 runner": "af0a0b4837781b2a03fc471c819ce4c6b95e4e4cc000c403fabe4ddb10f6b14c",
    "Cycle571 note": "9781ac6d6d920c17b275c41b13d20ccb9e65ea68a97b48dc8ed8487718708efc",
    "Cycle571 receipt": "6d75e5d7075c3e65f4a7d8a9406d3bd685cc58aa0be165dd0db5ffe34dc66e31",
    "Cycle571 cold": "5e4acfe172dc31dbc2f01db314a7414115fc17e4b7ce4164beea0f1f111b46cb",
    "Cycle577 runner": "0876bc8888193606446b5fe07f1fdd8e3ddef3b313551739b81be3792c820aa7",
    "Cycle577 note": "7617ee877ca22986e0eacc09d08e14f6246cbc75b6443961c8626a1b5435f18c",
    "Cycle577 receipt": "f7e6bbc40a4d56ee115ba43ddbab7bee4aff05227b988a057adc4420f51941ed",
    "Cycle577 cold": "1c77d2ca4bf860482d3e55596c85e0983f32e755e7ceaac33ff0576a928c8a36",
    "Cycle580 runner": "1f1acb34dc8976f5617319353e9591f64eae5cfe923a1dea736adfa792c4e718",
    "Cycle580 note": "47a6418c27965219ddc5d3c2a8bc39fd34aa6173d3d1c16e473a136113b9c787",
    "Cycle580 receipt": "9cf656c917ff738bc6d0d0e52dc8c251630aaedd86dd5a6b90dd4f7857cdbc1d",
    "Cycle580 cold": "890c68f44bf6cc563916304b51481def8aa3ad7009a6ecfe0b0a4cffc85cd7e6",
    "Cycle582 runner": "6b2e15a051c91542dcbebc6fe9dc4de24d6908dfbc36a2b44696809339a6b07c",
    "Cycle582 note": "0f77f19c52f6aa66e895baba2782f8f802601f74d21c45c7eced78ccfdc2f0c5",
    "Cycle582 receipt": "3ccacbe0eaf2b4e476956d0728e71d0d871a1aedb69f12d85c4368e4070ca4b0",
    "Cycle582 cold": "bd18e16e6019b65c5331764cf3cf101ef816c275a3a8e4f6d0026b334e936d11",
    "Cycle584 runner": "b7f2d262e4224bc298dd22b137e89e5e4118dc455e0454250908e503bb19be82",
    "Cycle584 note": "da6576714664f225025442b08a696e4a2b90acbd0a7f60439ab462be9a4f0059",
    "Cycle584 receipt": "a5a3c553a91a624edc5e4b104dd1e19d0f923df831b889aaa972cb40e7394872",
    "Cycle584 cold": "3bb01b04ccfe8418de93404395d2e0cb42ea06579b79d80aecb1b14163037729",
    "Cycle587 runner": "881e2c5a33217352a97df363f5c3dcd67980c2e672b59e072c6ecbc1cb0f27d1",
    "Cycle587 note": "4b1a4e6916da24c74086d83f154cdb474dc87a4954b6be9ea600f685fb9b8e4b",
    "Cycle587 receipt": "ed4ca30a1c174ec96eaeb3b10dc30f261efb274697acf061e23dd24dbb71a173",
    "Cycle587 cold": "ce59771c3263e0f8a77dbeccffeb8e61628fb3bc70b5542924e2e743d5d59fe8",
    "Cycle592 runner": "14d01e640eb1818c29aeb9f05313b2211e28e445d4798f3f6718d0b0fca0d62a",
    "Cycle592 note": "092f0bfc06f7a42d82ed10ade5f551bdb08ebe7040c8c2b8ba0b1b3ea1c971c7",
    "Cycle592 receipt": "edf069adbf58b66b30b6b9a66a85dd577b6c6c3170f833807dc57d59c8f14457",
    "Cycle592 cold": "cb2640da38cf7cb0a69e6351871d9a9ba93c712f6865d5055b0bd79f18acdc5c",
    "Cycle41 runner": "d8207fc0090ca926d060f536fedc2b2c031ccd50184e035c292e6b8eccb56814",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def one_hot(label: int, width: int) -> Word:
    if label not in range(width):
        raise ValueError("label leaves one-hot domain")
    return tuple(int(index == label) for index in range(width))


def singleton(bits: Word, name: str) -> int:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits) or sum(bits) != 1:
        raise ValueError(f"{name} is not one-hot")
    return bits.index(1)


def empirical(labels: tuple[int, ...], width: int = 8) -> np.ndarray:
    return np.asarray(tuple(labels.count(label) / len(labels) for label in range(width)))


# Bath law is frozen independently and textually before held-state definitions.
BATH_LAW = {
    "route_A": "eight-cell doubled-lane Margolus shift: onsite A_i/B_i SWAP then cross B_i/A_(i+1) SWAP",
    "route_B": "H on three zero address M2 then three address-to-environment CNOTs",
    "route_C": "three-bit reversible LFSR (b0,b1,b2)->(b2 xor b0,b0,b1)",
    "address_arity": 8,
    "ROM": "unchanged Cycle592 three-program denominator-eight table",
}
BATH_LAW_SHA256 = sha256(json.dumps(BATH_LAW, sort_keys=True).encode()).hexdigest()
EXPECTED_BATH_LAW_SHA256 = "ea1150b018833b032fd5bb0b9fa1466d54140f33e5897623efa0318d7864c175"


def plus_minus_state(plus_weight: float) -> np.ndarray:
    if not 0.0 <= plus_weight <= 1.0:
        raise ValueError("X-basis weight leaves unit interval")
    plus = c577.PLUS
    minus = (c577.ZERO - c577.ONE) / np.sqrt(2.0)
    return np.sqrt(plus_weight) * plus + np.sqrt(1.0 - plus_weight) * minus


# New off-grid held states are declared after the bath law and are absent from
# its hash.  Their denominators 3 and 15 cannot be represented exactly by an
# eight-address histogram.
HELD_NAMES = ("offgrid_X_2over3", "offgrid_Z2over3_X3over5")
HELD_STATES = (
    c577.kron_all(c577.ZERO.reshape(-1, 1), plus_minus_state(2 / 3).reshape(-1, 1), c577.ZERO.reshape(-1, 1)).reshape(-1),
    c577.kron_all(
        np.asarray((np.sqrt(2 / 3), np.sqrt(1 / 3)), dtype=complex).reshape(-1, 1),
        plus_minus_state(3 / 5).reshape(-1, 1), c577.ZERO.reshape(-1, 1),
    ).reshape(-1),
)
HELD_SIZES = (72, 120)
HELD_SHA256 = sha256(b"Cycle595-held-after-bath:offgrid-X-2/3;offgrid-Z2/3-X3/5;sizes72,120").hexdigest()


def grade(state: np.ndarray) -> np.ndarray:
    return c592.independent_grade_vector(state)


def compositions(total: int, width: int, prefix: tuple[int, ...] = ()):
    if width == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, width - 1, prefix + (value,))


def denominator8_best(target: np.ndarray) -> tuple[float, tuple[int, ...]]:
    best = (float("inf"), ())
    for counts in compositions(8, 8):
        residual = float(np.linalg.norm(np.asarray(counts) / 8.0 - target, ord=1))
        if residual < best[0]:
            best = (residual, counts)
    return best


# Route A: two disjoint uniform SWAP layers on eight doubled-lane cells.
A_SITES = tuple(range(8))
B_SITES = tuple(range(8, 16))
A_ONSITE = tuple(Gate("SWAP", (A_SITES[i], B_SITES[i]), f"A:onsite:{i}") for i in range(8))
A_CROSS = tuple(Gate("SWAP", (B_SITES[i], A_SITES[(i + 1) % 8]), f"A:cross:{i}") for i in range(8))
A_SCHEDULE = A_ONSITE + A_CROSS


def prepare_a(genesis: int) -> Word:
    if genesis not in range(8):
        raise ValueError("bath genesis leaves eight-cell ring")
    return one_hot(genesis, 16)


def bath_a_step(word: Word, *, delete_label: str | None = None) -> Word:
    if len(word) != 16 or sum(word) != 1 or any(word[s] for s in B_SITES):
        raise ValueError("Route A leaves one-carrier/blank-buffer code")
    output = c587.apply_schedule(word, A_SCHEDULE, delete_label=delete_label)
    if delete_label is None and (sum(output) != 1 or any(output[s] for s in B_SITES)):
        raise ValueError("Route A update leaves code")
    return output


def bath_a_address(word: Word) -> int:
    return singleton(tuple(word[s] for s in A_SITES), "Route A carrier")


def ring16_coordinates() -> tuple[tuple[int, int, int], ...]:
    points = [(x, 0, 0) for x in range(8)] + [(x, 1, 0) for x in range(7, -1, -1)]
    # The schedule names rails by logical cell (A_0..A_7,B_0..B_7), while
    # the cubic embedding alternates those rails around one physical cycle:
    # A_i--B_i--A_(i+1).  Return coordinates in logical-site order.
    coordinates: list[tuple[int, int, int] | None] = [None] * 16
    for cell in range(8):
        coordinates[A_SITES[cell]] = points[2 * cell]
        coordinates[B_SITES[cell]] = points[2 * cell + 1]
    assert all(point is not None for point in coordinates)
    return tuple(point for point in coordinates if point is not None)


def route_a_controls() -> dict[str, object]:
    eg_failures = inverse_failures = ledger_failures = interface_failures = 0
    orbit_rows = []
    for genesis in range(8):
        word = prepare_a(genesis)
        addresses = []
        for step in range(16):
            before = word
            word = bath_a_step(word)
            expected = (genesis + step + 1) % 8
            found = bath_a_address(word)
            eg_failures += found != expected
            inverse_failures += c587.apply_schedule(word, A_SCHEDULE, reverse=True) != before
            ledger_failures += int(sum(word) != 1 or any(word[s] for s in B_SITES))
            addresses.append(found)
        orbit_rows.append({"genesis": genesis, "first_orbit": tuple(addresses[:8]), "orbit_index_average": tuple(float(x) for x in empirical(tuple(addresses[:8])))})

    transition = np.zeros((8, 8))
    for address in range(8):
        transition[(address + 1) % 8, address] = 1.0
    uniform = np.ones(8) / 8.0
    invariant_residual = float(np.linalg.norm(transition @ uniform - uniform))
    eigenvalues = np.linalg.eigvals(transition)
    spectral_gap = 1.0 - float(sorted((abs(x) for x in eigenvalues), reverse=True)[1])
    instantaneous_tv = 0.5 * float(np.linalg.norm(one_hot(0, 8) - uniform, ord=1))
    orbit_index_average_max = max(float(np.linalg.norm(np.asarray(row["orbit_index_average"]) - uniform, ord=1)) for row in orbit_rows)

    # Feed every derived address to the unchanged Cycle592 ROM and exact
    # member/occurrence interface for its three lawful programs.
    for program, address in product(range(3), range(8)):
        rom = c592.physical_innovation_step(c592.prepare_a(program, address))
        member = singleton(tuple(rom[s] for s in c592.A_MEMBER), "Route A coupled member")
        history = singleton(tuple(rom[s] for s in c592.A_HISTORY), "Route A coupled history")
        base = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=history)
        fields, _law = c552.snapshot_view(c552.physical_step(base), 0)
        interface_failures += int(fields[:3] != (1, 1, 1))

    held_rows = []
    held_refusals = 0
    existing_rows = tuple(c592.table_grade(program) for program in range(3))
    for offset, (name, state, size) in enumerate(zip(HELD_NAMES, HELD_STATES, HELD_SIZES), start=3):
        q = grade(state)
        best_existing = min(float(np.linalg.norm(row - q, ord=1)) for row in existing_rows)
        best_d8, counts = denominator8_best(q)
        try:
            c592.prepare_a(offset, 0)
        except ValueError:
            held_refusals += 1
        held_rows.append({"name": name, "size": size, "grade": tuple(float(x) for x in q), "best_unchanged_ROM_L1": best_existing, "best_any_denominator8_L1": best_d8, "best_denominator8_counts": counts})

    witness = prepare_a(0)
    ideal = bath_a_step(witness)
    deleted = c587.apply_schedule(witness, A_SCHEDULE, delete_label="A:cross:0")
    deletion_residual = float(np.linalg.norm(np.asarray(deleted) - np.asarray(ideal)))
    frames = c577.c41.proper_cubic_rotations()
    coordinates = ring16_coordinates()
    edge_failures = 0
    for frame in frames:
        transformed = tuple(tuple(int(v) for v in frame @ np.asarray(point)) for point in coordinates)
        for gate in A_SCHEDULE:
            left, right = (transformed[site] for site in gate.sites)
            edge_failures += int(sum(abs(a - b) for a, b in zip(left, right)) != 1)
    result = {
        "route": "A TI doubled-lane reversible one-carrier address bath",
        "bath_law_sha256": BATH_LAW_SHA256,
        "physical_M2": 16,
        "translation_invariant_radius_cells": 1,
        "parallel_SWAP_layers": 2,
        "nearest_neighbor_two_M2_SWAPS_per_step": 16,
        "EG_failures": eg_failures, "inverse_failures": inverse_failures, "carrier_ledger_failures": ledger_failures,
        "orbit_rows": orbit_rows,
        "uniform_invariant_residual": invariant_residual,
        "eight_step_orbit_index_average_maximum_L1_residual": orbit_index_average_max,
        "instantaneous_delta_to_uniform_TV_every_step": instantaneous_tv,
        "permutation_spectral_gap": spectral_gap,
        "stochastic_mixing_or_convergence_derived": False,
        "exact_Cycle592_552_531_interface_failures": interface_failures,
        "new_offgrid_held_rows": held_rows,
        "unchanged_Cycle592_ROM_lawful_domain_refusals": held_refusals,
        "cross_edge_deletion_residual": deletion_residual,
        "proper_cubic_frames": len(frames), "all24_ring_edge_tests": len(frames) * 16, "all24_ring_edge_failures": edge_failures,
        "bath_carrier_catalytically_recurs": True,
        "fresh_ROM_archive_blocks_per_occurrence": 1,
        "ROM_archive_resource_renewal_derived": False,
        "uniform_probability_or_objective_actuality_derived": False,
        "pass": not any((eg_failures, inverse_failures, ledger_failures, interface_failures, edge_failures))
        and invariant_residual < TOL and orbit_index_average_max < TOL and instantaneous_tv > 0.8
        and abs(spectral_gap) < TOL and held_refusals == 2 and min(row["best_unchanged_ROM_L1"] for row in held_rows) > TOL
        and min(row["best_any_denominator8_L1"] for row in held_rows) > TOL and deletion_residual > TOL,
    }
    check("Route A derives a uniform orbit-index address marginal from a TI reversible bath while exposing zero stochastic mixing and unchanged-ROM off-grid refusal", result["pass"], result)
    return result


# Route B: coherent local uniform-address dilation with explicit environment.
H = c577.H
I2 = c577.I2
CNOT = np.asarray(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)), dtype=complex)


def apply_one(state: np.ndarray, matrix: np.ndarray, site: int, count: int) -> np.ndarray:
    tensor = state.reshape((2,) * count)
    moved = np.moveaxis(tensor, site, 0).reshape(2, -1)
    moved = matrix @ moved
    return np.moveaxis(moved.reshape((2,) + (2,) * (count - 1)), 0, site).reshape(-1)


def apply_two(state: np.ndarray, matrix: np.ndarray, first: int, second: int, count: int) -> np.ndarray:
    tensor = state.reshape((2,) * count)
    moved = np.moveaxis(tensor, (first, second), (0, 1)).reshape(4, -1)
    moved = matrix @ moved
    return np.moveaxis(moved.reshape((2, 2) + (2,) * (count - 2)), (0, 1), (first, second)).reshape(-1)


def reduced_density(state: np.ndarray, keep: tuple[int, ...], count: int) -> np.ndarray:
    trace = tuple(i for i in range(count) if i not in keep)
    moved = np.transpose(state.reshape((2,) * count), keep + trace).reshape(2 ** len(keep), -1)
    return moved @ moved.conj().T


def route_b_state(*, delete_h: int | None = None, delete_copy: int | None = None) -> np.ndarray:
    state = c577.ket(0, 64)
    for site in range(3):
        if site != delete_h:
            state = apply_one(state, H, site, 6)
    for site in range(3):
        if site != delete_copy:
            state = apply_two(state, CNOT, site, 3 + site, 6)
    return state


def route_b_inverse(state: np.ndarray) -> np.ndarray:
    for site in reversed(range(3)):
        state = apply_two(state, CNOT, site, 3 + site, 6)
    for site in reversed(range(3)):
        state = apply_one(state, H, site, 6)
    return state


def von_neumann_entropy(rho: np.ndarray) -> float:
    values = np.linalg.eigvalsh(rho)
    return float(-sum(value * np.log2(value) for value in values if value > TOL))


def route_b_controls() -> dict[str, object]:
    output = route_b_state()
    target = np.eye(8) / 8.0
    address_rho = reduced_density(output, (0, 1, 2), 6)
    environment_rho = reduced_density(output, (3, 4, 5), 6)
    uniform_residual = float(np.linalg.norm(address_rho - target))
    environment_residual = float(np.linalg.norm(environment_rho - target))
    inverse_residual = float(np.linalg.norm(route_b_inverse(output) - c577.ket(0, 64)))
    h_deletion_residual = float(np.linalg.norm(reduced_density(route_b_state(delete_h=0), (0, 1, 2), 6) - target))
    copy_deletion_residual = float(np.linalg.norm(reduced_density(route_b_state(delete_copy=0), (0, 1, 2), 6) - target))
    global_entropy = von_neumann_entropy(np.outer(output, output.conj()))
    local_entropy = von_neumann_entropy(address_rho)
    # Layout address_i at (i,0,0), environment_i at (i,1,0).
    frames = c577.c41.proper_cubic_rotations()
    edge_failures = 0
    for frame in frames:
        for i in range(3):
            left = frame @ np.asarray((i, 0, 0))
            right = frame @ np.asarray((i, 1, 0))
            edge_failures += int(sum(abs(int(a - b)) for a, b in zip(left, right)) != 1)
    result = {
        "route": "B open coherent H3/address-environment bath",
        "physical_M2_per_episode": 6,
        "one_M2_H": 3, "nearest_neighbor_address_environment_CNOT": 3,
        "uniform_reduced_address_residual": uniform_residual,
        "uniform_reduced_environment_residual": environment_residual,
        "full_unitary_inverse_residual": inverse_residual,
        "delete_H_reduced_residual": h_deletion_residual,
        "delete_environment_copy_reduced_residual": copy_deletion_residual,
        "global_pure_entropy_bits": global_entropy,
        "reduced_address_entropy_bits": local_entropy,
        "entropy_called_thermodynamic_or_work": False,
        "fresh_zero_M2_source_per_episode": 6,
        "retained_environment_sink_M2_per_episode": 3,
        "finite_two_episode_fresh_M2_debit": 12,
        "source_sink_renewal_derived": False,
        "all_eight_coherent_sectors_retained": True,
        "objective_address_or_Record_derived": False,
        "proper_cubic_frames": len(frames), "all24_copy_edge_tests": len(frames) * 3, "all24_copy_edge_failures": edge_failures,
        "pass": uniform_residual < TOL and environment_residual < TOL and inverse_residual < TOL
        and h_deletion_residual > TOL and copy_deletion_residual > TOL
        and abs(global_entropy) < TOL and abs(local_entropy - 3.0) < TOL and edge_failures == 0 and len(frames) == 24,
    }
    check("Route B derives a uniform reduced marginal from a local coherent dilation but retains all sectors and consumes unrenewed fresh source/sink M2", result["pass"], result)
    return result


# Route C: table-independent reversible maximal-period LFSR.
C_SCHEDULE = (
    Gate("CNOT", (2, 0), "C:feedback"),
    Gate("CNOT", (0, 2), "C:recover-x0"),
    Gate("SWAP", (1, 2), "C:rotate"),
)


def lfsr_step(state: int) -> int:
    if state not in range(8):
        raise ValueError("LFSR state leaves three-bit domain")
    bits = tuple((state >> i) & 1 for i in range(3))
    output = c587.apply_schedule(bits, C_SCHEDULE)
    return sum(bit << i for i, bit in enumerate(output))


def lfsr_orbit(genesis: int, length: int) -> tuple[int, ...]:
    if genesis not in range(8) or length < 1:
        raise ValueError("LFSR orbit leaves domain")
    state = genesis
    output = []
    for _ in range(length):
        state = lfsr_step(state)
        output.append(state)
    return tuple(output)


def route_c_controls() -> dict[str, object]:
    orbit = lfsr_orbit(1, 7)
    zero_orbit = lfsr_orbit(0, 7)
    permutation_failures = int(set(orbit) != set(range(1, 8)) or zero_orbit != (0,) * 7)
    inverse_failures = 0
    for state in range(8):
        bits = tuple((state >> i) & 1 for i in range(3))
        inverse_failures += c587.apply_schedule(c587.apply_schedule(bits, C_SCHEDULE), C_SCHEDULE, reverse=True) != bits
    uniform = np.ones(8) / 8.0
    address_L1 = float(np.linalg.norm(empirical(orbit) - uniform, ord=1))
    rom_rows = []
    for program in range(3):
        histories = tuple(c592.HISTORY_TABLE[program][address] for address in orbit)
        residual = float(np.linalg.norm(empirical(histories) - c592.table_grade(program), ord=1))
        rom_rows.append({"program": program, "seven_orbit_history_frequency": tuple(float(x) for x in empirical(histories)), "target_table_grade": tuple(float(x) for x in c592.table_grade(program)), "L1_residual": residual})
    # Activate the feedback control explicitly; the former site-1 one-hot
    # witness did not exercise the deleted CNOT and was therefore vacuous.
    deletion_witness = (0, 0, 1)
    ideal = c587.apply_schedule(deletion_witness, C_SCHEDULE)
    deleted = c587.apply_schedule(deletion_witness, C_SCHEDULE, delete_label="C:feedback")
    deletion_residual = float(np.linalg.norm(np.asarray(deleted) - np.asarray(ideal)))
    line = c587.static_line_compiler_controls(C_SCHEDULE, 3)
    result = {
        "route": "C table-independent reversible seven-cycle LFSR typicality comparator",
        "bath_law_sha256": BATH_LAW_SHA256,
        "orbit_from_one": orbit, "zero_fixed_orbit": zero_orbit,
        "permutation_orbit_failures": permutation_failures,
        "inverse_failures": inverse_failures,
        "seven_orbit_address_to_uniform8_L1_residual": address_L1,
        "unchanged_ROM_frequency_rows": rom_rows,
        "feedback_deletion_residual": deletion_residual,
        "static_nearest_neighbor_line_compiler": line,
        "law_contains_ROM_table_or_grade": False,
        "typicality_measure_or_objective_genesis_derived": False,
        "pass": not permutation_failures and not inverse_failures and address_L1 > TOL
        and min(row["L1_residual"] for row in rom_rows) > TOL and deletion_residual > TOL and line["pass"],
    }
    check("Route C gives an exact table-independent seven-cycle typicality comparator whose orbit visibly fails the required uniform-eight marginal", result["pass"], result)
    return result


def covariance_domain_controls() -> dict[str, object]:
    frames = c577.c41.proper_cubic_rotations()
    frame_failures = group_failures = tests = 0
    for frame in frames:
        for member in range(4):
            source = c552.prepare(member, 0, member, 0, edge=1, plus=1, minus=0, K_position=member)
            framed, axis = c552.frame_word(source, 0, frame)
            expected, expected_axis = c552.frame_word(c552.physical_step(source), 0, frame)
            frame_failures += int(c552.physical_step(framed) != expected or axis != expected_axis)
            tests += 1
    for left, right in product(frames, repeat=2):
        source = c552.prepare(0, 0, 0, 0, edge=1, plus=1, minus=0, K_position=0)
        for axis in range(3):
            _, axis1 = c552.frame_word(source, axis, right)
            _, axis2 = c552.frame_word(source, axis1, left)
            _, axisp = c552.frame_word(source, axis, left @ right)
            group_failures += axis2 != axisp
    malformed = (lambda: prepare_a(8), lambda: lfsr_orbit(8, 7), lambda: lfsr_orbit(1, 0), lambda: plus_minus_state(1.2), lambda: c592.prepare_a(3, 0))
    refused = 0
    for action in malformed:
        try:
            action()
        except ValueError:
            refused += 1
    result = {"proper_cubic_frames": len(frames), "all24_member_tests": tests, "all24_member_failures": frame_failures,
              "all576_axis_tests": len(frames) ** 2 * 3, "all576_axis_failures": group_failures,
              "malformed_domain_refusals": refused, "malformed_domain_total": len(malformed),
              "pass": len(frames) == 24 and frame_failures == group_failures == 0 and refused == len(malformed)}
    check("all24/all576 and lawful-domain controls remain exact", result["pass"], result)
    return result


def dependency_discipline_controls() -> dict[str, object]:
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    body = " ".join(note.lower().replace("`", "").replace("*", "").split())
    required = ("authority: none", "audit: unset", "route a", "route b", "route c", "35 exact-pinned surfaces",
                "conditional rom", "candidate instrument", "global irreversibility is not derived",
                "physical-m2 composition and leakage boundary", "off-grid", "bath law",
                "stationary", "mixing", "nearest-neighbor", "coherent sectors", "packet is not record", "frequency is not probability",
                "spent token is not energy", "schedule is not time", "all 24", "all 576", "supplied / derived / open",
                "n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n1 status: fail", "no axiom pressure")
    missing = tuple(fragment for fragment in required if fragment not in body)
    declared = re.search(r"Runner SHA-256:\s*([0-9a-f]{64})", note)
    routes = (
        {"family": "TI reversible Margolus carrier bath", "status": "ATTEMPTED", "terminal": "derive objective sampling/Record law and renew ROM archives"},
        {"family": "open coherent uniform-address dilation", "status": "ATTEMPTED", "terminal": "derive fresh source/sink renewal and one objective address"},
        {"family": "table-independent LFSR typicality", "status": "ATTEMPTED", "terminal": "derive correct eight-address invariant orbit and actuality measure"},
        {"family": "chaotic reversible lattice gas", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "prove ergodic marginal/mixing on a physical invariant shell"},
        {"family": "dissipative stationary reservoir", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "construct source/sink balance and thermodynamic semantics"},
        {"family": "continuous grade compiler", "status": "UNTESTED_OPEN_NOT_COUNTED", "terminal": "synthesize off-grid transition law without finite answer-table import"},
    )
    walls = ("bath stationary marginal", "objective actuality", "ROM/state-family law", "Record permanence", "frequency/probability calibration", "resource renewal")
    pairs = tuple({"pair": (walls[a], walls[b]), "independent": True, "reason": "neither tested closure has the other's typed witness"} for a, b in combinations(range(6), 2))
    hidden = ("one-carrier genesis", "finite periodic ring and chart", "H and zero-state source", "environment trace/access",
              "unchanged Cycle592 ROM/program domain", "Cycle552 interface inputs", "fresh ROM/archive capacity", "held states and finite sizes")
    residuals = (
        {"route": "A", "witness": "uniform orbit-index average but TV=7/8 and spectral gap zero", "meaning": "equidistribution, not stochastic mixing/probability"},
        {"route": "A held", "witness": "unchanged ROM refusal and positive denominator-eight residual", "meaning": "declared finite ROM wall, not universal impossibility"},
        {"route": "B", "witness": "uniform reduced diagonal and exact global inverse", "meaning": "open-channel marginal, not objective address/irreversibility"},
        {"route": "C", "witness": "seven-cycle marginal differs from uniform eight", "meaning": "this table-independent typicality law fails target"},
    )
    partial = ("retain Route A as a catalytic deterministic address enumerator", "retain Route B as a uniform coherent source diagnostic",
               "retain Route C as an orbit-support falsifier", "build held-state-independent continuous/rational approximation compiler with error budget",
               "derive stationary resource bath and separate framework Record law before probability calibration")
    steelman = {"mechanism": "a chaotic reversible lattice gas on a derived microcanonical shell could have an eight-address factor with provable mixing, while a continuous grade compiler and renewable formation medium handle off-grid states and Records",
                "terminal": "construct the local law, invariant shell, mixing bound, grade compiler, resource balance, actuality owner, and blinded Records", "status": "open"}
    echo = ("Cycle584 derived local transport but not stationary boundary supply", "Cycle592 supplied balanced address words and finite ROM",
            "Cycle595 derives deterministic orbit equidistribution but not mixing", "open dilation gives uniform marginal while retaining coherent sectors",
            "new off-grid states isolate the unchanged-ROM domain wall")
    qualifying = tuple(x for x in routes if x["status"] == "ATTEMPTED")
    receipt_cycles = ("552", "565", "571", "577", "580", "582", "584", "587", "592")
    receipt_checks = {}
    for cycle in receipt_cycles:
        receipt = json.loads(FROZEN_PATHS[f"Cycle{cycle} receipt"].read_text(encoding="utf-8"))
        cycle_checks = {
            "runner": receipt.get("runner_sha256") == FROZEN[f"Cycle{cycle} runner"],
            "note": receipt.get("note_sha256") == FROZEN[f"Cycle{cycle} note"],
            "verified": receipt.get("pass") is True
            and receipt.get("tests_passed") == receipt.get("tests_total"),
            "authority_audit": receipt.get("authority") == "none" and receipt.get("audit") == "unset",
        }
        if f"Cycle{cycle} cold" in FROZEN:
            cycle_checks["cold"] = receipt.get("cold_transcript_sha256") == FROZEN[f"Cycle{cycle} cold"]
        receipt_checks[f"Cycle{cycle}"] = cycle_checks
    discipline = {"N1_routes": routes, "N1_qualifying": len(qualifying), "N1_required": 5, "N1_status": "FAIL",
                  "N2_walls": walls, "N2_pairs": pairs, "N3_supplies": hidden, "N4_residuals": residuals,
                  "N5": "bounded route results only; no probability/Record/energy/time promotion", "N6": partial, "N7": steelman, "N8": echo,
                  "broad_no_go": "FAIL_DO_NOT_SHIP", "minimum_content": "FAIL_DO_NOT_SHIP", "shared_obstruction": "NOT_ESTABLISHED", "axiom_pressure": "NONE"}
    result = {"expected": FROZEN, "observed": observed, "bath_law_sha256": BATH_LAW_SHA256,
              "expected_bath_law_sha256": EXPECTED_BATH_LAW_SHA256, "held_sha256": HELD_SHA256,
              "note_missing": missing, "declared_runner_sha256": declared.group(1) if declared else None, "runner_sha256": file_sha(Path(__file__)),
              "receipt_checks": receipt_checks,
              "discipline": discipline,
              "inventory": {"supplied": hidden,
                            "derived": ("TI catalytic address orbit and uniform eight-step orbit-index average", "open coherent uniform reduced marginal", "LFSR orbit falsifier", "off-grid fixed-ROM/denominator residuals and all controls"),
                            "open": ("objective actuality and Record", "stochastic mixing/invariant physical ensemble", "continuous off-grid ROM", "archive/source renewal and thermodynamics", "Born calibration/time/source/gravity")},
              "pass": observed == FROZEN and BATH_LAW_SHA256 == EXPECTED_BATH_LAW_SHA256 and not missing and declared is not None
              and declared.group(1) == file_sha(Path(__file__))
              and all(all(checks.values()) for checks in receipt_checks.values())
              and len(qualifying) == 3 and len(pairs) == 15 and len(partial) == len(echo) == 5}
    check("exact shores, bath-before-held freeze, inventory, and N1-N8 block overclaim and axiom pressure", result["pass"], result)
    return result


@dataclass(frozen=True)
class Summary:
    authority: str = AUTHORITY
    audit: str = AUDIT
    strongest_result: str = "TI catalytic one-carrier address bath with exact uniform orbit-index marginal feeding unchanged Cycle592/552/531"
    stochastic_mixing: None = None
    objective_actuality: None = None
    framework_Record: None = None
    derived_Born_probability: None = None
    axiom_pressure: None = None


def main() -> int:
    started = time.perf_counter()
    signal.signal(signal.SIGALRM, lambda _s, _f: (_ for _ in ()).throw(TimeoutError("Cycle595 wall cap")))
    signal.alarm(int(WALL_CAP_SECONDS))
    try:
        a = route_a_controls(); b = route_b_controls(); c = route_c_controls(); cov = covariance_domain_controls(); dep = dependency_discipline_controls()
        resources = {"elapsed_seconds": time.perf_counter() - started, "maximum_RSS_bytes": rss_bytes(), "wall_cap_seconds": WALL_CAP_SECONDS, "RSS_cap_bytes": RSS_CAP_BYTES}
        check("cold resource caps", resources["elapsed_seconds"] < WALL_CAP_SECONDS and resources["maximum_RSS_bytes"] < RSS_CAP_BYTES, resources)
        print(json.dumps({"route_A": a, "route_B": b, "route_C": c, "covariance_domain": cov, "dependency_discipline_inventory": dep,
                          "resources": resources, "summary": Summary().__dict__, "pass": PASS, "fail": FAIL}, indent=2, sort_keys=True))
    finally:
        signal.alarm(0)
    print(f"RESULT pass={PASS} fail={FAIL}")
    print("authority=none; audit=unset; coherent sectors are not objective actuality; packet is not Record; frequency is not probability; spent token is not energy; schedule is not time")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
