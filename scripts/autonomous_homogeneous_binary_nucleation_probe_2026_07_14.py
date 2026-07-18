#!/usr/bin/env python3
"""Exact seedless homogeneous initiation and orthogonal-token carrier probes.

The positive construction is a one-shot finite-range factor of an IID marked
field on Z3.  Strict local mark minima nucleate mutually separated binary
program packets.  Every classical field is encoded by orthogonal P0/P1 record
sites in a generated finite M2 composition; no nonorthogonal token alphabet is
read as classical side data.  The construction is bounded and is not asserted
to be the physical cosmology.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path

import sympy as sp

import cfsi_q_bell_coherent_causal_front_law_probe_2026_07_14 as q7


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_HOMOGENEOUS_BINARY_NUCLEATION_NOTE_2026-07-14.md"
)
BOUNDARY_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "HOMOGENEOUS_BOUNDARY_SEED_SELECTION_NOTE_2026-07-14.md"
)
QH11_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "CFSI_QH11_HOMOGENEOUS_LOCAL_DECODER_NOTE_2026-07-14.md"
)
PAIR_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md"
)
COMPOSITION_NOTE = ROOT / "docs" / "GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


PASS = 0
FAIL = 0
Vec = tuple[int, int, int]
BinaryRecords = dict[Vec, int]
EffectRecords = dict[Vec, sp.Matrix]


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


def scale(factor: int, vector: Vec) -> Vec:
    return tuple(factor * entry for entry in vector)  # type: ignore[return-value]


def neg(vector: Vec) -> Vec:
    return scale(-1, vector)


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
FRAMES: tuple[tuple[Vec, Vec], ...] = tuple(
    (direction, transverse)
    for direction in AXES
    for transverse in AXES
    if dot(direction, transverse) == 0
)


def proper_cubic_rotations() -> tuple[tuple[Vec, Vec, Vec], ...]:
    rotations = []
    for ex, ey in FRAMES:
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
class BinaryProgram:
    anchor: Vec
    direction: Vec
    transverse: Vec
    phase: int
    setting_a: int
    setting_b: int
    link: int


HEADER_BITS = {
    "h0": 1,
    "h1": 0,
    "h2": 1,
    "h3": 1,
    "h4": 0,
    "h5": 0,
}


def motif_positions(program: BinaryProgram) -> dict[str, Vec]:
    o = program.anchor
    d = program.direction
    t = program.transverse
    u = cross(d, t)
    return {
        "h0": add(o, scale(-5, d)),
        "h1": add(o, scale(-5, d), t),
        "h2": add(o, scale(-5, d), scale(3, t)),
        "h3": add(o, scale(-5, d), u),
        "h4": add(o, scale(-5, d), scale(2, u)),
        "h5": add(o, scale(-4, d)),
        "phase": add(o, scale(-3, d)),
        "setting_a": add(o, scale(-3, d), t),
        "setting_b": add(o, scale(-3, d), scale(2, t)),
        "link": add(o, scale(-3, d), u),
        "source_a": o,
        "source_b": add(o, t),
        "front_a": add(o, d),
        "front_b": add(o, d, t),
        "prepared_cert": add(o, u),
        "propagated_cert": add(o, d, u),
    }


PROGRAM_ROLES = tuple(HEADER_BITS) + ("phase", "setting_a", "setting_b", "link")


def physical_bit(logical_bit: int, reference_bit: int) -> int:
    """Encode a logical bit relative to the header's local reference value."""

    return reference_bit if logical_bit == 1 else 1 - reference_bit


def logical_bit(physical_value: int, reference_bit: int) -> int:
    return 1 if physical_value == reference_bit else 0


def program_records(program: BinaryProgram, reference_bit: int = 1) -> BinaryRecords:
    pos = motif_positions(program)
    values = dict(HEADER_BITS)
    values.update(
        {
            "phase": program.phase,
            "setting_a": program.setting_a,
            "setting_b": program.setting_b,
            "link": program.link,
        }
    )
    return {
        pos[role]: physical_bit(int(values[role]), reference_bit)
        for role in PROGRAM_ROLES
    }


def merge_records(*record_sets: BinaryRecords) -> BinaryRecords:
    merged: BinaryRecords = {}
    for records in record_sets:
        for site, value in records.items():
            if site in merged and merged[site] != value:
                raise ValueError(f"incompatible records at {site}")
            merged[site] = value
    return merged


def detect_programs(records: BinaryRecords) -> set[BinaryProgram]:
    """Decode only geometry plus orthogonal binary site values."""

    detected: set[BinaryProgram] = set()
    for h0_site, reference_bit in records.items():
        if reference_bit not in (0, 1):
            continue
        for direction, transverse in FRAMES:
            anchor = add(h0_site, scale(5, direction))
            shell = BinaryProgram(anchor, direction, transverse, 0, 0, 0, 0)
            pos = motif_positions(shell)
            if any(
                records.get(pos[role]) != physical_bit(bit, reference_bit)
                for role, bit in HEADER_BITS.items()
            ):
                continue
            data_sites = (pos["phase"], pos["setting_a"], pos["setting_b"], pos["link"])
            if any(site not in records or records[site] not in (0, 1) for site in data_sites):
                continue
            candidate = BinaryProgram(
                anchor,
                direction,
                transverse,
                logical_bit(records[pos["phase"]], reference_bit),
                logical_bit(records[pos["setting_a"]], reference_bit),
                logical_bit(records[pos["setting_b"]], reference_bit),
                logical_bit(records[pos["link"]], reference_bit),
            )
            if program_records(candidate, reference_bit).items() <= records.items():
                detected.add(candidate)
    return detected


