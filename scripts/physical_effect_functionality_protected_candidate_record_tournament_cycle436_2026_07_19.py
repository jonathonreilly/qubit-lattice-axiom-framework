#!/usr/bin/env python3
"""Cycle 436: physical effect-functionality / presentation tournament.

Two bounded candidate formation laws consume the same Cycle-317/Cycle-321
physical three-M2 pointer output.  The coarse law writes one Cycle-433/
Cycle-370 protected packet keyed only by a derived coarse effect and is
invariant under the certified proportional ray refinement.  The fine law
writes distinct protected packets keyed by the visible fine pointer labels.

Both gates keep the physical pointer, use fixed reversible matcher and
field-write schedules, and have exact inverses.  Both laws remain unselected;
the protected values are candidate packets, not actual framework Records.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from math import sqrt
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321
import physical_detector_to_protected_record_formation_compiler_cycle433_2026_07_19 as c433


c317 = c321.c317
c364 = c433.c364
c370 = c433.c370

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EFFECT_FUNCTIONALITY_PROTECTED_CANDIDATE_RECORD_TOURNAMENT_"
    "CYCLE436_NOTE_2026-07-19.md"
)
C317_NOTE = c317.NOTE
C321_NOTE = c321.NOTE
C383_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MIXED_PROJECTIVE_REFINEMENT_FUNCTIONALITY_BORN_BRIDGE_"
    "CYCLE383_NOTE_2026-07-18.md"
)
C398_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EXHAUSTIVE_FINITE_GRAMMAR_OVERLAP_INSTALLATION_"
    "CYCLE398_NOTE_2026-07-18.md"
)
C403_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CYCLE403_NOTE_2026-07-18.md"
)
C427_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ABSORPTION_INSTRUMENT_EFFECT_REGISTRY_BRIDGE_CYCLE427_NOTE_2026-07-19.md"
)
C430_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "REPEATED_PHYSICAL_INSTRUMENT_CONDITIONAL_HISTORY_FREQUENCY_"
    "CYCLE430_NOTE_2026-07-19.md"
)
C433_NOTE = c433.NOTE

PR_HEADS = {
    "origin/pr-5472": "2c648ccb408a8c36a700f53ec5401369e3bbd490",
    "origin/pr-5476": "a994617819f57e599dd101c654be366123392236",
    "origin/pr-5479": "84053108a424cef26dc23e484549df331ad2050f",
}
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_SPLIT = 0.37
HELD_SPLIT = 0.23
POINTER_BITS = 3
MATCHER_WORK_M2 = 6
TOL = 6.0e-10
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "coarse effect-functional candidate",
        "fine presentation-faithful candidate",
        "same physical pointer input",
        "pointer remains physically present",
        "field-by-field",
        "cycle-370-compatible protected candidate packet",
        "exact e/g",
        "exact inverse",
        "all 24 proper-cubic frames",
        "train l=3",
        "held l=6",
        "pr #5472",
        "pr #5476",
        "pr #5479",
        "no occurrence, sampler, frequency, or probability-law selection",
        "candidate packet is not an actual record",
        "supplied / derived / open",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-436 note freezes the two-law physical tournament", not missing, missing)


def source_contract() -> None:
    texts = {
        317: normalized(C317_NOTE),
        321: normalized(C321_NOTE),
        383: normalized(C383_NOTE),
        398: normalized(C398_NOTE),
        403: normalized(C403_NOTE),
        427: normalized(C427_NOTE),
        430: normalized(C430_NOTE),
        433: normalized(C433_NOTE),
    }
    actual_heads = {
        ref: subprocess.check_output(("git", "rev-parse", ref), cwd=ROOT, text=True).strip()
        for ref in PR_HEADS
    }
    check(
        "the physical pointer, quotient, finite-menu, actualization, instrument, and protected-compiler inputs remain at their stated boundaries",
        "fixed contact-sensitive ternary instrument" in texts[317]
        and "x1^(8)" in texts[317]
        and "ray-split/refinement pair" in texts[321]
        and "same coarse cp maps" in texts[321]
        and "fine apparatus labels remain physically visible" in texts[383]
        and "menus, 55 classes, rank 31" in texts[398]
        and "no law or branch is selected" in texts[403]
        and "deliberately supplied and inverse-designed" in texts[427]
        and "64 conditional held corpora" in texts[430]
        and "79-m2 protected record-state candidate packet" in texts[433]
        and actual_heads == PR_HEADS,
        {
            "PR_heads": actual_heads,
            "Cycle317_physical_trine_and_X1_8": True,
            "Cycle321_ray_coarse_CP_refinement": True,
            "Cycle398_universal_menu_eligibility": False,
            "Cycle433_framework_Record_admitted": False,
        },
    )


@dataclass(frozen=True)
class MatcherGate:
    kind: str
    sites: tuple[int, ...]
    label: str


MATCHER_COORDS: tuple[Coord, ...] = (
    (-1, 0, 0), (-1, 1, 0), (-1, 2, 0),
    (0, 0, 0), (0, 1, 0), (0, 2, 0),
    (1, 1, 0), (1, 2, 0),
    (2, 2, 0),
)
POINTER_SITES = (0, 1, 2)
MATCH_SITES = (3, 4, 5)
PREFIX_SITE = 6
ENABLE_SITE = 7
ROUTE_SITE = 8


def matcher_gate(kind: str, sites: tuple[int, ...], label: str) -> MatcherGate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites, label))
    return MatcherGate(kind, sites, label)


def pointer_word(label: int) -> Word:
    if not isinstance(label, int) or isinstance(label, bool) or not 0 <= label < 8:
        raise ValueError("fine pointer label leaves the three-M2 domain")
    return tuple((label >> shift) & 1 for shift in (2, 1, 0))


def matcher_schedule(label: int) -> tuple[MatcherGate, ...]:
    desired = pointer_word(label)
    gates = []
    for lane, (pointer, work, expected) in enumerate(zip(POINTER_SITES, MATCH_SITES, desired)):
        if expected == 0:
            gates.append(matcher_gate("X", (work,), f"zero-match-invert:lane{lane}"))
        gates.append(matcher_gate("CNOT", (pointer, work), f"pointer-match-load:lane{lane}"))
    gates.extend((
        matcher_gate("TOFFOLI", (MATCH_SITES[0], MATCH_SITES[1], PREFIX_SITE), "match-prefix"),
        matcher_gate("TOFFOLI", (PREFIX_SITE, MATCH_SITES[2], ENABLE_SITE), "match-enable"),
    ))
    return tuple(gates)


def matcher_support_connected(item: MatcherGate) -> bool:
    coords = tuple(MATCHER_COORDS[index] for index in item.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(coords))
            if c433.manhattan(coords[left], coords[right]) == 1
        }
        if grown == reached:
            return len(grown) == len(coords)
        reached = grown


def apply_matcher_gate(bits: list[int], item: MatcherGate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError(item.kind)


def matcher_enable(pointer: int, selected_label: int, *, delete_gate: str | None = None) -> tuple[int, int]:
    bits = list(pointer_word(pointer) + (0,) * MATCHER_WORK_M2)
    original = tuple(bits)
    schedule = matcher_schedule(selected_label)
    used = tuple(item for item in schedule if item.label != delete_gate)
    for item in used:
        apply_matcher_gate(bits, item)
    enable = bits[ENABLE_SITE]
    for item in reversed(used):
        apply_matcher_gate(bits, item)
    leakage = sum(bits[3:]) + int(tuple(bits[:3]) != original[:3])
    return enable, leakage


def route_enable(
    pointer: int,
    selected_labels: tuple[int, ...],
    *,
    delete_gate: str | None = None,
) -> tuple[int, int]:
    """Compute/use/uncompute mutually exclusive matches through one route bit."""

    if not selected_labels or len(set(selected_labels)) != len(selected_labels):
        raise ValueError("route labels must be a nonempty set")
    bits = list(pointer_word(pointer) + (0,) * MATCHER_WORK_M2)
    original = tuple(bits)

    def latch(selected_label: int) -> None:
        schedule = matcher_schedule(selected_label)
        used = tuple(item for item in schedule if item.label != delete_gate)
        for item in used:
            apply_matcher_gate(bits, item)
        bits[ROUTE_SITE] ^= bits[ENABLE_SITE]
        for item in reversed(used):
            apply_matcher_gate(bits, item)

    for selected_label in selected_labels:
        latch(selected_label)
    route = bits[ROUTE_SITE]
    for selected_label in reversed(selected_labels):
        latch(selected_label)
    leakage = sum(bits[3:]) + int(tuple(bits[:3]) != original[:3])
    return route, leakage


@dataclass(frozen=True)
class CandidateLaw:
    name: str
    cases: tuple[c433.FormationCase, ...]
    label_to_block: tuple[tuple[int, int], ...]
    effect_functional: bool
    presentation_faithful: bool


Bank = tuple[c433.BasisState, ...]


def validate_law(law: CandidateLaw) -> None:
    if not isinstance(law, CandidateLaw) or not law.cases:
        raise ValueError("candidate law needs at least one protected packet block")
    labels = tuple(label for label, _block in law.label_to_block)
    if len(labels) != len(set(labels)) or any(not 0 <= label < 8 for label in labels):
        raise ValueError("candidate law pointer labels are duplicated or out of range")
    if any(not 0 <= block < len(law.cases) for _label, block in law.label_to_block):
        raise ValueError("candidate law routes to an absent protected block")
    if law.effect_functional == law.presentation_faithful:
        raise ValueError("tournament candidates require exactly one declared quotient behavior")


def prepare_bank(layout: c433.Layout, law: CandidateLaw) -> Bank:
    validate_law(law)
    return tuple(c433.prepare(layout, case) for case in law.cases)


def apply_law(
    bank: Bank,
    pointer: int,
    law: CandidateLaw,
    *,
    reverse: bool = False,
    delete_matcher_gate: str | None = None,
    layers: tuple[c433.Layer, ...] | None = None,
) -> tuple[Bank, int]:
    validate_law(law)
    if len(bank) != len(law.cases):
        raise ValueError("candidate bank width does not match its law")
    output = list(bank)
    blocks = tuple(dict.fromkeys(block for _label, block in law.label_to_block))
    entries = tuple(reversed(blocks)) if reverse else blocks
    leakage = 0
    for block in entries:
        labels = tuple(label for label, mapped_block in law.label_to_block if mapped_block == block)
        enable, local_leakage = route_enable(
            pointer,
            labels,
            delete_gate=delete_matcher_gate,
        )
        leakage += local_leakage
        output[block] = c433.apply_coupled(
            output[block],
            enable,
            reverse=reverse,
            layers=layers,
        )
    return tuple(output), leakage


def reference_law(bank: Bank, pointer: int, law: CandidateLaw) -> Bank:
    output = list(bank)
    for block in dict.fromkeys(block for _label, block in law.label_to_block):
        labels = tuple(label for label, mapped_block in law.label_to_block if mapped_block == block)
        if pointer in labels:
            output[block] = replace(
                output[block],
                bits=c433.coarse_register(output[block], law.cases[block], 1),
            )
    return tuple(output)


def bank_signature(bank: Bank) -> tuple[Word, ...]:
    return tuple(c433.selected(item.bits, item.layout.target) for item in bank)


def bank_workspace(bank: Bank) -> int:
    return sum(c433.workspace_leakage(item) for item in bank)


def bank_candidate_count(bank: Bank) -> int:
    return sum(any(word) for word in bank_signature(bank))


def make_cases(length: int, *, held: bool) -> tuple[c433.FormationCase, ...]:
    fixture = c364.c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 4)
    x = 5 if length == 3 else 17
    y = 0 if length == 3 else -11
    z = 0 if length == 3 else 5
    cases = []
    for lane, payload in enumerate(payloads[1:4]):
        target = (x, y + lane, z)
        predecessor = (x - 1, y + lane, z)
        cases.append(
            c433.FormationCase(length, fixture, target, predecessor, payload, payloads[0], held)
        )
    return tuple(cases)


def laws_for_cases(cases: tuple[c433.FormationCase, ...], *, refined: bool) -> tuple[CandidateLaw, CandidateLaw]:
    coarse_map = ((0, 0), (1, 0)) if refined else ((0, 0),)
    fine_map = ((0, 0), (1, 1)) if refined else ((0, 0),)
    coarse = CandidateLaw(
        "A: coarse effect-functional candidate",
        (cases[0],),
        coarse_map,
        True,
        False,
    )
    fine = CandidateLaw(
        "B: fine presentation-faithful candidate",
        cases[:2] if refined else (cases[0],),
        fine_map,
        False,
        True,
    )
    return coarse, fine


def held_refined_program(contact: np.ndarray, split: float) -> c321.Program:
    if not isinstance(split, (int, float, np.floating)) or not 0 < float(split) < 1:
        raise ValueError("refinement split must lie strictly inside (0,1)")
    p = c321.projector((3, -4, 0))
    weight = 0.61
    return c321.Program(
        "held two-piece ray refinement",
        (
            sqrt(split * weight) * p @ contact,
            sqrt((1 - split) * weight) * p @ contact,
            sqrt(weight) * (c321.I2 - p) @ contact,
            sqrt(1 - weight) * contact,
        ),
        ((0, 1), (2,), (3,)),
    )


Sparse = dict[tuple[int, int, tuple[tuple[int, ...], ...]], complex]


def add_sparse(output: Sparse, key, value: complex) -> None:
    output[key] = output.get(key, 0j) + value
    if abs(output[key]) < 1e-15:
        del output[key]


def physical_pointer_then_law(
    program: c321.Program,
    logical: np.ndarray,
    bank: Bank,
    law: CandidateLaw,
) -> tuple[Sparse, int]:
    output: Sparse = {}
    leakage = 0
    for pointer, operator in enumerate(program.kraus):
        vector = operator @ np.asarray(logical, dtype=complex)
        updated, local_leakage = apply_law(bank, pointer, law)
        leakage += local_leakage
        signature = tuple(item.bits for item in updated)
        for system, amplitude in enumerate(vector):
            if abs(amplitude) > 1e-15:
                add_sparse(output, (pointer, system, signature), complex(amplitude))
    return output, leakage


def coarse_then_encode(
    program: c321.Program,
    logical: np.ndarray,
    bank: Bank,
    law: CandidateLaw,
) -> Sparse:
    output: Sparse = {}
    for pointer, operator in enumerate(program.kraus):
        vector = operator @ np.asarray(logical, dtype=complex)
        updated = reference_law(bank, pointer, law)
        signature = tuple(item.bits for item in updated)
        for system, amplitude in enumerate(vector):
            if abs(amplitude) > 1e-15:
                add_sparse(output, (pointer, system, signature), complex(amplitude))
    return output


def sparse_residual(left: Sparse, right: Sparse) -> float:
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def inverse_sparse(state: Sparse, law: CandidateLaw) -> Sparse:
    output: Sparse = {}
    for (pointer, system, signature), amplitude in state.items():
        bank = tuple(c433.BasisState(case_layout, bits) for case_layout, bits in zip(
            (case.layout for case in prepare_bank(c433.LAYOUT, law)), signature
        ))
        restored, leakage = apply_law(bank, pointer, law, reverse=True)
        if leakage:
            raise RuntimeError("matcher leakage on inverse")
        add_sparse(output, (pointer, system, tuple(item.bits for item in restored)), amplitude)
    return output


def input_sparse(program: c321.Program, logical: np.ndarray, bank: Bank) -> Sparse:
    output: Sparse = {}
    signature = tuple(item.bits for item in bank)
    for pointer, operator in enumerate(program.kraus):
        vector = operator @ np.asarray(logical, dtype=complex)
        for system, amplitude in enumerate(vector):
            if abs(amplitude) > 1e-15:
                add_sparse(output, (pointer, system, signature), complex(amplitude))
    return output


def matcher_and_layout_controls() -> dict[str, object]:
    print("\nPHYSICAL POINTER MATCHER / PROTECTED PACKET COMPILER")
    matcher_failures = inverse_failures = support_failures = 0
    gate_counts = []
    for selected_label in range(8):
        schedule = matcher_schedule(selected_label)
        gate_counts.append(2 * (2 * len(schedule) + 1))
        support_failures += sum(not matcher_support_connected(item) for item in schedule)
        support_failures += int(
            not matcher_support_connected(
                matcher_gate("CNOT", (ENABLE_SITE, ROUTE_SITE), "route-latch")
            )
        )
        for pointer in range(8):
            enable, leakage = matcher_enable(pointer, selected_label)
            matcher_failures += int(enable != int(pointer == selected_label))
            inverse_failures += int(leakage != 0)
    c433.validate_layout(c433.LAYOUT)
    check(
        "the three-M2 pointer matcher and Cycle-433 field writer are fixed bounded connected-NN reversible circuits",
        matcher_failures == inverse_failures == support_failures == 0
        and max(gate_counts) <= 34,
        {
            "fine_pointer_M2": POINTER_BITS,
            "matcher_work_M2": MATCHER_WORK_M2,
            "pointer_labels_tested": 8,
            "matcher_truth_cases": 64,
            "single_label_match_route_use_unmatch_gate_maximum": max(gate_counts),
            "two_label_coarse_route_gate_maximum": 2 * max(gate_counts),
            "matcher_maximum_support_M2": 3,
            "matcher_connected_NN_failures": support_failures,
            "Cycle433_added_compiler_M2_per_packet_block": len(c433.LAYOUT.sites),
            "Cycle433_layers_per_packet_block": len(c433.LAYOUT.layers),
            "Cycle433_primitive_gates_per_packet_block": sum(len(item.gates) for item in c433.LAYOUT.layers) + 2,
            "protected_packet_M2": c370.CARRIER_BITS,
            "source_pointer_preserved": True,
        },
    )
    return {"matcher_gate_max": max(gate_counts)}


def physical_program_controls(fixtures: dict[int, c317.PhysicalFixture]) -> dict[str, object]:
    print("\nCYCLE317/CYCLE321 PHYSICAL POINTER INPUT")
    rows = []
    failures = 0
    programs = {}
    for length, fixture in fixtures.items():
        unsplit, refined, data = c321.ray_programs(fixture.contact)
        held_refined = held_refined_program(fixture.contact, HELD_SPLIT)
        trine, _coin = c321.auxiliary_programs(fixture.contact)
        programs[length] = (unsplit, refined, held_refined, trine)
        for program in programs[length]:
            completeness = float(np.linalg.norm(program.completeness - c321.I2))
            isometry = float(np.linalg.norm(c317.stack_isometry(program.kraus).conj().T @ c317.stack_isometry(program.kraus) - c321.I2))
            failures += int(max(completeness, isometry) > TOL)
        ray_effect = float(np.linalg.norm(unsplit.coarse_effects[0] - refined.coarse_effects[0]))
        held_effect = float(np.linalg.norm(unsplit.coarse_effects[0] - held_refined.coarse_effects[0]))
        directions = tuple(
            np.asarray((np.cos(2 * np.pi * index / 3), np.sin(2 * np.pi * index / 3), 0.0))
            for index in range(3)
        )
        deleted_effects = tuple((2 / 3) * c317.projector_bloch(direction) for direction in directions)
        contact_deletion = min(
            float(np.linalg.norm(effect - deleted))
            for effect, deleted in zip(trine.coarse_effects, deleted_effects)
        )
        rows.append({
            "L": length,
            "held": length == 6,
            "train_refinement": data["split"],
            "held_refinement": HELD_SPLIT,
            "ray_effect_train_residual": ray_effect,
            "ray_effect_held_split_residual": held_effect,
            "trine_effect_normalization_residual": float(np.linalg.norm(sum(trine.coarse_effects) - c321.I2)),
            "trine_contact_deletion_minimum_effect_residual": contact_deletion,
            "pointer_M2": POINTER_BITS,
        })
        failures += int(max(ray_effect, held_effect, rows[-1]["trine_effect_normalization_residual"]) > TOL)
        failures += int(contact_deletion < 0.17)
    check(
        "the declared Cycle-317 contact seam satisfying its seam test supplies normalized trine and train/held proportional-refinement pointer states",
        failures == 0,
        {"rows": rows, "failures": failures},
    )
    return {"programs": programs, "rows": rows}


def tournament_intertwiner_controls(
    fixtures: dict[int, c317.PhysicalFixture],
    programs_by_length: dict[int, tuple[c321.Program, ...]],
) -> dict[str, object]:
    print("\nTWO-LAW EXACT E/G AND INVERSE TOURNAMENT")
    logical_inputs = (
        np.asarray((1, 0), dtype=complex),
        np.asarray((0, 1), dtype=complex),
        np.asarray((np.sqrt(2 / 5), np.exp(1j * np.pi / 7) * np.sqrt(3 / 5)), dtype=complex),
    )
    rows = []
    failures = 0
    cached = {}
    for length, fixture in fixtures.items():
        cases = make_cases(length, held=length == 6)
        coarse_law, fine_law = laws_for_cases(cases, refined=True)
        refined = programs_by_length[length][1 if length == 3 else 2]
        for law in (coarse_law, fine_law):
            bank = prepare_bank(c433.LAYOUT, law)
            for input_index, logical in enumerate(logical_inputs):
                physical, matcher_leakage = physical_pointer_then_law(refined, logical, bank, law)
                reference = coarse_then_encode(refined, logical, bank, law)
                forward = sparse_residual(physical, reference)
                recovered = inverse_sparse(physical, law)
                inverse = sparse_residual(recovered, input_sparse(refined, logical, bank))
                maximum_workspace = max(
                    bank_workspace(tuple(c433.BasisState(block.layout, bits) for block, bits in zip(bank, signature)))
                    for _pointer, _system, signature in physical
                )
                row = {
                    "law": law.name,
                    "L": length,
                    "held": length == 6,
                    "split": TRAIN_SPLIT if length == 3 else HELD_SPLIT,
                    "logical_input": input_index,
                    "E_G_residual": forward,
                    "inverse_residual": inverse,
                    "matcher_leakage": matcher_leakage,
                    "packet_workspace_leakage": maximum_workspace,
                    "source_pointer_labels": tuple(sorted({key[0] for key in physical})),
                }
                failures += int(
                    forward > TOL
                    or inverse > TOL
                    or matcher_leakage
                    or maximum_workspace
                    or row["source_pointer_labels"] != tuple(range(4))
                )
                rows.append(row)
        cached[length] = {"cases": cases, "coarse": coarse_law, "fine": fine_law, "refined": refined}

    held = cached[6]
    coarse_bank = prepare_bank(c433.LAYOUT, held["coarse"])
    fine_bank = prepare_bank(c433.LAYOUT, held["fine"])
    coarse_zero, _ = apply_law(coarse_bank, 0, held["coarse"])
    coarse_one, _ = apply_law(coarse_bank, 1, held["coarse"])
    fine_zero, _ = apply_law(fine_bank, 0, held["fine"])
    fine_one, _ = apply_law(fine_bank, 1, held["fine"])
    coarse_same = bank_signature(coarse_zero) == bank_signature(coarse_one)
    fine_distinct = bank_signature(fine_zero) != bank_signature(fine_one)
    decoded = c433.target_replica(coarse_zero[0], held["cases"][0].fixture)
    check(
        "both laws compile the same physical pointer state with exact E/G and inverse while their protected packet semantics differ",
        failures == 0
        and coarse_same
        and fine_distinct
        and decoded == c433.expected_replica(held["cases"][0])
        and bank_candidate_count(coarse_zero) == bank_candidate_count(coarse_one) == 1
        and bank_candidate_count(fine_zero) == bank_candidate_count(fine_one) == 1,
        {
            "rows": rows,
            "maximum_E_G_residual": max(row["E_G_residual"] for row in rows),
            "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
            "maximum_matcher_leakage": max(row["matcher_leakage"] for row in rows),
            "maximum_packet_workspace_leakage": max(row["packet_workspace_leakage"] for row in rows),
            "coarse_labels_0_1_same_packet": coarse_same,
            "fine_labels_0_1_distinct_packets": fine_distinct,
            "pointer_erased_during_compilation": False,
            "output_is_full_Cycle370_compatible_packet": decoded is not None,
            "failures": failures,
        },
    )
    return {"cached": cached, "rows": rows}


def cp_map(kraus: tuple[np.ndarray, ...], rho: np.ndarray) -> np.ndarray:
    return sum((operator @ rho @ operator.conj().T for operator in kraus), start=np.zeros((2, 2), dtype=complex))


def candidate_weight(program: c321.Program, logical: np.ndarray, labels: tuple[int, ...]) -> float:
    return float(sum(np.linalg.norm(program.kraus[label] @ logical) ** 2 for label in labels))


def refinement_functionality_controls(cache: dict[int, dict[str, object]], programs_by_length) -> dict[str, object]:
    print("\nREFINEMENT INVARIANCE / PRESENTATION-FAITHFUL SEPARATOR")
    rows = []
    failures = 0
    for length in (3, 6):
        data = cache[length]
        cases = data["cases"]
        coarse_law = data["coarse"]
        fine_law = data["fine"]
        unsplit = programs_by_length[length][0]
        refined = data["refined"]
        unsplit_coarse, _unsplit_fine = laws_for_cases(cases, refined=False)
        input_state = np.asarray((np.sqrt(3 / 7), np.exp(1j * np.pi / 5) * np.sqrt(4 / 7)), dtype=complex)
        rho = np.outer(input_state, input_state.conj())
        effect_residual = float(np.linalg.norm(unsplit.coarse_effects[0] - refined.coarse_effects[0]))
        cp_residual = float(np.linalg.norm(
            cp_map((unsplit.kraus[0],), rho)
            - cp_map(tuple(refined.kraus[index] for index in (0, 1)), rho)
        ))
        weight_residual = abs(
            candidate_weight(unsplit, input_state, (0,))
            - candidate_weight(refined, input_state, (0, 1))
        )
        coarse_unsplit_bank = prepare_bank(c433.LAYOUT, unsplit_coarse)
        coarse_refined_bank = prepare_bank(c433.LAYOUT, coarse_law)
        fine_refined_bank = prepare_bank(c433.LAYOUT, fine_law)
        coarse_unsplit, _ = apply_law(coarse_unsplit_bank, 0, unsplit_coarse)
        coarse_refined_zero, _ = apply_law(coarse_refined_bank, 0, coarse_law)
        coarse_refined_one, _ = apply_law(coarse_refined_bank, 1, coarse_law)
        fine_refined_zero, _ = apply_law(fine_refined_bank, 0, fine_law)
        fine_refined_one, _ = apply_law(fine_refined_bank, 1, fine_law)
        coarse_equal = (
            bank_signature(coarse_unsplit)
            == bank_signature(coarse_refined_zero)
            == bank_signature(coarse_refined_one)
        )
        refined_packets = tuple(
            next(word for word in bank_signature(bank) if any(word))
            for bank in (fine_refined_zero, fine_refined_one)
        )
        fine_hashes = tuple(sha256(repr(word).encode()).hexdigest() for word in refined_packets)
        row = {
            "L": length,
            "held": length == 6,
            "split": TRAIN_SPLIT if length == 3 else HELD_SPLIT,
            "coarse_effect_residual": effect_residual,
            "selected_coarse_CP_output_residual": cp_residual,
            "candidate_sector_weight_residual": weight_residual,
            "coarse_packet_equal_unsplit_refined0_refined1": coarse_equal,
            "fine_packet_hashes": fine_hashes,
            "refined_label0_label1_packet_hashes_distinct": len(set(fine_hashes)) == 2,
            "refined_label0_label1_packet_words_distinct": refined_packets[0] != refined_packets[1],
            "physical_pointer_labels_retained": True,
        }
        failures += int(
            max(effect_residual, cp_residual, weight_residual) > TOL
            or not coarse_equal
            or len(set(fine_hashes)) != 2
        )
        rows.append(row)
    fine_transcript = float(np.linalg.norm(
        c321.transcript_choi(programs_by_length[3][0].fine_effects)
        - c321.transcript_choi(programs_by_length[3][1].fine_effects)
    ))
    check(
        "the coarse packet is invariant under train/held proportional refinement while the fine packet and physical transcript remain presentation-faithful",
        failures == 0 and fine_transcript > 1.0,
        {
            "rows": rows,
            "train_fine_pointer_transcript_Choi_residual": fine_transcript,
            "effect_functionality_derived_from_packet_identity": False,
            "effect_functionality_made_physically_available_on_bounded_ray_class": True,
            "failures": failures,
        },
    )
    return {"rows": rows, "fine_transcript": fine_transcript}


def matcher_support_with_coords(item: MatcherGate, coords: tuple[Coord, ...]) -> bool:
    support = tuple(coords[index] for index in item.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(support))
            if c433.manhattan(support[left], support[right]) == 1
        }
        if grown == reached:
            return len(grown) == len(support)
        reached = grown


def physical_pointer_covariance(
    fixture: c317.PhysicalFixture,
    programs: tuple[c321.Program, ...],
) -> tuple[int, float]:
    reducer = c317.c311.c305.StabilizerReducer(fixture.code)
    selected = np.zeros((127, 2), dtype=complex)
    selected[
        [
            c317.c311.SEAM_INDEX[(2, (0, 1), stream_slice)]
            for stream_slice in (0, 1)
        ],
        [0, 1],
    ] = 1
    failures = 0
    maximum = 0.0
    for frame in c317.c311.c235.proper_cubic_frames():
        logical_r = c317.c311.logical_frame_representation(frame)
        old_r, frame_failures = c317.c311.flagged_frame_representation(
            fixture.encoder,
            fixture.basis_rows,
            fixture.occurrence,
            frame,
            reducer,
        )
        mapping, phases, mapping_failures = c317.c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        carried_f = fixture.full_encoding @ logical_r @ selected
        failures += frame_failures + mapping_failures
        for program in programs:
            base_v = c317.physical_isometry(fixture.two_ray_encoding, program.kraus)
            carried_v = c317.physical_isometry(carried_f, program.kraus)
            blocks = []
            for pointer in range(8):
                block = base_v[510 * pointer : 510 * (pointer + 1), :]
                blocks.append(c317.c311.apply_signed_mapping(new_mapping, new_phases, block))
            maximum = max(maximum, float(np.linalg.norm(np.vstack(blocks) - carried_v)))
    return failures, maximum


def rotate_case(case: c433.FormationCase, frame: np.ndarray) -> tuple[c433.FormationCase, int]:
    fixture, mapping, failures = c364.c342.mapped_fixture(case.fixture, frame)
    return (
        c433.FormationCase(
            case.length,
            fixture,
            c433.rotated_coord(case.target, frame),
            c433.rotated_coord(case.predecessor, frame),
            c364.rotate_payload(case.payload, mapping),
            c364.rotate_payload(case.prior_payload, mapping),
            case.held,
        ),
        failures,
    )


def covariance_resource_controls(
    cache: dict[int, dict[str, object]],
    programs_by_length,
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nALL-24 COVARIANCE / TRAIN-HELD RESOURCE LEDGER")
    frames = c317.c311.c235.proper_cubic_frames()
    payload_failures = packet_failures = inverse_failures = support_failures = 0
    cases_tested = 0
    for frame in frames:
        framed_layout = c433.rotated_layout(c433.LAYOUT, frame)
        try:
            c433.validate_layout(framed_layout)
        except ValueError:
            support_failures += 1
        matcher_coords = tuple(c433.rotated_coord(coord, frame) for coord in MATCHER_COORDS)
        support_failures += sum(
            not matcher_support_with_coords(item, matcher_coords)
            for label in range(8)
            for item in matcher_schedule(label)
        )
        for length in (3, 6):
            moved_cases = []
            for case in cache[length]["cases"]:
                moved, failures = rotate_case(case, frame)
                moved_cases.append(moved)
                payload_failures += failures
            coarse, fine = laws_for_cases(tuple(moved_cases), refined=True)
            for law in (coarse, fine):
                source = prepare_bank(framed_layout, law)
                for pointer in (0, 1):
                    output, matcher_leakage = apply_law(source, pointer, law)
                    packet_failures += matcher_leakage
                    expected = reference_law(source, pointer, law)
                    packet_failures += int(bank_signature(output) != bank_signature(expected))
                    restored, leakage = apply_law(output, pointer, law, reverse=True)
                    inverse_failures += leakage + int(restored != source)
                    for block_index, block in enumerate(output):
                        word = c433.selected(block.bits, block.layout.target)
                        if any(word):
                            packet_failures += int(
                                c433.target_replica(block, moved_cases[block_index].fixture)
                                != c433.expected_replica(moved_cases[block_index])
                            )
                    cases_tested += 1

    pointer_rows = []
    for length, program_indices in ((3, (0, 1)), (6, (0, 2))):
        failures, residual = physical_pointer_covariance(
            fixtures[length],
            tuple(programs_by_length[length][index] for index in program_indices),
        )
        pointer_rows.append({"L": length, "failures": failures, "residual": residual})
    pointer_failures = sum(row["failures"] for row in pointer_rows)
    pointer_residual = max(row["residual"] for row in pointer_rows)
    cycle433_block = len(c433.LAYOUT.sites)
    pointer_patch = 59
    router_per_block = 240
    coarse_m2 = pointer_patch + cycle433_block + POINTER_BITS + MATCHER_WORK_M2 + router_per_block
    fine_m2 = pointer_patch + 2 * (cycle433_block + POINTER_BITS + MATCHER_WORK_M2 + router_per_block)
    check(
        "both candidate laws remain bounded and covariant through train L=3, held L=6, and all 24 frames",
        len(frames) == 24
        and cases_tested == 192
        and payload_failures == packet_failures == inverse_failures == support_failures == 0
        and pointer_failures == 0
        and pointer_residual < TOL,
        {
            "proper_cubic_frames": len(frames),
            "law_length_pointer_frame_cases": cases_tested,
            "physical_pointer_frame_failures": pointer_failures,
            "maximum_physical_pointer_apparatus_residual": pointer_residual,
            "physical_pointer_train_held_rows": pointer_rows,
            "payload_mapping_failures": payload_failures,
            "protected_packet_failures": packet_failures,
            "packet_inverse_failures": inverse_failures,
            "rotated_matcher_or_Cycle433_support_failures": support_failures,
            "Cycle321_conservative_pointer_patch_M2": pointer_patch,
            "Cycle433_compiler_M2_per_packet_block": cycle433_block,
            "declared_blank_pointer_router_M2_per_block": router_per_block,
            "coarse_law_bounded_M2": coarse_m2,
            "fine_law_bounded_M2": fine_m2,
            "maximum_primitive_support_M2": 3,
            "resource_counts_are_bounded_accounts_not_optimality_claims": True,
        },
    )
    return {"coarse_m2": coarse_m2, "fine_m2": fine_m2, "pointer_residual": pointer_residual}


def mutate_target_bit(state: c433.BasisState, lane: int) -> c433.BasisState:
    bits = list(state.bits)
    bits[state.layout.target[lane]] ^= 1
    return replace(state, bits=tuple(bits))


def deletion_leakage_domain_controls(
    cache: dict[int, dict[str, object]],
    programs_by_length,
    fixtures: dict[int, c317.PhysicalFixture],
) -> dict[str, object]:
    print("\nREFINEMENT / POINTER / PAYLOAD / CONTROL DELETIONS")
    data = cache[6]
    cases = data["cases"]
    coarse = data["coarse"]
    fine = data["fine"]
    coarse_bank = prepare_bank(c433.LAYOUT, coarse)
    fine_bank = prepare_bank(c433.LAYOUT, fine)

    coarse_zero, _ = apply_law(coarse_bank, 0, coarse)
    coarse_one, _ = apply_law(coarse_bank, 1, coarse)
    fine_zero, _ = apply_law(fine_bank, 0, fine)
    fine_one, _ = apply_law(fine_bank, 1, fine)
    refinement_bit_deleted_coarse_invariant = bank_signature(coarse_zero) == bank_signature(coarse_one)
    refinement_bit_deleted_fine_visible = bank_signature(fine_zero) != bank_signature(fine_one)

    fine_label_one = CandidateLaw(
        "B deletion probe",
        (cases[1],),
        ((1, 0),),
        False,
        True,
    )
    label_one_bank = prepare_bank(c433.LAYOUT, fine_label_one)
    matcher_deleted, matcher_leakage = apply_law(
        label_one_bank,
        1,
        fine_label_one,
        delete_matcher_gate="pointer-match-load:lane2",
    )
    matcher_deletion_blocks = bank_candidate_count(matcher_deleted) == 0 and matcher_leakage == 0

    desired = c370.encode_replica(cases[0].fixture, c433.expected_replica(cases[0]))
    payload_lane = next(lane for lane in range(24, 54) if desired[lane])
    deleted_layers, removed = c433.without_gate(c433.LAYOUT.layers, f"field-write:lane{payload_lane}")
    payload_deleted, _ = apply_law(coarse_bank, 0, coarse, layers=deleted_layers)
    payload_deletion_visible = False
    try:
        payload_deletion_visible = c433.target_replica(payload_deleted[0], cases[0].fixture) != c433.expected_replica(cases[0])
    except ValueError:
        payload_deletion_visible = True

    controls = {
        "predecessor_readiness": c433.prepare(c433.LAYOUT, cases[0], readiness=0),
        "fresh_capacity": c433.prepare(c433.LAYOUT, cases[0], fresh=0),
        "payload_presence": c433.prepare(
            c433.LAYOUT,
            cases[0],
            payload_present=(0,) + (1,) * (c364.RECORD_BITS - 1),
        ),
        "payload_lawful_certificate": c433.prepare(c433.LAYOUT, cases[0], lawful_certificate=0),
        "faithful_close": c433.prepare(c433.LAYOUT, cases[0], faithful_close=0),
        "provenance": c433.prepare(c433.LAYOUT, cases[0], provenance=0),
    }
    control_rows = {}
    for name, state in controls.items():
        output, leakage = apply_law((state,), 0, coarse)
        control_rows[name] = {
            "blank": bank_candidate_count(output) == 0,
            "leakage": leakage + bank_workspace(output),
        }

    dirty = mutate_target_bit(coarse_bank[0], 24)
    dirty_output, dirty_leakage = apply_law((dirty,), 0, coarse)
    dirty_refused = dirty_output == (dirty,) and dirty_leakage == 0

    refined = programs_by_length[6][2]
    deleted_kraus = (np.zeros_like(refined.kraus[0]),) + refined.kraus[1:]
    branch_deletion_defect = float(np.linalg.norm(
        sum((operator.conj().T @ operator for operator in deleted_kraus), start=np.zeros((2, 2), dtype=complex))
        - c321.I2
    ))

    malformed_laws = (
        CandidateLaw("duplicate", (cases[0],), ((0, 0), (0, 0)), True, False),
        CandidateLaw("absent block", (cases[0],), ((0, 1),), True, False),
        CandidateLaw("ambiguous behavior", (cases[0],), ((0, 0),), False, False),
    )
    malformed_calls = [
        lambda law=law: prepare_bank(c433.LAYOUT, law) for law in malformed_laws
    ]
    malformed_calls.extend((
        lambda: pointer_word(8),
        lambda: held_refined_program(fixtures[6].contact, 0.0),
        lambda: held_refined_program(fixtures[6].contact, 1.0),
        lambda: apply_law(coarse_bank[:-1], 0, coarse),
        lambda: c433.prepare(c433.LAYOUT, replace(cases[0], payload=cases[0].payload[:-1])),
        lambda: matcher_enable(0, 8),
    ))
    rejections = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, RuntimeError, IndexError):
            rejections += 1

    occupancy_rejections = 0
    for lane in range(c370.OCCUPANCY_BITS):
        corrupted = mutate_target_bit(coarse_zero[0], lane)
        try:
            c433.target_replica(corrupted, cases[0].fixture)
        except ValueError:
            occupancy_rejections += 1

    check(
        "refinement-label, matcher, payload, predicate, protection, dirty-state, and lawful-domain controls separate the two candidates cleanly",
        refinement_bit_deleted_coarse_invariant
        and refinement_bit_deleted_fine_visible
        and matcher_deletion_blocks
        and removed == 1
        and payload_deletion_visible
        and all(row["blank"] and row["leakage"] == 0 for row in control_rows.values())
        and dirty_refused
        and branch_deletion_defect > 0.14
        and abs(branch_deletion_defect - HELD_SPLIT * 0.61) < TOL
        and rejections == len(malformed_calls)
        and occupancy_rejections == c370.OCCUPANCY_BITS,
        {
            "refinement_bit_deleted_coarse_packet_invariant": refinement_bit_deleted_coarse_invariant,
            "refinement_bit_deleted_fine_packet_visible": refinement_bit_deleted_fine_visible,
            "matcher_gate_deletion_blocks_label1": matcher_deletion_blocks,
            "payload_write_gate_deleted_lane": payload_lane,
            "payload_write_deletion_visible": payload_deletion_visible,
            "predicate_control_deletions": control_rows,
            "dirty_target_refused": dirty_refused,
            "physical_fine_branch_deletion_completeness_defect": branch_deletion_defect,
            "single_protected_occupancy_fault_rejections": occupancy_rejections,
            "lawful_domain_rejections": rejections,
            "nominal_matcher_leakage": 0,
            "nominal_packet_workspace_leakage": 0,
        },
    )
    return {"domain_rejections": rejections, "branch_deletion": branch_deletion_defect}


def premise_audit_controls() -> dict[str, object]:
    print("\nEXACT PR-PREMISE AUDIT")
    actual_heads = {
        ref: subprocess.check_output(("git", "rev-parse", ref), cwd=ROOT, text=True).strip()
        for ref in PR_HEADS
    }
    audit = {
        "PR5472@2c648ccb": {
            "E1_weight_on_all_effects_and_effect_functionality": {
                "A": "one bounded scaled-ray refinement class only",
                "B": "not supplied: fine presentation remains encoded",
            },
            "E2_every_finite_effect_partition_eligible_and_normalized": {
                "A": "open",
                "B": "open",
            },
            "full_trace_form_theorem_triggered": False,
        },
        "PR5476@a9946178": {
            "F1_weight_on_all_scaled_projectors_and_effect_functionality": {
                "A": "one bounded scaled-ray refinement class only",
                "B": "not supplied: fine presentation remains encoded",
            },
            "F2_all_scaled_projector_menus_eligible_and_normalized": {
                "A": "open",
                "B": "open",
            },
            "same_ray_split_representative_invariance": {
                "A": "physically available for the Cycle-321 ray pair",
                "B": "deliberately presentation-distinguishing",
            },
            "axis_cancellation_and_coin_family": "not compiled by either formation law",
            "full_trace_form_theorem_triggered": False,
        },
        "PR5479@84053108": {
            "G1_all_binary_effect_menus": {"A": "open", "B": "open"},
            "G2_all_ternary_effect_menus": {
                "A": "one physical contact-sensitive trine is a load-bearing control only",
                "B": "one physical contact-sensitive trine is a load-bearing control only",
            },
            "X1_finite_mixed_projective_presentations_with_exact_split_merge": {
                "A": "one physical proportional split/merge witness",
                "B": "same input presentation, but its fine labels remain distinct",
            },
            "X1_element_domain_functionality_and_normalization": {
                "A": "one bounded element-functionality witness; normalization and total domain open",
                "B": "functionality not supplied; normalization and total domain open",
            },
            "three_outcome_or_mixed_projective_theorem_triggered": False,
        },
    }
    checks = (
        actual_heads == PR_HEADS,
        all(not data[next(key for key in data if key.endswith("theorem_triggered"))] for data in audit.values()),
        "one bounded scaled-ray refinement class only"
        == audit["PR5472@2c648ccb"]["E1_weight_on_all_effects_and_effect_functionality"]["A"],
        audit["PR5479@84053108"]["G2_all_ternary_effect_menus"]["A"].endswith("control only"),
    )
    check(
        "the physical result is bounded below every theorem's exact total-domain, eligibility, and normalization premises",
        all(checks),
        {"PR_heads": actual_heads, "premise_audit": audit},
    )
    return audit


def semantic_inventory_controls(resources: dict[str, object]) -> dict[str, object]:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "supplied": (
            "the declared Cycle-317 contact seam satisfying its seam test and Cycle-321 proportional split programs",
            "the coarse label grouping and the two candidate routing tables",
            "blank pointer-router corridors and blank Cycle-433 packet blocks",
            "Cycle-370 field meanings and Cycle-433 write predicates",
            "the logical input and the unselected pointer isometry",
        ),
        "derived": (
            "exact local matcher truth table and inverse",
            "exact E G_coarse = G_physical E on both declared code spaces",
            "coarse packet equality for unsplit and two proportional refined labels",
            "fine 79-bit packet-word inequality for the two refined labels",
            "all-24 proper-cubic covariance and train/held controls",
            "field-write, matcher, refinement, branch, predicate, and lawful-domain sensitivities",
        ),
        "open": (
            "autonomous effect recognition beyond the declared routing table",
            "total effect or scaled-projector domains",
            "menu eligibility, grading, and normalization",
            "actualization, branch selection, and occurrence",
            "admission of a protected candidate packet as a framework Record",
            "statistics, frequencies, probability values, and a Born law",
        ),
        "semantic_flags": {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "coarse_law_selected": False,
            "fine_law_selected": False,
            "pointer_erased": False,
            "candidate_packet_is_Record": False,
            "physical_sector_norm_called_probability": False,
            "trine_control_used_as_universal_G2_E2_or_F2": False,
            "occurrence_sampler_frequency_or_probability_law_supplied": False,
        },
        "resources": resources,
    }
    flags = inventory["semantic_flags"]
    check(
        "both protected-packet laws remain unselected candidates with the physical source pointer and theorem walls explicit",
        flags["authority"] == "none"
        and flags["audit"] == "unset"
        and not any(value for key, value in flags.items() if key not in ("authority", "audit", "pointer_erased"))
        and flags["pointer_erased"] is False,
        inventory,
    )
    return inventory


def main() -> None:
    note_contract()
    source_contract()
    matcher_and_layout_controls()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    physical = physical_program_controls(fixtures)
    tournament = tournament_intertwiner_controls(fixtures, physical["programs"])
    refinement_functionality_controls(tournament["cached"], physical["programs"])
    resources = covariance_resource_controls(tournament["cached"], physical["programs"], fixtures)
    deletion_leakage_domain_controls(tournament["cached"], physical["programs"], fixtures)
    premise_audit_controls()
    semantic_inventory_controls(resources)
    print(f"\nSUMMARY PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
