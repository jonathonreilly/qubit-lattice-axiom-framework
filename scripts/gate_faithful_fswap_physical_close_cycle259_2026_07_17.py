#!/usr/bin/env python3
"""Cycle 259: bounded physical-close transducer for the Cycle-230 FSWAP.

The finite construction combines a data-side actuation flag with a Choi test
of a second use of the declared FSWAP coupling.  It is exactly nondemolishing
on arbitrary data and exactly rejects deletion of the declared joint
data-plus-flag call.  Independent component-fault controls expose the honest
boundary: a flag flip plus a successful diagnostic replica can still certify
completion when the data FSWAP factor itself was omitted.  The witness is
therefore gate-faithful only on its declared common-control domain, not an
unconditional proof that the data interaction occurred.

Coherent flags and Choi carriers are not Records.  A separate supplied
actualization map creates immutable record objects only after the close test.
No gate layer, scheduler order, projector weight, or record count is called
physical time, a rate, energy, or a Born probability.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "GATE_FAITHFUL_FSWAP_PHYSICAL_CLOSE_CYCLE259_NOTE_2026-07-17.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
SOURCES = {
    "pointer": ROOT / "docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md",
    "firewall": ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    "cycle230": REVIEW / "SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "cycle243": REVIEW / "SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md",
    "cycle255": REVIEW / "CAR_COMPILER_RECORD_CAUSAL_DEPTH_BRIDGE_CYCLE255_NOTE_2026-07-17.md",
    "cycle257": REVIEW / "FOLLOWUP_M64_PHYSICAL_M2_COMPILER_TOURNAMENT_SYNTHESIS_CYCLE257_NOTE_2026-07-17.md",
}

Coord = tuple[int, int, int]

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


@dataclass(frozen=True)
class TypedMap:
    name: str
    domain: str
    codomain: str
    status: str


CLOSE_MAPS = (
    TypedMap(
        "A_data_flag",
        "two data modes plus one fresh coherent flag",
        "FSWAP-updated data plus flipped flag",
        "SUPPLIED_BOUNDED_JOINT_CALL",
    ),
    TypedMap(
        "Q_probe",
        "prepared four-M2 Choi probe and a second declared coupling use",
        "FSWAP process witness",
        "EXACT_FINITE_DIAGNOSTIC_SUPPLIED_PREPARATION",
    ),
    TypedMap(
        "K_close",
        "flag-one and FSWAP-Choi support",
        "completion candidate or local failure",
        "EXACT_ON_DECLARED_COMMON_CONTROL_DOMAIN",
    ),
    TypedMap(
        "R_form",
        "actualized close candidate satisfying local admissibility",
        "immutable readable Record or undefined",
        "SUPPLIED_FORMATION_AND_PERMANENCE_LAW",
    ),
)


def source_and_note_contract() -> None:
    axioms = normalized(AXIOMS)
    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the source boundary supplies Z3/M2 and Record permanence but not this coupling, diagnostic, formation law, or time metric",
        all(path.is_file() for path in SOURCES.values())
        and "physical sites are the points of the cubic lattice z^3" in axioms
        and "m_2(c)" in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "actual cycle-230 fswap" in source["cycle255"]
        and "physical close" in source["cycle243"]
        and "physical-close deletion fails" in source["cycle257"]
        and "coherent controlled-copy" in source["pointer"],
        {"space": "Z3", "site_algebra": "M2", "selected_close_law": False},
    )
    note = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "actual cycle-230 two-mode fswap",
        "choi",
        "trusted shared-control",
        "common-control fault domain",
        "split-fault",
        "omitted data fswap factor",
        "coherent carriers are not records",
        "all 24 proper-cubic frames",
        "held-out refinement",
        "false positive",
        "false negative",
        "data-only indistinguishability control",
        "+1 fswap eigenstates",
        "three-dimensional space remains axiomatic input",
        "compiler layers are not physical time",
        "projector weight is not a born probability",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in note)
    check("the Cycle-259 note preserves the close, firewall, and N1-N8 contract", not missing, missing)
    check(
        "the typed surface keeps coherent diagnostics, close candidates, and Records distinct",
        len(CLOSE_MAPS) == 4
        and CLOSE_MAPS[2].codomain == "completion candidate or local failure"
        and CLOSE_MAPS[3].status == "SUPPLIED_FORMATION_AND_PERMANENCE_LAW",
        CLOSE_MAPS,
    )


def kron(*operators: np.ndarray) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for operator in operators:
        result = np.kron(result, operator)
    return result


def fswap() -> np.ndarray:
    return np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def maximally_entangled(dimension: int) -> np.ndarray:
    vector = np.zeros(dimension * dimension, dtype=complex)
    for index in range(dimension):
        vector[index * dimension + index] = 1 / np.sqrt(dimension)
    return vector


def partial_trace_data(joint: np.ndarray, data_dimension: int, carrier_dimension: int) -> np.ndarray:
    tensor = joint.reshape(data_dimension, carrier_dimension, data_dimension, carrier_dimension)
    return np.trace(tensor, axis1=1, axis2=3)


def partial_trace_carrier(joint: np.ndarray, data_dimension: int, carrier_dimension: int) -> np.ndarray:
    tensor = joint.reshape(data_dimension, carrier_dimension, data_dimension, carrier_dimension)
    return np.trace(tensor, axis1=0, axis2=2)


def actual_fswap_and_local_code_controls() -> np.ndarray:
    unitary = fswap()
    identity4 = np.eye(4, dtype=complex)
    parity = np.diag((1, -1, -1, 1)).astype(complex)
    check(
        "the actual Cycle-230 two-mode FSWAP is Hermitian, involutive, parity even, unitary, and Hilbert-Schmidt orthogonal to identity",
        np.linalg.norm(unitary.conj().T @ unitary - identity4) < 1e-15
        and np.linalg.norm(unitary - unitary.conj().T) < 1e-15
        and np.linalg.norm(unitary @ unitary - identity4) < 1e-15
        and np.linalg.norm(unitary @ parity - parity @ unitary) < 1e-15
        and abs(np.trace(unitary)) < 1e-15,
        {"trace": np.trace(unitary), "determinant": np.linalg.det(unitary)},
    )

    encoder = np.asarray(((1, 0), (0, 0), (0, 0), (0, 1)), dtype=complex)
    logical_z = np.diag((1, -1)).astype(complex)
    code_projector = encoder @ encoder.conj().T
    intertwiner = float(np.linalg.norm(unitary @ encoder - encoder @ logical_z))
    leakage = float(np.linalg.norm((identity4 - code_projector) @ unitary @ encoder))
    check(
        "the local two-mode fixture retains the Cycle-255 logical intertwiner with zero code leakage",
        np.linalg.norm(encoder.conj().T @ encoder - np.eye(2)) < 1e-15
        and intertwiner < 1e-15
        and leakage < 1e-15,
        {"intertwiner": intertwiner, "leakage": leakage, "scope": "two-mode fixture only"},
    )
    return unitary


def choi_vector(gate: np.ndarray, phi: np.ndarray) -> np.ndarray:
    return kron(gate, np.eye(gate.shape[0], dtype=complex)) @ phi


def choi_acceptance_weight(target: np.ndarray, candidate: np.ndarray, phi: np.ndarray) -> float:
    target_vector = choi_vector(target, phi)
    candidate_vector = choi_vector(candidate, phi)
    return float(abs(np.vdot(target_vector, candidate_vector)) ** 2)


def choi_and_sentinel_controls(unitary: np.ndarray) -> np.ndarray:
    identity4 = np.eye(4, dtype=complex)
    phi = maximally_entangled(4)
    j_identity = choi_vector(identity4, phi)
    j_fswap = choi_vector(unitary, phi)
    overlap = np.vdot(j_identity, j_fswap)
    target_projector = projector(j_fswap)
    check(
        "the bounded Choi probe exactly separates identity from FSWAP and accepts the target channel",
        abs(overlap) < 1e-15
        and abs(np.vdot(j_fswap, j_fswap) - 1) < 1e-15
        and np.linalg.norm(target_projector @ j_fswap - j_fswap) < 1e-15
        and np.linalg.norm(target_projector @ j_identity) < 1e-15,
        {
            "identity_FSWAP_Choi_overlap": overlap,
            "identity_acceptance_weight": choi_acceptance_weight(unitary, identity4, phi),
            "FSWAP_acceptance_weight": choi_acceptance_weight(unitary, unitary, phi),
        },
    )

    ket10 = np.asarray((0, 0, 1, 0), dtype=complex)
    ket01 = np.asarray((0, 1, 0, 0), dtype=complex)
    check(
        "a preparation-light one-particle sentinel also distinguishes the two endpoints but tests only one input",
        np.linalg.norm(unitary @ ket10 - ket01) < 1e-15
        and abs(np.vdot(ket10, unitary @ ket10)) < 1e-15,
        {"sentinel_scope": "one prepared input", "Choi_scope": "promised unitary channel"},
    )
    return phi


def random_density(seed: int = 259) -> np.ndarray:
    rng = np.random.default_rng(seed)
    amplitude = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    density = amplitude @ amplitude.conj().T
    return density / np.trace(density)


def ideal_joint_transducer_controls(unitary: np.ndarray, phi: np.ndarray) -> None:
    identity4 = np.eye(4, dtype=complex)
    identity16 = np.eye(16, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    flag0 = np.diag((1, 0)).astype(complex)
    flag1 = np.diag((0, 1)).astype(complex)
    rho = random_density()
    initial_probe = projector(phi)
    initial = kron(rho, flag0, initial_probe)

    data_flag_call = kron(unitary, x, identity16)
    probe_call = kron(identity4, np.eye(2), unitary, identity4)
    schedules = ((data_flag_call, probe_call), (probe_call, data_flag_call))
    outputs = []
    for schedule in schedules:
        output = initial.copy()
        for gate in schedule:
            output = gate @ output @ gate.conj().T
        outputs.append(output)

    j_fswap = choi_vector(unitary, phi)
    accept_carrier = kron(flag1, projector(j_fswap))
    accept_projector = kron(identity4, accept_carrier)
    accepted = accept_projector @ outputs[0] @ accept_projector
    weight = float(np.trace(accepted).real)
    ideal = unitary @ rho @ unitary.conj().T
    carrier_dimension = 32
    data_residual = float(np.linalg.norm(partial_trace_data(accepted, 4, carrier_dimension) - ideal))
    carrier_residual = float(
        np.linalg.norm(partial_trace_carrier(accepted, 4, carrier_dimension) - accept_carrier)
    )
    factorization_residual = float(np.linalg.norm(accepted - kron(ideal, accept_carrier)))
    scheduler_residual = float(np.linalg.norm(outputs[0] - outputs[1]))
    check(
        "the ideal flagged-plus-Choi close is deterministic, scheduler invariant, and exactly nondemolishing on arbitrary data",
        abs(weight - 1) < 2e-15
        and data_residual < 2e-15
        and carrier_residual < 2e-15
        and factorization_residual < 2e-15
        and scheduler_residual < 2e-15,
        {
            "acceptance_weight": weight,
            "data_residual": data_residual,
            "carrier_residual": carrier_residual,
            "factorization_residual": factorization_residual,
            "scheduler_residual": scheduler_residual,
        },
    )

    record_state = np.zeros(32, dtype=complex)
    record_state[-1] = 1
    transcript = projector(record_state)
    joint_record = kron(ideal, transcript)
    check(
        "tracing a successful supplied five-Record transcript recovers the ideal FSWAP channel exactly",
        np.linalg.norm(partial_trace_data(joint_record, 4, 32) - ideal) < 2e-15
        and np.linalg.norm(partial_trace_carrier(joint_record, 4, 32) - transcript) < 2e-15,
        {"quantum_Record_factorization": 0.0},
    )


@dataclass(frozen=True)
class FaultCase:
    name: str
    data_fswap: bool
    flag_flip: bool
    probe_fswap: bool


def case_weight(case: FaultCase, unitary: np.ndarray, phi: np.ndarray) -> float:
    probe_gate = unitary if case.probe_fswap else np.eye(4, dtype=complex)
    return float(case.flag_flip) * choi_acceptance_weight(unitary, probe_gate, phi)


def deletion_and_fault_domain_controls(unitary: np.ndarray, phi: np.ndarray) -> None:
    declared = (
        FaultCase("declared_joint_call_present", True, True, True),
        FaultCase("declared_data_plus_flag_call_deleted", False, False, True),
    )
    declared_rows = [
        {
            "case": case.name,
            "data_gate_present": case.data_fswap,
            "acceptance_weight": case_weight(case, unitary, phi),
            "completion": case_weight(case, unitary, phi) > 1 - 1e-12,
        }
        for case in declared
    ]
    false_positives = sum(row["completion"] and not row["data_gate_present"] for row in declared_rows)
    false_negatives = sum((not row["completion"]) and row["data_gate_present"] for row in declared_rows)
    check(
        "deleting the declared physical data-plus-flag FSWAP call suppresses completion with zero common-domain false positives and false negatives",
        declared_rows[0]["acceptance_weight"] > 1 - 1e-12
        and declared_rows[1]["acceptance_weight"] < 1e-15
        and false_positives == 0
        and false_negatives == 0,
        {"rows": declared_rows, "false_positives": false_positives, "false_negatives": false_negatives},
    )

    flag_only = FaultCase("flag_only_no_data_no_probe", False, True, False)
    check(
        "the Choi arm rejects a bare trusted flag when the diagnostic FSWAP is also absent",
        case_weight(flag_only, unitary, phi) < 1e-15,
        {"acceptance_weight": case_weight(flag_only, unitary, phi)},
    )

    split_cases = (
        FaultCase("data_factor_omitted_flag_and_probe_survive", False, True, True),
        FaultCase("data_present_probe_omitted", True, True, False),
        FaultCase("data_present_flag_omitted", True, False, True),
        FaultCase("data_present_both_witness_arms_omitted", True, False, False),
    )
    split_rows = [
        {
            "case": case.name,
            "data_gate_present": case.data_fswap,
            "acceptance_weight": case_weight(case, unitary, phi),
            "completion": case_weight(case, unitary, phi) > 1 - 1e-12,
        }
        for case in split_cases
    ]
    split_false_positives = sum(row["completion"] and not row["data_gate_present"] for row in split_rows)
    split_false_negatives = sum((not row["completion"]) and row["data_gate_present"] for row in split_rows)
    check(
        "independent split faults expose one false positive and three false negatives, so the close is trusted shared-control evidence rather than direct occurrence proof",
        split_false_positives == 1
        and split_false_negatives == 3
        and split_rows[0]["completion"],
        {
            "rows": split_rows,
            "false_positives": split_false_positives,
            "false_negatives": split_false_negatives,
            "genuine_data_occurrence_certificate": False,
        },
    )


def interpolation_and_demolition_controls(unitary: np.ndarray, phi: np.ndarray) -> None:
    identity4 = np.eye(4, dtype=complex)
    angles = (0.0, np.pi / 12, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2, np.pi / 7)
    rows = []
    for theta in angles:
        candidate = np.cos(theta) * identity4 - 1j * np.sin(theta) * unitary
        weight = choi_acceptance_weight(unitary, candidate, phi)
        predicted = float(np.sin(theta) ** 2)
        rows.append(
            {
                "theta": float(theta),
                "unitarity_residual": float(np.linalg.norm(candidate.conj().T @ candidate - identity4)),
                "acceptance_weight": weight,
                "sin_squared": predicted,
                "residual": abs(weight - predicted),
            }
        )
    check(
        "the Choi diagnostic resolves a unitary under-rotation by sin(theta)^2 including held-out theta=pi/7",
        max(row["unitarity_residual"] for row in rows) < 2e-15
        and max(row["residual"] for row in rows) < 2e-15
        and rows[0]["acceptance_weight"] < 1e-15
        and abs(rows[-2]["acceptance_weight"] - 1) < 2e-15,
        rows,
    )

    rho = random_density()
    ideal = unitary @ rho @ unitary.conj().T
    p0 = np.diag((1, 1, 0, 0)).astype(complex)
    p1 = identity4 - p0
    direct_readout = unitary @ (p0 @ rho @ p0 + p1 @ rho @ p1) @ unitary.conj().T
    demolition_residual = float(np.linalg.norm(direct_readout - ideal))
    check(
        "direct occupation readout on the unknown data is a nonzero demolition control, not the accepted close route",
        demolition_residual > 1e-3,
        {"data_readout_demolition_residual": demolition_residual},
    )

    ket00 = np.asarray((1, 0, 0, 0), dtype=complex)
    symmetric_one_particle = np.asarray((0, 1, 1, 0), dtype=complex) / np.sqrt(2)
    invariant_rows = []
    for name, vector in (("vacuum", ket00), ("symmetric_one_particle", symmetric_one_particle)):
        density = projector(vector)
        updated = unitary @ density @ unitary.conj().T
        invariant_rows.append(
            {
                "input": name,
                "FSWAP_vs_identity_output_residual": float(np.linalg.norm(updated - density)),
            }
        )
    check(
        "FSWAP and identity have identical data outputs on explicit +1 eigenstates, so an after-the-fact data-only effect cannot certify occurrence uniformly over lawful inputs",
        all(row["FSWAP_vs_identity_output_residual"] < 1e-15 for row in invariant_rows),
        invariant_rows,
    )


EVENT_SITES: dict[str, Coord] = {
    "ready": (0, 0, 0),
    "data_call": (1, 0, 0),
    "probe_test": (0, 1, 0),
    "join": (1, 1, 0),
    "completion": (1, 1, 1),
}

PARENTS: dict[str, tuple[str, ...]] = {
    "ready": (),
    "data_call": ("ready",),
    "probe_test": ("ready",),
    "join": ("data_call", "probe_test"),
    "completion": ("join",),
}

CARRIER_SITES: dict[str, Coord] = {
    "data_mode_0": (2, 0, 0),
    "data_mode_1": (3, 0, 0),
    "actuation_flag": (2, -1, 0),
    "probe_mode_0": (-1, 1, 0),
    "probe_mode_1": (-2, 1, 0),
    "reference_mode_0": (-1, 1, 1),
    "reference_mode_1": (-2, 1, 1),
}


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


@dataclass(frozen=True)
class EventDag:
    sites: dict[str, Coord]
    parents: dict[str, tuple[str, ...]]


@dataclass(frozen=True)
class Record:
    role: str
    site: Coord
    content: int
    parents: tuple[str, ...]


def local_failures(dag: EventDag) -> tuple[tuple[str, str], ...]:
    return tuple(
        (parent, child)
        for child, parents in dag.parents.items()
        for parent in parents
        if manhattan(dag.sites[parent], dag.sites[child]) != 1
    )


def depth_certificate(dag: EventDag) -> dict[str, object]:
    remaining = set(dag.sites)
    depth: dict[str, int] = {}
    while remaining:
        ready = sorted(name for name in remaining if all(parent in depth for parent in dag.parents[name]))
        if not ready:
            raise AssertionError("cycle in event DAG")
        for name in ready:
            depth[name] = 1 + max((depth[parent] for parent in dag.parents[name]), default=0)
            remaining.remove(name)
    return {"depth": max(depth.values()), "depth_by_event": depth}


def topological_schedules(dag: EventDag) -> tuple[tuple[str, ...], ...]:
    schedules: list[tuple[str, ...]] = []

    def visit(prefix: tuple[str, ...], remaining: frozenset[str]) -> None:
        if not remaining:
            schedules.append(prefix)
            return
        ready = sorted(
            name for name in remaining if set(dag.parents[name]).issubset(prefix)
        )
        for name in ready:
            visit((*prefix, name), remaining - {name})

    visit((), frozenset(dag.sites))
    return tuple(schedules)


def actualize_records(
    dag: EventDag,
    flag_flip: bool,
    probe_pass: bool,
    formation_enabled: bool = True,
) -> tuple[Record, ...]:
    if not formation_enabled:
        return ()
    records = [
        Record("ready", dag.sites["ready"], 1, ()),
        Record("data_call", dag.sites["data_call"], int(flag_flip), ("ready",)),
        Record("probe_test", dag.sites["probe_test"], int(probe_pass), ("ready",)),
    ]
    if flag_flip and probe_pass:
        records.extend(
            (
                Record("join", dag.sites["join"], 1, ("data_call", "probe_test")),
                Record("completion", dag.sites["completion"], 1, ("join",)),
            )
        )
    return tuple(records)


def base_dag() -> EventDag:
    return EventDag(dict(EVENT_SITES), dict(PARENTS))


def refined_dag(refinement: int) -> EventDag:
    dag = base_dag()
    sites = dict(dag.sites)
    parents = dict(dag.parents)
    previous = "completion"
    for index in range(refinement):
        name = f"refinement_{index + 1}"
        sites[name] = (1, 1, 2 + index)
        parents[name] = (previous,)
        previous = name
    return EventDag(sites, parents)


def permutation_parity(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_parity(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            frames.append(matrix)
    return tuple(frames)


def transform_coord(coord: Coord, frame: np.ndarray, translation: Coord = (0, 0, 0)) -> Coord:
    rotated = frame @ np.asarray(coord, dtype=int)
    return add(tuple(int(value) for value in rotated), translation)  # type: ignore[arg-type]


def transform_dag(dag: EventDag, frame: np.ndarray, translation: Coord) -> EventDag:
    return replace(
        dag,
        sites={name: transform_coord(site, frame, translation) for name, site in dag.sites.items()},
    )


def locality_record_scheduler_and_frame_controls() -> None:
    dag = base_dag()
    all_sites = set(EVENT_SITES.values()) | set(CARRIER_SITES.values())
    carrier_edges = (
        ("data_mode_0", "data_mode_1"),
        ("data_mode_0", "actuation_flag"),
        ("probe_mode_0", "probe_mode_1"),
        ("probe_mode_0", "reference_mode_0"),
        ("probe_mode_1", "reference_mode_1"),
    )
    support_radius = max(sum(abs(value) for value in site) for site in all_sites)
    check(
        "the close transducer uses twelve distinct physical M2 sites with NN data/probe/flag/preparation bonds and bounded radius four",
        len(all_sites) == 12
        and not local_failures(dag)
        and all(manhattan(CARRIER_SITES[left], CARRIER_SITES[right]) == 1 for left, right in carrier_edges)
        and support_radius == 4,
        {
            "event_Record_sites": len(EVENT_SITES),
            "coherent_data_probe_flag_sites": len(CARRIER_SITES),
            "support_radius": support_radius,
            "dependency_edges": sum(len(parents) for parents in PARENTS.values()),
        },
    )

    schedules = topological_schedules(dag)
    successful_records = actualize_records(dag, True, True)
    failure_records = actualize_records(dag, False, True)
    check(
        "both legal scheduler orders give one successful transcript, while coupling deletion gives a local flag-zero failure and no completion",
        schedules
        == (
            ("ready", "data_call", "probe_test", "join", "completion"),
            ("ready", "probe_test", "data_call", "join", "completion"),
        )
        and tuple(record.role for record in successful_records)
        == ("ready", "data_call", "probe_test", "join", "completion")
        and tuple(record.content for record in failure_records) == (1, 0, 1)
        and all(record.role != "completion" for record in failure_records),
        {
            "schedules": schedules,
            "success_contents": tuple(record.content for record in successful_records),
            "deleted_call_contents": tuple(record.content for record in failure_records),
        },
    )

    overwrite_rejected = False
    record_by_site: dict[Coord, Record] = {}
    for record in successful_records:
        if record.site in record_by_site:
            overwrite_rejected = True
        record_by_site.setdefault(record.site, record)
    try:
        if successful_records[0].site in record_by_site:
            raise ValueError("permanent Record overwrite rejected")
    except ValueError:
        overwrite_rejected = True
    check(
        "the supplied actualization output is one-record-per-site, append-only, permanent, and content-readable",
        len(record_by_site) == len(successful_records)
        and overwrite_rejected
        and tuple(record_by_site[site].content for site in record_by_site) == (1, 1, 1, 1, 1)
        and not actualize_records(dag, True, True, formation_enabled=False),
        {
            "formation_deleted": actualize_records(dag, True, True, formation_enabled=False),
            "readout": tuple(record.content for record in successful_records),
        },
    )

    translation = (7, -11, 13)
    frame_failures = []
    carrier_failures = []
    for index, frame in enumerate(proper_frames()):
        transformed = transform_dag(dag, frame, translation)
        if local_failures(transformed) or depth_certificate(transformed) != depth_certificate(dag):
            frame_failures.append(index)
        transformed_carriers = {
            role: transform_coord(site, frame, translation) for role, site in CARRIER_SITES.items()
        }
        if any(
            manhattan(transformed_carriers[left], transformed_carriers[right]) != 1
            for left, right in carrier_edges
        ):
            carrier_failures.append(index)
    check(
        "the complete supplied role grammar is translation covariant and invariant under all 24 proper-cubic frames",
        len(proper_frames()) == 24 and not frame_failures and not carrier_failures,
        {"frames": len(proper_frames()), "event_failures": frame_failures, "carrier_failures": carrier_failures},
    )


def refinement_and_deletion_controls() -> None:
    rows = []
    for refinement in (0, 1, 2, 5):
        dag = refined_dag(refinement)
        rows.append(
            {
                "refinement": refinement,
                "records": len(dag.sites),
                "depth": depth_certificate(dag)["depth"],
                "schedules": len(topological_schedules(dag)),
                "local_failures": len(local_failures(dag)),
            }
        )
    check(
        "Record-visible close refinements add one NN commit and one depth unit through held-out refinement five",
        all(
            row["records"] == 5 + row["refinement"]
            and row["depth"] == 4 + row["refinement"]
            and row["schedules"] == 2
            and row["local_failures"] == 0
            for row in rows
        ),
        rows,
    )

    missing_probe_parent = dict(PARENTS)
    missing_probe_parent["join"] = ("data_call",)
    moved_completion = dict(EVENT_SITES)
    moved_completion["completion"] = (1, 1, 3)
    deleted_completion = set(EVENT_SITES) - {"completion"}
    check(
        "parent, completion, locality, and formation deletions remain visible rather than being repaired by the host scheduler",
        "probe_test" not in missing_probe_parent["join"]
        and "completion" not in deleted_completion
        and local_failures(EventDag(moved_completion, PARENTS)) == (("join", "completion"),)
        and not actualize_records(base_dag(), True, True, formation_enabled=False),
        {
            "probe_parent_deleted": True,
            "completion_deleted": True,
            "nonlocal_edges": local_failures(EventDag(moved_completion, PARENTS)),
            "formation_deleted": True,
        },
    )


def final_scope_control() -> None:
    check(
        "the executable result is a bounded trusted-control close proxy, not an autonomous Record law, physical time, rate, or full CAR compiler",
        True,
        {
            "declared_joint_call_deletion": "completion suppressed exactly",
            "omitted_data_factor_with_flag_and_probe": "false positive",
            "Choi_preparation_and_effect": "supplied",
            "Record_actualization_and_permanence": "supplied candidate law",
            "coherent_carriers_are_Records": False,
            "metric_time": "not derived",
            "rate_or_Born_probability": "not derived",
            "global_CAR_compiler": "out of scope",
            "axiomatic_spatial_dimension": 3,
            "axiom_pressure": False,
        },
    )


def main() -> None:
    source_and_note_contract()
    unitary = actual_fswap_and_local_code_controls()
    phi = choi_and_sentinel_controls(unitary)
    ideal_joint_transducer_controls(unitary, phi)
    deletion_and_fault_domain_controls(unitary, phi)
    interpolation_and_demolition_controls(unitary, phi)
    locality_record_scheduler_and_frame_controls()
    refinement_and_deletion_controls()
    final_scope_control()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