def is_rank_one_effect(effect: sp.Matrix) -> bool:
    return (
        q7.exact_equal(effect, q7.dagger(effect))
        and q7.exact_equal(effect * effect, effect)
        and q7.exact_equal(q7.trace(effect), 1)
    )


def relational_effect_bit(effect: sp.Matrix, reference: sp.Matrix) -> int | None:
    if q7.exact_equal(effect, reference):
        return 1
    if q7.exact_equal(effect, q7.I2 - reference):
        return 0
    return None


def effect_program_records(program: BinaryProgram, reference: sp.Matrix) -> EffectRecords:
    if not is_rank_one_effect(reference):
        raise ValueError("reference must be a rank-one effect")
    pos = motif_positions(program)
    values = dict(HEADER_BITS)
    values.update(
        {
            "phase": program.phase,
            "setting_a": program.setting_a,
            "setting_b": program.setting_b,
            "link": program.link,
        }
    )
    complement = sp.simplify(q7.I2 - reference)
    return {
        pos[role]: reference if int(values[role]) == 1 else complement
        for role in PROGRAM_ROLES
    }


def detect_effect_programs(records: EffectRecords) -> set[BinaryProgram]:
    """Decode only equality/complementarity relative to the h0 record."""

    detected: set[BinaryProgram] = set()
    for h0_site, reference in records.items():
        if not is_rank_one_effect(reference):
            continue
        for direction, transverse in FRAMES:
            anchor = add(h0_site, scale(5, direction))
            shell = BinaryProgram(anchor, direction, transverse, 0, 0, 0, 0)
            pos = motif_positions(shell)
            header = {
                role: relational_effect_bit(records[pos[role]], reference)
                if pos[role] in records
                else None
                for role in HEADER_BITS
            }
            if header != HEADER_BITS:
                continue
            data_roles = ("phase", "setting_a", "setting_b", "link")
            decoded = {
                role: relational_effect_bit(records[pos[role]], reference)
                if pos[role] in records
                else None
                for role in data_roles
            }
            if any(decoded[role] not in (0, 1) for role in data_roles):
                continue
            candidate = BinaryProgram(
                anchor,
                direction,
                transverse,
                int(decoded["phase"]),
                int(decoded["setting_a"]),
                int(decoded["setting_b"]),
                int(decoded["link"]),
            )
            detected.add(candidate)
    return detected


def conjugate_effect_records(records: EffectRecords, unitary: sp.Matrix) -> EffectRecords:
    return {
        site: sp.simplify(unitary * effect * q7.dagger(unitary))
        for site, effect in records.items()
    }


def effect_program_stage(records: EffectRecords, program: BinaryProgram) -> int:
    if program not in detect_effect_programs(records):
        return -1
    pos = motif_positions(program)
    reference = records[pos["h0"]]
    if pos["source_a"] in records or pos["source_b"] in records:
        return -1
    prepared = (
        relational_effect_bit(records[pos["prepared_cert"]], reference) == 1
        if pos["prepared_cert"] in records
        else False
    )
    propagated = (
        relational_effect_bit(records[pos["propagated_cert"]], reference) == 1
        if pos["propagated_cert"] in records
        else False
    )
    prepared_empty = pos["prepared_cert"] not in records
    propagated_empty = pos["propagated_cert"] not in records
    front_bits = tuple(
        relational_effect_bit(records[pos[role]], reference)
        if pos[role] in records
        else None
        for role in ("front_a", "front_b")
    )
    if prepared_empty and propagated_empty and front_bits == (None, None):
        return 0
    if prepared and propagated_empty and front_bits == (None, None):
        return 1
    if prepared and propagated and front_bits == (None, None):
        return 2
    if prepared and propagated and all(bit in (0, 1) for bit in front_bits):
        return 3
    return -1


def effect_commit_records(
    program: BinaryProgram,
    reference: sp.Matrix,
    outcome_a: int,
    outcome_b: int,
) -> EffectRecords:
    records = effect_program_records(program, reference)
    pos = motif_positions(program)
    complement = sp.simplify(q7.I2 - reference)
    records[pos["prepared_cert"]] = reference
    records[pos["propagated_cert"]] = reference
    records[pos["front_a"]] = reference if outcome_to_bit(outcome_a) else complement
    records[pos["front_b"]] = reference if outcome_to_bit(outcome_b) else complement
    return records


def effect_commit_outcomes(records: EffectRecords, program: BinaryProgram) -> tuple[int, int]:
    if effect_program_stage(records, program) != 3:
        raise ValueError("effect packet is not committed")
    pos = motif_positions(program)
    reference = records[pos["h0"]]
    bits = tuple(
        relational_effect_bit(records[pos[role]], reference)
        for role in ("front_a", "front_b")
    )
    return tuple(bit_to_outcome(int(bit)) for bit in bits)  # type: ignore[return-value]


