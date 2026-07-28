#!/usr/bin/env python3
"""Cycle-722 epoch-fed endpoint/interval and causal-order harness.

This runner supplies one explicit packet-map convention, realizes every map
read as a literal Stage-E word after the composed Cycle-721 epoch, and feeds
the landed Cycle-610 EventChain and Cycle-612 JointOrder implementations
without modifying either harness.  The decoded integers remain circuit data;
they are not identified with physical time, duration, rate, or cadence.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/EPOCH_FED_ENDPOINT_INTERVAL_HARNESS_CYCLE722_BOUNDED_THEOREM_"
    "NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle721_collision_free_epoch_composition_2026_07_28.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/frontier_cycle722_epoch_fed_endpoint_interval_harness_2026_07_28.py",
    "docs/EPOCH_FED_ENDPOINT_INTERVAL_HARNESS_CYCLE722_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from dataclasses import asdict
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from time import perf_counter

import frontier_cycle721_collision_free_epoch_composition_2026_07_28 as EPOCH
import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704


IDENTITY_SEQUENCE = tuple(range(24))
IDENTITY_POSITIONS = {2: 2, 11: 11, 23: 23}
FROZEN_INTERVALS = {
    "interval(2,11)": 9,
    "interval(11,23)": 12,
    "interval(2,23)": 21,
    "interval(11,2)": -9,
}
VARIANTS = ("primary", "alternate_port")
SHAPES = ((2, 2, 2), (3, 2, 2))


def clone_slots(slots: list[EPOCH.Slot]) -> list[EPOCH.Slot]:
    """Copy the mutable retain-after sets before extending the epoch."""
    return [
        EPOCH.Slot(
            slot.stage,
            [
                EPOCH.WordUse(
                    word.word_id,
                    word.stage,
                    word.family,
                    dict(word.accesses),
                    set(word.retain_after),
                )
                for word in slot.words
            ],
        )
        for slot in slots
    ]


def namespace_stop(bundle: EPOCH.EpochBundle) -> int:
    stops = [stop for _start, stop in bundle.namespace.ranges.values()]
    stops.extend(register + 1 for register in bundle.namespace.g_site_to_register.values())
    return max(stops)


def register_trace(
    slots: list[EPOCH.Slot], register: int
) -> list[tuple[int, EPOCH.WordUse, str, str]]:
    trace = []
    for slot_index, slot in enumerate(slots):
        for word in slot.words:
            if register in word.accesses:
                role, mode = word.accesses[register]
                trace.append((slot_index, word, role, mode))
    return trace


def retained_witness(
    bundle: EPOCH.EpochBundle,
    register: int,
    origin_stage: str,
) -> dict[str, object]:
    trace = register_trace(bundle.slots, register)
    origin_writes = [
        (slot_index, word, role, mode)
        for slot_index, word, role, mode in trace
        if word.stage == origin_stage and mode == "write"
    ]
    if not trace or not origin_writes:
        return {
            "register": register,
            "origin_stage": origin_stage,
            "valid": False,
            "reason": "missing trace or declared origin-stage write",
        }
    slot_index, owner, role, mode = trace[-1]
    origin_slot, origin, origin_role, _origin_mode = origin_writes[-1]
    return {
        "register": register,
        "origin_stage": origin_stage,
        "origin_slot": origin_slot,
        "origin_word": origin.word_id,
        "origin_family": origin.family,
        "origin_role": origin_role,
        "owner_slot": slot_index,
        "owner_stage": owner.stage,
        "owner_word": owner.word_id,
        "owner_family": owner.family,
        "owner_role": role,
        "owner_mode": mode,
        "retained_after_owner": register in owner.retain_after,
        "valid": register in owner.retain_after,
    }


def packet_sources(
    bundle: EPOCH.EpochBundle,
    *,
    verify_values: bool,
) -> tuple[list[dict[str, object]], bool]:
    """Read the five supplied packet fields from declared retained registers."""
    pump_start, pump_stop = bundle.namespace.ranges["pump_syndrome_bank"]
    if pump_stop - pump_start < 3:
        raise ValueError("epoch exposes fewer than three pump syndromes")
    pump_registers = (pump_start, pump_start + 1, pump_start + 2)

    if bundle.variant == "primary":
        bell_start, bell_stop = bundle.namespace.ranges[
            "Bell_measurement_ancillae"
        ]
        if bell_stop - bell_start < 2:
            raise ValueError("epoch exposes fewer than two Bell ancillae")
        endpoint_registers = (bell_start, bell_start + 1)
        endpoint_roles = ("Bell_measurement_ancilla_0", "Bell_measurement_ancilla_1")
        endpoint_stage = "B"
    else:
        port_bank_start = bundle.namespace.q + 6 * bundle.port
        endpoint_registers = (port_bank_start, port_bank_start + 1)
        endpoint_roles = ("declared_port_parity_0", "declared_port_parity_1")
        endpoint_stage = "B"

    declarations = (
        ("certificate", endpoint_roles[0], endpoint_registers[0], endpoint_stage),
        ("binder", endpoint_roles[1], endpoint_registers[1], endpoint_stage),
        ("actuality", "pump_syndrome_0", pump_registers[0], "A"),
        ("admissibility", "pump_syndrome_1", pump_registers[1], "A"),
        ("law_domain", "pump_syndrome_2", pump_registers[2], "A"),
    )

    width = bundle.fixture.qubits + bundle.fixture.matter_qubits
    pump_values = (
        tuple(
            int(EPOCH.M.symplectic(
                bundle.pump_corrections[index].symplectic(width),
                bundle.pump_rows[index].symplectic(width),
                width,
            ))
            for index in range(3)
        )
        if verify_values else (1, 1, 1)
    )
    if bundle.variant == "primary" and verify_values:
        endpoint_values = tuple(
            int(EPOCH.M.symplectic(
                bundle.compiled["corrections"][index].symplectic(width),
                bundle.compiled["words"][index]["row"].symplectic(width),
                width,
            ))
            for index in range(2)
        )
        semantic_certificate = {
            "kind": "private-dual Bell outcome read from bundle rows",
            "values": endpoint_values,
        }
    elif bundle.variant == "primary":
        endpoint_values = (1, 1)
        semantic_certificate = {
            "kind": "covariance key-only rebuild; values verified on source bundle",
            "values": endpoint_values,
        }
    elif verify_values:
        f2 = EPOCH.f2_stage_action_failures(bundle)
        parity_failures = int(f2["failure_fields"]["parity_failures"])
        endpoint_values = (int(parity_failures == 0),) * 2
        semantic_certificate = {
            "kind": "declared port-parity carrier with unchanged F2 parity certificate",
            "parity_failures": parity_failures,
            "values": endpoint_values,
        }
    else:
        endpoint_values = (1, 1)
        semantic_certificate = {
            "kind": "covariance key-only rebuild; values verified on source bundle",
            "values": endpoint_values,
        }

    values = (*endpoint_values, *pump_values)
    sources = []
    for (field, register_role, register, origin_stage), value in zip(
        declarations, values
    ):
        witness = (
            retained_witness(bundle, register, origin_stage)
            if verify_values
            else {
                "register": register,
                "origin_stage": origin_stage,
                "valid": True,
                "kind": "covariance key-only rebuild",
            }
        )
        sources.append({
            "field": field,
            "register_role": register_role,
            "register": register,
            "value": int(value),
            "retained_witness": witness,
        })
    clean = (
        all(source["value"] == 1 for source in sources)
        and all(source["retained_witness"]["valid"] for source in sources)
    )
    for source in sources[:2]:
        source["semantic_certificate"] = semantic_certificate
    return sources, clean


def stage_e_key_multiset(
    slots: list[EPOCH.Slot],
) -> Counter[tuple[object, ...]]:
    keys: Counter[tuple[object, ...]] = Counter()
    for slot in slots:
        if slot.stage != "E":
            continue
        for word in slot.words:
            identity = int(word.word_id.rsplit(":", 1)[-1])
            access_surface = tuple(sorted(
                (role, mode) for role, mode in word.accesses.values()
            ))
            keys[(slot.stage, word.family, identity, access_surface)] += 1
    return keys


def key_digest(keys: Counter[tuple[object, ...]]) -> str:
    return sha256(repr(sorted(keys.items())).encode()).hexdigest()


def build_stage_e(
    bundle: EPOCH.EpochBundle,
    *,
    verify_values: bool,
) -> tuple[list[EPOCH.Slot], list[dict[str, object]], list[dict[str, object]], bool]:
    sources, sources_clean = packet_sources(bundle, verify_values=verify_values)
    slots = clone_slots(bundle.slots)
    record_start = namespace_stop(bundle)
    table = []
    for position, identity in enumerate(IDENTITY_SEQUENCE):
        record_register = record_start + position
        accesses = {
            int(source["register"]): (str(source["field"]), "read")
            for source in sources
        }
        accesses[record_register] = ("packet_record", "write")
        word_id = f"E:epoch_packet:{identity}"
        slots.append(EPOCH.Slot("E", [EPOCH.WordUse(
            word_id,
            f"E:{position:02d}",
            f"epoch_packet_{bundle.variant}",
            accesses,
        )]))
        table.append({
            "opportunity_position_zero_based": position,
            "tick_identity": identity,
            "orientation": 1,
            "certificate": int(sources[0]["value"]),
            "binder": int(sources[1]["value"]),
            "actuality": int(sources[2]["value"]),
            "admissibility": int(sources[3]["value"]),
            "law_domain": int(sources[4]["value"]),
            "source_registers": {
                str(source["field"]): {
                    "register": int(source["register"]),
                    "register_role": source["register_role"],
                }
                for source in sources
            },
            "packet_record_register": record_register,
            "stage_e_word": word_id,
        })
    return slots, table, sources, sources_clean


def extend_and_walk(bundle: EPOCH.EpochBundle) -> dict[str, object]:
    slots, table, sources, sources_clean = build_stage_e(
        bundle, verify_values=True
    )
    handoffs = EPOCH.declare_handoffs(slots)
    walk = EPOCH.liveness_walk(slots, handoffs)
    e_word_ids = {
        word.word_id
        for slot in slots if slot.stage == "E"
        for word in slot.words
    }
    e_handoffs = {
        edge for edge in handoffs if edge[1] in e_word_ids
    }
    e_keys = stage_e_key_multiset(slots)
    lawful = (
        sources_clean
        and walk["collision_count"] == 0
        and walk["violation_count"] == 0
        and walk["handoffs_declared"] == walk["handoffs_consumed"]
        and len(e_handoffs) == 5 * len(IDENTITY_SEQUENCE)
    )
    return {
        "slots": slots,
        "handoffs": handoffs,
        "walk": walk,
        "table": table,
        "sources": sources,
        "sources_clean": sources_clean,
        "e_handoffs": e_handoffs,
        "e_key_multiset": e_keys,
        "lawful": lawful,
    }


def interval_quadruple(chain: object) -> dict[str, int | None]:
    return {
        "interval(2,11)": chain.interval(2, 11),
        "interval(11,23)": chain.interval(11, 23),
        "interval(2,23)": chain.interval(2, 23),
        "interval(11,2)": chain.interval(11, 2),
    }


def feed_unchanged_chain(table: list[dict[str, object]]) -> dict[str, object]:
    chain = C704.C610.EventChain(bank=24)
    statuses = []
    rotor_failures = 0
    predecessor_failures = 0
    expected_rotor = 14
    expected_predecessor = None
    expected_rows = []
    for row in table:
        status = chain.admit(
            tick_id=int(row["tick_identity"]),
            orientation=int(row["orientation"]),
            certificate=int(row["certificate"]),
            binder=int(row["binder"]),
            actuality=int(row["actuality"]),
            admissibility=int(row["admissibility"]),
            law_domain=int(row["law_domain"]),
        )
        statuses.append(status)
        expected_rotor = (expected_rotor + 1) % 16
        expected_rows.append({
            "identity": int(row["tick_identity"]),
            "rotor": expected_rotor,
            "carry": int(expected_rotor == 0),
            "predecessor": expected_predecessor,
        })
        expected_predecessor = int(row["tick_identity"])
        if status == "admitted":
            observed = chain.cells[-1]
            rotor_failures += (
                observed.rotor != expected_rotor
                or observed.carry != int(expected_rotor == 0)
            )
            predecessor_failures += observed.predecessor != expected_rows[-1][
                "predecessor"
            ]
        else:
            rotor_failures += 1
            predecessor_failures += 1
    observed_rows = [asdict(cell) for cell in chain.cells]
    return {
        "statuses": statuses,
        "all_admitted": statuses == ["admitted"] * len(table),
        "rotor_seed": 14,
        "first_rotor": observed_rows[0]["rotor"] if observed_rows else None,
        "rotor_failures": rotor_failures,
        "predecessor_failures": predecessor_failures,
        "expected_rotor_carry_predecessor": expected_rows,
        "observed_cells": observed_rows,
        "intervals": interval_quadruple(chain),
        "pass": (
            statuses == ["admitted"] * 24
            and len(observed_rows) == 24
            and observed_rows[0]["rotor"] == 15
            and rotor_failures == 0
            and predecessor_failures == 0
            and interval_quadruple(chain) == FROZEN_INTERVALS
        ),
    }


def unchanged_joint_order() -> tuple[dict[str, object], bool]:
    joint = C704.joint_order_controls()
    expected = {
        "consistent_statuses": ("admitted", "admitted"),
        "consistent_acyclic": True,
        "inverted_first": "admitted",
        "inverted_refusal": "refused_inverted",
        "forced_cycle_detected": True,
        "no_endpoint_status": "no_opportunity",
    }
    passed = (
        all(joint[key] == value for key, value in expected.items())
        and joint["JointOrder_class_module"] == C704.C612.JointOrder.__module__
    )
    return joint, passed


def sha_pin_certificate() -> dict[str, object]:
    cycle610 = sha256(Path(C704.C610.__file__).read_bytes()).hexdigest()
    cycle612 = sha256(Path(C704.C612.__file__).read_bytes()).hexdigest()
    return {
        "Cycle610": {
            "path": str(Path(C704.C610.__file__).resolve()),
            "observed": cycle610,
            "expected_from_C704": C704.C610_SHA256,
            "pass": cycle610 == C704.C610_SHA256,
        },
        "Cycle612": {
            "path": str(Path(C704.C612.__file__).resolve()),
            "observed": cycle612,
            "expected_from_C704": C704.C612_SHA256,
            "pass": cycle612 == C704.C612_SHA256,
        },
        "pass": (
            cycle610 == C704.C610_SHA256
            and cycle612 == C704.C612_SHA256
        ),
    }


def deleted_handoff_control(extension: dict[str, object]) -> dict[str, object]:
    first_word = extension["table"][0]["stage_e_word"]
    actuality_register = extension["table"][0]["source_registers"][
        "actuality"
    ]["register"]
    candidates = sorted(
        edge for edge in extension["e_handoffs"]
        if edge[1] == first_word and edge[2] == actuality_register
    )
    if len(candidates) != 1:
        return {
            "detected": False,
            "reason": "unique first-E actuality handoff not found",
            "candidates": candidates,
        }
    deleted = candidates[0]
    damaged_handoffs = set(extension["handoffs"])
    damaged_handoffs.remove(deleted)
    damaged = EPOCH.liveness_walk(extension["slots"], damaged_handoffs)
    needle = (
        f"handoff_read_without_edge:slot="
    )
    named = [
        violation for violation in damaged["violations"]
        if needle in violation
        and f"register={deleted[2]}" in violation
        and f"{deleted[0]}->{deleted[1]}" in violation
    ]
    return {
        "deleted_handoff": deleted,
        "named_violation": named[0] if named else None,
        "violation_count": damaged["violation_count"],
        "detected": bool(named),
    }


def admission_controls(
    table: list[dict[str, object]],
    baseline_joint: dict[str, object],
) -> dict[str, object]:
    flipped = [dict(row) for row in table]
    flip_position = IDENTITY_POSITIONS[11]
    flipped[flip_position] = dict(flipped[flip_position])
    flipped[flip_position]["actuality"] = 0
    flip_chain = C704.C610.EventChain(bank=24)
    flip_statuses = []
    for row in flipped:
        flip_statuses.append(flip_chain.admit(
            tick_id=int(row["tick_identity"]),
            orientation=int(row["orientation"]),
            certificate=int(row["certificate"]),
            binder=int(row["binder"]),
            actuality=int(row["actuality"]),
            admissibility=int(row["admissibility"]),
            law_domain=int(row["law_domain"]),
        ))
    degraded = interval_quadruple(flip_chain)

    full_chain = C704.C610.EventChain(bank=24)
    for row in table:
        full_chain.admit(
            tick_id=int(row["tick_identity"]),
            orientation=int(row["orientation"]),
            certificate=int(row["certificate"]),
            binder=int(row["binder"]),
            actuality=int(row["actuality"]),
            admissibility=int(row["admissibility"]),
            law_domain=int(row["law_domain"]),
        )
    exhausted = full_chain.admit(
        tick_id=24,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )

    hostile_identities = list(IDENTITY_SEQUENCE)
    hostile_identities[11], hostile_identities[23] = (
        hostile_identities[23],
        hostile_identities[11],
    )
    hostile_chain = C704.C610.EventChain(bank=24)
    hostile_statuses = [
        hostile_chain.admit(
            tick_id=identity,
            orientation=1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        for identity in hostile_identities
    ]
    hostile_intervals = interval_quadruple(hostile_chain)
    hostile_joint = C704.joint_order_controls()

    return {
        "actuality_flip": {
            "identity": 11,
            "position_zero_based": flip_position,
            "status": flip_statuses[flip_position],
            "interval_degradation": degraded,
            "frozen_quadruple_complete": degraded == FROZEN_INTERVALS,
            "detected": (
                flip_statuses[flip_position] == "refused_supplied"
                and degraded == {
                    "interval(2,11)": None,
                    "interval(11,23)": None,
                    "interval(2,23)": 20,
                    "interval(11,2)": None,
                }
            ),
        },
        "twenty_fifth_admission": {
            "identity": 24,
            "status": exhausted,
            "detected": exhausted == "exhausted",
        },
        "hostile_order": {
            "identity_sequence": hostile_identities,
            "statuses": hostile_statuses,
            "intervals": hostile_intervals,
            "joint_order_outcomes": hostile_joint,
            "joint_order_unchanged": hostile_joint == baseline_joint,
            "detected": (
                hostile_statuses == ["admitted"] * 24
                and hostile_intervals != FROZEN_INTERVALS
                and hostile_joint == baseline_joint
            ),
        },
    }


def assignment_targets(node: ast.AST) -> list[ast.AST]:
    if isinstance(node, (ast.Tuple, ast.List)):
        output = []
        for element in node.elts:
            output.extend(assignment_targets(element))
        return output
    return [node]


def attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, ast.Attribute):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def module_identity_tripwire() -> dict[str, object]:
    source = Path(__file__).read_text()
    tree = ast.parse(source, filename=__file__)
    imported_aliases = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_aliases.update(
                alias.asname or alias.name.split(".")[0] for alias in node.names
            )
        elif isinstance(node, ast.ImportFrom):
            imported_aliases.update(
                alias.asname or alias.name for alias in node.names
            )

    forbidden_classes = [
        node.name for node in ast.walk(tree)
        if isinstance(node, (ast.ClassDef, ast.AsyncFunctionDef))
        and node.name in ("JointOrder", "EventChain")
    ]
    attribute_assignments = []
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets = [
                target
                for raw in node.targets
                for target in assignment_targets(raw)
            ]
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets = assignment_targets(node.target)
        for target in targets:
            if (
                isinstance(target, ast.Attribute)
                and attribute_root(target) in imported_aliases
            ):
                attribute_assignments.append({
                    "line": target.lineno,
                    "root": attribute_root(target),
                    "attribute": target.attr,
                })
    setattr_calls = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "setattr"
            and node.args
            and attribute_root(node.args[0]) in imported_aliases
        ):
            setattr_calls.append(node.lineno)
    return {
        "forbidden_class_definitions": forbidden_classes,
        "imported_module_attribute_assignments": attribute_assignments,
        "setattr_calls_on_imports": setattr_calls,
        "EventChain_class_module": C704.C610.EventChain.__module__,
        "JointOrder_class_module": C704.C612.JointOrder.__module__,
        "detected": (
            not forbidden_classes
            and not attribute_assignments
            and not setattr_calls
        ),
    }


def covariance_certificate(
    atlas: dict[str, object],
    source_bundles: dict[str, EPOCH.EpochBundle],
    source_extensions: dict[str, dict[str, object]],
) -> dict[str, object]:
    frames = EPOCH.PORT.proper_cubic_frames()
    shifts = tuple(product((0, 1), repeat=3))
    source_keys = {
        variant: source_extensions[variant]["e_key_multiset"]
        for variant in VARIANTS
    }
    failures = Counter({variant: 0 for variant in VARIANTS})
    first_failures: dict[str, object] = {}
    transported_root_failures = 0
    transported_port_failures = 0
    contexts = 0

    source = source_bundles["primary"]
    for frame_index, frame in enumerate(frames):
        for shift in shifts:
            contexts += 1
            cells = EPOCH.Q.affine_cells(source.fixture.cells, frame, shift)
            root = EPOCH.affine_coord(source.root, frame, shift)
            port_cell = EPOCH.affine_coord(
                source.fixture.cells[source.port], frame, shift
            )
            axis_order = EPOCH.mapped_axis_order(frame, source.axis_order)
            primary = EPOCH.build_epoch(
                (2, 2, 2),
                "primary",
                atlas,
                cells=cells,
                root=root,
                axis_order=axis_order,
                port_cell=port_cell,
                declare_edges=False,
            )
            alternate = EPOCH.build_epoch(
                (2, 2, 2),
                "alternate_port",
                atlas,
                cells=cells,
                root=root,
                axis_order=axis_order,
                port_cell=port_cell,
                recurrent_override=primary.recurrent,
                declare_edges=False,
            )
            rebuilt = {"primary": primary, "alternate_port": alternate}
            for variant in VARIANTS:
                target = rebuilt[variant]
                slots, _table, _sources, _clean = build_stage_e(
                    target, verify_values=False
                )
                observed = stage_e_key_multiset(slots)
                if observed != source_keys[variant]:
                    failures[variant] += 1
                    if variant not in first_failures:
                        first_failures[variant] = {
                            "frame_index": frame_index,
                            "frame": frame.tolist(),
                            "shift": shift,
                            "missing": tuple(
                                (source_keys[variant] - observed).items()
                            )[:3],
                            "excess": tuple(
                                (observed - source_keys[variant]).items()
                            )[:3],
                        }
                transported_root_failures += target.root != root
                transported_port_failures += (
                    target.fixture.cells[target.port] != port_cell
                )

    return {
        "proper_cubic_frames": len(frames),
        "translation_parities": len(shifts),
        "contexts": contexts,
        "variants": {
            variant: {
                "source_E_key_count": sum(source_keys[variant].values()),
                "source_E_key_digest": key_digest(source_keys[variant]),
                "E_key_multiset_failures": failures[variant],
            }
            for variant in VARIANTS
        },
        "transported_root_failures": transported_root_failures,
        "transported_port_failures": transported_port_failures,
        "first_failures": first_failures,
        "pass": (
            len(frames) == 24
            and len(shifts) == 8
            and contexts == 24 * 8
            and not any(failures.values())
            and transported_root_failures == 0
            and transported_port_failures == 0
        ),
    }


def main() -> int:
    started = perf_counter()
    checks: list[dict[str, object]] = []

    def check(label: str, condition: bool, detail: object = "") -> bool:
        passed = bool(condition)
        checks.append({"label": label, "pass": passed, "detail": detail})
        print("PASS" if passed else "FAIL", label, "::", detail)
        return passed

    atlas = EPOCH.P.build_private_atlases()
    bundles: dict[str, dict[str, EPOCH.EpochBundle]] = {}
    extensions: dict[str, dict[str, dict[str, object]]] = {}
    feeds: dict[str, dict[str, dict[str, object]]] = {}
    boxes: dict[str, object] = {}
    for shape in SHAPES:
        shape_key = "x".join(map(str, shape))
        primary = EPOCH.build_epoch(shape, "primary", atlas)
        alternate = EPOCH.build_epoch(
            shape,
            "alternate_port",
            atlas,
            recurrent_override=primary.recurrent,
        )
        bundles[shape_key] = {
            "primary": primary,
            "alternate_port": alternate,
        }
        extensions[shape_key] = {}
        feeds[shape_key] = {}
        boxes[shape_key] = {}
        for variant in VARIANTS:
            extension = extend_and_walk(bundles[shape_key][variant])
            feed = feed_unchanged_chain(extension["table"])
            extensions[shape_key][variant] = extension
            feeds[shape_key][variant] = feed
            walk = extension["walk"]
            boxes[shape_key][variant] = {
                "shape": list(shape),
                "variant": variant,
                "base_slots": len(bundles[shape_key][variant].slots),
                "extended_slots": walk["slots_walked"],
                "extended_words": walk["words_walked"],
                "register_touches": walk["register_touches"],
                "registers_seen": walk["registers_seen"],
                "handoffs_declared": walk["handoffs_declared"],
                "handoffs_consumed": walk["handoffs_consumed"],
                "E_handoffs_declared_and_consumed": len(
                    extension["e_handoffs"]
                ),
                "collision_count": walk["collision_count"],
                "violation_count": walk["violation_count"],
                "final_state_census": walk["final_state_census"],
                "packet_register_start": extension["table"][0][
                    "packet_record_register"
                ],
                "packet_register_stop": extension["table"][-1][
                    "packet_record_register"
                ] + 1,
                "source_registers_clean_and_retained": extension[
                    "sources_clean"
                ],
                "lawful": extension["lawful"],
            }

    liveness_gate = all(
        extensions[shape][variant]["lawful"]
        for shape in extensions for variant in VARIANTS
    )
    feed_gate = all(
        feeds[shape][variant]["pass"]
        for shape in feeds for variant in VARIANTS
    )
    check(
        "both variants have collision-free extended Stage-E schedules with every E handoff consumed on 2x2x2 and 3x2x2",
        liveness_gate,
        {
            shape: {
                variant: {
                    "collisions": boxes[shape][variant]["collision_count"],
                    "violations": boxes[shape][variant]["violation_count"],
                    "E_handoffs": boxes[shape][variant][
                        "E_handoffs_declared_and_consumed"
                    ],
                }
                for variant in VARIANTS
            }
            for shape in boxes
        },
    )
    check(
        "every epoch-fed opportunity is admitted by unchanged Cycle610 with independent rotor/carry arithmetic and the frozen interval quadruple",
        feed_gate,
        {
            shape: {
                variant: feeds[shape][variant]["intervals"]
                for variant in VARIANTS
            }
            for shape in feeds
        },
    )

    joint, joint_gate = unchanged_joint_order()
    check(
        "unchanged Cycle612 returns the six frozen causal-order outcomes and its landed class module",
        joint_gate,
        joint,
    )

    sha_pins = sha_pin_certificate()
    check(
        "the on-disk Cycle610 and Cycle612 harnesses equal C704's SHA pins",
        sha_pins["pass"],
        {
            name: row["observed"]
            for name, row in sha_pins.items() if isinstance(row, dict)
        },
    )

    base_extension = extensions["2x2x2"]["primary"]
    deleted = deleted_handoff_control(base_extension)
    admission = admission_controls(base_extension["table"], joint)
    tripwire = module_identity_tripwire()
    controls = {
        "deleted_E_handoff": deleted,
        **admission,
        "module_identity_tripwire": tripwire,
    }
    controls_gate = (
        deleted["detected"]
        and admission["actuality_flip"]["detected"]
        and admission["twenty_fifth_admission"]["detected"]
        and admission["hostile_order"]["detected"]
        and tripwire["detected"]
    )
    check(
        "deleted handoff, flipped actuality, 25th admission, hostile order, and module-identity tripwire controls are all detected",
        controls_gate,
        {
            "deleted_E_handoff": deleted["detected"],
            "actuality_flip": admission["actuality_flip"]["detected"],
            "twenty_fifth_admission": admission[
                "twenty_fifth_admission"
            ]["detected"],
            "hostile_order": admission["hostile_order"]["detected"],
            "module_identity_tripwire": tripwire["detected"],
        },
    )

    source_bundles = bundles["2x2x2"]
    source_extensions = extensions["2x2x2"]
    covariance = covariance_certificate(
        atlas, source_bundles, source_extensions
    )
    check(
        "Stage-E geometry-free key multisets are invariant over 24 proper cubic frames x 8 translation parities for both variants",
        covariance["pass"],
        {
            "contexts": covariance["contexts"],
            "failures": {
                variant: covariance["variants"][variant][
                    "E_key_multiset_failures"
                ]
                for variant in VARIANTS
            },
        },
    )

    fixtures = EPOCH.fixture_certificate()
    check(
        "the unchanged mass/contact and Cycle-230 fixture residuals remain below 4e-10",
        fixtures["pass"],
        fixtures,
    )

    packet_map = {
        "convention": (
            "Supplied packet map: zero-based opportunities use ascending "
            "identities 0..23 and orientation +1. Certificate/binder use "
            "two retained Bell ancillae for primary or two declared retained "
            "port-parity carriers for alternate_port; the other three bits "
            "use retained Stage-A pump syndromes."
        ),
        "identity_sequence": list(IDENTITY_SEQUENCE),
        "declared_identity_positions_zero_based": {
            str(identity): position
            for identity, position in IDENTITY_POSITIONS.items()
        },
        "variants": {
            variant: {
                "source_register_declarations": source_extensions[variant][
                    "sources"
                ],
                "table": source_extensions[variant]["table"],
            }
            for variant in VARIANTS
        },
    }
    interval_projection = {
        "frozen": FROZEN_INTERVALS,
        "by_box_variant": {
            shape: {
                variant: {
                    "intervals": feeds[shape][variant]["intervals"],
                    "all_admitted": feeds[shape][variant]["all_admitted"],
                    "rotor_seed": feeds[shape][variant]["rotor_seed"],
                    "first_rotor": feeds[shape][variant]["first_rotor"],
                    "rotor_failures": feeds[shape][variant]["rotor_failures"],
                    "predecessor_failures": feeds[shape][variant][
                        "predecessor_failures"
                    ],
                }
                for variant in VARIANTS
            }
            for shape in feeds
        },
    }

    requirements_3_to_8 = (
        feed_gate
        and joint_gate
        and sha_pins["pass"]
        and liveness_gate
        and controls_gate
        and covariance["pass"]
    )
    passing = all(row["pass"] for row in checks)
    runtime_seconds = perf_counter() - started
    claim_boundary = [
        (
            "The packet map is a supplied convention: which epoch registers "
            "feed which admission bits is declared, not derived. No autonomous "
            "packet map, occurrence rule, or admission law is claimed."
        ),
        (
            "Decoded intervals are circuit data; nothing here is physical "
            "time, duration, rate, or cadence."
        ),
        (
            "\"Coherent source-lift tournament\" is an undefined forward "
            "reference in the Cycle-720 verdict and is not attempted here. "
            "C_source is unchanged: there is no energy/stress/resource source, "
            "reciprocal response, sign/scale law, or gravity identification."
        ),
        (
            "No refit is performed: every imported fixture and harness "
            "constant is consumed unchanged."
        ),
    ]
    report = {
        "status": "PASS" if passing else "FAIL",
        "checks": checks,
        "packet_map": packet_map,
        "boxes": boxes,
        "variants": list(VARIANTS),
        "interval_projection": interval_projection,
        "unchanged_Cycle612": joint,
        "sha_pins": sha_pins,
        "covariance": covariance,
        "controls": controls,
        "fixtures": fixtures,
        "derived": [
            "literal Stage-E WordUse reads and one fresh retained packet register per opportunity",
            "extended clean/live/retained liveness walks and explicit handoff consumption",
            "unchanged Cycle610 admission, rotor/carry recomputation, predecessor checks, and interval projection",
            "unchanged Cycle612 frozen causal-order outcomes",
            "Stage-E key covariance over the transported epoch",
        ],
        "supplied": [
            "ascending identity sequence 0..23 with identities 2, 11, and 23 at zero-based positions 2, 11, and 23",
            "orientation +1 and the declared packet-map register roles",
            "the endpoint opportunity, occurrence/admission/domain interpretation, finite bank, epoch root, port, and input variant",
        ],
        "open": [
            "autonomous packet mapping, occurrence, admission, law-domain, or identity selection",
            "physical time, duration, rate, cadence, Record permanence, or empirical unit",
            "coherent source lift, C_source dynamics, reciprocal response, gravity, or continuum interpretation",
        ],
        "claim_boundary": claim_boundary,
        "epoch_fed_interval_harness": bool(requirements_3_to_8),
        "harness_modified": False,
        "autonomous_packet_map": False,
        "physical_time_identified": False,
        "source_lift_attempted": False,
        "runtime_seconds": runtime_seconds,
        "authority": "none",
        "audit": "unset",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
