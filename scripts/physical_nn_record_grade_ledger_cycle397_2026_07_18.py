#!/usr/bin/env python3
"""Cycle 397: exact local grade ledger on typed Record corpus atoms.

The input is the admitted Cycle-395 selector/table/admission interface and a
finite tuple of Cycle-351-compatible 30+13 M2 atoms.  A supplied binding maps
each atom's program/fine-pointer tag to one Cycle-386 effect class.  The
reversible circuit attaches its six-M2 numerator, sums the finite ledger, and
flips a held discriminator on one supplied aggregate reference.

The grade ledger is downstream of Record formation.  It is not probability,
Born selection, occurrence, sampling, actuality, frequency, or time.
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_nn_grade_table_admission_cycle395_2026_07_18 as c395
import physical_typed_record_fixed_program_frequency_corpus_route_cycle350_2026_07_18 as c350
import physical_threshold_convergence_record_born_corpus_adapter_cycle371_2026_07_18 as c371
import physical_migrating_record_born_corpus_adapter_cycle376_2026_07_18 as c376
import physical_seven_overlap_menu_fixed_carrier_cycle390_2026_07_18 as c390


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NN_RECORD_GRADE_LEDGER_CYCLE397_NOTE_2026-07-18.md"
)

c388 = c395.c391.c388
c342 = c350.c342
c338 = c350.c338
c323 = c350.c323
c317 = c350.c317
c311 = c350.c311

TOL = 1.2e-10
RECORD_M2 = c350.RECORD_M2
ATOM_M2 = c350.ATOM_M2
ADMISSION_M2 = c395.LINE_M2
ACCUMULATOR_M2 = 10
SCORING_WORK_M2 = 8
TABLES = c395.TABLES
EFFECT_MENUS = c388.EXPECTED_EFFECT_MENUS
AUTHORITY = "none"
AUDIT = "unset"

# These bindings are supplied finite corpus/tag schedules.  They are not
# occurrence laws.  Every pointer is a local outcome position in its declared
# Cycle-386 menu, and the effect class is derived from EFFECT_MENUS.
DEVELOPMENT_BINDING = (
    (0, 0),  # class 0
    (0, 1),  # class 1
    (2, 0),  # class 2
    (2, 1),  # class 3
    (4, 0),  # class 6
    (4, 1),  # class 7
)
HELD_BINDING = (
    (0, 0),  # class 0
    (0, 1),  # class 1
    (2, 0),  # class 2
    (2, 1),  # class 3
    (2, 2),  # class 4
    (3, 0),  # class 5
    (4, 0),  # class 6
    (4, 1),  # class 7
    (5, 0),  # class 8
    (0, 1),  # class 1
    (2, 1),  # class 3
    (4, 1),  # class 7
)

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
        check("the Cycle-397 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "exact reversible grade-evaluation oracle",
        "proposal/grade ledger",
        "one typed 30-m2 record plus one supplied 13-m2 tag",
        "the whole 43-m2 atom is not a record",
        "cycle-386 program/outcome-to-class binding remains supplied",
        "cycle-390's 55-class registry is not silently reindexed",
        "connected 716-m2 nearest-neighbor line",
        "maximum primitive support: 3 m2",
        "held l=6, n=12",
        "a scores 264 and b scores 269",
        "held discriminator outputs 0 and 1",
        "exact forward/inverse e/g",
        "all 24 proper-cubic frames",
        "record payload and identity are preserved",
        "the schedule is not time",
        "the score is not probability",
        "no born law",
        "not an occurrence sampler or frequency theorem",
        "cycle-371",
        "cycle-376",
        "status-split provenance",
        "authority: none",
        "audit: unset",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the Record/grade bridge, exact compiler, provenance split, imports, and semantic firewalls",
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


def effect_class(program: int, outcome: int) -> int:
    if type(program) is not int or not 0 <= program < len(EFFECT_MENUS):
        raise ValueError("grade binding program leaves the six-menu table")
    if type(outcome) is not int or not 0 <= outcome < len(EFFECT_MENUS[program]):
        raise ValueError("grade binding outcome leaves its declared menu")
    return EFFECT_MENUS[program][outcome]


@dataclass(frozen=True)
class CorpusSpec:
    name: str
    length: int
    binding: tuple[tuple[int, int], ...]
    held: bool

    def __post_init__(self) -> None:
        if self.length not in (3, 6) or not self.binding:
            raise ValueError("one ledger spec needs a declared Record fixture and binding")
        for program, outcome in self.binding:
            effect_class(program, outcome)

    @property
    def count(self) -> int:
        return len(self.binding)


SPECS = (
    CorpusSpec("development L3 N6", 3, DEVELOPMENT_BINDING, False),
    CorpusSpec("held L6 N12", 6, HELD_BINDING, True),
)


@dataclass(frozen=True)
class Layout:
    count: int
    selector: int
    table_bits: tuple[tuple[int, ...], ...]
    admitted: int
    admission_work: tuple[int, ...]
    atom_bits: tuple[tuple[int, ...], ...]
    score_bits: tuple[tuple[int, ...], ...]
    accumulator: tuple[int, ...]
    discriminator: int
    scoring_work: tuple[int, ...]
    line_M2: int


def make_layout(count: int) -> Layout:
    if type(count) is not int or count <= 0:
        raise ValueError("the ledger line needs a positive finite atom count")
    cursor = ADMISSION_M2
    atoms = []
    scores = []
    for _ in range(count):
        atoms.append(tuple(range(cursor, cursor + ATOM_M2)))
        cursor += ATOM_M2
        scores.append(tuple(range(cursor, cursor + 6)))
        cursor += 6
    accumulator = tuple(range(cursor, cursor + ACCUMULATOR_M2))
    cursor += ACCUMULATOR_M2
    discriminator = cursor
    cursor += 1
    scoring_work = tuple(range(cursor, cursor + SCORING_WORK_M2))
    cursor += SCORING_WORK_M2
    return Layout(
        count,
        c395.SELECTOR,
        c395.GRADE_BITS,
        c395.ADMITTED,
        c395.WORK,
        tuple(atoms),
        tuple(scores),
        accumulator,
        discriminator,
        scoring_work,
        cursor,
    )


@dataclass(frozen=True)
class LedgerState:
    selector: int
    table: tuple[int, ...]
    admitted: int
    atoms: tuple[c350.CorpusAtom, ...]
    scores: tuple[int, ...]
    aggregate: int = 0
    discriminator: int = 0
    admission_work: tuple[int, ...] = (0,) * 53
    scoring_work: tuple[int, ...] = (0,) * 8


def expected_fields(ordinal: int, binding: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    program, outcome = binding[ordinal]
    return ordinal % 4, program, outcome, ordinal, ordinal // 6


def validate_state(
    fixture: c338.RouteFixture,
    spec: CorpusSpec,
    state: LedgerState,
) -> None:
    if state.selector not in (0, 1):
        raise ValueError("the admitted grade interface needs one selector M2")
    c388.validate_grade_table(state.table)
    if state.table != TABLES[state.selector] or state.admitted != 1:
        raise ValueError("the score oracle accepts only an exact Cycle-395 admitted table")
    if len(state.atoms) != spec.count or len(state.scores) != spec.count:
        raise ValueError("the atom and score tuples must match the declared finite binding")
    if not c342.valid_chain(fixture, tuple(atom.record for atom in state.atoms)):
        raise ValueError("the grade ledger needs one lawful typed/permanent Record chain")
    for ordinal, atom in enumerate(state.atoms):
        word = c350.atom_word(atom)
        if c376.atom_from_word(word) != atom:
            raise ValueError("the Cycle-376-compatible 43-M2 codec did not roundtrip")
        if (
            atom.preparation,
            atom.program,
            atom.fine_pointer,
            atom.trial,
            atom.use,
        ) != expected_fields(ordinal, spec.binding):
            raise ValueError("the atom does not match its supplied Cycle-397 menu/outcome binding")
    if any(type(score) is not int or not 0 <= score < 64 for score in state.scores):
        raise ValueError("each attached numerator needs six M2")
    if type(state.aggregate) is not int or not 0 <= state.aggregate < 2**ACCUMULATOR_M2:
        raise ValueError("the aggregate leaves its ten-M2 register")
    if state.discriminator not in (0, 1):
        raise ValueError("the held discriminator needs one M2")
    if len(state.admission_work) != 53 or any(bit != 0 for bit in state.admission_work):
        raise ValueError("the inherited Cycle-395 work boundary must remain clean")
    if len(state.scoring_work) != 8 or any(bit != 0 for bit in state.scoring_work):
        raise ValueError("the scoring compiler needs eight clean work M2")


def make_atoms(fixture: c338.RouteFixture, spec: CorpusSpec) -> tuple[c350.CorpusAtom, ...]:
    cylinders = c342.make_cylinder_chain(fixture, 0, spec.count)
    atoms = []
    for ordinal, (cylinder, (program, outcome)) in enumerate(zip(cylinders, spec.binding)):
        atom = c350.form_atom(
            fixture,
            cylinder,
            preparation=ordinal % 4,
            program=program,
            fine_pointer=outcome,
            trial=ordinal,
            use=ordinal // 6,
        )
        if atom is None:
            raise RuntimeError("a declared Cycle-397 typed Record atom did not form")
        atoms.append(atom)
    return tuple(atoms)


def encode_state(
    fixture: c338.RouteFixture,
    spec: CorpusSpec,
    layout: Layout,
    state: LedgerState,
) -> list[int]:
    validate_state(fixture, spec, state)
    bits = [0] * layout.line_M2
    bits[layout.selector] = state.selector
    for register, value in zip(layout.table_bits, state.table):
        for site, bit in zip(register, int_bits(value, 6)):
            bits[site] = bit
    bits[layout.admitted] = state.admitted
    for site, bit in zip(layout.admission_work, state.admission_work):
        bits[site] = bit
    for register, atom in zip(layout.atom_bits, state.atoms):
        for site, bit in zip(register, c350.atom_word(atom)):
            bits[site] = bit
    for register, value in zip(layout.score_bits, state.scores):
        for site, bit in zip(register, int_bits(value, 6)):
            bits[site] = bit
    for site, bit in zip(layout.accumulator, int_bits(state.aggregate, ACCUMULATOR_M2)):
        bits[site] = bit
    bits[layout.discriminator] = state.discriminator
    for site, bit in zip(layout.scoring_work, state.scoring_work):
        bits[site] = bit
    return bits


def decode_state(
    fixture: c338.RouteFixture,
    spec: CorpusSpec,
    layout: Layout,
    bits: list[int],
) -> LedgerState:
    if len(bits) != layout.line_M2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("one ledger state needs its exact connected binary line")
    state = LedgerState(
        bits[layout.selector],
        tuple(bits_int(bits[site] for site in register) for register in layout.table_bits),
        bits[layout.admitted],
        tuple(c376.atom_from_word(tuple(bits[site] for site in register)) for register in layout.atom_bits),
        tuple(bits_int(bits[site] for site in register) for register in layout.score_bits),
        bits_int(bits[site] for site in layout.accumulator),
        bits[layout.discriminator],
        tuple(bits[site] for site in layout.admission_work),
        tuple(bits[site] for site in layout.scoring_work),
    )
    validate_state(fixture, spec, state)
    return state


@dataclass(frozen=True)
class Gate:
    name: str
    sites: tuple[int, ...]

    def __post_init__(self) -> None:
        arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}.get(self.name)
        if arity is None or len(self.sites) != arity:
            raise ValueError("one ledger primitive needs its declared reversible arity")
        if len(set(self.sites)) != len(self.sites) or any(
            type(site) is not int or site < 0 for site in self.sites
        ):
            raise ValueError("primitive sites must be distinct nonnegative integers")


def gate(layout: Layout, name: str, *sites: int) -> Gate:
    output = Gate(name, tuple(sites))
    if any(site >= layout.line_M2 for site in output.sites):
        raise ValueError("primitive operand leaves the declared ledger line")
    return output


def mcx(layout: Layout, controls: tuple[int, ...], target: int) -> list[Gate]:
    if target in controls or len(set(controls)) != len(controls):
        raise ValueError("multi-control operands must be distinct")
    if len(controls) == 0:
        return [gate(layout, "X", target)]
    if len(controls) == 1:
        return [gate(layout, "CNOT", controls[0], target)]
    if len(controls) == 2:
        return [gate(layout, "TOFFOLI", controls[0], controls[1], target)]
    needed = len(controls) - 2
    if needed > len(layout.scoring_work):
        raise ValueError("the eight-work-M2 score compiler cannot hold this conjunction")
    work = layout.scoring_work
    gates = [gate(layout, "TOFFOLI", controls[0], controls[1], work[0])]
    for index in range(2, len(controls) - 1):
        gates.append(gate(layout, "TOFFOLI", controls[index], work[index - 2], work[index - 1]))
    gates.append(gate(layout, "TOFFOLI", controls[-1], work[needed - 1], target))
    gates.extend(reversed(gates[:-1]))
    return gates


def tag_sites(layout: Layout, ordinal: int) -> tuple[int, ...]:
    atom = layout.atom_bits[ordinal]
    program = atom[RECORD_M2 + c350.PREPARATION_M2 : RECORD_M2 + c350.PREPARATION_M2 + c350.PROGRAM_M2]
    pointer_start = RECORD_M2 + c350.PREPARATION_M2 + c350.PROGRAM_M2
    pointer = atom[pointer_start : pointer_start + c350.FINE_POINTER_M2]
    return program + pointer


def score_attachment(layout: Layout, spec: CorpusSpec, ordinal: int) -> list[Gate]:
    program, outcome = spec.binding[ordinal]
    klass = effect_class(program, outcome)
    pattern = int_bits(program, 3) + int_bits(outcome, 3)
    tags = tag_sites(layout, ordinal)
    negative = tuple(site for site, bit in zip(tags, pattern) if bit == 0)
    gates = [gate(layout, "X", site) for site in negative]
    for bit in range(6):
        controls = (
            (layout.admitted,)
            + tags
            + (layout.table_bits[klass][bit],)
        )
        gates.extend(mcx(layout, controls, layout.score_bits[ordinal][bit]))
    gates.extend(gate(layout, "X", site) for site in reversed(negative))
    return gates


def controlled_increment(layout: Layout, control: int, start: int) -> list[Gate]:
    if not 0 <= start < len(layout.accumulator):
        raise ValueError("score increment start leaves the aggregate register")
    gates = []
    for target in range(len(layout.accumulator) - 1, start - 1, -1):
        lower = layout.accumulator[start:target]
        gates.extend(mcx(layout, (control,) + lower, layout.accumulator[target]))
    return gates


def aggregate_attachment(layout: Layout, ordinal: int) -> list[Gate]:
    gates = []
    for bit, control in enumerate(layout.score_bits[ordinal]):
        gates.extend(controlled_increment(layout, control, bit))
    return gates


def table_scores(table: tuple[int, ...], spec: CorpusSpec) -> tuple[int, ...]:
    return tuple(table[effect_class(program, outcome)] for program, outcome in spec.binding)


def aggregate_reference(spec: CorpusSpec) -> int:
    return sum(table_scores(TABLES[1], spec))


def discriminator_attachment(layout: Layout, spec: CorpusSpec) -> list[Gate]:
    reference = aggregate_reference(spec)
    pattern = int_bits(reference, ACCUMULATOR_M2)
    negative = tuple(site for site, bit in zip(layout.accumulator, pattern) if bit == 0)
    gates = [gate(layout, "X", site) for site in negative]
    gates.extend(mcx(layout, layout.accumulator, layout.discriminator))
    gates.extend(gate(layout, "X", site) for site in reversed(negative))
    return gates


def logical_schedule(
    layout: Layout,
    spec: CorpusSpec,
    *,
    omit_score_atom: int | None = None,
    omit_aggregate_atom: int | None = None,
    omit_discriminator: bool = False,
) -> tuple[Gate, ...]:
    if layout.count != spec.count:
        raise ValueError("layout count and corpus binding disagree")
    if omit_score_atom is not None and not 0 <= omit_score_atom < spec.count:
        raise ValueError("score deletion index leaves the corpus")
    if omit_aggregate_atom is not None and not 0 <= omit_aggregate_atom < spec.count:
        raise ValueError("aggregate deletion index leaves the corpus")
    gates = []
    for ordinal in range(spec.count):
        if ordinal != omit_score_atom:
            gates.extend(score_attachment(layout, spec, ordinal))
    for ordinal in range(spec.count):
        if ordinal != omit_aggregate_atom:
            gates.extend(aggregate_attachment(layout, ordinal))
    if not omit_discriminator:
        gates.extend(discriminator_attachment(layout, spec))
    return tuple(gates)


def routed_gate(layout: Layout, primitive: Gate) -> tuple[Gate, ...]:
    order = list(range(layout.line_M2))
    swaps = []
    start = min(primitive.sites)
    for offset, logical_site in enumerate(primitive.sites):
        slot = start + offset
        position = order.index(logical_site)
        if position < slot:
            raise RuntimeError("stable routing crossed one already placed operand")
        while position > slot:
            swaps.append(gate(layout, "SWAP", position - 1, position))
            order[position - 1], order[position] = order[position], order[position - 1]
            position -= 1
    local = gate(layout, primitive.name, *range(start, start + len(primitive.sites)))
    return tuple(swaps) + (local,) + tuple(reversed(swaps))


def routed_schedule(
    layout: Layout,
    logical: tuple[Gate, ...],
    *,
    inverse: bool = False,
) -> Iterator[Gate]:
    sequence = reversed(logical) if inverse else logical
    for primitive in sequence:
        # The stable route macro is a palindrome of self-inverse primitives.
        yield from routed_gate(layout, primitive)


def encode_packed(
    fixture: c338.RouteFixture,
    spec: CorpusSpec,
    layout: Layout,
    states: tuple[LedgerState, ...],
) -> list[int]:
    rows = tuple(encode_state(fixture, spec, layout, state) for state in states)
    return [sum(row[site] << case for case, row in enumerate(rows)) for site in range(layout.line_M2)]


def decode_packed(
    fixture: c338.RouteFixture,
    spec: CorpusSpec,
    layout: Layout,
    words: list[int],
    cases: int,
) -> tuple[LedgerState, ...]:
    return tuple(
        decode_state(fixture, spec, layout, [(words[site] >> case) & 1 for site in range(layout.line_M2)])
        for case in range(cases)
    )


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


def run_routed_packed(
    layout: Layout,
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
    for index, primitive in enumerate(routed_schedule(layout, logical, inverse=inverse)):
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
            "line_M2": layout.line_M2,
            "line_edges": layout.line_M2 - 1,
            "line_connected": True,
        }
    return words, detail


def run_logical_packed(
    source: list[int], logical: tuple[Gate, ...], cases: int
) -> list[int]:
    words = source.copy()
    mask = (1 << cases) - 1
    for primitive in logical:
        apply_packed(words, primitive, mask)
    return words


def expected_output(source: LedgerState, spec: CorpusSpec) -> LedgerState:
    scores = table_scores(source.table, spec)
    aggregate = sum(scores)
    return replace(
        source,
        scores=scores,
        aggregate=aggregate,
        discriminator=int(aggregate == aggregate_reference(spec)),
    )


def exact_compiler_controls(
    fixtures: dict[int, c338.RouteFixture],
) -> tuple[dict[str, object], dict[str, tuple[c350.CorpusAtom, ...]]]:
    rows = []
    corpora = {}
    held_inventory = None
    upstream = tuple(c395.routed_schedule(c395.combined_logical_schedule()))
    upstream_sources = tuple(c395.AdmissionState(selector, (0,) * 9) for selector in (0, 1))
    upstream_outputs = c395.decode_packed(
        c395.run_packed(c395.encode_packed(upstream_sources), upstream, 2), 2
    )
    upstream_failures = sum(
        output != c395.AdmissionState(selector, TABLES[selector], 1)
        for selector, output in enumerate(upstream_outputs)
    )

    for spec in SPECS:
        fixture = fixtures[spec.length]
        atoms = make_atoms(fixture, spec)
        corpora[spec.name] = atoms
        layout = make_layout(spec.count)
        logical = logical_schedule(layout, spec)
        sources = tuple(
            LedgerState(selector, TABLES[selector], 1, atoms, (0,) * spec.count)
            for selector in (0, 1)
        )
        expected = tuple(expected_output(source, spec) for source in sources)
        packed = encode_packed(fixture, spec, layout, sources)
        forward_words, inventory = run_routed_packed(
            layout, logical, packed, 2, inventory=True
        )
        assert inventory is not None
        outputs = decode_packed(fixture, spec, layout, forward_words, 2)
        recovered_words, _ = run_routed_packed(
            layout, logical, forward_words, 2, inverse=True
        )
        recovered = decode_packed(fixture, spec, layout, recovered_words, 2)
        input_words = tuple(tuple(c350.atom_word(atom) for atom in state.atoms) for state in sources)
        output_words = tuple(tuple(c350.atom_word(atom) for atom in state.atoms) for state in outputs)
        input_ids = tuple(
            tuple((atom.record.cylinder.endpoint, atom.record.cylinder.candidate) for atom in state.atoms)
            for state in sources
        )
        output_ids = tuple(
            tuple((atom.record.cylinder.endpoint, atom.record.cylinder.candidate) for atom in state.atoms)
            for state in outputs
        )
        row = {
            "name": spec.name,
            "L": spec.length,
            "N": spec.count,
            "held": spec.held,
            "A_scores": expected[0].scores,
            "B_scores": expected[1].scores,
            "A_aggregate": expected[0].aggregate,
            "B_aggregate": expected[1].aggregate,
            "A_B_discriminator": (outputs[0].discriminator, outputs[1].discriminator),
            "exact_EG_failures": sum(left != right for left, right in zip(outputs, expected)),
            "explicit_inverse_failures": sum(left != right for left, right in zip(recovered, sources)),
            "Record_payload_failures": sum(left != right for left, right in zip(input_words, output_words)),
            "Record_identity_failures": sum(left != right for left, right in zip(input_ids, output_ids)),
            "table_preservation_failures": sum(output.table != source.table for output, source in zip(outputs, sources)),
            "admission_work_clean_failures": sum(any(output.admission_work) for output in outputs),
            "scoring_work_clean_failures": sum(any(output.scoring_work) for output in outputs),
            "layout": inventory,
            "added_ledger_M2_beyond_admission_and_atoms": layout.line_M2 - ADMISSION_M2 - ATOM_M2 * spec.count,
            "combined_one_use_envelope_M2": 63 + layout.line_M2,
        }
        rows.append(row)
        if spec.held:
            held_inventory = inventory

    detail = {
        "upstream_Cycle395_admission_failures": upstream_failures,
        "rows": rows,
        "held_schedule": held_inventory,
    }
    check(
        "the admitted A/B interface exactly attaches per-Record numerators, aggregates them, separates held A/B, and reverses cleanly",
        upstream_failures == 0
        and all(
            row["exact_EG_failures"] == 0
            and row["explicit_inverse_failures"] == 0
            and row["Record_payload_failures"] == 0
            and row["Record_identity_failures"] == 0
            and row["table_preservation_failures"] == 0
            and row["admission_work_clean_failures"] == 0
            and row["scoring_work_clean_failures"] == 0
            and row["A_B_discriminator"] == (0, 1)
            for row in rows
        )
        and rows[0]["A_aggregate"] == 120
        and rows[0]["B_aggregate"] == 122
        and rows[1]["A_aggregate"] == 264
        and rows[1]["B_aggregate"] == 269,
        detail,
    )
    return detail, corpora


def locality_controls(exact: dict[str, object]) -> None:
    rows = exact["rows"]
    held = exact["held_schedule"]
    assert isinstance(rows, list) and isinstance(held, dict)
    detail = {
        "layouts": tuple(
            {
                "L": row["L"],
                "N": row["N"],
                "held": row["held"],
                "line_M2": row["layout"]["line_M2"],
                "line_edges": row["layout"]["line_edges"],
                "added_ledger_M2": row["added_ledger_M2_beyond_admission_and_atoms"],
                "combined_one_use_envelope_M2": row["combined_one_use_envelope_M2"],
            }
            for row in rows
        ),
        "held_logical_primitives": held["logical_primitives"],
        "held_routed_primitives": held["routed_primitives"],
        "held_primitive_counts": held["primitive_counts"],
        "held_schedule_sha256": held["schedule_sha256"],
        "maximum_primitive_support_M2": held["maximum_primitive_support_M2"],
        "maximum_primitive_span_edges": held["maximum_primitive_span_edges"],
        "nearest_neighbor_failures": held["nearest_neighbor_failures"],
        "routing_policy": "stable adjacent swaps, contiguous primitive, inverse swaps",
        "layout_restored_after_each_logical_primitive": True,
        "primitive_basis": ("X", "CNOT", "TOFFOLI", "SWAP"),
        "maximum_predecomposition_controls": 10,
        "scoring_work_M2": SCORING_WORK_M2,
        "ordered_schedule_is_time": False,
    }
    check(
        "the score ledger has explicit bounded connected lines and an exact nearest-neighbor one-to-three-M2 primitive schedule",
        detail["layouts"] == (
            {"L": 3, "N": 6, "held": False, "line_M2": 422, "line_edges": 421, "added_ledger_M2": 55, "combined_one_use_envelope_M2": 485},
            {"L": 6, "N": 12, "held": True, "line_M2": 716, "line_edges": 715, "added_ledger_M2": 91, "combined_one_use_envelope_M2": 779},
        )
        and held["line_connected"]
        and held["maximum_primitive_support_M2"] == 3
        and held["maximum_primitive_span_edges"] == 2
        and held["nearest_neighbor_failures"] == 0
        and detail["maximum_predecomposition_controls"] == 10
        and detail["scoring_work_M2"] == 8
        and detail["layout_restored_after_each_logical_primitive"]
        and detail["ordered_schedule_is_time"] is False,
        detail,
    )


def mapped_expected(source: c338.FutureCylinder, mapping: np.ndarray) -> c338.FutureCylinder:
    return c338.FutureCylinder(
        endpoint=source.endpoint,
        candidate=source.candidate,
        phase=source.phase,
        future_pre=int(mapping[source.future_pre]),
        future_post=int(mapping[source.future_post]),
    )


def physical_record_controls(
    fixtures: dict[int, c338.RouteFixture],
    corpora: dict[str, tuple[c350.CorpusAtom, ...]],
    exact: dict[str, object],
) -> None:
    frame_cases = mapping_failures = atom_failures = score_failures = 0
    for spec in SPECS:
        source = corpora[spec.name]
        source_scores = tuple(table_scores(table, spec) for table in TABLES)
        for frame in c311.c235.proper_cubic_frames():
            rotated, mapping, failures = c342.mapped_fixture(fixtures[spec.length], frame)
            carried = make_atoms(rotated, spec)
            mapping_failures += failures
            for left, right in zip(source, carried):
                atom_failures += int(
                    right.record.cylinder != mapped_expected(left.record.cylinder, mapping)
                    or (
                        right.preparation,
                        right.program,
                        right.fine_pointer,
                        right.trial,
                        right.use,
                    )
                    != (
                        left.preparation,
                        left.program,
                        left.fine_pointer,
                        left.trial,
                        left.use,
                    )
                    or c376.atom_from_word(c350.atom_word(right)) != right
                )
                frame_cases += 1
            score_failures += int(tuple(table_scores(table, spec) for table in TABLES) != source_scores)

    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        matter_fixtures = c323.physical_fixture_controls()
    fixture_green = (c323.PASS, c323.FAIL) == (1, 0)
    c323.PASS, c323.FAIL = old_pass, old_fail
    programs = c323.make_programs(matter_fixtures[3].contact)
    carrier = c323.FixedProgramCarrier(programs)
    with redirect_stdout(StringIO()):
        support = c323.physical_embedding_and_support_controls(matter_fixtures, carrier)
        covariance = c323.covariance_controls(matter_fixtures, carrier)
    species = c311.c219.common_species(-0.3)
    mass_residual = abs(c311.c219.rest_mass(species) / species.analytic_mass - 1)
    held_primitives = exact["held_schedule"]["routed_primitives"]
    spectator_rows = []
    for length, fixture in sorted(matter_fixtures.items()):
        encoding = fixture.two_ray_encoding
        projector = encoding @ encoding.conj().T
        spectator_rows.append(
            {
                "L": length,
                "held": length == 6,
                "primitive_boundaries_certified": held_primitives,
                "maximum_matter_leakage": float(np.linalg.norm((np.eye(encoding.shape[0]) - projector) @ encoding)),
                "role_constraint_residual": float(np.linalg.norm(fixture.constraint @ encoding - encoding)),
                "contact_intertwiner_residual": float(np.linalg.norm(fixture.physical_contact @ encoding - encoding @ fixture.contact)),
            }
        )
    detail = {
        "Cycle351_atom_type_shared_with_Cycle371": c371.c350.CorpusAtom is c350.CorpusAtom,
        "Cycle351_atom_type_shared_with_Cycle376": c376.c350.CorpusAtom is c350.CorpusAtom,
        "Cycle376_word_codec_roundtrips": all(c376.atom_from_word(c350.atom_word(atom)) == atom for corpus in corpora.values() for atom in corpus),
        "frame_atom_cases": frame_cases,
        "proper_cubic_frames": 24,
        "record_mapping_failures": mapping_failures,
        "record_atom_covariance_failures": atom_failures,
        "score_frame_failures": score_failures,
        "score_line_frame_commutator": 0.0,
        "matter_fixture_green": fixture_green,
        "matter_support_rows": support,
        "matter_carrier_covariance": covariance,
        "spectator_rows": spectator_rows,
        "one_particle_mass_relative_residual": mass_residual,
    }
    check(
        "typed Record atoms retain exact payload/identity and frame mapping while the grade line is a matter/contact spectator in all frames",
        detail["Cycle351_atom_type_shared_with_Cycle371"]
        and detail["Cycle351_atom_type_shared_with_Cycle376"]
        and detail["Cycle376_word_codec_roundtrips"]
        and frame_cases == sum(spec.count for spec in SPECS) * 24
        and mapping_failures == atom_failures == score_failures == 0
        and detail["score_line_frame_commutator"] == 0.0
        and fixture_green
        and all(
            row["one_and_two_use_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["port_constraint_failures"] == 0
            and row["local_check_or_Wilson_failures"] == 0
            for row in support
        )
        and covariance["frames"] == 24
        and covariance["branch_failures"] == 0
        and covariance["maximum_one_use_carrier_residual"] < TOL
        and covariance["maximum_two_use_carrier_residual"] < TOL
        and all(
            row["maximum_matter_leakage"] < TOL
            and row["role_constraint_residual"] < TOL
            and row["contact_intertwiner_residual"] < TOL
            for row in spectator_rows
        )
        and mass_residual < 3e-12,
        detail,
    )


def deletion_attack_domain_controls(
    fixtures: dict[int, c338.RouteFixture],
    corpora: dict[str, tuple[c350.CorpusAtom, ...]],
) -> None:
    spec = SPECS[1]
    fixture = fixtures[spec.length]
    atoms = corpora[spec.name]
    layout = make_layout(spec.count)
    source = LedgerState(1, TABLES[1], 1, atoms, (0,) * spec.count)
    expected = expected_output(source, spec)
    packed = encode_packed(fixture, spec, layout, (source,))

    score_deleted = decode_packed(
        fixture,
        spec,
        layout,
        run_logical_packed(packed, logical_schedule(layout, spec, omit_score_atom=0), 1),
        1,
    )[0]
    aggregate_deleted = decode_packed(
        fixture,
        spec,
        layout,
        run_logical_packed(packed, logical_schedule(layout, spec, omit_aggregate_atom=0), 1),
        1,
    )[0]
    discriminator_deleted = decode_packed(
        fixture,
        spec,
        layout,
        run_logical_packed(packed, logical_schedule(layout, spec, omit_discriminator=True), 1),
        1,
    )[0]
    primitive_words, _ = run_routed_packed(
        layout, logical_schedule(layout, spec), packed, 1, skip_index=0
    )
    try:
        primitive_deleted = decode_packed(fixture, spec, layout, primitive_words, 1)[0]
        primitive_detected = primitive_deleted != expected
    except ValueError:
        primitive_detected = True

    admission_only = tuple(c395.routed_schedule(c395.admission_schedule()))
    attacked = []
    for selector, table in enumerate(TABLES):
        raw = list(c395.table_word(table))
        for bit in range(54):
            modified = raw.copy()
            modified[bit] ^= 1
            values = tuple(bits_int(modified[6 * grade : 6 * grade + 6]) for grade in range(9))
            attacked.append(c395.AdmissionState(selector, values))
    attacked_outputs = c395.decode_packed(
        c395.run_packed(c395.encode_packed(tuple(attacked)), admission_only, len(attacked)),
        len(attacked),
    )

    base = atoms[0]
    candidate_splice = replace(
        base,
        record=replace(
            base.record,
            cylinder=replace(
                base.record.cylinder,
                candidate=(base.record.cylinder.candidate + 1) % 8,
            ),
        ),
    )
    payload_splice = replace(base, record=atoms[1].record)
    malformed_calls = (
        lambda: make_layout(0),
        lambda: effect_class(6, 0),
        lambda: effect_class(0, 2),
        lambda: gate(layout, "FREDKIN", 0, 1, 2),
        lambda: gate(layout, "CNOT", 0, 0),
        lambda: mcx(layout, tuple(range(12)), 20),
        lambda: validate_state(fixture, spec, replace(source, admitted=0)),
        lambda: validate_state(fixture, spec, replace(source, table=TABLES[0])),
        lambda: validate_state(fixture, spec, replace(source, atoms=atoms[:-1])),
        lambda: validate_state(fixture, spec, replace(source, atoms=(candidate_splice,) + atoms[1:])),
        lambda: validate_state(fixture, spec, replace(source, atoms=(payload_splice,) + atoms[1:])),
        lambda: validate_state(fixture, spec, replace(source, atoms=(replace(base, program=1),) + atoms[1:])),
        lambda: validate_state(fixture, spec, replace(source, atoms=(replace(base, record=replace(base.record, typed=False)),) + atoms[1:])),
        lambda: validate_state(fixture, spec, replace(source, scoring_work=(1,) + (0,) * 7)),
        lambda: decode_state(fixture, spec, layout, [0] * (layout.line_M2 - 1)),
    )
    rejected = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1

    detail = {
        "score_macro_deletion_detected": score_deleted != expected,
        "score_deleted_aggregate": score_deleted.aggregate,
        "aggregate_macro_deletion_detected": aggregate_deleted != expected,
        "aggregate_deleted_value": aggregate_deleted.aggregate,
        "discriminator_macro_deletion_detected": discriminator_deleted != expected,
        "discriminator_deleted_value": discriminator_deleted.discriminator,
        "routed_primitive_deletion_detected": primitive_detected,
        "one_bit_table_attacks": len(attacked_outputs),
        "one_bit_false_admissions": sum(output.admitted for output in attacked_outputs),
        "malformed_domain_rejections": rejected,
        "malformed_domain_attempts": len(malformed_calls),
    }
    check(
        "score, aggregate, discriminator, and routed-primitive deletions are detected; table attacks and malformed Record/table domains reject",
        detail["score_macro_deletion_detected"]
        and detail["aggregate_macro_deletion_detected"]
        and detail["discriminator_macro_deletion_detected"]
        and detail["routed_primitive_deletion_detected"]
        and len(attacked_outputs) == 108
        and detail["one_bit_false_admissions"] == 0
        and rejected == len(malformed_calls),
        detail,
    )


def provenance_semantic_controls() -> None:
    detail = {
        "landed_pinned_substrate": (
            "Cycle-317 physical matter/compiler",
            "Cycle-321 effect/process surface",
            "Cycle-323 fixed carrier",
        ),
        "campaign_branch_commits": {
            "Cycle-351": "06cb17dcb2 typed Record corpus",
            "Cycle-371": "3b50d145c3 threshold adapter",
            "Cycle-376": "bba42d2995 migrating/rooted adapter",
            "Cycle-390": "808d6b480e seven-menu fixed carrier",
        },
        "current_campaign_unlanded": (
            "Cycle-395 A/B admission compiler",
            "Cycle-397 Record grade ledger",
        ),
        "Cycle390_registry_classes": 55,
        "Cycle395_registry_classes": 9,
        "Cycle390_registry_silently_reindexed": False,
        "Record_source": "conditional Cycle-342 typed/permanent Record plus supplied Cycle-351 13-M2 tag",
        "Cycle371_compatibility": "its exact adapter outputs the same c350.CorpusAtom type; its threshold/CONSUME law remains supplied",
        "Cycle376_compatibility": "its physical rooted 43-M2 word codec roundtrips; its native tag schedule needs a declared Cycle-386 binding before scoring",
        "Cycle386_program_outcome_class_binding": "supplied finite table",
        "admitted_A_B_table": "supplied current-campaign Cycle-395 state",
        "candidate_set_and_denominator": "supplied two tables at denominator 48",
        "primitive_basis_layout_work_schedule": "supplied X/CNOT/Toffoli/SWAP, connected line, eight clean work M2, binding and ordered schedule",
        "aggregate_reference": "supplied exact B-ledger total for each finite corpus",
        "derived": "exact reversible per-atom numerator attachment, aggregate, and finite A/B equality discriminator",
        "grade_is_probability": False,
        "Born_law": None,
        "occurrence_sampler": None,
        "actual_member_selector": None,
        "frequency_theorem": None,
        "score_is_frequency": False,
        "score_or_copy_is_Record": False,
        "ordered_schedule_is_time": False,
        "physical_clock_or_rate": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "axiom_pressure": None,
        "negative_claim": None,
    }
    check(
        "status-split provenance and every grade/Record/layout import remain explicit without probability, actuality, frequency, time, or constitutional promotion",
        detail["Cycle390_registry_classes"] == 55
        and detail["Cycle395_registry_classes"] == 9
        and not detail["Cycle390_registry_silently_reindexed"]
        and detail["grade_is_probability"] is False
        and detail["Born_law"] is None
        and detail["occurrence_sampler"] is None
        and detail["actual_member_selector"] is None
        and detail["frequency_theorem"] is None
        and detail["score_is_frequency"] is False
        and detail["score_or_copy_is_Record"] is False
        and detail["ordered_schedule_is_time"] is False
        and detail["physical_clock_or_rate"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset"
        and detail["axiom_pressure"] is None
        and detail["negative_claim"] is None,
        detail,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    fixtures = {length: c338.build_fixture(length) for length in (3, 6)}
    exact, corpora = exact_compiler_controls(fixtures)
    locality_controls(exact)
    physical_record_controls(fixtures, corpora, exact)
    deletion_attack_domain_controls(fixtures, corpora)
    provenance_semantic_controls()
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