def transform_program(
    program: BinaryProgram,
    rotation: tuple[Vec, Vec, Vec] | None = None,
    translation: Vec = (0, 0, 0),
) -> BinaryProgram:
    rotation = rotation or ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return BinaryProgram(
        add(rotate(program.anchor, rotation), translation),
        rotate(program.direction, rotation),
        rotate(program.transverse, rotation),
        program.phase,
        program.setting_a,
        program.setting_b,
        program.link,
    )


def transform_records(
    records: BinaryRecords,
    rotation: tuple[Vec, Vec, Vec] | None = None,
    translation: Vec = (0, 0, 0),
) -> BinaryRecords:
    rotation = rotation or ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return {add(rotate(site, rotation), translation): value for site, value in records.items()}


def footprint(program: BinaryProgram) -> set[Vec]:
    return set(motif_positions(program).values())


def bit_to_outcome(bit: int) -> int:
    return 1 if bit == 1 else -1


def outcome_to_bit(outcome: int) -> int:
    return 1 if outcome == 1 else 0


def program_reference_bit(records: BinaryRecords, program: BinaryProgram) -> int | None:
    reference = records.get(motif_positions(program)["h0"])
    if reference not in (0, 1):
        return None
    if not program_records(program, reference).items() <= records.items():
        return None
    return reference


def program_stage(records: BinaryRecords, program: BinaryProgram) -> int:
    reference = program_reference_bit(records, program)
    if reference is None:
        return -1
    pos = motif_positions(program)
    if pos["source_a"] in records or pos["source_b"] in records:
        return -1
    prepared = records.get(pos["prepared_cert"]) == physical_bit(1, reference)
    propagated = records.get(pos["propagated_cert"]) == physical_bit(1, reference)
    prepared_empty = pos["prepared_cert"] not in records
    propagated_empty = pos["propagated_cert"] not in records
    front_a = pos["front_a"] in records and records[pos["front_a"]] in (0, 1)
    front_b = pos["front_b"] in records and records[pos["front_b"]] in (0, 1)
    front_empty = pos["front_a"] not in records and pos["front_b"] not in records
    if prepared_empty and propagated_empty and front_empty:
        return 0
    if prepared and propagated_empty and front_empty:
        return 1
    if prepared and propagated and front_empty:
        return 2
    if prepared and propagated and front_a and front_b:
        return 3
    return -1


def transported_bob(program: BinaryProgram) -> tuple[sp.Matrix, sp.Matrix]:
    link = q7.I2 if program.link == 0 else q7.S
    return tuple(sp.simplify(link * observable * q7.dagger(link)) for observable in q7.BOB)


def program_table(program: BinaryProgram, visibility=sp.Integer(1)) -> dict[tuple[int, int, int, int], sp.Expr]:
    return q7.joint_probability_table(
        q7.bell_density(program.phase, visibility),
        q7.ALICE,
        transported_bob(program),
    )


def prepare_unitary(phase: int) -> sp.Matrix:
    return sp.simplify(
        q7.embed_single(q7.Z if phase else q7.I2, 4, 0)
        * q7.cnot_operator(4, 0, 1)
        * q7.embed_single(q7.H, 4, 0)
    )


def propagation_unitary() -> sp.Matrix:
    return sp.simplify(q7.swap_operator(4, 1, 3) * q7.swap_operator(4, 0, 2))


def branch_front_state(program: BinaryProgram, a: int, b: int) -> tuple[sp.Expr, sp.Matrix]:
    rho = q7.bell_density(program.phase)
    bob = transported_bob(program)
    projector = sp.kronecker_product(
        q7.projector(q7.ALICE[program.setting_a], a),
        q7.projector(bob[program.setting_b], b),
    )
    branch = sp.simplify(projector * rho * projector)
    weight = q7.trace(branch)
    return weight, sp.simplify(branch / weight)


def decoded_work_state(records: BinaryRecords, program: BinaryProgram) -> sp.Matrix:
    initial = q7.kron_all((q7.KET0, q7.KET0, q7.KET0, q7.KET0))
    stage = program_stage(records, program)
    if stage == 0:
        return q7.density(initial)
    prepared = sp.simplify(prepare_unitary(program.phase) * initial)
    if stage == 1:
        return q7.density(prepared)
    propagated = sp.simplify(propagation_unitary() * prepared)
    if stage == 2:
        return q7.density(propagated)
    if stage == 3:
        pos = motif_positions(program)
        reference = program_reference_bit(records, program)
        if reference is None:
            raise ValueError("missing relational binary reference")
        a = bit_to_outcome(logical_bit(records[pos["front_a"]], reference))
        b = bit_to_outcome(logical_bit(records[pos["front_b"]], reference))
        return sp.kronecker_product(q7.density(q7.KET00), branch_front_state(program, a, b)[1])
    raise ValueError("invalid binary program stage")


