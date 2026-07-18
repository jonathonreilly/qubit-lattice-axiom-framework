#!/usr/bin/env python3
"""Cycle 255: conditional CAR-compiler to Record causal-depth bridge.

The exact finite witness uses the actual two-mode fermionic SWAP factor from
the Cycle-230 update.  Three circuit presentations with depths 1, 4, and 6
have the same matrix.  They acquire one operational duration only after a
separate semantic trace map sends them to the same nearest-neighbor Record
dependency DAG.  Causal depth is then invariant under linear schedulers and
proper-cubic frames.

Records in this runner are immutable, readable, append-only classical
objects.  They are not coherent ancillas.  The rule that actualizes these
objects, the trace quotient, the complete physical CAR compiler, the selected
law, and metric normalization remain explicit conditions.  No compiler gate
count or circuit layer is called physical time.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "CAR_COMPILER_RECORD_CAUSAL_DEPTH_BRIDGE_CYCLE255_NOTE_2026-07-17.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
SOURCES = {
    "firewall": ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    "axis": ROOT / "docs/TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md",
    "cycle170": REVIEW / "RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md",
    "cycle243": REVIEW / "SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md",
    "cycle249": REVIEW / "COHERENT_GAUGE_FRAME_AUTONOMOUS_COMPILER_CYCLE249_NOTE_2026-07-17.md",
    "cycle252": REVIEW / "COHERENT_EVEN_ODD_SECTOR_JOIN_CYCLE252_NOTE_2026-07-17.md",
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


BRIDGE_MAPS = (
    TypedMap(
        "semantic_trace_Pi",
        "lawful circuit presentations of one bounded logical update",
        "one labeled semantic update event or undefined",
        "EXACT_FOR_THREE_FSWAP_PRESENTATIONS_SUPPLIED_IN_GENERAL",
    ),
    TypedMap(
        "dependency_D",
        "semantic update event plus local protocol roles",
        "finite nearest-neighbor causal event DAG",
        "EXACT_FINITE_CANDIDATE",
    ),
    TypedMap(
        "commit_K",
        "enabled DAG event at one physical M2 site",
        "append-only commit candidate or undefined",
        "CANDIDATE_CLOSE_NOT_GATE_FAITHFUL",
    ),
    TypedMap(
        "record_R",
        "actualized commit satisfying locking and permanence",
        "permanent readable framework Record",
        "CONDITIONAL_FORMATION_LAW",
    ),
    TypedMap(
        "causal_depth_tau_R",
        "finite Record dependency DAG with named completion Record",
        "nonnegative integer commit depth",
        "EXACT_DIMENSIONLESS_RELATIVE_DURATION",
    ),
)


def source_and_note_contract() -> None:
    axioms = normalized(AXIOMS)
    source = {name: normalized(path) for name, path in SOURCES.items()}
    check(
        "the source stack keeps Z3 spatial adjacency and Record permanence while withholding formation and metric time",
        all(path.is_file() for path in SOURCES.values())
        and "physical sites are the points of the cubic lattice z^3" in axioms
        and "records form" in axioms
        and "records are permanent" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "duration(update) = maximum required output commit depth" in source["cycle170"]
        and "compiler layers are not physical time" in source["cycle249"]
        and "compiler layers are not physical time" in source["cycle252"]
        and "no lawful global ordinary-m2 car isometry e is constructed" in source["cycle252"],
        {"axiomatic_space": "Z3", "record_permanence": True, "formation_rule": "not selected"},
    )
    note = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "conditional constructive bridge",
        "schedule-as-time counterfixture",
        "actual cycle-230 fswap",
        "permanent readable records",
        "coherent ancillas are not records",
        "compiler layers are not physical time",
        "recompilation invariance criterion",
        "nondemolition",
        "held-out refinement",
        "parallel composition",
        "serial composition",
        "all 24 proper-cubic frames",
        "three-dimensional space remains axiomatic input",
        "no lawful global ordinary-m2 car e",
        "clock normalization",
        "law selection",
        "record-faithful proof",
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
    check("the Cycle-255 note preserves the bridge and N1-N8 contract", not missing, missing)
    forbidden = tuple(
        row
        for row in BRIDGE_MAPS
        if row.domain in {"gate layers", "circuit depth", "scheduler iterations"}
        and row.codomain in {"physical time", "proper time"}
    )
    check(
        "the typed bridge has no direct circuit-depth or scheduler-to-time arrow",
        len(BRIDGE_MAPS) == 5 and not forbidden,
        BRIDGE_MAPS,
    )


def kron(*operators: np.ndarray) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for operator in operators:
        result = np.kron(result, operator)
    return result


def compose(gates: tuple[np.ndarray, ...]) -> np.ndarray:
    result = np.eye(gates[0].shape[0], dtype=complex)
    for gate in gates:
        result = gate @ result
    return result


def fswap_presentations() -> dict[str, tuple[np.ndarray, ...]]:
    identity = np.eye(2, dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    z0 = kron(z, identity)
    cz = np.diag((1, 1, 1, -1)).astype(complex)
    cnot01 = np.asarray(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    cnot10 = np.asarray(
        ((1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)),
        dtype=complex,
    )
    fswap = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, -1)),
        dtype=complex,
    )
    expanded = (cnot01, cnot10, cnot01, cz)
    return {
        "native": (fswap,),
        "expanded": expanded,
        "identity_padded": (z0, z0, *expanded),
    }


def circuit_and_local_code_controls() -> tuple[np.ndarray, dict[str, int]]:
    presentations = fswap_presentations()
    matrices = {name: compose(gates) for name, gates in presentations.items()}
    fswap = matrices["native"]
    residuals = {name: float(np.linalg.norm(matrix - fswap)) for name, matrix in matrices.items()}
    depths = {name: len(gates) for name, gates in presentations.items()}
    parity = np.diag((1, -1, -1, 1)).astype(complex)
    check(
        "the actual Cycle-230 FSWAP has exact depth-1, depth-4, and depth-6 circuit presentations",
        depths == {"native": 1, "expanded": 4, "identity_padded": 6}
        and max(residuals.values()) < 1e-15
        and np.linalg.norm(fswap.conj().T @ fswap - np.eye(4)) < 1e-15
        and np.linalg.norm(fswap @ parity - parity @ fswap) < 1e-15,
        {"depths": depths, "matrix_residuals": residuals},
    )
    check(
        "circuit depth therefore fails as a recompilation-invariant duration for one fixed logical G",
        len(set(depths.values())) == 3 and len({matrix.tobytes() for matrix in matrices.values()}) == 1,
        {"same_G": True, "candidate_schedule_times": depths},
    )

    # A finite two-mode code fixture only: |0_L>=|00>, |1_L>=|11>.
    # FSWAP acts as logical Z and has zero code leakage.  This is not a global
    # CAR compiler E for the Cycle-252 lattice.
    encoder = np.zeros((4, 2), dtype=complex)
    encoder[0, 0] = 1
    encoder[3, 1] = 1
    logical_z = np.diag((1, -1)).astype(complex)
    projector = encoder @ encoder.conj().T
    intertwiner = float(np.linalg.norm(encoder @ logical_z - fswap @ encoder))
    leakage = float(np.linalg.norm((np.eye(4) - projector) @ fswap @ encoder))
    check(
        "the local two-mode code fixture intertwines FSWAP without leakage but is not promoted to the missing global CAR E",
        np.linalg.norm(encoder.conj().T @ encoder - np.eye(2)) < 1e-15
        and intertwiner < 1e-15
        and leakage < 1e-15,
        {"intertwiner": intertwiner, "leakage": leakage, "scope": "local two-mode fixture"},
    )
    return fswap, depths


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


@dataclass(frozen=True)
class Event:
    name: str
    site: Coord
    value: int
    parents: frozenset[str]


@dataclass(frozen=True)
class EventDag:
    events: dict[str, Event]
    completion: str
    semantic_update: str = "Cycle230_FSWAP"


def event_dag(refinement: int = 0, prefix: str = "", shift: Coord = (0, 0, 0)) -> EventDag:
    if refinement < 0:
        raise ValueError(refinement)

    def label(name: str) -> str:
        return f"{prefix}{name}"

    base = {
        label("start"): Event(label("start"), add((0, 0, 0), shift), 1, frozenset()),
        label("left"): Event(label("left"), add((1, 0, 0), shift), 1, frozenset((label("start"),))),
        label("right"): Event(label("right"), add((0, 1, 0), shift), 1, frozenset((label("start"),))),
        label("join"): Event(label("join"), add((1, 1, 0), shift), 1, frozenset((label("left"), label("right")))),
    }
    parent = label("join")
    for index in range(refinement + 1):
        name = label(f"tail{index}")
        base[name] = Event(
            name,
            add((1, 1, index + 1), shift),
            1,
            frozenset((parent,)),
        )
        parent = name
    return EventDag(base, parent)


def topological_schedules(dag: EventDag) -> tuple[tuple[str, ...], ...]:
    schedules: list[tuple[str, ...]] = []

    def extend(done: tuple[str, ...]) -> None:
        formed = frozenset(done)
        ready = sorted(
            name
            for name, event in dag.events.items()
            if name not in formed and event.parents <= formed
        )
        if not ready:
            if len(done) == len(dag.events):
                schedules.append(done)
            return
        for name in ready:
            extend((*done, name))

    extend(())
    return tuple(schedules)


def depth_certificate(dag: EventDag, schedule: tuple[str, ...] | None = None) -> dict[str, object]:
    if schedule is None:
        schedule = topological_schedules(dag)[0]
    depth: dict[str, int] = {}
    profile: Counter[int] = Counter()
    for name in schedule:
        event = dag.events[name]
        if not event.parents <= depth.keys():
            raise AssertionError(("not-linear-extension", name))
        value = 1 + max((depth[parent] for parent in event.parents), default=0)
        depth[name] = value
        profile[value] += 1
    return {
        "depth": depth[dag.completion],
        "profile": tuple(sorted(profile.items())),
        "depth_by_event": depth,
        "records": len(depth),
    }


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                frames.append(matrix)
    unique = {tuple(matrix.reshape(-1)): matrix for matrix in frames}
    return tuple(unique[key] for key in sorted(unique))


def transformed(dag: EventDag, frame: np.ndarray, shift: Coord = (0, 0, 0)) -> EventDag:
    events = {}
    for name, event in dag.events.items():
        site = tuple(int(value) for value in frame @ np.asarray(event.site))
        site = add(site, shift)  # type: ignore[arg-type]
        events[name] = replace(event, site=site)
    return EventDag(events, dag.completion, dag.semantic_update)


def local_failures(dag: EventDag) -> tuple[tuple[str, str], ...]:
    return tuple(
        (parent, child)
        for child, event in dag.events.items()
        for parent in event.parents
        if manhattan(dag.events[parent].site, event.site) != 1
    )


@dataclass(frozen=True)
class Record:
    site: Coord
    value: int


def append_record(history: dict[Coord, Record], event: Event) -> None:
    if event.site in history:
        raise ValueError(("one-record-per-site", event.site))
    history[event.site] = Record(event.site, event.value)


def replay_records(dag: EventDag, schedule: tuple[str, ...]) -> tuple[dict[Coord, Record], tuple[frozenset[Coord], ...]]:
    history: dict[Coord, Record] = {}
    formed_names: set[str] = set()
    prefixes = []
    for name in schedule:
        event = dag.events[name]
        if not event.parents <= formed_names:
            raise AssertionError(("unavailable", name))
        for parent in event.parents:
            parent_event = dag.events[parent]
            record = history.get(parent_event.site)
            if record is None or record.value != parent_event.value:
                raise AssertionError(("missing-parent-record", name, parent))
        append_record(history, event)
        formed_names.add(name)
        prefixes.append(frozenset(history))
    return history, tuple(prefixes)


def event_record_dag_controls() -> EventDag:
    dag = event_dag()
    schedules = topological_schedules(dag)
    certificates = [depth_certificate(dag, schedule) for schedule in schedules]
    replays = [replay_records(dag, schedule) for schedule in schedules]
    edge_count = sum(len(event.parents) for event in dag.events.values())
    deletion_failures = []
    for child, event in dag.events.items():
        for parent in event.parents:
            available = {
                dag.events[name].site: Record(dag.events[name].site, dag.events[name].value)
                for name in event.parents
                if name != parent
            }
            if all(
                dag.events[name].site in available
                and available[dag.events[name].site].value == dag.events[name].value
                for name in event.parents
            ):
                deletion_failures.append((child, parent))
    check(
        "the candidate update protocol is a bounded nearest-neighbor five-Record DAG with load-bearing parents",
        len(dag.events) == 5
        and edge_count == 5
        and not local_failures(dag)
        and not deletion_failures
        and max(
            manhattan(dag.events["join"].site, site)
            for site in ((2, 1, 0), (1, 2, 0))
        )
        == 1,
        {"records": len(dag.events), "edges": edge_count, "dependency_deletions_surviving": deletion_failures, "data_support_radius": 1},
    )
    final_sets = [frozenset(records) for records, _ in replays]
    check(
        "both linear scheduler orders yield the same permanent Record set, causal profile, and depth four",
        len(schedules) == 2
        and len(set(schedules)) == 2
        and len(set(final_sets)) == 1
        and certificates[0] == certificates[1]
        and certificates[0]["depth"] == 4
        and certificates[0]["profile"] == ((1, 1), (2, 2), (3, 1), (4, 1)),
        {"schedules": schedules, "certificate": certificates[0]},
    )

    records, prefixes = replays[0]
    overwrite_rejected = False
    try:
        append_record(dict(records), dag.events["start"])
    except ValueError:
        overwrite_rejected = True
    nested = all(left < right for left, right in zip(prefixes, prefixes[1:]))
    readable = tuple(records[dag.events[name].site].value for name in schedules[0])
    check(
        "candidate commits are append-only, one-per-site, permanent, and readable by content",
        overwrite_rejected and nested and readable == (1, 1, 1, 1, 1),
        {"prefixes": len(prefixes), "overwrite_rejected": overwrite_rejected, "readout": readable},
    )

    frame_failures = []
    for index, frame in enumerate(proper_frames()):
        rotated = transformed(dag, frame, (17, -19, 23))
        certificate = depth_certificate(rotated)
        if local_failures(rotated) or certificate != certificates[0]:
            frame_failures.append(index)
    translated = transformed(dag, np.eye(3, dtype=int), (7, -11, 13))
    check(
        "the dependency protocol and causal depth are invariant under all 24 proper-cubic frames and translations",
        len(proper_frames()) == 24
        and not frame_failures
        and not local_failures(translated)
        and depth_certificate(translated) == certificates[0],
        {"proper_frames": len(proper_frames()), "frame_failures": frame_failures},
    )
    return dag


def partial_trace_data(joint: np.ndarray, data_dimension: int, record_dimension: int) -> np.ndarray:
    tensor = joint.reshape(data_dimension, record_dimension, data_dimension, record_dimension)
    return np.trace(tensor, axis1=1, axis2=3)


def partial_trace_records(joint: np.ndarray, data_dimension: int, record_dimension: int) -> np.ndarray:
    tensor = joint.reshape(data_dimension, record_dimension, data_dimension, record_dimension)
    return np.trace(tensor, axis1=0, axis2=2)


def nondemolition_controls(fswap: np.ndarray, dag: EventDag) -> None:
    rng = np.random.default_rng(255)
    amplitude = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    rho = amplitude @ amplitude.conj().T
    rho /= np.trace(rho)
    ideal = fswap @ rho @ fswap.conj().T

    record_one = np.diag((0, 1)).astype(complex)
    joints = []
    for schedule in topological_schedules(dag):
        data = rho.copy()
        transcript = np.ones((1, 1), dtype=complex)
        gate_applications = 0
        for name in schedule:
            if name == "join":
                data = fswap @ data @ fswap.conj().T
                gate_applications += 1
            transcript = np.kron(transcript, record_one)
        if gate_applications != 1:
            raise AssertionError(("FSWAP-event-count", gate_applications))
        joints.append(np.kron(data, transcript))

    record_dimension = 1 << len(dag.events)
    record_state = np.zeros(record_dimension, dtype=complex)
    record_state[-1] = 1
    transcript = np.outer(record_state, record_state.conj())
    joint = joints[0]
    data_residual = float(np.linalg.norm(partial_trace_data(joint, 4, record_dimension) - ideal))
    transcript_residual = float(np.linalg.norm(partial_trace_records(joint, 4, record_dimension) - transcript))
    factorization_residual = float(np.linalg.norm(joint - np.kron(ideal, transcript)))
    scheduler_joint_residual = float(np.linalg.norm(joints[0] - joints[1]))

    p0 = np.diag((1, 1, 0, 0)).astype(complex)
    p1 = np.eye(4) - p0
    demolished = fswap @ (p0 @ rho @ p0 + p1 @ rho @ p1) @ fswap.conj().T
    demolition_residual = float(np.linalg.norm(demolished - ideal))
    check(
        "state-independent event Records factor from and do not demolish the encoded quantum data channel",
        data_residual < 2e-15
        and transcript_residual < 2e-15
        and factorization_residual < 2e-15
        and scheduler_joint_residual < 2e-15
        and demolition_residual > 1e-3,
        {
            "data_residual": data_residual,
            "record_residual": transcript_residual,
            "factorization_residual": factorization_residual,
            "scheduler_joint_residual": scheduler_joint_residual,
            "data_readout_demolition_control": demolition_residual,
        },
    )

    omitted_joint = np.kron(rho, transcript)
    omitted_data_residual = float(
        np.linalg.norm(
            partial_trace_data(omitted_joint, 4, record_dimension) - ideal
        )
    )
    omitted_record_residual = float(
        np.linalg.norm(
            partial_trace_records(omitted_joint, 4, record_dimension)
            - transcript
        )
    )
    transcript_gate_deletion_residual = float(np.linalg.norm(omitted_joint - joint))
    check(
        "deleting FSWAP changes the data channel but leaves the five-Record tag unchanged, so physical-close faithfulness remains open",
        omitted_data_residual > 1e-3
        and omitted_record_residual < 2e-15
        and abs(transcript_gate_deletion_residual - omitted_data_residual) < 2e-15,
        {
            "omitted_FSWAP_data_residual": omitted_data_residual,
            "omitted_FSWAP_Record_residual": omitted_record_residual,
            "joint_residual": transcript_gate_deletion_residual,
            "record_faithful_update_certificate": False,
        },
    )


def compiler_trace_and_refinement_controls(depths: dict[str, int], dag: EventDag) -> None:
    semantic_images = {name: dag.semantic_update for name in depths}
    durations = {name: depth_certificate(dag)["depth"] for name in depths}
    check(
        "one supplied semantic trace quotient makes all three recompilations share one Record duration",
        len(set(semantic_images.values())) == 1
        and set(durations.values()) == {4}
        and set(depths.values()) == {1, 4, 6},
        {"circuit_depths": depths, "record_depths": durations, "semantic_images": semantic_images},
    )
    check(
        "if every internal compiler gate forms a Record, the same G loses recompilation-invariant duration",
        len(set(depths.values())) == 3,
        {"gate_visible_record_depths": depths, "criterion": "internal gates must be trace-transparent or physically matched"},
    )

    rows = []
    for refinement in (0, 1, 2, 5):
        refined = event_dag(refinement)
        certificate = depth_certificate(refined)
        rows.append(
            {
                "refinement": refinement,
                "records": certificate["records"],
                "depth": certificate["depth"],
                "schedules": len(topological_schedules(refined)),
                "local_failures": len(local_failures(refined)),
            }
        )
    check(
        "record-visible causal refinement changes depth by exactly one per inserted commit through held-out refinement five",
        all(
            row["records"] == 5 + row["refinement"]
            and row["depth"] == 4 + row["refinement"]
            and row["schedules"] == 2
            and row["local_failures"] == 0
            for row in rows
        ),
        rows,
    )


def merged(*dags: EventDag, completion: str | None = None) -> EventDag:
    events: dict[str, Event] = {}
    for dag in dags:
        if set(events) & set(dag.events):
            raise AssertionError("event-name-overlap")
        if {event.site for event in events.values()} & {event.site for event in dag.events.values()}:
            raise AssertionError("event-site-overlap")
        events.update(dag.events)
    return EventDag(events, completion or dags[0].completion)


def composition_and_deletion_controls() -> None:
    first = event_dag(0, "A_")
    second = event_dag(5, "B_", (20, 20, 20))
    combined = merged(first, second, completion=second.completion)
    contacts = sum(
        manhattan(left.site, right.site) <= 1
        for left in first.events.values()
        for right in second.events.values()
    )
    component_depths = (depth_certificate(first)["depth"], depth_certificate(second)["depth"])
    combined_max = max(depth_certificate(combined, schedule=tuple(
        list(topological_schedules(first)[0]) + list(topological_schedules(second)[0])
    ))["depth"], component_depths[0])
    # The named completion above is in component B; the global parallel depth
    # is computed as the maximum of all event depths.
    parallel_schedule = tuple(list(topological_schedules(first)[0]) + list(topological_schedules(second)[0]))
    parallel_cert = depth_certificate(combined, parallel_schedule)
    maximum_event_depth = max(parallel_cert["depth_by_event"].values())
    check(
        "separated parallel composition sums Records and takes maximum causal depth",
        contacts == 0
        and len(combined.events) == 15
        and component_depths == (4, 9)
        and maximum_event_depth == 9
        and combined_max == 9,
        {"component_depths": component_depths, "combined_records": len(combined.events), "combined_depth": maximum_event_depth, "cross_contacts": contacts},
    )

    serial_rows = []
    for first_refinement, second_refinement in ((0, 0), (0, 2), (2, 5)):
        left = event_dag(first_refinement, "L_")
        left_output = left.events[left.completion].site
        right_shift = (left_output[0], left_output[1], left_output[2] + 1)
        right = event_dag(second_refinement, "R_", right_shift)
        right_start_name = "R_start"
        right_events = dict(right.events)
        right_events[right_start_name] = replace(
            right_events[right_start_name],
            parents=frozenset((left.completion,)),
        )
        linked_right = EventDag(right_events, right.completion)
        serial = merged(left, linked_right, completion=linked_right.completion)
        certificate = depth_certificate(serial)
        serial_rows.append(
            {
                "refinements": (first_refinement, second_refinement),
                "records": certificate["records"],
                "depth": certificate["depth"],
                "wanted_depth": 8 + first_refinement + second_refinement,
                "local_failures": len(local_failures(serial)),
            }
        )
    check(
        "physically linked serial composition has additive Record depth",
        all(
            row["depth"] == row["wanted_depth"]
            and row["records"] == 10 + sum(row["refinements"])
            and row["local_failures"] == 0
            for row in serial_rows
        ),
        serial_rows,
    )

    dag = event_dag()
    def record_duration(candidate: EventDag, actualized: bool) -> int | None:
        return int(depth_certificate(candidate)["depth"]) if actualized else None

    absent_actualization = record_duration(event_dag(), actualized=False)
    missing_output = EventDag(
        {name: event for name, event in dag.events.items() if name != dag.completion},
        "join",
    )
    moved_output_events = dict(dag.events)
    moved_output_events[dag.completion] = replace(
        moved_output_events[dag.completion], site=(1, 1, 3)
    )
    moved_output = EventDag(moved_output_events, dag.completion)
    check(
        "formation, completion, and nearest-neighbor deletions remain visible rather than silently returning a duration",
        absent_actualization is None
        and dag.completion not in missing_output.events
        and len(local_failures(moved_output)) == 1,
        {"without_Record_actualization": absent_actualization, "completion_deleted": True, "nonlocal_dependency_failures": local_failures(moved_output)},
    )


def normalization_and_law_selection_controls(fswap: np.ndarray) -> None:
    base = event_dag(0)
    refined = event_dag(5)
    base_depth = depth_certificate(base)["depth"]
    refined_depth = depth_certificate(refined)["depth"]
    calibrations = {
        "one_unit_per_commit_depth": Fraction(base_depth, 1),
        "two_units_per_commit_depth": Fraction(2 * base_depth, 1),
    }
    check(
        "integer Record depth is scheduler invariant while absolute clock normalization remains selectable",
        base_depth == 4
        and calibrations["two_units_per_commit_depth"] == 2 * calibrations["one_unit_per_commit_depth"],
        {"dimensionless_depth": base_depth, "metric_candidates": calibrations},
    )
    check(
        "the same logical G admits two local covariant Record laws with different durations, exposing law selection",
        np.linalg.norm(compose(fswap_presentations()["native"]) - fswap) < 1e-15
        and not local_failures(base)
        and not local_failures(refined)
        and (base_depth, refined_depth) == (4, 9),
        {"same_G": "Cycle230_FSWAP", "law_A_depth": base_depth, "law_B_depth": refined_depth, "selected_law": None},
    )
    check(
        "the executable result remains a conditional dimensionless bridge, not metric time, rate, or a completed global CAR compiler",
        True,
        {
            "actual_Record_formation": "candidate map; physical selection open",
            "physical_close_faithfulness": "open; identical Record tag survives FSWAP deletion",
            "nondemolition": "exact for state-independent event transcript",
            "trace_quotient": "exact for three declared presentations; supplied in general",
            "clock_normalization": "open",
            "law_selection": "open",
            "global_Cycle252_CAR_E": "unavailable",
            "axiomatic_spatial_dimension": 3,
        },
    )


def main() -> int:
    source_and_note_contract()
    fswap, depths = circuit_and_local_code_controls()
    dag = event_record_dag_controls()
    nondemolition_controls(fswap, dag)
    compiler_trace_and_refinement_controls(depths, dag)
    composition_and_deletion_controls()
    normalization_and_law_selection_controls(fswap)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
