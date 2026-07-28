#!/usr/bin/env python3
"""Independent checker for the companion-bank packet projection.

The primary runner is parsed only as source data and blocklisted from import.
This checker independently rebuilds the selected parent bundles and static
field predicates, traces the selected registers through the parent liveness
table, and reconstructs admission, rotor/carry, and interval semantics.  It
does not reinterpret those predicates as simulated register-state values.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_"
    "PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py",
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "docs/COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
CYCLE610_PATH = AUDIT_INPUT_PATHS[3]
CYCLE612_PATH = AUDIT_INPUT_PATHS[4]

TOP_LEVEL_BLOCKLIST = {
    "frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28"
}

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704
import frontier_companion_bank_epoch_liveness_2026_07_28 as EPOCH


_BLOCKED_AFTER_IMPORTS = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
assert not _BLOCKED_AFTER_IMPORTS, (
    f"primary projection runner imported transitively: {_BLOCKED_AFTER_IMPORTS}"
)

FROZEN_INTERVALS = {
    "interval(2,11)": 9,
    "interval(11,23)": 12,
    "interval(2,23)": 21,
    "interval(11,2)": -9,
}
DEGRADED_INTERVALS = {
    "interval(2,11)": None,
    "interval(11,23)": None,
    "interval(2,23)": 20,
    "interval(11,2)": None,
}
CHECKS: list[dict[str, object]] = []


def check(label: str, condition: bool, detail: object = "") -> None:
    """Emit the Cycle-721-style line and retain its report row."""
    passed = bool(condition)
    CHECKS.append({"label": label, "pass": passed, "detail": detail})
    print("PASS" if passed else "FAIL", label)


def module_assignment(tree: ast.Module, name: str) -> ast.AST:
    """Return a named module-level assignment value without executing it."""
    matches: list[ast.AST] = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            if node.value is not None:
                matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(f"expected one module assignment for {name}, found {len(matches)}")
    return matches[0]


def literal_identity_sequence(node: ast.AST) -> tuple[int, ...]:
    """Evaluate only a literal tuple/list or the exact tuple(range(...)) form."""
    try:
        value = ast.literal_eval(node)
    except (ValueError, TypeError):
        value = None
    if isinstance(value, (tuple, list)) and all(
        isinstance(item, int) and not isinstance(item, bool) for item in value
    ):
        return tuple(value)

    if not (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "tuple"
        and len(node.args) == 1
        and not node.keywords
    ):
        raise ValueError("IDENTITY_SEQUENCE is not a supported literal form")
    range_call = node.args[0]
    if not (
        isinstance(range_call, ast.Call)
        and isinstance(range_call.func, ast.Name)
        and range_call.func.id == "range"
        and 1 <= len(range_call.args) <= 3
        and not range_call.keywords
    ):
        raise ValueError("IDENTITY_SEQUENCE is not tuple(range(literal integers))")
    bounds = tuple(ast.literal_eval(argument) for argument in range_call.args)
    if not all(
        isinstance(bound, int) and not isinstance(bound, bool) for bound in bounds
    ):
        raise ValueError("range bounds are not literal integers")
    return tuple(range(*bounds))


def assignment_values(function: ast.FunctionDef, name: str) -> list[ast.AST]:
    values: list[ast.AST] = []
    for node in ast.walk(function):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            if node.value is not None:
                values.append(node.value)
    return values


def extract_declared_register_roles(tree: ast.Module) -> tuple[dict[str, object], ...]:
    functions = [
        node for node in tree.body
        if (
            isinstance(node, ast.FunctionDef)
            and node.name == "packet_field_certificates"
        )
    ]
    if len(functions) != 1:
        raise ValueError("expected one packet_field_certificates function")
    function = functions[0]

    endpoint_role_values = assignment_values(function, "endpoint_roles")
    endpoint_roles = []
    for value in endpoint_role_values:
        literal = ast.literal_eval(value)
        if not (
            isinstance(literal, tuple)
            and len(literal) == 2
            and all(isinstance(role, str) for role in literal)
        ):
            raise ValueError("endpoint_roles is not a literal string pair")
        if literal not in endpoint_roles:
            endpoint_roles.append(literal)
    if len(endpoint_roles) != 2:
        raise ValueError(f"expected two endpoint role variants, found {len(endpoint_roles)}")

    endpoint_stage_values = assignment_values(function, "endpoint_stage")
    endpoint_stages = []
    for value in endpoint_stage_values:
        literal = ast.literal_eval(value)
        if not isinstance(literal, str):
            raise ValueError("endpoint_stage is not literal text")
        if literal not in endpoint_stages:
            endpoint_stages.append(literal)
    if endpoint_stages != ["B"]:
        raise ValueError(f"endpoint_stage does not resolve uniquely to B: {endpoint_stages}")

    declaration_values = assignment_values(function, "declarations")
    if len(declaration_values) != 1 or not isinstance(
        declaration_values[0], (ast.Tuple, ast.List)
    ):
        raise ValueError("declarations is not one literal row table")

    rows: list[dict[str, object]] = []
    for row in declaration_values[0].elts:
        if not isinstance(row, (ast.Tuple, ast.List)) or len(row.elts) != 4:
            raise ValueError("malformed declaration row")
        field = ast.literal_eval(row.elts[0])
        role_node = row.elts[1]
        if isinstance(role_node, ast.Constant) and isinstance(role_node.value, str):
            roles = (role_node.value,)
        elif (
            isinstance(role_node, ast.Subscript)
            and isinstance(role_node.value, ast.Name)
            and role_node.value.id == "endpoint_roles"
        ):
            index = ast.literal_eval(role_node.slice)
            if not isinstance(index, int) or isinstance(index, bool):
                raise ValueError("endpoint role index is not a literal integer")
            roles = tuple(variant[index] for variant in endpoint_roles)
        else:
            raise ValueError(f"unsupported register role expression: {ast.dump(role_node)}")
        stage_node = row.elts[3]
        if isinstance(stage_node, ast.Constant) and isinstance(
            stage_node.value, str
        ):
            origin_stage = stage_node.value
        elif isinstance(stage_node, ast.Name) and stage_node.id == "endpoint_stage":
            origin_stage = endpoint_stages[0]
        else:
            raise ValueError(
                f"unsupported origin stage expression: {ast.dump(stage_node)}"
            )
        if not isinstance(field, str) or not isinstance(origin_stage, str):
            raise ValueError("declaration field/stage is not literal text")
        rows.append({
            "field": field,
            "register_roles": roles,
            "register_expression": ast.unparse(row.elts[2]),
            "origin_stage": origin_stage,
        })
    return tuple(rows)


def parse_primary() -> tuple[str, ast.Module]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    return source, ast.parse(source, filename=PRIMARY_PATH)


def packet_map_extraction() -> dict[str, object]:
    _source, tree = parse_primary()
    identities = literal_identity_sequence(
        module_assignment(tree, "IDENTITY_SEQUENCE")
    )
    identity_positions = ast.literal_eval(
        module_assignment(tree, "IDENTITY_POSITIONS")
    )
    if not isinstance(identity_positions, dict):
        raise ValueError("IDENTITY_POSITIONS is not a literal dictionary")
    declarations = extract_declared_register_roles(tree)
    table = (
        ("identity_sequence", identities),
        ("identity_positions", tuple(sorted(identity_positions.items()))),
        (
            "declared_register_roles",
            tuple(
                (
                    row["field"],
                    row["register_roles"],
                    row["register_expression"],
                    row["origin_stage"],
                )
                for row in declarations
            ),
        ),
    )
    digest = sha256(repr(table).encode()).hexdigest()
    ascending = all(left < right for left, right in zip(identities, identities[1:]))
    anchors_present = {2, 11, 23}.issubset(identities)
    positions_match = all(
        identity in identities
        and identities.index(identity) == position
        for identity, position in identity_positions.items()
    )
    fields = tuple(row["field"] for row in declarations)
    passed = (
        ascending
        and anchors_present
        and len(identities) == 24
        and len(set(identities)) == 24
        and positions_match
        and fields
        == (
            "certificate",
            "binder",
            "actuality",
            "admissibility",
            "law_domain",
        )
    )
    return {
        "pass": passed,
        "identity_sequence": identities,
        "identity_positions": identity_positions,
        "identities_strictly_ascending": ascending,
        "required_identities_present": anchors_present,
        "opportunities": len(identities),
        "declared_register_roles": declarations,
        "table_sha256": digest,
    }


def independent_liveness_trace(
    bundle: EPOCH.EpochBundle,
    register: int,
    origin_stage: str,
) -> dict[str, object]:
    """Rebuild the selected register's parent-schedule trace."""
    trace = []
    for slot_index, slot in enumerate(bundle.slots):
        for word in slot.words:
            if register not in word.accesses:
                continue
            role, mode = word.accesses[register]
            trace.append({
                "slot": slot_index,
                "stage": word.stage,
                "word": word.word_id,
                "family": word.family,
                "role": role,
                "mode": mode,
                "retained_after": register in word.retain_after,
            })
    origin_writes = [
        row for row in trace
        if row["stage"] == origin_stage and row["mode"] == "write"
    ]
    owner = trace[-1] if trace else None
    return {
        "register": register,
        "origin_stage": origin_stage,
        "trace_length": len(trace),
        "origin_write_count": len(origin_writes),
        "origin_word": origin_writes[-1]["word"] if origin_writes else None,
        "final_owner": owner,
        "pass": bool(
            origin_writes
            and owner is not None
            and owner["retained_after"]
        ),
    }