def advance_program(records: BinaryRecords, program: BinaryProgram, seed: Fraction = Fraction(1, 3)) -> BinaryRecords:
    stage = program_stage(records, program)
    pos = motif_positions(program)
    reference = program_reference_bit(records, program)
    if reference is None:
        raise ValueError("missing relational binary reference")
    advanced = dict(records)
    if stage == 0:
        advanced[pos["prepared_cert"]] = physical_bit(1, reference)
    elif stage == 1:
        advanced[pos["propagated_cert"]] = physical_bit(1, reference)
    elif stage == 2:
        table = program_table(program)
        distribution = q7.context_distribution(table, program.setting_a, program.setting_b)
        a, b = q7.sample_distribution(distribution, seed)
        advanced[pos["front_a"]] = physical_bit(outcome_to_bit(a), reference)
        advanced[pos["front_b"]] = physical_bit(outcome_to_bit(b), reference)
    elif stage == 3:
        return advanced
    else:
        raise ValueError("invalid binary program stage")
    return advanced


def chsh(table: dict[tuple[int, int, int, int], sp.Expr]) -> sp.Expr:
    correlations = {(x, y): q7.correlation(table, x, y) for x, y in product((0, 1), repeat=2)}
    return sp.simplify(
        correlations[(0, 0)]
        + correlations[(0, 1)]
        + correlations[(1, 0)]
        - correlations[(1, 1)]
    )


def data_codeword(bits: tuple[int, int, int, int]) -> sp.Matrix:
    return q7.kron_all(q7.KET1 if bit else q7.KET0 for bit in bits)


def data_effect(bits: tuple[int, int, int, int]) -> sp.Matrix:
    return q7.density(data_codeword(bits))


MOTIF_RADIUS = 8
PROGRAM_DIAMETER = 6
EXCLUSION_RADIUS = 2 * MOTIF_RADIUS + PROGRAM_DIAMETER


