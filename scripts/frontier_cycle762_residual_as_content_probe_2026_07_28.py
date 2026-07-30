#!/usr/bin/env python3
"""Cycle 762: first bounded probe of residual as physical content.

Cycle 759's primary is read only as AST data.  Its exact landed residual
projection is isolated and applied to the same 44 pairwise-separated k=2
configurations in the four held two-bank epochs.  The resulting 176-key,
25-signature map is then tested for continued-update conservation, a closed
XOR/cocycle algebra, and orbit-homogeneous signature sectors.

This is residue characterization only.  It introduces no supplier, changes no
predicate, and makes no selection or actuality claim.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/RESIDUAL_AS_CONTENT_PROBE_CYCLE762_BOUNDED_THEOREM_NOTE_"
    "2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, defaultdict
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PRIMARY_DATA_PATH = (
    "scripts/frontier_cycle759_multisource_postimage_law_2026_07_28.py"
)
PRIMARY_MODULE_NAME = (
    "frontier_cycle759_multisource_postimage_law_2026_07_28"
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
CONTINUATION_UPDATES = 16
STDOUT_LIMIT_BYTES = 150 * 1024

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []

Coordinate = tuple[str, str, int]
Residual = tuple[tuple[str, str, int, int], ...]
Key = tuple[int, tuple[int, ...]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(rows: object) -> str:
    return sha256(compact(rows).encode("utf-8")).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def attribute_root(node: ast.Attribute) -> str | None:
    root: ast.expr = node
    while isinstance(root, ast.Attribute):
        root = root.value
    return root.id if isinstance(root, ast.Name) else None


def labeled_check_expression(
    functions: dict[str, ast.FunctionDef], label: str
) -> ast.expr:
    for node in ast.walk(functions["main"]):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "check"
            and len(node.args) >= 2
            and isinstance(node.args[0], ast.Constant)
            and node.args[0].value == label
        ):
            return node.args[1]
    raise AssertionError(("missing Cycle 759 check", label))


def extract_cycle759_projection() -> tuple[object, dict[str, object]]:
    """Compile only the two residual-projection functions selected by AST."""

    path = ROOT / PRIMARY_DATA_PATH
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_DATA_PATH)
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    names = ("watched_bank_registers", "postimage_residual")
    selected = tuple(functions[name] for name in names)
    module_roots = {
        node.name: tuple(
            sorted(
                {
                    root
                    for child in ast.walk(node)
                    if isinstance(child, ast.Attribute)
                    for root in (attribute_root(child),)
                    if root in {"F750", "M736", "K"}
                }
            )
        )
        for node in selected
    }
    expected_roots = {
        "watched_bank_registers": ("K",),
        "postimage_residual": ("K",),
    }
    forbidden_calls = tuple(
        child.func.id
        for node in selected
        for child in ast.walk(node)
        if isinstance(child, ast.Call)
        and isinstance(child.func, ast.Name)
        and child.func.id in {"eval", "exec", "__import__", "open"}
    )
    census_expression = labeled_check_expression(
        functions,
        "B_residual_census_all_44_all_epochs_exact_and_lawful",
    )
    signature_expression = labeled_check_expression(
        functions,
        "B_residual_is_configuration_dependent_not_uniform",
    )
    frozen_176_present = any(
        isinstance(node, ast.Constant) and node.value == 176
        for node in ast.walk(census_expression)
    )
    frozen_epoch_signature_counts_present = any(
        isinstance(node, ast.Tuple)
        and tuple(
            element.value
            for element in node.elts
            if isinstance(element, ast.Constant)
        )
        == (1, 1, 12, 14)
        and len(node.elts) == 4
        for node in ast.walk(signature_expression)
    )
    isolated = ast.Module(body=list(selected), type_ignores=[])
    ast.fix_missing_locations(isolated)
    namespace: dict[str, object] = {"K": K}
    exec(
        compile(isolated, PRIMARY_DATA_PATH, "exec"),
        namespace,
        namespace,
    )
    projection = namespace["postimage_residual"]
    audit = {
        "primary_path": PRIMARY_DATA_PATH,
        "read_as_AST_data": True,
        "primary_module_imported": PRIMARY_MODULE_NAME in sys.modules,
        "selected_functions": names,
        "selected_module_roots": module_roots,
        "expected_module_roots": expected_roots,
        "forbidden_calls": forbidden_calls,
        "frozen_176_literal_reextracted": frozen_176_present,
        "frozen_epoch_signature_counts_reextracted":
            frozen_epoch_signature_counts_present,
        "projection_AST_sha256": digest_rows(
            tuple(ast.dump(node, include_attributes=False) for node in selected)
        ),
        "source_sha256": sha256(source.encode("utf-8")).hexdigest(),
        "isolated_projection_pass": (
            module_roots == expected_roots
            and not forbidden_calls
            and frozen_176_present
            and frozen_epoch_signature_counts_present
            and PRIMARY_MODULE_NAME not in sys.modules
        ),
    }
    return projection, audit


def held_two_bank_epochs() -> tuple[
    tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    tuple[object, ...],
    dict[str, object],
]:
    """Rebuild the four Cycle-719 held epochs without a Cycle-750 supplier."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    baseline_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        expected = K.A.apply_semantic(before, allocator)
        baseline_failures += after != expected
        baseline_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        baseline_failures += any(rail_b)
        baseline_failures += len(trace) != len(program)
        epochs.append((event, direction, before))
        state = after
    return tuple(epochs), program, {
        "epochs": len(epochs),
        "directions": tuple(row[1] for row in epochs),
        "program_stations": len(program),
        "baseline_failures": baseline_failures,
        "terminal_state_sha256": digest_rows(state),
    }


