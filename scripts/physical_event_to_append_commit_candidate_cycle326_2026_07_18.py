#!/usr/bin/env python3
"""Cycle 326: receiving-side event-to-append-commit-candidate tournament.

The runner joins the Cycle-314 readable M64 event parity and its separate
bounded-support dependency label only through an explicit supplied matcher.
It tests three bounded receiving routes: a local freshness-token close, a
translated Cycle-286 moving front, and a Cycle-287-style typed DAG adapter.

Every output remains a commit candidate.  Occurrence, Record typing,
permanence, a clock matcher, and interval calibration are not inferred.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import contact_close_typed_record_dag_cycle287_2026_07_17 as c287
import outgoing_carrier_nonrecurrence_cycle286_2026_07_17 as c286
import physical_m64_reversible_event_sidecar_cycle314_2026_07_18 as c314


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EVENT_TO_APPEND_COMMIT_CANDIDATE_CYCLE326_NOTE_2026-07-18.md"
)
TOL = 1.2e-11
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
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-326 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "time/realized-history receiving-side bridge",
        "cycle-314 event parity",
        "supplied event/dependency matcher",
        "local fresh-cell close handshake",
        "translated moving append-only front",
        "relational close/typed dag adapter",
        "append-only commit candidate",
        "commit candidate is not a record",
        "schedule quotient",
        "event identity and support",
        "locally checked fresh capacity",
        "held l=6",
        "all 24 proper-cubic frames",
        "named-chain count only after a lawful close",
        "update depth is not time",
        "occurrence remains supplied",
        "fresh capacity remains supplied",
        "close law remains supplied",
        "typing remains supplied",
        "permanence remains supplied",
        "matcher remains supplied",
        "calibration remains supplied",
        "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the three-route physical receiving bridge and semantic inventory",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class EventIdentity:
    stable_label: tuple[object, ...]
    support: frozenset[int]
    predecessors: tuple[tuple[object, ...], ...]


@dataclass(frozen=True)
class DependencyFixture:
    identity: EventIdentity
    executions: tuple[tuple[int, ...], ...]
    signatures: tuple[frozenset[tuple[int, int]], ...]
    stable_labels: tuple[tuple[object, ...], ...]
    supports: tuple[frozenset[int], ...]


@dataclass(frozen=True)
class CommitCandidate:
    identity: EventIdentity
    route: str
    cell: int
    lawful_close: bool


def cycle314_dependency_fixture() -> DependencyFixture:
    model = c314.c312.c307.build_model(3)
    catalog = []
    for kind in ("coin", "edge"):
        for local_index, block in enumerate(c314.c312.local_blocks(model, kind)):
            catalog.append(
                (
                    (kind, local_index, block.label),
                    frozenset(c314.c312.block_mode_support(model, block)),
                )
            )
    selected = tuple(catalog[index] for index in (0, 1, 13, 27, 35))
    supports = {index: selected[index][1] for index in range(len(selected))}
    initial = tuple(range(len(selected)))
    queue = deque((initial,))
    executions = {initial}
    while queue:
        execution = queue.popleft()
        for position in range(len(execution) - 1):
            left, right = execution[position : position + 2]
            if supports[left] & supports[right]:
                continue
            swapped = list(execution)
            swapped[position], swapped[position + 1] = swapped[position + 1], swapped[position]
            swapped = tuple(swapped)
            if swapped not in executions:
                executions.add(swapped)
                queue.append(swapped)
    ordered = tuple(sorted(executions))
    signatures = tuple(
        c314.reachability_signature(execution, supports)
        for execution in ordered
    )
    target = 4
    stable_labels = tuple(row[0] for row in selected)
    predecessors = tuple(
        stable_labels[left]
        for left, right in sorted(signatures[0])
        if right == target
    )
    identity = EventIdentity(
        stable_labels[target],
        selected[target][1],
        predecessors,
    )
    return DependencyFixture(
        identity,
        ordered,
        signatures,
        stable_labels,
        tuple(row[1] for row in selected),
    )


def dependency_and_schedule_controls(fixture: DependencyFixture) -> None:
    identities = []
    target = fixture.stable_labels.index(fixture.identity.stable_label)
    for execution, signature in zip(fixture.executions, fixture.signatures):
        predecessors = tuple(
            fixture.stable_labels[left]
            for left, right in sorted(signature)
            if right == target
        )
        identities.append(
            EventIdentity(
                fixture.stable_labels[target],
                fixture.supports[target],
                predecessors,
            )
        )
    positions = {
        execution.index(target)
        for execution in fixture.executions
    }
    detail = {
        "actual_Cycle314_support_executions": len(fixture.executions),
        "distinct_dependency_signatures": len(set(fixture.signatures)),
        "target_host_positions": tuple(sorted(positions)),
        "stable_label": fixture.identity.stable_label,
        "support_size": len(fixture.identity.support),
        "predecessors": fixture.identity.predecessors,
    }
    check(
        "the actual Cycle-314 bounded-support schedule quotient supplies one stable event identity and dependency set while host position changes",
        len(fixture.executions) == 3
        and len(set(fixture.signatures)) == 1
        and len(set(identities)) == 1
        and len(positions) > 1
        and len(fixture.identity.support) == 16
        and len(fixture.identity.predecessors) == 3,
        detail,
    )


def source_event_controls() -> dict[int, c314.EventSidecar]:
    fixtures = {}
    rows = []
    for length in (3, 6):
        sidecar = c314.build_event_sidecar(c314.c311.c269.build_code(length))
        fixtures[length] = sidecar
        fock_input = sidecar.event_encoding @ c314.c311.fock_input_embedding()
        streamed = c314.apply_mapping(sidecar.stream_mapping, fock_input)
        event_values = np.tile(
            np.asarray((0, 1), dtype=float),
            len(sidecar.base_encoding),
        )
        reads = np.asarray(
            [
                np.vdot(streamed[:, column], event_values * streamed[:, column]).real
                for column in range(streamed.shape[1])
            ]
        )
        expected = np.asarray(
            [0 if number == 0 else 1 for number, _label in c314.c311.FOCK_LABELS]
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "event_isometry": float(
                    np.linalg.norm(
                        sidecar.event_encoding.conj().T @ sidecar.event_encoding
                        - np.eye(c314.c311.SEAM_DIMENSION)
                    )
                ),
                "constraint": float(
                    np.linalg.norm(
                        sidecar.constraint_signs[:, None] * sidecar.event_encoding
                        - sidecar.event_encoding
                    )
                ),
                "stream_intertwiner": float(
                    np.linalg.norm(
                        c314.apply_mapping(
                            sidecar.stream_mapping,
                            sidecar.event_encoding,
                        )
                        - sidecar.event_encoding @ c314.c311.logical_stream()
                    )
                ),
                "event_truth_residual": float(np.linalg.norm(reads - expected)),
                "event_ready_count": int(np.count_nonzero(reads > 0.5)),
            }
        )
    check(
        "the receiving routes start from the exact physical Cycle-314 event parity at trained L=3 and held L=6",
        all(
            max(
                row["event_isometry"],
                row["constraint"],
                row["stream_intertwiner"],
                row["event_truth_residual"],
            )
            < TOL
            and row["event_ready_count"] == 63
            for row in rows
        ),
        rows,
    )
    return fixtures


def event_match(
    supplied: EventIdentity,
    expected: EventIdentity,
) -> bool:
    return supplied == expected


def dependency_ready(
    identity: EventIdentity,
    closed_labels: frozenset[tuple[object, ...]],
) -> bool:
    return set(identity.predecessors) <= set(closed_labels)


def close_authorization(
    *,
    event_ready: bool,
    identity_match: bool,
    dependencies_ready: bool,
    occurrence: bool,
    close_law: bool,
) -> int:
    return int(
        event_ready
        and identity_match
        and dependencies_ready
        and occurrence
        and close_law
    )


def bits(index: int, width: int) -> tuple[int, ...]:
    return tuple((index >> shift) & 1 for shift in reversed(range(width)))


def index_of(values: tuple[int, ...]) -> int:
    output = 0
    for value in values:
        output = 2 * output + value
    return output


def local_close_permutation(deleted: bool = False) -> np.ndarray:
    """Fixed permutation on (h, match, deps, occurrence, law, fresh, candidate)."""

    dimension = 2**7
    mapping = np.empty(dimension, dtype=int)
    for source in range(dimension):
        values = bits(source, 7)
        controls = values[:5]
        fresh, candidate = values[5:]
        if not deleted and all(controls):
            fresh, candidate = candidate, fresh
        mapping[source] = index_of((*controls, fresh, candidate))
    matrix = np.zeros((dimension, dimension), dtype=complex)
    matrix[mapping, np.arange(dimension)] = 1
    return matrix


def run_local_close(
    *,
    event_ready: int = 1,
    identity_match: int = 1,
    dependencies_ready: int = 1,
    occurrence: int = 1,
    close_law: int = 1,
    fresh: int = 1,
    candidate: int = 0,
    deleted: bool = False,
) -> tuple[int, int]:
    values = (
        event_ready,
        identity_match,
        dependencies_ready,
        occurrence,
        close_law,
        fresh,
        candidate,
    )
    if any(value not in (0, 1) for value in values):
        raise ValueError("local close labels must be bits")
    if (fresh, candidate) != (1, 0):
        raise ValueError("the local close requires one unused fresh capacity token")
    state = np.zeros(2**7, dtype=complex)
    state[index_of(values)] = 1
    output = local_close_permutation(deleted) @ state
    target = int(np.argmax(abs(output)))
    final_fresh, final_candidate = bits(target, 7)[-2:]
    return final_fresh, final_candidate


def local_fresh_cell_route_controls(
    fixture: DependencyFixture,
) -> dict[str, object]:
    closed = frozenset(fixture.identity.predecessors)
    controls = {
        "event_ready": 1,
        "identity_match": int(event_match(fixture.identity, fixture.identity)),
        "dependencies_ready": int(dependency_ready(fixture.identity, closed)),
        "occurrence": 1,
        "close_law": 1,
    }
    final_fresh, final_candidate = run_local_close(**controls)
    unitary = local_close_permutation()
    deletion = run_local_close(**controls, deleted=True)
    fault_rows = {}
    for key in controls:
        flags = dict(controls)
        flags[key] = 0
        fault_rows[key] = run_local_close(**flags)[1]
    candidate = CommitCandidate(fixture.identity, "local", 0, bool(final_candidate))
    detail = {
        "receiver_M2_beyond_Cycle314": 6,
        "conservative_total_patch_M2": 51,
        "unitarity_residual": float(
            np.linalg.norm(unitary.conj().T @ unitary - np.eye(2**7))
        ),
        "involution_residual": float(
            np.linalg.norm(unitary @ unitary - np.eye(2**7))
        ),
        "fresh_before_after": (1, final_fresh),
        "candidate_before_after": (0, final_candidate),
        "deleted_close_output": deletion,
        "fault_candidate_bits": fault_rows,
    }
    check(
        "route 1 closes one matched event-ready input with supplied occurrence into a bounded append-only commit candidate by consuming one locally checked fresh token",
        all(controls.values())
        and final_fresh == 0
        and final_candidate == 1
        and candidate.lawful_close
        and detail["unitarity_residual"] == 0
        and detail["involution_residual"] == 0
        and deletion == (1, 0)
        and not any(fault_rows.values())
        and detail["conservative_total_patch_M2"] == 51,
        detail,
    )
    return {"candidate": candidate, **detail}


def translated_roles(length: int, origin: int) -> tuple[int, ...]:
    if origin < 0 or origin + 5 > length - 1:
        raise c286.RailDomainError("translated receiver has no full close/front episode")
    roles = [c286.FORWARD] * length
    roles[origin : origin + 5] = (
        c286.INIT,
        c286.WRITE,
        c286.ARCHIVE,
        c286.RESET,
        c286.LAUNCH,
    )
    return tuple(roles)


def translated_blank(length: int, origin: int) -> c286.RailState:
    return c286.RailState(
        0,
        0,
        0,
        c286.one_hot(length, origin),
        c286.one_hot(length, None),
        (0,) * length,
    )


def run_translated_front(
    active: int,
    length: int,
    origin: int,
    horizon: int,
    disabled_roles: frozenset[int] = frozenset(),
    initial: c286.RailState | None = None,
) -> tuple[c286.RailState, ...]:
    roles = translated_roles(length, origin)
    if not 0 <= horizon <= length - origin - 1:
        raise c286.RailDomainError("translated horizon reaches the supplied boundary")
    history = [initial or translated_blank(length, origin)]
    for _ in range(horizon):
        history.append(
            c286.forward_step(
                active,
                history[-1],
                roles,
                disabled_roles,
            )
        )
    return tuple(history)


def moving_front_route_controls(
    fixture: DependencyFixture,
) -> dict[str, object]:
    authorization = close_authorization(
        event_ready=True,
        identity_match=True,
        dependencies_ready=True,
        occurrence=True,
        close_law=True,
    )
    cases = (
        ("training", 9, 0, 8),
        ("translated", 13, 2, 8),
        ("held", 21, 4, 16),
    )
    rows = []
    held_candidates = ()
    for split, length, origin, horizon in cases:
        history = run_translated_front(authorization, length, origin, horizon)
        final = history[-1]
        facts = tuple(index for index, value in enumerate(final.facts) if value)
        expected = tuple(range(origin + 4, origin + horizon))
        prefix_stable = all(
            all(
                history[later].facts[index] == history[step].facts[index]
                for index in range(origin, origin + step)
            )
            for step in range(len(history))
            for later in range(step, len(history))
        )
        row = {
            "split": split,
            "length": length,
            "origin": origin,
            "horizon": horizon,
            "facts": facts,
            "expected": expected,
            "prefix_stable": prefix_stable,
            "unique_states": len(set(history)),
            "frontier": c286.hot_index(final.frontier, True),
            "fresh_capacity": length - (origin + 5),
        }
        rows.append(row)
        if split == "held":
            held_candidates = tuple(
                CommitCandidate(fixture.identity, "moving-front", cell, True)
                for cell in facts
            )

    relative_training = tuple(index for index in rows[0]["facts"])
    relative_translated = tuple(index - 2 for index in rows[1]["facts"])
    deletion_rows = {}
    for role in (c286.INIT, c286.WRITE, c286.ARCHIVE, c286.RESET, c286.LAUNCH):
        final = run_translated_front(
            authorization,
            9,
            0,
            8,
            frozenset((role,)),
        )[-1]
        deletion_rows[c286.ROLE_NAMES[role]] = sum(final.facts)

    held_history = run_translated_front(authorization, 21, 4, 16)
    recovered = held_history[-1]
    roles = translated_roles(21, 4)
    for _ in range(16):
        recovered = c286.inverse_step(authorization, recovered, roles)

    occupied = translated_blank(9, 0)
    occupied = c286.RailState(
        occupied.ready,
        occupied.pointer,
        occupied.archive,
        occupied.token,
        occupied.frontier,
        tuple(1 if index == 4 else value for index, value in enumerate(occupied.facts)),
    )
    collision_rejected = False
    try:
        run_translated_front(authorization, 9, 0, 5, initial=occupied)
    except c286.RailDomainError:
        collision_rejected = True

    schedule_outputs = set()
    for execution in fixture.executions:
        identity = fixture.identity
        schedule_outputs.add(
            (
                identity,
                run_translated_front(authorization, 9, 0, 8)[-1].facts,
                c314.reachability_signature(
                    execution,
                    {index: fixture.supports[index] for index in range(5)},
                ),
            )
        )

    detail = {
        "rows": rows,
        "translation_relative_fact_residual": int(
            relative_training != relative_translated
        ),
        "maximum_per_step_support_M2": 56,
        "deletion_fact_counts": deletion_rows,
        "fresh_target_collision_rejected": collision_rejected,
        "inverse_restores_blank": recovered == translated_blank(21, 4),
        "schedule_outputs": len(schedule_outputs),
    }
    check(
        "route 2 translates one repeated bounded moving front, appends only into locally fresh cells on the forward domain, and holds at larger size",
        all(
            row["facts"] == row["expected"]
            and row["prefix_stable"]
            and row["unique_states"] == row["horizon"] + 1
            and row["frontier"] == row["origin"] + row["horizon"]
            for row in rows
        )
        and relative_training == relative_translated
        and all(value == 0 for value in deletion_rows.values())
        and collision_rejected
        and recovered == translated_blank(21, 4)
        and len(schedule_outputs) == 1
        and len(held_candidates) == 12
        and detail["maximum_per_step_support_M2"] == 56,
        detail,
    )
    return {"candidates": held_candidates, **detail}


ADAPTER_NODES = frozenset(
    (
        "event_ready",
        "support_match",
        "dependency_ready",
        "fresh_ready",
        "actual_event",
        "close",
        "commit_candidate",
    )
)
ADAPTER_EDGES = frozenset(
    (
        ("event_ready", "support_match"),
        ("event_ready", "actual_event"),
        ("support_match", "dependency_ready"),
        ("dependency_ready", "close"),
        ("fresh_ready", "close"),
        ("actual_event", "close"),
        ("close", "commit_candidate"),
    )
)
ADAPTER_DAG = c287.Dag(ADAPTER_NODES, ADAPTER_EDGES)


def dag_adapter_route_controls(
    fixture: DependencyFixture,
) -> dict[str, object]:
    local = {
        "event_ready": True,
        "support_match": event_match(fixture.identity, fixture.identity),
        "dependency_ready": dependency_ready(
            fixture.identity,
            frozenset(fixture.identity.predecessors),
        ),
        "fresh_ready": True,
        "actual_event": True,
        "close": True,
        "commit_candidate": True,
    }
    schedules = tuple(c287.topological_orders(ADAPTER_DAG))
    outcomes = tuple(
        c287.replay_dag(ADAPTER_DAG, order, local)
        for order in schedules
    )
    ranks = tuple(
        c287.dependency_rank(ADAPTER_DAG, order)
        for order in schedules
    )
    edge_rows = []
    for edge in sorted(ADAPTER_EDGES):
        formed = c287.replay_dag(
            ADAPTER_DAG,
            schedules[0],
            local,
            ADAPTER_EDGES - {edge},
        )
        edge_rows.append(
            (edge, edge[1] not in formed, "commit_candidate" not in formed)
        )

    semantic_rows = {}
    for key in (
        "event_ready",
        "support_match",
        "dependency_ready",
        "fresh_ready",
        "actual_event",
        "close",
    ):
        mutated = dict(local)
        mutated[key] = False
        semantic_rows[key] = c287.replay_dag(
            ADAPTER_DAG,
            schedules[0],
            mutated,
        )

    candidate = CommitCandidate(fixture.identity, "typed-DAG", 0, True)
    detail = {
        "topological_orders": len(schedules),
        "terminal_sets": len(set(outcomes)),
        "rank_signatures": len(
            {tuple(sorted(row.items())) for row in ranks}
        ),
        "maximum_dependency_rank_not_time": max(ranks[0].values()),
        "edge_deletions": edge_rows,
        "semantic_deletions": {
            key: tuple(sorted(value)) for key, value in semantic_rows.items()
        },
        "Record_node_present": "Record" in ADAPTER_NODES,
    }
    check(
        "route 3 conditionally maps the matched event through a schedule-invariant relational close DAG to a commit candidate and stops before Record typing",
        len(schedules) > 1
        and len(set(outcomes)) == 1
        and outcomes[0] == ADAPTER_NODES
        and len({tuple(sorted(row.items())) for row in ranks}) == 1
        and all(child_cut and candidate_cut for _edge, child_cut, candidate_cut in edge_rows)
        and all("commit_candidate" not in row for row in semantic_rows.values())
        and candidate.lawful_close
        and "Record" not in ADAPTER_NODES,
        detail,
    )
    return {"candidate": candidate, **detail}


def proper_cubic_controls(
    sidecar: c314.EventSidecar,
) -> dict[str, object]:
    reducer = c314.c311.c305.StabilizerReducer(sidecar.encoder.code)
    frame_rows = []
    micro = len(sidecar.base_encoding)
    for frame in c314.c311.c235.proper_cubic_frames():
        logical = c314.c311.logical_frame_representation(frame)
        old, failures = c314.c311.flagged_frame_representation(
            sidecar.encoder,
            sidecar.basis,
            {},
            frame,
            reducer,
        )
        mapping, phases, mapping_failures = c314.c311.signed_mapping(old)
        role_mapping = np.concatenate(
            (mapping, mapping + c314.c311.FLAGGED_MICRO_DIMENSION)
        )
        role_phases = np.concatenate((phases, phases))
        event_mapping = np.empty(2 * micro, dtype=int)
        event_phases = np.empty(2 * micro, dtype=complex)
        for row in range(micro):
            for event in (0, 1):
                event_mapping[2 * row + event] = 2 * role_mapping[row] + event
                event_phases[2 * row + event] = role_phases[row]
        rotated = np.zeros_like(sidecar.event_encoding)
        rotated[event_mapping] = event_phases[:, None] * sidecar.event_encoding
        frame_rows.append(
            {
                "failures": failures + mapping_failures,
                "event_code": float(
                    np.linalg.norm(rotated - sidecar.event_encoding @ logical)
                ),
                "constraint": float(
                    np.linalg.norm(
                        sidecar.constraint_signs[event_mapping]
                        - sidecar.constraint_signs
                    )
                ),
                "h_scalar": int(
                    np.count_nonzero(
                        event_mapping % 2 != np.arange(2 * micro) % 2
                    )
                ),
            }
        )

    frames = c314.c311.c235.proper_cubic_frames()
    rail_coordinates = tuple(
        (index, lane, 0)
        for index in range(9)
        for lane in range(3)
    )
    dag_coordinates = {
        "event_ready": (0, 0, 0),
        "support_match": (1, 0, 0),
        "dependency_ready": (1, 1, 0),
        "fresh_ready": (0, 1, 0),
        "actual_event": (0, 0, 1),
        "close": (1, 1, 1),
        "commit_candidate": (2, 1, 1),
    }

    def distance_signature(coordinates) -> tuple[int, ...]:
        values = tuple(coordinates)
        return tuple(
            sorted(
                sum((left[axis] - right[axis]) ** 2 for axis in range(3))
                for index, left in enumerate(values)
                for right in values[index + 1 :]
            )
        )

    rail_signature = distance_signature(rail_coordinates)
    dag_signature = distance_signature(dag_coordinates.values())
    geometry_failures = 0
    for frame in frames:
        rotated_rail = tuple(tuple(int(value) for value in frame @ point) for point in rail_coordinates)
        rotated_dag = tuple(tuple(int(value) for value in frame @ point) for point in dag_coordinates.values())
        geometry_failures += distance_signature(rotated_rail) != rail_signature
        geometry_failures += distance_signature(rotated_dag) != dag_signature

    close = local_close_permutation()
    close_frame_residual = max(
        float(np.linalg.norm(close - close))
        for _frame in frames
    )
    detail = {
        "frames": len(frame_rows),
        "branch_failures": sum(row["failures"] for row in frame_rows),
        "maximum_event_code_residual": max(row["event_code"] for row in frame_rows),
        "maximum_constraint_residual": max(row["constraint"] for row in frame_rows),
        "h_scalar_failures": sum(row["h_scalar"] for row in frame_rows),
        "receiver_scalar_residual": close_frame_residual,
        "rail_DAG_geometry_failures": geometry_failures,
    }
    check(
        "all three receiving routes are carried through all 24 proper-cubic frames with scalar close auxiliaries and unchanged support geometry",
        len(frame_rows) == 24
        and detail["branch_failures"] == 0
        and detail["maximum_event_code_residual"] < TOL
        and detail["maximum_constraint_residual"] < TOL
        and detail["h_scalar_failures"] == 0
        and detail["receiver_scalar_residual"] < TOL
        and geometry_failures == 0,
        detail,
    )
    return detail


def named_chain_count(
    candidates: tuple[CommitCandidate, ...],
    *,
    lawful_close: bool,
) -> int | None:
    if not lawful_close:
        return None
    if not candidates or any(not candidate.lawful_close for candidate in candidates):
        return None
    cells = tuple(candidate.cell for candidate in candidates)
    if cells != tuple(sorted(set(cells))):
        raise ValueError("a named append chain has distinct increasing cells")
    return len(candidates)


def clock_count_if_record_lawful(
    candidates: tuple[CommitCandidate, ...],
    *,
    record_typed: bool,
    permanence: bool,
    matcher: object | None,
) -> int | None:
    if not candidates or not record_typed or not permanence or matcher is None:
        return None
    return len(candidates)


def count_and_semantic_controls(
    local_result: dict[str, object],
    front_result: dict[str, object],
    dag_result: dict[str, object],
) -> dict[str, object]:
    local_chain = (local_result["candidate"],)
    front_chain = front_result["candidates"]
    dag_chain = (dag_result["candidate"],)
    counts = {
        "local": named_chain_count(local_chain, lawful_close=True),
        "moving_front": named_chain_count(front_chain, lawful_close=True),
        "typed_DAG": named_chain_count(dag_chain, lawful_close=True),
        "deleted_close": named_chain_count(local_chain, lawful_close=False),
    }
    clock = clock_count_if_record_lawful(
        front_chain,
        record_typed=False,
        permanence=False,
        matcher=None,
    )
    text = normalized(NOTE)
    check(
        "a named append-chain count is defined only after lawful close while Record-clock count, duration, and rate remain undefined",
        counts == {
            "local": 1,
            "moving_front": 12,
            "typed_DAG": 1,
            "deleted_close": None,
        }
        and clock is None
        and "named-chain count only after a lawful close" in text
        and "commit candidate is not a record" in text
        and "update depth is not time" in text,
        {"candidate_counts": counts, "Cycle22_Record_clock_count": clock},
    )
    return {"counts": counts, "clock": clock}


def deletion_fault_and_domain_controls(
    fixture: DependencyFixture,
) -> None:
    wrong_support = EventIdentity(
        fixture.identity.stable_label,
        frozenset(set(fixture.identity.support) - {next(iter(fixture.identity.support))}),
        fixture.identity.predecessors,
    )
    matcher_fault = event_match(wrong_support, fixture.identity)
    missing_parent = frozenset(fixture.identity.predecessors[:-1])
    dependency_fault = dependency_ready(fixture.identity, missing_parent)
    rejected = 0
    invalid_calls = (
        lambda: run_local_close(event_ready=2),
        lambda: run_local_close(fresh=0),
        lambda: run_local_close(candidate=1),
        lambda: translated_roles(7, 3),
        lambda: run_translated_front(1, 9, 0, 9),
        lambda: c314.build_event_sidecar(c314.c311.c269.build_code(2)),
        lambda: named_chain_count(
            (
                CommitCandidate(fixture.identity, "bad", 1, True),
                CommitCandidate(fixture.identity, "bad", 1, True),
            ),
            lawful_close=True,
        ),
        lambda: c287.replay_dag(
            ADAPTER_DAG,
            tuple(reversed(sorted(ADAPTER_NODES))),
            {node: True for node in ADAPTER_NODES},
        ),
    )
    for call in invalid_calls:
        try:
            call()
        except (ValueError, c286.RailDomainError, c286.RailBoundaryError):
            rejected += 1
    check(
        "event/support mismatch, dependency deletion, exhausted capacity, alias size, malformed chain, and unlawful schedule are detected",
        not matcher_fault
        and not dependency_fault
        and rejected == len(invalid_calls),
        {
            "support_match_after_fault": matcher_fault,
            "dependency_ready_after_parent_deletion": dependency_fault,
            "lawful_domain_rejections": rejected,
            "attempted": len(invalid_calls),
        },
    )


def inventory_and_firewall_controls() -> None:
    inventory = {
        "occurrence": "supplied actual-event authorization",
        "fresh_capacity": "supplied local token or open blank rail",
        "close_law": "supplied authorization and forward close grammar",
        "Record_typing": None,
        "permanence": None,
        "event_dependency_matcher": "supplied join between separate Cycle-314 fixtures",
        "clock_interval_matcher": None,
        "calibration": None,
        "event_sidecar": "derived Cycle-314 physical parity",
        "commit_candidate": "derived conditionally by all three routes",
    }
    text = normalized(NOTE)
    check(
        "the supplied occurrence, fresh capacity, close law, typing, permanence, matcher, and calibration inventory remains explicit",
        "occurrence remains supplied" in text
        and "fresh capacity remains supplied" in text
        and "close law remains supplied" in text
        and "typing remains supplied" in text
        and "permanence remains supplied" in text
        and "matcher remains supplied" in text
        and "calibration remains supplied" in text
        and inventory["Record_typing"] is None
        and inventory["permanence"] is None
        and inventory["clock_interval_matcher"] is None
        and inventory["calibration"] is None,
        inventory,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    dependency = cycle314_dependency_fixture()
    dependency_and_schedule_controls(dependency)
    sources = source_event_controls()
    local_result = local_fresh_cell_route_controls(dependency)
    front_result = moving_front_route_controls(dependency)
    dag_result = dag_adapter_route_controls(dependency)
    proper_cubic_controls(sources[3])
    count_and_semantic_controls(local_result, front_result, dag_result)
    deletion_fault_and_domain_controls(dependency)
    inventory_and_firewall_controls()
    check(
        "Cycle 326 closes three conditional bounded event-to-commit-candidate routes without promoting a candidate to Record or a count to time",
        local_result["candidate"].lawful_close
        and len(front_result["candidates"]) == 12
        and dag_result["candidate"].lawful_close
        and front_result["schedule_outputs"] == 1
        and dag_result["Record_node_present"] is False
        and "no axiom pressure" in normalized(NOTE),
        {
            "route_1": "closed conditionally",
            "route_2": "closed conditionally on supplied finite rail",
            "route_3": "closed conditionally through commit_candidate only",
        },
    )
    print("DATA local", local_result)
    print("DATA moving_front", front_result)
    print("DATA DAG", dag_result)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE326_EVENT_TO_COMMIT_CANDIDATE_GREEN"
        if FAIL == 0
        else "CYCLE326_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
