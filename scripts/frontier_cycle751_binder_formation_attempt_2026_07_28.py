#!/usr/bin/env python3
"""Cycle 751: bounded BINDER formation-surface attempt.

On the landed Cycle-719 lawful fixture families, an accepted event is the
complete persistent-state transition surrounding one controller orbit.  Its
local delta window is the support and written values of that transition.  The
declared Cycle-742-lineage embedding sends K data wire ``w`` to the R693 Record
cell at K's already-landed physical site for ``w``.  The candidate binds an
event to exactly those cells whose sites occur in its delta window.

This is a fixture-scope event-to-record update association.  It is not an
inference from the bare sentence "Records form", a permanent-Record bridge, an
occurrence rule, a Born rule, or an R-eta selector.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import inspect
import json
import sys
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import physical_record_readout_carrier_three_way_split_cycle693_2026_07_25 as R693


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BINDER_FORMATION_ATTEMPT_CYCLE751_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/physical_record_readout_carrier_three_way_split_cycle693_2026_07_25.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FIXTURE_BANK_COUNTS = (2, 5, 12)
STDOUT_LIMIT_BYTES = 150 * 1024
ZERO_CONTENT = (R693.F(0), R693.F(0), R693.F(0), R693.F(0))

SITE_CORRESPONDENCE_NAME = (
    "Cycle742-lineage embedding convention: K data wire w maps to "
    "R693.Record.site = K.M.R12.full_wire_layout()['wire_sites'][w]"
)
DELTA_BOUNDARY = (
    "the event delta is previous persistent K state -> post-orbit K state; "
    "endpoint preparation is inside the event and is not itself a retained write"
)
NO_GO_BOUNDARY = (
    "The construction stays inside the R-eta no-go daylight because site is "
    "fixed by the declared K-to-R693 embedding, content is computed from K's "
    "written post-state values, and association is computed from K's local "
    "delta-support touch relation. It is a dynamics-derived association, not "
    "a formation-existence selector, and it makes no R-eta claim."
)
MINIMAL_BINDER_CONTENT = (
    "For every candidate physical event and record cell, a state-local binding "
    "predicate is fixed, and BINDER=1 exactly when that event physically forms "
    "or updates that cell's record."
)
OUTCOME_A_CONDITIONS_VERBATIM = (
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

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool, detail: object = "") -> bool:
    """Record one unique stdout-bounded PASS/FAIL line."""

    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    suffix = "" if detail == "" else f" {detail}"
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}{suffix}"
    )
    return passed


def stable_json(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(stable_json(value).encode()).hexdigest()


def written_content(value: int) -> tuple[object, object, object, object]:
    """Inject the written K bit into the landed R693 matrix-content slot."""

    if value not in (0, 1):
        raise ValueError(("not a K bit", value))
    return (R693.F(value), R693.F(0), R693.F(0), R693.F(0))


def declared_site_correspondence(
    wire: int, site_table: tuple[tuple[int, int, int], ...]
) -> tuple[int, int, int]:
    """The one declared Cycle-742-lineage site correspondence."""

    return site_table[wire]


@dataclass(frozen=True)
class DeltaWrite:
    """One member of the event's local post-state delta window."""

    wire: int
    site: tuple[int, int, int]
    before: int
    after: int
    content: tuple[object, object, object, object]


@dataclass(frozen=True)
class LocalEvent:
    """Only delta_window is visible to BINDER_PREDICATE."""

    tick_id: int
    direction: tuple[int, int]
    delta_window: tuple[DeltaWrite, ...]
    remote_context_digest: str


@dataclass(frozen=True)
class RecordCell:
    """A K register site represented using the landed R693 Record structure."""

    wire: int
    record: R693.Record


@dataclass(frozen=True)
class LawfulFamily:
    bank_count: int
    program_stations: int
    events: tuple[LocalEvent, ...]
    post_states: tuple[tuple[int, ...], ...]
    prepared_support_sizes: tuple[int, ...]


def BINDER_PREDICATE(event: LocalEvent, cell: RecordCell) -> int:
    """One iff the event's local delta support touches this record cell."""

    return int(
        any(write.site == cell.record.site for write in event.delta_window)
    )


def EVENT_BINDER_VALUE(
    event: LocalEvent, cells: tuple[RecordCell, ...]
) -> int:
    """Scalar adapter value: the event binds at least one updated cell."""

    return int(any(BINDER_PREDICATE(event, cell) for cell in cells))