def k2_positions() -> tuple[tuple[int, ...], ...]:
    configurations = M736.configuration_census()["configurations"]
    return tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 2
    )


def support(residual: Residual) -> frozenset[Coordinate]:
    return frozenset(
        (domain, register, wire)
        for domain, register, wire, content in residual
        if content
    )


def canonical_support(
    row: frozenset[Coordinate],
) -> tuple[Coordinate, ...]:
    return tuple(sorted(row))


def frozen_map_certificate(
    projection: object,
    epochs: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    program: tuple[object, ...],
    positions: tuple[tuple[int, ...], ...],
) -> tuple[
    dict[Key, Residual],
    dict[Key, tuple[int, ...]],
    dict[tuple[int, ...], tuple[object, ...]],
    dict[str, object],
]:
    composition_words = {
        row: M736.synchronous_composition_word(program, row)
        for row in positions
    }
    residual_map: dict[Key, Residual] = {}
    post_states: dict[Key, tuple[int, ...]] = {}
    rows = []
    per_epoch: dict[int, Counter[Residual]] = {}
    composition_failures = 0
    rail_failures = 0
    inverse_failures = 0
    nonbinary_contents = 0
    for event, direction, before in epochs:
        counts: Counter[Residual] = Counter()
        for row in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=row
            )
            expected = K.A.apply_semantic(
                before, composition_words[row]
            )
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after, program, token_positions=row, reverse=True
            )
            residual = projection(after, FIXTURE_BANKS)
            key = (event, row)
            residual_map[key] = residual
            post_states[key] = after
            counts[residual] += 1
            composition_failures += after != expected
            expected_rail = tuple(
                int(station in row) for station in range(len(program))
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            inverse_failures += (
                restored != before
                or inverse_a != rail_a
                or inverse_b != rail_b
            )
            nonbinary_contents += sum(
                content != 1
                for _domain, _register, _wire, content in residual
            )
            rows.append((event, direction, row, residual))
        per_epoch[event] = counts
    all_signatures = set(residual_map.values())
    certificate = {
        "definition": (
            "key=(held epoch, persistent M736 source-position pair); value="
            "Cycle-759 AST-extracted exact nonzero landed residual"
        ),
        "keys": len(residual_map),
        "epochs": len(epochs),
        "configurations_per_epoch": len(positions),
        "unique_signatures": len(all_signatures),
        "unique_signatures_by_epoch": tuple(
            len(per_epoch[event]) for event, _direction, _before in epochs
        ),
        "signature_multiplicity_census": dict(
            sorted(
                Counter(
                    Counter(residual_map.values()).values()
                ).items()
            )
        ),
        "composition_failures": composition_failures,
        "rail_return_failures": rail_failures,
        "literal_inverse_failures": inverse_failures,
        "nonbinary_contents": nonbinary_contents,
        "map_sha256": digest_rows(rows),
        "key_sha256": digest_rows(
            tuple((event, row) for event, row in residual_map)
        ),
    }
    return residual_map, post_states, composition_words, certificate


def continuation_census(
    projection: object,
    residual_map: dict[Key, Residual],
    post_states: dict[Key, tuple[int, ...]],
    composition_words: dict[tuple[int, ...], tuple[object, ...]],
    program: tuple[object, ...],
) -> tuple[
    dict[Key, tuple[frozenset[Coordinate], ...]], dict[str, object]
]:
    traces: dict[Key, tuple[frozenset[Coordinate], ...]] = {}
    state_periods: Counter[int | None] = Counter()
    distinct_signatures: Counter[int] = Counter()
    invariant = 0
    transported_fixed_weight = 0
    monotone_growing = 0
    has_decrease = 0
    first_update_composition_failures = 0
    first_update_rail_failures = 0
    content_changes = 0
    coordinate_toggles = 0
    minimum_weight = None
    maximum_weight = 0
    trace_rows = []

    for key, state0 in post_states.items():
        _event, positions = key
        word = composition_words[positions]
        state = state0
        states_seen = {state0: 0}
        period = None
        residual_trace = [support(residual_map[key])]
        for update in range(1, CONTINUATION_UPDATES + 1):
            next_state = K.A.apply_semantic(state, word)
            if update == 1:
                direct, rail_a, rail_b, _trace = K.run_orbit(
                    state, program, token_positions=positions
                )
                expected_rail = tuple(
                    int(station in positions)
                    for station in range(len(program))
                )
                first_update_composition_failures += direct != next_state
                first_update_rail_failures += (
                    rail_a != expected_rail or any(rail_b)
                )
            next_residual = projection(next_state, FIXTURE_BANKS)
            residual_trace.append(support(next_residual))
            previous_support = residual_trace[-2]
            current_support = residual_trace[-1]
            content_changes += current_support != previous_support
            coordinate_toggles += len(previous_support ^ current_support)
            if period is None and next_state in states_seen:
                if states_seen[next_state] != 0:
                    raise AssertionError(
                        ("noninitial repeat under reversible word", key, update)
                    )
                period = update
            states_seen.setdefault(next_state, update)
            state = next_state

        trace = tuple(residual_trace)
        traces[key] = trace
        weights = tuple(map(len, trace))
        unique = len(set(trace))
        invariant += unique == 1
        transported_fixed_weight += (
            len(set(weights)) == 1 and unique > 1
        )
        monotone_growing += (
            all(
                weights[index + 1] >= weights[index]
                for index in range(CONTINUATION_UPDATES)
            )
            and any(
                weights[index + 1] > weights[index]
                for index in range(CONTINUATION_UPDATES)
            )
        )
        has_decrease += any(
            weights[index + 1] < weights[index]
            for index in range(CONTINUATION_UPDATES)
        )
        state_periods[period] += 1
        distinct_signatures[unique] += 1
        minimum_weight = (
            min(weights)
            if minimum_weight is None
            else min(minimum_weight, *weights)
        )
        maximum_weight = max(maximum_weight, *weights)
        trace_rows.append(
            (
                key,
                tuple(canonical_support(row) for row in trace),
                period,
            )
        )

    periodic = sum(
        count for period, count in state_periods.items()
        if period is not None
    )
    census = {
        "definition": (
            "One continuation update is one complete 11-Q controller orbit, "
            "applied by M736's exact synchronous-composition word.  All 176 "
            "first continuations are also rerun through K.run_orbit."
        ),
        "keys": len(traces),
        "additional_updates_per_key": CONTINUATION_UPDATES,
        "projected_states_per_key": CONTINUATION_UPDATES + 1,
        "first_update_composition_failures":
            first_update_composition_failures,
        "first_update_rail_return_failures":
            first_update_rail_failures,
        "signature_invariant_keys": invariant,
        "fixed_weight_transport_keys": transported_fixed_weight,
        "exact_full_state_periodic_keys_within_bound": periodic,
        "full_state_period_census": {
            ("not_closed_within_bound" if period is None else str(period)):
                count
            for period, count in sorted(
                state_periods.items(),
                key=lambda item: (
                    item[0] is None,
                    item[0] if item[0] is not None else 0,
                ),
            )
        },
        "monotone_nondecreasing_with_growth_keys": monotone_growing,
        "keys_with_a_residual_weight_decrease": has_decrease,
        "distinct_projected_signature_census": dict(
            sorted(distinct_signatures.items())
        ),
        "residual_weight_range": (minimum_weight, maximum_weight),
        "content_changing_transitions": content_changes,
        "coordinate_toggle_incidences": coordinate_toggles,
        "family_wide_conservation_or_transport": (
            invariant == len(traces)
            or transported_fixed_weight == len(traces)
        ),
        "family_wide_period_proved_within_bound":
            periodic == len(traces),
        "family_wide_growth": monotone_growing == len(traces),
        "law_candidate_for_next_cycle": None,
        "trace_sha256": digest_rows(trace_rows),
    }
    if census["family_wide_conservation_or_transport"]:
        census["law_candidate_for_next_cycle"] = (
            "landed residual support is conserved/transported under each "
            "continued k=2 update"
        )
    elif census["family_wide_period_proved_within_bound"]:
        census["law_candidate_for_next_cycle"] = (
            "landed residual is periodic with exact closed full-state orbits"
        )
    elif census["family_wide_growth"]:
        census["law_candidate_for_next_cycle"] = (
            "landed residual support grows monotonically"
        )
    return traces, census


def algebra_census(
    residual_map: dict[Key, Residual],
    traces: dict[Key, tuple[frozenset[Coordinate], ...]],
) -> dict[str, object]:
    frozen = {support(residual) for residual in residual_map.values()}
    empty: frozenset[Coordinate] = frozenset()
    frozen_with_identity = frozen | {empty}
    pair_cases = 0
    pair_closed = 0
    for left in frozen:
        for right in frozen:
            pair_cases += 1
            pair_closed += (left ^ right) in frozen_with_identity

    cocycle_cases = 0
    cocycle_failures = 0
    absolute_xor_cases = 0
    increment_in_frozen_set = 0
    observed_compositions_in_frozen_set = 0
    successor_by_signature: dict[
        frozenset[Coordinate], set[frozenset[Coordinate]]
    ] = defaultdict(set)
    increment_by_signature: dict[
        frozenset[Coordinate], set[frozenset[Coordinate]]
    ] = defaultdict(set)
    rows = []
    for key, trace in traces.items():
        r0, r1, r2 = trace[:3]
        delta_01 = r0 ^ r1
        delta_12 = r1 ^ r2
        delta_02 = r0 ^ r2
        composed = delta_01 ^ delta_12
        cocycle_cases += 1
        cocycle_failures += composed != delta_02
        absolute_xor_cases += r2 == (r0 ^ r1)
        increment_in_frozen_set += delta_01 in frozen_with_identity
        observed_compositions_in_frozen_set += composed in frozen_with_identity
        successor_by_signature[r0].add(r1)
        increment_by_signature[r0].add(delta_01)
        rows.append(
            (
                key,
                canonical_support(r0),
                canonical_support(r1),
                canonical_support(r2),
                canonical_support(delta_01),
                canonical_support(delta_12),
                canonical_support(delta_02),
            )
        )

    successor_splits = {
        row: len(outputs)
        for row, outputs in successor_by_signature.items()
        if len(outputs) > 1
    }
    increment_splits = {
        row: len(outputs)
        for row, outputs in increment_by_signature.items()
        if len(outputs) > 1
    }
    closed_algebra = pair_closed == pair_cases
    factorized_cocycle = (
        not successor_splits and not increment_splits
    )
    nontrivial_candidate = closed_algebra and factorized_cocycle
    return {
        "definition": (
            "pi(s) is the binary landed residual support.  Transition "
            "residue delta(s,F)=pi(s) XOR pi(Fs); the two-step cocycle test "
            "compares delta(s,F^2) with delta(s,F) XOR delta(Fs,F)."
        ),
        "frozen_signatures": len(frozen),
        "ordered_frozen_signature_pairs": pair_cases,
        "xor_outputs_in_frozen_set_with_zero_adjoined": pair_closed,
        "xor_outputs_outside_frozen_set_with_zero_adjoined":
            pair_cases - pair_closed,
        "closed_25_signature_XOR_algebra": closed_algebra,
        "two_step_cocycle_cases": cocycle_cases,
        "two_step_cocycle_failures": cocycle_failures,
        "cocycle_status": (
            "KINEMATIC_COBoundary_IDENTITY"
            if not cocycle_failures
            else "COCYCLE_FAILURE"
        ),
        "absolute_residue_XOR_additive_cases": absolute_xor_cases,
        "one_step_increments_in_frozen_set_with_zero":
            increment_in_frozen_set,
        "two_step_increments_in_frozen_set_with_zero":
            observed_compositions_in_frozen_set,
        "current_signature_classes": len(successor_by_signature),
        "successor_deterministic_classes":
            len(successor_by_signature) - len(successor_splits),
        "successor_split_classes": len(successor_splits),
        "successor_branch_count_census": dict(
            sorted(
                Counter(
                    len(outputs)
                    for outputs in successor_by_signature.values()
                ).items()
            )
        ),
        "increment_deterministic_classes":
            len(increment_by_signature) - len(increment_splits),
        "increment_split_classes": len(increment_splits),
        "increment_branch_count_census": dict(
            sorted(
                Counter(
                    len(outputs)
                    for outputs in increment_by_signature.values()
                ).items()
            )
        ),
        "nontrivial_signature_cocycle_factorizes": factorized_cocycle,
        "law_candidate_for_next_cycle": (
            "the 25 residual signatures form a closed XOR cocycle algebra"
            if nontrivial_candidate
            else None
        ),
        "honest_interpretation": (
            "The exact XOR equality is the telescoping identity for a "
            "projected bit-vector coboundary.  It is not promoted to a "
            "dynamical law unless the 25-signature set closes and the "
            "successor/increment descends to signature classes."
        ),
        "algebra_table_sha256": digest_rows(rows),
    }


def sector_census(
    residual_map: dict[Key, Residual],
    traces: dict[Key, tuple[frozenset[Coordinate], ...]],
) -> dict[str, object]:
    per_epoch = []
    total_classes = 0
    homogeneous_classes = 0
    split_classes = 0
    within_pairs = 0
    matching_pairs = 0
    discordant_pairs = 0
    rows_for_digest = []

    for event in range(2 * FIXTURE_BANKS):
        keys = tuple(key for key in residual_map if key[0] == event)
        groups: dict[frozenset[Coordinate], list[Key]] = defaultdict(list)
        for key in keys:
            groups[support(residual_map[key])].append(key)
        class_rows = []
        for signature, members in sorted(
            groups.items(), key=lambda item: canonical_support(item[0])
        ):
            fingerprints = Counter(
                tuple(
                    canonical_support(projected)
                    for projected in traces[key][1:]
                )
                for key in members
            )
            class_pairs = comb(len(members), 2)
            class_matching = sum(
                comb(count, 2) for count in fingerprints.values()
            )
            class_discordant = class_pairs - class_matching
            homogeneous = len(fingerprints) == 1
            signature_digest = digest_rows(canonical_support(signature))
            row = {
                "signature_sha256": signature_digest,
                "configurations": len(members),
                "distinct_continuation_behaviors": len(fingerprints),
                "within_class_pairs": class_pairs,
                "matching_behavior_pairs": class_matching,
                "discordant_behavior_pairs": class_discordant,
                "orbit_homogeneous": homogeneous,
            }
            class_rows.append(row)
            rows_for_digest.append((event, canonical_support(signature), row))
            total_classes += 1
            homogeneous_classes += homogeneous
            split_classes += not homogeneous
            within_pairs += class_pairs
            matching_pairs += class_matching
            discordant_pairs += class_discordant
        per_epoch.append(
            {
                "event": event,
                "configurations": len(keys),
                "signature_classes": len(groups),
                "class_size_census": dict(
                    sorted(Counter(map(len, groups.values())).items())
                ),
                "homogeneous_classes": sum(
                    row["orbit_homogeneous"] for row in class_rows
                ),
                "split_classes": sum(
                    not row["orbit_homogeneous"] for row in class_rows
                ),
                "class_rows": tuple(class_rows),
            }
        )

    candidate = split_classes == 0
    return {
        "definition": (
            "Within each held epoch, the frozen signature partitions all 44 "
            "configurations.  Orbit behavior is the exact 16-update landed "
            "residual trace after the frozen post-update state."
        ),
        "epochs": len(per_epoch),
        "configurations_per_epoch": tuple(
            row["configurations"] for row in per_epoch
        ),
        "signature_classes_per_epoch": tuple(
            row["signature_classes"] for row in per_epoch
        ),
        "total_epoch_signature_classes": total_classes,
        "orbit_homogeneous_classes": homogeneous_classes,
        "orbit_split_classes": split_classes,
        "within_signature_unordered_pairs": within_pairs,
        "matching_orbit_behavior_pairs": matching_pairs,
        "discordant_orbit_behavior_pairs": discordant_pairs,
        "per_epoch": tuple(per_epoch),
        "derived_quantum_number_on_probe": candidate,
        "law_candidate_for_next_cycle": (
            "the landed residual signature is an orbit-sector quantum number"
            if candidate
            else None
        ),
        "sector_table_sha256": digest_rows(rows_for_digest),
    }


def outcome_certificate(
    conservation: dict[str, object],
    algebra: dict[str, object],
    sectors: dict[str, object],
    primary_audit: dict[str, object],
) -> dict[str, object]:
    candidates = {
        "conservation": conservation["law_candidate_for_next_cycle"],
        "algebra": algebra["law_candidate_for_next_cycle"],
        "sector": sectors["law_candidate_for_next_cycle"],
    }
    frozen_candidates = tuple(
        candidate for candidate in candidates.values()
        if candidate is not None
    )
    if frozen_candidates:
        outcome = "RESIDUAL_CONTENT_LAW_CANDIDATE_FROZEN"
        statement = (
            "At least one nontrivial family-wide residual-content structure "
            "survives this bounded probe; its exact candidate is frozen for "
            "the next cycle."
        )
    else:
        outcome = "NO_FAMILY_WIDE_RESIDUAL_CONTENT_LAW"
        statement = (
            "The 176-key residue changes nonconservatively, the 25 signatures "
            "do not close or support a descended XOR cocycle, and signature "
            "classes split by continued orbit behavior.  These exact "
            "negatives sharpen the forcing entry."
        )
    keys = {
        "residual_characterization_only": True,
        "cycle759_primary_read_as_data": True,
        "cycle759_primary_imported":
            primary_audit["primary_module_imported"],
        "new_supplier_added": False,
        "selection_predicate_changed": False,
        "selector_retested": False,
        "actuality_selected": False,
        "conservation_candidate_frozen":
            candidates["conservation"] is not None,
        "algebra_candidate_frozen":
            candidates["algebra"] is not None,
        "sector_candidate_frozen":
            candidates["sector"] is not None,
        "only_kinematic_XOR_coboundary":
            algebra["cocycle_status"]
            == "KINEMATIC_COBoundary_IDENTITY"
            and candidates["algebra"] is None,
        "forcing_negative_sharpened": not frozen_candidates,
        "ring11_only": True,
        "pairwise_separated_k2_only": True,
        "two_bank_four_epoch_fixture_only": True,
        "continuation_bound_updates": CONTINUATION_UPDATES,
        "higher_k_extended": False,
        "arbitrary_ring_claimed": False,
        "W3_closed": False,
    }
    return {
        "outcome": outcome,
        "statement": statement,
        "candidate_laws_for_next_cycle": candidates,
        "frozen_candidate_count": len(frozen_candidates),
        "honest_outcome_keys": keys,
        "scope_statement": (
            "This is an exhaustive characterization of the supplied 176 "
            "ring-11/two-bank keys through a declared 16-update continuation "
            "window.  Nonclosure within that window is not an infinite-time "
            "aperiodicity claim, and no selection, supplier, higher-k, "
            "arbitrary-ring, genesis, renewal, or W3 conclusion is made."
        ),
    }


def main() -> int:
    started = monotonic()

    projection, primary_audit = extract_cycle759_projection()
    epochs, program, epoch_anchor = held_two_bank_epochs()
    positions = k2_positions()
    held = K.held_certificate(FIXTURE_BANKS)
    residual_map, post_states, composition_words, frozen_map = (
        frozen_map_certificate(
            projection, epochs, program, positions
        )
    )
    check(
        "A_anchors_and_Cycle759_176_key_map_reextracted",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and primary_audit["isolated_projection_pass"]
        and not primary_audit["primary_module_imported"]
        and epoch_anchor["epochs"] == 4
        and epoch_anchor["directions"]
        == ((1, 0), (0, 1), (1, 0), (0, 1))
        and epoch_anchor["program_stations"] == RING_STATIONS
        and epoch_anchor["baseline_failures"] == 0
        and held["events"] == 4
        and held["logical_failures"] == 0
        and held["fixed_word_failures"] == 0
        and held["inverse_failures"] == 0
        and held["postimage_failures"] == 0
        and held["token_return_failures"] == 0
        and len(positions) == M736.EXPECTED_COUNTS_BY_K[2] == 44
        and frozen_map["keys"] == 176
        and frozen_map["epochs"] == 4
        and frozen_map["configurations_per_epoch"] == 44
        and frozen_map["unique_signatures"] == 25
        and frozen_map["unique_signatures_by_epoch"] == (1, 1, 12, 14)
        and frozen_map["composition_failures"] == 0
        and frozen_map["rail_return_failures"] == 0
        and frozen_map["literal_inverse_failures"] == 0
        and frozen_map["nonbinary_contents"] == 0,
    )

    traces, conservation = continuation_census(
        projection,
        residual_map,
        post_states,
        composition_words,
        program,
    )
    check(
        "B_conservation_transport_period_growth_census_exact",
        conservation["keys"] == 176
        and conservation["additional_updates_per_key"]
        == CONTINUATION_UPDATES
        and conservation["projected_states_per_key"]
        == CONTINUATION_UPDATES + 1
        and conservation["first_update_composition_failures"] == 0
        and conservation["first_update_rail_return_failures"] == 0
        and sum(
            conservation[
                "distinct_projected_signature_census"
            ].values()
        )
        == 176
        and sum(
            conservation["full_state_period_census"].values()
        )
        == 176
        and conservation["signature_invariant_keys"] == 0
        and conservation["keys_with_a_residual_weight_decrease"] == 176
        and not conservation[
            "family_wide_conservation_or_transport"
        ]
        and not conservation[
            "family_wide_period_proved_within_bound"
        ]
        and not conservation["family_wide_growth"]
        and conservation["law_candidate_for_next_cycle"] is None,
    )

    algebra = algebra_census(residual_map, traces)
    check(
        "C_25_signature_algebra_and_two_step_cocycle_census_exact",
        algebra["frozen_signatures"] == 25
        and algebra["ordered_frozen_signature_pairs"] == 25 * 25
        and (
            algebra[
                "xor_outputs_in_frozen_set_with_zero_adjoined"
            ]
            + algebra[
                "xor_outputs_outside_frozen_set_with_zero_adjoined"
            ]
            == 25 * 25
        )
        and algebra["two_step_cocycle_cases"] == 176
        and algebra["two_step_cocycle_failures"] == 0
        and algebra["cocycle_status"]
        == "KINEMATIC_COBoundary_IDENTITY"
        and not algebra["closed_25_signature_XOR_algebra"]
        and algebra["successor_split_classes"] > 0
        and algebra["increment_split_classes"] > 0
        and not algebra[
            "nontrivial_signature_cocycle_factorizes"
        ]
        and algebra["law_candidate_for_next_cycle"] is None,
    )

    sectors = sector_census(residual_map, traces)
    check(
        "D_signature_sector_orbit_behavior_census_exact",
        sectors["epochs"] == 4
        and sectors["configurations_per_epoch"]
        == (44, 44, 44, 44)
        and sectors["signature_classes_per_epoch"]
        == (1, 1, 12, 14)
        and sectors["total_epoch_signature_classes"] == 28
        and (
            sectors["orbit_homogeneous_classes"]
            + sectors["orbit_split_classes"]
            == sectors["total_epoch_signature_classes"]
        )
        and (
            sectors["matching_orbit_behavior_pairs"]
            + sectors["discordant_orbit_behavior_pairs"]
            == sectors["within_signature_unordered_pairs"]
        )
        and sectors["orbit_split_classes"] > 0
        and sectors["discordant_orbit_behavior_pairs"] > 0
        and not sectors["derived_quantum_number_on_probe"]
        and sectors["law_candidate_for_next_cycle"] is None,
    )

    outcome = outcome_certificate(
        conservation, algebra, sectors, primary_audit
    )
    keys = outcome["honest_outcome_keys"]
    check(
        "E_honest_outcome_keys_no_selection_or_new_supplier",
        outcome["outcome"]
        == "NO_FAMILY_WIDE_RESIDUAL_CONTENT_LAW"
        and outcome["frozen_candidate_count"] == 0
        and keys["residual_characterization_only"]
        and keys["cycle759_primary_read_as_data"]
        and not keys["cycle759_primary_imported"]
        and not keys["new_supplier_added"]
        and not keys["selection_predicate_changed"]
        and not keys["selector_retested"]
        and not keys["actuality_selected"]
        and not keys["conservation_candidate_frozen"]
        and not keys["algebra_candidate_frozen"]
        and not keys["sector_candidate_frozen"]
        and keys["only_kinematic_XOR_coboundary"]
        and keys["forcing_negative_sharpened"]
        and keys["ring11_only"]
        and keys["pairwise_separated_k2_only"]
        and keys["two_bank_four_epoch_fixture_only"]
        and keys["continuation_bound_updates"]
        == CONTINUATION_UPDATES
        and not keys["higher_k_extended"]
        and not keys["arbitrary_ring_claimed"]
        and not keys["W3_closed"],
    )

    elapsed = monotonic() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "anchors": {
            "Cycle719_held_two_bank": {
                key: value
                for key, value in held.items()
                if key not in {"state", "chain"}
            },
            "held_epoch_reconstruction": epoch_anchor,
            "M736_k2_configurations": len(positions),
        },
        "certificate_A_primary_AST_and_frozen_map": {
            "primary_AST_audit": primary_audit,
            "frozen_map": frozen_map,
        },
        "certificate_B_conservation": conservation,
        "certificate_C_algebra": algebra,
        "certificate_D_sectors": sectors,
        "certificate_E_outcome": outcome,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE762_RESIDUAL_AS_CONTENT_PROBE_PASS"
            if all(CHECKS.values())
            else "CYCLE762_RESIDUAL_AS_CONTENT_PROBE_HONEST_FAIL"
        ),
    }
    preliminary = compact(report)
    projected_size = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(preliminary.encode("utf-8"))
        + 4096
    )
    check(
        "OUTPUT_stdout_under_150KB_and_runtime_bounded",
        projected_size < STDOUT_LIMIT_BYTES
        and elapsed < AUDIT_TIMEOUT_SEC
        and NOTE_PATH.endswith(".md"),
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE762_RESIDUAL_AS_CONTENT_PROBE_PASS"
        if report["pass"]
        else "CYCLE762_RESIDUAL_AS_CONTENT_PROBE_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
    final_json = compact(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
