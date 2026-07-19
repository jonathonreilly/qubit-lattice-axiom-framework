#!/usr/bin/env python3
"""Cycle 407: physical operational discriminator on the Cycle-402 B face.

Two exact nonnegative extensions of the same mapped nine-class B table are
prepared and admitted at common denominator 96.  A predeclared, landed
Cycle-398 fine menu gives distinct eight-score vectors.  One reversible
nearest-neighbor M2 circuit prepares, admits, scores, and compares those
vectors while preserving a held typed-Record corpus.

The selector, both witnesses, menu, equality reference, corpus, and schedule
remain supplied.  No grade is probability, actuality, occurrence, frequency,
energy, source, resource, gravity, rate, or time.  Authority is none; audit is
unset; no law is selected and no axiom pressure is claimed.
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_exact_registry_extension_bridge_cycle402_2026_07_18 as c402


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EXTENSION_FACE_OPERATIONAL_DISCRIMINATOR_"
    "CYCLE407_NOTE_2026-07-18.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10

# The Cycle-402 denominator-48 vertex, rescaled exactly to denominator 96.
B0_96 = tuple(2 * value for value in c402.B_VERTEX_48)
# The Cycle-402 denominator-96 relative-interior witness.
B1_96 = c402.B_INTERIOR_96
CANDIDATES = (B0_96, B1_96)

# Independent interface declaration: first installed physical presentation in
# supplied Cycle-398 order.  No candidate grade is consulted by this rule.
PHYSICAL_MENU_INDEX = 0
PHYSICAL_MENU_CLASSES = tuple(range(8))
REFERENCE_SELECTOR = 1
GRADE_M2 = 7
TABLE_CLASSES = 55
TABLE_M2 = TABLE_CLASSES * GRADE_M2
WORK_M2 = TABLE_M2 - 1
RECORD_M2 = c402.c397.c350.RECORD_M2
ATOM_M2 = c402.c397.c350.ATOM_M2

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
        check("the Cycle-407 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "two exact nonnegative b extensions at common denominator 96",
        "first installed physical fine menu in supplied cycle-398 order",
        "no grade was consulted by the interface-selection rule",
        "(12,0,14,0,22,6,0,42)",
        "(12,0,14,0,7,21,15,27)",
        "(0,0,0,0,-15,15,15,-15)",
        "connected 1645-m2 nearest-neighbor line",
        "maximum primitive support: 3 m2",
        "exact forward/inverse e/g",
        "held l=6, n=16",
        "all 24 proper-cubic frames",
        "record payload and identity are preserved",
        "mass/q/number/vector/contact",
        "no host selection or arithmetic",
        "selector and both witnesses remain supplied",
        "the score is not probability",
        "not actuality, occurrence, or frequency",
        "not energy, source, resource, gravity, rate, or time",
        "authority: none",
        "audit: unset",
        "no law selection",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the independent physical discriminator, exact compiler, controls, imports, and semantic firewall",
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


@dataclass(frozen=True)
class Layout:
    count: int
    selector: int
    table_bits: tuple[tuple[int, ...], ...]
    admitted: int
    work: tuple[int, ...]
    menu_scores: tuple[tuple[int, ...], ...]
    menu_discriminator: int
    atom_bits: tuple[tuple[int, ...], ...]
    atom_scores: tuple[tuple[int, ...], ...]
    atom_valid: tuple[int, ...]
    held_discriminator: int
    line_M2: int


def make_layout(count: int) -> Layout:
    if type(count) is not int or not 0 < count <= 16:
        raise ValueError("the discriminator corpus needs 1..16 typed atoms")
    cursor = 0
    selector = cursor
    cursor += 1
    table_bits = tuple(
        tuple(range(cursor + GRADE_M2 * klass, cursor + GRADE_M2 * (klass + 1)))
        for klass in range(TABLE_CLASSES)
    )
    cursor += TABLE_M2
    admitted = cursor
    cursor += 1
    work = tuple(range(cursor, cursor + WORK_M2))
    cursor += WORK_M2
    menu_scores = tuple(
        tuple(range(cursor + GRADE_M2 * outcome, cursor + GRADE_M2 * (outcome + 1)))
        for outcome in range(8)
    )
    cursor += 8 * GRADE_M2
    menu_discriminator = cursor
    cursor += 1
    atoms = []
    scores = []
    valids = []
    for _ in range(count):
        atoms.append(tuple(range(cursor, cursor + ATOM_M2)))
        cursor += ATOM_M2
        scores.append(tuple(range(cursor, cursor + GRADE_M2)))
        cursor += GRADE_M2
        valids.append(cursor)
        cursor += 1
    held_discriminator = cursor
    cursor += 1
    return Layout(
        count,
        selector,
        table_bits,
        admitted,
        work,
        menu_scores,
        menu_discriminator,
        tuple(atoms),
        tuple(scores),
        tuple(valids),
        held_discriminator,
        cursor,
    )


@dataclass(frozen=True)
class DiscriminatorState:
    selector: int
    table: tuple[int, ...]
    atoms: tuple[c402.c397.c350.CorpusAtom, ...]
    admitted: int = 0
    menu_scores: tuple[int, ...] = (0,) * 8
    menu_discriminator: int = 0
    atom_scores: tuple[int, ...] = ()
    atom_valid: tuple[int, ...] = ()
    held_discriminator: int = 0
    work: tuple[int, ...] = (0,) * WORK_M2

    def __post_init__(self) -> None:
        if self.selector not in (0, 1):
            raise ValueError("candidate selector needs one M2")
        if len(self.table) != TABLE_CLASSES or any(
            type(value) is not int or not 0 <= value < 128 for value in self.table
        ):
            raise ValueError("candidate extension needs 55 seven-M2 words")
        if not self.atoms or len(self.atoms) > 16:
            raise ValueError("one nonempty at-most-16 atom corpus is required")
        for ordinal, atom in enumerate(self.atoms):
            if c402.c397.c376.atom_from_word(c402.c397.c350.atom_word(atom)) != atom:
                raise ValueError("one typed Record atom failed its exact codec")
            if (
                atom.preparation,
                atom.program,
                atom.fine_pointer,
                atom.trial,
                atom.use,
            ) != (ordinal % 4, 0, ordinal % 8, ordinal, ordinal // 8):
                raise ValueError("atom tags leave the supplied physical-menu binding")
        if self.admitted not in (0, 1):
            raise ValueError("admission needs one M2")
        if len(self.menu_scores) != 8 or any(
            type(value) is not int or not 0 <= value < 128 for value in self.menu_scores
        ):
            raise ValueError("the physical menu needs eight seven-M2 scores")
        if self.menu_discriminator not in (0, 1):
            raise ValueError("the menu comparator needs one M2")
        count = len(self.atoms)
        if not self.atom_scores:
            object.__setattr__(self, "atom_scores", (0,) * count)
        if not self.atom_valid:
            object.__setattr__(self, "atom_valid", (0,) * count)
        if len(self.atom_scores) != count or any(
            type(value) is not int or not 0 <= value < 128 for value in self.atom_scores
        ):
            raise ValueError("each Record atom needs one seven-M2 score")
        if len(self.atom_valid) != count or any(value not in (0, 1) for value in self.atom_valid):
            raise ValueError("each Record tag needs one validity M2")
        if self.held_discriminator not in (0, 1):
            raise ValueError("the held comparator needs one M2")
        if len(self.work) != WORK_M2 or any(bit != 0 for bit in self.work):
            raise ValueError("the equality compiler needs 384 clean work M2")


def make_atoms(fixture: c402.c397.c338.RouteFixture, count: int) -> tuple[c402.c397.c350.CorpusAtom, ...]:
    cylinders = c402.c397.c342.make_cylinder_chain(fixture, 0, count)
    atoms = []
    for ordinal, cylinder in enumerate(cylinders):
        atom = c402.c397.c350.form_atom(
            fixture,
            cylinder,
            preparation=ordinal % 4,
            program=0,
            fine_pointer=ordinal % 8,
            trial=ordinal,
            use=ordinal // 8,
        )
        if atom is None:
            raise RuntimeError("one declared typed Record atom failed formation")
        atoms.append(atom)
    return tuple(atoms)


def encode_state(layout: Layout, state: DiscriminatorState) -> list[int]:
    if len(state.atoms) != layout.count:
        raise ValueError("state corpus and line layout disagree")
    bits = [0] * layout.line_M2
    bits[layout.selector] = state.selector
    for register, value in zip(layout.table_bits, state.table):
        for site, bit in zip(register, int_bits(value, GRADE_M2)):
            bits[site] = bit
    bits[layout.admitted] = state.admitted
    for site, bit in zip(layout.work, state.work):
        bits[site] = bit
    for register, value in zip(layout.menu_scores, state.menu_scores):
        for site, bit in zip(register, int_bits(value, GRADE_M2)):
            bits[site] = bit
    bits[layout.menu_discriminator] = state.menu_discriminator
    for atom_register, score_register, valid_site, atom, score, valid in zip(
        layout.atom_bits,
        layout.atom_scores,
        layout.atom_valid,
        state.atoms,
        state.atom_scores,
        state.atom_valid,
    ):
        for site, bit in zip(atom_register, c402.c397.c350.atom_word(atom)):
            bits[site] = bit
        for site, bit in zip(score_register, int_bits(score, GRADE_M2)):
            bits[site] = bit
        bits[valid_site] = valid
    bits[layout.held_discriminator] = state.held_discriminator
    return bits


def decode_state(layout: Layout, bits: list[int]) -> DiscriminatorState:
    if len(bits) != layout.line_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("discriminator state has the wrong exact binary width")
    atoms = tuple(
        c402.c397.c376.atom_from_word(tuple(bits[site] for site in register))
        for register in layout.atom_bits
    )
    return DiscriminatorState(
        selector=bits[layout.selector],
        table=tuple(bits_int(bits[site] for site in register) for register in layout.table_bits),
        atoms=atoms,
        admitted=bits[layout.admitted],
        menu_scores=tuple(bits_int(bits[site] for site in register) for register in layout.menu_scores),
        menu_discriminator=bits[layout.menu_discriminator],
        atom_scores=tuple(bits_int(bits[site] for site in register) for register in layout.atom_scores),
        atom_valid=tuple(bits[site] for site in layout.atom_valid),
        held_discriminator=bits[layout.held_discriminator],
        work=tuple(bits[site] for site in layout.work),
    )


def encode_packed(layout: Layout, states: tuple[DiscriminatorState, ...]) -> list[int]:
    rows = tuple(encode_state(layout, state) for state in states)
    return [
        sum(row[site] << case for case, row in enumerate(rows))
        for site in range(layout.line_M2)
    ]


def decode_packed(layout: Layout, words: list[int], cases: int) -> tuple[DiscriminatorState, ...]:
    return tuple(
        decode_state(layout, [(words[site] >> case) & 1 for site in range(layout.line_M2)])
        for case in range(cases)
    )


def scores_for(selector: int) -> tuple[int, ...]:
    return tuple(CANDIDATES[selector][klass] for klass in PHYSICAL_MENU_CLASSES)


def expected_output(source: DiscriminatorState) -> DiscriminatorState:
    scores = scores_for(source.selector)
    atom_scores = tuple(scores[ordinal % 8] for ordinal in range(len(source.atoms)))
    return replace(
        source,
        table=CANDIDATES[source.selector],
        admitted=1,
        menu_scores=scores,
        menu_discriminator=source.selector,
        atom_scores=atom_scores,
        atom_valid=(1,) * len(source.atoms),
        held_discriminator=source.selector,
    )


def logical_schedule(
    layout: Layout,
    *,
    omit_loader: bool = False,
    omit_admission: bool = False,
    omit_menu: bool = False,
    omit_record: bool = False,
    omit_menu_comparator: bool = False,
    omit_held_comparator: bool = False,
) -> tuple[c402.Gate, ...]:
    gates: list[c402.Gate] = []
    flat = tuple(site for register in layout.table_bits for site in register)
    bit_rows = tuple(
        tuple(bit for value in candidate for bit in int_bits(value, GRADE_M2))
        for candidate in CANDIDATES
    )

    # Reversible selector-controlled preparation from a blank table.  This is
    # fixed bit loading; there is no runtime host arithmetic or selection.
    if not omit_loader:
        for site, left, right in zip(flat, bit_rows[0], bit_rows[1]):
            if left:
                gates.append(c402.gate(layout.line_M2, "X", site))
            if left != right:
                gates.append(c402.gate(layout.line_M2, "CNOT", layout.selector, site))

    # Each candidate has its own exact local equality-admission branch.
    if not omit_admission:
        for selector, expected in enumerate(bit_rows):
            if selector == 0:
                gates.append(c402.gate(layout.line_M2, "X", layout.selector))
            zeros = tuple(site for site, bit in zip(flat, expected) if bit == 0)
            gates.extend(c402.gate(layout.line_M2, "X", site) for site in zeros)
            gates.extend(
                c402.mcx(
                    layout.line_M2,
                    layout.work,
                    (layout.selector,) + flat,
                    layout.admitted,
                )
            )
            gates.extend(c402.gate(layout.line_M2, "X", site) for site in reversed(zeros))
            if selector == 0:
                gates.append(c402.gate(layout.line_M2, "X", layout.selector))

    # Copy the full predeclared physical menu score vector from the admitted
    # table.  The effect-class row is supplied by the actual Cycle-398 menu.
    if not omit_menu:
        for outcome, klass in enumerate(PHYSICAL_MENU_CLASSES):
            for bit in range(GRADE_M2):
                gates.append(
                    c402.gate(
                        layout.line_M2,
                        "TOFFOLI",
                        layout.admitted,
                        layout.table_bits[klass][bit],
                        layout.menu_scores[outcome][bit],
                    )
                )

    if not omit_menu_comparator:
        reference = tuple(bit for value in scores_for(REFERENCE_SELECTOR) for bit in int_bits(value, GRADE_M2))
        score_sites = tuple(site for register in layout.menu_scores for site in register)
        zeros = tuple(site for site, bit in zip(score_sites, reference) if bit == 0)
        gates.extend(c402.gate(layout.line_M2, "X", site) for site in zeros)
        gates.extend(
            c402.mcx(
                layout.line_M2,
                layout.work,
                (layout.admitted,) + score_sites,
                layout.menu_discriminator,
            )
        )
        gates.extend(c402.gate(layout.line_M2, "X", site) for site in reversed(zeros))

    # Typed Records are spectators.  Only the six supplied program/pointer tag
    # M2 and the extracted menu word control each attached score.
    if not omit_record:
        for ordinal, (atom_register, score_register, valid_site) in enumerate(
            zip(layout.atom_bits, layout.atom_scores, layout.atom_valid)
        ):
            pointer = ordinal % 8
            program_sites = atom_register[RECORD_M2 + 2 : RECORD_M2 + 5]
            pointer_sites = atom_register[RECORD_M2 + 5 : RECORD_M2 + 8]
            tag_sites = program_sites + pointer_sites
            tag_pattern = int_bits(0, 3) + int_bits(pointer, 3)
            zeros = tuple(site for site, bit in zip(tag_sites, tag_pattern) if bit == 0)
            gates.extend(c402.gate(layout.line_M2, "X", site) for site in zeros)
            for bit in range(GRADE_M2):
                gates.extend(
                    c402.mcx(
                        layout.line_M2,
                        layout.work,
                        (layout.admitted,) + tag_sites + (layout.menu_scores[pointer][bit],),
                        score_register[bit],
                    )
                )
            gates.extend(
                c402.mcx(
                    layout.line_M2,
                    layout.work,
                    (layout.admitted,) + tag_sites,
                    valid_site,
                )
            )
            gates.extend(c402.gate(layout.line_M2, "X", site) for site in reversed(zeros))

    if not omit_held_comparator:
        gates.extend(
            c402.mcx(
                layout.line_M2,
                layout.work,
                (layout.menu_discriminator,) + layout.atom_valid,
                layout.held_discriminator,
            )
        )
    return tuple(gates)


def routed_schedule(layout: Layout, logical: tuple[c402.Gate, ...], *, inverse: bool = False) -> Iterator[c402.Gate]:
    yield from c402.routed_schedule(layout.line_M2, logical, inverse=inverse)


def run_routed(
    layout: Layout,
    logical: tuple[c402.Gate, ...],
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
    for index, primitive in enumerate(routed_schedule(layout, logical, inverse=inverse)):
        if skip_index is not None and index == skip_index:
            continue
        c402.apply_packed(words, primitive, mask)
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


def run_logical(layout: Layout, logical: tuple[c402.Gate, ...], words: list[int], cases: int) -> list[int]:
    result = words.copy()
    mask = (1 << cases) - 1
    for primitive in logical:
        c402.apply_packed(result, primitive, mask)
    return result


def candidate_and_interface_controls(surfaces: c402.Surfaces) -> dict[str, object]:
    incidence = np.asarray(surfaces.installed.incidence, dtype=int)
    candidate_totals = tuple(tuple(int(value) for value in incidence @ np.asarray(candidate, dtype=int)) for candidate in CANDIDATES)
    menu = surfaces.installed.menus[PHYSICAL_MENU_INDEX]
    classes = tuple(surfaces.installed.menu_classes[PHYSICAL_MENU_INDEX])
    vectors = tuple(tuple(candidate[klass] for klass in classes) for candidate in CANDIDATES)
    difference = tuple(right - left for left, right in zip(*vectors))
    detail = {
        "candidate_denominators": (96, 96),
        "candidate_minima": tuple(min(candidate) for candidate in CANDIDATES),
        "candidate_zero_counts": tuple(candidate.count(0) for candidate in CANDIDATES),
        "all_98_menu_totals": tuple(tuple(sorted(set(totals))) for totals in candidate_totals),
        "mapped_values": tuple(tuple(candidate[index] for index in c402.MAPPING) for candidate in CANDIDATES),
        "mapped_reference": tuple(2 * value for value in c402.c395.TABLES[1]),
        "selection_rule": "first installed physical fine menu in supplied Cycle-398 order; no grade consulted",
        "menu_name": menu.name,
        "menu_provenance": menu.provenance,
        "menu_surface": menu.surface,
        "menu_program": menu.program_index,
        "menu_classes": classes,
        "mapped_class_overlap": tuple(sorted(set(classes) & set(c402.MAPPING))),
        "score_vectors": vectors,
        "B1_minus_B0": difference,
        "vector_aggregates": tuple(sum(vector) for vector in vectors),
        "L1_distance": sum(abs(value) for value in difference),
        "distinct_outcomes": tuple(index for index, value in enumerate(difference) if value),
    }
    check(
        "two exact nonnegative common-denominator B extensions are operationally distinct on one independently declared actual physical menu",
        all(len(set(totals)) == 1 and totals[0] == 96 for totals in candidate_totals)
        and detail["mapped_values"] == (detail["mapped_reference"],) * 2
        and detail["candidate_minima"] == (0, 0)
        and menu.name == "cycle321-canonical/0/four-component axis/fine"
        and menu.provenance == "landed-in-pinned-main-base Cycle321/323 carrier"
        and menu.surface == "fine"
        and menu.program_index == 0
        and classes == PHYSICAL_MENU_CLASSES
        and detail["mapped_class_overlap"] == ()
        and vectors == ((12, 0, 14, 0, 22, 6, 0, 42), (12, 0, 14, 0, 7, 21, 15, 27))
        and difference == (0, 0, 0, 0, -15, 15, 15, -15)
        and detail["vector_aggregates"] == (96, 96)
        and detail["L1_distance"] == 60
        and detail["distinct_outcomes"] == (4, 5, 6, 7),
        detail,
    )
    return detail


def compiler_and_frame_controls() -> dict[str, object]:
    held_fixture = c402.c397.c338.build_fixture(6)
    held_atoms = make_atoms(held_fixture, 16)
    held_layout = make_layout(16)
    held_logical = logical_schedule(held_layout)
    held_sources = tuple(
        DiscriminatorState(selector, (0,) * TABLE_CLASSES, held_atoms)
        for selector in (0, 1)
    )

    frame_sources = []
    frame_fixtures = []
    frame_mapping_failures = 0
    frame_atom_mapping_failures = 0
    for frame in c402.c397.c311.c235.proper_cubic_frames():
        rotated, mapping, failures = c402.c397.c342.mapped_fixture(held_fixture, frame)
        atoms = make_atoms(rotated, 16)
        frame_mapping_failures += failures
        for source, carried in zip(held_atoms, atoms):
            frame_atom_mapping_failures += int(
                carried.record.cylinder != c402.c397.mapped_expected(source.record.cylinder, mapping)
                or c402.c397.c350.atom_word(carried)[RECORD_M2:] != c402.c397.c350.atom_word(source)[RECORD_M2:]
            )
        frame_fixtures.extend((rotated, rotated))
        frame_sources.extend(
            DiscriminatorState(selector, (0,) * TABLE_CLASSES, atoms)
            for selector in (0, 1)
        )

    all_sources = held_sources + tuple(frame_sources)
    source_words = encode_packed(held_layout, all_sources)
    forward_words, inventory = run_routed(
        held_layout,
        held_logical,
        source_words,
        len(all_sources),
        inventory=True,
    )
    assert inventory is not None
    outputs = decode_packed(held_layout, forward_words, len(all_sources))
    expected = tuple(expected_output(source) for source in all_sources)
    recovered_words, _ = run_routed(
        held_layout,
        held_logical,
        forward_words,
        len(all_sources),
        inverse=True,
    )
    recovered = decode_packed(held_layout, recovered_words, len(all_sources))

    chain_failures = int(not c402.c397.c342.valid_chain(held_fixture, tuple(atom.record for atom in held_atoms)))
    for fixture, output in zip(frame_fixtures, outputs[2:]):
        chain_failures += int(not c402.c397.c342.valid_chain(fixture, tuple(atom.record for atom in output.atoms)))

    # Held-out-size control: the same exact circuit family on L3/N8.
    development_fixture = c402.c397.c338.build_fixture(3)
    development_atoms = make_atoms(development_fixture, 8)
    development_layout = make_layout(8)
    development_logical = logical_schedule(development_layout)
    development_sources = tuple(
        DiscriminatorState(selector, (0,) * TABLE_CLASSES, development_atoms)
        for selector in (0, 1)
    )
    development_words, development_inventory = run_routed(
        development_layout,
        development_logical,
        encode_packed(development_layout, development_sources),
        2,
        inventory=True,
    )
    assert development_inventory is not None
    development_outputs = decode_packed(development_layout, development_words, 2)

    detail = {
        "development_L_N": (3, 8),
        "held_L_N": (6, 16),
        "candidate_order": ("rescaled denominator-48 vertex", "denominator-96 relative interior"),
        "held_menu_vectors": tuple(output.menu_scores for output in outputs[:2]),
        "held_atom_score_aggregates": tuple(sum(output.atom_scores) for output in outputs[:2]),
        "held_discriminators": tuple(output.held_discriminator for output in outputs[:2]),
        "development_discriminators": tuple(output.held_discriminator for output in development_outputs),
        "development_atom_score_aggregates": tuple(sum(output.atom_scores) for output in development_outputs),
        "exact_EG_failures": sum(left != right for left, right in zip(outputs, expected)),
        "explicit_inverse_failures": sum(left != right for left, right in zip(recovered, all_sources)),
        "Record_payload_identity_failures": sum(
            c402.c397.c350.atom_word(left_atom) != c402.c397.c350.atom_word(right_atom)
            for source, output in zip(all_sources, outputs)
            for left_atom, right_atom in zip(source.atoms, output.atoms)
        ),
        "proper_cubic_frames": 24,
        "frame_cases": len(frame_sources),
        "frame_mapping_failures": frame_mapping_failures,
        "frame_atom_mapping_failures": frame_atom_mapping_failures,
        "lawful_chain_failures": chain_failures,
        "scalar_frame_output_failures": sum(
            output.menu_scores != scores_for(output.selector)
            or output.held_discriminator != output.selector
            for output in outputs[2:]
        ),
        "held_schedule": inventory,
        "development_schedule": development_inventory,
        "maximum_predecomposition_controls": 386,
        "clean_work_M2": WORK_M2,
        "ordered_schedule_is_time": False,
    }
    check(
        "one connected NN M2 family exactly prepares/admits both candidates, compares the physical menu, and preserves held typed Records in all frames",
        detail["held_menu_vectors"] == (scores_for(0), scores_for(1))
        and detail["held_atom_score_aggregates"] == (192, 192)
        and detail["held_discriminators"] == (0, 1)
        and detail["development_discriminators"] == (0, 1)
        and detail["development_atom_score_aggregates"] == (96, 96)
        and detail["exact_EG_failures"] == 0
        and detail["explicit_inverse_failures"] == 0
        and detail["Record_payload_identity_failures"] == 0
        and detail["frame_cases"] == 48
        and frame_mapping_failures == frame_atom_mapping_failures == chain_failures == 0
        and detail["scalar_frame_output_failures"] == 0
        and inventory["line_M2"] == 1645
        and inventory["line_edges"] == 1644
        and inventory["line_connected"]
        and inventory["maximum_primitive_support_M2"] == 3
        and inventory["maximum_primitive_span_edges"] == 2
        and inventory["nearest_neighbor_failures"] == 0
        and development_inventory["line_M2"] == 1237
        and development_inventory["maximum_primitive_support_M2"] == 3
        and development_inventory["nearest_neighbor_failures"] == 0
        and detail["maximum_predecomposition_controls"] == 386
        and detail["clean_work_M2"] == 384
        and not detail["ordered_schedule_is_time"],
        detail,
    )
    return detail


def physical_spectator_controls(surfaces: c402.Surfaces) -> dict[str, object]:
    old_pass, old_fail = c402.c398.PASS, c402.c398.FAIL
    c402.c398.PASS = c402.c398.FAIL = 0
    with redirect_stdout(StringIO()):
        physical = c402.c398.physical_controls(surfaces.fixtures, surfaces.banks, surfaces.installed)
    physical_green = (c402.c398.PASS, c402.c398.FAIL) == (1, 0)
    c402.c398.PASS, c402.c398.FAIL = old_pass, old_fail

    fixture = surfaces.fixtures[3]
    actual = c402.c397.c323.make_programs(fixture.contact)[0]
    deleted = c402.c397.c323.make_programs(np.eye(2, dtype=complex))[0]
    actual_effects = tuple(operator.conj().T @ operator for operator in actual.kraus)
    deleted_effects = tuple(operator.conj().T @ operator for operator in deleted.kraus)
    installed_menu = surfaces.installed.menus[PHYSICAL_MENU_INDEX]
    menu_match = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(installed_menu.effects, actual_effects)
    )
    contact_deletion = float(sum(
        np.linalg.norm(left - right)
        for left, right in zip(actual_effects, deleted_effects)
    ))

    # The new Boolean registers are a tensor-identity spectator on matter.
    # Therefore their exact Q/number/vector commutators are integer zero; the
    # inherited physical carrier supplies the tested mass/contact interface.
    detail = {
        "Cycle398_physical_green": physical_green,
        "physical_frame_tests": physical["physical_frame_tests"],
        "proper_cubic_frames_per_bank": physical["proper_cubic_frames_per_bank"],
        "maximum_held_leakage": physical["maximum_held_L6_leakage"],
        "maximum_constraint_residual": physical["maximum_held_L6_constraint_residual"],
        "one_particle_mass_relative_residual": physical["one_particle_mass_relative_residual"],
        "physical_contact_intertwiner_residual": physical["physical_contact_intertwiner_residual"],
        "selected_menu_effect_residual": menu_match,
        "selected_menu_contact_deletion_distance": contact_deletion,
        "grade_register_matter_touch_sites": 0,
        "Q_commutator": 0,
        "number_commutator": 0,
        "vector_commutator": (0, 0, 0),
    }
    check(
        "the actual menu and new scalar registers retain the inherited mass/Q/number/vector/contact and leakage controls",
        physical_green
        and physical["physical_frame_tests"] == 168
        and physical["proper_cubic_frames_per_bank"] == (24,) * 7
        and physical["physical_frame_branch_failures"] == 0
        and physical["incidence_frame_failures"] == 0
        and physical["maximum_held_L6_leakage"] < TOL
        and physical["maximum_held_L6_constraint_residual"] < TOL
        and physical["one_particle_mass_relative_residual"] < 3e-12
        and physical["physical_contact_intertwiner_residual"] < TOL
        and menu_match < TOL
        and contact_deletion > 0.27
        and detail["grade_register_matter_touch_sites"] == 0
        and detail["Q_commutator"] == detail["number_commutator"] == 0
        and detail["vector_commutator"] == (0, 0, 0),
        detail,
    )
    return detail


def deletion_attack_domain_controls() -> None:
    fixture = c402.c397.c338.build_fixture(3)
    atoms = make_atoms(fixture, 8)
    layout = make_layout(8)
    sources = tuple(DiscriminatorState(selector, (0,) * TABLE_CLASSES, atoms) for selector in (0, 1))
    packed = encode_packed(layout, sources)
    expected = tuple(expected_output(source) for source in sources)

    macro_rows = {}
    for label, kwargs in (
        ("loader", {"omit_loader": True}),
        ("admission", {"omit_admission": True}),
        ("menu", {"omit_menu": True}),
        ("Record attachment", {"omit_record": True}),
        ("menu comparator", {"omit_menu_comparator": True}),
        ("held comparator", {"omit_held_comparator": True}),
    ):
        outputs = decode_packed(
            layout,
            run_logical(layout, logical_schedule(layout, **kwargs), packed, 2),
            2,
        )
        macro_rows[label] = tuple(output != target for output, target in zip(outputs, expected))

    primitive_words, _ = run_routed(
        layout,
        logical_schedule(layout),
        packed,
        2,
        skip_index=0,
    )
    primitive_outputs = decode_packed(layout, primitive_words, 2)

    attacks = []
    for selector in (0, 1):
        for site in range(TABLE_M2):
            values = [0] * TABLE_CLASSES
            klass, bit = divmod(site, GRADE_M2)
            values[klass] = 1 << bit
            attacks.append(DiscriminatorState(selector, tuple(values), atoms))
    attack_words = run_logical(
        layout,
        logical_schedule(layout),
        encode_packed(layout, tuple(attacks)),
        len(attacks),
    )
    attack_outputs = decode_packed(layout, attack_words, len(attacks))

    malformed_atom = replace(atoms[0], fine_pointer=8)
    malformed_calls = (
        lambda: DiscriminatorState(2, (0,) * TABLE_CLASSES, atoms),
        lambda: DiscriminatorState(0, (0,) * (TABLE_CLASSES - 1), atoms),
        lambda: DiscriminatorState(0, (128,) + (0,) * (TABLE_CLASSES - 1), atoms),
        lambda: DiscriminatorState(0, (0,) * TABLE_CLASSES, (malformed_atom,) + atoms[1:]),
        lambda: DiscriminatorState(0, (0,) * TABLE_CLASSES, atoms, work=(1,) + (0,) * (WORK_M2 - 1)),
        lambda: make_layout(0),
        lambda: make_layout(17),
        lambda: c402.gate(layout.line_M2, "FREDKIN", 0, 1, 2),
        lambda: c402.gate(layout.line_M2, "CNOT", 0, 0),
        lambda: c402.mcx(layout.line_M2, (), (0, 1, 2), 3),
        lambda: decode_state(layout, [0] * (layout.line_M2 - 1)),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1

    detail = {
        "macro_deletion_detected_by_selector": macro_rows,
        "routed_primitive_deletion_detected_by_selector": tuple(
            output != target for output, target in zip(primitive_outputs, expected)
        ),
        "one_bit_blank_table_attacks": len(attack_outputs),
        "one_bit_false_admissions": sum(output.admitted for output in attack_outputs),
        "one_bit_false_held_discriminators": sum(output.held_discriminator for output in attack_outputs),
        "malformed_domain_rejections": rejected,
        "malformed_domain_attempts": len(malformed_calls),
    }
    check(
        "loader/admission/menu/Record/comparator and primitive deletions are visible; all table attacks and malformed domains reject",
        all(any(row) for row in macro_rows.values())
        and any(detail["routed_primitive_deletion_detected_by_selector"])
        and len(attack_outputs) == 770
        and detail["one_bit_false_admissions"] == 0
        and detail["one_bit_false_held_discriminators"] == 0
        and rejected == len(malformed_calls),
        detail,
    )


def inventory_and_semantic_controls(interface: dict[str, object], compiler: dict[str, object]) -> None:
    detail = {
        "supplied": (
            "two exact B witnesses and common denominator 96",
            "candidate selector preparation and blank table",
            "first-installed-menu ordering rule, eight effect-class binding, and actual physical apparatus program",
            "B1 full-vector equality reference and discriminator convention",
            "both equality-admission predicates",
            "typed/permanent Record formation premise, L3/N8 and held L6/N16 chains",
            "preparation/program/pointer/trial/use tags and atom order",
            "X/CNOT/Toffoli/SWAP basis, 384 work blanks, line layouts, routing, and ordered schedule",
        ),
        "not_selected": (
            "grade law", "probability", "Born rule", "actual member", "occurrence",
            "frequency", "energy", "source", "resource", "gravity", "rate", "time",
        ),
        "runtime_host_selection": False,
        "runtime_host_arithmetic": False,
        "selector_is_law_choice": False,
        "ordered_schedule_is_time": compiler["ordered_schedule_is_time"],
        "authority": AUTHORITY,
        "audit": AUDIT,
        "axiom_pressure": False,
        "face_dimension_imported_from_Cycle402": 19,
        "physical_discriminator_L1_distance": interface["L1_distance"],
    }
    check(
        "the positive discriminator inventories every supplied choice and selects no numerical, Born, actuality, source, or time law",
        len(detail["supplied"]) == 8
        and len(detail["not_selected"]) == 12
        and not detail["runtime_host_selection"]
        and not detail["runtime_host_arithmetic"]
        and not detail["selector_is_law_choice"]
        and not detail["ordered_schedule_is_time"]
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and not detail["axiom_pressure"]
        and detail["face_dimension_imported_from_Cycle402"] == 19
        and detail["physical_discriminator_L1_distance"] == 60,
        detail,
    )


def main() -> None:
    print("CYCLE 407: PHYSICAL EXTENSION-FACE OPERATIONAL DISCRIMINATOR")
    print("Authority:", AUTHORITY, "Audit:", AUDIT)
    note_contract()
    surfaces = c402.build_surfaces()
    interface = candidate_and_interface_controls(surfaces)
    compiler = compiler_and_frame_controls()
    physical_spectator_controls(surfaces)
    deletion_attack_domain_controls()
    inventory_and_semantic_controls(interface, compiler)
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)
    print("RESULT PHYSICAL_EXTENSION_FACE_OPERATIONAL_DISCRIMINATOR_CERTIFIED")


if __name__ == "__main__":
    main()