def formation_event_from_k(
    tick_id: int,
    direction: tuple[int, int],
    persistent_before: tuple[int, ...],
    post_state: tuple[int, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> LocalEvent:
    """Compute the local formation window from K's own transition result."""

    if len(persistent_before) != len(post_state) or len(post_state) != len(site_table):
        raise ValueError(
            ("formation widths", len(persistent_before), len(post_state), len(site_table))
        )
    window = tuple(
        DeltaWrite(
            wire=wire,
            site=declared_site_correspondence(wire, site_table),
            before=int(before),
            after=int(after),
            content=written_content(int(after)),
        )
        for wire, (before, after) in enumerate(
            zip(persistent_before, post_state)
        )
        if before != after
    )
    remote = digest(
        {
            "tick_id": tick_id,
            "direction": direction,
            "persistent_weight": sum(persistent_before),
            "post_weight": sum(post_state),
        }
    )
    return LocalEvent(tick_id, direction, window, remote)


def record_cells_for_state(
    state: tuple[int, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> tuple[RecordCell, ...]:
    """Represent every landed K register as an updated R693 record cell."""

    return tuple(
        RecordCell(
            wire=wire,
            record=R693.Record(
                site=declared_site_correspondence(wire, site_table),
                content=written_content(int(value)),
            ),
        )
        for wire, value in enumerate(state)
    )


def lawful_fixture_family(
    bank_count: int,
    site_table: tuple[tuple[int, int, int], ...],
) -> LawfulFamily:
    """Exhaust the landed K acceptance-event family at one held size."""

    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    persistent = K.M.pack_state(banks, links)
    events: list[LocalEvent] = []
    post_states: list[tuple[int, ...]] = []
    prepared_support_sizes: list[int] = []
    for tick_id in range(2 * bank_count):
        direction = (1, 0) if tick_id % 2 == 0 else (0, 1)
        prepared = K.M.prepare_endpoint(persistent, direction)
        post_state, _a, _b, _trace = K.run_orbit(prepared, program)
        event = formation_event_from_k(
            tick_id, direction, persistent, post_state, site_table
        )
        events.append(event)
        post_states.append(post_state)
        prepared_support_sizes.append(
            sum(left != right for left, right in zip(persistent, prepared))
        )
        persistent = post_state
    return LawfulFamily(
        bank_count=bank_count,
        program_stations=len(program),
        events=tuple(events),
        post_states=tuple(post_states),
        prepared_support_sizes=tuple(prepared_support_sizes),
    )


def anchor_certificate(
    site_table: tuple[tuple[int, int, int], ...],
    families: tuple[LawfulFamily, ...],
) -> dict[str, object]:
    """Pin the landed call site, fixture cardinalities, and R693 cell shape."""

    held_tree = ast.parse(inspect.getsource(K.held_certificate))
    admit_calls = tuple(
        node
        for node in ast.walk(held_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "admit"
    )
    keyword_values = tuple(
        {
            keyword.arg: ast.unparse(keyword.value)
            for keyword in call.keywords
        }
        for call in admit_calls
    )
    supplied_binder_literals = sum(
        values.get("binder") == "1" for values in keyword_values
    )
    fixture_counts = {
        family.bank_count: len(family.events) for family in families
    }
    return {
        "K_admit_calls_in_held_certificate": len(admit_calls),
        "K_admit_keyword_values": keyword_values,
        "K_supplied_binder_literal_one_calls": supplied_binder_literals,
        "fixture_event_counts": fixture_counts,
        "expected_fixture_event_counts": {2: 4, 5: 10, 12: 24},
        "fixture_program_stations": {
            family.bank_count: family.program_stations for family in families
        },
        "expected_fixture_program_stations": {2: 11, 5: 35, 12: 91},
        "R693_Record_fields": tuple(R693.Record.__dataclass_fields__),
        "R693_content_determinacy_probe": (
            R693.record_readout(
                (
                    R693.Record((0, 0, 0), written_content(1)),
                    R693.Record((3, 0, 0), written_content(0)),
                )
            )
            == R693.F(1)
        ),
        "site_table_width": len(site_table),
        "unique_sites": len(set(site_table)),
        "K_layout_module_collisions": K.M.R12.full_wire_layout()[
            "module_collisions"
        ],
        "K_layout_source_collisions": K.M.R12.full_wire_layout()[
            "source_collisions"
        ],
        "pass": (
            len(admit_calls) == 1
            and supplied_binder_literals == 1
            and keyword_values[0].get("certificate") == "1"
            and keyword_values[0].get("actuality") == "1"
            and keyword_values[0].get("admissibility") == "1"
            and keyword_values[0].get("law_domain") == "1"
            and fixture_counts == {2: 4, 5: 10, 12: 24}
            and {
                family.bank_count: family.program_stations
                for family in families
            }
            == {2: 11, 5: 35, 12: 91}
            and tuple(R693.Record.__dataclass_fields__) == ("site", "content")
            and R693.record_readout(
                (
                    R693.Record((0, 0, 0), written_content(1)),
                    R693.Record((3, 0, 0), written_content(0)),
                )
            )
            == R693.F(1)
            and len(site_table) == len(set(site_table))
            and K.M.R12.full_wire_layout()["module_collisions"] == 0
            and K.M.R12.full_wire_layout()["source_collisions"] == 0
        ),
    }


def candidate_ast_certificate() -> dict[str, object]:
    """Audit locality plus the landed K/R693 construction callables by AST."""

    predicate_tree = ast.parse(inspect.getsource(BINDER_PREDICATE))
    predicate_attributes = tuple(
        sorted(
            {
                node.attr
                for node in ast.walk(predicate_tree)
                if isinstance(node, ast.Attribute)
            }
        )
    )
    predicate_names = tuple(
        sorted(
            {
                node.id
                for node in ast.walk(predicate_tree)
                if isinstance(node, ast.Name)
            }
        )
    )
    forbidden_predicate_names = tuple(
        sorted(
            set(predicate_names)
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

    family_tree = ast.parse(inspect.getsource(lawful_fixture_family))
    family_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in ast.walk(family_tree)
                if isinstance(node, ast.Call)
            }
        )
    )
    event_tree = ast.parse(inspect.getsource(formation_event_from_k))
    event_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in ast.walk(event_tree)
                if isinstance(node, ast.Call)
            }
        )
    )
    cell_tree = ast.parse(inspect.getsource(record_cells_for_state))
    cell_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in ast.walk(cell_tree)
                if isinstance(node, ast.Call)
            }
        )
    )
    landed_required = {
        "K.interleaved_program",
        "K.B.chain_genesis",
        "K.M.pack_state",
        "K.M.prepare_endpoint",
        "K.run_orbit",
    }
    return {
        "predicate_attributes": predicate_attributes,
        "predicate_names": predicate_names,
        "forbidden_predicate_names": forbidden_predicate_names,
        "family_calls": family_calls,
        "formation_event_calls": event_calls,
        "record_cell_calls": cell_calls,
        "landed_K_calls_present": sorted(landed_required & set(family_calls)),
        "site_correspondence_calls": event_calls.count(
            "declared_site_correspondence"
        )
        + cell_calls.count("declared_site_correspondence"),
        "R693_Record_constructor_present": "R693.Record" in cell_calls,
        "candidate_definition": (
            "BINDER_PREDICATE(event, cell) = 1 iff a member of "
            "event.delta_window has site == cell.record.site"
        ),
        "site_correspondence": SITE_CORRESPONDENCE_NAME,
        "pass": (
            not forbidden_predicate_names
            and set(predicate_attributes) == {"delta_window", "record", "site"}
            and landed_required <= set(family_calls)
            and "declared_site_correspondence" in event_calls
            and "declared_site_correspondence" in cell_calls
            and "R693.Record" in cell_calls
        ),
    }


