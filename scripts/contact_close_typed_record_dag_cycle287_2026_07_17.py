#!/usr/bin/env python3
"""Cycle 287: conditional event-to-Record receiving DAG for Cycle 281.

The Cycle-281 couple/archive/recouple is driven by a Cycle-282-style physical
one-hot program state.  Its positive close and history carrier feed an
explicit event -> commit -> Record dependency DAG only when lawful occurrence,
commit, Record-typing, and permanence inputs are supplied.  Program phase and
dependency rank are not interpreted as time, and no clock count is produced.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_autonomous_apparatus_law_cycle282_2026_07_17 as c282
import matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17 as c281


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONTACT_CLOSE_TYPED_RECORD_DAG_CYCLE287_NOTE_2026-07-17.md"
)
TOL = 4.0e-11
PASS = 0
FAIL = 0

IDLE, WRITE, ARCHIVE, RESET, CLOSE, EXPORT = range(6)
ROLE_NAMES = {
    IDLE: "IDLE",
    WRITE: "U_I_WRITE",
    ARCHIVE: "ARCHIVE",
    RESET: "U_I_RESET",
    CLOSE: "POSITIVE_CLOSE",
    EXPORT: "HISTORY_EXPORT",
}
RECEIVER_PROGRAM = (
    WRITE,
    ARCHIVE,
    RESET,
    CLOSE,
    EXPORT,
    IDLE,
    IDLE,
    IDLE,
    IDLE,
    IDLE,
    IDLE,
    IDLE,
)


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
        check("the Cycle-287 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-281 same-code deletion-faithful positive close",
        "cycle-282 physical program state",
        "typed event→commit→record→causal-dag contract",
        "conditional on lawful occurrence and record typing",
        "schedule/topological-order invariance",
        "all edge deletions",
        "proper-cubic carried covariance",
        "parallel composition",
        "serial composition",
        "deleting either u_i removes the candidate event and commit",
        "apparatus steps and program phase are not time",
        "no clock count is assigned",
        "named recurrent record chain is absent",
        "interval matcher is absent",
        "supplied-interface inventory",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent obstruction",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "note preserves the conditional DAG, clock firewall, inventory, and N1-N8 contracts",
        not missing,
        missing,
    )


def receiver_permutation(role: int) -> np.ndarray:
    if role == ARCHIVE:
        return c281.permutation_for_flip(
            c281.ARCHIVE, {c281.POINTER: 1}
        )
    if role == CLOSE:
        return c281.permutation_for_flip(
            c281.CLOSE,
            {c281.ARCHIVE: 1, c281.POINTER: 0},
        )
    if role == EXPORT:
        return c281.permutation_for_flip(
            c281.HISTORY,
            {c281.ARCHIVE: 1, c281.CLOSE: 1},
        )
    raise ValueError(("role has no interface permutation", role))


def one_hot_token(phase: int, length: int) -> tuple[int, ...]:
    if not 0 <= phase < length:
        raise ValueError("phase outside physical program rail")
    return tuple(int(index == phase) for index in range(length))


def apply_program_role(
    state: np.ndarray,
    role: int,
    *,
    first: str,
    second: str,
) -> np.ndarray:
    if role == WRITE:
        return c281.apply_coupling(state, first)
    if role == RESET:
        return c281.apply_coupling(state, second)
    if role in (ARCHIVE, CLOSE, EXPORT):
        return c281.apply_permutation(state, receiver_permutation(role))
    if role == IDLE:
        return state.copy()
    raise ValueError(("unknown receiver role", role))


def program_trajectory(
    initial: np.ndarray,
    *,
    first: str = "ideal",
    second: str = "ideal",
    program: tuple[int, ...] = RECEIVER_PROGRAM,
    phase: int = 0,
    steps: int = 5,
) -> tuple[tuple[np.ndarray, ...], tuple[tuple[int, ...], ...]]:
    if len(program) != len(c282.PROGRAM):
        raise ValueError("receiver uses the twelve-site Cycle-282 rail")
    if any(role not in ROLE_NAMES for role in program):
        raise ValueError("unknown physical receiver role")
    if steps < 0:
        raise ValueError("steps must be nonnegative")
    token = one_hot_token(phase, len(program))
    states = [initial]
    tokens = [token]
    for _ in range(steps):
        role = program[phase]
        states.append(
            apply_program_role(
                states[-1], role, first=first, second=second
            )
        )
        phase = (phase + 1) % len(program)
        tokens.append(one_hot_token(phase, len(program)))
    return tuple(states), tuple(tokens)


def programmed_isometry(
    first: str = "ideal",
    second: str = "ideal",
    program: tuple[int, ...] = RECEIVER_PROGRAM,
    phase: int = 0,
) -> np.ndarray:
    blank = c281.basis(c281.ANCILLA_DIMENSION, 0)
    columns = []
    for occupation in range(c281.MATTER_DIMENSION):
        initial = np.kron(c281.basis(c281.MATTER_DIMENSION, occupation), blank)
        states, _tokens = program_trajectory(
            initial,
            first=first,
            second=second,
            program=program,
            phase=phase,
        )
        columns.append(states[-1])
    return np.column_stack(columns)


def ancilla_index(state: np.ndarray) -> int:
    support = np.flatnonzero(np.abs(state) > 1.0e-13)
    if len(support) != 1 or abs(abs(state[support[0]]) - 1) > TOL:
        raise ValueError("expected one classical basis trajectory")
    return int(support[0] % c281.ANCILLA_DIMENSION)


@dataclass(frozen=True)
class PhysicalPacket:
    write: bool
    archive: bool
    reset: bool
    candidate_event: bool
    history_export: bool
    close_effect_norm: float
    history_effect_norm: float


def physical_packet(first: str = "ideal", second: str = "ideal") -> PhysicalPacket:
    active = np.kron(
        c281.basis(c281.MATTER_DIMENSION, 0b11),
        c281.basis(c281.ANCILLA_DIMENSION, 0),
    )
    stages, _tokens = program_trajectory(active, first=first, second=second)
    words = tuple(ancilla_index(state) for state in stages)
    bit = lambda word, position: (word >> position) & 1
    isometry = programmed_isometry(first, second)
    close_effect = c281.ancilla_effect(isometry, {c281.CLOSE: 1})
    history_effect = c281.ancilla_effect(isometry, {c281.HISTORY: 1})
    close_norm = float(np.linalg.norm(close_effect))
    history_norm = float(np.linalg.norm(history_effect))
    return PhysicalPacket(
        write=bit(words[1], c281.POINTER) == 1,
        archive=(
            bit(words[2], c281.POINTER) == 1
            and bit(words[2], c281.ARCHIVE) == 1
        ),
        reset=(
            bit(words[3], c281.POINTER) == 0
            and bit(words[3], c281.ARCHIVE) == 1
        ),
        candidate_event=bit(words[4], c281.CLOSE) == 1 and close_norm > TOL,
        history_export=(
            bit(words[5], c281.HISTORY) == 1 and history_norm > TOL
        ),
        close_effect_norm=close_norm,
        history_effect_norm=history_norm,
    )


def physical_program_and_close_controls() -> dict[str, PhysicalPacket]:
    programmed = programmed_isometry()
    direct = c281.isometry(c281.candidate_gates())
    program_residual = float(np.linalg.norm(programmed - direct))
    tokens = tuple(one_hot_token(phase, len(RECEIVER_PROGRAM)) for phase in range(6))
    check(
        "a Cycle-282-style physical one-hot program state drives the exact Cycle-281 five-stage receiver",
        program_residual < TOL
        and len(RECEIVER_PROGRAM) == len(c282.PROGRAM) == 12
        and len(set(RECEIVER_PROGRAM[:5])) == 5
        and all(sum(token) == 1 for token in tokens)
        and 3 * len(RECEIVER_PROGRAM) == 36,
        {
            "program_isometry_residual": program_residual,
            "active_roles": tuple(ROLE_NAMES[role] for role in RECEIVER_PROGRAM[:5]),
            "rail_M2": len(RECEIVER_PROGRAM),
            "role_marker_M2": 3 * len(RECEIVER_PROGRAM),
            "host_selected_stage_actions": 0,
        },
    )

    packets = {
        "ideal": physical_packet(),
        "delete_first_U_I": physical_packet(first="deleted"),
        "delete_second_U_I": physical_packet(second="deleted"),
        "delete_both_U_I": physical_packet(first="deleted", second="deleted"),
    }
    _, q = c281.contact_projectors()
    check(
        "the programmed ideal candidate event/history effects equal Q while deleting either U_I removes both",
        packets["ideal"].write
        and packets["ideal"].archive
        and packets["ideal"].reset
        and packets["ideal"].candidate_event
        and packets["ideal"].history_export
        and abs(packets["ideal"].close_effect_norm - np.linalg.norm(q)) < TOL
        and all(
            not packet.candidate_event
            and not packet.history_export
            and packet.close_effect_norm < TOL
            and packet.history_effect_norm < TOL
            for label, packet in packets.items()
            if label != "ideal"
        ),
        packets,
    )
    return packets


@dataclass(frozen=True)
class Dag:
    nodes: frozenset[str]
    edges: frozenset[tuple[str, str]]


BASE_NODES = frozenset(
    (
        "write",
        "archive",
        "reset",
        "candidate_event",
        "history_export",
        "actual_event",
        "commit",
        "Record",
        "permanent_Record",
    )
)
BASE_EDGES = frozenset(
    (
        ("write", "archive"),
        ("archive", "reset"),
        ("archive", "candidate_event"),
        ("reset", "candidate_event"),
        ("candidate_event", "history_export"),
        ("candidate_event", "actual_event"),
        ("actual_event", "commit"),
        ("history_export", "commit"),
        ("commit", "Record"),
        ("Record", "permanent_Record"),
    )
)
BASE_DAG = Dag(BASE_NODES, BASE_EDGES)


def parents(dag: Dag) -> dict[str, frozenset[str]]:
    return {
        node: frozenset(left for left, right in dag.edges if right == node)
        for node in dag.nodes
    }


def topological_orders(dag: Dag):
    parent_map = parents(dag)

    def visit(order: tuple[str, ...], remaining: frozenset[str]):
        if not remaining:
            yield order
            return
        ready = sorted(
            node
            for node in remaining
            if parent_map[node] <= set(order)
        )
        for node in ready:
            yield from visit(order + (node,), remaining - {node})

    yield from visit((), dag.nodes)


def local_formation(
    packet: PhysicalPacket,
    *,
    occurrence: bool,
    commit_map: bool,
    record_typing: bool,
    permanence: bool,
) -> dict[str, bool]:
    for label, value in {
        "occurrence": occurrence,
        "commit_map": commit_map,
        "record_typing": record_typing,
        "permanence": permanence,
    }.items():
        if not isinstance(value, bool):
            raise ValueError(f"{label} must be explicitly Boolean")
    return {
        "write": packet.write,
        "archive": packet.archive,
        "reset": packet.reset,
        "candidate_event": packet.candidate_event,
        "history_export": packet.history_export,
        "actual_event": occurrence,
        "commit": commit_map,
        "Record": record_typing,
        "permanent_Record": permanence,
    }


def replay_dag(
    dag: Dag,
    order: tuple[str, ...],
    local: dict[str, bool],
    available_edges: frozenset[tuple[str, str]] | None = None,
) -> frozenset[str]:
    if set(order) != set(dag.nodes) or len(order) != len(dag.nodes):
        raise ValueError("schedule must contain every DAG node exactly once")
    position = {node: index for index, node in enumerate(order)}
    if any(position[left] >= position[right] for left, right in dag.edges):
        raise ValueError("schedule is not a topological order")
    available = dag.edges if available_edges is None else available_edges
    parent_map = parents(dag)
    formed: set[str] = set()
    for node in order:
        inputs = parent_map[node]
        if local[node] and all(
            parent in formed and (parent, node) in available
            for parent in inputs
        ):
            formed.add(node)
    return frozenset(formed)


def dependency_rank(dag: Dag, order: tuple[str, ...]) -> dict[str, int]:
    parent_map = parents(dag)
    ranks = {}
    for node in order:
        ranks[node] = 1 + max(
            (ranks[parent] for parent in parent_map[node]),
            default=0,
        )
    return ranks


def prefix_dag(dag: Dag, prefix: str) -> Dag:
    return Dag(
        frozenset(f"{prefix}:{node}" for node in dag.nodes),
        frozenset(
            (f"{prefix}:{left}", f"{prefix}:{right}")
            for left, right in dag.edges
        ),
    )


def parallel_dag() -> Dag:
    first = prefix_dag(BASE_DAG, "A")
    second = prefix_dag(BASE_DAG, "B")
    return Dag(first.nodes | second.nodes, first.edges | second.edges)


def serial_dag() -> Dag:
    parallel = parallel_dag()
    return Dag(
        parallel.nodes,
        parallel.edges | {("A:permanent_Record", "B:write")},
    )


def prefixed_local(local: dict[str, bool], *prefixes: str) -> dict[str, bool]:
    return {
        f"{prefix}:{node}": value
        for prefix in prefixes
        for node, value in local.items()
    }


def conditional_dag_controls(packets: dict[str, PhysicalPacket]) -> dict[str, object]:
    ideal_local = local_formation(
        packets["ideal"],
        occurrence=True,
        commit_map=True,
        record_typing=True,
        permanence=True,
    )
    schedules = tuple(topological_orders(BASE_DAG))
    outcomes = tuple(replay_dag(BASE_DAG, order, ideal_local) for order in schedules)
    ranks = tuple(dependency_rank(BASE_DAG, order) for order in schedules)
    check(
        "the conditional receiving DAG is invariant under every base topological order",
        len(schedules) == 2
        and len(set(outcomes)) == 1
        and outcomes[0] == BASE_NODES
        and len({tuple(sorted(row.items())) for row in ranks}) == 1,
        {
            "topological_orders": schedules,
            "formed_nodes": tuple(sorted(outcomes[0])),
            "maximum_dependency_rank_not_time": max(ranks[0].values()),
        },
    )

    order = schedules[0]
    edge_rows = []
    for edge in sorted(BASE_DAG.edges):
        cut = BASE_DAG.edges - {edge}
        formed = replay_dag(BASE_DAG, order, ideal_local, cut)
        edge_rows.append(
            {
                "edge": edge,
                "child_removed": edge[1] not in formed,
                "permanent_Record_removed": "permanent_Record" not in formed,
            }
        )
    check(
        "all edge deletions are load bearing for their child and the final conditional permanent Record",
        len(edge_rows) == len(BASE_EDGES) == 10
        and all(row["child_removed"] and row["permanent_Record_removed"] for row in edge_rows),
        edge_rows,
    )

    semantic_rows = {}
    for key in ("occurrence", "commit_map", "record_typing", "permanence"):
        flags = {
            "occurrence": True,
            "commit_map": True,
            "record_typing": True,
            "permanence": True,
        }
        flags[key] = False
        formed = replay_dag(
            BASE_DAG,
            order,
            local_formation(packets["ideal"], **flags),
        )
        semantic_rows[key] = tuple(sorted(formed))
    check(
        "occurrence, commit, Record typing, and conditional permanence uses remain separately exposed to deletion",
        "actual_event" not in semantic_rows["occurrence"]
        and "commit" not in semantic_rows["occurrence"]
        and "commit" not in semantic_rows["commit_map"]
        and "Record" not in semantic_rows["record_typing"]
        and "Record" in semantic_rows["permanence"]
        and "permanent_Record" not in semantic_rows["permanence"],
        semantic_rows,
    )

    fault_rows = {}
    for label in ("delete_first_U_I", "delete_second_U_I", "delete_both_U_I"):
        formed = replay_dag(
            BASE_DAG,
            order,
            local_formation(
                packets[label],
                occurrence=True,
                commit_map=True,
                record_typing=True,
                permanence=True,
            ),
        )
        fault_rows[label] = tuple(sorted(formed))
    check(
        "deleting either U_I removes the candidate event and commit even when every semantic import is granted",
        all(
            "candidate_event" not in row
            and "commit" not in row
            and "Record" not in row
            for row in fault_rows.values()
        ),
        fault_rows,
    )
    return {
        "base_topological_orders": len(schedules),
        "base_dependency_rank": max(ranks[0].values()),
        "edge_deletions": len(edge_rows),
    }


def composition_controls(packet: PhysicalPacket) -> dict[str, int]:
    base_local = local_formation(
        packet,
        occurrence=True,
        commit_map=True,
        record_typing=True,
        permanence=True,
    )
    rows = {}
    for label, dag, expected_schedules, expected_rank in (
        ("parallel", parallel_dag(), 194_480, 8),
        ("serial", serial_dag(), 4, 16),
    ):
        local = prefixed_local(base_local, "A", "B")
        terminal = None
        count = 0
        rank_signatures = set()
        for order in topological_orders(dag):
            formed = replay_dag(dag, order, local)
            if terminal is None:
                terminal = formed
            elif formed != terminal:
                raise AssertionError((label, "schedule dependence"))
            rank = dependency_rank(dag, order)
            rank_signatures.add(tuple(sorted(rank.items())))
            count += 1
        maximum_rank = max(dict(next(iter(rank_signatures))).values())
        rows[label] = {
            "schedules": count,
            "formed": len(terminal or ()),
            "maximum_dependency_rank_not_time": maximum_rank,
            "rank_signatures": len(rank_signatures),
        }
        if count != expected_schedules or maximum_rank != expected_rank:
            rows[label]["unexpected"] = True
    check(
        "parallel and serial conditional Record-DAG compositions are topological-order invariant",
        rows["parallel"]
        == {
            "schedules": 194_480,
            "formed": 18,
            "maximum_dependency_rank_not_time": 8,
            "rank_signatures": 1,
        }
        and rows["serial"]
        == {
            "schedules": 4,
            "formed": 18,
            "maximum_dependency_rank_not_time": 16,
            "rank_signatures": 1,
        },
        rows,
    )

    serial = serial_dag()
    serial_order = next(topological_orders(serial))
    serial_cut = serial.edges - {("A:permanent_Record", "B:write")}
    formed = replay_dag(
        serial,
        serial_order,
        prefixed_local(base_local, "A", "B"),
        serial_cut,
    )
    check(
        "the serial join is load bearing while parallel composition has no hidden cross-edge",
        "A:permanent_Record" in formed
        and "B:write" not in formed
        and not (
            parallel_dag().edges
            & {
                (left, right)
                for left in prefix_dag(BASE_DAG, "A").nodes
                for right in prefix_dag(BASE_DAG, "B").nodes
            }
        ),
        {"serial_join_cut_formed": tuple(sorted(formed))},
    )
    return {label: int(row["schedules"]) for label, row in rows.items()}


NODE_COORDS = {
    "write": (0, 0, 0),
    "archive": (1, 0, 0),
    "reset": (1, 1, 0),
    "candidate_event": (0, 1, 0),
    "history_export": (0, 1, 1),
    "actual_event": (0, 1, 0),
    "commit": (0, 1, 1),
    "Record": (1, 1, 1),
    "permanent_Record": (1, 1, 1),
}


def distance_signature(coordinates: dict[str, tuple[int, int, int]]) -> tuple:
    return tuple(
        sorted(
            (
                left,
                right,
                sum(
                    (coordinates[left][axis] - coordinates[right][axis]) ** 2
                    for axis in range(3)
                ),
            )
            for index, left in enumerate(sorted(coordinates))
            for right in sorted(coordinates)[index + 1 :]
        )
    )


def covariance_controls() -> None:
    code = c281.c269.build_code(3)
    base_bs = c281.c278.cell_bs(code, (0, 0, 0))
    local_family = set(code.local_checks)
    central_pivots, central_bad = c281.c278.phase_reducer(
        list(code.local_checks + code.wilsons), code.qubits
    )
    base_signature = distance_signature(NODE_COORDS)
    failures = []
    frames = c281.c235.proper_cubic_frames()
    for frame in frames:
        frame_vertex, frame_edge = c281.c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c281.c269.repair_data(
            code.graph, frame_vertex, frame_edge
        )
        transformed_bs = tuple(
            c281.c235.apply_gauge(
                c281.c235.permute_pauli(row, frame_edge),
                toggles,
                pairs,
                flips,
            )
            for row in base_bs
        )
        transformed_local = {
            c281.c235.apply_gauge(
                c281.c235.permute_pauli(row, frame_edge),
                toggles,
                pairs,
                flips,
            )
            for row in code.local_checks
        }
        transformed_wilsons = tuple(
            c281.c235.apply_gauge(
                c281.c235.permute_pauli(row, frame_edge),
                toggles,
                pairs,
                flips,
            )
            for row in code.wilsons
        )
        carried = {
            label: tuple(int(value) for value in frame @ np.asarray(site))
            for label, site in NODE_COORDS.items()
        }
        valid = (
            round(float(np.linalg.det(frame))) == 1
            and set(transformed_bs) == set(base_bs)
            and transformed_local == local_family
            and not central_bad
            and all(
                not c281.c278.reduce_pauli(
                    row, central_pivots, code.qubits
                ).symplectic(code.qubits)
                for row in transformed_wilsons
            )
            and distance_signature(carried) == base_signature
        )
        if not valid:
            failures.append(frame.tolist())
    check(
        "the Q-controlled receiver, carried program roles, and conditional DAG have proper-cubic carried covariance",
        len(frames) == 24 and not failures,
        {
            "proper_cubic_frames": len(frames),
            "failures": failures,
            "Q_role": "proper-cubic scalar",
            "program_and_DAG_roles": "carried supplied data",
        },
    )


def clock_count_if_lawful(
    record_chain: tuple[str, ...],
    *,
    recurrent: bool,
    matcher: object | None,
) -> None:
    if not record_chain or not recurrent or matcher is None:
        return None
    raise AssertionError("Cycle 287 must not instantiate a clock")


def time_firewall_and_inventory_controls() -> dict[str, object]:
    inventory = {
        "occurrence": "supplied lawful actual-event/identity map",
        "commit": "supplied event-to-append-only-commit map K",
        "Record_typing_and_formation": "supplied map R",
        "permanence": "supplied by current Record axiom only after lawful Record typing",
        "program_role_word": "supplied Cycle-282-style physical state",
        "program_phase_origin": "supplied physical control state",
        "named_recurrent_Record_chain": None,
        "interval_matcher": None,
        "clock_calibration": None,
    }
    candidate = clock_count_if_lawful(
        ("A:Record", "B:Record"),
        recurrent=False,
        matcher=None,
    )
    text = normalized(NOTE)
    check(
        "apparatus steps, program phase, scheduler order, and dependency rank remain distinct from time",
        candidate is None
        and inventory["named_recurrent_Record_chain"] is None
        and inventory["interval_matcher"] is None
        and "apparatus steps and program phase are not time" in text
        and "no clock count is assigned" in text,
        inventory,
    )
    return inventory


def lawful_domain_controls() -> None:
    blank = np.kron(
        c281.basis(c281.MATTER_DIMENSION, 0),
        c281.basis(c281.ANCILLA_DIMENSION, 0),
    )
    rejected = 0
    invalid = (
        {"program": RECEIVER_PROGRAM[:-1]},
        {"program": (99,) * len(RECEIVER_PROGRAM)},
        {"phase": len(RECEIVER_PROGRAM)},
        {"steps": -1},
        {"first": "unknown"},
    )
    for arguments in invalid:
        try:
            program_trajectory(blank, **arguments)
        except ValueError:
            rejected += 1
    try:
        local_formation(
            physical_packet(),
            occurrence=1,  # type: ignore[arg-type]
            commit_map=True,
            record_typing=True,
            permanence=True,
        )
    except ValueError:
        rejected += 1
    check(
        "lawful domain rejects malformed program, phase, coupling, and semantic-import inputs",
        rejected == 6,
        rejected,
    )


def main() -> int:
    note_contract()
    packets = physical_program_and_close_controls()
    dag_data = conditional_dag_controls(packets)
    composition = composition_controls(packets["ideal"])
    covariance_controls()
    inventory = time_firewall_and_inventory_controls()
    lawful_domain_controls()
    check(
        "the conditional receiving bridge creates no route-independent obstruction or axiom pressure",
        dag_data["edge_deletions"] == 10
        and composition == {"parallel": 194_480, "serial": 4}
        and inventory["interval_matcher"] is None
        and "no route-independent obstruction" in normalized(NOTE)
        and "no axiom pressure" in normalized(NOTE),
    )
    print("DATA physical_packets", packets)
    print("DATA dag", dag_data)
    print("DATA composition_schedules", composition)
    print("DATA supplied_inventory", inventory)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    if FAIL:
        print("RESULT CYCLE287_CONTACT_CLOSE_TYPED_RECORD_DAG_RED")
        return 1
    print("RESULT CYCLE287_CONTACT_CLOSE_TYPED_RECORD_DAG_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
