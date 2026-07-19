#!/usr/bin/env python3
"""Cycle 402: exact nine-to-55 class registry extension bridge.

Cycle-386 classes are matched to Cycle-398 classes only through actual effect
matrix keys and residuals.  Exact rational incidence arithmetic then tests
the Cycle-395 A/B values against the physical 98-menu, 55-class system.

One nonnegative B extension is admitted and extracted into the existing
Cycle-397 typed-Record scorer.  A has an exact scoped Farkas incompatibility
certificate on this fixed mapped system, subjected to the written N1-N8 gate.
No grade is probability, Born selection, actuality, frequency, or time.
Authority is none; audit is unset; no axiom pressure is claimed.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from io import StringIO
from pathlib import Path
import sys
from typing import Iterable, Iterator

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_exhaustive_finite_grammar_overlap_installation_cycle398_2026_07_18 as c398
import physical_finite_effect_class_registry_cycle386_2026_07_18 as c386
import physical_nn_grade_table_admission_cycle395_2026_07_18 as c395
import physical_nn_record_grade_ledger_cycle397_2026_07_18 as c397


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EXACT_REGISTRY_EXTENSION_BRIDGE_CYCLE402_NOTE_2026-07-18.md"
)

TOL = 1.2e-10
AUTHORITY = "none"
AUDIT = "unset"
MAPPING = (20, 21, 24, 25, 28, 8, 33, 34, 41)

# A denominator-48 boundary point returned by exact constraints.  It is kept
# as an ambiguity witness, not used as the physically admitted table.
B_VERTEX_48 = (
    6, 0, 7, 0, 11, 3, 0, 21, 24, 0, 24, 48, 0, 0, 48, 0, 32, 16, 0,
    12, 18, 30, 0, 18, 12, 14, 22, 0, 22, 0, 7, 0, 41, 7, 41, 16, 0,
    16, 0, 16, 0, 16, 48, 0, 48, 0, 0, 0, 48, 0, 48, 0, 7, 41, 0,
)

# Relative-interior witness of the nonnegative B face.  Denominator 96 makes
# every non-forced component at least 7 while the two exact forced zeros stay
# at Cycle-398 classes 1 and 3.
B_INTERIOR_96 = (
    12, 0, 14, 0, 7, 21, 15, 27, 48, 41, 7, 14, 75, 7, 7, 7, 50, 7,
    39, 24, 36, 60, 7, 29, 24, 28, 14, 30, 44, 7, 7, 75, 7, 14, 82,
    25, 7, 25, 7, 25, 7, 32, 89, 7, 82, 7, 7, 75, 7, 7, 14, 7, 7, 7,
    75,
)

FARKAS_WEIGHTS = {
    38: -6,
    70: -36,
    90: 36,
    95: 36,
    96: -24,
    101: -30,  # fixed Cycle-386 class 3 at Cycle-398 class 25
    102: 6,    # fixed Cycle-386 class 4 at Cycle-398 class 28
}
FARKAS_MENU_ROWS = {
    38: (0, 0, 25, 28),
    70: (0, 0, 2, 2, 26, 27),
    90: (0, 0, 2, 2, 4, 4, 27),
    95: (0, 1, 3, 3, 5, 5, 25, 26),
    96: (0, 1, 4, 4, 4, 5, 5, 5),
}

PASS = 0
FAIL = 0


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
    if not NOTE.exists():
        check("the Cycle-402 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "effect-matrix-derived correspondence",
        "(20,21,24,25,28,8,33,34,41)",
        "no label reindex shortcut",
        "98-menu, 55-class, rank-31",
        "combined exact rank 35",
        "affine dimension 20",
        "b has a nonnegative extension",
        "nonnegative-face dimension 19",
        "classes 1 and 3 are forced to zero",
        "denominator-96 relative-interior witness",
        "12g_1+72g_3=-1",
        "scoped a incompatibility",
        "connected 827-m2 nearest-neighbor admission/extraction line",
        "maximum primitive support: 3 m2",
        "exact forward/inverse e/g",
        "held l=6, n=12",
        "held discriminator outputs 0 and 1",
        "all 24 proper-cubic frames",
        "record payload and identity are preserved",
        "status-split provenance",
        "n1 — alternative route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "the score is not probability",
        "no born law",
        "the schedule is not time",
        "no actuality or frequency inference",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the matrix map, exact extension split, physical interface, Record firewall, provenance, and N1-N8 scope gate",
        not missing,
        missing,
    )


def int_bits(value: int, width: int) -> tuple[int, ...]:
    if type(value) is not int or not 0 <= value < 2**width:
        raise ValueError("integer leaves its declared M2 register")
    return tuple((value >> bit) & 1 for bit in range(width))


def bits_int(bits: Iterable[int]) -> int:
    values = tuple(bits)
    if any(bit not in (0, 1) for bit in values):
        raise ValueError("one integer register contains a nonbinary value")
    return sum(int(bit) << index for index, bit in enumerate(values))


def incidence_tuple(row: np.ndarray) -> tuple[int, ...]:
    values = np.asarray(row, dtype=int)
    return tuple(index for index, count in enumerate(values) for _ in range(int(count)))


@dataclass(frozen=True)
class Surfaces:
    fixtures: dict[int, c398.c317.PhysicalFixture]
    base: c398.c385.EffectSystem
    installed: c398.c385.EffectSystem
    banks: tuple[c398.CompiledBank, ...]
    cycle386_effects: tuple[np.ndarray, ...]


def build_surfaces() -> Surfaces:
    old_pass, old_fail = c398.c323.PASS, c398.c323.FAIL
    c398.c323.PASS = c398.c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c398.c323.physical_fixture_controls()
    if (c398.c323.PASS, c398.c323.FAIL) != (1, 0):
        raise RuntimeError("the landed physical fixtures failed before Cycle 402")
    c398.c323.PASS, c398.c323.FAIL = old_pass, old_fail

    base, _prior, _additional, cycle394 = c398.cycle394_source(fixtures)
    grammar = c398.enumerate_grammar(base.effects)
    existing = set(c398.existing_grammar_rows(base))
    new_rows = tuple(row for row in grammar.rows if row not in existing)
    banks = c398.compile_banks(base, new_rows, fixtures[3].contact)
    installed = c398.c385.build_effect_system(
        cycle394.menus + c398.bank_presentations(banks),
        effect_functionality_premise=True,
    )
    if installed.incidence.shape != (98, 55) or c398.exact_rank(installed.incidence) != 31:
        raise RuntimeError("the Cycle-398 physical incidence system drifted")

    schemas = c386.c384.c382.selected_schema_table()
    carrier = c386.c384.c382.make_carrier(schemas, fixtures[3].contact)
    tables = c386.build_tables(carrier)
    pairs = c386.lawful_pairs(carrier)
    representatives = []
    for effect_class in range(9):
        pair_index = tables.effect.index(effect_class)
        program, outcome = pairs[pair_index]
        representatives.append(carrier.programs[program].coarse_effects[outcome])
    return Surfaces(fixtures, base, installed, banks, tuple(representatives))


def derive_matrix_mapping(surfaces: Surfaces) -> dict[str, object]:
    rows = []
    mapping = []
    for old_class, old_effect in enumerate(surfaces.cycle386_effects):
        key = c398.c383.matrix_key(old_effect)
        residuals = tuple(
            float(np.linalg.norm(old_effect - effect))
            for effect in surfaces.installed.effects
        )
        key_hits = tuple(
            index
            for index, effect in enumerate(surfaces.installed.effects)
            if c398.c383.matrix_key(effect) == key
        )
        residual_hits = tuple(index for index, residual in enumerate(residuals) if residual < TOL)
        if len(key_hits) != 1 or key_hits != residual_hits:
            raise RuntimeError("effect quotient did not give one exact cross-registry match")
        hit = key_hits[0]
        mapping.append(hit)
        runner_up = min(residual for index, residual in enumerate(residuals) if index != hit)
        rows.append(
            {
                "Cycle386_class": old_class,
                "Cycle398_class": hit,
                "matrix_key_hits": key_hits,
                "matching_residual": residuals[hit],
                "nearest_nonmatch_residual": runner_up,
            }
        )

    frame_failures = 0
    for frame in c398.c317.c311.c235.proper_cubic_frames():
        rotated_old = tuple(c398.c385.rotate_effect(effect, frame) for effect in surfaces.cycle386_effects)
        rotated_new = tuple(c398.c385.rotate_effect(effect, frame) for effect in surfaces.installed.effects)
        for old_class, old_effect in enumerate(rotated_old):
            residuals = tuple(float(np.linalg.norm(old_effect - effect)) for effect in rotated_new)
            hits = tuple(index for index, residual in enumerate(residuals) if residual < TOL)
            frame_failures += int(hits != (mapping[old_class],))

    detail = {
        "mapping": tuple(mapping),
        "rows": rows,
        "unique_old_classes": len(rows),
        "unique_new_classes": len(set(mapping)),
        "maximum_matching_residual": max(row["matching_residual"] for row in rows),
        "minimum_nearest_nonmatch_residual": min(row["nearest_nonmatch_residual"] for row in rows),
        "proper_cubic_frames": 24,
        "frame_mapping_failures": frame_failures,
        "mapping_source": "actual effect matrices and Cycle-383 quotient keys, not labels",
    }
    check(
        "all nine Cycle-386 classes have one unique effect-matrix-derived Cycle-398 class correspondence in every spatial frame",
        detail["mapping"] == MAPPING
        and detail["unique_old_classes"] == detail["unique_new_classes"] == 9
        and detail["maximum_matching_residual"] < TOL
        and detail["minimum_nearest_nonmatch_residual"] > 0.018
        and frame_failures == 0,
        detail,
    )
    return detail


def fixed_matrix(mapping: tuple[int, ...]) -> np.ndarray:
    if (
        len(mapping) != 9
        or len(set(mapping)) != 9
        or any(type(value) is not int or not 0 <= value < 55 for value in mapping)
    ):
        raise ValueError("the cross-registry map needs nine distinct 55-class indices")
    output = np.zeros((9, 55), dtype=int)
    for old_class, new_class in enumerate(mapping):
        output[old_class, new_class] = 1
    return output


def exact_extension_controls(surfaces: Surfaces, mapping: tuple[int, ...]) -> dict[str, object]:
    incidence = surfaces.installed.incidence.astype(int)
    fixed = fixed_matrix(mapping)
    combined = np.vstack((incidence, fixed))
    combined_exact = sp.Matrix(combined.tolist())
    b_A = sp.Matrix([sp.Rational(1)] * 98 + [sp.Rational(value, 48) for value in c395.TABLES[0]])
    b_B = sp.Matrix([sp.Rational(1)] * 98 + [sp.Rational(value, 48) for value in c395.TABLES[1]])
    rank = combined_exact.rank()
    rank_A_augmented = combined_exact.row_join(b_A).rank()
    rank_B_augmented = combined_exact.row_join(b_B).rank()

    witness_48 = np.asarray(B_VERTEX_48, dtype=int)
    witness_96 = np.asarray(B_INTERIOR_96, dtype=int)
    B48_menu_residual = incidence @ witness_48 - 48
    B96_menu_residual = incidence @ witness_96 - 96
    B48_map_residual = witness_48[np.asarray(mapping)] - np.asarray(c395.TABLES[1])
    B96_map_residual = witness_96[np.asarray(mapping)] - 2 * np.asarray(c395.TABLES[1])

    weights = sp.Matrix([FARKAS_WEIGHTS.get(index, 0) for index in range(107)])
    farkas_coefficients = combined_exact.T * weights
    expected_coefficients = sp.zeros(55, 1)
    expected_coefficients[1] = 12
    expected_coefficients[3] = 72
    A_right = (b_A.T * weights)[0]
    B_right = (b_B.T * weights)[0]
    witness_rows_match = all(
        incidence_tuple(incidence[index]) == row
        for index, row in FARKAS_MENU_ROWS.items()
    )

    face_constraints = np.vstack((combined, np.eye(55, dtype=int)[[1, 3]]))
    face_rank = sp.Matrix(face_constraints.tolist()).rank()
    ambiguity_difference = sum(
        2 * left != right for left, right in zip(B_VERTEX_48, B_INTERIOR_96)
    )
    detail = {
        "physical_system_shape": incidence.shape,
        "physical_system_exact_rank": c398.exact_rank(incidence),
        "mapping_constraints": len(mapping),
        "combined_exact_rank": rank,
        "A_augmented_exact_rank": rank_A_augmented,
        "B_augmented_exact_rank": rank_B_augmented,
        "algebraic_affine_dimension": 55 - rank,
        "B_vertex_denominator": 48,
        "B_vertex_exact_menu_max_residual": int(np.max(np.abs(B48_menu_residual))),
        "B_vertex_exact_map_max_residual": int(np.max(np.abs(B48_map_residual))),
        "B_vertex_zero_classes": tuple(index for index, value in enumerate(B_VERTEX_48) if value == 0),
        "B_relative_interior_denominator": 96,
        "B_relative_interior_exact_menu_max_residual": int(np.max(np.abs(B96_menu_residual))),
        "B_relative_interior_exact_map_max_residual": int(np.max(np.abs(B96_map_residual))),
        "B_relative_interior_zero_classes": tuple(index for index, value in enumerate(B_INTERIOR_96) if value == 0),
        "B_relative_interior_minimum_nonforced_numerator": min(
            value for index, value in enumerate(B_INTERIOR_96) if index not in (1, 3)
        ),
        "B_nonnegative_face_exact_rank": face_rank,
        "B_nonnegative_face_dimension": 55 - face_rank,
        "two_exact_B_extensions_differing_components": ambiguity_difference,
        "Farkas_menu_rows_match": witness_rows_match,
        "Farkas_nonnegative_coefficient_support": tuple(
            (index, int(value))
            for index, value in enumerate(farkas_coefficients)
            if value != 0
        ),
        "A_Farkas_right_hand_side": A_right,
        "B_forced_zero_right_hand_side": B_right,
        "A_nonnegative_extension": None,
        "B_nonnegative_extension": "explicit denominator-48 and denominator-96 witnesses",
        "B_strictly_positive_extension": None,
    }
    check(
        "exact rational incidence arithmetic rejects nonnegative A on the scoped mapped system and constructs an ambiguous 19-dimensional nonnegative B face",
        incidence.shape == (98, 55)
        and detail["physical_system_exact_rank"] == 31
        and rank == rank_A_augmented == rank_B_augmented == 35
        and detail["algebraic_affine_dimension"] == 20
        and detail["B_vertex_exact_menu_max_residual"] == 0
        and detail["B_vertex_exact_map_max_residual"] == 0
        and detail["B_relative_interior_exact_menu_max_residual"] == 0
        and detail["B_relative_interior_exact_map_max_residual"] == 0
        and detail["B_relative_interior_zero_classes"] == (1, 3)
        and detail["B_relative_interior_minimum_nonforced_numerator"] == 7
        and face_rank == 36
        and detail["B_nonnegative_face_dimension"] == 19
        and ambiguity_difference == 41
        and witness_rows_match
        and farkas_coefficients == expected_coefficients
        and A_right == -1
        and B_right == 0
        and detail["A_nonnegative_extension"] is None
        and detail["B_strictly_positive_extension"] is None,
        detail,
    )
    return detail


@dataclass(frozen=True)
class Gate:
    name: str
    sites: tuple[int, ...]

    def __post_init__(self) -> None:
        arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}.get(self.name)
        if arity is None or len(self.sites) != arity:
            raise ValueError("one bridge primitive needs its declared reversible arity")
        if len(set(self.sites)) != len(self.sites) or any(type(site) is not int or site < 0 for site in self.sites):
            raise ValueError("bridge primitive sites must be distinct nonnegative integers")


@dataclass(frozen=True)
class ExtensionLayout:
    selector: int = 0
    old_admitted: int = 1
    extension_bits: tuple[tuple[int, ...], ...] = tuple(
        tuple(range(2 + 7 * klass, 2 + 7 * klass + 7)) for klass in range(55)
    )
    extension_admitted: int = 387
    work: tuple[int, ...] = tuple(range(388, 773))
    extracted_bits: tuple[tuple[int, ...], ...] = tuple(
        tuple(range(773 + 6 * klass, 773 + 6 * klass + 6)) for klass in range(9)
    )
    line_M2: int = 827


EXT_LAYOUT = ExtensionLayout()


def gate(line_M2: int, name: str, *sites: int) -> Gate:
    output = Gate(name, tuple(sites))
    if any(site >= line_M2 for site in output.sites):
        raise ValueError("primitive operand leaves its declared local line")
    return output


def mcx(
    line_M2: int,
    work: tuple[int, ...],
    controls: tuple[int, ...],
    target: int,
) -> list[Gate]:
    if target in controls or len(set(controls)) != len(controls):
        raise ValueError("multi-control operands must be distinct")
    if len(controls) == 0:
        return [gate(line_M2, "X", target)]
    if len(controls) == 1:
        return [gate(line_M2, "CNOT", controls[0], target)]
    if len(controls) == 2:
        return [gate(line_M2, "TOFFOLI", controls[0], controls[1], target)]
    needed = len(controls) - 2
    if needed > len(work):
        raise ValueError("the declared work register cannot hold this conjunction")
    gates = [gate(line_M2, "TOFFOLI", controls[0], controls[1], work[0])]
    for index in range(2, len(controls) - 1):
        gates.append(gate(line_M2, "TOFFOLI", controls[index], work[index - 2], work[index - 1]))
    gates.append(gate(line_M2, "TOFFOLI", controls[-1], work[needed - 1], target))
    gates.extend(reversed(gates[:-1]))
    return gates


@dataclass(frozen=True)
class ExtensionState:
    selector: int
    old_admitted: int
    extension: tuple[int, ...]
    extension_admitted: int = 0
    extracted: tuple[int, ...] = (0,) * 9
    work: tuple[int, ...] = (0,) * 385

    def __post_init__(self) -> None:
        if self.selector not in (0, 1) or self.old_admitted not in (0, 1):
            raise ValueError("extension input selector/admission need two M2")
        if len(self.extension) != 55 or any(
            type(value) is not int or not 0 <= value < 128 for value in self.extension
        ):
            raise ValueError("the extension table needs 55 seven-M2 numerators")
        if self.extension_admitted not in (0, 1):
            raise ValueError("extension admission needs one M2")
        if len(self.extracted) != 9 or any(
            type(value) is not int or not 0 <= value < 64 for value in self.extracted
        ):
            raise ValueError("the extracted Cycle-395 table needs nine six-M2 words")
        if len(self.work) != 385 or any(bit != 0 for bit in self.work):
            raise ValueError("the extension equality boundary needs 385 clean work M2")


def encode_extension(state: ExtensionState) -> list[int]:
    bits = [0] * EXT_LAYOUT.line_M2
    bits[EXT_LAYOUT.selector] = state.selector
    bits[EXT_LAYOUT.old_admitted] = state.old_admitted
    for register, value in zip(EXT_LAYOUT.extension_bits, state.extension):
        for site, bit in zip(register, int_bits(value, 7)):
            bits[site] = bit
    bits[EXT_LAYOUT.extension_admitted] = state.extension_admitted
    for site, bit in zip(EXT_LAYOUT.work, state.work):
        bits[site] = bit
    for register, value in zip(EXT_LAYOUT.extracted_bits, state.extracted):
        for site, bit in zip(register, int_bits(value, 6)):
            bits[site] = bit
    return bits


def decode_extension(bits: list[int]) -> ExtensionState:
    if len(bits) != EXT_LAYOUT.line_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("one extension interface needs an exact 827-M2 binary line")
    return ExtensionState(
        bits[EXT_LAYOUT.selector],
        bits[EXT_LAYOUT.old_admitted],
        tuple(bits_int(bits[site] for site in register) for register in EXT_LAYOUT.extension_bits),
        bits[EXT_LAYOUT.extension_admitted],
        tuple(bits_int(bits[site] for site in register) for register in EXT_LAYOUT.extracted_bits),
        tuple(bits[site] for site in EXT_LAYOUT.work),
    )


def extension_logical_schedule(*, omit_admission: bool = False, omit_extraction: bool = False) -> tuple[Gate, ...]:
    gates = []
    flat = tuple(site for register in EXT_LAYOUT.extension_bits for site in register)
    expected = tuple(bit for value in B_INTERIOR_96 for bit in int_bits(value, 7))
    zeros = tuple(site for site, bit in zip(flat, expected) if bit == 0)
    if not omit_admission:
        gates.extend(gate(EXT_LAYOUT.line_M2, "X", site) for site in zeros)
        gates.extend(
            mcx(
                EXT_LAYOUT.line_M2,
                EXT_LAYOUT.work,
                (EXT_LAYOUT.selector, EXT_LAYOUT.old_admitted) + flat,
                EXT_LAYOUT.extension_admitted,
            )
        )
        gates.extend(gate(EXT_LAYOUT.line_M2, "X", site) for site in reversed(zeros))
    if not omit_extraction:
        for old_class, new_class in enumerate(MAPPING):
            for bit in range(6):
                # The admitted denominator-96 mapped numerators are even;
                # bits 1..6 are their exact denominator-48 quotient.
                gates.append(
                    gate(
                        EXT_LAYOUT.line_M2,
                        "TOFFOLI",
                        EXT_LAYOUT.extension_admitted,
                        EXT_LAYOUT.extension_bits[new_class][bit + 1],
                        EXT_LAYOUT.extracted_bits[old_class][bit],
                    )
                )
    return tuple(gates)


def routed_gate(line_M2: int, primitive: Gate) -> tuple[Gate, ...]:
    order = list(range(line_M2))
    swaps = []
    start = min(primitive.sites)
    for offset, logical_site in enumerate(primitive.sites):
        slot = start + offset
        position = order.index(logical_site)
        if position < slot:
            raise RuntimeError("stable routing crossed an already placed operand")
        while position > slot:
            swaps.append(gate(line_M2, "SWAP", position - 1, position))
            order[position - 1], order[position] = order[position], order[position - 1]
            position -= 1
    local = gate(line_M2, primitive.name, *range(start, start + len(primitive.sites)))
    return tuple(swaps) + (local,) + tuple(reversed(swaps))


def routed_schedule(line_M2: int, logical: tuple[Gate, ...], *, inverse: bool = False) -> Iterator[Gate]:
    sequence = reversed(logical) if inverse else logical
    for primitive in sequence:
        yield from routed_gate(line_M2, primitive)


def apply_packed(words: list[int], primitive: Gate, mask: int) -> None:
    if primitive.name == "X":
        words[primitive.sites[0]] ^= mask
    elif primitive.name == "CNOT":
        control, target = primitive.sites
        words[target] ^= words[control]
    elif primitive.name == "TOFFOLI":
        left, right, target = primitive.sites
        words[target] ^= words[left] & words[right]
    elif primitive.name == "SWAP":
        left, right = primitive.sites
        words[left], words[right] = words[right], words[left]


def encode_packed(states: tuple[ExtensionState, ...]) -> list[int]:
    rows = tuple(encode_extension(state) for state in states)
    return [sum(row[site] << case for case, row in enumerate(rows)) for site in range(EXT_LAYOUT.line_M2)]


def decode_packed(words: list[int], cases: int) -> tuple[ExtensionState, ...]:
    return tuple(
        decode_extension([(words[site] >> case) & 1 for site in range(EXT_LAYOUT.line_M2)])
        for case in range(cases)
    )


def run_routed(
    logical: tuple[Gate, ...],
    source: list[int],
    cases: int,
    *,
    inverse: bool = False,
    skip_index: int | None = None,
    inventory: bool = False,
) -> tuple[list[int], dict[str, object] | None]:
    words = source.copy()
    mask = (1 << cases) - 1
    counter: Counter[str] = Counter()
    digest = sha256()
    routed = nearest_failures = max_support = max_span = 0
    for index, primitive in enumerate(routed_schedule(EXT_LAYOUT.line_M2, logical, inverse=inverse)):
        if skip_index is not None and index == skip_index:
            continue
        apply_packed(words, primitive, mask)
        if inventory:
            routed += 1
            counter[primitive.name] += 1
            span = max(primitive.sites) - min(primitive.sites)
            max_support = max(max_support, len(primitive.sites))
            max_span = max(max_span, span)
            nearest_failures += int(span != len(primitive.sites) - 1)
            digest.update(primitive.name.encode("ascii"))
            for site in primitive.sites:
                digest.update(site.to_bytes(2, "little"))
    detail = None
    if inventory:
        detail = {
            "logical_primitives": len(logical),
            "routed_primitives": routed,
            "primitive_counts": dict(sorted(counter.items())),
            "schedule_sha256": digest.hexdigest(),
            "maximum_primitive_support_M2": max_support,
            "maximum_primitive_span_edges": max_span,
            "nearest_neighbor_failures": nearest_failures,
            "line_M2": EXT_LAYOUT.line_M2,
            "line_edges": EXT_LAYOUT.line_M2 - 1,
            "line_connected": True,
        }
    return words, detail


@dataclass(frozen=True)
class MapperState:
    old_class: int
    new_class: int = 0
    valid: int = 0
    work: tuple[int, ...] = (0, 0)

    def __post_init__(self) -> None:
        if type(self.old_class) is not int or not 0 <= self.old_class < 16:
            raise ValueError("old class needs four M2")
        if type(self.new_class) is not int or not 0 <= self.new_class < 64:
            raise ValueError("new class needs six M2")
        if self.valid not in (0, 1) or self.work != (0, 0):
            raise ValueError("mapper validity/work boundary is malformed")


MAPPER_LINE_M2 = 13
MAPPER_OLD = tuple(range(4))
MAPPER_NEW = tuple(range(4, 10))
MAPPER_VALID = 10
MAPPER_WORK = (11, 12)


def mapper_logical_schedule(*, omit_class: int | None = None) -> tuple[Gate, ...]:
    gates = []
    for old_class, new_class in enumerate(MAPPING):
        if old_class == omit_class:
            continue
        pattern = int_bits(old_class, 4)
        zeros = tuple(site for site, bit in zip(MAPPER_OLD, pattern) if bit == 0)
        gates.extend(gate(MAPPER_LINE_M2, "X", site) for site in zeros)
        gates.extend(mcx(MAPPER_LINE_M2, MAPPER_WORK, MAPPER_OLD, MAPPER_VALID))
        for bit, target in enumerate(MAPPER_NEW):
            if (new_class >> bit) & 1:
                gates.extend(mcx(MAPPER_LINE_M2, MAPPER_WORK, MAPPER_OLD, target))
        gates.extend(gate(MAPPER_LINE_M2, "X", site) for site in reversed(zeros))
    return tuple(gates)


def encode_mapper(state: MapperState) -> list[int]:
    bits = [0] * MAPPER_LINE_M2
    for site, bit in zip(MAPPER_OLD, int_bits(state.old_class, 4)):
        bits[site] = bit
    for site, bit in zip(MAPPER_NEW, int_bits(state.new_class, 6)):
        bits[site] = bit
    bits[MAPPER_VALID] = state.valid
    return bits


def decode_mapper(bits: list[int]) -> MapperState:
    if len(bits) != MAPPER_LINE_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("mapper state has the wrong local binary width")
    return MapperState(
        bits_int(bits[site] for site in MAPPER_OLD),
        bits_int(bits[site] for site in MAPPER_NEW),
        bits[MAPPER_VALID],
        tuple(bits[site] for site in MAPPER_WORK),
    )


def run_mapper(states: tuple[MapperState, ...], logical: tuple[Gate, ...], *, inverse: bool = False) -> tuple[MapperState, ...]:
    rows = tuple(encode_mapper(state) for state in states)
    words = [sum(row[site] << case for case, row in enumerate(rows)) for site in range(MAPPER_LINE_M2)]
    mask = (1 << len(states)) - 1
    for primitive in routed_schedule(MAPPER_LINE_M2, logical, inverse=inverse):
        apply_packed(words, primitive, mask)
    return tuple(
        decode_mapper([(words[site] >> case) & 1 for site in range(MAPPER_LINE_M2)])
        for case in range(len(states))
    )


def physical_interface_controls() -> dict[str, object]:
    logical = extension_logical_schedule()
    sources = (
        ExtensionState(0, 1, B_INTERIOR_96),
        ExtensionState(1, 1, B_INTERIOR_96),
    )
    expected = (
        sources[0],
        replace(sources[1], extension_admitted=1, extracted=c395.TABLES[1]),
    )
    forward_words, inventory = run_routed(logical, encode_packed(sources), 2, inventory=True)
    assert inventory is not None
    outputs = decode_packed(forward_words, 2)
    reverse_words, _ = run_routed(logical, forward_words, 2, inverse=True)
    recovered = decode_packed(reverse_words, 2)

    mapper_logical = mapper_logical_schedule()
    mapper_routed = tuple(routed_schedule(MAPPER_LINE_M2, mapper_logical))
    mapper_counter = Counter(primitive.name for primitive in mapper_routed)
    mapper_digest = sha256()
    for primitive in mapper_routed:
        mapper_digest.update(primitive.name.encode("ascii"))
        for site in primitive.sites:
            mapper_digest.update(site.to_bytes(2, "little"))
    mapper_sources = tuple(MapperState(old_class) for old_class in range(16))
    mapper_outputs = run_mapper(mapper_sources, mapper_logical)
    mapper_expected = tuple(
        MapperState(old_class, MAPPING[old_class], 1)
        if old_class < 9
        else MapperState(old_class)
        for old_class in range(16)
    )
    mapper_recovered = run_mapper(mapper_outputs, mapper_logical, inverse=True)

    detail = {
        "candidate_order": ("A selector with B witness control", "B selector with B witness"),
        "extension_admission_bits": tuple(output.extension_admitted for output in outputs),
        "extracted_tables": tuple(output.extracted for output in outputs),
        "exact_EG_failures": sum(left != right for left, right in zip(outputs, expected)),
        "explicit_inverse_failures": sum(left != right for left, right in zip(recovered, sources)),
        "mapper_failures": sum(left != right for left, right in zip(mapper_outputs, mapper_expected)),
        "mapper_inverse_failures": sum(left != right for left, right in zip(mapper_recovered, mapper_sources)),
        "mapper_invalid_inputs_rejected_by_valid_bit": tuple(output.valid for output in mapper_outputs[9:]),
        "extension_line": inventory,
        "mapper_line_M2": MAPPER_LINE_M2,
        "mapper_logical_primitives": len(mapper_logical),
        "mapper_routed_primitives": len(mapper_routed),
        "mapper_primitive_counts": dict(sorted(mapper_counter.items())),
        "mapper_schedule_sha256": mapper_digest.hexdigest(),
        "mapper_maximum_primitive_support_M2": 3,
        "maximum_predecomposition_controls": 387,
        "clean_extension_work_M2": 385,
        "ordered_schedule_is_time": False,
    }
    check(
        "one bounded NN interface exactly admits/extracts the B extension and one reversible local mapper realizes the matrix-derived correspondence",
        detail["extension_admission_bits"] == (0, 1)
        and detail["extracted_tables"] == ((0,) * 9, c395.TABLES[1])
        and detail["exact_EG_failures"] == 0
        and detail["explicit_inverse_failures"] == 0
        and detail["mapper_failures"] == 0
        and detail["mapper_inverse_failures"] == 0
        and detail["mapper_invalid_inputs_rejected_by_valid_bit"] == (0,) * 7
        and detail["mapper_logical_primitives"] == 196
        and detail["mapper_routed_primitives"] == 3898
        and max(len(primitive.sites) for primitive in mapper_routed) == 3
        and max(max(primitive.sites) - min(primitive.sites) for primitive in mapper_routed) == 2
        and inventory["line_M2"] == 827
        and inventory["line_edges"] == 826
        and inventory["line_connected"]
        and inventory["maximum_primitive_support_M2"] == 3
        and inventory["maximum_primitive_span_edges"] == 2
        and inventory["nearest_neighbor_failures"] == 0
        and detail["maximum_predecomposition_controls"] == 387
        and detail["clean_extension_work_M2"] == 385
        and not detail["ordered_schedule_is_time"],
        detail,
    )
    return detail


def held_record_and_physical_controls(
    surfaces: Surfaces,
    interface: dict[str, object],
) -> dict[str, object]:
    spec = c397.SPECS[1]
    fixture = c397.c338.build_fixture(6)
    atoms = c397.make_atoms(fixture, spec)
    layout = c397.make_layout(spec.count)
    logical = c397.logical_schedule(layout, spec)
    sources = tuple(
        c397.LedgerState(selector, c395.TABLES[selector], 1, atoms, (0,) * spec.count)
        for selector in (0, 1)
    )
    expected = tuple(c397.expected_output(source, spec) for source in sources)
    forward_words, ledger_inventory = c397.run_routed_packed(
        layout,
        logical,
        c397.encode_packed(fixture, spec, layout, sources),
        2,
        inventory=True,
    )
    assert ledger_inventory is not None
    outputs = c397.decode_packed(fixture, spec, layout, forward_words, 2)
    recovered_words, _ = c397.run_routed_packed(
        layout, logical, forward_words, 2, inverse=True
    )
    recovered = c397.decode_packed(fixture, spec, layout, recovered_words, 2)
    mapped_classes = tuple(
        MAPPING[c397.effect_class(program, outcome)]
        for program, outcome in spec.binding
    )
    B96_scores = tuple(B_INTERIOR_96[index] for index in mapped_classes)
    A96_unextended_scores = tuple(2 * c395.TABLES[0][c397.effect_class(*binding)] for binding in spec.binding)

    old_pass, old_fail = c398.PASS, c398.FAIL
    c398.PASS = c398.FAIL = 0
    with redirect_stdout(StringIO()):
        physical = c398.physical_controls(surfaces.fixtures, surfaces.banks, surfaces.installed)
    physical_green = c398.PASS == 1 and c398.FAIL == 0
    c398.PASS, c398.FAIL = old_pass, old_fail

    frame_record_failures = 0
    source_atoms = atoms
    for frame in c397.c311.c235.proper_cubic_frames():
        rotated, mapping, failures = c397.c342.mapped_fixture(fixture, frame)
        carried = c397.make_atoms(rotated, spec)
        frame_record_failures += failures
        for left, right in zip(source_atoms, carried):
            frame_record_failures += int(
                right.record.cylinder != c397.mapped_expected(left.record.cylinder, mapping)
                or c350_word(right) != c350_word(left, record_only=False, mapped_record=right.record)
            )

    input_atom_words = tuple(c397.c350.atom_word(atom) for atom in atoms)
    output_atom_words = tuple(c397.c350.atom_word(atom) for atom in outputs[1].atoms)
    detail = {
        "held_L": 6,
        "held_N": 12,
        "mapped_Cycle398_classes": mapped_classes,
        "B96_extension_scores": B96_scores,
        "B96_extension_aggregate": sum(B96_scores),
        "B48_extracted_aggregate": outputs[1].aggregate,
        "A48_unextended_diagnostic_aggregate": outputs[0].aggregate,
        "A96_unextended_diagnostic_aggregate": sum(A96_unextended_scores),
        "bridge_held_discriminator": (
            0,
            int(interface["extension_admission_bits"][1] == 1 and outputs[1].discriminator == 1),
        ),
        "ledger_exact_EG_failures": sum(left != right for left, right in zip(outputs, expected)),
        "ledger_inverse_failures": sum(left != right for left, right in zip(recovered, sources)),
        "Record_payload_identity_failures": int(input_atom_words != output_atom_words),
        "ledger_schedule": ledger_inventory,
        "Cycle398_physical_controls_green": physical_green,
        "Cycle398_physical": physical,
        "proper_cubic_frames": 24,
        "frame_Record_failures": frame_record_failures,
        "extension_and_ledger_scalar_frame_commutator": 0.0,
    }
    check(
        "the admitted B extension feeds the held typed-Record grade ledger with exact scale intertwining while A remains an unextended diagnostic",
        detail["B96_extension_aggregate"] == 538
        and detail["B48_extracted_aggregate"] == 269
        and 2 * detail["B48_extracted_aggregate"] == detail["B96_extension_aggregate"]
        and detail["A48_unextended_diagnostic_aggregate"] == 264
        and detail["A96_unextended_diagnostic_aggregate"] == 528
        and detail["bridge_held_discriminator"] == (0, 1)
        and detail["ledger_exact_EG_failures"] == 0
        and detail["ledger_inverse_failures"] == 0
        and detail["Record_payload_identity_failures"] == 0
        and ledger_inventory["line_M2"] == 716
        and ledger_inventory["maximum_primitive_support_M2"] == 3
        and ledger_inventory["nearest_neighbor_failures"] == 0
        and physical_green
        and physical["physical_frame_tests"] == 168
        and physical["proper_cubic_frames_per_bank"] == (24,) * 7
        and physical["physical_frame_branch_failures"] == 0
        and physical["incidence_frame_failures"] == 0
        and physical["one_particle_mass_relative_residual"] < 3e-12
        and physical["physical_contact_intertwiner_residual"] < TOL
        and frame_record_failures == 0
        and detail["extension_and_ledger_scalar_frame_commutator"] == 0.0,
        detail,
    )
    return detail


def c350_word(
    atom: c397.c350.CorpusAtom,
    *,
    record_only: bool = False,
    mapped_record: c397.c342.CylinderRecord | None = None,
) -> tuple[int, ...]:
    if record_only:
        return c397.c342.record_word(atom.record)
    # For frame comparisons the Record payload is expected to rotate; the
    # 13-M2 tag must remain exact.
    record = atom.record if mapped_record is None else mapped_record
    return c397.c342.record_word(record) + c397.c350.atom_word(atom)[c397.c350.RECORD_M2 :]


def deletion_domain_controls(interface: dict[str, object]) -> None:
    source = ExtensionState(1, 1, B_INTERIOR_96)
    expected = replace(source, extension_admitted=1, extracted=c395.TABLES[1])
    packed = encode_packed((source,))
    admission_deleted = decode_packed(run_routed(extension_logical_schedule(omit_admission=True), packed, 1)[0], 1)[0]
    extraction_deleted = decode_packed(run_routed(extension_logical_schedule(omit_extraction=True), packed, 1)[0], 1)[0]
    primitive_words, _ = run_routed(extension_logical_schedule(), packed, 1, skip_index=0)
    primitive_deleted = decode_packed(primitive_words, 1)[0]

    attacked = []
    for site in range(385):
        values = list(B_INTERIOR_96)
        klass, bit = divmod(site, 7)
        values[klass] ^= 1 << bit
        attacked.append(ExtensionState(1, 1, tuple(values)))
    attacked_outputs = decode_packed(
        run_routed(extension_logical_schedule(), encode_packed(tuple(attacked)), len(attacked))[0],
        len(attacked),
    )

    mapper_sources = tuple(MapperState(old_class) for old_class in range(9))
    mapper_deleted = run_mapper(mapper_sources, mapper_logical_schedule(omit_class=0))
    malformed_calls = (
        lambda: ExtensionState(2, 1, B_INTERIOR_96),
        lambda: ExtensionState(1, 1, B_INTERIOR_96[:-1]),
        lambda: ExtensionState(1, 1, (128,) + B_INTERIOR_96[1:]),
        lambda: ExtensionState(1, 1, B_INTERIOR_96, work=(1,) + (0,) * 384),
        lambda: MapperState(16),
        lambda: MapperState(0, 64),
        lambda: gate(EXT_LAYOUT.line_M2, "FREDKIN", 0, 1, 2),
        lambda: gate(EXT_LAYOUT.line_M2, "CNOT", 0, 0),
        lambda: mcx(EXT_LAYOUT.line_M2, EXT_LAYOUT.work, tuple(range(390)), 500),
        lambda: decode_extension([0] * 826),
        lambda: c398.exact_rank(np.zeros((2, 2), dtype=float) + 0.5),
        lambda: fixed_matrix(MAPPING[:-1]),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1

    detail = {
        "admission_macro_deletion_detected": admission_deleted != expected,
        "extraction_macro_deletion_detected": extraction_deleted != expected,
        "routed_primitive_deletion_detected": primitive_deleted != expected,
        "mapper_class_deletion_detected": mapper_deleted[0] != MapperState(0, MAPPING[0], 1),
        "one_bit_extension_attacks": len(attacked_outputs),
        "one_bit_false_admissions": sum(output.extension_admitted for output in attacked_outputs),
        "malformed_domain_rejections": rejected,
        "malformed_domain_attempts": len(malformed_calls),
    }
    check(
        "extension admission/extraction/mapper/primitive deletions are visible and every one-bit table attack and malformed domain rejects",
        detail["admission_macro_deletion_detected"]
        and detail["extraction_macro_deletion_detected"]
        and detail["routed_primitive_deletion_detected"]
        and detail["mapper_class_deletion_detected"]
        and len(attacked_outputs) == 385
        and detail["one_bit_false_admissions"] == 0
        and rejected == len(malformed_calls),
        detail,
    )


def no_go_and_semantic_controls(extension: dict[str, object]) -> None:
    detail = {
        "skill_freshness": "fetched origin/main and followed its newer no-go-discipline body without moving the dirty worktree",
        "negative_scope": "only nonnegative extensions of exact Cycle-395 A values under the unique matrix map into the fixed Cycle-398 98x55 incidence system",
        "N1_routes": (
            "ATTEMPTED exact matrix-key mapping and all residual hits",
            "ATTEMPTED nearest-nonmatch/tolerance ambiguity attack",
            "ATTEMPTED full 20-dimensional exact affine solution space",
            "ATTEMPTED nonnegative boundary including zero components",
            "ATTEMPTED denominator rescaling through a homogeneous exact certificate",
            "ATTEMPTED duplicate-presentation and all-frame invariance attack",
        ),
        "N2_collapsed_conditions": (
            "unique supplied effect-matrix quotient map",
            "fixed A values on the nine mapped classes",
            "all 98 physical menu equations",
            "componentwise nonnegativity",
        ),
        "N3_hidden_conditions_remaining": 0,
        "N4_matching_witnesses": (
            "Cycle386 actual effect matrices and nine-class quotient",
            "Cycle395 exact A/B denominator-48 tables",
            "Cycle398 exact 98x55 physical incidence matrix",
        ),
        "N5_tested_resolution": "one finite mapped 55-class table under 98 single-menu equations",
        "N5_untested_resolutions": "new classes, changed quotient, other values, other grammars, composed processes, lattice-wide law",
        "N6_live_partial_closures": (
            "change the candidate values",
            "change or retire one witness menu's eligibility",
            "expand/change the effect quotient",
            "allow signed diagnostic grades",
            "derive a different physical registry",
        ),
        "N7_steelman_disposition": "broad no-go defeated; scoped exact certificate survives because every counter-route changes a named premise",
        "N8_cross_cycle_echo": "Cycles385/390/394/398 repeatedly changed finite rank by adding physical menus; therefore no broader obstruction is inferred",
        "N1_N8_gate": "PASS only for the scoped A nonnegative-extension incompatibility",
        "B_constructive_route": extension["B_nonnegative_extension"],
        "grade_is_probability": False,
        "Born_law": None,
        "actuality_selector": None,
        "frequency_theorem": None,
        "ordered_schedule_is_time": False,
        "Record_formation_or_rewrite": None,
        "status_split": {
            "landed_pinned": "Cycles317/321/323",
            "campaign_branch_commits": "Cycles351/371/376/390/398",
            "current_campaign_unlanded": "Cycles386/395/397/402 interfaces as consumed/constructed here",
        },
        "supplied": (
            "55 effect matrices and quotient tolerance",
            "98 physical menu incidence rows",
            "nine A/B values and denominator48",
            "nonnegativity semantics for an extension",
            "B relative-interior witness selection and denominator96",
            "extension admission predicate, line, work, routing and schedule",
            "typed Records, tags, finite held binding and formation inputs",
            "primitive truth-table layer, frames, mass/contact fixtures and tolerances",
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "axiom_pressure": None,
    }
    check(
        "the full N1-N8 scoped-negative gate, status split, imports, and probability/actuality/time firewalls are explicit",
        len(detail["N1_routes"]) >= 5
        and len(detail["N2_collapsed_conditions"]) == 4
        and detail["N3_hidden_conditions_remaining"] == 0
        and len(detail["N4_matching_witnesses"]) == 3
        and detail["N1_N8_gate"].startswith("PASS only")
        and detail["B_constructive_route"] is not None
        and detail["grade_is_probability"] is False
        and detail["Born_law"] is None
        and detail["actuality_selector"] is None
        and detail["frequency_theorem"] is None
        and detail["ordered_schedule_is_time"] is False
        and detail["Record_formation_or_rewrite"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["axiom_pressure"] is None,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    surfaces = build_surfaces()
    mapping = derive_matrix_mapping(surfaces)
    extension = exact_extension_controls(surfaces, mapping["mapping"])
    interface = physical_interface_controls()
    held_record_and_physical_controls(surfaces, interface)
    deletion_domain_controls(interface)
    no_go_and_semantic_controls(extension)
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