def independent_parent_field_certificates() -> dict[str, object]:
    """Recompute the five predicates without importing the primary runner."""
    atlas = EPOCH.P.build_private_atlases()
    rows: dict[str, object] = {}
    passing = True
    for shape in ((2, 2, 2), (3, 2, 2)):
        shape_key = "x".join(map(str, shape))
        primary = EPOCH.build_epoch(shape, "primary", atlas)
        alternate = EPOCH.build_epoch(
            shape,
            "alternate_port",
            atlas,
            recurrent_override=primary.recurrent,
        )
        rows[shape_key] = {}
        for variant, bundle in (
            ("primary", primary),
            ("alternate_port", alternate),
        ):
            width = bundle.fixture.qubits + bundle.fixture.matter_qubits
            pump_start, pump_stop = bundle.namespace.ranges[
                "pump_syndrome_bank"
            ]
            pump_registers = (pump_start, pump_start + 1, pump_start + 2)
            pump_values = tuple(
                int(EPOCH.M.symplectic(
                    bundle.pump_corrections[index].symplectic(width),
                    bundle.pump_rows[index].symplectic(width),
                    width,
                ))
                for index in range(3)
            )

            if variant == "primary":
                endpoint_start, endpoint_stop = bundle.namespace.ranges[
                    "Bell_measurement_ancillae"
                ]
                endpoint_registers = (
                    endpoint_start,
                    endpoint_start + 1,
                )
                endpoint_values = tuple(
                    int(EPOCH.M.symplectic(
                        bundle.compiled["corrections"][index].symplectic(
                            width
                        ),
                        bundle.compiled["words"][index]["row"].symplectic(
                            width
                        ),
                        width,
                    ))
                    for index in range(2)
                )
                endpoint_predicate = {
                    "kind": "static private-dual/row pairing",
                    "range_size": endpoint_stop - endpoint_start,
                }
            else:
                endpoint_start = bundle.namespace.q + 6 * bundle.port
                endpoint_registers = (
                    endpoint_start,
                    endpoint_start + 1,
                )
                parity_failures = int(
                    EPOCH.f2_stage_action_failures(bundle)[
                        "failure_fields"
                    ]["parity_failures"]
                )
                endpoint_values = (int(parity_failures == 0),) * 2
                endpoint_predicate = {
                    "kind": "static absence-of-port-parity-failure predicate",
                    "parity_failures": parity_failures,
                }

            registers = (*endpoint_registers, *pump_registers)
            stages = ("B", "B", "A", "A", "A")
            values = (*endpoint_values, *pump_values)
            traces = tuple(
                independent_liveness_trace(bundle, register, stage)
                for register, stage in zip(registers, stages)
            )
            walk = EPOCH.liveness_walk(bundle.slots, bundle.handoffs)
            row_pass = (
                pump_stop - pump_start >= 3
                and values == (1, 1, 1, 1, 1)
                and all(trace["pass"] for trace in traces)
                and walk["collision_count"] == 0
                and walk["violation_count"] == 0
                and walk["handoffs_declared"] == walk["handoffs_consumed"]
            )
            passing = passing and row_pass
            rows[shape_key][variant] = {
                "values": values,
                "value_semantics": (
                    "static algebraic predicates, not simulated "
                    "register-state values"
                ),
                "endpoint_predicate": endpoint_predicate,
                "pump_predicate": "three static private-dual/row pairings",
                "selected_register_traces": traces,
                "parent_walk": {
                    "slots": walk["slots_walked"],
                    "collisions": walk["collision_count"],
                    "violations": walk["violation_count"],
                    "handoffs_declared": walk["handoffs_declared"],
                    "handoffs_consumed": walk["handoffs_consumed"],
                },
                "pass": row_pass,
            }
    return {
        "pass": passing,
        "primary_runner_imported": bool(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
        "register_state_readout_evaluated": False,
        "boxes": rows,
    }


@dataclass(frozen=True)
class IndependentCell:
    identity: int
    rotor: int
    carry: int
    predecessor: int | None
    binder: int
    valid: int
    orientation: int


class IndependentChain:
    """Independent finite admission and interval implementation."""

    def __init__(self, bank: int):
        self.bank = bank
        self.rotor = 14
        self.cells: list[IndependentCell] = []
        self.admitted_identities: set[int] = set()
        self.exhausted = False

    def admit(
        self,
        *,
        tick_id: int,
        orientation: int,
        certificate: int,
        binder: int,
        actuality: int,
        admissibility: int,
        law_domain: int,
    ) -> str:
        opportunity = bool(certificate and binder)
        freshness = tick_id not in self.admitted_identities
        if not opportunity:
            return "no_opportunity"
        if not freshness:
            return "refused_fresh"
        if not (actuality and admissibility and law_domain):
            return "refused_supplied"
        if len(self.cells) >= self.bank:
            self.exhausted = True
            return "exhausted"
        rotor = (self.rotor + 1) % 16
        predecessor = self.cells[-1].identity if self.cells else None
        self.cells.append(IndependentCell(
            identity=tick_id,
            rotor=rotor,
            carry=int(rotor == 0),
            predecessor=predecessor,
            binder=int(bool(binder)),
            valid=1,
            orientation=orientation,
        ))
        self.admitted_identities.add(tick_id)
        self.rotor = rotor
        return "admitted"

    def interval(self, start_identity: int, end_identity: int) -> int | None:
        positions = {cell.identity: index for index, cell in enumerate(self.cells)}
        if start_identity not in positions or end_identity not in positions:
            return None
        start = positions[start_identity]
        end = positions[end_identity]
        if start > end:
            reverse = self.interval(end_identity, start_identity)
            return None if reverse is None else -reverse
        span = self.cells[start + 1:end + 1]
        predecessor = self.cells[start].identity
        for cell in span:
            if cell.predecessor != predecessor or not cell.valid or not cell.binder:
                return None
            predecessor = cell.identity
        carries = sum(cell.carry for cell in span)
        rotor_delta = self.cells[end].rotor - self.cells[start].rotor
        return 16 * carries + rotor_delta


def interval_quadruple(chain: object) -> dict[str, int | None]:
    return {
        "interval(2,11)": chain.interval(2, 11),
        "interval(11,23)": chain.interval(11, 23),
        "interval(2,23)": chain.interval(2, 23),
        "interval(11,2)": chain.interval(11, 2),
    }


def landed_cell_tuple(cell: object) -> tuple[object, ...]:
    return tuple(
        getattr(cell, field)
        for field in (
            "identity",
            "rotor",
            "carry",
            "predecessor",
            "binder",
            "valid",
            "orientation",
        )
    )


def independent_cell_tuple(cell: IndependentCell) -> tuple[object, ...]:
    return (
        cell.identity,
        cell.rotor,
        cell.carry,
        cell.predecessor,
        cell.binder,
        cell.valid,
        cell.orientation,
    )


def feed_pair(
    identities: tuple[int, ...],
    *,
    false_actuality_identity: int | None = None,
) -> tuple[IndependentChain, object, list[dict[str, object]]]:
    independent = IndependentChain(bank=24)
    landed = C704.C610.EventChain(bank=24)
    comparisons = []
    for identity in identities:
        actuality = int(identity != false_actuality_identity)
        arguments = {
            "tick_id": identity,
            "orientation": 1,
            "certificate": 1,
            "binder": 1,
            "actuality": actuality,
            "admissibility": 1,
            "law_domain": 1,
        }
        independent_status = independent.admit(**arguments)
        landed_status = landed.admit(**arguments)
        states_equal = True
        if independent_status == "admitted" and landed_status == "admitted":
            states_equal = (
                independent_cell_tuple(independent.cells[-1])
                == landed_cell_tuple(landed.cells[-1])
            )
        comparisons.append({
            "identity": identity,
            "independent_status": independent_status,
            "landed_status": landed_status,
            "status_equal": independent_status == landed_status,
            "new_cell_equal": states_equal,
        })
    return independent, landed, comparisons


def independent_interval_certificate(
    extraction: dict[str, object],
) -> dict[str, object]:
    identities = tuple(int(item) for item in extraction["identity_sequence"])
    independent, landed, comparisons = feed_pair(identities)
    independent_quadruple = interval_quadruple(independent)
    landed_quadruple = interval_quadruple(landed)
    agreement = all(
        row["status_equal"]
        and row["new_cell_equal"]
        and row["independent_status"] == "admitted"
        for row in comparisons
    )
    passed = (
        agreement
        and len(independent.cells) == 24
        and len(landed.cells) == 24
        and independent_quadruple == FROZEN_INTERVALS
        and landed_quadruple == FROZEN_INTERVALS
    )
    return {
        "pass": passed,
        "grammar": (
            "ADMIT = opportunity AND freshness AND actuality AND "
            "admissibility AND law_domain; opportunity = certificate AND binder"
        ),
        "rotor_seed": 14,
        "rotor_rule": "rotor=(previous_rotor+1)%16; carry=int(rotor==0)",
        "interval_rule": "16*sum(carries_after_start_through_end)+end_rotor-start_rotor",
        "admission_comparisons": comparisons,
        "admission_by_admission_agreement": agreement,
        "independent_quadruple": independent_quadruple,
        "landed_cycle610_quadruple": landed_quadruple,
    }


def unchanged_612_certificate() -> dict[str, object]:
    observed = C704.joint_order_controls()
    expected = {
        "consistent_statuses": ("admitted", "admitted"),
        "consistent_acyclic": True,
        "inverted_first": "admitted",
        "inverted_refusal": "refused_inverted",
        "forced_cycle_detected": True,
        "no_endpoint_status": "no_opportunity",
    }
    frozen_outcomes_equal = all(observed[key] == value for key, value in expected.items())
    module_equal = (
        observed["JointOrder_class_module"]
        == C704.C612.JointOrder.__module__
    )
    return {
        "pass": frozen_outcomes_equal and module_equal,
        "expected_six_frozen_outcomes": expected,
        "observed": observed,
        "six_frozen_outcomes_equal": frozen_outcomes_equal,
        "JointOrder_class_module_equal": module_equal,
    }


def sha_pin_certificate() -> dict[str, object]:
    paths = {
        "Cycle610": (ROOT / CYCLE610_PATH).resolve(),
        "Cycle612": (ROOT / CYCLE612_PATH).resolve(),
    }
    observed = {
        label: sha256(path.read_bytes()).hexdigest()
        for label, path in paths.items()
    }
    expected = {
        "Cycle610": C704.C610_SHA256,
        "Cycle612": C704.C612_SHA256,
    }
    module_paths = {
        "Cycle610": Path(C704.C610.__file__).resolve(),
        "Cycle612": Path(C704.C612.__file__).resolve(),
    }
    pins_equal = all(observed[label] == expected[label] for label in paths)
    module_paths_equal = all(module_paths[label] == paths[label] for label in paths)
    return {
        "pass": pins_equal and module_paths_equal,
        "paths": {label: str(path) for label, path in paths.items()},
        "module_paths": {
            label: str(path) for label, path in module_paths.items()
        },
        "observed_sha256": observed,
        "expected_C704_pins": expected,
        "pins_equal": pins_equal,
        "module_paths_equal": module_paths_equal,
    }


def fault_certificate(extraction: dict[str, object]) -> dict[str, object]:
    identities = tuple(int(item) for item in extraction["identity_sequence"])

    independent_flip, landed_flip, flip_comparisons = feed_pair(
        identities, false_actuality_identity=11
    )
    flip_index = identities.index(11)
    independent_flip_quadruple = interval_quadruple(independent_flip)
    landed_flip_quadruple = interval_quadruple(landed_flip)
    flip_pass = (
        flip_comparisons[flip_index]["independent_status"] == "refused_supplied"
        and flip_comparisons[flip_index]["landed_status"] == "refused_supplied"
        and independent_flip_quadruple == DEGRADED_INTERVALS
        and landed_flip_quadruple == DEGRADED_INTERVALS
        and any(value is None for value in independent_flip_quadruple.values())
    )

    independent_full, landed_full, full_comparisons = feed_pair(identities)
    extra_arguments = {
        "tick_id": max(identities) + 1,
        "orientation": 1,
        "certificate": 1,
        "binder": 1,
        "actuality": 1,
        "admissibility": 1,
        "law_domain": 1,
    }
    independent_exhausted = independent_full.admit(**extra_arguments)
    landed_exhausted = landed_full.admit(**extra_arguments)
    exhaustion_pass = (
        all(row["status_equal"] and row["new_cell_equal"] for row in full_comparisons)
        and independent_exhausted == "exhausted"
        and landed_exhausted == "exhausted"
    )

    hostile = list(identities)
    index_11 = hostile.index(11)
    index_23 = hostile.index(23)
    hostile[index_11], hostile[index_23] = hostile[index_23], hostile[index_11]
    independent_hostile, landed_hostile, hostile_comparisons = feed_pair(
        tuple(hostile)
    )
    independent_hostile_quadruple = interval_quadruple(independent_hostile)
    landed_hostile_quadruple = interval_quadruple(landed_hostile)
    hostile_pass = (
        hostile.index(23) < hostile.index(11)
        and all(
            row["status_equal"]
            and row["new_cell_equal"]
            and row["independent_status"] == "admitted"
            for row in hostile_comparisons
        )
        and independent_hostile_quadruple == landed_hostile_quadruple
        and independent_hostile_quadruple != FROZEN_INTERVALS
    )
    return {
        "pass": flip_pass and exhaustion_pass and hostile_pass,
        "actuality_flip": {
            "identity": 11,
            "independent_status": flip_comparisons[flip_index][
                "independent_status"
            ],
            "landed_status": flip_comparisons[flip_index]["landed_status"],
            "independent_quadruple": independent_flip_quadruple,
            "landed_quadruple": landed_flip_quadruple,
            "incomplete": any(
                value is None for value in independent_flip_quadruple.values()
            ),
            "pass": flip_pass,
        },
        "twenty_fifth_admission": {
            "identity": extra_arguments["tick_id"],
            "independent_status": independent_exhausted,
            "landed_status": landed_exhausted,
            "pass": exhaustion_pass,
        },
        "hostile_order": {
            "identity_sequence": hostile,
            "23_before_11": hostile.index(23) < hostile.index(11),
            "independent_quadruple": independent_hostile_quadruple,
            "landed_quadruple": landed_hostile_quadruple,
            "differs_from_frozen": (
                independent_hostile_quadruple != FROZEN_INTERVALS
            ),
            "pass": hostile_pass,
        },
    }


def assignment_targets(node: ast.AST) -> list[ast.AST]:
    if isinstance(node, (ast.Tuple, ast.List)):
        output = []
        for element in node.elts:
            output.extend(assignment_targets(element))
        return output
    return [node]


def attribute_root_name(node: ast.Attribute) -> str | None:
    value: ast.AST = node
    while isinstance(value, (ast.Attribute, ast.Subscript)):
        value = value.value
    return value.id if isinstance(value, ast.Name) else None


def primary_source_discipline() -> dict[str, object]:
    _source, tree = parse_primary()
    forbidden_classes = [
        node.name for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
        and node.name in {"JointOrder", "EventChain"}
    ]
    imported_harness_aliases: set[str] = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith(("frontier_", "physical_")):
                    imported_harness_aliases.add(
                        alias.asname or alias.name.split(".", 1)[0]
                    )
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").startswith(("frontier_", "physical_")):
                imported_harness_aliases.update(
                    alias.asname or alias.name for alias in node.names
                )

    attribute_assignments = []
    for node in ast.walk(tree):
        targets: list[ast.AST] = []
        if isinstance(node, ast.Assign):
            for target in node.targets:
                targets.extend(assignment_targets(target))
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.extend(assignment_targets(node.target))
        for target in targets:
            if (
                isinstance(target, ast.Attribute)
                and attribute_root_name(target) in imported_harness_aliases
            ):
                attribute_assignments.append({
                    "line": target.lineno,
                    "target": ast.unparse(target),
                })

    audit_node = module_assignment(tree, "AUDIT_INPUT_PATHS")
    audit_literal = None
    audit_literal_error = None
    try:
        audit_literal = ast.literal_eval(audit_node)
    except (ValueError, TypeError) as exc:
        audit_literal_error = f"{type(exc).__name__}: {exc}"
    audit_is_literal_tuple = (
        isinstance(audit_node, ast.Tuple)
        and isinstance(audit_literal, tuple)
    )
    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    return {
        "pass": (
            not forbidden_classes
            and not attribute_assignments
            and audit_is_literal_tuple
            and not blocked_present
        ),
        "forbidden_class_definitions": forbidden_classes,
        "imported_harness_aliases": sorted(imported_harness_aliases),
        "attribute_assignments_onto_imported_harnesses": attribute_assignments,
        "AUDIT_INPUT_PATHS_literal_tuple": audit_is_literal_tuple,
        "AUDIT_INPUT_PATHS_literal_value": audit_literal,
        "AUDIT_INPUT_PATHS_literal_error": audit_literal_error,
        "blocked_primary_imports_present": blocked_present,
    }


def run_certificate(
    label: str,
    function: Callable[[], dict[str, object]],
) -> dict[str, object]:
    try:
        result = function()
    except Exception as exc:
        result = {
            "pass": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
    check(label, bool(result.get("pass")), result)
    return result


def main() -> None:
    started = perf_counter()
    extraction = run_certificate(
        "packet_map_extraction",
        packet_map_extraction,
    )
    parent_fields = run_certificate(
        "independent_parent_field_certificates",
        independent_parent_field_certificates,
    )
    interval = run_certificate(
        "independent_interval_certificate",
        lambda: independent_interval_certificate(extraction),
    )
    unchanged_612 = run_certificate(
        "unchanged_612_certificate",
        unchanged_612_certificate,
    )
    sha_pins = run_certificate(
        "sha_pin_certificate",
        sha_pin_certificate,
    )
    faults = run_certificate(
        "fault_certificate",
        lambda: fault_certificate(extraction),
    )
    discipline = run_certificate(
        "primary_source_discipline",
        primary_source_discipline,
    )

    passing = all(row["pass"] for row in CHECKS)
    report = {
        "status": "PASS" if passing else "FAIL",
        "authority": "none",
        "audit": "unset",
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
        "checks": CHECKS,
        "certificates": {
            "packet_map_extraction": extraction,
            "parent_field_certificates": parent_fields,
            "independent_interval": interval,
            "unchanged_612": unchanged_612,
            "sha_pins": sha_pins,
            "faults": faults,
            "primary_source_discipline": discipline,
        },
        "claim_boundary": {
            "register_state_readout_evaluated": False,
            "reversible_packet_encoder_evaluated": False,
            "cycle612_packet_feed_evaluated": False,
            "static_field_predicates_recomputed": bool(
                parent_fields.get("pass")
            ),
        },
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = sha256(json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))
    print(
        "COMPANION_BANK_ENDPOINT_INTERVAL_PROJECTION_INDEPENDENT_CHECK_PASS"
        if passing
        else "COMPANION_BANK_ENDPOINT_INTERVAL_PROJECTION_INDEPENDENT_CHECK_FAIL"
    )
    if not passing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
