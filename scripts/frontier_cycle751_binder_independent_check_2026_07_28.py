#!/usr/bin/env python3
"""Independent, data-only checker for the bounded Cycle-751 BINDER claim."""
from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import inspect
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Callable

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
)

TARGET_MODULE = "frontier_cycle751_binder_formation_attempt_2026_07_28"
FIXTURE_BANK_COUNTS = (2, 5, 12)
EXPECTED_EVENTS = 38
EXPECTED_SITES = 5_815
EXPECTED_LOCALITY_COMPARISONS = 220_970
EXPECTED_WRITES_AND_BINDINGS = 829
STDOUT_LIMIT_BYTES = 150 * 1024
SCOPE_LANGUAGE_VERBATIM = "three flags derived, ACTUAL standing; w3 open"

EXPECTED_SITE_CORRESPONDENCE = (
    "Cycle742-lineage embedding convention: K data wire w maps to "
    "R693.Record.site = K.M.R12.full_wire_layout()['wire_sites'][w]"
)
EXPECTED_SCOPE_CONDITIONS = (
    "bank_count in (2, 5, 12) and event in range(2 * bank_count)",
    "the initial persistent state is K.M.pack_state(*K.B.chain_genesis(bank_count))",
    "direction is (1, 0) for even event and (0, 1) for odd event",
    "prepared = K.M.prepare_endpoint(persistent_before, direction)",
    "post_state = K.run_orbit(prepared, K.interleaved_program(bank_count))[0]",
    "the event delta is persistent_before -> post_state",
    "wire w is the R693 record cell at K.M.R12.full_wire_layout()['wire_sites'][w]",
    "BINDER is evaluated after the orbit and before EventChain.admit",
    "certificate=actuality=admissibility=law_domain=1 remain supplied",
)
EXPECTED_NO_GO_DAYLIGHT = (
    "The construction stays inside the R-eta no-go daylight because site is "
    "fixed by the declared K-to-R693 embedding, content is computed from K's "
    "written post-state values, and association is computed from K's local "
    "delta-support touch relation. It is a dynamics-derived association, not "
    "a formation-existence selector, and it makes no R-eta claim."
)


@dataclass(frozen=True)
class OwnWrite:
    wire: int
    site: tuple[int, int, int]
    before: int
    after: int
    content: tuple[object, object, object, object]


@dataclass(frozen=True)
class OwnEvent:
    bank_count: int
    tick_id: int
    direction: tuple[int, int]
    delta_window: tuple[OwnWrite, ...]
    remote_context: str


@dataclass(frozen=True)
class OwnCell:
    wire: int
    record: R693.Record


@dataclass(frozen=True)
class OwnFamily:
    bank_count: int
    program_stations: int
    events: tuple[OwnEvent, ...]
    post_states: tuple[tuple[int, ...], ...]
    token_return_failures: int
    semantic_failures: int


