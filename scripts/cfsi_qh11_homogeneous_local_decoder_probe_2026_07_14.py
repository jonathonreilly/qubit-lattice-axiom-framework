#!/usr/bin/env python3
"""Exact probes for a homogeneous, record-decoded CFSI-Q microstage law.

The model replaces the hand-enumerated CFSI-Q7 ray schedule with one finite
motif decoder applied at every lattice site and every oriented cubic frame.
Immutable program records determine orientation, phase, settings, a finite
mixed-frame link, and collision priority.  Two append-only stage certificates
make the coherent work state reconstructible from records at every transaction
boundary.  The construction is bounded and is not asserted to be nature's law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Iterable

import sympy as sp

import cfsi_q_bell_coherent_causal_front_law_probe_2026_07_14 as q7


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CFSI_QH11_HOMOGENEOUS_LOCAL_DECODER_NOTE_2026-07-14.md"
)
Q7_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CFSI_Q_BELL_COHERENT_CAUSAL_FRONT_LAW_NOTE_2026-07-14.md"
)
SCHEDULE_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md"
)
PAIR_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


PASS = 0
FAIL = 0
Vec = tuple[int, int, int]
Token = tuple[object, ...]
Records = dict[Vec, Token]


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def add(*vectors: Vec) -> Vec:
    return tuple(sum(vector[axis] for vector in vectors) for axis in range(3))  # type: ignore[return-value]


def neg(vector: Vec) -> Vec:
    return tuple(-entry for entry in vector)  # type: ignore[return-value]


def subtract(left: Vec, right: Vec) -> Vec:
    return add(left, neg(right))


def dot(left: Vec, right: Vec) -> int:
    return sum(left[axis] * right[axis] for axis in range(3))


def cross(left: Vec, right: Vec) -> Vec:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def l1(left: Vec, right: Vec) -> int:
    return sum(abs(entry) for entry in subtract(left, right))


AXES: tuple[Vec, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def proper_cubic_rotations() -> tuple[tuple[Vec, Vec, Vec], ...]:
    rotations = []
    for ex in AXES:
        for ey in AXES:
            if dot(ex, ey) != 0:
                continue
            ez = cross(ex, ey)
            if ez in AXES:
                rotations.append((ex, ey, ez))
    return tuple(rotations)


def rotate(vector: Vec, rotation: tuple[Vec, Vec, Vec]) -> Vec:
    ex, ey, ez = rotation
    return (
        vector[0] * ex[0] + vector[1] * ey[0] + vector[2] * ez[0],
        vector[0] * ex[1] + vector[1] * ey[1] + vector[2] * ez[1],
        vector[0] * ex[2] + vector[1] * ey[2] + vector[2] * ez[2],
    )


@dataclass(frozen=True)
class Program:
    anchor: Vec
    direction: Vec
    transverse: Vec
    phase: int
    setting_a: int
    setting_b: int
    link: int
    priority: int
    nonce: str


def program_key(program: Program) -> tuple:
    return (
        program.anchor,
        program.direction,
        program.transverse,
        program.nonce,
        program.phase,
        program.setting_a,
        program.setting_b,
        program.link,
        program.priority,
    )


def motif_positions(program: Program) -> dict[str, Vec]:
    o = program.anchor
    d = program.direction
    t = program.transverse
    u = cross(d, t)
    return {
        "priority": add(o, neg(d), neg(t)),
        "phase": add(o, neg(d)),
        "link": add(o, neg(d), t),
        "source_a": o,
        "source_b": add(o, t),
        "front_a": add(o, d),
        "front_b": add(o, d, t),
        "setting_a": add(o, d, neg(t)),
        "setting_b": add(o, d, t, t),
        "prepared_cert": add(o, u),
        "propagated_cert": add(o, d, u),
    }


def program_token(program: Program, role: str, value: object) -> Token:
    return ("program", program.nonce, role, value)


def program_records(program: Program) -> Records:
    pos = motif_positions(program)
    return {
        pos["priority"]: program_token(program, "priority", program.priority),
        pos["phase"]: program_token(program, "phase", program.phase),
        pos["link"]: program_token(program, "link", program.link),
        pos["setting_a"]: program_token(program, "setting-a", program.setting_a),
        pos["setting_b"]: program_token(program, "setting-b", program.setting_b),
    }


def merge_record_sets(*sets: Records) -> Records:
    merged: Records = {}
    for records in sets:
        for site, token in records.items():
            if site in merged and merged[site] != token:
                raise ValueError(f"incompatible records at {site}")
            merged[site] = token
    return merged


def token_value(records: Records, site: Vec, nonce: str, role: str):
    token = records.get(site)
    if token is None or len(token) != 4:
        return None
    if token[:3] != ("program", nonce, role):
        return None
    return token[3]


def detect_programs(records: Records) -> set[Program]:
    """Apply one coordinate-free finite motif decoder everywhere."""

    detected: set[Program] = set()
    phase_records = [
        (site, token)
        for site, token in records.items()
        if len(token) == 4 and token[0] == "program" and token[2] == "phase"
    ]
    for phase_site, token in phase_records:
        nonce = str(token[1])
        phase = token[3]
        for direction in AXES:
            anchor = add(phase_site, direction)
            for transverse in AXES:
                if dot(direction, transverse) != 0:
                    continue
                shell = Program(anchor, direction, transverse, int(phase), 0, 0, 0, 0, nonce)
                pos = motif_positions(shell)
                priority = token_value(records, pos["priority"], nonce, "priority")
                link = token_value(records, pos["link"], nonce, "link")
                setting_a = token_value(records, pos["setting_a"], nonce, "setting-a")
                setting_b = token_value(records, pos["setting_b"], nonce, "setting-b")
                if None in (priority, link, setting_a, setting_b):
                    continue
                candidate = Program(
                    anchor,
                    direction,
                    transverse,
                    int(phase),
                    int(setting_a),
                    int(setting_b),
                    int(link),
                    int(priority),
                    nonce,
                )
                if program_records(candidate).items() <= records.items():
                    detected.add(candidate)
    return detected


def footprint(program: Program) -> set[Vec]:
    return set(motif_positions(program).values())


def conflicts(left: Program, right: Program) -> bool:
    return bool(footprint(left) & footprint(right))


def admitted_programs(records: Records) -> set[Program]:
    """Static local strict-priority maxima; admitted footprints are disjoint."""

    programs = detect_programs(records)
    return {
        program
        for program in programs
        if all(
            program.priority > other.priority
            for other in programs
            if other != program and conflicts(program, other)
        )
    }


def prepared_token(program: Program) -> Token:
    return ("stage", program.nonce, "prepared")


def propagated_token(program: Program) -> Token:
    return ("stage", program.nonce, "propagated")


def outcome_token(program: Program, party: str, outcome: int) -> Token:
    return ("outcome", program.nonce, party, outcome)


def outcome_at(records: Records, site: Vec, program: Program, party: str) -> int | None:
    token = records.get(site)
    if token is None or len(token) != 4 or token[:3] != ("outcome", program.nonce, party):
        return None
    return int(token[3])


def program_stage(records: Records, program: Program) -> int:
    """Return 0 blank, 1 prepared, 2 propagated, 3 committed, or -1 invalid."""

    if not program_records(program).items() <= records.items():
        return -1
    pos = motif_positions(program)
    if pos["source_a"] in records or pos["source_b"] in records:
        return -1
    prepared = records.get(pos["prepared_cert"]) == prepared_token(program)
    propagated = records.get(pos["propagated_cert"]) == propagated_token(program)
    a = outcome_at(records, pos["front_a"], program, "alice")
    b = outcome_at(records, pos["front_b"], program, "bob")
    front_pair = a is not None and b is not None
    front_empty = pos["front_a"] not in records and pos["front_b"] not in records
    if not prepared and not propagated and front_empty:
        return 0
    if prepared and not propagated and front_empty:
        return 1
    if prepared and propagated and front_empty:
        return 2
    if prepared and propagated and front_pair:
        return 3
    return -1


def link_unitary(link: int) -> sp.Matrix:
    if link == 0:
        return q7.I2
    if link == 1:
        return q7.S
    raise ValueError("declared finite repertoire has link in {0,1}")


def transported_bob_observables(link: int) -> tuple[sp.Matrix, sp.Matrix]:
    transport = link_unitary(link)
    return tuple(sp.simplify(transport * observable * q7.dagger(transport)) for observable in q7.BOB)


def program_table(program: Program, visibility=sp.Integer(1)) -> dict[tuple[int, int, int, int], sp.Expr]:
    rho = q7.bell_density(program.phase, visibility)
    return q7.joint_probability_table(rho, q7.ALICE, transported_bob_observables(program.link))


def program_branch_state(program: Program, a: int, b: int) -> tuple[sp.Expr, sp.Matrix]:
    rho = q7.bell_density(program.phase)
    bob = transported_bob_observables(program.link)
    joint = sp.kronecker_product(
        q7.projector(q7.ALICE[program.setting_a], a),
        q7.projector(bob[program.setting_b], b),
    )
    branch = sp.simplify(joint * rho * joint)
    weight = q7.trace(branch)
    return weight, sp.simplify(branch / weight)


def prepare_unitary(phase: int) -> sp.Matrix:
    prepare_h = q7.embed_single(q7.H, 4, 0)
    entangle = q7.cnot_operator(4, 0, 1)
    phase_gate = q7.embed_single(q7.Z if phase else q7.I2, 4, 0)
    return sp.simplify(phase_gate * entangle * prepare_h)


def propagation_unitary() -> sp.Matrix:
    return sp.simplify(q7.swap_operator(4, 1, 3) * q7.swap_operator(4, 0, 2))


def decoded_work_state(records: Records, program: Program) -> sp.Matrix:
    """Reconstruct the four-work-qubit state from immutable records."""

    stage = program_stage(records, program)
    initial = q7.kron_all((q7.KET0, q7.KET0, q7.KET0, q7.KET0))
    if stage == 0:
        return q7.density(initial)
    if stage == 1:
        return q7.density(sp.simplify(prepare_unitary(program.phase) * initial))
    if stage == 2:
        propagated = sp.simplify(propagation_unitary() * prepare_unitary(program.phase) * initial)
        return q7.density(propagated)
    if stage == 3:
        pos = motif_positions(program)
        a = outcome_at(records, pos["front_a"], program, "alice")
        b = outcome_at(records, pos["front_b"], program, "bob")
        if a is None or b is None:
            raise ValueError("committed stage lacks an outcome")
        post_front = program_branch_state(program, a, b)[1]
        return sp.kronecker_product(q7.density(q7.KET00), post_front)
    raise ValueError("record pattern is not a valid microstage")


def advance_program(records: Records, program: Program, seed: Fraction = Fraction(1, 3)) -> Records:
    """Apply the one exact next-stage rule for an admitted motif."""

    if program not in admitted_programs(records):
        raise ValueError("program is not the local collision winner")
    pos = motif_positions(program)
    stage = program_stage(records, program)
    advanced = dict(records)
    if stage == 0:
        advanced[pos["prepared_cert"]] = prepared_token(program)
    elif stage == 1:
        advanced[pos["propagated_cert"]] = propagated_token(program)
    elif stage == 2:
        table = program_table(program)
        distribution = q7.context_distribution(table, program.setting_a, program.setting_b)
        a, b = q7.sample_distribution(distribution, seed)
        advanced[pos["front_a"]] = outcome_token(program, "alice", a)
        advanced[pos["front_b"]] = outcome_token(program, "bob", b)
    elif stage == 3:
        return advanced
    else:
        raise ValueError("invalid stage pattern")
    return advanced


def advance_in_order(records: Records, order: Iterable[Program], seeds: dict[tuple, Fraction]) -> Records:
    advanced = dict(records)
    for program in order:
        advanced = advance_program(advanced, program, seeds[program_key(program)])
    return advanced


def transform_program(
    program: Program,
    rotation: tuple[Vec, Vec, Vec] | None = None,
    translation: Vec = (0, 0, 0),
) -> Program:
    rotation = rotation or ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return Program(
        add(rotate(program.anchor, rotation), translation),
        rotate(program.direction, rotation),
        rotate(program.transverse, rotation),
        program.phase,
        program.setting_a,
        program.setting_b,
        program.link,
        program.priority,
        program.nonce,
    )


def transform_records(
    records: Records,
    rotation: tuple[Vec, Vec, Vec] | None = None,
    translation: Vec = (0, 0, 0),
) -> Records:
    rotation = rotation or ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return {add(rotate(site, rotation), translation): token for site, token in records.items()}


def distribution_equal(left: dict, right: dict) -> bool:
    return left.keys() == right.keys() and all(q7.exact_equal(left[key], right[key]) for key in left)


def chsh(table: dict[tuple[int, int, int, int], sp.Expr]) -> sp.Expr:
    correlations = {
        (x, y): q7.correlation(table, x, y)
        for x, y in product((0, 1), repeat=2)
    }
    return sp.simplify(
        correlations[(0, 0)]
        + correlations[(0, 1)]
        + correlations[(1, 0)]
        - correlations[(1, 1)]
    )


def token_projector(index: int) -> sp.Matrix:
    vector = sp.Matrix([1, index + 1])
    return sp.simplify(vector * q7.dagger(vector) / (q7.dagger(vector) * vector)[0])


def source_contract() -> None:
    section("A - Source and authority boundary")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").split())
    q7_note = Q7_NOTE.read_text(encoding="utf-8").lower()
    schedule = SCHEDULE_NOTE.read_text(encoding="utf-8").lower()
    pair = PAIR_NOTE.read_text(encoding="utf-8").lower()
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note changes no live surface", "changes no axiom, registry, or audit" in note)
    check("A note names CFSI-QH11", "cfsi-qh11" in note)
    check("A predecessor CFSI-Q7 construction exists", "pass=146" in q7_note or "cfsi-q7" in q7_note)
    check("A schedule acceptance control is connected", "causal input relation" in schedule)
    check("A exact-law-value pair is connected", "one-record transcript" in pair)
    check("A current site carrier remains M2", "M_2(C)" in axioms)
    check("A current predictive state qualification remains records", "A state is a configuration of records." in axioms)


def homogeneous_motif_and_covariance() -> None:
    section("B - Homogeneous finite motif decoder and cubic covariance")
    program = Program((7, -3, 5), (1, 0, 0), (0, 1, 0), 1, 0, 1, 1, 3, "alpha")
    pos = motif_positions(program)
    check("B the homogeneous motif has eleven distinct physical sites", len(set(pos.values())) == 11)
    check("B orientation is an ordered orthogonal cubic pair", program.direction in AXES and program.transverse in AXES and dot(program.direction, program.transverse) == 0)
    check("B the derived third axis is a positive cubic axis", cross(program.direction, program.transverse) in AXES)
    check("B both coherent source and propagation gates lie on nearest-neighbor edges", l1(pos["source_a"], pos["source_b"]) == 1 and l1(pos["source_a"], pos["front_a"]) == 1 and l1(pos["source_b"], pos["front_b"]) == 1)
    check("B both stage certificate writes are nearest a work carrier", l1(pos["prepared_cert"], pos["source_a"]) == 1 and l1(pos["propagated_cert"], pos["front_a"]) == 1)
    diameter = max(l1(left, right) for left in pos.values() for right in pos.values())
    check("B motif support has finite L1 diameter five", diameter == 5)
    records = program_records(program)
    check("B one local decoder recovers the program without an address schedule", detect_programs(records) == {program})

    rotations = proper_cubic_rotations()
    check("B the cubic proper-rotation group has 24 elements", len(rotations) == 24)
    rotation_covariant = True
    for rotation in rotations:
        transformed = transform_program(program, rotation)
        transformed_records = transform_records(records, rotation)
        rotation_covariant &= detect_programs(transformed_records) == {transformed}
        rotation_covariant &= cross(transformed.direction, transformed.transverse) == rotate(cross(program.direction, program.transverse), rotation)
    check("B decoder is covariant under all 24 proper cubic rotations", rotation_covariant)

    translations = ((0, 0, 0), (11, -7, 2), (-4, 9, -13))
    check(
        "B decoder is exactly translation covariant",
        all(
            detect_programs(transform_records(records, translation=shift))
            == {transform_program(program, translation=shift)}
            for shift in translations
        ),
    )


def collision_arbitration() -> None:
    section("C - Static local collision arbitration")
    base = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0, 3, "high")
    normal = cross(base.direction, base.transverse)
    overlap = Program(add(base.anchor, normal), base.direction, base.transverse, 1, 1, 1, 1, 1, "low")
    check("C chosen motifs have overlapping full footprints", conflicts(base, overlap))
    check("C their immutable program-record sites remain compatible", set(program_records(base)).isdisjoint(program_records(overlap)))
    records = merge_record_sets(program_records(base), program_records(overlap))
    detected = detect_programs(records)
    check("C decoder sees both overlapping ready motifs", detected == {base, overlap})
    check("C unique higher recorded priority wins the overlap", admitted_programs(records) == {base})
    after_winner_starts = advance_program(records, base)
    check("C immutable arbitration keeps the loser rejected after the winner starts", admitted_programs(after_winner_starts) == {base})
    check("C a winner certificate occupying loser work support makes the loser stage invalid", program_stage(after_winner_starts, overlap) == -1)

    tied_base = Program(base.anchor, base.direction, base.transverse, base.phase, base.setting_a, base.setting_b, base.link, 2, base.nonce)
    tied_overlap = Program(overlap.anchor, overlap.direction, overlap.transverse, overlap.phase, overlap.setting_a, overlap.setting_b, overlap.link, 2, overlap.nonce)
    tied_records = merge_record_sets(program_records(tied_base), program_records(tied_overlap))
    check("C an exact priority tie blocks both conflicting motifs", admitted_programs(tied_records) == set())

    distant = Program((8, 0, 0), (1, 0, 0), (0, 1, 0), 0, 1, 0, 0, 0, "far")
    combined = merge_record_sets(records, program_records(distant))
    check("C a distant disjoint motif remains independently admitted", admitted_programs(combined) == {base, distant})
    winners = admitted_programs(combined)
    check("C every pair of admitted motifs has disjoint full support", all(not conflicts(left, right) for left in winners for right in winners if left != right))

    rotation = proper_cubic_rotations()[7]
    rotated_records = transform_records(records, rotation, (5, -2, 9))
    rotated_base = transform_program(base, rotation, (5, -2, 9))
    check("C collision winner transforms covariantly", admitted_programs(rotated_records) == {rotated_base})


def exact_microstages_and_record_decoder() -> None:
    section("D - Append-only microstage certificates and work-state reconstruction")
    program = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 1, 0, 0, 0, 2, "stage")
    records0 = program_records(program)
    check("D program-only records decode the blank stage", program_stage(records0, program) == 0)
    state0 = decoded_work_state(records0, program)

    records1 = advance_program(records0, program)
    check("D first deterministic transition appends only the prepared certificate", set(records1) - set(records0) == {motif_positions(program)["prepared_cert"]})
    check("D prepared certificate decodes stage one", program_stage(records1, program) == 1)
    state1 = decoded_work_state(records1, program)
    check("D stage-one state is the exact local preparation unitary output", q7.exact_equal(state1, sp.simplify(prepare_unitary(program.phase) * state0 * q7.dagger(prepare_unitary(program.phase)))))

    records2 = advance_program(records1, program)
    check("D second deterministic transition appends only the propagated certificate", set(records2) - set(records1) == {motif_positions(program)["propagated_cert"]})
    check("D two certificates decode the propagated stage", program_stage(records2, program) == 2)
    state2 = decoded_work_state(records2, program)
    check("D stage-two state is the exact disjoint-SWAP output", q7.exact_equal(state2, sp.simplify(propagation_unitary() * state1 * q7.dagger(propagation_unitary()))))

    records3 = advance_program(records2, program, Fraction(7, 20))
    pos = motif_positions(program)
    check("D sampled commit appends exactly the two front outcomes", set(records3) - set(records2) == {pos["front_a"], pos["front_b"]})
    check("D outcome records decode the committed stage", program_stage(records3, program) == 3)
    state3 = decoded_work_state(records3, program)
    check("D committed decoder returns a normalized work state", q7.exact_equal(q7.trace(state3), 1))
    source_blank = sp.kronecker_product(q7.density(q7.KET00), sp.eye(4))
    check("D committed decoder keeps the coherent source pair exactly blank", q7.exact_equal(q7.trace(source_blank * state3), 1))
    check("D every transition preserves all earlier records verbatim", all(records1[site] == token for site, token in records0.items()) and all(records2[site] == token for site, token in records1.items()) and all(records3[site] == token for site, token in records2.items()))
    check("D a complete stage sequence uses no unrecorded microstage counter", [program_stage(records, program) for records in (records0, records1, records2, records3)] == [0, 1, 2, 3])

    invalid = dict(records1)
    invalid[pos["front_a"]] = outcome_token(program, "alice", 1)
    check("D a torn half-commit is rejected rather than silently decoded", program_stage(invalid, program) == -1)


def mixed_frame_transport_and_bell_law() -> None:
    section("E - Mixed-frame link transport and exact Bell laws")
    common = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0, 2, "frame0")
    twisted = Program((7, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 1, 2, "frame1")
    common_table = program_table(common)
    twisted_table = program_table(twisted)
    check("E common-frame program reaches exact Tsirelson CHSH", q7.exact_equal(chsh(common_table), 2 * sp.sqrt(2)))
    check("E quarter-turn Bob link changes the exact relative-frame CHSH", q7.exact_equal(chsh(twisted_table), sp.sqrt(2)))
    check("E the recorded relational link changes future transcript probabilities", any(not q7.exact_equal(common_table[key], twisted_table[key]) for key in common_table))
    check("E every mixed-frame context remains normalized", all(q7.exact_equal(sum(q7.context_distribution(twisted_table, x, y).values()), 1) for x, y in product((0, 1), repeat=2)))
    check("E mixed-frame transport remains no-signalling", all(q7.exact_equal(sum(twisted_table[(x, y, a, b)] for b in q7.OUTCOMES), sp.Rational(1, 2)) for x, y, a in product((0, 1), (0, 1), q7.OUTCOMES)) and all(q7.exact_equal(sum(twisted_table[(x, y, a, b)] for a in q7.OUTCOMES), sp.Rational(1, 2)) for x, y, b in product((0, 1), (0, 1), q7.OUTCOMES)))

    link = q7.S
    local_change = q7.H
    changed_local_bob = tuple(sp.simplify(local_change * observable * q7.dagger(local_change)) for observable in q7.BOB)
    changed_link = sp.simplify(link * q7.dagger(local_change))
    original_physical = transported_bob_observables(1)
    changed_physical = tuple(sp.simplify(changed_link * observable * q7.dagger(changed_link)) for observable in changed_local_bob)
    check("E a Bob-local coordinate change plus inverse link update preserves all physical effects", all(q7.exact_equal(original_physical[index], changed_physical[index]) for index in range(2)))
    check("E one pointer axis cannot detect the tested twist", q7.exact_equal(q7.S * q7.Z * q7.dagger(q7.S), q7.Z))
    check("E a second noncommuting axis detects the tested twist", not q7.exact_equal(q7.S * q7.X * q7.dagger(q7.S), q7.X))


def causal_order_and_projective_joint_law() -> None:
    section("F - Disjoint event order and finite projective law")
    left = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0, 2, "left")
    right = Program((8, 0, 0), (0, 1, 0), (0, 0, 1), 1, 1, 0, 1, 2, "right")
    initial = merge_record_sets(program_records(left), program_records(right))
    check("F two disjoint programs are both admitted", admitted_programs(initial) == {left, right})

    stage2 = initial
    for _ in range(2):
        stage2 = advance_in_order(stage2, (left, right), {program_key(left): Fraction(1, 5), program_key(right): Fraction(4, 5)})
    check("F both independent motifs reach the propagated stage", program_stage(stage2, left) == 2 and program_stage(stage2, right) == 2)
    seeds = {program_key(left): Fraction(7, 20), program_key(right): Fraction(13, 20)}
    left_first = advance_in_order(stage2, (left, right), seeds)
    right_first = advance_in_order(stage2, (right, left), seeds)
    check("F event-addressed sampling makes disjoint commit order pathwise invariant", left_first == right_first)
    check("F both commit orders end in the same pair of completed record motifs", program_stage(left_first, left) == 3 and program_stage(left_first, right) == 3)

    left_dist = q7.context_distribution(program_table(left), left.setting_a, left.setting_b)
    right_dist = q7.context_distribution(program_table(right), right.setting_a, right.setting_b)
    joint = {
        (left_outcome, right_outcome): sp.simplify(left_weight * right_weight)
        for left_outcome, left_weight in left_dist.items()
        for right_outcome, right_weight in right_dist.items()
    }
    check("F two-cell joint branch law has sixteen histories", len(joint) == 16)
    check("F two-cell joint branch law normalizes exactly", q7.exact_equal(sum(joint.values()), 1))
    left_marginal = {
        outcome: sp.simplify(sum(weight for (left_outcome, _), weight in joint.items() if left_outcome == outcome))
        for outcome in left_dist
    }
    check("F joint-law marginalization recovers the first local instrument", distribution_equal(left_marginal, left_dist))


def record_markov_sufficiency() -> None:
    section("G - Record-Markov sufficiency for the declared finite repertoire")
    program = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 1, 0, 0, 2, "markov")
    records = program_records(program)
    clone = dict(records)
    check("G equal complete record configurations decode equal program sets", detect_programs(records) == detect_programs(clone))
    check("G equal complete records decode equal stages and work states", program_stage(records, program) == program_stage(clone, program) and q7.exact_equal(decoded_work_state(records, program), decoded_work_state(clone, program)))
    check("G equal complete records decode equal next transcript tables", distribution_equal(program_table(program), program_table(next(iter(detect_programs(clone))))))

    link0 = program
    link1 = Program(program.anchor, program.direction, program.transverse, program.phase, program.setting_a, program.setting_b, 1, program.priority, program.nonce)
    records_link0 = program_records(link0)
    records_link1 = program_records(link1)
    stripped_link0 = {site: token for site, token in records_link0.items() if token[2] != "link"}
    stripped_link1 = {site: token for site, token in records_link1.items() if token[2] != "link"}
    check("G deleting the binary link record merges the two finite descriptions", stripped_link0 == stripped_link1)
    check("G the merged link descriptions have different future laws", any(not q7.exact_equal(program_table(link0)[key], program_table(link1)[key]) for key in program_table(link0)))

    phase1 = Program(program.anchor, program.direction, program.transverse, 1, program.setting_a, program.setting_b, program.link, program.priority, program.nonce)
    stripped_phase0 = {site: token for site, token in records.items() if token[2] != "phase"}
    stripped_phase1 = {site: token for site, token in program_records(phase1).items() if token[2] != "phase"}
    check("G deleting the phase record merges opposite coherent preparations", stripped_phase0 == stripped_phase1)
    check("G opposite merged preparations retain different future tables", any(not q7.exact_equal(program_table(program)[key], program_table(phase1)[key]) for key in program_table(program)))

    prepared = advance_program(records, program)
    stripped_stage0 = {site: token for site, token in records.items() if token[0] != "stage"}
    stripped_stage1 = {site: token for site, token in prepared.items() if token[0] != "stage"}
    check("G deleting stage certificates merges blank and prepared records", stripped_stage0 == stripped_stage1)
    check("G the merged stages represent different work states", not q7.exact_equal(decoded_work_state(records, program), decoded_work_state(prepared, program)))

    high = Program((20, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0, 3, "p-high")
    low = Program(add(high.anchor, cross(high.direction, high.transverse)), high.direction, high.transverse, 0, 0, 0, 0, 1, "p-low")
    swapped_high = Program(high.anchor, high.direction, high.transverse, high.phase, high.setting_a, high.setting_b, high.link, 1, high.nonce)
    swapped_low = Program(low.anchor, low.direction, low.transverse, low.phase, low.setting_a, low.setting_b, low.link, 3, low.nonce)
    first_collision = merge_record_sets(program_records(high), program_records(low))
    second_collision = merge_record_sets(program_records(swapped_high), program_records(swapped_low))
    strip_priority = lambda configuration: {site: token for site, token in configuration.items() if token[2] != "priority"}
    check("G deleting collision-priority records merges opposite winner programs", strip_priority(first_collision) == strip_priority(second_collision))
    check("G collision priority changes the next admitted event", admitted_programs(first_collision) == {high} and admitted_programs(second_collision) == {swapped_low})


def exact_law_value_ablation() -> None:
    section("H - Paired exact-law-value ablation")
    program = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0, 2, "value")
    ideal = program_table(program, sp.Integer(1))
    noisy = program_table(program, sp.Rational(1, 2))
    check("H visibility one gives exact Bell-optimal CHSH", q7.exact_equal(chsh(ideal), 2 * sp.sqrt(2)))
    check("H visibility one half gives exact sub-Bell CHSH", q7.exact_equal(chsh(noisy), sp.sqrt(2)))
    check("H both exact law values normalize in every context", all(q7.exact_equal(sum(q7.context_distribution(table, x, y).values()), 1) for table in (ideal, noisy) for x, y in product((0, 1), repeat=2)))
    check("H both exact law values retain full outcome support", all(table[key].is_positive for table in (ideal, noisy) for key in table))
    check("H identical homogeneous decoders can carry different transcript laws", any(not q7.exact_equal(ideal[key], noisy[key]) for key in ideal))
    seed = Fraction(19, 50)
    ideal_outcome = q7.sample_distribution(q7.context_distribution(ideal, 0, 0), seed)
    noisy_outcome = q7.sample_distribution(q7.context_distribution(noisy, 0, 0), seed)
    check("H one event-addressed seed separates the exact law values", ideal_outcome != noisy_outcome)


def finite_program_alphabet_and_domain() -> None:
    section("I - Finite program alphabet in the current one-site carrier")
    program = Program((0, 0, 0), (1, 0, 0), (0, 1, 0), 1, 1, 0, 1, 3, "alphabet")
    records = program_records(program)
    records = advance_program(records, program)
    records = advance_program(records, program)
    records = advance_program(records, program, Fraction(2, 5))
    tokens = sorted(set(records.values()), key=repr)
    projectors = [token_projector(index) for index in range(len(tokens))]
    check("I every finite symbolic record token has an M2 rank-one encoding", all(q7.exact_equal(projector * projector, projector) and q7.exact_equal(q7.trace(projector), 1) for projector in projectors))
    check("I the finite token encoding is injective", all(not q7.exact_equal(projectors[left], projectors[right]) for left in range(len(projectors)) for right in range(left + 1, len(projectors))))
    check("I role, nonce, value, stage, and outcome are explicit record data", any(token[0] == "program" for token in tokens) and any(token[0] == "stage" for token in tokens) and any(token[0] == "outcome" for token in tokens))
    check("I open-versus-recorded remains external record-map status", all(site not in records for site in (motif_positions(program)["source_a"], motif_positions(program)["source_b"])))
    check("I the construction still uses eleven physical M2 sites per motif", len(footprint(program)) == 11)


def documentation_contract() -> None:
    section("J - Scope, residual, and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "cfsi-qh11",
        "translation-covariant",
        "all 24 proper cubic rotations",
        "strict-priority",
        "collision",
        "prepared certificate",
        "propagated certificate",
        "record-markov sufficiency",
        "relational link",
        "one binary link bit",
        "exact law value",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    for phrase in required:
        check(f"J note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    homogeneous_motif_and_covariance()
    collision_arbitration()
    exact_microstages_and_record_decoder()
    mixed_frame_transport_and_bell_law()
    causal_order_and_projective_joint_law()
    record_markov_sufficiency()
    exact_law_value_ablation()
    finite_program_alphabet_and_domain()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