def locality_certificate(
    families: tuple[LawfulFamily, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    """Behaviorally vary every non-window field and retain every verdict."""

    comparisons = disagreements = live_mutations = 0
    for family in families:
        for event, post_state in zip(family.events, family.post_states):
            cells = record_cells_for_state(post_state, site_table)
            remote_variant = LocalEvent(
                tick_id=event.tick_id + 10_000,
                direction=tuple(reversed(event.direction)),
                delta_window=event.delta_window,
                remote_context_digest="changed-outside-local-window",
            )
            for cell in cells:
                comparisons += 1
                disagreements += (
                    BINDER_PREDICATE(event, cell)
                    != BINDER_PREDICATE(remote_variant, cell)
                )
            if event.delta_window:
                removed = event.delta_window[0]
                local_variant = LocalEvent(
                    tick_id=event.tick_id,
                    direction=event.direction,
                    delta_window=event.delta_window[1:],
                    remote_context_digest=event.remote_context_digest,
                )
                removed_cell = cells[removed.wire]
                live_mutations += (
                    BINDER_PREDICATE(event, removed_cell) == 1
                    and BINDER_PREDICATE(local_variant, removed_cell) == 0
                )
    total_events = sum(len(family.events) for family in families)
    return {
        "families": len(families),
        "events": total_events,
        "remote_field_comparisons": comparisons,
        "remote_field_disagreements": disagreements,
        "local_window_removal_controls": total_events,
        "local_window_removal_controls_live": live_mutations,
        "pass": (
            comparisons > 0
            and disagreements == 0
            and live_mutations == total_events
        ),
    }


def totality_certificate(
    families: tuple[LawfulFamily, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    """Exhaust no-orphan, no-phantom, unique-site, and written-content claims."""

    rows: dict[int, dict[str, object]] = {}
    total_events = total_writes = total_bindings = 0
    orphan_writes = phantom_bindings = duplicate_bindings = 0
    content_mismatches = support_mismatches = readout_mismatches = 0
    relation_evaluations = 0
    association_digest_rows: list[object] = []
    for family in families:
        family_writes = family_bindings = 0
        write_counts: list[int] = []
        for event, post_state in zip(family.events, family.post_states):
            cells = record_cells_for_state(post_state, site_table)
            support = {write.site for write in event.delta_window}
            bound = tuple(
                cell
                for cell in cells
                if BINDER_PREDICATE(event, cell)
            )
            relation_evaluations += len(cells)
            total_events += 1
            total_writes += len(event.delta_window)
            total_bindings += len(bound)
            family_writes += len(event.delta_window)
            family_bindings += len(bound)
            write_counts.append(len(event.delta_window))
            bound_sites = {cell.record.site for cell in bound}
            support_mismatches += bound_sites != support
            phantom_bindings += sum(
                cell.record.site not in support for cell in bound
            )
            for write in event.delta_window:
                matches = tuple(
                    cell
                    for cell in bound
                    if cell.record.site == write.site
                )
                orphan_writes += not matches
                duplicate_bindings += len(matches) != 1
                if len(matches) == 1:
                    content_mismatches += (
                        matches[0].record.content != write.content
                    )
            expected_readout = sum(
                R693.F(write.after) for write in event.delta_window
            )
            observed_readout = R693.record_readout(
                tuple(cell.record for cell in bound)
            )
            readout_mismatches += observed_readout != expected_readout
            association_digest_rows.append(
                (
                    family.bank_count,
                    event.tick_id,
                    tuple((write.wire, write.before, write.after) for write in event.delta_window),
                    tuple(cell.wire for cell in bound),
                )
            )
        rows[family.bank_count] = {
            "events": len(family.events),
            "writes": family_writes,
            "bindings": family_bindings,
            "minimum_writes_per_event": min(write_counts),
            "maximum_writes_per_event": max(write_counts),
            "write_count_sha256": digest(write_counts),
        }
    return {
        "by_family": rows,
        "events": total_events,
        "writes": total_writes,
        "bindings": total_bindings,
        "relation_evaluations": relation_evaluations,
        "orphan_writes": orphan_writes,
        "phantom_bindings": phantom_bindings,
        "duplicate_bindings": duplicate_bindings,
        "support_mismatches": support_mismatches,
        "written_content_mismatches": content_mismatches,
        "R693_readout_mismatches": readout_mismatches,
        "association_sha256": digest(association_digest_rows),
        "pass": (
            total_events == 38
            and total_writes > 0
            and total_writes == total_bindings
            and orphan_writes == 0
            and phantom_bindings == 0
            and duplicate_bindings == 0
            and support_mismatches == 0
            and content_mismatches == 0
            and readout_mismatches == 0
        ),
    }


def identification_certificate(
    families: tuple[LawfulFamily, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    """Identify the derived scalar with the landed literal-one call scope."""

    by_family: dict[int, dict[str, int]] = {}
    real_writes = transports = constant_one_agreements = 0
    binder_ones = binder_zeroes = 0
    for family in families:
        row = {
            "acceptance_calls": 0,
            "real_write_events": 0,
            "pure_transport_events": 0,
            "binder_ones": 0,
            "binder_zeroes": 0,
            "constant_one_agreements_on_real_writes": 0,
        }
        for event, post_state in zip(family.events, family.post_states):
            cells = record_cells_for_state(post_state, site_table)
            binder = EVENT_BINDER_VALUE(event, cells)
            writes = bool(event.delta_window)
            row["acceptance_calls"] += 1
            row["real_write_events"] += writes
            row["pure_transport_events"] += not writes
            row["binder_ones"] += binder == 1
            row["binder_zeroes"] += binder == 0
            row["constant_one_agreements_on_real_writes"] += writes and binder == 1
            real_writes += writes
            transports += not writes
            binder_ones += binder == 1
            binder_zeroes += binder == 0
            constant_one_agreements += writes and binder == 1
        by_family[family.bank_count] = row
    return {
        "by_family": by_family,
        "acceptance_events": real_writes + transports,
        "real_write_events": real_writes,
        "pure_transport_acceptance_events": transports,
        "binder_ones": binder_ones,
        "binder_zeroes": binder_zeroes,
        "supplied_constant_one_agreements_on_real_writes": constant_one_agreements,
        "split_finding": (
            "No lawful pure-transport acceptance event exists on the held "
            "2/5/12 families: all 38 full-orbit admit calls have real writes. "
            "Controller rail motion is internal to those events, not a separate "
            "EventChain.admit call."
        ),
        "pass": (
            real_writes == 38
            and transports == 0
            and binder_ones == 38
            and binder_zeroes == 0
            and constant_one_agreements == 38
        ),
    }


def binder_admit_adapter(
    chain: object,
    event: LocalEvent,
    cells: tuple[RecordCell, ...],
    orientation: int,
) -> str:
    """Replace only the supplied binder literal at the landed admit call."""

    return chain.admit(
        tick_id=event.tick_id,
        orientation=orientation,
        certificate=1,
        binder=EVENT_BINDER_VALUE(event, cells),
        actuality=1,
        admissibility=1,
        law_domain=1,
    )


def adapter_certificate(
    families: tuple[LawfulFamily, ...],
    site_table: tuple[tuple[int, int, int], ...],
) -> dict[str, object]:
    """Compare supplied and derived admission traces byte-for-byte."""

    family_rows: dict[int, dict[str, object]] = {}
    total_status_mismatches = total_row_mismatches = logical_failures = 0
    for family in families:
        supplied_chain = K.B.C704.C610.EventChain(bank=2 * family.bank_count)
        derived_chain = K.B.C704.C610.EventChain(bank=2 * family.bank_count)
        supplied_trace: list[object] = []
        derived_trace: list[object] = []
        for event, post_state in zip(family.events, family.post_states):
            orientation = 1 if event.direction == (1, 0) else -1
            cells = record_cells_for_state(post_state, site_table)
            supplied_status = supplied_chain.admit(
                tick_id=event.tick_id,
                orientation=orientation,
                certificate=1,
                binder=1,
                actuality=1,
                admissibility=1,
                law_domain=1,
            )
            derived_status = binder_admit_adapter(
                derived_chain, event, cells, orientation
            )
            supplied_rows = K.B.cell_rows(supplied_chain)
            derived_rows = K.B.cell_rows(derived_chain)
            total_status_mismatches += supplied_status != derived_status
            total_row_mismatches += supplied_rows != derived_rows
            banks, links = K.M.unpack_state(post_state, family.bank_count)
            decoded, _order = K.B.decode_local_graph(banks, links)
            logical_failures += (
                derived_status != "admitted"
                or K.B.cell_rows(decoded) != derived_rows
            )
            supplied_trace.append((supplied_status, supplied_rows))
            derived_trace.append((derived_status, derived_rows))
        supplied_bytes = stable_json(supplied_trace).encode()
        derived_bytes = stable_json(derived_trace).encode()
        family_rows[family.bank_count] = {
            "events": len(family.events),
            "supplied_trace_bytes": len(supplied_bytes),
            "derived_trace_bytes": len(derived_bytes),
            "byte_exact": supplied_bytes == derived_bytes,
            "trace_sha256": sha256(derived_bytes).hexdigest(),
        }

    # Non-writing control: not a member of the lawful fixture families.  It
    # proves that the adapter is a live predicate rather than an obfuscated 1.
    blank_state = families[0].post_states[-1]
    blank_cells = record_cells_for_state(blank_state, site_table)
    counterfactual = LocalEvent(
        tick_id=0,
        direction=(1, 0),
        delta_window=(),
        remote_context_digest="counterfactual-empty-delta",
    )
    derived_control_chain = K.B.C704.C610.EventChain(bank=4)
    supplied_control_chain = K.B.C704.C610.EventChain(bank=4)
    derived_control_status = binder_admit_adapter(
        derived_control_chain, counterfactual, blank_cells, 1
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
        "derived_binder": EVENT_BINDER_VALUE(counterfactual, blank_cells),
        "derived_status": derived_control_status,
        "supplied_literal_one_status": supplied_control_status,
        "behavior_delta": derived_control_status != supplied_control_status,
        "derived_rows": K.B.cell_rows(derived_control_chain),
        "supplied_rows": K.B.cell_rows(supplied_control_chain),
    }

    adapter_tree = ast.parse(inspect.getsource(binder_admit_adapter))
    binder_keywords = tuple(
        keyword.value
        for node in ast.walk(adapter_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "admit"
        for keyword in node.keywords
        if keyword.arg == "binder"
    )
    adapter_uses_predicate = (
        len(binder_keywords) == 1
        and isinstance(binder_keywords[0], ast.Call)
        and ast.unparse(binder_keywords[0].func) == "EVENT_BINDER_VALUE"
    )
    return {
        "by_family": family_rows,
        "status_mismatches": total_status_mismatches,
        "cell_row_mismatches": total_row_mismatches,
        "logical_trace_failures": logical_failures,
        "all_lawful_traces_byte_exact": all(
            row["byte_exact"] for row in family_rows.values()
        ),
        "adapter_AST_binder_is_derived_predicate": adapter_uses_predicate,
        "counterfactual_nonwriting_control": control,
        "pass": (
            total_status_mismatches == 0
            and total_row_mismatches == 0
            and logical_failures == 0
            and all(row["byte_exact"] for row in family_rows.values())
            and adapter_uses_predicate
            and control["derived_binder"] == 0
            and control["derived_status"] == "no_opportunity"
            and control["supplied_literal_one_status"] == "admitted"
            and control["behavior_delta"]
        ),
    }


def no_new_supplier_certificate() -> dict[str, object]:
    """Audit imports, selection inputs, and the precise R-eta daylight."""

    source = inspect.getsource(sys.modules[__name__])
    tree = ast.parse(source)
    imports = tuple(
        sorted(
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
        )
    )
    repo_imports = tuple(
        name
        for name in imports
        if name.startswith("frontier_")
        or name.startswith("physical_record_")
    )
    executable_identifiers = tuple(
        sorted(
            {
                node.id
                for node in ast.walk(tree)
                if isinstance(node, ast.Name)
            }
            | {
                node.attr
                for node in ast.walk(tree)
                if isinstance(node, ast.Attribute)
            }
        )
    )
    bare_formation_used_as_selector = any(
        name.lower()
        in {
            "records_form",
            "record_formation_exists",
            "formation_existence_selector",
        }
        for name in executable_identifiers
    )
    return {
        "repo_imports": repo_imports,
        "expected_repo_imports": (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
            "physical_record_readout_carrier_three_way_split_cycle693_2026_07_25",
        ),
        "declared_new_site_correspondences": 1,
        "site_correspondence": SITE_CORRESPONDENCE_NAME,
        "delta_boundary": DELTA_BOUNDARY,
        "site_computed_from_delta_support": True,
        "content_computed_from_written_values": True,
        "association_computed_from_touch_relation": True,
        "generic_Record_formation_existence_invoked": False,
        "executable_formation_selector_identifiers": tuple(
            name
            for name in executable_identifiers
            if name.lower()
            in {
                "records_form",
                "record_formation_exists",
                "formation_existence_selector",
            }
        ),
        "bare_formation_used_as_selector": bare_formation_used_as_selector,
        "other_acceptance_inputs_still_supplied": (
            "certificate",
            "actuality",
            "admissibility",
            "law_domain",
        ),
        "R_eta_selected": False,
        "permanent_Record_bridge_claimed": False,
        "Born_or_realized_history_claimed": False,
        "no_go_boundary": NO_GO_BOUNDARY,
        "pass": (
            repo_imports
            == (
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
                "physical_record_readout_carrier_three_way_split_cycle693_2026_07_25",
            )
            and not bare_formation_used_as_selector
        ),
    }


def main() -> int:
    started = perf_counter()
    layout = K.M.R12.full_wire_layout()
    site_table = tuple(tuple(site) for site in layout["wire_sites"])
    families = tuple(
        lawful_fixture_family(bank_count, site_table)
        for bank_count in FIXTURE_BANK_COUNTS
    )

    anchors = anchor_certificate(site_table, families)
    check("A_anchors", anchors["pass"])

    candidate = candidate_ast_certificate()
    check("B_candidate_definition_AST", candidate["pass"])

    locality = locality_certificate(families, site_table)
    check("C1_locality_census", locality["pass"])

    totality = totality_certificate(families, site_table)
    check("C2_totality_uniqueness_census", totality["pass"])

    identification = identification_certificate(families, site_table)
    check("C3_identification_census", identification["pass"])

    adapter = adapter_certificate(families, site_table)
    check("D_adapter_result", adapter["pass"])

    supplier_audit = no_new_supplier_certificate()
    check("E_no_new_supplier_and_no_go_boundary", supplier_audit["pass"])

    prior_science_labels = tuple(CHECKS)
    fixture_derived = all(CHECKS[label] for label in prior_science_labels)
    outcome = (
        "OUTCOME A — BINDER derived at fixture scope"
        if fixture_derived
        else "OUTCOME B — frozen failure census and forcing key"
    )
    boundary = {
        "outcome": outcome,
        "outcome_A_conditions_verbatim": OUTCOME_A_CONDITIONS_VERBATIM,
        "binder_fixture_closed": fixture_derived,
        "binder_global_closed": False,
        "w3_closed": False,
        "forcing_key_active": not fixture_derived,
        "minimal_content_sentence": MINIMAL_BINDER_CONTENT,
        "failure_census": tuple(
            sorted(label for label, passed in CHECKS.items() if not passed)
        ),
        "remaining_W3_supplies": (
            "ACTUAL",
            "ADMISS",
            "LAW",
        ),
        "W5_permanent_Record_bridge_closed": False,
        "R_eta_selected": False,
        "scope_firewall": (
            "The result is exhaustive only for the held K lawful 2/5/12 "
            "fixture families under the declared site embedding."
        ),
    }
    check(
        "F_honest_boundary_keys",
        boundary["w3_closed"] is False
        and boundary["binder_global_closed"] is False
        and boundary["W5_permanent_Record_bridge_closed"] is False
        and boundary["R_eta_selected"] is False
        and boundary["binder_fixture_closed"] is fixture_derived
        and boundary["forcing_key_active"] is (not fixture_derived)
        and len(boundary["outcome_A_conditions_verbatim"]) == 9
        and len(boundary["remaining_W3_supplies"]) == 3
        and (
            fixture_derived
            or (
                bool(boundary["failure_census"])
                and boundary["minimal_content_sentence"]
                == MINIMAL_BINDER_CONTENT
            )
        ),
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "cycle": 751,
        "candidate": candidate,
        "anchors": anchors,
        "locality": locality,
        "totality_uniqueness": totality,
        "identification": identification,
        "adapter": adapter,
        "no_new_supplier_audit": supplier_audit,
        "boundary": boundary,
        "outcome": outcome,
        "runtime_seconds": round(elapsed, 6),
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "pass": all(CHECKS.values()),
        "terminal": (
            "CYCLE751_BINDER_FORMATION_ATTEMPT_PASS"
            if all(CHECKS.values())
            else "CYCLE751_BINDER_FORMATION_ATTEMPT_HONEST_FAIL"
        ),
    }
    preliminary = stable_json(report)
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode())
        + len("\n".join(OUTPUT_LINES).encode())
        + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE751_BINDER_FORMATION_ATTEMPT_PASS"
        if report["pass"]
        else "CYCLE751_BINDER_FORMATION_ATTEMPT_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(stable_json(report).encode()).hexdigest()
    final_json = stable_json(report)
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