def _stable_json(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def _digest(value: object) -> str:
    return sha256(_stable_json(value).encode()).hexdigest()


def _source_tree() -> ast.Module:
    """Read the blocklisted primary only as source data; never import it."""

    if TARGET_MODULE in sys.modules:
        raise AssertionError("Cycle 751 primary was imported")
    return ast.parse(Path(BLOCKLIST[0]).read_text(encoding="utf-8"))


def _assignment_node(tree: ast.Module, name: str) -> ast.expr:
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                return node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return node.value
    raise KeyError(("missing module assignment", name))


def _literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(_assignment_node(tree, name))


def _function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise KeyError(("missing function", name))


def _return_dict(function: ast.FunctionDef) -> dict[str, ast.expr]:
    candidates = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if not candidates:
        raise KeyError(("function has no dict return", function.name))
    dictionary = max(candidates, key=lambda item: len(item.keys))
    result: dict[str, ast.expr] = {}
    for key, value in zip(dictionary.keys, dictionary.values):
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            result[key.value] = value
    return result


def _literal_or_unparse(node: ast.expr) -> object:
    try:
        return ast.literal_eval(node)
    except (ValueError, TypeError):
        return ast.unparse(node)


def extraction() -> dict[str, object]:
    """AST-extract the blocklisted candidate, census routes, and boundaries."""

    tree = _source_tree()
    audit_node = _assignment_node(tree, "AUDIT_INPUT_PATHS")
    target_audit_inputs = ast.literal_eval(audit_node)
    target_timeout = _literal_assignment(tree, "AUDIT_TIMEOUT_SEC")
    target_note = _literal_assignment(tree, "NOTE_PATH")
    target_fixtures = _literal_assignment(tree, "FIXTURE_BANK_COUNTS")
    site_name = _literal_assignment(tree, "SITE_CORRESPONDENCE_NAME")
    scope_conditions = _literal_assignment(tree, "OUTCOME_A_CONDITIONS_VERBATIM")
    no_go_daylight = _literal_assignment(tree, "NO_GO_BOUNDARY")

    predicate = _function_node(tree, "BINDER_PREDICATE")
    predicate_attributes = {
        node.attr for node in ast.walk(predicate) if isinstance(node, ast.Attribute)
    }
    predicate_names = {
        node.id for node in ast.walk(predicate) if isinstance(node, ast.Name)
    }
    predicate_text = ast.unparse(predicate)
    predicate_is_delta_touch = (
        predicate_attributes == {"delta_window", "record", "site"}
        and "event.delta_window" in predicate_text
        and "write.site == cell.record.site" in predicate_text
        and not (
            predicate_names
            & {
                "K",
                "R693",
                "tick_id",
                "direction",
                "remote_context_digest",
                "persistent_before",
                "post_state",
                "site_table",
            }
        )
    )

    correspondence = _function_node(tree, "declared_site_correspondence")
    correspondence_returns = [
        ast.unparse(node.value)
        for node in ast.walk(correspondence)
        if isinstance(node, ast.Return) and node.value is not None
    ]
    declared_correspondence_is_index = correspondence_returns == ["site_table[wire]"]

    formation = _function_node(tree, "formation_event_from_k")
    formation_text = ast.unparse(formation)
    cells = _function_node(tree, "record_cells_for_state")
    cells_text = ast.unparse(cells)
    delta_construction_declared = all(
        text in formation_text
        for text in (
            "zip(persistent_before, post_state)",
            "if before != after",
            "site=declared_site_correspondence(wire, site_table)",
            "content=written_content(int(after))",
        )
    )
    cell_construction_declared = (
        "R693.Record" in cells_text
        and "site=declared_site_correspondence(wire, site_table)" in cells_text
        and "content=written_content(int(value))" in cells_text
    )

    locality_keys = set(_return_dict(_function_node(tree, "locality_certificate")))
    totality_keys = set(_return_dict(_function_node(tree, "totality_certificate")))
    identification = _function_node(tree, "identification_certificate")
    identification_map = _return_dict(identification)
    split_strings = [
        node.value
        for node in ast.walk(identification)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and node.value.startswith("No lawful pure-transport acceptance event")
    ]
    split_finding = split_strings[0] if len(split_strings) == 1 else ""
    census_routes_present = (
        {
            "remote_field_comparisons",
            "remote_field_disagreements",
            "local_window_removal_controls",
            "local_window_removal_controls_live",
        }
        <= locality_keys
        and {
            "events",
            "writes",
            "bindings",
            "relation_evaluations",
            "orphan_writes",
            "phantom_bindings",
            "duplicate_bindings",
            "support_mismatches",
        }
        <= totality_keys
        and {
            "acceptance_events",
            "real_write_events",
            "pure_transport_acceptance_events",
            "binder_ones",
            "binder_zeroes",
            "split_finding",
        }
        <= set(identification_map)
        and "all 38 full-orbit admit calls have real writes" in split_finding
    )

    main = _function_node(tree, "main")
    boundary_nodes = [
        node.value
        for node in ast.walk(main)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "boundary"
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    ]
    if len(boundary_nodes) != 1:
        raise AssertionError(("boundary dictionaries", len(boundary_nodes)))
    boundary_map: dict[str, ast.expr] = {}
    for key, value in zip(boundary_nodes[0].keys, boundary_nodes[0].values):
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            boundary_map[key.value] = value
    boundary_values = {
        key: _literal_or_unparse(boundary_map[key])
        for key in (
            "binder_fixture_closed",
            "binder_global_closed",
            "w3_closed",
            "forcing_key_active",
            "remaining_W3_supplies",
            "W5_permanent_Record_bridge_closed",
            "R_eta_selected",
        )
    }
    outcome_constants = {
        node.value
        for node in ast.walk(main)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    boundary_declared = (
        boundary_values
        == {
            "binder_fixture_closed": "fixture_derived",
            "binder_global_closed": False,
            "w3_closed": False,
            "forcing_key_active": "not fixture_derived",
            "remaining_W3_supplies": ("ACTUAL", "ADMISS", "LAW"),
            "W5_permanent_Record_bridge_closed": False,
            "R_eta_selected": False,
        }
        and "OUTCOME A — BINDER derived at fixture scope" in outcome_constants
    )

    supplier_map = _return_dict(_function_node(tree, "no_new_supplier_certificate"))
    no_go_key_declared = (
        ast.unparse(supplier_map["no_go_boundary"]) == "NO_GO_BOUNDARY"
        and ast.literal_eval(supplier_map["R_eta_selected"]) is False
        and ast.literal_eval(supplier_map["generic_Record_formation_existence_invoked"])
        is False
    )

    passed = all(
        (
            isinstance(audit_node, ast.Tuple),
            target_audit_inputs == AUDIT_INPUT_PATHS,
            target_timeout == AUDIT_TIMEOUT_SEC,
            target_note == NOTE_PATH,
            target_fixtures == FIXTURE_BANK_COUNTS,
            site_name == EXPECTED_SITE_CORRESPONDENCE,
            scope_conditions == EXPECTED_SCOPE_CONDITIONS,
            no_go_daylight == EXPECTED_NO_GO_DAYLIGHT,
            predicate_is_delta_touch,
            declared_correspondence_is_index,
            delta_construction_declared,
            cell_construction_declared,
            census_routes_present,
            boundary_declared,
            no_go_key_declared,
        )
    )
    return {
        "pass": passed,
        "candidate_definition": (
            "event.delta_window contains a write whose site equals cell.record.site"
        ),
        "declared_site_correspondence": correspondence_returns[0],
        "AUDIT_INPUT_PATHS_literal_tuple": isinstance(audit_node, ast.Tuple),
        "AUDIT_INPUT_PATHS": target_audit_inputs,
        "census_claims_extracted": {
            "locality_comparisons": EXPECTED_LOCALITY_COMPARISONS,
            "bindings": EXPECTED_WRITES_AND_BINDINGS,
            "controls": EXPECTED_EVENTS,
            "pure_transport_events": 0,
        },
        "split_finding": split_finding,
        "boundary": boundary_values,
        "outcome_A_present": (
            "OUTCOME A — BINDER derived at fixture scope" in outcome_constants
        ),
        "no_go_daylight_keyed": no_go_key_declared,
    }


def _written_content(value: int) -> tuple[object, object, object, object]:
    if value not in (0, 1):
        raise ValueError(("non-bit written value", value))
    return (R693.F(value), R693.F(0), R693.F(0), R693.F(0))


def _declared_site(
    wire: int, site_table: tuple[tuple[int, int, int], ...]
) -> tuple[int, int, int]:
    """Independent implementation of the extracted site-table correspondence."""

    return site_table[wire]


def _own_controller_step(
    data: tuple[int, ...],
    program: tuple[object, ...],
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    """Rebuild K's forward Q/R step directly from its landed local semantics."""

    output = data
    for station, active in enumerate(a_tokens):
        if active:
            output = K.A.apply_semantic(output, K.mapped_macro(program[station]))
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(len(program)):
        a[station], b[station] = b[station], a[station]
    for station in range(len(program)):
        target = (station + 1) % len(program)
        b[station], a[target] = a[target], b[station]
    return output, tuple(a), tuple(b)


def _own_orbit(
    state: tuple[int, ...], program: tuple[object, ...]
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    a_tokens = (1,) + (0,) * (len(program) - 1)
    b_tokens = (0,) * len(program)
    output = state
    for _step in range(len(program)):
        output, a_tokens, b_tokens = _own_controller_step(
            output, program, a_tokens, b_tokens
        )
    return output, a_tokens, b_tokens


def _own_event(
    bank_count: int,
    tick_id: int,
    direction: tuple[int, int],
    persistent_before: tuple[int, ...],
    post_state: tuple[int, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> OwnEvent:
    if not (
        len(persistent_before) == len(post_state) == len(site_table)
    ):
        raise ValueError("state/site width mismatch")
    window = tuple(
        OwnWrite(
            wire=wire,
            site=_declared_site(wire, site_table),
            before=int(before),
            after=int(after),
            content=_written_content(int(after)),
        )
        for wire, (before, after) in enumerate(zip(persistent_before, post_state))
        if before != after
    )
    remote = _digest(
        (
            bank_count,
            tick_id,
            direction,
            sum(persistent_before),
            sum(post_state),
        )
    )
    return OwnEvent(bank_count, tick_id, direction, window, remote)


def _record_cells(
    state: tuple[int, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> tuple[OwnCell, ...]:
    return tuple(
        OwnCell(
            wire=wire,
            record=R693.Record(
                site=_declared_site(wire, site_table),
                content=_written_content(int(value)),
            ),
        )
        for wire, value in enumerate(state)
    )


def _own_binder_predicate(event: OwnEvent, cell: OwnCell) -> int:
    """Independent BINDER: one exactly on a delta-support/site touch."""

    return int(
        any(write.site == cell.record.site for write in event.delta_window)
    )


def _own_event_binder(event: OwnEvent, cells: tuple[OwnCell, ...]) -> int:
    return int(any(_own_binder_predicate(event, cell) for cell in cells))


def _build_families() -> tuple[
    tuple[tuple[int, int, int], ...], tuple[OwnFamily, ...]
]:
    layout = K.M.R12.full_wire_layout()
    site_table = tuple(tuple(site) for site in layout["wire_sites"])
    families: list[OwnFamily] = []
    for bank_count in FIXTURE_BANK_COUNTS:
        program = K.interleaved_program(bank_count)
        banks, links = K.B.chain_genesis(bank_count)
        persistent = K.M.pack_state(banks, links)
        events: list[OwnEvent] = []
        post_states: list[tuple[int, ...]] = []
        token_failures = semantic_failures = 0
        for tick_id in range(2 * bank_count):
            direction = (1, 0) if tick_id % 2 == 0 else (0, 1)
            prepared = K.M.prepare_endpoint(persistent, direction)
            post_state, a_tokens, b_tokens = _own_orbit(prepared, program)
            expected = K.A.apply_semantic(
                prepared, K.M.global_allocator_word(bank_count)
            )
            semantic_failures += post_state != expected
            token_failures += (
                a_tokens != (1,) + (0,) * (len(program) - 1)
                or any(b_tokens)
            )
            events.append(
                _own_event(
                    bank_count,
                    tick_id,
                    direction,
                    persistent,
                    post_state,
                    site_table,
                )
            )
            post_states.append(post_state)
            persistent = post_state
        families.append(
            OwnFamily(
                bank_count=bank_count,
                program_stations=len(program),
                events=tuple(events),
                post_states=tuple(post_states),
                token_return_failures=token_failures,
                semantic_failures=semantic_failures,
            )
        )
    return site_table, tuple(families)


def candidate_recount() -> dict[str, object]:
    """Independently recount locality, totality, and the delta-touch relation."""

    site_table, families = _build_families()
    comparisons = disagreements = controls = live_controls = 0
    events = writes = bindings = relation_evaluations = 0
    orphans = phantoms = duplicates = support_mismatches = 0
    content_mismatches = readout_mismatches = binder_zeroes = 0
    association_rows: list[object] = []
    by_family: dict[int, dict[str, int]] = {}

    for family in families:
        family_writes = family_bindings = 0
        for event, post_state in zip(family.events, family.post_states):
            cells = _record_cells(post_state, site_table)
            remote_variant = OwnEvent(
                bank_count=event.bank_count + 1_000,
                tick_id=event.tick_id + 10_000,
                direction=tuple(reversed(event.direction)),
                delta_window=event.delta_window,
                remote_context="adversarial-remote-mutation",
            )
            for cell in cells:
                comparisons += 1
                disagreements += (
                    _own_binder_predicate(event, cell)
                    != _own_binder_predicate(remote_variant, cell)
                )

            controls += 1
            if event.delta_window:
                removed = event.delta_window[0]
                removed_variant = OwnEvent(
                    event.bank_count,
                    event.tick_id,
                    event.direction,
                    event.delta_window[1:],
                    event.remote_context,
                )
                live_controls += (
                    _own_binder_predicate(event, cells[removed.wire]) == 1
                    and _own_binder_predicate(
                        removed_variant, cells[removed.wire]
                    )
                    == 0
                )

            support = {write.site for write in event.delta_window}
            bound = tuple(
                cell
                for cell in cells
                if _own_binder_predicate(event, cell)
            )
            relation_evaluations += len(cells)
            events += 1
            writes += len(event.delta_window)
            bindings += len(bound)
            family_writes += len(event.delta_window)
            family_bindings += len(bound)
            binder_zeroes += _own_event_binder(event, cells) == 0
            bound_sites = {cell.record.site for cell in bound}
            support_mismatches += bound_sites != support
            phantoms += sum(cell.record.site not in support for cell in bound)
            for write in event.delta_window:
                matches = tuple(
                    cell for cell in bound if cell.record.site == write.site
                )
                orphans += not matches
                duplicates += len(matches) != 1
                if len(matches) == 1:
                    content_mismatches += (
                        matches[0].record.content != write.content
                    )
            expected_readout = sum(
                (R693.F(write.after) for write in event.delta_window),
                R693.F(0),
            )
            observed_readout = R693.record_readout(
                tuple(cell.record for cell in bound)
            )
            readout_mismatches += observed_readout != expected_readout
            association_rows.append(
                (
                    family.bank_count,
                    event.tick_id,
                    tuple(write.wire for write in event.delta_window),
                    tuple(cell.wire for cell in bound),
                )
            )
        by_family[family.bank_count] = {
            "events": len(family.events),
            "writes": family_writes,
            "bindings": family_bindings,
        }

    token_failures = sum(family.token_return_failures for family in families)
    semantic_failures = sum(family.semantic_failures for family in families)
    passed = (
        len(site_table) == EXPECTED_SITES
        and len(set(site_table)) == EXPECTED_SITES
        and events == EXPECTED_EVENTS
        and comparisons == relation_evaluations == EXPECTED_LOCALITY_COMPARISONS
        and disagreements == 0
        and controls == live_controls == EXPECTED_EVENTS
        and writes == bindings == EXPECTED_WRITES_AND_BINDINGS
        and (orphans, phantoms, duplicates, support_mismatches) == (0, 0, 0, 0)
        and content_mismatches == readout_mismatches == binder_zeroes == 0
        and token_failures == semantic_failures == 0
        and by_family
        == {
            2: {"events": 4, "writes": 89, "bindings": 89},
            5: {"events": 10, "writes": 218, "bindings": 218},
            12: {"events": 24, "writes": 522, "bindings": 522},
        }
    )
    return {
        "pass": passed,
        "sites": len(site_table),
        "events": events,
        "locality_comparisons": comparisons,
        "locality_disagreements": disagreements,
        "delta_removal_controls": controls,
        "live_delta_removal_controls": live_controls,
        "writes": writes,
        "bindings": bindings,
        "orphans": orphans,
        "phantoms": phantoms,
        "duplicates": duplicates,
        "support_mismatches": support_mismatches,
        "content_mismatches": content_mismatches,
        "readout_mismatches": readout_mismatches,
        "binder_zeroes": binder_zeroes,
        "controller_semantic_failures": semantic_failures,
        "controller_token_return_failures": token_failures,
        "by_family": by_family,
        "association_sha256": _digest(association_rows),
    }


def transport_probe() -> dict[str, object]:
    """Search every held lawful acceptance event for an empty write delta."""

    _site_table, families = _build_families()
    accepted = real_writes = pure_transports = status_failures = 0
    frozen_counterexamples: list[object] = []
    by_family: dict[int, dict[str, int]] = {}
    for family in families:
        chain = K.B.C704.C610.EventChain(bank=2 * family.bank_count)
        family_accepted = family_real = family_transport = 0
        for event, post_state in zip(family.events, family.post_states):
            orientation = 1 if event.direction == (1, 0) else -1
            status = chain.admit(
                tick_id=event.tick_id,
                orientation=orientation,
                certificate=1,
                binder=1,
                actuality=1,
                admissibility=1,
                law_domain=1,
            )
            lawful = status == "admitted"
            status_failures += not lawful
            accepted += lawful
            family_accepted += lawful
            if lawful and event.delta_window:
                real_writes += 1
                family_real += 1
            elif lawful:
                pure_transports += 1
                family_transport += 1
                frozen_counterexamples.append(
                    {
                        "bank_count": family.bank_count,
                        "tick_id": event.tick_id,
                        "direction": event.direction,
                        "delta_writes": 0,
                        "post_state_sha256": sha256(bytes(post_state)).hexdigest(),
                    }
                )
        by_family[family.bank_count] = {
            "accepted": family_accepted,
            "real_write_events": family_real,
            "pure_transport_events": family_transport,
        }
    passed = (
        accepted == real_writes == EXPECTED_EVENTS
        and pure_transports == status_failures == 0
        and not frozen_counterexamples
    )
    return {
        "pass": passed,
        "sweep": "all held 2/5/12 full-orbit acceptance events",
        "accepted_events": accepted,
        "real_write_events": real_writes,
        "pure_transport_acceptance_events": pure_transports,
        "status_failures": status_failures,
        "frozen_counterexamples": frozen_counterexamples,
        "by_family": by_family,
        "verdict": (
            "ABSENT: no lawful empty-delta acceptance event"
            if not frozen_counterexamples
            else "FOUND: frozen empty-delta lawful counterexample"
        ),
    }


def _own_binder_admit_adapter(
    chain: object,
    event: OwnEvent,
    cells: tuple[OwnCell, ...],
    orientation: int,
) -> str:
    return chain.admit(
        tick_id=event.tick_id,
        orientation=orientation,
        certificate=1,
        binder=_own_event_binder(event, cells),
        actuality=1,
        admissibility=1,
        law_domain=1,
    )


def adapter_recount() -> dict[str, object]:
    """Run an independent predicate adapter and compare complete lawful traces."""

    site_table, families = _build_families()
    status_mismatches = row_mismatches = logical_failures = 0
    derived_binder_zeroes = 0
    by_family: dict[int, dict[str, object]] = {}
    for family in families:
        supplied_chain = K.B.C704.C610.EventChain(bank=2 * family.bank_count)
        derived_chain = K.B.C704.C610.EventChain(bank=2 * family.bank_count)
        supplied_trace: list[object] = []
        derived_trace: list[object] = []
        for event, post_state in zip(family.events, family.post_states):
            orientation = 1 if event.direction == (1, 0) else -1
            cells = _record_cells(post_state, site_table)
            binder = _own_event_binder(event, cells)
            derived_binder_zeroes += binder == 0
            supplied_status = supplied_chain.admit(
                tick_id=event.tick_id,
                orientation=orientation,
                certificate=1,
                binder=1,
                actuality=1,
                admissibility=1,
                law_domain=1,
            )
            derived_status = _own_binder_admit_adapter(
                derived_chain, event, cells, orientation
            )
            supplied_rows = K.B.cell_rows(supplied_chain)
            derived_rows = K.B.cell_rows(derived_chain)
            status_mismatches += supplied_status != derived_status
            row_mismatches += supplied_rows != derived_rows
            banks, links = K.M.unpack_state(post_state, family.bank_count)
            decoded, _order = K.B.decode_local_graph(banks, links)
            logical_failures += (
                derived_status != "admitted"
                or K.B.cell_rows(decoded) != derived_rows
            )
            supplied_trace.append((supplied_status, supplied_rows))
            derived_trace.append((derived_status, derived_rows))
        supplied_bytes = _stable_json(supplied_trace).encode()
        derived_bytes = _stable_json(derived_trace).encode()
        by_family[family.bank_count] = {
            "events": len(family.events),
            "byte_exact": supplied_bytes == derived_bytes,
            "supplied_trace_bytes": len(supplied_bytes),
            "derived_trace_bytes": len(derived_bytes),
            "trace_sha256": sha256(derived_bytes).hexdigest(),
        }

    blank_state = families[0].post_states[-1]
    blank_cells = _record_cells(blank_state, site_table)
    empty_event = OwnEvent(
        bank_count=2,
        tick_id=0,
        direction=(1, 0),
        delta_window=(),
        remote_context="independent-empty-delta-control",
    )
    derived_control_chain = K.B.C704.C610.EventChain(bank=4)
    supplied_control_chain = K.B.C704.C610.EventChain(bank=4)
    derived_control_status = _own_binder_admit_adapter(
        derived_control_chain, empty_event, blank_cells, 1
    )
    supplied_control_status = supplied_control_chain.admit(
        tick_id=0,
        orientation=1,
        certificate=1,
        binder=1,
        actuality=1,
        admissibility=1,
        law_domain=1,
    )
    control = {
        "lawful_fixture_member": False,
        "delta_writes": 0,
        "derived_binder": _own_event_binder(empty_event, blank_cells),
        "derived_status": derived_control_status,
        "supplied_literal_one_status": supplied_control_status,
        "behavior_delta": derived_control_status != supplied_control_status,
        "derived_rows": K.B.cell_rows(derived_control_chain),
        "supplied_rows": K.B.cell_rows(supplied_control_chain),
    }
    passed = (
        status_mismatches == row_mismatches == logical_failures == 0
        and derived_binder_zeroes == 0
        and sum(row["events"] for row in by_family.values()) == EXPECTED_EVENTS
        and all(row["byte_exact"] for row in by_family.values())
        and control["derived_binder"] == 0
        and control["derived_status"] == "no_opportunity"
        and control["supplied_literal_one_status"] == "admitted"
        and control["behavior_delta"]
    )
    return {
        "pass": passed,
        "status_mismatches": status_mismatches,
        "cell_row_mismatches": row_mismatches,
        "logical_trace_failures": logical_failures,
        "derived_binder_zeroes_on_lawful_events": derived_binder_zeroes,
        "all_lawful_traces_byte_exact": all(
            row["byte_exact"] for row in by_family.values()
        ),
        "by_family": by_family,
        "empty_delta_control": control,
    }


def no_new_supplier_audit() -> dict[str, object]:
    """Locate the R-eta daylight and reject executable formation selectors."""

    tree = _source_tree()
    repo_imports = tuple(
        sorted(
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
            if alias.name.startswith("frontier_")
            or alias.name.startswith("physical_record_")
        )
    )
    expected_imports = (
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        "physical_record_readout_carrier_three_way_split_cycle693_2026_07_25",
    )
    forbidden_selectors = {
        "records_form",
        "record_formation_exists",
        "formation_existence_selector",
    }
    executable_identifiers = {
        node.id for node in ast.walk(tree) if isinstance(node, ast.Name)
    } | {
        node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
    }
    selector_identifiers = tuple(
        sorted(executable_identifiers & forbidden_selectors)
    )
    selector_calls = tuple(
        sorted(
            ast.unparse(node.func)
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and (
                ast.unparse(node.func).lower() in forbidden_selectors
                or ast.unparse(node.func).lower().split(".")[-1]
                in forbidden_selectors
            )
        )
    )
    dynamic_import_calls = tuple(
        sorted(
            ast.unparse(node.func)
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and ast.unparse(node.func) in {"__import__", "importlib.import_module"}
        )
    )
    no_go_daylight = _literal_assignment(tree, "NO_GO_BOUNDARY")
    supplier_map = _return_dict(_function_node(tree, "no_new_supplier_certificate"))
    keyed_daylight = (
        ast.unparse(supplier_map["no_go_boundary"]) == "NO_GO_BOUNDARY"
        and ast.literal_eval(supplier_map["R_eta_selected"]) is False
        and ast.literal_eval(supplier_map["site_computed_from_delta_support"])
        is True
        and ast.literal_eval(supplier_map["content_computed_from_written_values"])
        is True
        and ast.literal_eval(supplier_map["association_computed_from_touch_relation"])
        is True
        and ast.literal_eval(supplier_map["generic_Record_formation_existence_invoked"])
        is False
    )
    passed = (
        repo_imports == expected_imports
        and not selector_identifiers
        and not selector_calls
        and not dynamic_import_calls
        and no_go_daylight == EXPECTED_NO_GO_DAYLIGHT
        and "dynamics-derived association" in no_go_daylight
        and "not a formation-existence selector" in no_go_daylight
        and keyed_daylight
        and TARGET_MODULE not in sys.modules
    )
    return {
        "pass": passed,
        "repo_imports": repo_imports,
        "executable_formation_selector_identifiers": selector_identifiers,
        "formation_selector_calls": selector_calls,
        "dynamic_import_calls": dynamic_import_calls,
        "R_eta_daylight_located_in_primary_key": keyed_daylight,
        "dynamics_derived_association": (
            "dynamics-derived association" in no_go_daylight
        ),
        "R_eta_selected": False,
        "primary_imported": TARGET_MODULE in sys.modules,
    }


def discipline(extracted: dict[str, object]) -> dict[str, object]:
    """Check blocklist separation and the candidate's verbatim scope firewall."""

    held_tree = ast.parse(inspect.getsource(K.held_certificate))
    admit_calls = [
        node
        for node in ast.walk(held_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "admit"
    ]
    held_keywords = (
        {
            keyword.arg: _literal_or_unparse(keyword.value)
            for keyword in admit_calls[0].keywords
        }
        if len(admit_calls) == 1
        else {}
    )
    blocklist_clean = (
        set(AUDIT_INPUT_PATHS).isdisjoint(BLOCKLIST)
        and TARGET_MODULE not in sys.modules
        and tuple(module.__name__ for module in (K, R693))
        == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
            "physical_record_readout_carrier_three_way_split_cycle693_2026_07_25",
        )
    )
    boundary = extracted.get("boundary", {})
    scope_firewall = (
        extracted.get("outcome_A_present") is True
        and isinstance(boundary, dict)
        and boundary.get("binder_fixture_closed") == "fixture_derived"
        and boundary.get("binder_global_closed") is False
        and boundary.get("w3_closed") is False
        and boundary.get("remaining_W3_supplies")
        == ("ACTUAL", "ADMISS", "LAW")
        and len(boundary.get("remaining_W3_supplies", ())) == 3
        and "ACTUAL" in boundary.get("remaining_W3_supplies", ())
    )
    landed_call_scope = (
        len(admit_calls) == 1
        and held_keywords.get("binder") == 1
        and all(
            held_keywords.get(name) == 1
            for name in ("certificate", "actuality", "admissibility", "law_domain")
        )
    )
    record_shape = tuple(R693.Record.__dataclass_fields__) == ("site", "content")
    passed = (
        AUDIT_TIMEOUT_SEC == 900
        and NOTE_PATH
        == "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
        )
        and BLOCKLIST
        == (
            "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
        )
        and blocklist_clean
        and scope_firewall
        and landed_call_scope
        and record_shape
    )
    return {
        "pass": passed,
        "blocklist_clean": blocklist_clean,
        "scope_language_verbatim": SCOPE_LANGUAGE_VERBATIM,
        "three_standing_flags": boundary.get("remaining_W3_supplies")
        if isinstance(boundary, dict)
        else None,
        "ACTUAL_standing": (
            isinstance(boundary, dict)
            and "ACTUAL" in boundary.get("remaining_W3_supplies", ())
        ),
        "w3_open": (
            isinstance(boundary, dict) and boundary.get("w3_closed") is False
        ),
        "fixture_scope_derived": (
            isinstance(boundary, dict)
            and boundary.get("binder_fixture_closed") == "fixture_derived"
        ),
        "landed_admit_literal_scope": landed_call_scope,
        "R693_Record_fields": tuple(R693.Record.__dataclass_fields__),
    }


def _guarded(
    label: str, function: Callable[[], dict[str, object]]
) -> tuple[str, dict[str, object]]:
    try:
        result = function()
        if not isinstance(result, dict) or "pass" not in result:
            raise TypeError("certificate did not return a pass-bearing dictionary")
        result["pass"] = bool(result["pass"])
        return label, result
    except Exception as exc:  # honest FAIL receipt instead of an early crash
        return label, {
            "pass": False,
            "error_type": type(exc).__name__,
            "error": str(exc),
        }


def main() -> int:
    started = perf_counter()
    reports: dict[str, dict[str, object]] = {}

    label, extracted = _guarded("extraction", extraction)
    reports[label] = extracted
    for label, function in (
        ("candidate_recount", candidate_recount),
        ("transport_probe", transport_probe),
        ("adapter_recount", adapter_recount),
        ("no_new_supplier_audit", no_new_supplier_audit),
    ):
        name, result = _guarded(label, function)
        reports[name] = result

    name, result = _guarded(
        "discipline", lambda: discipline(reports["extraction"])
    )
    reports[name] = result

    elapsed = perf_counter() - started
    timeout_clean = elapsed < AUDIT_TIMEOUT_SEC
    all_pass = all(report["pass"] for report in reports.values()) and timeout_clean
    summary: dict[str, object] = {
        "cycle": 751,
        "independent_check": True,
        "candidate_executed_or_imported": TARGET_MODULE in sys.modules,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_seconds": round(elapsed, 6),
        "timeout_clean": timeout_clean,
        "reports": reports,
        "checks_passed": sum(report["pass"] for report in reports.values()),
        "checks_failed": sum(not report["pass"] for report in reports.values()),
        "pass": all_pass,
        "terminal": (
            "CYCLE751_BINDER_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE751_BINDER_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    summary["report_sha256"] = _digest(summary)
    lines = [
        "{} {} :: {}".format(
            "PASS" if report["pass"] else "FAIL",
            label,
            _stable_json(report),
        )
        for label, report in reports.items()
    ]
    lines.append("SUMMARY_JSON " + _stable_json(summary))
    lines.append(str(summary["terminal"]))
    text = "\n".join(lines) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "pass": False,
            "reason": "stdout bound exceeded before emission",
            "computed_bytes": len(text.encode()),
            "limit_bytes": STDOUT_LIMIT_BYTES,
            "runtime_seconds": round(elapsed, 6),
        }
        sys.stdout.write(
            "FAIL OUTPUT_stdout_under_150KB :: "
            + _stable_json(fallback)
            + "\nCYCLE751_BINDER_INDEPENDENT_CHECK_HONEST_FAIL\n"
        )
        return 1
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