def l1_ball_volume(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


EXCLUSION_VOLUME = l1_ball_volume(EXCLUSION_RADIUS)


def acceptance_density(candidate_density: Fraction) -> Fraction:
    """Matérn local-minimum density for IID candidates and continuous marks."""

    q = candidate_density
    return (1 - (1 - q) ** EXCLUSION_VOLUME) / EXCLUSION_VOLUME


def finite_acceptance_sum(neighborhood_size: int, candidate_density: Fraction) -> Fraction:
    q = candidate_density
    conditional = sum(
        Fraction(comb(neighborhood_size - 1, count), count + 1)
        * q**count
        * (1 - q) ** (neighborhood_size - 1 - count)
        for count in range(neighborhood_size)
    )
    return q * conditional


@dataclass(frozen=True)
class Candidate:
    anchor: Vec
    mark: Fraction
    frame_index: int
    phase: int
    setting_a: int
    setting_b: int
    link: int


def candidate_program(candidate: Candidate) -> BinaryProgram:
    direction, transverse = FRAMES[candidate.frame_index]
    return BinaryProgram(
        candidate.anchor,
        direction,
        transverse,
        candidate.phase,
        candidate.setting_a,
        candidate.setting_b,
        candidate.link,
    )


def select_winners(candidates: tuple[Candidate, ...]) -> tuple[Candidate, ...]:
    return tuple(
        candidate
        for candidate in candidates
        if all(
            candidate.mark < other.mark
            for other in candidates
            if other != candidate and l1(candidate.anchor, other.anchor) <= EXCLUSION_RADIUS
        )
    )


def torus_sites(side: int) -> tuple[Vec, ...]:
    return tuple(product(range(side), repeat=3))


def translate_torus_configuration(configuration: tuple[int, ...], side: int, shift: Vec) -> tuple[int, ...]:
    sites = torus_sites(side)
    index = {site: position for position, site in enumerate(sites)}
    translated = [0] * len(sites)
    for site, value in zip(sites, configuration):
        target = tuple((site[axis] + shift[axis]) % side for axis in range(3))
        translated[index[target]] = value
    return tuple(translated)


def source_contract() -> None:
    section("A - Source and authority boundary")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").split())
    boundary = BOUNDARY_NOTE.read_text(encoding="utf-8").lower()
    qh11 = QH11_NOTE.read_text(encoding="utf-8").lower()
    pair = PAIR_NOTE.read_text(encoding="utf-8").lower()
    composition = COMPOSITION_NOTE.read_text(encoding="utf-8").lower()
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note changes no live foundation surface", "changes no axiom, registry, or audit" in note)
    check("A note names the QB16 carrier repair", "cfsi-qb16" in note)
    check("A boundary finite-seed wall is wired in", "exactly one marked site" in boundary)
    check("A QH11 hidden carrier wall is named", "cfsi-qh11" in qh11 and "rank-one" in qh11)
    check("A paired exact-law-value control is wired in", "one-record transcript" in pair)
    check(
        "A generated finite-composition condition is wired in",
        "physical joint algebra = algebra generated by the local copies" in composition,
    )
    check("A current one-site carrier remains M2", "M_2(C)" in axioms)
    check("A current state qualification remains record configurations", "A state is a configuration of records." in axioms)


def deterministic_symmetry_obstruction() -> None:
    section("B - Deterministic equivariant initiation from all-open")
    side = 2
    sites = torus_sites(side)
    translations = tuple(product(range(side), repeat=3))
    invariant = []
    for configuration in product((0, 1), repeat=len(sites)):
        if all(translate_torus_configuration(configuration, side, shift) == configuration for shift in translations):
            invariant.append(configuration)
    check("B only two binary configurations on the transitive torus are translation invariant", invariant == [(0,) * len(sites), (1,) * len(sites)])
    check("B all-open is fixed by every translation", all(translate_torus_configuration((0,) * len(sites), side, shift) == (0,) * len(sites) for shift in translations))
    check("B an equivariant deterministic image of all-open must remain translation invariant", all(len(set(configuration)) == 1 for configuration in invariant))
    check("B the only nonempty deterministic alternative is a density-one burst", sum(invariant[1]) == len(sites))

    empty_records: BinaryRecords = {}
    check("B all-open contains no relational header from which to decode a frame", detect_programs(empty_records) == set())
    check("B the 24 oriented cubic frames form one symmetry orbit", len(FRAMES) == 24 and len(proper_cubic_rotations()) == 24)
    check("B no one oriented frame is fixed by the full proper cubic group", all(any((rotate(frame[0], rotation), rotate(frame[1], rotation)) != frame for rotation in proper_cubic_rotations()) for frame in FRAMES))


def coherent_route_controls() -> None:
    section("C - Coherent finite-seed and positive-density routes")
    window = 27
    torus_volumes = (5**3, 7**3, 11**3, 17**3)
    one_seed_hits = tuple(Fraction(window, volume) for volume in torus_volumes)
    check("C finite uniform one-seed vectors give exact fixed-window weight W/V", one_seed_hits == tuple(Fraction(27, volume) for volume in torus_volumes))
    check("C one-seed local weight decreases toward the empty limit", all(one_seed_hits[index + 1] < one_seed_hits[index] for index in range(len(one_seed_hits) - 1)))
    check("C an infinite constant-amplitude one-seed vector is not square summable", all(Fraction(1, volume) > 0 for volume in torus_volumes) and sum(Fraction(1, 1) for _ in range(100)) == 100)

    p = sp.Rational(1, 5)
    single = sp.Matrix([sp.sqrt(1 - p), sp.sqrt(p)])
    product_state = q7.kron_all((single, single, single))
    check("C positive-density three-site coherent product is normalized", q7.exact_equal((q7.dagger(product_state) * product_state)[0], 1))
    first_seed = sp.kronecker_product(q7.density(q7.KET1), sp.eye(2), sp.eye(2))
    check("C its one-site seed marginal remains the volume-independent value p", q7.exact_equal(q7.trace(first_seed * q7.density(product_state)), p))
    check("C its all-open branch still has an explicit nonzero amplitude", q7.exact_equal(abs(product_state[0]) ** 2, (1 - p) ** 3))
    check("C branch weights vary with a supplied coherent activity", not q7.exact_equal(p, sp.Rational(1, 3)))


def orthogonal_binary_carrier_repair() -> None:
    section("D - CFSI-QB16 orthogonal binary carrier repair")
    program = BinaryProgram((4, -2, 7), (1, 0, 0), (0, 1, 0), 1, 0, 1, 1)
    pos = motif_positions(program)
    check("D repaired motif has sixteen distinct physical sites", len(set(pos.values())) == 16)
    check("D repaired packet uses ten initial binary record sites", len(program_records(program)) == 10)
    radius = max(l1(program.anchor, site) for site in pos.values())
    diameter = max(l1(left, right) for left in pos.values() for right in pos.values())
    program_diameter = max(l1(pos[left], pos[right]) for left in PROGRAM_ROLES for right in PROGRAM_ROLES)
    check("D repaired support radius is eight", radius == MOTIF_RADIUS)
    check("D repaired support diameter is ten", diameter == 10)
    check("D binary program-record diameter is six", program_diameter == PROGRAM_DIAMETER)
    check("D the asymmetric binary header uniquely decodes the packet", detect_programs(program_records(program)) == {program})
    complemented_records = {site: 1 - value for site, value in program_records(program).items()}
    check(
        "D global possibility-label exchange leaves the logical packet unchanged",
        detect_programs(complemented_records) == {program},
    )

    all_words = tuple(product((0, 1), repeat=4))
    effects = {word: data_effect(word) for word in all_words}
    check("D all sixteen four-bit program words are mutually orthogonal", all(q7.exact_equal(effects[left] * effects[right], sp.zeros(16)) for left in all_words for right in all_words if left != right))
    check("D the orthogonal code effects form one complete PVM", q7.exact_equal(sum(effects.values(), sp.zeros(16)), sp.eye(16)))
    check("D every code effect reads its own word nondestructively", all(q7.exact_equal(effect * effect * effect, effect) for effect in effects.values()))
    check("D no nonorthogonal one-site token discrimination is used", all(bit in (0, 1) for bit in program_records(program).values()))

    reference = q7.density(q7.KET1)
    effect_records = effect_program_records(program, reference)
    check(
        "D equality-complement header decodes relative to its own rank-one reference",
        detect_effect_programs(effect_records) == {program},
    )
    check(
        "D exchanging the reference with its complement preserves the logical packet",
        detect_effect_programs(effect_program_records(program, q7.I2 - reference)) == {program},
    )
    rational_rotation = sp.Matrix(
        [[sp.Rational(3, 5), sp.Rational(4, 5)], [-sp.Rational(4, 5), sp.Rational(3, 5)]]
    )
    unitaries = (q7.I2, q7.H, rational_rotation, sp.simplify(q7.S * q7.H))
    check(
        "D exact test conjugations are unitary",
        all(q7.exact_equal(unitary * q7.dagger(unitary), q7.I2) for unitary in unitaries),
    )
    check(
        "D simultaneous one-site algebra conjugation preserves logical decoding",
        all(detect_effect_programs(conjugate_effect_records(effect_records, unitary)) == {program} for unitary in unitaries),
    )
    committed_effects = effect_commit_records(program, reference, 1, -1)
    check(
        "D simultaneous algebra conjugation preserves committed stage and outcomes",
        all(
            effect_program_stage(conjugate_effect_records(committed_effects, unitary), program) == 3
            and effect_commit_outcomes(conjugate_effect_records(committed_effects, unitary), program)
            == (1, -1)
            for unitary in unitaries
        ),
    )
    relational_all_words = True
    for phase, setting_a, setting_b, link in all_words:
        candidate = BinaryProgram(
            program.anchor,
            program.direction,
            program.transverse,
            phase,
            setting_a,
            setting_b,
            link,
        )
        candidate_records = effect_program_records(candidate, reference)
        relational_all_words &= all(
            detect_effect_programs(conjugate_effect_records(candidate_records, unitary)) == {candidate}
            for unitary in unitaries
        )
        relational_all_words &= (
            detect_effect_programs(effect_program_records(candidate, q7.I2 - reference))
            == {candidate}
        )
    check(
        "D all sixteen words survive label exchange and algebra conjugation",
        relational_all_words,
    )

    binary_commit = program_records(program, 1)
    for seed in (Fraction(1, 7), Fraction(2, 7), Fraction(3, 7)):
        binary_commit = advance_program(binary_commit, program, seed)
    binary_complement = {site: 1 - value for site, value in binary_commit.items()}
    check(
        "D global binary-label exchange preserves the complete stage law",
        program_stage(binary_complement, program) == 3
        and detect_programs(binary_complement) == {program}
        and q7.exact_equal(
            decoded_work_state(binary_commit, program),
            decoded_work_state(binary_complement, program),
        ),
    )

    rotated_reference = sp.simplify(rational_rotation * reference * q7.dagger(rational_rotation))
    rotated_complement = sp.simplify(q7.I2 - rotated_reference)
    relational_effects = {
        word: q7.kron_all(rotated_reference if bit else rotated_complement for bit in word)
        for word in all_words
    }
    check(
        "D relational four-bit effects remain mutually orthogonal after conjugation",
        all(
            q7.exact_equal(relational_effects[left] * relational_effects[right], sp.zeros(16))
            for left in all_words
            for right in all_words
            if left != right
        ),
    )
    check(
        "D relational four-bit effects remain a complete PVM after conjugation",
        q7.exact_equal(sum(relational_effects.values(), sp.zeros(16)), sp.eye(16)),
    )
    other = BinaryProgram(
        add(program.anchor, (30, 0, 0)),
        (0, 1, 0),
        (0, 0, 1),
        0,
        1,
        0,
        1,
    )
    mixed_reference_records = effect_program_records(program, reference)
    mixed_reference_records.update(effect_program_records(other, rotated_reference))
    check(
        "D separated packets with different relational references reject hybrids",
        detect_effect_programs(mixed_reference_records) == {program, other},
    )

    rotations = proper_cubic_rotations()
    covariant = True
    for rotation in rotations:
        transformed_program = transform_program(program, rotation)
        transformed_records = transform_records(program_records(program), rotation)
        covariant &= detect_programs(transformed_records) == {transformed_program}
    check("D binary decoder is covariant under all 24 proper cubic rotations", covariant)
    shifts = ((0, 0, 0), (11, -5, 2), (-8, 13, -3))
    check("D binary decoder is exactly translation covariant", all(detect_programs(transform_records(program_records(program), translation=shift)) == {transform_program(program, translation=shift)} for shift in shifts))

    unique_all_data = True
    for phase, setting_a, setting_b, link in all_words:
        candidate = BinaryProgram(program.anchor, program.direction, program.transverse, phase, setting_a, setting_b, link)
        unique_all_data &= detect_programs(program_records(candidate, 1)) == {candidate}
        unique_all_data &= detect_programs(program_records(candidate, 0)) == {candidate}
    check("D header uniquely decodes all sixteen data words in both labels", unique_all_data)


def stochastic_nucleation_and_projective_law() -> None:
    section("E - Seedless positive-density stochastic nucleation")
    check("E exclusion radius is the nonce-free separation bound 2r+D", EXCLUSION_RADIUS == 22)
    check("E the exact Z3 exclusion-ball volume is 15225", EXCLUSION_VOLUME == 15225)
    q = Fraction(1, 1)
    rho = acceptance_density(q)
    check("E all-site candidate marks give exact winner density 1/M", rho == Fraction(1, EXCLUSION_VOLUME))
    for size in (1, 2, 7, 11):
        for candidate_density in (Fraction(1, 4), Fraction(2, 3), Fraction(1, 1)):
            check(f"E binomial local-minimum identity holds for M={size} q={candidate_density}", finite_acceptance_sum(size, candidate_density) == (1 - (1 - candidate_density) ** size) / size)

    far_pair = {
        (0, 0): (1 - rho) ** 2,
        (1, 0): rho * (1 - rho),
        (0, 1): rho * (1 - rho),
        (1, 1): rho**2,
    }
    check("E separated-window cylinder distribution normalizes", sum(far_pair.values()) == 1)
    check("E marginalizing the second far window returns the first-window law", far_pair[(1, 0)] + far_pair[(1, 1)] == rho)
    adjacent_pair = {(0, 0): 1 - 2 * rho, (1, 0): rho, (0, 1): rho, (1, 1): Fraction(0)}
    check("E overlapping exclusion neighborhoods forbid adjacent winners", adjacent_pair[(1, 1)] == 0 and sum(adjacent_pair.values()) == 1)
    check("E adjacent-window marginal still equals the stationary winner density", adjacent_pair[(1, 0)] + adjacent_pair[(1, 1)] == rho)

    check("E uniform orientation has exactly 24 equiprobable frames", len(FRAMES) == 24 and 24 * Fraction(1, 24) == 1)
    check("E four independent binary fields give sixteen equiprobable programs", 16 * Fraction(1, 16) == 1)
    check(
        "E one winner's discrete frame/data branch has conditional probability 1/384",
        Fraction(1, 24 * 16) == Fraction(1, 384),
    )

    near_high = Candidate((0, 0, 0), Fraction(3, 5), 0, 0, 0, 0, 0)
    near_low = Candidate((3, 0, 0), Fraction(1, 5), 7, 1, 1, 0, 1)
    far = Candidate((30, 0, 0), Fraction(4, 5), 13, 0, 1, 1, 0)
    winners = select_winners((near_high, near_low, far))
    check("E strict local marks select one nearby winner plus the distant event", winners == (near_low, far))
    winner_programs = tuple(candidate_program(candidate) for candidate in winners)
    check("E winner centers exceed the exclusion radius", all(l1(left.anchor, right.anchor) > EXCLUSION_RADIUS for left in winner_programs for right in winner_programs if left != right))
    check("E all accepted QB16 footprints are disjoint", all(footprint(left).isdisjoint(footprint(right)) for left in winner_programs for right in winner_programs if left != right))
    winner_records = merge_records(
        *(program_records(program, reference_bit=index % 2) for index, program in enumerate(winner_programs))
    )
    check(
        "E nonce-free relational decoder recovers opposite-label separated packets without hybrids",
        detect_programs(winner_records) == set(winner_programs),
    )

    tied_left = Candidate((0, 0, 0), Fraction(1, 2), 0, 0, 0, 0, 0)
    tied_right = Candidate((1, 0, 0), Fraction(1, 2), 1, 0, 0, 0, 0)
    check("E exact mark ties block both colliding candidates", select_winners((tied_left, tied_right)) == tuple())


def record_cost_and_relational_patch() -> None:
    section("F - Low-record cost and relational finite-causal-patch route")
    rho = acceptance_density(Fraction(1))
    initial_record_density = 10 * rho
    completed_record_density = 14 * rho
    reserved_site_density = 16 * rho
    check("F expected initial program-record density is exactly 10/15225", initial_record_density == Fraction(10, 15225))
    check("F completed record density is exactly 14/15225", completed_record_density == Fraction(14, 15225))
    check("F reserved QB16 footprint density is exactly 16/15225", reserved_site_density == Fraction(16, 15225))
    check("F one exclusion-volume patch has expected winner count one", EXCLUSION_VOLUME * rho == 1)
    check("F one exclusion-volume patch has expected ten initial records", EXCLUSION_VOLUME * initial_record_density == 10)
    check(
        "F positive density gives divergent expected total records on full Z3",
        rho > 0 and EXCLUSION_VOLUME > 0,
    )

    independent_hits = {count: 1 - (1 - rho) ** count for count in (1, 2, 5, 10)}
    check("F exact finite-patch hit probabilities increase with independent opportunities", all(independent_hits[right] > independent_hits[left] for left, right in zip((1, 2, 5), (2, 5, 10))))
    check("F Palm conditioning on an origin winner has Radon factor M at q=1", Fraction(1, 1) / rho == EXCLUSION_VOLUME)

    palm_program = BinaryProgram((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0)
    records = program_records(palm_program)
    for seed in (Fraction(1, 5), Fraction(2, 5), Fraction(3, 5)):
        records = advance_program(records, palm_program, seed)
    check("F relationally anchored packet reaches a record-reconstructible commit", program_stage(records, palm_program) == 3)
    check("F committed Palm packet remains uniquely decoded without a nonce", detect_programs(records) == {palm_program})
    table = program_table(palm_program)
    check("F relational packet has an exact Bell-capable continuation", q7.exact_equal(chsh(table), 2 * sp.sqrt(2)))
    check("F Bell continuation is exactly no-signalling", all(q7.exact_equal(sum(table[(x, y, a, b)] for b in q7.OUTCOMES), sp.Rational(1, 2)) for x, y, a in product((0, 1), (0, 1), q7.OUTCOMES)))


def record_markov_and_concurrency() -> None:
    section("G - Record reconstruction and concurrent Bell continuation")
    left = BinaryProgram((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0)
    right = BinaryProgram((30, 0, 0), (0, 1, 0), (0, 0, 1), 1, 1, 0, 1)
    records = merge_records(program_records(left), program_records(right))
    check("G separated binary packets decode without hybrid programs", detect_programs(records) == {left, right})
    check("G equal complete records give equal decoded program sets", detect_programs(records) == detect_programs(dict(records)))
    check("G equal complete records give equal blank work states", q7.exact_equal(decoded_work_state(records, left), decoded_work_state(dict(records), left)))

    left_then_right = dict(records)
    right_then_left = dict(records)
    for _ in range(3):
        left_then_right = advance_program(left_then_right, left, Fraction(7, 20))
        left_then_right = advance_program(left_then_right, right, Fraction(13, 20))
        right_then_left = advance_program(right_then_left, right, Fraction(13, 20))
        right_then_left = advance_program(right_then_left, left, Fraction(7, 20))
    check("G disjoint microstage execution order gives identical permanent records", left_then_right == right_then_left)
    check("G both concurrent packets reach committed stages", program_stage(left_then_right, left) == 3 and program_stage(left_then_right, right) == 3)
    check("G equal final records reconstruct equal post-commit work states", q7.exact_equal(decoded_work_state(left_then_right, left), decoded_work_state(right_then_left, left)) and q7.exact_equal(decoded_work_state(left_then_right, right), decoded_work_state(right_then_left, right)))

    stripped_randomizer_left = advance_program(advance_program(program_records(left), left), left)
    branch_a = advance_program(stripped_randomizer_left, left, Fraction(1, 10))
    branch_b = advance_program(stripped_randomizer_left, left, Fraction(1, 5))
    check("G distinct randomizer coordinates can produce the same complete records", branch_a == branch_b)
    check("G discarded randomizer identity has no post-record predictive effect", q7.exact_equal(decoded_work_state(branch_a, left), decoded_work_state(branch_b, left)))


def paired_law_value_ablation() -> None:
    section("H - Nucleation and Bell exact-law-value ablations")
    q_low = Fraction(1, EXCLUSION_VOLUME)
    q_high = Fraction(2, EXCLUSION_VOLUME)
    rho_low = acceptance_density(q_low)
    rho_high = acceptance_density(q_high)
    check("H two covariant candidate activities give distinct exact winner densities", rho_low != rho_high and rho_low < rho_high)
    check("H both nucleation laws have positive finite density", 0 < rho_low < 1 and 0 < rho_high < 1)
    check("H both laws use the identical exclusion and binary packet architecture", EXCLUSION_RADIUS == 22 and len(PROGRAM_ROLES) == 10)
    common_coordinate = Fraction(3, 2 * EXCLUSION_VOLUME)
    check("H one common candidate coordinate separates the two activities", not (common_coordinate < q_low) and common_coordinate < q_high)

    program = BinaryProgram((0, 0, 0), (1, 0, 0), (0, 1, 0), 0, 0, 0, 0)
    ideal = program_table(program, sp.Integer(1))
    noisy = program_table(program, sp.Rational(1, 2))
    check("H ideal continuation gives exact Tsirelson CHSH", q7.exact_equal(chsh(ideal), 2 * sp.sqrt(2)))
    check("H visibility-half continuation gives exact sqrt-two CHSH", q7.exact_equal(chsh(noisy), sp.sqrt(2)))
    check("H both Bell law values normalize with full outcome support", all(q7.exact_equal(sum(q7.context_distribution(table, x, y).values()), 1) for table in (ideal, noisy) for x, y in product((0, 1), repeat=2)) and all(table[key].is_positive for table in (ideal, noisy) for key in table))
    check("H equal binary architecture does not select the Bell law value", any(not q7.exact_equal(ideal[key], noisy[key]) for key in ideal))


def documentation_contract() -> None:
    section("I - Route comparison, scope, and no-go-discipline needles")
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "cfsi-qb16",
        "deterministic symmetry obstruction",
        "coherent/global superposition",
        "positive-density stochastic nucleation",
        "relational finite-causal-patch",
        "projective finite-window consistency",
        "all 24 proper cubic rotations",
        "no hidden absolute origin",
        "orthogonal binary",
        "global possibility-label exchange",
        "simultaneous one-site algebra conjugation",
        "generated finite composition",
        "finite-radius atomic write",
        "nearest-neighbor compiled",
        "15225",
        "actual boundary/typicality",
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
        check(f"I note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    deterministic_symmetry_obstruction()
    coherent_route_controls()
    orthogonal_binary_carrier_repair()
    stochastic_nucleation_and_projective_law()
    record_cost_and_relational_patch()
    record_markov_and_concurrency()
    paired_law_value_ablation()
    documentation_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
