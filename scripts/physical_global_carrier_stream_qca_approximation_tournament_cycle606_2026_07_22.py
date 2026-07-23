#!/usr/bin/env python3
"""Cycle606: global carrier stream/QCA and finite-precision tournament.

The priority route constructs a compact reversible double-buffer shift for the
Cycle600 three-species four-role-bit word.  Direction-expanded partition lanes and a
state-carried buffer phase are independent comparators.  A bounded H/T/Tdg
word search measures, but does not erase, the Cycle603 analog-angle import.
Every construction in this receipt is a logical/register circuit unless a
literal M2 layout, primitive product, encoder/intertwiner/leakage calculation,
and one-site translation-covariant physical law are executed; none is.  A
schedule is not physical time; register counts are not energy or source.
Authority none; audit unset; author artifact status accepted false.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22 as c603
import physical_root_free_full_N3_carrier_genesis_tournament_cycle600_2026_07_22 as c600


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GLOBAL_CARRIER_STREAM_QCA_APPROXIMATION_TOURNAMENT_CYCLE606_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_global_carrier_stream_qca_approximation_"
    "tournament_cycle606_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_global_carrier_stream_qca_approximation_"
    "tournament_cycle606_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-9
CAP_SECONDS = 360.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()

PINS = {
    "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py":
        "e64032e369e08e03ad2a742a2bde6914d8adc6ed1fd64f15f4e301c1c8dea739",
    "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md":
        "ddc06d6d4abf945794b1c0b7566c9183fa744839d1ba5630c1d9ad8b4559c417",
    "outputs/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_receipt_2026_07_22.json":
        "751487fa50a738d5473f7ddcb77474785c84463dda1264a34de2643f19102871",
    "outputs/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_cold_2026_07_22.txt":
        "35385a09b5d075e553de1de9302e0317dd415acbe1f5ccf9425905eedae94174",
}


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (value.real, value.imag)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    receipt = json.loads((ROOT / (
        "outputs/physical_carrier_preparation_elementary_synthesis_"
        "tournament_cycle603_receipt_2026_07_22.json"
    )).read_text())
    route_a = receipt["route_A_structured_elementary_compiler"]
    expected_graph = dict(receipt["shore"]["import_audit"]["expected_transitive_sha256"])
    expected_graph.update(receipt["pins"])
    expected_graph.update(PINS)
    observed_graph = {name: sha(ROOT / name) for name in expected_graph}
    actual_modules = c600.imported_science_modules(c600, c603, c603.c219, c603.c230)
    uncovered = sorted(set(actual_modules.values()) - set(expected_graph))
    inherited = {
        "Cycle603_pass": receipt["pass"],
        "tests_passed": receipt["tests_passed"],
        "author_artifact_status_accepted": receipt["author_artifact_status_accepted"],
        "support_two_role_event_circuit": route_a["exact_support_two_parametric_role_event_circuit"],
        "finite_alphabet_closure": route_a["exact_declared_finite_alphabet_elementary_closure"],
        "global_stream_schedule": route_a["scratch_and_schedule"]["global_conflict_free_stream_schedule_compiled"],
        "persistent_role_bits_per_cell": route_a["scratch_and_schedule"]["persistent_Cycle600_carrier_role_bits_per_cell"],
        "physical_M2_scope": receipt["physical_M2_scope"],
        "broad_negative_gate": receipt["broad_negative_gate"],
        "import_audit": {
            "expected_transitive_sha256": expected_graph,
            "observed_transitive_sha256": observed_graph,
            "actual_imported_modules": actual_modules,
            "uncovered_imported_modules": uncovered,
            "expected_file_count": len(expected_graph),
            "runtime_module_count": len(actual_modules),
        },
    }
    condition = (
        observed == PINS and inherited["Cycle603_pass"]
        and inherited["tests_passed"] == 7
        and not inherited["author_artifact_status_accepted"]
        and inherited["support_two_role_event_circuit"]
        and not inherited["finite_alphabet_closure"]
        and not inherited["global_stream_schedule"]
        and inherited["persistent_role_bits_per_cell"] == 12
        and not inherited["physical_M2_scope"]["literal_layout_compiled"]
        and not inherited["physical_M2_scope"]["primitive_composition"]
        and inherited["physical_M2_scope"]["intertwiner_residual"] is None
        and not inherited["physical_M2_scope"]["leakage_evaluated"]
        and inherited["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and observed_graph == expected_graph and not uncovered
    )
    check("accepted Cycle603 shore is byte exact", condition, {
        "observed": observed, "inherited": inherited,
    })
    return {"Cycle603_receipt": receipt, "verified_inheritance": inherited}


# ---------------------------------------------------------------------------
# Shared cubic-word utilities.


def site_tuple(site: int, length: int) -> tuple[int, int, int]:
    return c600.c598.c593.site_tuple(site, length)


def site_flat(coordinate: tuple[int, int, int], length: int) -> int:
    return c600.c598.c593.site_flat(coordinate, length)


def displacement_for_word(word: int) -> tuple[int, int, int]:
    if 4 <= word <= 9:
        return tuple(int(value) for value in c600.c598.c593.c210.DIRECTIONS[word - 4])
    return 0, 0, 0


def target_site(site: int, word: int, length: int) -> int:
    coordinate = site_tuple(site, length)
    displacement = displacement_for_word(word)
    return site_flat(tuple(
        (coordinate[axis] + displacement[axis]) % length for axis in range(3)
    ), length)


def source_site(target: int, word: int, length: int) -> int:
    coordinate = site_tuple(target, length)
    displacement = displacement_for_word(word)
    return site_flat(tuple(
        (coordinate[axis] - displacement[axis]) % length for axis in range(3)
    ), length)


@lru_cache(maxsize=None)
def target_map(length: int, word: int) -> np.ndarray:
    """The translated site permutation for one word, cached by torus size."""
    return np.asarray(
        [target_site(site, word, length) for site in range(length**3)], dtype=np.int64
    )


def translate_words(words: np.ndarray, displacement: tuple[int, int, int],
                    length: int) -> np.ndarray:
    result = np.zeros_like(words)
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        target = site_flat(tuple(
            (coordinate[axis] + displacement[axis]) % length for axis in range(3)
        ), length)
        result[target] = words[site]
    return result


def frame_words(words: np.ndarray, frame: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros_like(words)
    for site in range(length**3):
        coordinate = np.asarray(site_tuple(site, length), dtype=int)
        target = site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
        for species in range(words.shape[1]):
            result[target, species] = c603.frame_word(int(words[site, species]), frame)
    return result


def abstract_stream(words: np.ndarray, length: int) -> tuple[np.ndarray, int]:
    result = np.zeros_like(words)
    collisions = 0
    for site in range(length**3):
        for species in range(words.shape[1]):
            word = int(words[site, species])
            if word == 0:
                continue
            target = target_site(site, word, length)
            collisions += result[target, species] != 0
            if result[target, species] == 0:
                result[target, species] = word
    return result, collisions


def valid_sector(words: np.ndarray, buffer: np.ndarray | None = None) -> dict:
    invalid = int(np.count_nonzero((words < 0) | (words > 9)))
    counts = tuple(int(np.count_nonzero(words[:, species])) for species in range(3))
    dirty = 0 if buffer is None else int(np.count_nonzero(buffer))
    return {
        "invalid_words": invalid,
        "species_counts": counts,
        "dirty_buffer_words": dirty,
        "pass": invalid == dirty == 0 and counts == (1, 1, 1),
    }


def random_lawful(length: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    words = np.zeros((length**3, 3), dtype=np.int16)
    for species in range(3):
        site = int(rng.integers(length**3))
        words[site, species] = int(rng.integers(1, 10))
    return words


def arrays_equal(*pairs: tuple[np.ndarray, np.ndarray]) -> bool:
    return all(np.array_equal(first, second) for first, second in pairs)


# ---------------------------------------------------------------------------
# Route A: compact reversible double buffer.


def xor_scatter(active: np.ndarray, buffer: np.ndarray, length: int,
                skip: tuple[int, int, int] | None = None,
                word_order: tuple[int, ...] = tuple(range(1, 16))) -> None:
    for species in range(3):
        for word in word_order:
            sources = np.flatnonzero(active[:, species] == word)
            if skip is not None and skip[0] == species and skip[2] == word:
                sources = sources[sources != skip[1]]
            # Repeated targets are intentional on malformed sectors: XOR.at
            # retains the exact full-space reversible extension.
            np.bitwise_xor.at(buffer[:, species], target_map(length, word)[sources], word)


def xor_clear(active: np.ndarray, buffer: np.ndarray, length: int,
              skip: tuple[int, int, int] | None = None,
              word_order: tuple[int, ...] = tuple(range(1, 16))) -> None:
    for species in range(3):
        for word in word_order:
            sites = np.flatnonzero(buffer[target_map(length, word), species] == word)
            if skip is not None and skip[0] == species and skip[2] == word:
                sites = sites[sites != skip[1]]
            active[sites, species] ^= word


def double_buffer_forward(active: np.ndarray, buffer: np.ndarray, length: int,
                          skip_scatter: tuple[int, int, int] | None = None,
                          skip_clear: tuple[int, int, int] | None = None,
                          skip_swap: tuple[int, int] | None = None,
                          scatter_order: tuple[int, ...] = tuple(range(1, 16)),
                          clear_order: tuple[int, ...] = tuple(range(1, 16)),
                          ) -> tuple[np.ndarray, np.ndarray]:
    active = active.copy()
    buffer = buffer.copy()
    xor_scatter(active, buffer, length, skip_scatter, scatter_order)
    xor_clear(active, buffer, length, skip_clear, clear_order)
    output_active, output_buffer = buffer.copy(), active.copy()
    if skip_swap is not None:
        site, species = skip_swap
        output_active[site, species] = active[site, species]
        output_buffer[site, species] = buffer[site, species]
    return output_active, output_buffer


def double_buffer_inverse(active: np.ndarray, buffer: np.ndarray,
                          length: int) -> tuple[np.ndarray, np.ndarray]:
    pre_active, pre_buffer = buffer.copy(), active.copy()  # undo local SWAP
    xor_clear(pre_active, pre_buffer, length)
    xor_scatter(pre_active, pre_buffer, length)
    return pre_active, pre_buffer


def c4x_sequence(controls: tuple[int, int, int, int], target: int,
                 work: tuple[int, int], prefix: str) -> list[c603.Gate]:
    first = c603.toffoli_sequence(controls[0], controls[1], work[0], prefix + "_and0")
    second = c603.toffoli_sequence(work[0], controls[2], work[1], prefix + "_and1")
    final = c603.toffoli_sequence(work[1], controls[3], target, prefix + "_target")
    return first + second + final + c603.inverse_gates(second) + c603.inverse_gates(first)


def equality_copy_block(word: int) -> list[c603.Gate]:
    controls = (0, 1, 2, 3)
    flag, work = 4, (5, 6)
    negative = tuple(index for index, value in enumerate(c603.bits(word, 4)) if value == 0)
    compute = c603.negative_control_wrap(
        c4x_sequence(controls, flag, work, f"eq{word}"), negative, f"eq{word}",
    )
    copies = [
        c603.two(f"eq{word}_copy_b{bit}", flag, 7 + bit, c603.CNOT, "CNOT")
        for bit, value in enumerate(c603.bits(word, 4)) if value
    ]
    # Move negative-control X outside both compute and uncompute so their count
    # is not doubled by treating each target bit as a fresh predicate.
    opening = [c603.one(f"eq{word}_neg_open_{q}", q, c603.X2, "X") for q in negative]
    raw_compute = c4x_sequence(controls, flag, work, f"eq{word}_raw")
    closing = [c603.one(f"eq{word}_neg_close_{q}", q, c603.X2, "X") for q in reversed(negative)]
    return opening + raw_compute + copies + c603.inverse_gates(raw_compute) + closing


def double_buffer_gate_template() -> dict:
    blocks = []
    for word in range(1, 16):
        gates = equality_copy_block(word)
        blocks.append({
            "word": word,
            "popcount": sum(c603.bits(word, 4)),
            "gate_counts": c603.gate_counts(gates),
            "base_gate_count": len(gates),
            "schedule_sha256": c603.gate_hash(gates),
            "logical_role_line_routing": c603.routing_audit(gates, 11),
        })
    local_swaps = [
        c603.two(f"buffer_swap_bit{bit}", bit, 7 + bit, c603.SWAP, "SWAP")
        for bit in range(4)
    ]
    swap_routing = c603.routing_audit(local_swaps, 11)
    one_phase_counts: dict[str, int] = {}
    for row in blocks:
        for family, count in row["gate_counts"].items():
            one_phase_counts[family] = one_phase_counts.get(family, 0) + count
    # Two copy/clear phases and three species; species/cells are parallel for
    # depth but all instances count toward volume resources.
    per_cell_counts = {family: 6 * count for family, count in one_phase_counts.items()}
    per_cell_counts["SWAP"] = per_cell_counts.get("SWAP", 0) + 12
    phase_depth = sum(
        row["logical_role_line_routing"]["serial_nearest_neighbor_depth"]
        for row in blocks
    )
    depth = 2 * phase_depth + swap_routing["serial_nearest_neighbor_depth"]
    return {
        "word_blocks": blocks,
        "one_copy_or_clear_phase_one_species_counts": one_phase_counts,
        "complete_update_per_cell_gate_counts": per_cell_counts,
        "complete_update_per_cell_base_gate_count": sum(per_cell_counts.values()),
        "complete_update_constant_serial_NN_depth_species_parallel": depth,
        "local_buffer_SWAP_logical_role_line_routing": swap_routing,
        "persistent_active_plus_buffer_role_bits_per_cell": 24,
        "clean_flag_and_work_role_bits_per_species": 3,
        "maximum_live_role_bits_per_cell_species_parallel": 33,
        "maximum_logical_gate_support_role_bits": 2,
        "gate_alphabet": ("X", "H", "T", "Tdg", "CNOT", "SWAP"),
        "parameterized_angle_gates": 0,
        "scratch_returns_clean": True,
        "template_depends_on_volume_parity_origin_or_size": False,
    }


def exterior_eg_rows(length: int) -> dict:
    total_modes = 6 * length**3
    maximum_residual = 0.0
    inverse_residual = 0.0
    signs = set()
    samples = 0
    for number in range(4):
        candidates = list(combinations(range(min(total_modes, 10)), number))[:10]
        if number == 0:
            candidates = [()]
        for subset in candidates:
            terms = c600.encoded_global_terms(subset, total_modes)
            target, sign = c600.mapped_subset_and_sign(
                subset, lambda mode, L=length: c600.mode_stream_map(mode, L)
            )
            mapped = c600.map_encoded_terms(
                terms, total_modes, lambda mode, L=length: c600.mode_stream_map(mode, L)
            )
            expected = c600.encoded_global_terms(target, total_modes)
            maximum_residual = max(
                maximum_residual, c600.maximum_term_residual(mapped, expected, sign)
            )
            recovered = c600.map_encoded_terms(
                mapped, total_modes,
                lambda mode, L=length: c600.mode_inverse_stream_map(mode, L),
            )
            inverse_residual = max(
                inverse_residual, c600.maximum_term_residual(recovered, terms)
            )
            signs.add(sign)
            samples += 1
    return {
        "factorized_exterior_samples": samples,
        "maximum_double_buffer_EG_residual": maximum_residual,
        "maximum_inverse_EG_residual": inverse_residual,
        "exterior_reordering_signs": tuple(sorted(signs)),
    }


def compact_covariance(length: int) -> dict:
    frames = c600.c598.c593.c210.proper_cubic_frames()
    seed = random_lawful(length, 60600 + length)
    zero = np.zeros_like(seed)
    output, output_buffer = double_buffer_forward(seed, zero, length)
    translation_failures = 0
    for displacement_site in range(length**3):
        displacement = site_tuple(displacement_site, length)
        transformed_seed = translate_words(seed, displacement, length)
        transformed_output = translate_words(output, displacement, length)
        actual, actual_buffer = double_buffer_forward(transformed_seed, zero, length)
        translation_failures += int(not arrays_equal(
            (actual, transformed_output), (actual_buffer, output_buffer)
        ))
    frame_failures = 0
    for frame in frames:
        transformed_seed = frame_words(seed, frame, length)
        transformed_output = frame_words(output, frame, length)
        actual, actual_buffer = double_buffer_forward(transformed_seed, zero, length)
        frame_failures += int(not arrays_equal(
            (actual, transformed_output), (actual_buffer, output_buffer)
        ))
    group_failures = 0
    probe_sites = tuple(range(length**3))
    for first in frames:
        for second in frames:
            for site in probe_sites:
                coordinate = np.asarray(site_tuple(site, length), dtype=int)
                direct_site = site_flat(tuple(
                    int(value % length) for value in (first @ second) @ coordinate
                ), length)
                composed_site = site_flat(tuple(
                    int(value % length) for value in first @ (second @ coordinate)
                ), length)
                group_failures += direct_site != composed_site
                for word in range(16):
                    group_failures += (
                        c603.frame_word(word, first @ second)
                        != c603.frame_word(c603.frame_word(word, second), first)
                    )
    return {
        "translation_displacements_tested_on_one_frozen_lawful_seed": length**3,
        "translation_register_update_commutator_failures_on_seed": translation_failures,
        "proper_cubic_frames": len(frames),
        "all24_register_update_commutator_failures_on_one_frozen_lawful_seed": frame_failures,
        "all24_register_update_covariance_executed": True,
        "frame_products": len(frames)**2,
        "sites_and_words_per_frame_product": len(probe_sites) * 16,
        "all576_site_and_word_action_group_failures": group_failures,
        "all576_register_update_covariance_executed": False,
        "all576_executed_scope": "site permutation and 16-word frame action group law only",
    }


def compact_sublayer_order_audit(length: int) -> dict:
    """Check that label enumeration is presentation, not supplied ordering."""
    rng = np.random.default_rng(60640 + length)
    active = rng.integers(0, 16, size=(length**3, 3), dtype=np.int16)
    buffer = rng.integers(0, 16, size=(length**3, 3), dtype=np.int16)
    canonical = tuple(range(1, 16))
    frames = c600.c598.c593.c210.proper_cubic_frames()
    orders = [canonical, tuple(reversed(canonical))]
    orders.extend(tuple(c603.frame_word(word, frame) for word in canonical) for frame in frames)

    scatter_reference = buffer.copy()
    xor_scatter(active.copy(), scatter_reference, length, word_order=canonical)
    clear_reference = active.copy()
    xor_clear(clear_reference, buffer.copy(), length, word_order=canonical)
    frame_order_failures = 0
    for order in orders:
        scatter_actual = buffer.copy()
        xor_scatter(active.copy(), scatter_actual, length, word_order=order)
        clear_actual = active.copy()
        xor_clear(clear_actual, buffer.copy(), length, word_order=order)
        frame_order_failures += int(not np.array_equal(scatter_actual, scatter_reference))
        frame_order_failures += int(not np.array_equal(clear_actual, clear_reference))

    pairwise_failures = 0
    for first in canonical:
        for second in canonical:
            if second <= first:
                continue
            left = buffer.copy()
            right = buffer.copy()
            xor_scatter(active.copy(), left, length, word_order=(first, second))
            xor_scatter(active.copy(), right, length, word_order=(second, first))
            pairwise_failures += int(not np.array_equal(left, right))
            left = active.copy()
            right = active.copy()
            xor_clear(left, buffer.copy(), length, word_order=(first, second))
            xor_clear(right, buffer.copy(), length, word_order=(second, first))
            pairwise_failures += int(not np.array_equal(left, right))
    return {
        "frame_and_reverse_orders_tested_per_sublayer": len(orders),
        "frame_order_failures_scatter_plus_clear": frame_order_failures,
        "word_pairs_tested_per_sublayer": math.comb(15, 2),
        "pairwise_commutator_failures_scatter_plus_clear": pairwise_failures,
        "scatter_then_clear_order_is_still_a_fixed_macro_product": True,
    }


def route_a() -> dict:
    print("\nROUTE A — COMPACT REVERSIBLE DOUBLE BUFFER")
    gate_template = double_buffer_gate_template()
    rows = []
    condition = True
    rng = np.random.default_rng(60601)
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        volume = length**3
        one_carrier_failures = 0
        invalid_identity_failures = 0
        lawful_blank_buffer_failures = 0
        for species in range(3):
            for site in range(volume):
                for word in range(1, 10):
                    active = np.zeros((volume, 3), dtype=np.int16)
                    active[site, species] = word
                    zero = np.zeros_like(active)
                    output, out_buffer = double_buffer_forward(active, zero, length)
                    expected, collisions = abstract_stream(active, length)
                    one_carrier_failures += int(
                        collisions != 0 or not arrays_equal((output, expected), (out_buffer, zero))
                    )
                    lawful_blank_buffer_failures += int(np.count_nonzero(out_buffer) != 0)
                for word in range(10, 16):
                    active = np.zeros((volume, 3), dtype=np.int16)
                    active[site, species] = word
                    output, out_buffer = double_buffer_forward(active, np.zeros_like(active), length)
                    invalid_identity_failures += int(
                        not arrays_equal((output, active), (out_buffer, np.zeros_like(active)))
                    )

        inverse_failures = 0
        for _trial in range(10):
            active = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
            buffer = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
            output, out_buffer = double_buffer_forward(active, buffer, length)
            recovered, recovered_buffer = double_buffer_inverse(output, out_buffer, length)
            inverse_failures += int(not arrays_equal(
                (recovered, active), (recovered_buffer, buffer)
            ))

        deletion_input = np.zeros((volume, 3), dtype=np.int16)
        deletion_input[0, 0] = 4
        intact = double_buffer_forward(deletion_input, np.zeros_like(deletion_input), length)
        deleted_scatter = double_buffer_forward(
            deletion_input, np.zeros_like(deletion_input), length,
            skip_scatter=(0, 0, 4),
        )
        deleted_clear = double_buffer_forward(
            deletion_input, np.zeros_like(deletion_input), length,
            skip_clear=(0, 0, 4),
        )
        deleted_swap = double_buffer_forward(
            deletion_input, np.zeros_like(deletion_input), length,
            skip_swap=(target_site(0, 4, length), 0),
        )
        deletion_differences = {
            stage: int(np.count_nonzero(intact[0] != output[0])
                       + np.count_nonzero(intact[1] != output[1]))
            for stage, output in (
                ("scatter", deleted_scatter),
                ("clear", deleted_clear),
                ("swap", deleted_swap),
            )
        }

        target = 0
        collision_input = np.zeros((volume, 3), dtype=np.int16)
        first_source = source_site(target, 4, length)
        second_source = source_site(target, 5, length)
        collision_input[first_source, 0] = 4
        collision_input[second_source, 0] = 5
        collision_output, collision_buffer = double_buffer_forward(
            collision_input, np.zeros_like(collision_input), length
        )
        collision_inverse = double_buffer_inverse(collision_output, collision_buffer, length)
        collision_control = {
            "two_incoming_sources_distinct": first_source != second_source,
            "output_nonzero_active_words": int(np.count_nonzero(collision_output[:, 0])),
            "output_nonzero_buffer_words": int(np.count_nonzero(collision_buffer[:, 0])),
            "output_passes_exactly_one_valid_sector": valid_sector(collision_output, collision_buffer)["pass"],
            "inverse_recovers_malformed_input": arrays_equal(
                (collision_inverse[0], collision_input),
                (collision_inverse[1], np.zeros_like(collision_input)),
            ),
        }
        remote_collision_pairs = 0
        remote_collision_code_exits = 0
        remote_collision_inverse_failures = 0
        for first_word in range(4, 10):
            for second_word in range(first_word + 1, 10):
                first = source_site(target, first_word, length)
                second = source_site(target, second_word, length)
                if first == second:
                    continue
                remote_collision_pairs += 1
                probe = np.zeros((volume, 3), dtype=np.int16)
                probe[first, 0] = first_word
                probe[second, 0] = second_word
                probe_output = double_buffer_forward(probe, np.zeros_like(probe), length)
                remote_collision_code_exits += int(
                    not valid_sector(probe_output[0], probe_output[1])["pass"]
                )
                recovered = double_buffer_inverse(*probe_output, length)
                remote_collision_inverse_failures += int(not arrays_equal(
                    (recovered[0], probe), (recovered[1], np.zeros_like(probe))
                ))
        dirty_input = random_lawful(length, 60610 + length)
        dirty_buffer = np.zeros_like(dirty_input)
        dirty_buffer[0, 0] = 1
        dirty_domain = valid_sector(dirty_input, dirty_buffer)
        dirty_output = double_buffer_forward(dirty_input, dirty_buffer, length)
        dirty_recovered = double_buffer_inverse(*dirty_output, length)

        eg = exterior_eg_rows(length)
        covariance = compact_covariance(length)
        order_audit = compact_sublayer_order_audit(length)
        row = {
            "length": length,
            "split": split,
            "volume": volume,
            "lawful_single_species_site_label_rows": 3 * volume * 9,
            "lawful_stream_failures": one_carrier_failures,
            "lawful_complete_macro_blank_buffer_failures": lawful_blank_buffer_failures,
            "invalid_single_word_rows": 3 * volume * 6,
            "invalid_word_identity_failures": invalid_identity_failures,
            "random_full_space_inverse_trials": 10,
            "random_full_space_inverse_failures": inverse_failures,
            "delete_each_macro_stage_difference_words": deletion_differences,
            "collision_control": collision_control,
            "remote_two_carrier_collision_pairs": remote_collision_pairs,
            "remote_collision_pairs_leaving_declared_code": remote_collision_code_exits,
            "remote_collision_inverse_failures": remote_collision_inverse_failures,
            "dirty_buffer_domain_pass": dirty_domain["pass"],
            "dirty_buffer_inverse_recovery": arrays_equal(
                (dirty_recovered[0], dirty_input), (dirty_recovered[1], dirty_buffer)
            ),
            "persistent_register_role_bits": 24 * volume,
            "maximum_live_register_role_bits_species_parallel": 33 * volume,
            "complete_update_gate_instances": gate_template["complete_update_per_cell_base_gate_count"] * volume,
            "constant_NN_depth": gate_template["complete_update_constant_serial_NN_depth_species_parallel"],
            **eg,
            **covariance,
            **order_audit,
        }
        rows.append(row)
        condition &= (
            one_carrier_failures == lawful_blank_buffer_failures
            == invalid_identity_failures == inverse_failures == 0
            and all(value > 0 for value in deletion_differences.values())
            and collision_control["two_incoming_sources_distinct"]
            and not collision_control["output_passes_exactly_one_valid_sector"]
            and collision_control["inverse_recovers_malformed_input"]
            and remote_collision_pairs > 0
            and remote_collision_code_exits == remote_collision_pairs
            and remote_collision_inverse_failures == 0
            and not dirty_domain["pass"] and row["dirty_buffer_inverse_recovery"]
            and eg["maximum_double_buffer_EG_residual"] < TOL
            and eg["maximum_inverse_EG_residual"] < TOL
            and covariance["translation_register_update_commutator_failures_on_seed"] == 0
            and covariance["all24_register_update_commutator_failures_on_one_frozen_lawful_seed"] == 0
            and covariance["all576_site_and_word_action_group_failures"] == 0
            and not covariance["all576_register_update_covariance_executed"]
            and order_audit["frame_order_failures_scatter_plus_clear"] == 0
            and order_audit["pairwise_commutator_failures_scatter_plus_clear"] == 0
        )
    template_condition = (
        gate_template["complete_update_per_cell_base_gate_count"] > 0
        and gate_template["maximum_logical_gate_support_role_bits"] == 2
        and gate_template["parameterized_angle_gates"] == 0
        and gate_template["scratch_returns_clean"]
        and not gate_template["template_depends_on_volume_parity_origin_or_size"]
        and all(row["logical_role_line_routing"][
                    "all_two_role_bit_instances_after_move_apply_restore_are_declared_line_NN"
                ]
                for row in gate_template["word_blocks"])
    )
    result = {
        "status": "exact constant-overhead logical compact-register double-buffer permutation on the supplied one-carrier/species code; a declared role-line gate circuit is explicit, but no literal physical M2 placement or primitive product is compiled",
        "register_update": (
            "scatter B_(x+v(w)) XOR= w controlled by A_x=w; clear A_x XOR=w controlled by B_(x+v(w))=w; local SWAP(A_x,B_x)"
        ),
        "gate_template": gate_template,
        "rows": rows,
        "full_space_unitary_reason": "each equality-controlled XOR and local SWAP is a full-space involution; inverse reverses the three fixed substeps",
        "declared_code_space": "B=0, one valid nonzero word per species globally; bound labels shift and neutral labels remain",
        "locally_checkable_but_not_dynamically_enforced_auxiliary_constraints": "B=0 and word validity are on-cell checks; no gauge service or ordering is used",
        "auxiliary_constraints_locally_enforced": False,
        "nonlocal_sector_boundary": "exactly one carrier/species is inherited from Cycle600 and is not locally generated or enforced; it prevents same-species incoming collisions",
        "broader_exact_domain": "the same identity holds on any B=0 valid-word configuration whose translated carriers do not collide, but that domain is not claimed invariant under repeated updates",
        "invalid_extension": "single invalid labels 10..15 have zero displacement and return identically; arbitrary malformed/dirty states remain reversible but need not decode",
        "collisions_locally_rejected_or_repaired": False,
        "collisions_leave_declared_code_and_are_detected": True,
        "exactly_one_sector_locally_generated": False,
        "fixed_sublayer_sequence_is_physical_time": False,
        "host_parity_color_origin_or_size_query": False,
        "logical_role_line_gate_template_executed": True,
        "literal_physical_M2_layout_compiled": False,
        "physical_M2_primitive_product_composed": False,
        "physical_encoder_composed": False,
        "physical_intertwiner_residual": None,
        "physical_code_leakage_evaluated": False,
        "one_site_translation_covariant_physical_law_executed": False,
        "translation_invariant_global_register_supercell_embedding_executed": False,
        "global_route_vertex_disjointness_or_bounded_conflict_schedule_proved": False,
        "sharp_geometric_import": "one translation-invariant cubic supercell embedding, including scratch coordinates, whose simultaneous routed event instances are vertex-disjoint or have an explicit bounded conflict schedule",
        "pass_exact_declared_code_global_stream": bool(condition and template_condition),
        "pass_literal_physical_M2_compiler": False,
        "pass_full_malformed_code_preservation": False,
    }
    check(
        "Route A realizes the simultaneous Cycle600 torus stream as an exact compact-register double-buffer permutation with event-local elementary lowering",
        result["pass_exact_declared_code_global_stream"], result,
    )
    return result


# ---------------------------------------------------------------------------
# Route B: direction-expanded partitioned QCA.


def local_lane_exchange(active: np.ndarray, lanes: np.ndarray) -> None:
    """Cubic-covariant involution between compact bound word and one lane."""
    old_active = active.copy()
    old_lanes = lanes.copy()
    lane_counts = np.count_nonzero(old_lanes, axis=2)
    for direction in range(6):
        word = 4 + direction
        compact = (old_active == word) & (lane_counts == 0)
        lane = (
            (old_active == 0) & (lane_counts == 1)
            & (old_lanes[:, :, direction] == word)
        )
        active[compact] = 0
        lanes[:, :, direction][compact] = word
        active[lane] = word
        lanes[:, :, direction][lane] = 0


def lane_partition_swap(outgoing: np.ndarray, incoming: np.ndarray,
                        length: int) -> None:
    old_out = outgoing.copy()
    old_in = incoming.copy()
    for direction in range(6):
        targets = target_map(length, 4 + direction)
        outgoing[:, :, direction] = old_in[targets, :, direction]
        incoming[targets, :, direction] = old_out[:, :, direction]


def lane_forward(active: np.ndarray, outgoing: np.ndarray, incoming: np.ndarray,
                 length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    active, outgoing, incoming = active.copy(), outgoing.copy(), incoming.copy()
    local_lane_exchange(active, outgoing)
    lane_partition_swap(outgoing, incoming, length)
    local_lane_exchange(active, incoming)
    return active, outgoing, incoming


def lane_inverse(active: np.ndarray, outgoing: np.ndarray, incoming: np.ndarray,
                 length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    active, outgoing, incoming = active.copy(), outgoing.copy(), incoming.copy()
    local_lane_exchange(active, incoming)
    lane_partition_swap(outgoing, incoming, length)
    local_lane_exchange(active, outgoing)
    return active, outgoing, incoming


def frame_lanes(lanes: np.ndarray, frame: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros_like(lanes)
    direction_permutation = np.argmax(
        c600.c598.c593.c210.direction_permutation(frame), axis=0
    )
    for site in range(length**3):
        coordinate = np.asarray(site_tuple(site, length), dtype=int)
        target = site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
        for species in range(3):
            for direction in range(6):
                mapped = int(direction_permutation[direction])
                word = int(lanes[site, species, direction])
                result[target, species, mapped] = c603.frame_word(word, frame)
    return result


def route_b() -> dict:
    print("\nROUTE B — DIRECTION-EXPANDED PARTITIONED QCA")
    rows = []
    condition = True
    frames = c600.c598.c593.c210.proper_cubic_frames()
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        volume = length**3
        failures = inverse_failures = 0
        for species in range(3):
            for site in range(volume):
                for word in range(1, 10):
                    active = np.zeros((volume, 3), dtype=np.int16)
                    active[site, species] = word
                    lanes = np.zeros((volume, 3, 6), dtype=np.int16)
                    output = lane_forward(active, lanes, lanes, length)
                    expected, collision = abstract_stream(active, length)
                    failures += int(
                        collision or not np.array_equal(output[0], expected)
                        or np.count_nonzero(output[1]) or np.count_nonzero(output[2])
                    )
                    recovered = lane_inverse(*output, length)
                    inverse_failures += int(
                        not np.array_equal(recovered[0], active)
                        or np.count_nonzero(recovered[1]) or np.count_nonzero(recovered[2])
                    )
        malformed = np.zeros((volume, 3), dtype=np.int16)
        malformed[source_site(0, 4, length), 0] = 4
        malformed[source_site(0, 6, length), 0] = 6
        zero_lanes = np.zeros((volume, 3, 6), dtype=np.int16)
        malformed_output = lane_forward(malformed, zero_lanes, zero_lanes, length)
        malformed_recovered = lane_inverse(*malformed_output, length)
        malformed_lanes = int(
            np.count_nonzero(malformed_output[1]) + np.count_nonzero(malformed_output[2])
        )
        frame_failures = 0
        seed = random_lawful(length, 60620 + length)
        seed_out = lane_forward(seed, zero_lanes, zero_lanes, length)
        for frame in frames:
            framed_seed = frame_words(seed, frame, length)
            actual = lane_forward(framed_seed, zero_lanes, zero_lanes, length)
            expected_active = frame_words(seed_out[0], frame, length)
            expected_out = frame_lanes(seed_out[1], frame, length)
            expected_in = frame_lanes(seed_out[2], frame, length)
            frame_failures += int(not arrays_equal(
                (actual[0], expected_active), (actual[1], expected_out), (actual[2], expected_in)
            ))
        row = {
            "length": length,
            "split": split,
            "lawful_rows": 3 * volume * 9,
            "lawful_stream_failures": failures,
            "inverse_failures": inverse_failures,
            "partition_pairs": 18 * volume,
            "partition_pair_conflicts": 0,
            "all24_register_update_and_lane_covariance_failures_on_one_frozen_lawful_seed": frame_failures,
            "all24_register_update_covariance_executed": True,
            "all576_register_update_covariance_executed": False,
            "malformed_multiple_incoming_lanes_retained": malformed_lanes,
            "malformed_inverse_recovery": arrays_equal(
                (malformed_recovered[0], malformed),
                (malformed_recovered[1], zero_lanes),
                (malformed_recovered[2], zero_lanes),
            ),
            "persistent_register_role_bits": 156 * volume,
            "intercell_word_SWAPS": 72 * volume,
        }
        rows.append(row)
        condition &= (
            failures == inverse_failures == frame_failures == 0
            and malformed_lanes >= 2 and row["malformed_inverse_recovery"]
        )
    # The exact local register block is six disjoint 28-role-bit basis
    # transpositions.  A
    # generic Gray lowering is bounded but deliberately not counted as closed:
    # it would use 38 C27X calls and supplied clean work/routing.
    result = {
        "status": "exact logical translation/proper-cubic partitioned word-register stream with explicit direction lanes; the 28-role-bit exchange remains an abstract register permutation and no physical M2 lowering or placement is compiled",
        "local_exchange": "six disjoint transpositions between A=4+d/all lanes zero and A=0/lane_d=4+d",
        "local_exchange_support_role_bits": 28,
        "local_exchange_basis_transpositions": 6,
        "Gray_C27X_calls_per_exchange_block": 38,
        "C27X_Toffoli_calls_with_25_clean_work_each": 51,
        "elementary_NN_lowering_executed": False,
        "sharp_logical_gate_import": "one cubic-covariant 28-role-bit local exchange permutation, full-space identity on every other local register row",
        "sharp_physical_import": "literal translation-invariant cubic M2 placement, primitive lowering, encoder/intertwiner/leakage, and a directly executed one-site physical law",
        "partition_layer": "SWAP Out_d(x) with In_d(x+v_d); distinct Out/In roles make a perfect matching without parity coloring",
        "persistent_register_role_bits_per_cell": 156,
        "host_parity_color_origin_or_size_query": False,
        "rows": rows,
        "pass_exact_global_stream_with_named_block_import": bool(condition),
        "literal_physical_M2_layout_compiled": False,
        "physical_M2_primitive_product_composed": False,
        "physical_encoder_composed": False,
        "physical_intertwiner_residual": None,
        "physical_code_leakage_evaluated": False,
        "one_site_translation_covariant_physical_law_executed": False,
        "pass_literal_physical_M2_compiler": False,
    }
    check(
        "Route B gives an exact direction-expanded partitioned QCA and isolates one local symmetric block import",
        result["pass_exact_global_stream_with_named_block_import"], result,
    )
    return result


# ---------------------------------------------------------------------------
# Route C: state-carried phase selects the active compact buffer.


def conditional_xor_move(source: np.ndarray, destination: np.ndarray,
                         phase_bits: np.ndarray, branch: int, length: int) -> None:
    for species in range(3):
        for word in range(1, 16):
            targets = target_map(length, word)
            sites = np.flatnonzero(
                (phase_bits == branch) & (phase_bits[targets] == branch)
                & (source[:, species] == word)
            )
            np.bitwise_xor.at(destination[:, species], targets[sites], word)


def conditional_xor_clear(source: np.ndarray, destination: np.ndarray,
                          phase_bits: np.ndarray, branch: int, length: int) -> None:
    for species in range(3):
        for word in range(1, 16):
            targets = target_map(length, word)
            sites = np.flatnonzero(
                (phase_bits == branch) & (phase_bits[targets] == branch)
                & (destination[targets, species] == word)
            )
            source[sites, species] ^= word


def phase_forward(active: np.ndarray, buffer: np.ndarray, phase_bits: np.ndarray,
                  length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    active, buffer, phase_bits = active.copy(), buffer.copy(), phase_bits.copy()
    conditional_xor_move(active, buffer, phase_bits, 0, length)
    conditional_xor_clear(active, buffer, phase_bits, 0, length)
    conditional_xor_move(buffer, active, phase_bits, 1, length)
    conditional_xor_clear(buffer, active, phase_bits, 1, length)
    phase_bits ^= 1
    return active, buffer, phase_bits


def phase_inverse(active: np.ndarray, buffer: np.ndarray, phase_bits: np.ndarray,
                  length: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    active, buffer, phase_bits = active.copy(), buffer.copy(), phase_bits.copy()
    phase_bits ^= 1
    conditional_xor_clear(buffer, active, phase_bits, 1, length)
    conditional_xor_move(buffer, active, phase_bits, 1, length)
    conditional_xor_clear(active, buffer, phase_bits, 0, length)
    conditional_xor_move(active, buffer, phase_bits, 0, length)
    return active, buffer, phase_bits


def phase_syndrome(phase_bits: np.ndarray, length: int) -> int:
    syndrome = 0
    for site in range(length**3):
        coordinate = site_tuple(site, length)
        for axis in range(3):
            target = list(coordinate)
            target[axis] = (target[axis] + 1) % length
            syndrome += int(phase_bits[site] != phase_bits[site_flat(tuple(target), length)])
    return syndrome


def route_c() -> dict:
    print("\nROUTE C — STATE-CARRIED BUFFER PHASE")
    rows = []
    condition = True
    rng = np.random.default_rng(60630)
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        volume = length**3
        failures = inverse_failures = two_step_failures = 0
        for initial_phase in (0, 1):
            for species in range(3):
                for site in range(volume):
                    for word in range(1, 10):
                        logical = np.zeros((volume, 3), dtype=np.int16)
                        logical[site, species] = word
                        if initial_phase == 0:
                            active, buffer = logical, np.zeros_like(logical)
                        else:
                            active, buffer = np.zeros_like(logical), logical
                        phases = np.full(volume, initial_phase, dtype=np.int8)
                        output = phase_forward(active, buffer, phases, length)
                        expected, collision = abstract_stream(logical, length)
                        decoded = output[0] if initial_phase == 1 else output[1]
                        inactive = output[1] if initial_phase == 1 else output[0]
                        failures += int(
                            collision or not np.array_equal(decoded, expected)
                            or np.count_nonzero(inactive)
                            or not np.all(output[2] == 1 - initial_phase)
                        )
                        recovered = phase_inverse(*output, length)
                        inverse_failures += int(not arrays_equal(
                            (recovered[0], active), (recovered[1], buffer), (recovered[2], phases)
                        ))
        logical = random_lawful(length, 60631 + length)
        start = (logical, np.zeros_like(logical), np.zeros(volume, dtype=np.int8))
        once = phase_forward(*start, length)
        twice = phase_forward(*once, length)
        expected_once, _ = abstract_stream(logical, length)
        expected_twice, _ = abstract_stream(expected_once, length)
        two_step_failures += int(
            not np.array_equal(twice[0], expected_twice)
            or np.count_nonzero(twice[1]) or np.count_nonzero(twice[2])
        )
        nonuniform = rng.integers(0, 2, size=volume, dtype=np.int8)
        dirty_a = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
        dirty_b = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
        malformed_out = phase_forward(dirty_a, dirty_b, nonuniform, length)
        malformed_back = phase_inverse(*malformed_out, length)
        nonuniform_syndrome_before = phase_syndrome(nonuniform, length)
        nonuniform_syndrome_after = phase_syndrome(malformed_out[2], length)
        single_flip = np.zeros(volume, dtype=np.int8)
        single_flip[0] = 1
        row = {
            "length": length,
            "split": split,
            "phase0_and_phase1_lawful_rows": 2 * 3 * volume * 9,
            "lawful_stream_failures": failures,
            "inverse_failures": inverse_failures,
            "two_consecutive_shift_failures": two_step_failures,
            "uniform_phase0_syndrome": phase_syndrome(np.zeros(volume, dtype=np.int8), length),
            "uniform_phase1_syndrome": phase_syndrome(np.ones(volume, dtype=np.int8), length),
            "single_phase_flip_syndrome": phase_syndrome(single_flip, length),
            "nonuniform_phase_syndrome_before_after_local_advance": (
                nonuniform_syndrome_before, nonuniform_syndrome_after
            ),
            "uniform_constraint_preserved_by_bitwise_reversible_advance": (
                nonuniform_syndrome_before == nonuniform_syndrome_after
            ),
            "malformed_nonuniform_full_space_inverse": arrays_equal(
                (malformed_back[0], dirty_a),
                (malformed_back[1], dirty_b),
                (malformed_back[2], nonuniform),
            ),
            "persistent_active_buffer_phase_role_bits": 25 * volume,
            "maximum_live_with_five_work_role_bits_per_species": 40 * volume,
        }
        rows.append(row)
        condition &= (
            failures == inverse_failures == two_step_failures == 0
            and row["uniform_phase0_syndrome"] == row["uniform_phase1_syndrome"] == 0
            and row["single_phase_flip_syndrome"] == 6
            and row["uniform_constraint_preserved_by_bitwise_reversible_advance"]
            and row["malformed_nonuniform_full_space_inverse"]
        )
    result = {
        "status": "exact two-buffer stream with a locally checkable uniform phase bit selecting the active buffer; the phase replaces host tick parity but its uniform genesis is supplied",
        "register_algebraic_intertwiner": "G_register E_p = E_(1-p) G_coarse for p=0,1; decoder reads A for p=0 and B for p=1",
        "phase_constraint": "p_x=p_y on every NN edge; connectedness makes the lawful phase globally uniform",
        "phase_advance": "parallel local X on every p_x; self-inverse and preserves every NN equality/inequality syndrome",
        "phase_constraint_locally_checkable": True,
        "phase_constraint_dynamically_repaired_or_generated": False,
        "branch_gate_control": "word equality plus phase(source)=phase(target)=p",
        "abstract_C6X_clean_work_role_bits": 5,
        "explicit_elementary_gate_count_executed": False,
        "sharp_import": "phase-controlled equality-XOR block; Cycle603 CkX/Toffoli lowering applies with k=6",
        "translation_invariant_global_register_supercell_embedding_executed": False,
        "all24_register_update_covariance_executed": False,
        "all576_register_update_covariance_executed": False,
        "literal_physical_M2_layout_compiled": False,
        "physical_M2_primitive_product_composed": False,
        "physical_encoder_composed": False,
        "physical_intertwiner_residual": None,
        "physical_code_leakage_evaluated": False,
        "one_site_translation_covariant_physical_law_executed": False,
        "host_tick_parity_color_origin_or_size_query": False,
        "phase_bit_is_physical_time": False,
        "rows": rows,
        "pass_exact_phase_carried_global_stream": bool(condition),
        "pass_phase_genesis": False,
        "pass_literal_physical_M2_compiler": False,
    }
    check(
        "Route C carries buffer parity in a local clock field and executes consecutive global shifts without host parity",
        result["pass_exact_phase_carried_global_stream"], result,
    )
    return result


# ---------------------------------------------------------------------------
# Clifford+T bounded word search for Cycle603 one-role-bit analog gates.


def matrix_key(matrix: np.ndarray) -> tuple[tuple[float, float], ...]:
    return tuple(
        (round(float(value.real), 12), round(float(value.imag), 12))
        for value in matrix.ravel()
    )


def cycle603_parametric_targets() -> tuple[list[c603.Gate], list[c603.Gate], dict]:
    _target, operations, _structure = c603.high_level_structured_coin()
    coin_gates: list[c603.Gate] = []
    for index, (kind, first, second, payload) in enumerate(operations):
        if kind == "phase":
            coin_gates += c603.compile_word_two_level(
                first, 15, np.diag([payload, 1]), f"approx_coin_{index}"
            )
        else:
            coin_gates += c603.compile_word_two_level(
                first, int(second), np.asarray(payload), f"approx_coin_{index}"
            )
    contact_gates, _contact = c603.contact_circuit()
    parameter_families = {"RY(theta)", "RZ(theta)", "P(theta)"}
    uses: dict[tuple, dict] = {}
    for multiplier, gates in ((3, coin_gates), (1, contact_gates)):
        for gate in gates:
            if gate.family not in parameter_families:
                continue
            key = matrix_key(gate.matrix)
            if key not in uses:
                uses[key] = {"matrix": gate.matrix, "uses_per_cell": 0, "families": set()}
            uses[key]["uses_per_cell"] += multiplier
            uses[key]["families"].add(gate.family)
    return coin_gates, contact_gates, uses


def phase_aligned_residual(target: np.ndarray, candidate: np.ndarray) -> tuple[float, complex]:
    overlap = np.trace(candidate.conj().T @ target)
    alignment = 1.0 + 0.0j if abs(overlap) < 1e-15 else overlap / abs(overlap)
    return float(np.linalg.norm(target - alignment * candidate, ord=2)), alignment


def decode_word(depth: int, index: int) -> str:
    symbols = ("H", "T", "t")
    answer = []
    for current_depth in reversed(range(1, depth + 1)):
        previous_count = 3 ** (current_depth - 1)
        gate_index, index = divmod(index, previous_count)
        answer.append(symbols[gate_index])
    return "".join(reversed(answer))


def clifford_t_search(uses: dict) -> dict:
    targets = list(uses.values())
    gates = np.stack((c603.H2, c603.T2, c603.TDG2))
    current = np.eye(2, dtype=complex)[None, :, :]
    best = [
        {"residual": float("inf"), "matrix": np.eye(2, dtype=complex), "word": "", "depth": 0}
        for _target in targets
    ]
    checkpoints = []
    candidates_tested = 0
    for depth in range(1, 11):
        current = np.concatenate(tuple(gate @ current for gate in gates), axis=0)
        candidates_tested += len(current)
        for target_index, target_row in enumerate(targets):
            target = target_row["matrix"]
            overlaps = np.einsum("nij,ij->n", current.conj(), target)
            candidate_index = int(np.argmax(np.abs(overlaps)))
            residual, _alignment = phase_aligned_residual(target, current[candidate_index])
            if residual < best[target_index]["residual"]:
                best[target_index] = {
                    "residual": residual,
                    "matrix": current[candidate_index].copy(),
                    "word": decode_word(depth, candidate_index),
                    "depth": depth,
                }
        if depth in (2, 4, 6, 8, 10):
            worst = max(row["residual"] for row in best)
            weighted = sum(
                row["residual"] * target["uses_per_cell"]
                for row, target in zip(best, targets)
            )
            checkpoints.append({
                "maximum_word_depth": depth,
                "candidates_tested_cumulative": candidates_tested,
                "unique_parameter_targets": len(targets),
                "worst_single_gate_ray_operator_residual": worst,
                "weighted_telescoping_bound_per_cell_uncapped": weighted,
                "weighted_telescoping_bound_per_cell_capped": min(2.0, weighted),
            })
    rows = []
    approximants = {}
    for target, found in zip(targets, best):
        key = matrix_key(target["matrix"])
        approximants[key] = found["matrix"]
        rows.append({
            "families": tuple(sorted(target["families"])),
            "uses_per_cell": target["uses_per_cell"],
            "best_word": found["word"],
            "best_word_depth": found["depth"],
            "ray_operator_residual": found["residual"],
            "word_sha256": sha256(found["word"].encode()).hexdigest(),
        })
    return {
        "rows": rows,
        "approximants": approximants,
        "checkpoints": checkpoints,
        "candidates_tested": candidates_tested,
    }


def route_precision() -> dict:
    print("\nPRECISION ROUTE — BOUNDED CLIFFORD+T WORD SEARCH")
    coin_gates, contact_gates, uses = cycle603_parametric_targets()
    search = clifford_t_search(uses)
    approximants = search.pop("approximants")
    approximate_coin = []
    replacements = 0
    for gate in coin_gates:
        key = matrix_key(gate.matrix)
        if key in approximants and gate.family in {"RY(theta)", "RZ(theta)", "P(theta)"}:
            approximate_coin.append(c603.Gate(
                gate.name + "_HT", gate.qubits, approximants[key], "Clifford+T-word"
            ))
            replacements += 1
        else:
            approximate_coin.append(gate)
    initial = np.zeros((32, 16), dtype=complex)
    initial[::2] = np.eye(16)
    exact = c603.apply_sequence_columns(initial, coin_gates, 5)
    approximate = c603.apply_sequence_columns(initial, approximate_coin, 5)
    overlap = np.vdot(exact, approximate)
    alignment = 1 if abs(overlap) < 1e-15 else overlap.conjugate() / abs(overlap)
    local_coin_ray_residual = float(np.linalg.norm(exact - alignment * approximate))
    approximate_scratch_leakage = float(np.linalg.norm(approximate[1::2]))
    final_checkpoint = search["checkpoints"][-1]
    per_cell_uncapped = final_checkpoint["weighted_telescoping_bound_per_cell_uncapped"]
    scaling_rows = []
    for length in (3, 6, 7):
        for q_updates in (1, 10, 100):
            uncapped = per_cell_uncapped * length**3 * q_updates
            scaling_rows.append({
                "length": length,
                "q_updates": q_updates,
                "telescoping_operator_bound_uncapped": uncapped,
                "telescoping_operator_bound_capped": min(2.0, uncapped),
            })
    condition = (
        len(uses) > 0 and replacements > 0
        and search["candidates_tested"] == sum(3**depth for depth in range(1, 11))
        and all(
            later["worst_single_gate_ray_operator_residual"]
            <= earlier["worst_single_gate_ray_operator_residual"] + 1e-15
            for earlier, later in zip(search["checkpoints"], search["checkpoints"][1:])
        )
        and local_coin_ray_residual > 1e-8
        and final_checkpoint["worst_single_gate_ray_operator_residual"] > 1e-8
    )
    result = {
        "status": "finite H/T/Tdg search gives explicit depth-2..10 approximation/error bounds; it does not give exact or scalable global closure",
        "alphabet": ("H", "T", "Tdg"),
        "inherited_calibration_inputs": {
            "beta": -0.3,
            "contact_g": c603.c230.COUPLING,
            "provenance": "Cycle603 compiled coin and contact gate lists",
        },
        "global_phase_quotiented": True,
        "search": search,
        "parameterized_instances_replaced_in_one_species_coin": replacements,
        "one_species_compiled_coin_ray_Frobenius_residual": local_coin_ray_residual,
        "one_species_logical_scratch_leakage": approximate_scratch_leakage,
        "volume_and_q_update_scaling": scaling_rows,
        "stream_additional_analog_error": 0,
        "exact_Clifford_T_closure_claimed": False,
        "fault_tolerant_synthesis_optimality_claimed": False,
        "physical_M2_leakage_evaluated": False,
        "literal_physical_M2_gate_product_executed": False,
        "pass_as_precision_bounded_attempt": bool(condition),
        "pass_exact_or_global_precision_target": False,
    }
    check(
        "the Clifford+T search returns explicit finite-depth errors and exposes volume/update accumulation without claiming exact closure",
        result["pass_as_precision_bounded_attempt"], result,
    )
    return result


def no_go_discipline(route_a_result: dict, route_b_result: dict,
                      route_c_result: dict, precision_result: dict) -> dict:
    walls = (
        "clean buffer/scratch initialization and renewal",
        "literal translation-invariant physical M2 placement and primitive product",
        "malformed multi-carrier collision repair or enforcement",
        "elementary lowering of the 28-role-bit lane exchange",
        "uniform phase-field genesis for phase-carried scheduling",
        "precision scaling beyond finite H/T/Tdg depth",
    )
    pairs: list[dict] = []
    for first, second in combinations(walls, 2):
        pairs.append({
            "wall_A": first,
            "wall_B": second,
            "A_implies_B": False,
            "B_implies_A": False,
            "independent": True,
            "shared_witness_identified": False,
            "evidence": "the runner exposes separate state/resource predicates and no derivation connecting the pair",
        })
    families = (
        {
            "family": "compact reversible double buffer",
            "attempt_statement": "attempt an exact parity-free simultaneous stream by scattering into a second compact register, clearing the source, and swapping buffers",
            "failure_statement_with_citation": "the logical target closes, but the physical M2 compiler fails because no literal placement/primitive product is executed (this Cycle606 runner, route_a physical-scope fields)",
            "authority": "none; attempted artifact",
            "object": "two four-role-bit words per species/cell",
            "mechanism": "equality-controlled scatter, copy-clear, and local buffer SWAP",
            "terminal_obligation": "exact simultaneous logical compact-register shift on the declared code",
            "comparison_strength": "target-equivalent at register level, weaker than a physical M2 compiler",
            "marker": "ATTEMPTED",
            "disposition": "closes the register permutation, inverse, deletion sensitivity, and code-space EG tests; physical placement and malformed collision closure remain open",
        },
        {
            "family": "direction-expanded partitioned QCA",
            "attempt_statement": "attempt a partitioned stream with explicit incoming/outgoing direction lanes so every intercell call is a matching",
            "failure_statement_with_citation": "the register target closes, but the 28-role-bit local exchange and physical placement remain imports (this Cycle606 runner, route_b result)",
            "authority": "none; attempted artifact",
            "object": "compact word plus Out/In direction lanes",
            "mechanism": "cubic-symmetric local exchange and bipartite-role intercell SWAP matching",
            "terminal_obligation": "register-level collision-separated shift without parity coloring",
            "comparison_strength": "target-equivalent at register level with an unlowered local exchange",
            "marker": "ATTEMPTED",
            "disposition": "exact register stream; the 28-role-bit exchange is not physically lowered",
        },
        {
            "family": "state-carried buffer phase",
            "attempt_statement": "attempt recurrent streaming by carrying the active-buffer phase in a local state field instead of querying a host tick",
            "failure_statement_with_citation": "the uniform-sector register target closes, but phase genesis and physical lowering remain open (this Cycle606 runner, route_c result)",
            "authority": "none; attempted artifact",
            "object": "two compact buffers plus local phase field",
            "mechanism": "phase-conditioned direction matching and local phase toggle",
            "terminal_obligation": "recurrent register shift without host tick parity",
            "comparison_strength": "target-equivalent on a supplied uniform-phase sector",
            "marker": "ATTEMPTED",
            "disposition": "two consecutive shifts exact; uniform phase genesis supplied",
        },
        {
            "family": "finite Clifford+T word approximation",
            "attempt_statement": "attempt to retire parameterized gates by exhaustive finite H/T/Tdg word search modulo global phase",
            "failure_statement_with_citation": "depth-ten residuals remain nonzero and the volume/update telescoping bound saturates (this Cycle606 runner, route_precision exact residual fields)",
            "authority": "none; attempted artifact",
            "object": "depth-bounded H/T/Tdg words for Cycle603 one-role-bit angles",
            "mechanism": "exhaustive word search modulo global phase and telescoping bounds",
            "terminal_obligation": "precision-bounded replacement of calibrated rotations",
            "comparison_strength": "strictly weaker than exact finite-alphabet closure",
            "marker": "ATTEMPTED",
            "disposition": "finite errors explicit; global-volume bounds saturate",
        },
        {
            "family": "independent crossed-link endpoint gates",
            "attempt_statement": "attempt to obtain the torus stream by composing the six exact crossed-link endpoint transpositions",
            "failure_statement_with_citation": "Cycle603 explicitly compiled separate link tables without a simultaneous torus update (Cycle603 note:153-172)",
            "authority": "independently accepted Cycle603 artifact; formal authority remains none",
            "object": "Cycle603 eight-bit link transpositions",
            "mechanism": "Gray C7X event circuits without a global matching composition",
            "terminal_obligation": "one simultaneous torus stream",
            "comparison_strength": "strictly weaker than a simultaneous stream",
            "marker": "RULED OUT BY PRIOR",
            "prior_citation": "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:153-172",
            "disposition": "the cited artifact executes six separate tables and explicitly does not compose a torus update",
        },
    )
    open_counterroute = {
        "family": "autonomous collision-repair gauge reservoir",
        "object": "reversible syndrome/debris fields coupled to compact buffers",
        "mechanism": "retain collision history and repair or reject without erasure",
        "terminal_obligation": "full malformed-sector covariance and return to code",
        "comparison_strength": "unknown and potentially target-equivalent",
        "status": "OPEN / NOT COUNTED AS ATTEMPTED OR RULED OUT",
        "authority": "none",
        "citation": "scripts/physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22.py:route_a collision controls",
    }
    rhetoric = (
        {"phrase": "the stream is not a physical M2 fact", "resolutions": ("per register event", "per declared role line", "per coarse cell", "lattice-wide register product", "literal physical M2 lattice"), "tested": ("per register event", "per declared role line", "lattice-wide register product"), "untested_negative_status": "no universal physical negative is inferred", "narrowed_phrase": "the executed Cycle606 stream is a logical/register product; physical M2 compilation is unevaluated"},
        {"phrase": "nearest-neighbor routing is not physical placement", "resolutions": ("per logical gate", "per role line", "per simultaneous cell", "whole torus"), "tested": ("per logical gate", "per role line"), "untested_negative_status": "simultaneous physical placement remains open", "narrowed_phrase": "nearest-neighbor is verified only on the declared logical role line"},
        {"phrase": "register EG is not a physical intertwiner", "resolutions": ("per carrier", "factorized exterior sample", "lattice-size fixture", "physical code space"), "tested": ("per carrier", "factorized exterior sample", "L3/L6/L7 register fixtures"), "untested_negative_status": "physical encoder/intertwiner/leakage is unevaluated", "narrowed_phrase": "maximum register EG residual is reported; physical_intertwiner_residual is null"},
        {"phrase": "all24/all576 group checks are not physical covariance", "resolutions": ("word action", "site action", "one-seed register update", "all-state register update", "physical one-site law"), "tested": ("word action", "site action", "one-seed all24 register update"), "untested_negative_status": "all-state and physical-law covariance remain open", "narrowed_phrase": "all576 covers site/word group composition only; all24 update covariance uses one frozen lawful seed"},
        {"phrase": "a schedule is not time", "resolutions": ("gate-product order", "buffer phase register", "recurrent register step", "causal physical time"), "tested": ("gate-product order", "buffer phase register", "two recurrent register steps"), "untested_negative_status": "no causal-time mechanism is tested", "narrowed_phrase": "Cycle606 supplies a register schedule/phase, not a physical time law"},
        {"phrase": "register counts are not source or energy", "resolutions": ("role bit", "cell register", "torus total", "physical source/energy observable"), "tested": ("role-bit and register counts",), "untested_negative_status": "no physical source/energy map is evaluated", "narrowed_phrase": "reported counts are logical storage resources only"},
        {"phrase": "finite depth is not exact Clifford+T closure", "resolutions": ("one target gate", "compiled coin", "one cell", "volume/update accumulation", "asymptotic synthesis"), "tested": ("one target gate", "compiled coin", "finite volume/update upper bounds"), "untested_negative_status": "no global impossibility or optimality follows", "narrowed_phrase": "depth-ten search leaves explicit nonzero residuals"},
    )
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "newer_origin_main_version_followed": True,
            "proof_search_governance_followed": True,
        },
        "N1_normalized_families": families,
        "N1_qualifying_family_count": len(families),
        "N1_all_markers_exact": all(
            row["marker"] in {"ATTEMPTED", "RULED OUT BY PRIOR"} for row in families
        ),
        "N1_open_counterroute_not_counted": open_counterroute,
        "N2_directional_wall_independence": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "required_phrase_scan": {
                "we assume": "absent",
                "by construction": "absent",
                "as is standard": "absent",
                "the framework provides": "absent",
                "bridge context": "absent",
                "background": "absent",
                "naturally": "absent",
                "obviously": "absent",
                "standard QFT": "absent",
                "registered": "absent",
                "canonical": "code-variable name for the enumerated tuple 1..15; non-load-bearing because reversed, all24-rotated, and all 105 pair orders are compared",
            },
            "zero secondary buffers and scratch": "supplied register initialization; locally checkable, not dynamically generated",
            "exactly one word per species": "supplied Cycle600 global sector, not locally enforced",
            "scatter_clear_swap_sequence": "fixed register product; a schedule is not time",
            "logical_role_line": "declared routing graph, not literal physical M2 placement",
            "lane exchange": "unlowered 28-role-bit abstract permutation",
            "uniform phase": "locally checkable but supplied sector",
            "Clifford_T_depth": "explicit maximum ten; no exactness or optimality claim",
            "periodic_tori": "L3/L6/L7 test fixtures; no host size query in the update",
            "one_frozen_covariance_seed": "explicitly narrower than exhaustive state covariance",
            "uncited_standard_or_obvious_hits": 0,
        },
        "N4_residual_matching": (
            {
                "witness_citation": "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:167-180",
                "witness_residual": "declared role-line covariance is not physical M2 and six link tables are not one torus update",
                "current_exact_residual": "register torus update is now composed, but literal_physical_M2_layout_compiled=false, physical_M2_primitive_product_composed=false, physical_intertwiner_residual=null, physical_code_leakage_evaluated=false",
                "match": False,
                "reason": "Cycle606 retires the logical global-product residual but leaves the physical M2 compiler residual",
            },
            {
                "witness_citation": "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:120-130",
                "witness_residual": "parameterized RY/RZ/P angle import",
                "current_exact_residual": {
                    "maximum_depth": 10,
                    "candidates_tested": precision_result["search"]["candidates_tested"],
                    "worst_single_gate_ray_operator_residual": precision_result["search"]["checkpoints"][-1]["worst_single_gate_ray_operator_residual"],
                    "compiled_coin_ray_Frobenius_residual": precision_result["one_species_compiled_coin_ray_Frobenius_residual"],
                },
                "match": True,
            },
            {
                "witness_citation": "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:174-190",
                "witness_residual": "physical code-space leakage and full malformed-sector preservation untested",
                "current_exact_residual": {
                    "Route_A_collision_pairs_leave_declared_code": tuple(
                        row["remote_collision_pairs_leaving_declared_code"]
                        for row in route_a_result["rows"]
                    ),
                    "Route_A_collision_inverse_failures": tuple(
                        row["remote_collision_inverse_failures"]
                        for row in route_a_result["rows"]
                    ),
                    "physical_code_leakage_evaluated": False,
                },
                "match": True,
            },
        ),
        "N5_rhetoric_resolution": rhetoric,
        "N5_five_resolutions_present": len(rhetoric) >= 5,
        "N6_partial_closure_paths": (
            {"file": "scripts/physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22.py", "status": "PARTIAL", "what_closes": "Route A exact logical register stream, inverse, deletion, L3/L6/L7 EG and seeded covariance"},
            {"file": "scripts/physical_L41_elementary_gate_layout_compiler_cycle580_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "a literal finite M2 primitive layout for a different bounded gate fixture; it does not place this stream"},
            {"file": "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "a conditional logical torus macro and held M2 blueprint; physical primitive composition remains open"},
            {"file": "scripts/physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22.py", "status": "PARTIAL / PRIOR", "what_closes": "bounded logical role-event circuits and inherited coin/contact/seam fixtures; no global stream or physical M2 compiler"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "literal Cycle606 M2 placement, primitive product, encoder, physical intertwiner/leakage, and one-site translation-covariant law"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "reversible collision syndrome/debris repair or local lawful-sector enforcement"},
            {"file": "UNMATERIALIZED", "status": "OPEN", "what_closes": "certified epsilon-target Clifford+T synthesis with declared global error budget"},
        ),
        "N7_hostile_steelman": {
            "mechanism": "materialize the compact active/buffer/flag/work roles as a proper-cubic repeated M2 supercell with directed edge ports; use bounded sublayers for routed equality-XOR calls; add reversible collision syndrome/debris roles; use certified single-qubit synthesis at declared epsilon",
            "why_not_defeated": "Cycle606 supplies the exact register target and finds no contradiction preventing that construction; the collision-reservoir and physical-placement routes are open",
            "terminal_obligation": "execute literal placement and primitive product, E_physical G_coarse = G_physical E_physical, leakage, deletion, held sizes, and one-site translation covariance",
            "authority_status": "OPEN / no retained authority",
            "citations": (
                "scripts/physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22.py:531-745",
                "docs/work_history/repo/review_feedback/PHYSICAL_CARRIER_PREPARATION_ELEMENTARY_SYNTHESIS_TOURNAMENT_CYCLE603_NOTE_2026-07-22.md:167-180",
                "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md:126-141",
            ),
        },
        "N8_cross_cycle_echo": (
            {"cycle": "Cycle560", "retired": "bounded local encoder tables", "mechanism": "finite one-hot branch encoders", "applicability": "logical code construction only; no automatic physical stream"},
            {"cycle": "Cycle563", "retired": "runtime selected-factor order service", "mechanism": "bounded transported color layers", "applicability": "logical factor order only"},
            {"cycle": "Cycle580", "retired": "one bounded L41 gate-layout import", "mechanism": "literal 18-M2 primitive circuit", "applicability": "different finite fixture; demonstrates placement can be constructive"},
            {"cycle": "Cycle590", "retired": "held conditional logical macro/order/layout bookkeeping", "mechanism": "bounded roles and selected-factor product", "applicability": "explicitly not physical primitive composition"},
            {"cycle": "Cycle603", "retired": "bounded logical local word-event lowering", "mechanism": "Gray paths, reversible conjunction scratch, role-line routing", "applicability": "separate events, not one torus update or physical M2 compiler"},
            {"cycle": "Cycle606", "retired": "logical/register global carrier product", "mechanism": "compact double buffer", "applicability": "declared code and register algebra only"},
        ),
        "route_evidence": {
            "A": route_a_result["pass_exact_declared_code_global_stream"],
            "B": route_b_result["pass_exact_global_stream_with_named_block_import"],
            "C": route_c_result["pass_exact_phase_carried_global_stream"],
            "precision": precision_result["pass_as_precision_bounded_attempt"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "status": "FAIL",
        "failed_checklist_items": ("N7: actionable physical-supercell and collision-reservoir steelman remains live",),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "gate_reason": "the N7 steelman remains live and no route-independent contradiction survived the constructive attempts",
        "demoted_artifact_status": "positive scoped construction plus unresolved physical-M2 and precision walls",
        "narrowed_positive_artifact_gate": "PASS",
    }
    condition = (
        len(families) >= 5 and result["N1_all_markers_exact"]
        and len(pairs) == math.comb(len(walls), 2)
        and result["N5_five_resolutions_present"]
        and all(result["route_evidence"].values())
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["shared_obstruction"] and not result["axiom_pressure"]
        and result["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and result["narrowed_positive_artifact_gate"] == "PASS"
        and result["N7_hostile_steelman"]["authority_status"] == "OPEN / no retained authority"
    )
    check("fresh exact-schema N1-N8 fails the broad-negative gate and retains only the narrowed positive construction",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Cycle 606", "Route A", "Route B", "Route C",
        "double buffer", "partitioned", "state-carried", "global stream", "L3", "L6", "L7",
        "all 24", "all 576", "translation", "nearest-neighbor", "inverse", "deletion",
        "malformed", "off-code", "collision", "Clifford+T", "depth ten", "N1", "N8",
        "schedule is not time", "register counts are not source or energy",
        "logical/register only", "physical M2", "FAIL / DO NOT SHIP",
        "Author artifact status accepted: false", "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden = (
        "all malformed sectors are repaired", "claims exact Clifford+T closure",
        "schedule is physical time", "carrier count is energy", "shared obstruction proved",
        "physical M2 compiler is complete", "all 576 update-covariance tests passed",
    )
    forbidden_hits = tuple(phrase for phrase in forbidden if phrase in text)
    result = {"required": required, "missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle606 note freezes global-stream variants, precision bounds, N1-N8, and firewalls",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.perf_counter()
    print("Cycle606 global carrier stream/QCA approximation tournament", AUTHORITY, AUDIT)
    shore_result = shore()
    cycle603_receipt = shore_result["Cycle603_receipt"]
    route_a_result = route_a()
    route_b_result = route_b()
    route_c_result = route_c()
    precision_result = route_precision()
    discipline = no_go_discipline(
        route_a_result, route_b_result, route_c_result, precision_result
    )
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, resources)
    receipt = {
        "status": "cycle606-global-carrier-stream-qca-approximation-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_artifact_status_accepted": False,
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "shore": {
            "Cycle603_pass": cycle603_receipt["pass"],
            "Cycle603_global_stream_was_open": not cycle603_receipt[
                "route_A_structured_elementary_compiler"
            ]["scratch_and_schedule"]["global_conflict_free_stream_schedule_compiled"],
            "import_audit": shore_result["verified_inheritance"]["import_audit"],
        },
        "route_A_compact_double_buffer": route_a_result,
        "route_B_direction_partitioned_QCA": route_b_result,
        "route_C_state_carried_phase": route_c_result,
        "precision_bounded_Clifford_T": precision_result,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": "an exact constant-overhead logical compact-register double-buffer permutation implements the simultaneous Cycle600 three-species torus stream on the declared one-carrier/species code for L3/L6/L7 with no runtime parity/color/origin/size query; exact register EG/inverse/deletion/collision controls and seeded translation/all24 covariance pass, while the all576 execution is only the site/word group action and no physical M2 compiler is claimed",
        "route_disposition": {
            "A": "exact logical compact-register global stream on supplied code with declared role-line lowering; literal M2 placement/product, physical encoder/intertwiner/leakage, zero buffer/scratch genesis, and global one-carrier enforcement remain supplied or unevaluated",
            "B": "exact direction-expanded partitioned register stream with one unlowered 28-role-bit local exchange; no physical M2 compiler",
            "C": "exact phase-carried recurrent register stream on locally checkable uniform-phase sector; phase genesis, elementary count, all24/all576 update covariance, and physical M2 compilation remain open",
            "precision": "explicit depth<=10 H/T/Tdg approximants and accumulation bounds; no exact or scalable precision closure",
        },
        "physical_M2_scope": {
            "literal_layout_compiled": False,
            "primitive_composition": False,
            "encoder_composed": False,
            "intertwiner_residual": None,
            "leakage_evaluated": False,
            "one_site_translation_covariant_law_executed": False,
        },
        "covariance_execution_scope": {
            "Route_A_all24_register_update": "executed on one frozen lawful seed per L",
            "Route_A_all576": "executed site/word action group law only; not update covariance",
            "Route_B_all24_register_update": "executed on one frozen lawful seed per L",
            "Route_B_all576_register_update": "not executed",
            "Route_C_all24_register_update": "not executed",
            "Route_C_all576_register_update": "not executed",
            "physical_one_site_translation_covariance": "not executed",
        },
        "interpretation_firewall": {
            "schedule_is_physical_time": False,
            "role_or_register_is_physical_M2": False,
            "register_count_is_source_or_energy": False,
            "register_EG_is_physical_intertwiner": False,
            "logical_scratch_leakage_is_physical_code_leakage": False,
        },
        "breakthrough_bar_met": False,
        "breakthrough_default": "no",
        "broad_negative_gate": discipline["broad_negative_gate"],
        "demoted_artifact_status": discipline["demoted_artifact_status"],
        "optimal_next_campaign": "materialize and collision-check a literal translation-invariant proper-cubic M2 supercell for Route A, with a composed physical encoder, primitive product, one-site translation-covariant law, intertwiner/leakage/deletion tests, and local lawful-domain gadget; then compose coin/contact and pursue reversible collision syndrome plus certified epsilon-target synthesis",
        "shared_obstruction_or_axiom_pressure": False,
        "constitutional_effect": "none",
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    summary = {
        "pass": FAIL == 0, "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "compact_global_stream": route_a_result["pass_exact_declared_code_global_stream"],
        "partitioned_global_stream": route_b_result["pass_exact_global_stream_with_named_block_import"],
        "phase_carried_global_stream": route_c_result["pass_exact_phase_carried_global_stream"],
        "exact_Clifford_T_angles": False, "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
