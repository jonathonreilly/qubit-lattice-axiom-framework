#!/usr/bin/env python3
"""Independent bounded checker for the Cycle 730 local charge-row guard.

The Cycle 730 primary is parsed as source data only.  Its functions are never
imported or executed.  Controller programs and gate objects come only from the
declared Cycle 719 module; every simulator and charge-law evaluator below is
implemented here.  The checker keeps existential row projection separate from
the per-active-station circuit guard.
"""

from __future__ import annotations

import ast
from importlib.abc import MetaPathFinder
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md"
DIRECT_INPUT_PATHS = (
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
PRIMARY_IMPORT_BLOCKLIST = (
    "frontier_cycle730_charge_row_enforcement_2026_07_28",
)

STDOUT_LIMIT_CHARACTERS = 20_000
ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = ROOT / DIRECT_INPUT_PATHS[0]

# These are the bounded claims the checker must recover and then independently
# recount.  Keeping the table literal makes the check target mechanically
# inspectable without executing this checker.
FROZEN_EXPECTATIONS = (
    ("two_bank_stations", 11),
    ("two_bank_nonidentity_stations", 11),
    ("two_bank_violation_cases", 23),
    ("two_bank_refusal_events", 45),
    ("padded_stations", 130),
    ("padded_nonidentity_stations", 91),
    ("padded_violation_cases", 183),
    ("padded_refusal_events", 341),
    ("ring11_rail_h_cases", 8388608),
    ("ring11_sector_cases", 4194304),
    ("ring11_sector_cases_per_h", 2097152),
    ("ring11_fixed_reference_passes_per_h", 2048),
    ("witness_A_mask", 33),
    ("witness_B_mask", 0),
    ("witness_refs_mask", 62),
    ("witness_h", 0),
    ("witness_token_sites", (0, 5)),
    ("cycle724_semantic_gates", 98034),
    ("cycle730_semantic_gates", 99310),
    ("cycle730_added_semantic_gates", 1276),
)


class _PrimaryImportBlocker(MetaPathFinder):
    """Reject any accidental import of the checked Cycle 730 primary."""

    def find_spec(self, fullname, path=None, target=None):
        del path, target
        if fullname in PRIMARY_IMPORT_BLOCKLIST:
            raise ImportError(
                f"independent-check blocklist rejected {fullname}"
            )
        return None


_BLOCKER = _PrimaryImportBlocker()
sys.meta_path.insert(0, _BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


EXTRACTED: dict[str, object] = {}


def _expectations() -> dict[str, object]:
    return dict(FROZEN_EXPECTATIONS)


def _assignment_nodes(tree: ast.AST) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for node in getattr(tree, "body", ()):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            found[node.targets[0].id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            found[node.target.id] = node.value
    return found


def _function_nodes(tree: ast.AST) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in getattr(tree, "body", ())
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _literal(node: ast.AST) -> object:
    return ast.literal_eval(node)


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
    """Recursively recover literal mutable-input declarations, fail closed."""

    seen: set[str] = set()
    pending = list(direct_paths)
    while pending:
        relative = pending.pop()
        if relative in seen:
            continue
        seen.add(relative)
        if not (relative.startswith("scripts/") and relative.endswith(".py")):
            continue
        source_path = ROOT / relative
        tree = ast.parse(
            source_path.read_text(encoding="utf-8"),
            filename=str(source_path),
        )
        nested: tuple[str, ...] = ()
        for node in tree.body:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            if not any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in targets
            ):
                continue
            value = ast.literal_eval(node.value)
            if (
                not isinstance(value, (tuple, list))
                or not value
                or not all(isinstance(item, str) for item in value)
            ):
                raise ValueError(("invalid AUDIT_INPUT_PATHS", relative))
            nested = tuple(value)
            break
        pending.extend(nested)
    return tuple(sorted(seen))


def _returned_literal(
    function: ast.FunctionDef, key: str
) -> object:
    """Extract one constant-valued field from a function's returned dict."""

    for node in ast.walk(function):
        if not isinstance(node, ast.Return) or not isinstance(node.value, ast.Dict):
            continue
        for key_node, value_node in zip(node.value.keys, node.value.values):
            if (
                isinstance(key_node, ast.Constant)
                and key_node.value == key
            ):
                return _literal(value_node)
    raise KeyError((function.name, key))


def _integer_literals(function: ast.FunctionDef) -> frozenset[int]:
    return frozenset(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Constant)
        and type(node.value) is int
    )


def _compact(value: object, limit: int = 2600) -> str:
    text = json.dumps(value, sort_keys=True, default=repr, separators=(",", ":"))
    if len(text) <= limit:
        return text
    return json.dumps(
        {
            "characters": len(text),
            "prefix": text[: limit - 120],
            "truncated": True,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _mask(width: int) -> int:
    return (1 << width) - 1


def _next_source_bits(value: int, width: int) -> int:
    """Output site s receives input site s+1."""

    return ((value >> 1) | ((value & 1) << (width - 1))) & _mask(width)


def _marked_station(width: int) -> int:
    """Cycle-728 convention: first site of the lexicographically first edge."""

    return min((site, (site + 1) % width) for site in range(width))[0]


def _charge_row_mask(
    a: int, b: int, refs: int, h: int, width: int
) -> int:
    """Evaluate every L_s under the declared marked-edge XOR law."""

    twist = h << _marked_station(width)
    return (a ^ b ^ refs ^ _next_source_bits(refs, width) ^ twist) & _mask(
        width
    )


def _charge_row_value(
    a: int, b: int, refs: int, h: int, station: int, width: int
) -> int:
    return (
        ((a >> station) & 1)
        ^ ((b >> station) & 1)
        ^ ((refs >> station) & 1)
        ^ ((refs >> ((station + 1) % width)) & 1)
        ^ (h if station == _marked_station(width) else 0)
    )


def _reference_extension(
    a: int, b: int, h: int, width: int
) -> tuple[int, int]:
    """Solve all rows from ref_0=0 and return (reference mask, closure)."""

    rails = a ^ b
    refs = 0
    current = 0
    marked = _marked_station(width)
    for station in range(width):
        following = current ^ ((rails >> station) & 1)
        if station == marked:
            following ^= h
        if station + 1 < width:
            refs |= following << (station + 1)
            current = following
        else:
            return refs, following
    raise AssertionError("positive ring width required")


def _lawful_reference(width: int) -> tuple[int, int]:
    refs, closure = _reference_extension(_mask(width), 0, width & 1, width)
    if closure:
        raise AssertionError(("lawful reference closure", width))
    return refs, width & 1


def _program_nonidentity(program: tuple[object, ...]) -> tuple[int, ...]:
    return tuple(
        station
        for station, row in enumerate(program)
        if K.mapped_macro(row)
    )


def _violation_cases(
    program: tuple[object, ...],
) -> tuple[tuple[int, str, int | None, int, int], ...]:
    width = len(program)
    baseline_refs, baseline_h = _lawful_reference(width)
    cases: list[tuple[int, str, int | None, int, int]] = []
    for station in _program_nonidentity(program):
        for kind, flipped in (
            ("flip_ref_s", station),
            ("flip_ref_s_plus_1", (station + 1) % width),
        ):
            cases.append(
                (
                    station,
                    kind,
                    flipped,
                    baseline_refs ^ (1 << flipped),
                    baseline_h,
                )
            )
    marked = _marked_station(width)
    if K.mapped_macro(program[marked]):
        cases.append(
            (
                marked,
                "flip_h",
                None,
                baseline_refs,
                baseline_h ^ 1,
            )
        )
    return tuple(cases)


def _predicted_refusals(
    program: tuple[object, ...], refs: int, h: int
) -> tuple[tuple[int, int], ...]:
    """Independent one-token event prediction, with no circuit execution."""

    width = len(program)
    events = []
    for step in range(width):
        station = step
        if (
            K.mapped_macro(program[station])
            and _charge_row_value(
                1 << station, 0, refs, h, station, width
            )
        ):
            events.append((step, station))
    return tuple(events)


def _census_summary(program: tuple[object, ...]) -> dict[str, object]:
    cases = _violation_cases(program)
    events = []
    target_misses = 0
    for target, _kind, _flipped, refs, h in cases:
        case_events = _predicted_refusals(program, refs, h)
        events.extend(case_events)
        target_misses += not any(station == target for _step, station in case_events)
    return {
        "stations": len(program),
        "nonidentity_stations": len(_program_nonidentity(program)),
        "violation_cases": len(cases),
        "refusal_events": len(events),
        "target_station_misses": target_misses,
    }


def _source_conventions(
    source: str, functions: dict[str, ast.FunctionDef]
) -> dict[str, bool]:
    charge_text = ast.get_source_segment(
        source, functions["charge_row_value"]
    ) or ""
    cascade_text = ast.get_source_segment(
        source, functions["local_or_compute"]
    ) or ""
    controller_text = ast.get_source_segment(
        source, functions["extended_controller_build"]
    ) or ""
    cases_text = ast.get_source_segment(
        source, functions["charge_violation_cases"]
    ) or ""
    return {
        "charge_law_has_A_B_refs_next_and_h": all(
            token in charge_text
            for token in (
                "a[station]",
                "b[station]",
                "refs[station]",
                "refs[(station + 1) % stations]",
                "marked_station(stations)",
            )
        ),
        "cascade_is_recurrent_OR": all(
            token in cascade_text
            for token in (
                "or_into(inputs[0], inputs[1]",
                "outputs[index - 1]",
                "inputs[2:]",
            )
        ),
        "charge_is_seventh_dirty_input": (
            'layout["charge_base"] + station' in controller_text
            and "LOCAL_ROW_INPUTS" in cascade_text
        ),
        "two_ref_flips_and_marked_h_flip": all(
            token in cases_text
            for token in (
                '"flip_ref_s"',
                '"flip_ref_s_plus_1"',
                '"flip_h"',
            )
        ),
    }


def extraction() -> tuple[bool, dict[str, object]]:
    """AST-extract the primary's literals, law, censuses, and conventions."""

    source = PRIMARY_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(PRIMARY_PATH))
    nodes = _assignment_nodes(tree)
    functions = _function_nodes(tree)
    required = (
        "AUDIT_TIMEOUT_SEC",
        "NOTE_PATH",
        "DIRECT_INPUT_PATHS",
        "AUDIT_INPUT_PATHS",
        "OR_INTERMEDIATE_PER_STATION",
        "LOCAL_ROW_INPUTS",
        "EXPECTED_CYCLE724_PADDED_GATES",
        "EXPECTED_CYCLE730_PADDED_GATES",
        "FROZEN_MATCHED_PARITY_MULTITOKEN_WITNESS",
    )
    values: dict[str, object] = {}
    failures: dict[str, str] = {}
    for name in required:
        try:
            values[name] = _literal(nodes[name])
        except Exception as exc:
            failures[name] = f"{type(exc).__name__}: {exc}"

    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    self_nodes = _assignment_nodes(self_tree)
    try:
        self_direct_inputs = _literal(self_nodes["DIRECT_INPUT_PATHS"])
        self_inputs = _literal(self_nodes["AUDIT_INPUT_PATHS"])
        self_blocklist = _literal(self_nodes["PRIMARY_IMPORT_BLOCKLIST"])
        self_frozen = _literal(self_nodes["FROZEN_EXPECTATIONS"])
    except Exception as exc:
        failures["checker_literals"] = f"{type(exc).__name__}: {exc}"
        self_direct_inputs = self_inputs = None
        self_blocklist = self_frozen = None

    expected = _expectations()
    two_bank = _census_summary(K.interleaved_program(2))
    padded = _census_summary(
        K.interleaved_program(12, physical_padding=True)
    )
    try:
        theorem_width = int(
            _returned_literal(
                functions["projection_and_local_guard_certificate"],
                "ring_stations",
            )
        )
        projection_integers = _integer_literals(
            functions["projection_and_local_guard_certificate"]
        )
        main_integers = _integer_literals(functions["main"])
    except Exception as exc:
        failures["primary_count_anchors"] = (
            f"{type(exc).__name__}: {exc}"
        )
        theorem_width = 0
        projection_integers = frozenset()
        main_integers = frozenset()
    theorem_cases = 2 * (1 << (2 * theorem_width))
    witness = dict(
        values.get("FROZEN_MATCHED_PARITY_MULTITOKEN_WITNESS", ())
    )
    conventions = (
        _source_conventions(source, functions)
        if all(
            name in functions
            for name in (
                "charge_row_value",
                "local_or_compute",
                "extended_controller_build",
                "charge_violation_cases",
            )
        )
        else {}
    )

    EXTRACTED.clear()
    EXTRACTED.update(values)
    EXTRACTED["two_bank_census"] = two_bank
    EXTRACTED["padded_census"] = padded
    EXTRACTED["ring11_rail_h_cases"] = theorem_cases
    EXTRACTED["conventions"] = conventions

    primary_direct_inputs = values.get("DIRECT_INPUT_PATHS")
    primary_inputs = values.get("AUDIT_INPUT_PATHS")
    try:
        primary_closure = declared_input_closure(
            tuple(primary_direct_inputs)
        )
        checker_closure = declared_input_closure(DIRECT_INPUT_PATHS)
    except Exception as exc:
        failures["declared_input_closure"] = (
            f"{type(exc).__name__}: {exc}"
        )
        primary_closure = checker_closure = ()
    primary_audit_literal = isinstance(values.get("AUDIT_INPUT_PATHS"), tuple)
    primary_closure_exact = primary_closure == primary_inputs
    checker_closure_exact = checker_closure == AUDIT_INPUT_PATHS
    checker_literals_exact = (
        self_direct_inputs == DIRECT_INPUT_PATHS
        and self_inputs == AUDIT_INPUT_PATHS
        and self_blocklist == PRIMARY_IMPORT_BLOCKLIST
        and self_frozen == FROZEN_EXPECTATIONS
    )
    census_match = (
        two_bank["violation_cases"] == expected["two_bank_violation_cases"]
        and two_bank["refusal_events"] == expected["two_bank_refusal_events"]
        and padded["violation_cases"] == expected["padded_violation_cases"]
        and padded["refusal_events"] == expected["padded_refusal_events"]
    )
    witness_match = (
        witness.get("A_mask") == expected["witness_A_mask"]
        and witness.get("B_mask") == expected["witness_B_mask"]
        and witness.get("refs_mask") == expected["witness_refs_mask"]
        and witness.get("h") == expected["witness_h"]
        and witness.get("token_sites") == expected["witness_token_sites"]
    )
    counts_match = (
        values.get("EXPECTED_CYCLE724_PADDED_GATES")
        == expected["cycle724_semantic_gates"]
        and values.get("EXPECTED_CYCLE730_PADDED_GATES")
        == expected["cycle730_semantic_gates"]
        and theorem_cases == expected["ring11_rail_h_cases"]
        and expected["padded_nonidentity_stations"] in main_integers
        and expected["ring11_sector_cases_per_h"] in projection_integers
        and expected["ring11_sector_cases"] in projection_integers
    )
    primary_not_loaded = all(
        name not in sys.modules for name in PRIMARY_IMPORT_BLOCKLIST
    )
    passed = (
        not failures
        and primary_audit_literal
        and primary_closure_exact
        and checker_closure_exact
        and checker_literals_exact
        and census_match
        and witness_match
        and counts_match
        and values.get("OR_INTERMEDIATE_PER_STATION") == 5
        and values.get("LOCAL_ROW_INPUTS") == 7
        and conventions
        and all(conventions.values())
        and primary_not_loaded
    )
    return passed, {
        "ast_only_primary": True,
        "literal_failures": failures,
        "primary_AUDIT_tuple_literal": primary_audit_literal,
        "primary_declared_input_count": len(primary_inputs or ()),
        "primary_declared_input_closure_exact": primary_closure_exact,
        "checker_declared_input_count": len(AUDIT_INPUT_PATHS),
        "checker_declared_input_closure_exact": checker_closure_exact,
        "checker_AUDIT_and_blocklist_literals_exact": checker_literals_exact,
        "conventions": conventions,
        "two_bank_census": two_bank,
        "padded_census": padded,
        "primary_AST_count_anchors": {
            "ring_stations": theorem_width,
            "nonidentity_stations": (
                expected["padded_nonidentity_stations"] in main_integers
            ),
            "sector_cases_per_h": (
                expected["ring11_sector_cases_per_h"]
                in projection_integers
            ),
            "satisfying_reference_extensions_per_h": (
                expected["ring11_sector_cases"] in projection_integers
            ),
        },
        "theorem_cases": theorem_cases,
        "witness": witness,
        "word_sizes": (
            values.get("EXPECTED_CYCLE724_PADDED_GATES"),
            values.get("EXPECTED_CYCLE730_PADDED_GATES"),
        ),
        "primary_imported": not primary_not_loaded,
    }


Gate = tuple[str, tuple[int, ...]]


def _x(target: int) -> Gate:
    return ("X", (target,))


def _cn(control: int, target: int) -> Gate:
    return ("CNOT", (control, target))


def _tof(left: int, right: int, target: int) -> Gate:
    return ("TOF", (left, right, target))


def _apply_word(value: int, word: tuple[Gate, ...]) -> int:
    """Own integer simulator for X, CNOT, and Toffoli gates."""

    output = value
    for kind, wires in word:
        if kind == "X":
            output ^= 1 << wires[0]
        elif kind == "CNOT":
            if (output >> wires[0]) & 1:
                output ^= 1 << wires[1]
        elif kind == "TOF":
            if ((output >> wires[0]) & 1) and ((output >> wires[1]) & 1):
                output ^= 1 << wires[2]
        else:
            raise ValueError(("unsupported gate", kind))
    return output


def _apply_macro(value: int, word: tuple[object, ...]) -> int:
    """Own simulator for K gate data; K's semantic evaluator is not used."""

    output = value
    for gate in word:
        if gate.kind == "X":
            output ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            if (output >> gate.wires[0]) & 1:
                output ^= 1 << gate.wires[1]
        elif gate.kind == "TOF":
            if (
                ((output >> gate.wires[0]) & 1)
                and ((output >> gate.wires[1]) & 1)
            ):
                output ^= 1 << gate.wires[2]
        else:
            raise ValueError(("unsupported K gate", gate.kind))
    return output


def _mcx(
    controls: tuple[int, ...],
    target: int,
    scratch: tuple[int, ...],
) -> tuple[Gate, ...]:
    """Clean-scratch multi-control X decomposition, independently written."""

    if len(controls) == 1:
        return (_cn(controls[0], target),)
    if len(controls) == 2:
        return (_tof(controls[0], controls[1], target),)
    if len(scratch) < len(controls) - 2:
        raise ValueError(("MCX scratch", len(controls), len(scratch)))
    prefix = [_tof(controls[0], controls[1], scratch[0])]
    for index in range(2, len(controls) - 1):
        prefix.append(
            _tof(controls[index], scratch[index - 2], scratch[index - 1])
        )
    final = _tof(controls[-1], scratch[len(controls) - 3], target)
    return tuple(prefix) + (final,) + tuple(reversed(prefix))


def _swap(left: int, right: int) -> tuple[Gate, ...]:
    return (_cn(left, right), _cn(right, left), _cn(left, right))


def _data_width(program: tuple[object, ...]) -> int:
    return 1 + max(
        wire
        for row in program
        for gate in K.mapped_macro(row)
        for wire in gate.wires
    )


def _layout(data_width: int, stations: int) -> dict[str, int]:
    a_base = data_width
    b_base = a_base + stations
    work_base = b_base + stations
    syndrome_base = work_base + stations
    scratch_base = syndrome_base + stations
    or_base = scratch_base + 2 * stations
    ref_base = or_base + 5 * stations
    charge_base = ref_base + stations
    h_wire = charge_base + stations
    return {
        "data_width": data_width,
        "stations": stations,
        "a_base": a_base,
        "b_base": b_base,
        "work_base": work_base,
        "syndrome_base": syndrome_base,
        "scratch_base": scratch_base,
        "or_base": or_base,
        "ref_base": ref_base,
        "charge_base": charge_base,
        "h_wire": h_wire,
        "full_width": h_wire + 1,
    }


def _or_into(left: int, right: int, target: int) -> tuple[Gate, ...]:
    return (_cn(left, target), _cn(right, target), _tof(left, right, target))


def _or_cascade(
    inputs: tuple[int, ...],
    intermediates: tuple[int, ...],
    syndrome: int,
) -> tuple[Gate, ...]:
    if len(inputs) != 7 or len(intermediates) != 5:
        raise ValueError(("OR-cascade shape", len(inputs), len(intermediates)))
    outputs = intermediates + (syndrome,)
    word = list(_or_into(inputs[0], inputs[1], outputs[0]))
    for index, source in enumerate(inputs[2:], start=1):
        word.extend(_or_into(outputs[index - 1], source, outputs[index]))
    return tuple(word)


def _lifted_macro(
    macro: tuple[object, ...],
    token: int,
    enabled: int,
    scratch: tuple[int, ...],
) -> tuple[Gate, ...]:
    output: list[Gate] = []
    for gate in macro:
        if gate.kind == "X":
            output.extend(_mcx((token, enabled), gate.wires[0], scratch))
        elif gate.kind == "CNOT":
            output.extend(
                _mcx(
                    (token, enabled, gate.wires[0]),
                    gate.wires[1],
                    scratch,
                )
            )
        elif gate.kind == "TOF":
            output.extend(
                _mcx(
                    (token, enabled, gate.wires[0], gate.wires[1]),
                    gate.wires[2],
                    scratch,
                )
            )
        else:
            raise ValueError(("unsupported lifted gate", gate.kind))
    return tuple(output)


def _sandwich_word(
    program: tuple[object, ...],
) -> tuple[tuple[Gate, ...], dict[str, int]]:
    """Build the charge sandwich and R layers without primary code."""

    stations = len(program)
    layout = _layout(_data_width(program), stations)
    q: list[Gate] = []
    for station, row in enumerate(program):
        macro = K.mapped_macro(row)
        if not macro:
            continue
        charge = layout["charge_base"] + station
        charge_sources = (
            layout["a_base"] + station,
            layout["b_base"] + station,
            layout["ref_base"] + station,
            layout["ref_base"] + (station + 1) % stations,
        )
        if station == _marked_station(stations):
            charge_sources += (layout["h_wire"],)
        charge_word = tuple(_cn(source, charge) for source in charge_sources)
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty_inputs = (
            layout["b_base"] + station,
            layout["work_base"] + station,
            layout["a_base"] + left,
            layout["b_base"] + left,
            layout["a_base"] + right,
            layout["b_base"] + right,
            charge,
        )
        intermediates = tuple(
            layout["or_base"] + 5 * station + slot for slot in range(5)
        )
        syndrome = layout["syndrome_base"] + station
        or_word = _or_cascade(dirty_inputs, intermediates, syndrome)
        scratch = tuple(
            layout["scratch_base"] + 2 * station + slot for slot in range(2)
        )
        q.extend(charge_word)
        q.extend(or_word)
        q.append(_x(syndrome))
        q.extend(
            _lifted_macro(
                macro,
                layout["a_base"] + station,
                syndrome,
                scratch,
            )
        )
        q.append(_x(syndrome))
        q.extend(reversed(or_word))
        q.extend(reversed(charge_word))

    r1 = tuple(
        gate
        for station in range(stations)
        for gate in _swap(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    )
    r2 = tuple(
        gate
        for station in range(stations)
        for gate in _swap(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % stations,
        )
    )
    return tuple(q) + r1 + r2, layout


def _pack_source(
    data: int, layout: dict[str, int], refs: int, h: int
) -> int:
    output = data | (1 << layout["a_base"])
    for station in range(layout["stations"]):
        if (refs >> station) & 1:
            output |= 1 << (layout["ref_base"] + station)
    if h:
        output |= 1 << layout["h_wire"]
    return output


def _rows(value: int, layout: dict[str, int]) -> dict[str, int]:
    stations = layout["stations"]

    def bank(base: int, count: int) -> int:
        return (value >> base) & _mask(count)

    return {
        "data": value & _mask(layout["data_width"]),
        "A": bank(layout["a_base"], stations),
        "B": bank(layout["b_base"], stations),
        "work": bank(layout["work_base"], stations),
        "syndrome": bank(layout["syndrome_base"], stations),
        "scratch": bank(layout["scratch_base"], 2 * stations),
        "or_scratch": bank(layout["or_base"], 5 * stations),
        "refs": bank(layout["ref_base"], stations),
        "charge": bank(layout["charge_base"], stations),
        "h": (value >> layout["h_wire"]) & 1,
    }


def _direct_program(data: int, program: tuple[object, ...]) -> int:
    output = data
    for row in program:
        output = _apply_macro(output, K.mapped_macro(row))
    return output


def _identity_substituted_orbit(
    data: int,
    program: tuple[object, ...],
    refs: int,
    h: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Separate semantic model: replace every locally dirty macro by identity."""

    output = data
    events = []
    stations = len(program)
    for step in range(stations):
        station = step
        macro = K.mapped_macro(program[station])
        if not macro:
            continue
        a = 1 << station
        dirty = _charge_row_value(a, 0, refs, h, station, stations)
        if dirty:
            events.append((step, station))
        else:
            output = _apply_macro(output, macro)
    return output, tuple(events)


def _auxiliary_clean(rows: dict[str, int]) -> bool:
    return not any(
        rows[name]
        for name in (
            "B",
            "work",
            "syndrome",
            "scratch",
            "or_scratch",
            "charge",
        )
    )


def sandwich_recount() -> tuple[bool, dict[str, object]]:
    """Gate-simulate every 2-bank violation and recount the padded census."""

    expected = _expectations()
    program = K.interleaved_program(2)
    word, layout = _sandwich_word(program)
    refs, h = _lawful_reference(len(program))
    data = sum(
        1 << wire
        for wire in range(layout["data_width"])
        if (wire * wire + 3 * wire + 1) % 7 in (0, 1, 3)
    )
    source = _pack_source(data, layout, refs, h)
    observed = source
    for _step in range(len(program)):
        observed = _apply_word(observed, word)
    lawful_rows = _rows(observed, layout)
    expected_data = _direct_program(data, program)
    restored = observed
    inverse_word = tuple(reversed(word))
    for _step in range(len(program)):
        restored = _apply_word(restored, inverse_word)

    mismatch = 0
    register_failures = 0
    event_mismatches = 0
    target_misses = 0
    refusal_events = 0
    cases = _violation_cases(program)
    for target, _kind, _flipped, case_refs, case_h in cases:
        case_source = _pack_source(data, layout, case_refs, case_h)
        case_observed = case_source
        for _step in range(len(program)):
            case_observed = _apply_word(case_observed, word)
        case_rows = _rows(case_observed, layout)
        predicted_data, predicted_events = _identity_substituted_orbit(
            data, program, case_refs, case_h
        )
        direct_events = _predicted_refusals(program, case_refs, case_h)
        mismatch += case_rows["data"] != predicted_data
        event_mismatches += predicted_events != direct_events
        target_misses += not any(
            station == target for _step, station in predicted_events
        )
        refusal_events += len(predicted_events)
        register_failures += not (
            case_rows["A"] == 1
            and _auxiliary_clean(case_rows)
            and case_rows["refs"] == case_refs
            and case_rows["h"] == case_h
        )

    two_bank = {
        "stations": len(program),
        "nonidentity_stations": len(_program_nonidentity(program)),
        "violation_cases": len(cases),
        "refusal_events": refusal_events,
    }
    padded = _census_summary(
        K.interleaved_program(12, physical_padding=True)
    )
    lawful_ok = (
        lawful_rows["data"] == expected_data
        and lawful_rows["A"] == 1
        and _auxiliary_clean(lawful_rows)
        and lawful_rows["refs"] == refs
        and lawful_rows["h"] == h
        and restored == source
    )
    census_ok = (
        two_bank["violation_cases"] == expected["two_bank_violation_cases"]
        and two_bank["refusal_events"] == expected["two_bank_refusal_events"]
        and padded["violation_cases"] == expected["padded_violation_cases"]
        and padded["refusal_events"] == expected["padded_refusal_events"]
        and padded["target_station_misses"] == 0
    )
    passed = (
        lawful_ok
        and census_ok
        and mismatch == 0
        and event_mismatches == 0
        and target_misses == 0
        and register_failures == 0
    )
    return passed, {
        "own_gate_word_gates": len(word),
        "lawful_equivalence_and_full_return": lawful_ok,
        "literal_inverse_exact": restored == source,
        "two_bank": two_bank,
        "padded": padded,
        "literal_prediction_mismatches": mismatch,
        "independent_event_mismatches": event_mismatches,
        "target_station_misses": target_misses,
        "register_return_failures": register_failures,
    }


def projection_theorem_recount() -> tuple[bool, dict[str, object]]:
    """Exhaust ring-11 existential projection and the fixed-r distinction."""

    width = 11
    rail_mask = _mask(width)
    rail_states = 1 << (2 * width)
    parity = tuple(value.bit_count() & 1 for value in range(1 << width))
    extensions = tuple(
        tuple(_reference_extension(rails, 0, h, width) for rails in range(1 << width))
        for h in (0, 1)
    )

    total_cases = 0
    sector_cases = 0
    exact_separation_failures = 0
    local_row_failures = 0
    complement_failures = 0
    satisfying_reference_extensions = 0
    fixed_zero_reference_passes = [0, 0]
    per_h: list[dict[str, int]] = []
    for h in (0, 1):
        h_cases = 0
        h_sector = 0
        h_failures = 0
        for packed in range(rail_states):
            a = packed & rail_mask
            b = packed >> width
            rails = a ^ b
            in_sector = parity[rails] == h
            refs, closure = extensions[h][rails]
            canonical_pass = (
                closure == 0
                and _charge_row_mask(a, b, refs, h, width) == 0
            )
            complement_pass = (
                closure == 0
                and _charge_row_mask(
                    a, b, refs ^ rail_mask, h, width
                )
                == 0
            )
            projected_pass = canonical_pass or complement_pass
            fixed_zero_reference_passes[h] += (
                _charge_row_mask(a, b, 0, h, width) == 0
            )
            failure = projected_pass != in_sector
            failure |= canonical_pass != in_sector
            failure |= complement_pass != in_sector
            h_failures += failure
            exact_separation_failures += failure
            local_row_failures += in_sector and not canonical_pass
            complement_failures += in_sector and not complement_pass
            satisfying_reference_extensions += canonical_pass + complement_pass
            h_sector += in_sector
            h_cases += 1
        total_cases += h_cases
        sector_cases += h_sector
        per_h.append(
            {
                "h": h,
                "rail_states": h_cases,
                "matching_parity_states": h_sector,
                "fixed_zero_reference_passes":
                    fixed_zero_reference_passes[h],
                "zero_failure_count": h_failures,
            }
        )

    expected = _expectations()
    passed = (
        total_cases == expected["ring11_rail_h_cases"]
        and sector_cases == expected["ring11_sector_cases"]
        and all(
            row["matching_parity_states"]
            == expected["ring11_sector_cases_per_h"]
            for row in per_h
        )
        and all(
            row["fixed_zero_reference_passes"]
            == expected["ring11_fixed_reference_passes_per_h"]
            for row in per_h
        )
        and exact_separation_failures == 0
        and local_row_failures == 0
        and complement_failures == 0
        and satisfying_reference_extensions
        == 2 * expected["ring11_sector_cases"]
    )
    return passed, {
        "ring_stations": width,
        "rail_h_cases_exhausted": total_cases,
        "per_h": per_h,
        "matching_parity_cases": sector_cases,
        "satisfying_reference_extensions": satisfying_reference_extensions,
        "reference_extensions_per_matching_case":
            satisfying_reference_extensions // sector_cases,
        "exact_separation_failures": exact_separation_failures,
        "canonical_local_row_failures": local_row_failures,
        "complement_local_row_failures": complement_failures,
        "existential_reference_projection_iff_parity_equals_h":
            exact_separation_failures == 0,
        "one_fixed_reference_is_not_whole_sector":
            all(
                count
                == expected["ring11_fixed_reference_passes_per_h"]
                for count in fixed_zero_reference_passes
            ),
    }


def finite_ring_projection_recount() -> tuple[bool, dict[str, object]]:
    """Exhaust n=1..5 and test the general recurrence's edge cases."""

    rows = []
    failures = 0
    for width in range(1, 6):
        mask = _mask(width)
        multiplicities: set[int] = set()
        fixed_zero_counts = [0, 0]
        for h in (0, 1):
            for packed in range(1 << (2 * width)):
                a = packed & mask
                b = packed >> width
                matching = ((a ^ b).bit_count() & 1) == h
                solutions = sum(
                    _charge_row_mask(a, b, refs, h, width) == 0
                    for refs in range(1 << width)
                )
                expected_solutions = 2 if matching else 0
                failures += solutions != expected_solutions
                multiplicities.add(solutions)
                fixed_zero_counts[h] += (
                    _charge_row_mask(a, b, 0, h, width) == 0
                )
        expected_fixed = 1 << width
        failures += any(
            count != expected_fixed for count in fixed_zero_counts
        )
        rows.append(
            {
                "ring_stations": width,
                "solution_multiplicities": tuple(sorted(multiplicities)),
                "fixed_zero_reference_passes_per_h":
                    tuple(fixed_zero_counts),
                "expected_fixed_reference_passes_per_h":
                    expected_fixed,
            }
        )
    return failures == 0, {
        "domain_checked": "finite rings n=1..5, including n=1",
        "failures": failures,
        "rows": rows,
        "general_argument": (
            "XOR telescope gives necessity; choosing r_0 determines the "
            "chain, and ring closure is exactly the parity condition"
        ),
    }


def local_guard_non_global_counterexample() -> tuple[bool, dict[str, object]]:
    """Show a parity mismatch whose active station has a clean charge row."""

    width = 11
    a = 1
    b = 0
    refs = 2
    h = 0
    active_station = 0
    row_mask = _charge_row_mask(a, b, refs, h, width)
    parity_mismatch = ((a ^ b).bit_count() & 1) != h
    active_row_clean = ((row_mask >> active_station) & 1) == 0
    dirty_rows = tuple(
        station
        for station in range(width)
        if (row_mask >> station) & 1
    )
    passed = (
        parity_mismatch
        and active_row_clean
        and dirty_rows
        and active_station not in dirty_rows
    )
    return passed, {
        "ring_stations": width,
        "A_mask": a,
        "B_mask": b,
        "refs_mask": refs,
        "h": h,
        "active_station": active_station,
        "charge_row_mask": row_mask,
        "dirty_rows": dirty_rows,
        "parity_mismatch": parity_mismatch,
        "active_charge_row_clean": active_row_clean,
        "conclusion": "the circuit has no global parity acceptance bit",
    }


def static_witness_recount() -> tuple[bool, dict[str, object]]:
    """Reconstruct the frozen static two-token row-system witness."""

    expected = _expectations()
    width = 11
    a = expected["witness_A_mask"]
    b = expected["witness_B_mask"]
    h = expected["witness_h"]
    frozen_refs = expected["witness_refs_mask"]
    refs, closure = _reference_extension(a, b, h, width)
    row_mask = _charge_row_mask(a, b, refs, h, width)
    local_rows = tuple((row_mask >> station) & 1 for station in range(width))
    token_sites = tuple(
        station
        for station in range(width)
        if ((a ^ b) >> station) & 1
    )
    token_count = a.bit_count() + b.bit_count()
    parity_matches = ((a ^ b).bit_count() & 1) == h
    passed = (
        refs == frozen_refs
        and closure == 0
        and not any(local_rows)
        and token_sites == expected["witness_token_sites"]
        and token_count == 2
        and parity_matches
    )
    return passed, {
        "ring_stations": width,
        "A_mask": a,
        "B_mask": b,
        "canonical_refs_mask": refs,
        "frozen_refs_mask": frozen_refs,
        "h": h,
        "token_sites": token_sites,
        "token_count": token_count,
        "closure": closure,
        "local_rows": local_rows,
        "all_local_rows_pass": not any(local_rows),
        "token_parity_equals_h": parity_matches,
        "bounded_scope": (
            "static row-system witness only; no recurrent or global "
            "acceptance claim"
        ),
    }


def _rooted_at_k(node: ast.AST) -> bool:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return isinstance(node, ast.Name) and node.id == "K"


def _k_writes(tree: ast.AST) -> list[tuple[int, str]]:
    writes = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Attribute, ast.Subscript)):
            if isinstance(node.ctx, (ast.Store, ast.Del)) and _rooted_at_k(node):
                writes.append((node.lineno, ast.unparse(node)))
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in ("setattr", "delattr")
            and node.args
            and _rooted_at_k(node.args[0])
        ):
            writes.append((node.lineno, ast.unparse(node)))
    return writes


def _frozen_literal_failures(
    nodes: dict[str, ast.AST]
) -> dict[str, str]:
    failures = {}
    for name, node in nodes.items():
        if not name.startswith("FROZEN"):
            continue
        try:
            _literal(node)
        except Exception as exc:
            failures[name] = f"{type(exc).__name__}: {exc}"
    return failures


def discipline() -> tuple[bool, dict[str, object]]:
    """Check literal discipline, K immutability, and word-size arithmetic."""

    primary_source = PRIMARY_PATH.read_text(encoding="utf-8")
    primary_tree = ast.parse(primary_source, filename=str(PRIMARY_PATH))
    primary_nodes = _assignment_nodes(primary_tree)
    checker_source = Path(__file__).read_text(encoding="utf-8")
    checker_tree = ast.parse(checker_source, filename=__file__)
    checker_nodes = _assignment_nodes(checker_tree)

    primary_writes = _k_writes(primary_tree)
    checker_writes = _k_writes(checker_tree)
    primary_frozen_failures = _frozen_literal_failures(primary_nodes)
    checker_frozen_failures = _frozen_literal_failures(checker_nodes)

    direct_primary_imports = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            direct_primary_imports.extend(
                alias.name
                for alias in node.names
                if alias.name in PRIMARY_IMPORT_BLOCKLIST
            )
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module in PRIMARY_IMPORT_BLOCKLIST
        ):
            direct_primary_imports.append(node.module)

    expected = _expectations()
    program = K.interleaved_program(12, physical_padding=True)
    nonidentity = len(_program_nonidentity(program))
    base = int(EXTRACTED["EXPECTED_CYCLE724_PADDED_GATES"])
    observed = int(EXTRACTED["EXPECTED_CYCLE730_PADDED_GATES"])
    added_from_program_census = 14 * nonidentity + 2
    reproduced = base + added_from_program_census
    arithmetic_ok = (
        len(program) == expected["padded_stations"]
        and nonidentity == expected["padded_nonidentity_stations"]
        and added_from_program_census
        == expected["cycle730_added_semantic_gates"]
        and reproduced == observed == expected["cycle730_semantic_gates"]
    )
    primary_loaded = any(
        name in sys.modules for name in PRIMARY_IMPORT_BLOCKLIST
    )
    passed = (
        not primary_writes
        and not checker_writes
        and not primary_frozen_failures
        and not checker_frozen_failures
        and not direct_primary_imports
        and not primary_loaded
        and arithmetic_ok
    )
    return passed, {
        "primary_K_attribute_writes": primary_writes,
        "checker_K_attribute_writes": checker_writes,
        "primary_frozen_literal_failures": primary_frozen_failures,
        "checker_frozen_literal_failures": checker_frozen_failures,
        "checker_direct_primary_imports": direct_primary_imports,
        "primary_present_in_sys_modules": primary_loaded,
        "program_census": {
            "stations": len(program),
            "nonidentity_stations": nonidentity,
        },
        "word_size_arithmetic": {
            "cycle724": base,
            "per_nonidentity_delta": 14,
            "marked_edge_extra": 2,
            "added": added_from_program_census,
            "reproduced_cycle730": reproduced,
            "primary_cycle730": observed,
        },
    }


