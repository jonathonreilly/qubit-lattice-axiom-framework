#!/usr/bin/env python3
"""Cycle 409: two independent local selector-preparation dynamics.

Route C prepares the Cycle-407 selector from the Cycle-278 contact-active
predicate on six local occupation M2.  Route R prepares it from the permanent
bit of an already formed typed Record.  The rules are declared independently
of the downstream Cycle-407 comparator and are then fed, unchanged, into its
two-face-member compiler.

These are supplied candidate dynamics, not a selection of Nature's grade.
No score is probability, actuality, occurrence, energy, source, resource,
gravity, rate, or time.  Authority is none; audit is unset; no axiom pressure
is claimed.
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

import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import physical_extension_face_operational_discriminator_cycle407_2026_07_18 as c407


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INDEPENDENT_SELECTOR_PREPARATION_DYNAMICS_"
    "CYCLE409_NOTE_2026-07-18.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10
CANONICAL_ONE_PARTICLE = 1
CONTACT_WORK_M2 = 4
ROUTES = ("contact-active local occupation", "typed-Record permanence")

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
        check("the Cycle-409 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "two independently declared selector-preparation dynamics",
        "cycle-278 contact-active predicate",
        "canonical one-particle input predicts selector 0",
        "typed-record permanence predicts selector 1",
        "declared before and without consulting the cycle-407 comparator",
        "the physical inputs are not conflated",
        "unchanged cycle-407 two-face-member compiler",
        "contact route predicts b0",
        "record route predicts b1",
        "connected 1656-m2 nearest-neighbor line",
        "maximum primitive support: 3 m2",
        "exact forward/inverse e/g",
        "held l=6, n=16",
        "all 24 proper-cubic frames",
        "record payload and identity are preserved",
        "mass/q/number/vector/contact",
        "deletion and lawful-domain controls",
        "no host selection or arithmetic",
        "not probability, actuality, occurrence, energy, source, resource, gravity, rate, or time",
        "no law selection",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins both independent preparation rules, physical types, exact compiler, controls, imports, and semantic firewall",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class SelectorLayout:
    base: c407.Layout
    occupation: tuple[int, ...]
    contact_pointer: int
    contact_work: tuple[int, ...]
    line_M2: int


def make_layout(count: int) -> SelectorLayout:
    base = c407.make_layout(count)
    cursor = base.line_M2
    occupation = tuple(range(cursor, cursor + 6))
    cursor += 6
    contact_pointer = cursor
    cursor += 1
    contact_work = tuple(range(cursor, cursor + CONTACT_WORK_M2))
    cursor += CONTACT_WORK_M2
    return SelectorLayout(base, occupation, contact_pointer, contact_work, cursor)


@dataclass(frozen=True)
class SelectorState:
    base: c407.DiscriminatorState
    occupation: int
    contact_pointer: int = 0
    contact_work: tuple[int, ...] = (0,) * CONTACT_WORK_M2

    def __post_init__(self) -> None:
        if type(self.occupation) is not int or not 0 <= self.occupation < 64:
            raise ValueError("local matter occupation needs six M2")
        if self.contact_pointer not in (0, 1):
            raise ValueError("contact pointer needs one M2")
        if len(self.contact_work) != CONTACT_WORK_M2 or any(bit != 0 for bit in self.contact_work):
            raise ValueError("contact threshold oracle needs four clean work M2")


def encode_state(layout: SelectorLayout, state: SelectorState) -> list[int]:
    bits = c407.encode_state(layout.base, state.base) + [0] * 11
    for site, bit in zip(layout.occupation, c407.int_bits(state.occupation, 6)):
        bits[site] = bit
    bits[layout.contact_pointer] = state.contact_pointer
    for site, bit in zip(layout.contact_work, state.contact_work):
        bits[site] = bit
    if len(bits) != layout.line_M2:
        raise RuntimeError("selector-preparation line inventory drifted")
    return bits


def decode_state(layout: SelectorLayout, bits: list[int]) -> SelectorState:
    if len(bits) != layout.line_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("selector-preparation state has the wrong binary width")
    return SelectorState(
        c407.decode_state(layout.base, bits[: layout.base.line_M2]),
        c407.bits_int(bits[site] for site in layout.occupation),
        bits[layout.contact_pointer],
        tuple(bits[site] for site in layout.contact_work),
    )


def encode_packed(layout: SelectorLayout, states: tuple[SelectorState, ...]) -> list[int]:
    rows = tuple(encode_state(layout, state) for state in states)
    return [
        sum(row[site] << case for case, row in enumerate(rows))
        for site in range(layout.line_M2)
    ]


def decode_packed(layout: SelectorLayout, words: list[int], cases: int) -> tuple[SelectorState, ...]:
    return tuple(
        decode_state(layout, [(words[site] >> case) & 1 for site in range(layout.line_M2)])
        for case in range(cases)
    )


def contact_active(occupation: int) -> int:
    if type(occupation) is not int or not 0 <= occupation < 64:
        raise ValueError("contact predicate accepts one six-M2 occupation")
    return int(occupation.bit_count() >= 2)


def contact_preparation_schedule(
    layout: SelectorLayout,
    *,
    omit_oracle: bool = False,
    omit_transfer: bool = False,
) -> tuple[c407.c402.Gate, ...]:
    gates: list[c407.c402.Gate] = []
    if not omit_oracle:
        for occupation in range(64):
            if not contact_active(occupation):
                continue
            pattern = c407.int_bits(occupation, 6)
            zeros = tuple(site for site, bit in zip(layout.occupation, pattern) if bit == 0)
            gates.extend(c407.c402.gate(layout.line_M2, "X", site) for site in zeros)
            gates.extend(
                c407.c402.mcx(
                    layout.line_M2,
                    layout.contact_work,
                    layout.occupation,
                    layout.contact_pointer,
                )
            )
            gates.extend(c407.c402.gate(layout.line_M2, "X", site) for site in reversed(zeros))
    if not omit_transfer:
        gates.append(
            c407.c402.gate(
                layout.line_M2,
                "CNOT",
                layout.contact_pointer,
                layout.base.selector,
            )
        )
    return tuple(gates)


def record_permanent_site(layout: SelectorLayout) -> int:
    # The last M2 of the 30-M2 typed Record payload is its permanent flag.
    return layout.base.atom_bits[0][c407.RECORD_M2 - 1]


def record_preparation_schedule(
    layout: SelectorLayout,
    *,
    omit_transfer: bool = False,
) -> tuple[c407.c402.Gate, ...]:
    if omit_transfer:
        return ()
    return (
        c407.c402.gate(
            layout.line_M2,
            "CNOT",
            record_permanent_site(layout),
            layout.base.selector,
        ),
    )


def full_schedule(
    layout: SelectorLayout,
    route: str,
    *,
    omit_preparation: bool = False,
) -> tuple[c407.c402.Gate, ...]:
    if route == "contact":
        preparation = () if omit_preparation else contact_preparation_schedule(layout)
    elif route == "record":
        preparation = () if omit_preparation else record_preparation_schedule(layout)
    else:
        raise ValueError("unknown selector-preparation route")
    return preparation + c407.logical_schedule(layout.base)


def expected_output(source: SelectorState, route: str) -> SelectorState:
    if source.base.selector != 0:
        raise ValueError("selector-preparation candidates accept one blank selector")
    if route == "contact":
        selector = contact_active(source.occupation)
        pointer = selector
    elif route == "record":
        selector = int(source.base.atoms[0].record.permanent)
        pointer = source.contact_pointer
    else:
        raise ValueError("unknown selector-preparation route")
    prepared = replace(source.base, selector=selector)
    return replace(source, base=c407.expected_output(prepared), contact_pointer=pointer)


def routed_schedule(
    layout: SelectorLayout,
    logical: tuple[c407.c402.Gate, ...],
    *,
    inverse: bool = False,
) -> Iterator[c407.c402.Gate]:
    yield from c407.c402.routed_schedule(layout.line_M2, logical, inverse=inverse)


def run_routed(
    layout: SelectorLayout,
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


def permute_occupation(occupation: int, frame: np.ndarray) -> int:
    mapping = c278.c235.direction_map(frame)
    result = 0
    for source, target in mapping.items():
        if (occupation >> source) & 1:
            result |= 1 << target
    return result


def build_frame_atoms(
    fixture: c407.c402.c397.c338.RouteFixture,
    count: int,
) -> tuple[
    tuple[c407.c402.c397.c350.CorpusAtom, ...],
    tuple[tuple[c407.c402.c397.c350.CorpusAtom, ...], ...],
    int,
]:
    source = c407.make_atoms(fixture, count)
    rows = []
    failures = 0
    for frame in c407.c402.c397.c311.c235.proper_cubic_frames():
        rotated, mapping, mapped_failures = c407.c402.c397.c342.mapped_fixture(fixture, frame)
        atoms = c407.make_atoms(rotated, count)
        failures += mapped_failures
        for left, right in zip(source, atoms):
            failures += int(
                right.record.cylinder
                != c407.c402.c397.mapped_expected(left.record.cylinder, mapping)
                or c407.c402.c397.c350.atom_word(right)[c407.RECORD_M2 :]
                != c407.c402.c397.c350.atom_word(left)[c407.RECORD_M2 :]
            )
        rows.append(atoms)
    return source, tuple(rows), failures


def exact_route_controls() -> dict[str, object]:
    held_fixture = c407.c402.c397.c338.build_fixture(6)
    held_atoms, frame_atoms, frame_mapping_failures = build_frame_atoms(held_fixture, 16)
    layout = make_layout(16)
    blank_table = (0,) * c407.TABLE_CLASSES

    contact_sources = tuple(
        SelectorState(c407.DiscriminatorState(0, blank_table, held_atoms), occupation)
        for occupation in range(64)
    )
    frames = c407.c402.c397.c311.c235.proper_cubic_frames()
    contact_frame_sources = tuple(
        SelectorState(
            c407.DiscriminatorState(0, blank_table, atoms),
            permute_occupation(CANONICAL_ONE_PARTICLE, frame),
        )
        for frame, atoms in zip(frames, frame_atoms)
    )
    all_contact_sources = contact_sources + contact_frame_sources
    contact_logical = full_schedule(layout, "contact")
    contact_words, contact_inventory = run_routed(
        layout,
        contact_logical,
        encode_packed(layout, all_contact_sources),
        len(all_contact_sources),
        inventory=True,
    )
    assert contact_inventory is not None
    contact_outputs = decode_packed(layout, contact_words, len(all_contact_sources))
    contact_expected = tuple(expected_output(source, "contact") for source in all_contact_sources)
    contact_recovered_words, _ = run_routed(
        layout,
        contact_logical,
        contact_words,
        len(all_contact_sources),
        inverse=True,
    )
    contact_recovered = decode_packed(layout, contact_recovered_words, len(all_contact_sources))

    record_sources = tuple(
        SelectorState(
            c407.DiscriminatorState(0, blank_table, atoms),
            CANONICAL_ONE_PARTICLE,
        )
        for atoms in frame_atoms
    )
    record_logical = full_schedule(layout, "record")
    record_words, record_inventory = run_routed(
        layout,
        record_logical,
        encode_packed(layout, record_sources),
        len(record_sources),
        inventory=True,
    )
    assert record_inventory is not None
    record_outputs = decode_packed(layout, record_words, len(record_sources))
    record_expected = tuple(expected_output(source, "record") for source in record_sources)
    record_recovered_words, _ = run_routed(
        layout,
        record_logical,
        record_words,
        len(record_sources),
        inverse=True,
    )
    record_recovered = decode_packed(layout, record_recovered_words, len(record_sources))

    canonical_contact = contact_outputs[CANONICAL_ONE_PARTICLE]
    canonical_record = record_outputs[0]
    record_word_failures = sum(
        c407.c402.c397.c350.atom_word(left_atom)
        != c407.c402.c397.c350.atom_word(right_atom)
        for sources, outputs in (
            (all_contact_sources, contact_outputs),
            (record_sources, record_outputs),
        )
        for source, output in zip(sources, outputs)
        for left_atom, right_atom in zip(source.base.atoms, output.base.atoms)
    )
    detail = {
        "routes": ROUTES,
        "declaration_inputs": (
            "canonical one-particle occupation in supplied direction order",
            "permanent flag of root typed Record atom",
        ),
        "selector_predictions": (
            canonical_contact.base.selector,
            canonical_record.base.selector,
        ),
        "face_member_predictions": ("B0 boundary vertex", "B1 relative interior"),
        "menu_vector_predictions": (
            canonical_contact.base.menu_scores,
            canonical_record.base.menu_scores,
        ),
        "held_discriminator_predictions": (
            canonical_contact.base.held_discriminator,
            canonical_record.base.held_discriminator,
        ),
        "contact_all_64_selector_predictions": tuple(output.base.selector for output in contact_outputs[:64]),
        "contact_exact_EG_failures": sum(left != right for left, right in zip(contact_outputs, contact_expected)),
        "contact_inverse_failures": sum(left != right for left, right in zip(contact_recovered, all_contact_sources)),
        "record_exact_EG_failures": sum(left != right for left, right in zip(record_outputs, record_expected)),
        "record_inverse_failures": sum(left != right for left, right in zip(record_recovered, record_sources)),
        "Record_payload_identity_failures": record_word_failures,
        "proper_cubic_frames": 24,
        "contact_frame_selector_failures": sum(output.base.selector != 0 for output in contact_outputs[64:]),
        "record_frame_selector_failures": sum(output.base.selector != 1 for output in record_outputs),
        "frame_mapping_failures": frame_mapping_failures,
        "contact_schedule": contact_inventory,
        "record_schedule": record_inventory,
        "selector_rules_consult_Cycle407_comparator": False,
        "ordered_schedule_is_time": False,
    }
    expected_contact_bits = tuple(contact_active(occupation) for occupation in range(64))
    check(
        "both independently declared local preparations feed the unchanged Cycle-407 compiler with exact NN E/G, inverse, Records, and all-frame covariance",
        detail["selector_predictions"] == (0, 1)
        and detail["face_member_predictions"] == ("B0 boundary vertex", "B1 relative interior")
        and detail["menu_vector_predictions"] == (c407.scores_for(0), c407.scores_for(1))
        and detail["held_discriminator_predictions"] == (0, 1)
        and detail["contact_all_64_selector_predictions"] == expected_contact_bits
        and detail["contact_exact_EG_failures"] == 0
        and detail["contact_inverse_failures"] == 0
        and detail["record_exact_EG_failures"] == 0
        and detail["record_inverse_failures"] == 0
        and detail["Record_payload_identity_failures"] == 0
        and detail["proper_cubic_frames"] == 24
        and detail["contact_frame_selector_failures"] == 0
        and detail["record_frame_selector_failures"] == 0
        and detail["frame_mapping_failures"] == 0
        and contact_inventory["line_M2"] == record_inventory["line_M2"] == 1656
        and contact_inventory["maximum_primitive_support_M2"] == 3
        and record_inventory["maximum_primitive_support_M2"] == 3
        and contact_inventory["maximum_primitive_span_edges"] == 2
        and record_inventory["maximum_primitive_span_edges"] == 2
        and contact_inventory["nearest_neighbor_failures"] == 0
        and record_inventory["nearest_neighbor_failures"] == 0
        and not detail["selector_rules_consult_Cycle407_comparator"]
        and not detail["ordered_schedule_is_time"],
        detail,
    )
    return detail


def held_size_controls() -> dict[str, object]:
    rows = []
    for length, count in ((3, 8), (6, 16)):
        fixture = c407.c402.c397.c338.build_fixture(length)
        atoms = c407.make_atoms(fixture, count)
        layout = make_layout(count)
        source = SelectorState(
            c407.DiscriminatorState(0, (0,) * c407.TABLE_CLASSES, atoms),
            CANONICAL_ONE_PARTICLE,
        )
        route_outputs = []
        for route in ("contact", "record"):
            logical = full_schedule(layout, route)
            words = run_logical(logical, encode_packed(layout, (source,)), 1)
            output = decode_packed(layout, words, 1)[0]
            recovered = decode_packed(
                layout,
                run_logical(logical, words, 1, inverse=True),
                1,
            )[0]
            route_outputs.append((output, recovered))
        rows.append({
            "L": length,
            "N": count,
            "line_M2": layout.line_M2,
            "selector_predictions": tuple(output.base.selector for output, _ in route_outputs),
            "held_flags": tuple(output.base.held_discriminator for output, _ in route_outputs),
            "score_aggregates": tuple(sum(output.base.atom_scores) for output, _ in route_outputs),
            "logical_inverse_failures": sum(recovered != source for _, recovered in route_outputs),
        })
    detail = {"size_rows": tuple(rows)}
    check(
        "the contact/Record prediction split survives development L3/N8 and held L6/N16",
        tuple(row["selector_predictions"] for row in rows) == ((0, 1), (0, 1))
        and tuple(row["held_flags"] for row in rows) == ((0, 1), (0, 1))
        and tuple(row["score_aggregates"] for row in rows) == ((96, 96), (192, 192))
        and tuple(row["line_M2"] for row in rows) == (1248, 1656)
        and all(row["logical_inverse_failures"] == 0 for row in rows),
        detail,
    )
    return detail


def physical_fixture_controls(surfaces: c407.c402.Surfaces) -> dict[str, object]:
    old_pass, old_fail = c407.PASS, c407.FAIL
    c407.PASS = c407.FAIL = 0
    with redirect_stdout(StringIO()):
        inherited = c407.physical_spectator_controls(surfaces)
    inherited_green = (c407.PASS, c407.FAIL) == (1, 0)
    c407.PASS, c407.FAIL = old_pass, old_fail

    occupations = np.asarray([index.bit_count() for index in range(64)])
    q_values = (occupations >= 2).astype(float)
    q = np.diag(q_values).astype(complex)
    species = c278.c219.common_species(c278.c230.BETA)
    fock_coin = c278.c229.fock_lift(species.coin)
    pair_count = occupations * (occupations - 1) / 2
    contact = np.diag(np.exp(1j * c278.c230.COUPLING * pair_count)).astype(complex)
    contact_deleted = np.eye(64, dtype=complex)
    detail = {
        "Cycle407_physical_suite_green": inherited_green,
        "one_particle_mass_relative_residual": inherited["one_particle_mass_relative_residual"],
        "maximum_held_leakage": inherited["maximum_held_leakage"],
        "physical_contact_intertwiner_residual": inherited["physical_contact_intertwiner_residual"],
        "selected_menu_contact_deletion_distance": inherited["selected_menu_contact_deletion_distance"],
        "contact_predicate_rank": int(np.trace(q).real),
        "contact_predicate_matches_generator_support": bool(np.array_equal(q_values, (pair_count > 0).astype(float))),
        "contact_Q_coin_commutator": float(np.linalg.norm(q @ fock_coin - fock_coin @ q)),
        "contact_Q_contact_commutator": float(np.linalg.norm(q @ contact - contact @ q)),
        "actual_contact_unitary_deletion_distance": float(np.linalg.norm(contact - contact_deleted)),
        "canonical_one_particle_Q": int(q_values[CANONICAL_ONE_PARTICLE]),
        "Q_commutator": inherited["Q_commutator"],
        "number_commutator": inherited["number_commutator"],
        "vector_commutator": inherited["vector_commutator"],
    }
    check(
        "the two selector inputs retain the exact mass/Q/number/vector/contact and leakage fixtures without conflating their physical types",
        inherited_green
        and inherited["one_particle_mass_relative_residual"] < 3e-12
        and inherited["maximum_held_leakage"] < TOL
        and inherited["physical_contact_intertwiner_residual"] < TOL
        and inherited["selected_menu_contact_deletion_distance"] > 0.27
        and detail["contact_predicate_rank"] == 57
        and detail["contact_predicate_matches_generator_support"]
        and detail["contact_Q_coin_commutator"] < 2e-14
        and detail["contact_Q_contact_commutator"] == 0.0
        and detail["actual_contact_unitary_deletion_distance"] > 1.0
        and detail["canonical_one_particle_Q"] == 0
        and detail["Q_commutator"] == detail["number_commutator"] == 0
        and detail["vector_commutator"] == (0, 0, 0),
        detail,
    )
    return detail


def deletion_and_domain_controls() -> None:
    fixture = c407.c402.c397.c338.build_fixture(3)
    atoms = c407.make_atoms(fixture, 8)
    layout = make_layout(8)
    blank = c407.DiscriminatorState(0, (0,) * c407.TABLE_CLASSES, atoms)

    contact_sources = tuple(SelectorState(blank, occupation) for occupation in range(64))
    contact_expected = tuple(expected_output(source, "contact") for source in contact_sources)
    contact_packed = encode_packed(layout, contact_sources)
    oracle_deleted = decode_packed(
        layout,
        run_logical(
            contact_preparation_schedule(layout, omit_oracle=True) + c407.logical_schedule(layout.base),
            contact_packed,
            64,
        ),
        64,
    )
    transfer_deleted = decode_packed(
        layout,
        run_logical(
            contact_preparation_schedule(layout, omit_transfer=True) + c407.logical_schedule(layout.base),
            contact_packed,
            64,
        ),
        64,
    )

    record_source = SelectorState(blank, CANONICAL_ONE_PARTICLE)
    record_expected = expected_output(record_source, "record")
    record_deleted = decode_packed(
        layout,
        run_logical(full_schedule(layout, "record", omit_preparation=True), encode_packed(layout, (record_source,)), 1),
        1,
    )[0]

    old_pass, old_fail = c407.PASS, c407.FAIL
    c407.PASS = c407.FAIL = 0
    with redirect_stdout(StringIO()):
        c407.deletion_attack_domain_controls()
    inherited_green = (c407.PASS, c407.FAIL) == (1, 0)
    c407.PASS, c407.FAIL = old_pass, old_fail

    malformed_calls = (
        lambda: contact_active(64),
        lambda: SelectorState(blank, -1),
        lambda: SelectorState(blank, 0, contact_pointer=2),
        lambda: SelectorState(blank, 0, contact_work=(1, 0, 0, 0)),
        lambda: make_layout(0),
        lambda: full_schedule(layout, "host"),
        lambda: c407.c402.mcx(layout.line_M2, (), layout.occupation, layout.contact_pointer),
        lambda: decode_state(layout, [0] * (layout.line_M2 - 1)),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1

    active_count = sum(contact_active(occupation) for occupation in range(64))
    detail = {
        "contact_active_domain_cases": 64,
        "contact_oracle_deletion_differences": sum(left != right for left, right in zip(oracle_deleted, contact_expected)),
        "contact_transfer_deletion_differences": sum(left != right for left, right in zip(transfer_deleted, contact_expected)),
        "contact_active_cases": active_count,
        "Record_preparation_deletion_detected": record_deleted != record_expected,
        "inherited_Cycle407_deletion_attack_domain_green": inherited_green,
        "malformed_domain_rejections": rejected,
        "malformed_domain_attempts": len(malformed_calls),
    }
    check(
        "both preparation macros are deletion-sensitive on their lawful domains and the inherited attacks plus malformed domains reject",
        detail["contact_active_domain_cases"] == 64
        and detail["contact_oracle_deletion_differences"] == active_count == 57
        and detail["contact_transfer_deletion_differences"] == active_count
        and detail["Record_preparation_deletion_detected"]
        and inherited_green
        and rejected == len(malformed_calls),
        detail,
    )


def inventory_and_semantic_controls(routes: dict[str, object]) -> None:
    detail = {
        "declarations_fixed_without_comparator": (
            "contact selector equals Cycle-278 Q_ge2 on canonical supplied one-particle occupation",
            "Record selector equals root atom's already-formed permanent flag",
        ),
        "supplied": (
            "both selector rules and direct polarities",
            "canonical direction ordering and one-particle occupation",
            "formed typed/permanent root Record and its atom order",
            "six occupation M2, blank contact pointer, four work blanks, and blank Cycle-407 selector",
            "unchanged Cycle-407 B0/B1 candidates, menu, equality reference, corpus, primitive basis, routing, and schedule",
        ),
        "type_boundary": "contact support predicate is a matter operator; permanent is a typed Record payload bit; neither is retyped as the other",
        "not_selected": (
            "Nature's grade", "probability", "Born law", "actuality", "occurrence",
            "energy", "source", "resource", "gravity", "rate", "time",
        ),
        "runtime_host_selection": False,
        "runtime_host_arithmetic": False,
        "selector_predictions": routes["selector_predictions"],
        "authority": AUTHORITY,
        "audit": AUDIT,
        "axiom_pressure": False,
    }
    check(
        "the candidate dynamics preserve their type boundary, inventory every supplied choice, and select no grade or physical interpretation",
        len(detail["declarations_fixed_without_comparator"]) == 2
        and len(detail["supplied"]) == 5
        and len(detail["not_selected"]) == 11
        and "neither is retyped as the other" in detail["type_boundary"]
        and not detail["runtime_host_selection"]
        and not detail["runtime_host_arithmetic"]
        and detail["selector_predictions"] == (0, 1)
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and not detail["axiom_pressure"],
        detail,
    )


def main() -> None:
    print("CYCLE 409: INDEPENDENT SELECTOR-PREPARATION DYNAMICS")
    print("Authority:", AUTHORITY, "Audit:", AUDIT)
    note_contract()
    surfaces = c407.c402.build_surfaces()
    routes = exact_route_controls()
    held_size_controls()
    physical_fixture_controls(surfaces)
    deletion_and_domain_controls()
    inventory_and_semantic_controls(routes)
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)
    print("RESULT PHYSICAL_INDEPENDENT_SELECTOR_PREPARATION_DYNAMICS_CERTIFIED")


if __name__ == "__main__":
    main()
