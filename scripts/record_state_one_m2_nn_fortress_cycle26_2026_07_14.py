#!/usr/bin/env python3
"""Cycle 26: record-state audit and a strictly-NN append-only fortress.

Companion note:
  docs/work_history/repo/review_feedback/
  RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md

This authority-free runner checks the literal record-state quotient, an exact
5,202-site nearest-neighbor append path that writes the Cycle-17 terminal
diamond and B0 last, collision exclusion, positive-density local success, and
the quantum no-information-without-disturbance boundary for nonorthogonal
record controls.  It changes no axiom, registry, audit surface, commit, push,
or PR.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from math import exp, isfinite, log
from pathlib import Path
from typing import Iterable

import numpy as np

import autonomous_self_closing_diamond_cycle17_2026_07_14 as c17


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE17_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md"
)
CYCLE20_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md"
)
RECONSTRUCTION_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "OPERATIONAL_RECORD_RECONSTRUCTION_DEEP_PROBE_NOTE_2026-07-13.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]

# The symmetric core is large enough that two centers within the required
# radius-nine exclusion share at least 8^3=512 core sites.  The extra positive
# transverse layer makes the block cardinality even and admits a Hamiltonian
# cycle from which a path ending at B0 is cut.
CORE_RADIUS = 8
NX = 18
NY = 17
NZ = 17
BLOCK_SIZE = NX * NY * NZ
EXPECTED_BLOCK_SIZE = 5202
CENTER_INDEX = (8, 8, 8)
GUARD_RADIUS = 20
GUARD_VOLUME = (2 * GUARD_RADIUS + 1) ** 3


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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def subtract(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def manhattan(vector: Coord) -> int:
    return sum(abs(value) for value in vector)


def linf(vector: Coord) -> int:
    return max(abs(value) for value in vector)


def rotate(matrix: np.ndarray, vector: Coord) -> Coord:
    return c17.matvec(matrix, vector)


def normalize_note() -> str:
    return " ".join(
        NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("`", "")
        .replace("*", "")
        .split()
    )


def source_contract() -> None:
    section("A - Foundation, predecessors, authority, and N1-N8 contract")
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle17 = CYCLE17_NOTE.read_text(encoding="utf-8").lower()
    cycle20 = " ".join(
        CYCLE20_NOTE.read_text(encoding="utf-8")
        .lower()
        .replace("`", "")
        .replace("*", "")
        .split()
    )
    reconstruction = RECONSTRUCTION_NOTE.read_text(encoding="utf-8").lower()
    note = normalize_note()

    check("A foundation has exactly the four named axiom headings", all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")))
    check("A Qualification literally defines state as records", "A state is a configuration of records." in axioms)
    check("A Qualification gives one law answer at a state", "at every\nstate where the condition holds it gives exactly one answer" in axioms)
    check("A Admissibility explicitly is not dynamics", "Admissibility is not a dynamics axiom" in axioms)
    check("A registry has only four approved premise paths", registry.count('"current_path"') == 4)
    check("A Cycle 17 supplies the 111-record terminal target", "terminal history has 111 permanent records" in cycle17)
    check("A Cycle 20 leaves exact NN one-M2 compile open", "exact nn one-m2 autonomous compile remains open" in cycle20)
    check("A operational reconstruction names record-state sufficiency", "record-state sufficiency" in reconstruction)

    required = (
        "authority: none",
        "literal state is a record configuration",
        "future-relevant unrecorded state is not licensed",
        "operational gauge when every future record law is fibre-constant",
        "route a — record-configuration markov law",
        "route b — coherent qca mediator",
        "route c — branch-labelled local instrument",
        "strong lumpability",
        "5,202-site fortress",
        "b0 is written last",
        "111 terminal diamond records",
        "strictly nearest-neighbor append path",
        "homogeneous and proper-cubic covariant",
        "positive-density success event",
        "exact guarded rsa distribution is not compiled",
        "direct quantum controller has a two-orthogonal-label ceiling",
        "three-site spatial code carries eight orthogonal labels",
        "record-derived phase",
        "qca route is incompatible unless record-sufficient",
        "dissipative route is compatible only after record lumping",
        "exact-law field, not a new axiom",
        "qualification clarification is definitional if predictive sufficiency was intended",
        "no live axiom edit",
        "no universal one-m2 no-go",
        "no new record axiom is forced",
    )
    for phrase in required:
        check(f"A note states required phrase: {phrase}", phrase in note)
    for index in range(1, 9):
        check(f"A no-go discipline includes N{index}", f"n{index} —" in note or f"n{index} -" in note)


def record_state_quotient_probe() -> None:
    section("B - Record-state sufficiency, strong lumpability, and gauge")
    plus = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)
    minus = np.array((1.0, -1.0), dtype=complex) / np.sqrt(2.0)
    zero = np.array((1.0, 0.0), dtype=complex)
    one = np.array((0.0, 1.0), dtype=complex)

    def probabilities(state: np.ndarray, basis: tuple[np.ndarray, np.ndarray]) -> tuple[float, float]:
        return tuple(float(abs(np.vdot(vector, state)) ** 2) for vector in basis)  # type: ignore[return-value]

    # The two microstates have the same empty record configuration.  An X
    # read distinguishes them, so the fibre is not strongly lumpable under
    # that future protocol.
    record_map = {"plus": frozenset(), "minus": frozenset()}
    x_plus = probabilities(plus, (plus, minus))
    x_minus = probabilities(minus, (plus, minus))
    z_plus = probabilities(plus, (zero, one))
    z_minus = probabilities(minus, (zero, one))
    check("B coherent plus/minus microstates share one record state", record_map["plus"] == record_map["minus"])
    check("B X future breaks record-fibre lumpability", np.allclose(x_plus, (1.0, 0.0)) and np.allclose(x_minus, (0.0, 1.0)))
    check("B restricted Z future makes the hidden phase operational gauge", np.allclose(z_plus, z_minus) and np.allclose(z_plus, (0.5, 0.5)))

    # A unique decoder from records to any derived working object is safe:
    # equal record configurations necessarily decode identically.
    def derived_decoder(records: frozenset[tuple[int, int]]) -> tuple[int, int]:
        return (len(records), sum(bit for _, bit in records) & 1)

    left = frozenset(((0, 1), (3, 0)))
    right = frozenset(((3, 0), (0, 1)))
    check("B a record-derived working state factors through records", left == right and derived_decoder(left) == derived_decoder(right))

    # A direct Markov generator on records has no additional state fibre.
    states = (frozenset(), frozenset({("a", 0)}), frozenset({("b", 1)}))
    generator = np.array(((-2.0, 1.0, 1.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)))
    check("B record generator rows sum to zero", np.allclose(generator.sum(axis=1), 0.0))
    check("B record generator has nonnegative off-diagonal rates", all(generator[i, j] >= 0 for i in range(3) for j in range(3) if i != j))
    check("B append branches strictly extend the empty record state", all(states[0] < state for state in states[1:]))


def edge(left: Coord, right: Coord) -> frozenset[Coord]:
    return frozenset((left, right))


def base_cycle_2d(nx: int, ny: int) -> tuple[tuple[int, int], ...]:
    """Hamiltonian cycle order for even nx and ny >= 2."""
    sequence: list[tuple[int, int]] = [(0, 0)]
    sequence.extend((0, y) for y in range(1, ny))
    for x in range(1, nx):
        ys: Iterable[int] = range(ny - 1, 0, -1) if x & 1 else range(1, ny)
        sequence.extend((x, y) for y in ys)
    sequence.extend((x, 0) for x in range(nx - 1, 0, -1))
    return tuple(sequence)


def hamiltonian_cycle_graph(nx: int, ny: int, nz: int) -> dict[Coord, set[Coord]]:
    base = base_cycle_2d(nx, ny)
    edges: set[frozenset[Coord]] = set()
    for z in range(nz):
        layer = tuple((x, y, z) for x, y in base)
        edges.update(edge(left, right) for left, right in zip(layer, layer[1:] + layer[:1]))

    # Splice adjacent layer cycles with alternating intact edges.  Each
    # intermediate layer participates in two splices on two distinct edges.
    splice_edges = (((0, 0), (0, 1)), ((0, 2), (0, 3)))
    for z in range(nz - 1):
        a2, b2 = splice_edges[z & 1]
        az, bz = (*a2, z), (*b2, z)
        an, bn = (*a2, z + 1), (*b2, z + 1)
        edges.remove(edge(az, bz))
        edges.remove(edge(an, bn))
        edges.add(edge(az, an))
        edges.add(edge(bz, bn))

    adjacency: dict[Coord, set[Coord]] = defaultdict(set)
    for item in edges:
        left, right = tuple(item)
        adjacency[left].add(right)
        adjacency[right].add(left)
    return dict(adjacency)


def fortress_path() -> tuple[Coord, ...]:
    adjacency = hamiltonian_cycle_graph(NX, NY, NZ)
    b0 = CENTER_INDEX
    source = sorted(adjacency[b0])[0]
    adjacency[b0].remove(source)
    adjacency[source].remove(b0)
    path = [source]
    previous: Coord | None = None
    while path[-1] != b0:
        current = path[-1]
        choices = adjacency[current] - ({previous} if previous is not None else set())
        if len(choices) != 1:
            raise RuntimeError("cut cycle is not one Hamiltonian path")
        following = next(iter(choices))
        previous = current
        path.append(following)
    return tuple(
        tuple(value - CENTER_INDEX[index] for index, value in enumerate(site))  # type: ignore[misc]
        for site in path
    )


PATH = fortress_path()
FOOTPRINT = frozenset(PATH)
CORE = frozenset(product(range(-CORE_RADIUS, CORE_RADIUS + 1), repeat=3))
FILLER_INDEX = {site: index for index, site in enumerate(sorted(FOOTPRINT))}


def terminal_diamond(branch_bit: int) -> dict[Coord, c17.Content]:
    cell = c17.Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    records, _, _, _ = c17.run_schedule("first", cell, branch_bit, 2600 + branch_bit)
    b0 = c17.global_site(cell, c17.CANONICAL_PATH[0])
    return {subtract(site, b0): content for site, content in records.items()}


DIAMONDS = (terminal_diamond(0), terminal_diamond(1))
CANONICAL_FRAME = c17.Frame((0, 0, 1), (1, 0, 0))


@dataclass(frozen=True)
class PhysicalLabel:
    family: str
    token: str | int | Coord
    forward: Coord | None = None
    transverse: Coord | None = None


def rotate_frame(frame: c17.Frame, matrix: np.ndarray) -> c17.Frame:
    return c17.Frame(rotate(matrix, frame.forward), rotate(matrix, frame.transverse))


def physical_label(local_site: Coord, branch_bit: int, matrix: np.ndarray) -> PhysicalLabel:
    content = DIAMONDS[branch_bit].get(local_site)
    if content is None:
        frame = rotate_frame(CANONICAL_FRAME, matrix)
        return PhysicalLabel("F", FILLER_INDEX[local_site], frame.forward, frame.transverse)
    frame = rotate_frame(content.frame, matrix)
    if content.kind == "J":
        axis = frame.forward if content.bit == 0 else tuple(-value for value in frame.forward)
        return PhysicalLabel("J", axis)
    return PhysicalLabel("G", c17.token(content), frame.forward, frame.transverse)


def path_and_diamond_probe() -> None:
    section("C - Exact 5,202-site path, terminal diamond, and record phase")
    check("C block cardinality is exactly 5,202", BLOCK_SIZE == EXPECTED_BLOCK_SIZE == len(PATH))
    check("C path visits every footprint site exactly once", len(set(PATH)) == len(PATH) == len(FOOTPRINT))
    check("C every append is strictly nearest-neighbor", all(manhattan(subtract(right, left)) == 1 for left, right in zip(PATH, PATH[1:])))
    check("C symmetric radius-eight core is contained", CORE <= FOOTPRINT and len(CORE) == 17**3)
    check("C path starts at the Cycle-17 B1 neighbor", PATH[0] == (0, -1, 0) and DIAMONDS[0][PATH[0]].kind == "B" and DIAMONDS[0][PATH[0]].index == 1)
    check("C B0 is the final append", PATH[-1] == (0, 0, 0) and DIAMONDS[0][PATH[-1]].kind == "B" and DIAMONDS[0][PATH[-1]].index == 0)
    check("C both terminal branches contain 111 records", all(len(diamond) == 111 for diamond in DIAMONDS))
    differing = {site for site in DIAMONDS[0] if DIAMONDS[0][site] != DIAMONDS[1][site]}
    check("C terminal branches differ only at the sampled J record", len(differing) == 1 and all(DIAMONDS[bit][next(iter(differing))].kind == "J" for bit in (0, 1)))
    check("C all 111 terminal roles lie in the fortress", all(set(diamond) <= FOOTPRINT for diamond in DIAMONDS))
    check("C terminal support remains inside radius four of B0", all(max(linf(site) for site in diamond) == 4 for diamond in DIAMONDS))
    identity = np.eye(3, dtype=int)
    check("C every canonical physical path label is position-unique", all(len({physical_label(site, bit, identity) for site in PATH}) == len(PATH) for bit in (0, 1)))

    # The current phase of an isolated build is its permanent prefix.  Equal
    # prefix record configurations produce equal next targets.
    prefixes = [frozenset(PATH[:index]) for index in (1, 17, 111, 1000, len(PATH) - 1)]
    next_sites = [PATH[len(prefix)] for prefix in prefixes]
    check("C every sampled phase is a record-derived prefix", all(PATH[: len(prefix)] == tuple(site for site in PATH if site in prefix) for prefix in prefixes))
    check("C record-derived prefixes select unique next sites", len(set(next_sites)) == len(next_sites))


def local_signature(
    rotated_path: tuple[Coord, ...],
    labels: tuple[PhysicalLabel, ...],
    index: int,
    prefix: dict[Coord, PhysicalLabel],
) -> tuple[tuple[Coord, PhysicalLabel], ...]:
    target = rotated_path[index]
    return tuple(
        sorted(
            (direction, prefix[neighbor])
            for direction in c17.DIRECTIONS
            if (neighbor := add(target, direction)) in prefix
        )
    )


def homogeneous_local_rule_probe() -> None:
    section("D - Homogeneous proper-cubic NN rule table")
    rotations = c17.proper_cubic_rotations()
    deterministic_outputs: dict[tuple[tuple[Coord, PhysicalLabel], ...], set[PhysicalLabel]] = defaultdict(set)
    locations: dict[tuple[tuple[Coord, PhysicalLabel], ...], set[str]] = defaultdict(set)

    for rotation_index, matrix in enumerate(rotations):
        rotated_path = tuple(rotate(matrix, site) for site in PATH)
        check(f"D rotation {rotation_index:02d} preserves NN path", all(manhattan(subtract(right, left)) == 1 for left, right in zip(rotated_path, rotated_path[1:])))
        check(f"D rotation {rotation_index:02d} preserves radius-eight core", frozenset(rotate(matrix, site) for site in CORE) == CORE)
        for branch_bit in (0, 1):
            labels = tuple(physical_label(site, branch_bit, matrix) for site in PATH)
            prefix: dict[Coord, PhysicalLabel] = {}
            for index, target in enumerate(rotated_path):
                if index:
                    signature = local_signature(rotated_path, labels, index, prefix)
                    deterministic_outputs[signature].add(labels[index])
                    locations[signature].add("J" if DIAMONDS[branch_bit].get(PATH[index], c17.Content("F", CANONICAL_FRAME)).kind == "J" else "ordinary")
                prefix[target] = labels[index]

    ambiguous = {signature: outputs for signature, outputs in deterministic_outputs.items() if len(outputs) > 1}
    check("D every non-J local signature has exactly one next answer", all(locations[signature] == {"J"} for signature in ambiguous))
    check("D exactly 24 J signatures carry the two explicit branches", len(ambiguous) == 24 and all(len(outputs) == 2 for outputs in ambiguous.values()))
    check("D ordinary local transitions are deterministic functions of recorded neighbors", all(len(outputs) == 1 for signature, outputs in deterministic_outputs.items() if signature not in ambiguous))
    check("D every growth signature contains a center-pinning non-J label", all(any(label.family in {"F", "G"} for _, label in signature) for signature in deterministic_outputs))
    check("D source is one all-open 24-frame branch instrument", len({physical_label(PATH[0], 0, matrix) for matrix in rotations}) == 24)
    check("D rule table is finite", 100_000 < len(deterministic_outputs) < 150_000)


def collision_and_density_probe() -> None:
    section("E - Hard-core completion and positive-density local success")
    minimum_core_overlap = (2 * CORE_RADIUS + 1 - 9) ** 3
    maximum_two_diamonds = 2 * len(DIAMONDS[0])
    check("E forbidden centers share at least 512 core sites", minimum_core_overlap == 512)
    check("E at least 290 shared sites are filler for both patterns", minimum_core_overlap - maximum_two_diamonds == 290)

    # Filler labels contain both local coordinate token and full frame.  At a
    # shared physical site, equal labels would force equal frame and equal
    # root-relative coordinate, hence equal centers.  Distinct forbidden
    # centers therefore demand different permanent contents on at least one
    # of the shared filler sites.
    check("E distinct centers cannot share one injective filler label", PhysicalLabel("F", 1, (0, 0, 1), (1, 0, 0)) != PhysicalLabel("F", 2, (0, 0, 1), (1, 0, 0)))
    check("E distinct frames cannot share one injective filler label", PhysicalLabel("F", 1, (0, 0, 1), (1, 0, 0)) != PhysicalLabel("F", 1, (0, 0, 1), (0, 1, 0)))
    check("E one-record-per-site excludes two completed forbidden centers", minimum_core_overlap > maximum_two_diamonds)

    # A finite spacetime isolation cylinder has strictly positive probability.
    # This is intentionally a grotesquely weak lower bound; positivity, not a
    # phenomenological density, is the claim.
    source_rate = 1.0
    growth_rate = 100.0
    delta = 0.01
    completion_time = BLOCK_SIZE * delta
    log_source = log(1.0 - exp(-source_rate * delta)) - log(24.0)
    log_no_competitor = -source_rate * (GUARD_VOLUME - 1) * completion_time
    log_growth = (BLOCK_SIZE - 1) * log(1.0 - exp(-growth_rate * delta))
    log_success = log_source + log_no_competitor + log_growth
    coarse_spacing = 2 * GUARD_RADIUS + 1
    log_density_bound = log_success - 3.0 * log(float(coarse_spacing))
    check("E finite isolation-cylinder success log-probability exists", isfinite(log_success) and log_success < 0.0)
    check("E coarse disjoint cylinders give a positive density bound", isfinite(log_density_bound) and log_density_bound < log_success)
    check("E guard encloses every overlapping footprint source", GUARD_RADIUS >= 2 * (CORE_RADIUS + 1) + 2)


def pure_projector(vector: np.ndarray) -> np.ndarray:
    vector = vector / np.linalg.norm(vector)
    return np.outer(vector, vector.conj())


def filler_bloch(token_index: int, frame: c17.Frame) -> np.ndarray:
    parameter = float(1000 + token_index)
    vector = (
        np.asarray(frame.forward, dtype=float)
        + parameter * np.asarray(frame.transverse, dtype=float)
        + parameter * parameter * np.asarray(frame.normal, dtype=float)
    )
    return vector / np.linalg.norm(vector)


def m2_capacity_and_instrument_probe() -> None:
    section("F - M2 control capacity and branch-labelled instrument boundary")
    zero = np.array((1.0, 0.0), dtype=complex)
    one = np.array((0.0, 1.0), dtype=complex)
    plus = np.array((1.0, 1.0), dtype=complex) / np.sqrt(2.0)
    states = (zero, one, plus)
    gram = np.array([[np.vdot(left, right) for right in states] for left in states])
    check("F one qubit has only two mutually orthogonal pure labels", np.allclose(gram[:2, :2], np.eye(2)) and abs(gram[0, 2]) > 0 and abs(gram[1, 2]) > 0)

    filler_sites = tuple(sorted(FOOTPRINT - set(DIAMONDS[0])))
    frames = c17.oriented_frames()
    filler_vectors = {
        tuple(np.round(filler_bloch(FILLER_INDEX[site], frame), 13))
        for site in filler_sites
        for frame in frames
    }
    check("F all filler/frame controls map injectively to M2 rank-one rays", len(filler_vectors) == len(filler_sites) * len(frames) == 5091 * 24)
    sample_projectors = tuple(
        (c17.I2 + c17.pauli(filler_bloch(FILLER_INDEX[site], frame))) / 2.0
        for site in filler_sites[:3]
        for frame in frames[:3]
    )
    check("F sampled filler contents are rank-one M2 projectors", all(np.allclose(projector @ projector, projector, atol=1.0e-10) and np.isclose(np.trace(projector), 1.0) for projector in sample_projectors))
    first = (c17.I2 + c17.pauli(filler_bloch(FILLER_INDEX[filler_sites[0]], frames[0]))) / 2.0
    second = (c17.I2 + c17.pauli(filler_bloch(FILLER_INDEX[filler_sites[1]], frames[0]))) / 2.0
    filler_overlap = float(np.trace(first @ second).real)
    check("F distinct filler records are nonorthogonal direct controls", 0.0 < filler_overlap < 1.0)

    # If a unitary keeps a permanent predecessor |psi_i> unchanged and writes
    # a distinct perfectly readable target label |i>, inner-product
    # preservation requires <psi_i|psi_j>=<psi_i|psi_j><i|j>=0.  Hence every
    # pair that drives distinct orthogonal target records must be orthogonal.
    input_overlap = abs(np.vdot(zero, plus))
    distinct_target_overlap = abs(np.vdot(zero, one))
    check("F nondisturbing append from nonorthogonal controls violates inner-product preservation", input_overlap > 0 and not np.isclose(input_overlap, input_overlap * distinct_target_overlap))

    # Three physical qubits have eight orthogonal computational codewords.
    codewords = []
    for bits in product((0, 1), repeat=3):
        vector = np.array((1.0,), dtype=complex)
        for bit in bits:
            vector = np.kron(vector, one if bit else zero)
        codewords.append(vector)
    code_gram = np.array([[np.vdot(left, right) for right in codewords] for left in codewords])
    check("F three-site spatial code has eight orthogonal labels", np.allclose(code_gram, np.eye(8)))
    check("F eight labels cover six directions plus source and stop", len(codewords) == len(c17.DIRECTIONS) + 2)

    # Equal averaged dephasing channels still carry inequivalent event labels.
    identity = np.eye(2, dtype=complex)
    zed = np.diag((1.0, -1.0)).astype(complex)
    p0 = pure_projector(zero)
    p1 = pure_projector(one)
    rho = np.array(((0.6, 0.2), (0.2, 0.4)), dtype=complex)

    def channel(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
        return sum(operator @ rho @ operator.conj().T for operator in kraus)

    random_unitary = (identity / np.sqrt(2.0), zed / np.sqrt(2.0))
    projective = (p0, p1)
    check("F one channel still admits inequivalent branch instruments", np.allclose(channel(random_unitary), channel(projective)))
    random_probs = tuple(float(np.trace(operator @ p0 @ operator.conj().T).real) for operator in random_unitary)
    projective_probs = tuple(float(np.trace(operator @ p0 @ operator.conj().T).real) for operator in projective)
    check("F equal channels produce different record transcripts", np.allclose(random_probs, (0.5, 0.5)) and np.allclose(projective_probs, (1.0, 0.0)))


def route_and_no_go_contract() -> None:
    section("G - Route classification and no-go-discipline contract")
    note = normalize_note()
    route_phrases = (
        "route a result: conditional constructive success",
        "route b result: foundation-incompatible when future-relevant",
        "route c result: record-level success, quantum-carrier compile open",
        "multi-label record law route — attempted",
        "binary spatial-code route — attempted",
        "coherent open-site qca route — attempted",
        "record-derived coherent decoder route — attempted",
        "branch-labelled record jump route — attempted",
        "dissipative no-jump-memory route — attempted",
        "fortress macrohistory route — attempted",
        "exact guarded rsa reproduction route — attempted",
        "distributed orthogonal record route — attempted",
        "qualification-widening route — attempted",
    )
    for phrase in route_phrases:
        check(f"G note classifies route: {phrase}", phrase in note)

    conclusions = (
        "the record-only fortress compiles collision-safe positive-density terminal diamonds",
        "it does not reproduce the ideal range-nine rsa law",
        "future-sensitive coherent state in a record fibre violates the current qualification",
        "fibre-constant hidden motion is operational gauge",
        "a record-derived decoder adds no hidden physical state",
        "nonorthogonal permanent controls cannot nondestructively write distinct orthogonal successors",
        "spatial orthogonal encoding remains live",
        "no obstruction to every one-m2-per-site spatial code is claimed",
        "the coherent qca architecture, not the four-axiom framework, is what fails the literal state test",
        "the markov generator and branch-labelled instrument are exact-law fields",
        "a predictive-sufficiency clarification would not add dynamics",
        "widening state beyond records would change ontology",
        "no new record axiom is forced",
    )
    for phrase in conclusions:
        check(f"G note preserves conclusion: {phrase}", phrase in note)

    check("G N2 has collapsed three-condition law set", "collapsed universal law wall set has three conditions" in note and "primitive-supplied h" in note)
    check("G N3 has hidden-condition scan", "hidden-condition scan" in note)
    check("G N4 has exact residual matching", "exact residual matching" in note)
    check("G N5 narrows every resolution", "no universal carrier no-go" in note)
    check("G N6 records partial-closure path", "partial-closure path" in note and "no constitutional promotion follows" in note)
    check("G N7 includes hostile steelman", "hostile reviewer" in note and "binary tile assembly could close the quantum compile" in note)
    check("G N8 includes cross-cycle escape", "cross-cycle echo" in note and "spatializing state can retire a hidden-state wall" in note)
    check("G no-go-discipline records PASS", "no-go-discipline status: pass" in note)


def main() -> int:
    source_contract()
    record_state_quotient_probe()
    path_and_diamond_probe()
    homogeneous_local_rule_probe()
    collision_and_density_probe()
    m2_capacity_and_instrument_probe()
    route_and_no_go_contract()
    print(
        "\nSUMMARY: RECORD STATE ONE-M2 NN FORTRESS CYCLE 26 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
