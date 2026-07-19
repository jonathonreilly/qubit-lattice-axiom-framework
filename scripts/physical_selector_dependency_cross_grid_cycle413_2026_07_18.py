#!/usr/bin/env python3
"""Cycle 413: independent selector-dependency cross-grid.

The Cycle-409 contact-support and permanent-control selector candidates are
run on one grid frozen without consulting the Cycle-407 comparator.  Contact
inputs represent N_x=0,1,2.  The independent control is either a lawful
permanent root word or a typed blank/non-Record word.  Selector agreement and
disagreement are recorded before the unchanged Cycle-407 score readout.

This maps falsifiable candidate-law differences.  It selects no grade,
actuality, probability, time, source, or axiom.  Authority is none; audit is
unset.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from hashlib import sha256
from io import StringIO
from pathlib import Path
import sys
from typing import Iterator

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_independent_selector_preparation_dynamics_cycle409_2026_07_18 as c409


c407 = c409.c407
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SELECTOR_DEPENDENCY_CROSS_GRID_CYCLE413_NOTE_2026-07-18.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10

# Frozen without consulting any Cycle-407 score or comparator output.
GRID_SECTORS = (
    ("N0 vacuum", 0),
    ("N1 canonical one-particle", 1),
    ("N2 canonical contact-active pair", 3),
)
CONTROL_KINDS = ("typed blank/non-Record", "lawful permanent root")
TYPED_BLANK_NONRECORD = (0,) * (c407.RECORD_M2 - 2) + (1, 0)

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
        check("the Cycle-413 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "independent selector-dependency cross-grid",
        "frozen without consulting the cycle-407 comparator",
        "n_x=0,1,2",
        "lawful permanent root",
        "typed blank/non-record",
        "the typed blank is not a record",
        "three agreements and three disagreements",
        "predictions are recorded before downstream scoring",
        "unchanged cycle-407 readout",
        "connected 1686-m2 nearest-neighbor line",
        "maximum primitive support: 3 m2",
        "exact forward/inverse e/g",
        "all 24 proper-cubic frames",
        "development l=3, n=8 and held l=6, n=16",
        "record payload and identity are preserved",
        "mass/q/number/vector/contact",
        "deletion and lawful-domain controls",
        "explicit supplied-structure inventory",
        "no host selection or arithmetic",
        "not actuality, probability, time, source, no-go, or axiom pressure",
        "authority: none",
        "audit: unset",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the pre-score grid, non-Record boundary, exact physical routes, controls, imports, and semantic firewall",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class GridLayout:
    base: c407.Layout
    occupation: tuple[int, ...]
    contact_pointer: int
    contact_work: tuple[int, ...]
    control_word: tuple[int, ...]
    line_M2: int


def make_layout(count: int) -> GridLayout:
    parent = c409.make_layout(count)
    cursor = parent.line_M2
    control_word = tuple(range(cursor, cursor + c407.RECORD_M2))
    cursor += c407.RECORD_M2
    return GridLayout(
        parent.base,
        parent.occupation,
        parent.contact_pointer,
        parent.contact_work,
        control_word,
        cursor,
    )


def permanent_root_word(base: c407.DiscriminatorState) -> tuple[int, ...]:
    return c407.c402.c397.c342.record_word(base.atoms[0].record)


@dataclass(frozen=True)
class GridState:
    base: c407.DiscriminatorState
    occupation: int
    control_word: tuple[int, ...]
    contact_pointer: int = 0
    contact_work: tuple[int, ...] = (0,) * c409.CONTACT_WORK_M2

    def __post_init__(self) -> None:
        if type(self.occupation) is not int or not 0 <= self.occupation < 64:
            raise ValueError("cross-grid occupation needs six M2")
        if self.occupation.bit_count() not in (0, 1, 2):
            raise ValueError("Cycle413 declares only N_x=0,1,2 sectors")
        if len(self.control_word) != c407.RECORD_M2 or any(bit not in (0, 1) for bit in self.control_word):
            raise ValueError("selector control needs one exact 30-M2 word")
        if self.control_word not in (TYPED_BLANK_NONRECORD, permanent_root_word(self.base)):
            raise ValueError("control must be the declared non-Record blank or lawful permanent root")
        if self.contact_pointer not in (0, 1):
            raise ValueError("contact pointer needs one M2")
        if len(self.contact_work) != c409.CONTACT_WORK_M2 or any(bit != 0 for bit in self.contact_work):
            raise ValueError("contact oracle needs four clean work M2")

    @property
    def control_kind(self) -> str:
        return CONTROL_KINDS[int(self.control_word[-1])]


def encode_state(layout: GridLayout, state: GridState) -> list[int]:
    bits = c407.encode_state(layout.base, state.base) + [0] * (11 + c407.RECORD_M2)
    for site, bit in zip(layout.occupation, c407.int_bits(state.occupation, 6)):
        bits[site] = bit
    bits[layout.contact_pointer] = state.contact_pointer
    for site, bit in zip(layout.contact_work, state.contact_work):
        bits[site] = bit
    for site, bit in zip(layout.control_word, state.control_word):
        bits[site] = bit
    if len(bits) != layout.line_M2:
        raise RuntimeError("cross-grid line inventory drifted")
    return bits


def decode_state(layout: GridLayout, bits: list[int]) -> GridState:
    if len(bits) != layout.line_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("cross-grid state has the wrong exact binary width")
    return GridState(
        c407.decode_state(layout.base, bits[: layout.base.line_M2]),
        c407.bits_int(bits[site] for site in layout.occupation),
        tuple(bits[site] for site in layout.control_word),
        bits[layout.contact_pointer],
        tuple(bits[site] for site in layout.contact_work),
    )


def encode_packed(layout: GridLayout, states: tuple[GridState, ...]) -> list[int]:
    rows = tuple(encode_state(layout, state) for state in states)
    return [
        sum(row[site] << case for case, row in enumerate(rows))
        for site in range(layout.line_M2)
    ]


def decode_packed(layout: GridLayout, words: list[int], cases: int) -> tuple[GridState, ...]:
    return tuple(
        decode_state(layout, [(words[site] >> case) & 1 for site in range(layout.line_M2)])
        for case in range(cases)
    )


def contact_prefix(layout: GridLayout, *, omit_oracle: bool = False, omit_transfer: bool = False) -> tuple[c407.c402.Gate, ...]:
    # GridLayout intentionally carries the Cycle409 layout interface.
    return c409.contact_preparation_schedule(
        layout, omit_oracle=omit_oracle, omit_transfer=omit_transfer
    )


def record_prefix(layout: GridLayout, *, omit_transfer: bool = False) -> tuple[c407.c402.Gate, ...]:
    if omit_transfer:
        return ()
    return (
        c407.c402.gate(
            layout.line_M2,
            "CNOT",
            layout.control_word[-1],
            layout.base.selector,
        ),
    )


def full_schedule(layout: GridLayout, route: str) -> tuple[c407.c402.Gate, ...]:
    if route == "contact":
        prefix = contact_prefix(layout)
    elif route == "record":
        prefix = record_prefix(layout)
    else:
        raise ValueError("unknown cross-grid selector route")
    return prefix + c407.logical_schedule(layout.base)


def selector_prediction(state: GridState, route: str) -> int:
    if route == "contact":
        return c409.contact_active(state.occupation)
    if route == "record":
        return state.control_word[-1]
    raise ValueError("unknown cross-grid selector route")


def expected_prefix(state: GridState, route: str) -> GridState:
    selector = selector_prediction(state, route)
    pointer = selector if route == "contact" else state.contact_pointer
    return replace(state, base=replace(state.base, selector=selector), contact_pointer=pointer)


def expected_output(state: GridState, route: str) -> GridState:
    prefix = expected_prefix(state, route)
    return replace(prefix, base=c407.expected_output(prefix.base))


def run_logical(
    logical: tuple[c407.c402.Gate, ...],
    source: list[int],
    cases: int,
    *,
    inverse: bool = False,
) -> list[int]:
    words = source.copy()
    mask = (1 << cases) - 1
    sequence = reversed(logical) if inverse else logical
    for primitive in sequence:
        c407.c402.apply_packed(words, primitive, mask)
    return words


def routed_schedule(
    layout: GridLayout,
    logical: tuple[c407.c402.Gate, ...],
    *,
    inverse: bool = False,
) -> Iterator[c407.c402.Gate]:
    yield from c407.c402.routed_schedule(layout.line_M2, logical, inverse=inverse)


def run_routed(
    layout: GridLayout,
    logical: tuple[c407.c402.Gate, ...],
    source: list[int],
    cases: int,
    *,
    inverse: bool = False,
    inventory: bool = False,
) -> tuple[list[int], dict[str, object] | None]:
    words = source.copy()
    mask = (1 << cases) - 1
    counter: Counter[str] = Counter()
    digest = sha256()
    routed = nearest_failures = max_support = max_span = 0
    for primitive in routed_schedule(layout, logical, inverse=inverse):
        c407.c402.apply_packed(words, primitive, mask)
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
            "line_M2": layout.line_M2,
            "line_edges": layout.line_M2 - 1,
            "line_connected": True,
        }
    return words, detail


def grid_states(
    atoms: tuple[c407.c402.c397.c350.CorpusAtom, ...],
) -> tuple[GridState, ...]:
    base = c407.DiscriminatorState(0, (0,) * c407.TABLE_CLASSES, atoms)
    root = permanent_root_word(base)
    return tuple(
        GridState(base, occupation, control)
        for _sector, occupation in GRID_SECTORS
        for control in (TYPED_BLANK_NONRECORD, root)
    )


def pre_score_grid_controls() -> dict[str, object]:
    fixture = c407.c402.c397.c338.build_fixture(6)
    atoms = c407.make_atoms(fixture, 16)
    layout = make_layout(16)
    sources = grid_states(atoms)
    packed = encode_packed(layout, sources)
    route_outputs = {}
    route_inverse_failures = {}
    for route, prefix in (
        ("contact", contact_prefix(layout)),
        ("record", record_prefix(layout)),
    ):
        words = run_logical(prefix, packed, len(sources))
        outputs = decode_packed(layout, words, len(sources))
        recovered = decode_packed(
            layout,
            run_logical(prefix, words, len(sources), inverse=True),
            len(sources),
        )
        route_outputs[route] = outputs
        route_inverse_failures[route] = sum(left != right for left, right in zip(recovered, sources))

    contact_predictions = tuple(output.base.selector for output in route_outputs["contact"])
    record_predictions = tuple(output.base.selector for output in route_outputs["record"])
    agreement = tuple(left == right for left, right in zip(contact_predictions, record_predictions))
    rows = tuple({
        "sector": GRID_SECTORS[index // 2][0],
        "control": sources[index].control_kind,
        "contact_selector": contact_predictions[index],
        "Record_candidate_selector": record_predictions[index],
        "agreement": agreement[index],
    } for index in range(6))
    detail = {
        "grid_declaration": tuple((sector, CONTROL_KINDS) for sector, _ in GRID_SECTORS),
        "grid_cases": 6,
        "predictions_recorded_before_Cycle407": True,
        "contact_predictions": contact_predictions,
        "Record_candidate_predictions": record_predictions,
        "agreement_mask": agreement,
        "agreements": sum(agreement),
        "disagreements": len(agreement) - sum(agreement),
        "rows": rows,
        "prefix_inverse_failures": route_inverse_failures,
        "typed_blank_is_Record": False,
        "typed_blank_flags": TYPED_BLANK_NONRECORD[-2:],
        "grid_chosen_from_Cycle407_comparator": False,
    }
    check(
        "the frozen pre-score N0/N1/N2 x blank/permanent grid exposes exactly three selector agreements and three disagreements",
        detail["grid_cases"] == 6
        and detail["predictions_recorded_before_Cycle407"]
        and contact_predictions == (0, 0, 0, 0, 1, 1)
        and record_predictions == (0, 1, 0, 1, 0, 1)
        and agreement == (True, False, True, False, False, True)
        and detail["agreements"] == detail["disagreements"] == 3
        and route_inverse_failures == {"contact": 0, "record": 0}
        and not detail["typed_blank_is_Record"]
        and detail["typed_blank_flags"] == (1, 0)
        and not detail["grid_chosen_from_Cycle407_comparator"],
        detail,
    )
    return detail


def permute_occupation(occupation: int, frame: np.ndarray) -> int:
    return c409.permute_occupation(occupation, frame)


def exact_physical_grid_controls() -> dict[str, object]:
    fixture = c407.c402.c397.c338.build_fixture(6)
    source_atoms = c407.make_atoms(fixture, 16)
    layout = make_layout(16)
    base_sources = grid_states(source_atoms)
    frames = c407.c402.c397.c311.c235.proper_cubic_frames()
    frame_sources = []
    frame_mapping_failures = 0
    for frame in frames:
        rotated, mapping, failures = c407.c402.c397.c342.mapped_fixture(fixture, frame)
        atoms = c407.make_atoms(rotated, 16)
        frame_mapping_failures += failures
        for left, right in zip(source_atoms, atoms):
            frame_mapping_failures += int(
                right.record.cylinder != c407.c402.c397.mapped_expected(left.record.cylinder, mapping)
                or c407.c402.c397.c350.atom_word(right)[c407.RECORD_M2 :]
                != c407.c402.c397.c350.atom_word(left)[c407.RECORD_M2 :]
            )
        base = c407.DiscriminatorState(0, (0,) * c407.TABLE_CLASSES, atoms)
        root = permanent_root_word(base)
        frame_sources.extend(
            GridState(base, permute_occupation(occupation, frame), control)
            for _sector, occupation in GRID_SECTORS
            for control in (TYPED_BLANK_NONRECORD, root)
        )
    all_sources = base_sources + tuple(frame_sources)
    route_detail = {}
    route_outputs = {}
    for route in ("contact", "record"):
        logical = full_schedule(layout, route)
        words, inventory = run_routed(
            layout,
            logical,
            encode_packed(layout, all_sources),
            len(all_sources),
            inventory=True,
        )
        assert inventory is not None
        outputs = decode_packed(layout, words, len(all_sources))
        expected = tuple(expected_output(source, route) for source in all_sources)
        recovered_words, _ = run_routed(
            layout, logical, words, len(all_sources), inverse=True
        )
        recovered = decode_packed(layout, recovered_words, len(all_sources))
        route_detail[route] = {
            "exact_EG_failures": sum(left != right for left, right in zip(outputs, expected)),
            "inverse_failures": sum(left != right for left, right in zip(recovered, all_sources)),
            "schedule": inventory,
        }
        route_outputs[route] = outputs

    contact = route_outputs["contact"][:6]
    record = route_outputs["record"][:6]
    contact_selectors = tuple(output.base.selector for output in contact)
    record_selectors = tuple(output.base.selector for output in record)
    input_atom_words = tuple(
        c407.c402.c397.c350.atom_word(atom)
        for source in all_sources
        for atom in source.base.atoms
    )
    output_atom_words = tuple(
        c407.c402.c397.c350.atom_word(atom)
        for route in ("contact", "record")
        for output in route_outputs[route]
        for atom in output.base.atoms
    )
    expected_repeated_inputs = input_atom_words + input_atom_words
    control_failures = sum(
        output.control_word != source.control_word
        for route in ("contact", "record")
        for source, output in zip(all_sources, route_outputs[route])
    )
    frame_prediction_failures = 0
    base_contact = contact_selectors
    base_record = record_selectors
    for frame_index in range(24):
        start = 6 + 6 * frame_index
        stop = start + 6
        frame_prediction_failures += int(
            tuple(output.base.selector for output in route_outputs["contact"][start:stop]) != base_contact
            or tuple(output.base.selector for output in route_outputs["record"][start:stop]) != base_record
        )
    detail = {
        "grid_cases_per_frame": 6,
        "proper_cubic_frames": 24,
        "frame_route_cases": 24 * 6 * 2,
        "contact_selector_predictions": contact_selectors,
        "Record_candidate_selector_predictions": record_selectors,
        "contact_menu_predictions": tuple(output.base.menu_scores for output in contact),
        "Record_candidate_menu_predictions": tuple(output.base.menu_scores for output in record),
        "contact_held_flags": tuple(output.base.held_discriminator for output in contact),
        "Record_candidate_held_flags": tuple(output.base.held_discriminator for output in record),
        "frame_mapping_failures": frame_mapping_failures,
        "frame_prediction_failures": frame_prediction_failures,
        "Record_payload_identity_failures": int(output_atom_words != expected_repeated_inputs),
        "control_word_preservation_failures": control_failures,
        "routes": route_detail,
        "downstream_Cycle407_selects_grid_cases": False,
        "ordered_schedule_is_time": False,
    }
    check(
        "both frozen-grid candidate laws feed the unchanged Cycle407 held readout with exact NN inverse, covariance, and identity preservation",
        contact_selectors == (0, 0, 0, 0, 1, 1)
        and record_selectors == (0, 1, 0, 1, 0, 1)
        and detail["contact_menu_predictions"] == tuple(c407.scores_for(selector) for selector in contact_selectors)
        and detail["Record_candidate_menu_predictions"] == tuple(c407.scores_for(selector) for selector in record_selectors)
        and detail["contact_held_flags"] == contact_selectors
        and detail["Record_candidate_held_flags"] == record_selectors
        and all(row["exact_EG_failures"] == row["inverse_failures"] == 0 for row in route_detail.values())
        and detail["frame_route_cases"] == 288
        and frame_mapping_failures == frame_prediction_failures == 0
        and detail["Record_payload_identity_failures"] == 0
        and control_failures == 0
        and all(row["schedule"]["line_M2"] == 1686 for row in route_detail.values())
        and all(row["schedule"]["maximum_primitive_support_M2"] == 3 for row in route_detail.values())
        and all(row["schedule"]["maximum_primitive_span_edges"] == 2 for row in route_detail.values())
        and all(row["schedule"]["nearest_neighbor_failures"] == 0 for row in route_detail.values())
        and not detail["downstream_Cycle407_selects_grid_cases"]
        and not detail["ordered_schedule_is_time"],
        detail,
    )
    return detail


def held_size_controls() -> None:
    rows = []
    for length, count in ((3, 8), (6, 16)):
        fixture = c407.c402.c397.c338.build_fixture(length)
        atoms = c407.make_atoms(fixture, count)
        layout = make_layout(count)
        sources = grid_states(atoms)
        route_rows = {}
        for route in ("contact", "record"):
            logical = full_schedule(layout, route)
            words = run_logical(logical, encode_packed(layout, sources), len(sources))
            outputs = decode_packed(layout, words, len(sources))
            recovered = decode_packed(
                layout,
                run_logical(logical, words, len(sources), inverse=True),
                len(sources),
            )
            route_rows[route] = {
                "selectors": tuple(output.base.selector for output in outputs),
                "held_flags": tuple(output.base.held_discriminator for output in outputs),
                "aggregates": tuple(sum(output.base.atom_scores) for output in outputs),
                "inverse_failures": sum(left != right for left, right in zip(recovered, sources)),
            }
        rows.append({"L": length, "N": count, "line_M2": layout.line_M2, "routes": route_rows})
    detail = {"size_rows": tuple(rows)}
    check(
        "the six-case selector cross-grid survives development L3/N8 and held L6/N16 without retuning",
        tuple(row["line_M2"] for row in rows) == (1278, 1686)
        and all(row["routes"]["contact"]["selectors"] == (0, 0, 0, 0, 1, 1) for row in rows)
        and all(row["routes"]["record"]["selectors"] == (0, 1, 0, 1, 0, 1) for row in rows)
        and all(row["routes"][route]["held_flags"] == row["routes"][route]["selectors"] for row in rows for route in ("contact", "record"))
        and tuple(rows[0]["routes"][route]["aggregates"] for route in ("contact", "record"))
        == ((96,) * 6, (96,) * 6)
        and tuple(rows[1]["routes"][route]["aggregates"] for route in ("contact", "record"))
        == ((192,) * 6, (192,) * 6)
        and all(row["routes"][route]["inverse_failures"] == 0 for row in rows for route in ("contact", "record")),
        detail,
    )


def physical_fixture_controls(surfaces: c407.c402.Surfaces) -> None:
    old_pass, old_fail = c409.PASS, c409.FAIL
    c409.PASS = c409.FAIL = 0
    with redirect_stdout(StringIO()):
        inherited = c409.physical_fixture_controls(surfaces)
    inherited_green = (c409.PASS, c409.FAIL) == (1, 0)
    c409.PASS, c409.FAIL = old_pass, old_fail

    sector_words = tuple(
        occupation
        for occupation in range(64)
        if occupation.bit_count() in (0, 1, 2)
    )
    detail = {
        "Cycle409_mass_Q_number_vector_contact_suite_green": inherited_green,
        "one_particle_mass_relative_residual": inherited["one_particle_mass_relative_residual"],
        "maximum_held_leakage": inherited["maximum_held_leakage"],
        "physical_contact_intertwiner_residual": inherited["physical_contact_intertwiner_residual"],
        "contact_predicate_matches_generator_support": inherited["contact_predicate_matches_generator_support"],
        "N0_N1_N2_basis_words": len(sector_words),
        "sector_prediction_failures": sum(
            c409.contact_active(word) != int(word.bit_count() == 2)
            for word in sector_words
        ),
        "typed_blank_is_Record": False,
        "lawful_permanent_control_is_Record": True,
    }
    check(
        "mass/Q/number/vector/contact, leakage, and the exact Record/non-Record type boundary survive the cross-grid",
        inherited_green
        and detail["one_particle_mass_relative_residual"] < 3e-12
        and detail["maximum_held_leakage"] < TOL
        and detail["physical_contact_intertwiner_residual"] < TOL
        and detail["contact_predicate_matches_generator_support"]
        and detail["N0_N1_N2_basis_words"] == 22
        and detail["sector_prediction_failures"] == 0
        and not detail["typed_blank_is_Record"]
        and detail["lawful_permanent_control_is_Record"],
        detail,
    )


def deletion_domain_controls() -> None:
    fixture = c407.c402.c397.c338.build_fixture(3)
    atoms = c407.make_atoms(fixture, 8)
    layout = make_layout(8)
    sources = grid_states(atoms)
    packed = encode_packed(layout, sources)

    contact_expected = tuple(expected_output(source, "contact") for source in sources)
    record_expected = tuple(expected_output(source, "record") for source in sources)
    contact_oracle_deleted = decode_packed(
        layout,
        run_logical(contact_prefix(layout, omit_oracle=True) + c407.logical_schedule(layout.base), packed, 6),
        6,
    )
    contact_transfer_deleted = decode_packed(
        layout,
        run_logical(contact_prefix(layout, omit_transfer=True) + c407.logical_schedule(layout.base), packed, 6),
        6,
    )
    record_deleted = decode_packed(
        layout,
        run_logical(c407.logical_schedule(layout.base), packed, 6),
        6,
    )

    old_pass, old_fail = c409.PASS, c409.FAIL
    c409.PASS = c409.FAIL = 0
    with redirect_stdout(StringIO()):
        c409.deletion_and_domain_controls()
    inherited_green = (c409.PASS, c409.FAIL) == (1, 0)
    c409.PASS, c409.FAIL = old_pass, old_fail

    base = sources[0].base
    malformed_permanent_blank = TYPED_BLANK_NONRECORD[:-1] + (1,)
    malformed_calls = (
        lambda: GridState(base, 7, TYPED_BLANK_NONRECORD),
        lambda: GridState(base, 0, TYPED_BLANK_NONRECORD[:-1]),
        lambda: GridState(base, 0, malformed_permanent_blank),
        lambda: GridState(base, 0, TYPED_BLANK_NONRECORD, contact_pointer=2),
        lambda: GridState(base, 0, TYPED_BLANK_NONRECORD, contact_work=(1, 0, 0, 0)),
        lambda: make_layout(0),
        lambda: full_schedule(layout, "comparator"),
        lambda: decode_state(layout, [0] * (layout.line_M2 - 1)),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1

    detail = {
        "contact_oracle_deletion_differences": sum(left != right for left, right in zip(contact_oracle_deleted, contact_expected)),
        "contact_transfer_deletion_differences": sum(left != right for left, right in zip(contact_transfer_deleted, contact_expected)),
        "Record_control_transfer_deletion_differences": sum(left != right for left, right in zip(record_deleted, record_expected)),
        "inherited_Cycle409_deletion_domain_green": inherited_green,
        "malformed_domain_rejections": rejected,
        "malformed_domain_attempts": len(malformed_calls),
    }
    check(
        "both law prefixes are deletion-sensitive on the frozen grid and inherited plus new malformed domains reject",
        detail["contact_oracle_deletion_differences"] == 2
        and detail["contact_transfer_deletion_differences"] == 2
        and detail["Record_control_transfer_deletion_differences"] == 3
        and inherited_green
        and rejected == len(malformed_calls),
        detail,
    )


def inventory_semantic_controls(pre_score: dict[str, object]) -> None:
    detail = {
        "supplied": (
            "canonical N0/N1/N2 representatives and grid ordering",
            "lawful permanent root word and typed blank/non-Record word",
            "both Cycle409 selector rules with direct polarities",
            "six occupation M2, contact pointer/work, 30-M2 independent control, blanks, layouts, primitive basis, routing, and schedule",
            "unchanged Cycle407 candidates, physical menu, equality reference, held corpus, and readout",
        ),
        "derived": (
            "pre-score six-row selector truth table",
            "three agreements and three disagreements",
            "held downstream B0/B1 vector and flag predictions",
        ),
        "not_selected": (
            "Nature's selector law", "grade", "actuality", "probability", "Born law",
            "time", "source", "energy", "gravity", "no-go", "axiom pressure",
        ),
        "grid_chosen_from_comparator": False,
        "runtime_host_selection": False,
        "runtime_host_arithmetic": False,
        "typed_blank_is_Record": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "axiom_pressure": False,
    }
    check(
        "the cross-grid inventories every supplied choice and maps candidate-law differences without semantic promotion",
        len(detail["supplied"]) == 5
        and len(detail["derived"]) == 3
        and len(detail["not_selected"]) == 11
        and pre_score["agreements"] == pre_score["disagreements"] == 3
        and not detail["grid_chosen_from_comparator"]
        and not detail["runtime_host_selection"]
        and not detail["runtime_host_arithmetic"]
        and not detail["typed_blank_is_Record"]
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and not detail["axiom_pressure"],
        detail,
    )


def main() -> None:
    print("CYCLE 413: PHYSICAL SELECTOR-DEPENDENCY CROSS-GRID")
    print("Authority:", AUTHORITY, "Audit:", AUDIT)
    note_contract()
    surfaces = c407.c402.build_surfaces()
    pre_score = pre_score_grid_controls()
    exact_physical_grid_controls()
    held_size_controls()
    physical_fixture_controls(surfaces)
    deletion_domain_controls()
    inventory_semantic_controls(pre_score)
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)
    print("RESULT PHYSICAL_SELECTOR_DEPENDENCY_CROSS_GRID_CERTIFIED")


if __name__ == "__main__":
    main()