CERTIFICATES = (
    ("extraction", extraction),
    ("sandwich_recount", sandwich_recount),
    ("projection_theorem_recount", projection_theorem_recount),
    ("finite_ring_projection_recount", finite_ring_projection_recount),
    (
        "local_guard_non_global_counterexample",
        local_guard_non_global_counterexample,
    ),
    ("static_witness_recount", static_witness_recount),
    ("discipline", discipline),
)


def main() -> int:
    started = perf_counter()
    results: dict[str, bool] = {}
    details: dict[str, object] = {}
    lines = []
    for name, certificate in CERTIFICATES:
        try:
            passed, detail = certificate()
        except Exception as exc:
            passed = False
            detail = {
                "honest_exception": type(exc).__name__,
                "message": str(exc),
            }
        results[name] = bool(passed)
        details[name] = detail
        lines.append(
            f"{'PASS' if passed else 'FAIL'} {name} :: {_compact(detail)}"
        )

    runtime = perf_counter() - started
    within_timeout = runtime <= AUDIT_TIMEOUT_SEC
    passed_count = sum(results.values())
    all_pass = all(results.values()) and within_timeout
    summary = {
        "checker": "cycle730_local_charge_row_guard_independent_check",
        "declared_mutable_input_paths": len(AUDIT_INPUT_PATHS),
        "declared_input_closure_exact": bool(
            details.get("extraction", {}).get(
                "checker_declared_input_closure_exact", False
            )
        ),
        "blocklist": PRIMARY_IMPORT_BLOCKLIST,
        "certificates": f"{passed_count}/{len(CERTIFICATES)}",
        "failed": tuple(name for name, passed in results.items() if not passed),
        "pass": all_pass,
        "runtime_seconds": round(runtime, 6),
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
        "within_timeout": within_timeout,
    }
    lines.append(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    lines.append(
        "CYCLE730_LOCAL_GUARD_INDEPENDENT_CHECK_PASS"
        if all_pass
        else "CYCLE730_LOCAL_GUARD_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    text = "\n".join(lines) + "\n"
    if len(text) >= STDOUT_LIMIT_CHARACTERS:
        text = (
            json.dumps(
                {
                    **summary,
                    "pass": False,
                    "stdout_character_bound_failure": len(text),
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\nCYCLE730_LOCAL_GUARD_INDEPENDENT_CHECK_HONEST_FAIL\n"
        )
        all_pass = False
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
