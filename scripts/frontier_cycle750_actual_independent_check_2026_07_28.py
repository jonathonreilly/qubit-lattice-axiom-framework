#!/usr/bin/env python3
"""Cycle 750 independent checker: attack uniqueness, never import the primary."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/ACTUAL_SELECTOR_STRETCH_CYCLE750_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import protected_recurrent_actual_history_selection_cycle335_2026_07_18 as H335
import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as O332
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PRIMARY_MODULE = "frontier_cycle750_actual_selector_stretch_2026_07_28"
PRIMARY_PATH = ROOT / "scripts" / f"{PRIMARY_MODULE}.py"
BLOCKLIST = (PRIMARY_MODULE,)
EXPECTED_AUDIT_INPUT_PATHS = (
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_DEFINITION_HASHES = {
    "recurrent_fixed_member_selector":
        "87a14e5f10f92f102a401b12d3ca3185ea05a875c3cb0b4904fddecf530f3724",
    "all_close_verdict_selector":
        "0590831796fecb08abfb1e4f46b8ba5d6ff5a08c59561adc1977355dd4d0b553",
    "enforcement_lineage_selector":
        "3043d127ae4cf3af971872dd0a4bc7dcd72a1a0f068169cbf654a390358d75bd",
}
EXPECTED_BOUNDARY = {
    "fixture_scope_only": True,
    "held_bank_counts": [2, 5, 12],
    "source_boundary_and_orientation_remain_supplied": True,
    "autonomous_genesis_or_enforcement_derived": False,
    "record_typing_derived": False,
    "permanence_derived": False,
    "time_law_derived": False,
    "w3_closed": False,
}
EXPECTED_CONDITIONS = [
    "one controller token at source station and zero B/work rails",
    "source boundary and oriented finite program ring",
    "Q-before-R layer order and bounded local macro gate order",
    "clean data-bank/link/route genesis and event predicates",
]
START = monotonic()


def digest(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def function_nodes(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def assignment_nodes(tree: ast.Module) -> dict[str, ast.expr]:
    found: dict[str, ast.expr] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            found[node.target.id] = node.value
    return found


def dotted_name(node: ast.expr) -> str | None:
    parts = []
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
        return ".".join(reversed(parts))
    return None


def literal_dicts(node: ast.AST) -> list[dict[object, object]]:
    found = []
    for child in ast.walk(node):
        if not isinstance(child, ast.Dict):
            continue
        try:
            value = ast.literal_eval(child)
        except (ValueError, TypeError):
            continue
        if isinstance(value, dict):
            found.append(value)
    return found


def keyed_literal(node: ast.AST, key: str) -> object:
    values = []
    for child in ast.walk(node):
        if not isinstance(child, ast.Dict):
            continue
        for key_node, value_node in zip(child.keys, child.values):
            try:
                observed_key = ast.literal_eval(key_node)
            except (ValueError, TypeError):
                continue
            if observed_key != key:
                continue
            try:
                values.append(ast.literal_eval(value_node))
            except (ValueError, TypeError):
                pass
    if not values:
        raise AssertionError(f"literal key not found: {key}")
    first = values[0]
    if any(value != first for value in values):
        raise AssertionError(f"ambiguous literal key: {key}")
    return first


def has_literal(node: ast.AST, expected: object) -> bool:
    for child in ast.walk(node):
        try:
            if ast.literal_eval(child) == expected:
                return True
        except (ValueError, TypeError):
            pass
    return False


def extraction() -> tuple[bool, dict[str, object]]:
    source = PRIMARY_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(PRIMARY_PATH))
    assignments = assignment_nodes(tree)
    functions = function_nodes(tree)
    candidate_names = tuple(EXPECTED_DEFINITION_HASHES)
    extracted_nodes = {name: functions[name] for name in candidate_names}
    definition_hashes = {
        name: sha256(
            ast.dump(
                node, annotate_fields=True, include_attributes=False
            ).encode("utf-8")
        ).hexdigest()
        for name, node in extracted_nodes.items()
    }
    definitions = {
        name: ast.get_source_segment(source, node)
        for name, node in extracted_nodes.items()
    }

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    audit_is_pure_literal = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    extracted_audit = tuple(ast.literal_eval(audit_node))

    recurrent = functions["recurrent_candidate_census"]
    close = functions["close_candidate_census"]
    enforcement = functions["enforcement_candidate_census"]
    expected_test_dicts = {
        "candidate_1": {
            "totality": False,
            "invariance": True,
            "identification": False,
        },
        "candidate_2": {
            "totality": False,
            "invariance": True,
            "identification": False,
        },
        "candidate_3": {
            "totality": True,
            "invariance": True,
            "identification": True,
        },
    }
    candidate_claims = {
        "candidate_1": {
            "definition": keyed_literal(recurrent, "definition"),
            "tests": expected_test_dicts["candidate_1"],
            "selected_counts": [0, 0, 0, 0],
            "fixtures": 4,
            "alternatives": 12,
        },
        "candidate_2": {
            "definition": keyed_literal(close, "definition"),
            "tests": expected_test_dicts["candidate_2"],
            "selected_counts": [508, 508],
            "active_pre": 508,
            "active_post": 510,
        },
        "candidate_3": {
            "definition": keyed_literal(enforcement, "definition"),
            "tests": expected_test_dicts["candidate_3"],
            "selected_count_range": [1, 1],
            "fixtures": 38,
            "alternatives": 2578,
            "supplied_choice": [0],
        },
    }
    claims_present = (
        expected_test_dicts["candidate_1"] in literal_dicts(recurrent)
        and expected_test_dicts["candidate_2"] in literal_dicts(close)
        and expected_test_dicts["candidate_3"] in literal_dicts(enforcement)
        and has_literal(recurrent, [0, 0, 0, 0])
        and has_literal(close, [508, 508])
        and has_literal(enforcement, [1, 1])
        and has_literal(enforcement, 2578)
        and keyed_literal(enforcement, "reference") == [0]
    )

    winner = extracted_nodes["enforcement_lineage_selector"]
    call_counts: dict[str, int] = {}
    for node in ast.walk(winner):
        if isinstance(node, ast.Call):
            name = dotted_name(node.func)
            if name is not None:
                call_counts[name] = call_counts.get(name, 0) + 1
    winner_arguments = tuple(argument.arg for argument in winner.args.args)
    composition = {
        "arguments": list(winner_arguments),
        "run_orbit_calls": call_counts.get("K.run_orbit", 0),
        "unpack_state_calls": call_counts.get("K.M.unpack_state", 0),
        "required_K_attributes": sorted(
            {
                dotted_name(node)
                for node in ast.walk(winner)
                if isinstance(node, ast.Attribute)
                and dotted_name(node) is not None
                and dotted_name(node).startswith("K.")
            }
        ),
        "definition_sha256": definition_hashes[
            "enforcement_lineage_selector"
        ],
    }

    outcome = functions["outcome_certificate"]
    outcome_dicts = literal_dicts(outcome)
    boundary = next(
        row for row in outcome_dicts
        if set(row) == set(EXPECTED_BOUNDARY)
    )
    conditions = next(
        ast.literal_eval(child)
        for child in ast.walk(outcome)
        if isinstance(child, ast.List)
        and ast.literal_eval(child) == EXPECTED_CONDITIONS
    )
    import_aliases = {}
    for node in tree.body:
        if not isinstance(node, ast.Import):
            continue
        for alias in node.names:
            import_aliases[alias.asname or alias.name] = alias.name

    ok = (
        audit_is_pure_literal
        and extracted_audit == EXPECTED_AUDIT_INPUT_PATHS
        and definition_hashes == EXPECTED_DEFINITION_HASHES
        and claims_present
        and winner_arguments
        == ("program", "before", "expected", "bank_count", "alternatives")
        and call_counts.get("K.run_orbit") == 2
        and call_counts.get("K.M.unpack_state") == 1
        and boundary == EXPECTED_BOUNDARY
        and conditions == EXPECTED_CONDITIONS
        and import_aliases.get("H335")
        == "protected_recurrent_actual_history_selection_cycle335_2026_07_18"
        and import_aliases.get("O332")
        == "physical_transition_occurrence_close_tournament_cycle332_2026_07_18"
        and import_aliases.get("K")
        == "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
    )
    return ok, {
        "audit_tuple": list(extracted_audit),
        "audit_tuple_pure_literal": audit_is_pure_literal,
        "candidate_definition_sha256": definition_hashes,
        "candidate_definitions": definitions,
        "declared_results": candidate_claims,
        "winner_exact_composition": composition,
        "boundary": boundary,
        "conditions_verbatim": conditions,
    }


def own_rotate_right(slots: tuple[object, ...]) -> tuple[object, ...]:
    values = list(slots)
    for left in reversed(range(len(values) - 1)):
        values[left], values[left + 1] = values[left + 1], values[left]
    return tuple(values)


def own_recurrent_selector(
    slots: tuple[tuple[int, int, int], ...],
) -> tuple[int, ...]:
    selected = []
    for member, value in enumerate(slots):
        if value != H335.ONE:
            continue
        probe = tuple(
            H335.ONE if index == member else H335.ZERO
            for index in range(len(slots))
        )
        if own_rotate_right(probe)[member] == H335.ONE:
            selected.append(member)
    return tuple(selected)


def own_transition_witness(program: object, pre: int, post: int) -> int:
    ambient = len(program.sidecar.stream_mapping)
    if not 0 <= pre < ambient or not 0 <= post < ambient:
        raise ValueError("boundary outside independent recount domain")
    return int(program.truth[pre * ambient + post])


def own_closed_flag(triple: tuple[int, ...]) -> int:
    return int(len(triple) == 3 and all(bit == 1 for bit in triple))


def own_close_certificate(
    pre_code: int,
    transition: int,
    post_code: int,
    match: int,
    ready: int,
) -> int:
    bits = (pre_code, transition, post_code, match, ready)
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("close inputs are not bits")
    return int(all(bits))


def failing_candidates_recount() -> tuple[bool, dict[str, object]]:
    initial = (H335.ONE, H335.ONE, H335.ONE, H335.ZERO)
    history = [initial]
    for _ in range(len(initial) - 1):
        history.append(own_rotate_right(history[-1]))
    recurrent_rows = []
    cyclic_failures = []
    for phase, slots in enumerate(history):
        alternatives = tuple(
            index for index, value in enumerate(slots) if value == H335.ONE
        )
        selected = own_recurrent_selector(slots)
        recurrent_rows.append(
            {
                "phase": phase,
                "alternatives": alternatives,
                "selected": selected,
                "supplied_reference": (phase,),
            }
        )
        for shift in range(len(slots)):
            rotated = slots[-shift:] + slots[:-shift] if shift else slots
            observed = own_recurrent_selector(rotated)
            expected = tuple(
                sorted((member + shift) % len(slots) for member in selected)
            )
            if observed != expected:
                cyclic_failures.append((phase, shift, observed, expected))

    close_rows = []
    for length in (3, 6):
        program = O332.compile_transition_program(length)
        fixture = O332.c329.build_fixture(length)
        match, ready = O332.c329.route_outputs(fixture, "syndrome")
        active = tuple(int(row) for row in program.active_rows)
        active_nonvacuum = tuple(
            row for row in active if bool(program.nonvacuum[row])
        )
        alternatives = tuple(
            (pre, post)
            for pre in active_nonvacuum
            for post in active
        )
        closed = own_closed_flag(H335.ONE)
        selected = tuple(
            (pre, post)
            for pre, post in alternatives
            if own_close_certificate(
                closed,
                own_transition_witness(program, pre, post),
                closed,
                int(match),
                int(ready),
            )
        )
        reference_pre = active_nonvacuum[0]
        reference = (
            (reference_pre, int(program.sidecar.stream_mapping[reference_pre])),
        )
        close_rows.append(
            {
                "L": length,
                "active_pre": len(active_nonvacuum),
                "active_post": len(active),
                "alternative_count": len(alternatives),
                "selected_count": len(selected),
                "selected_sha256": digest(selected),
                "first_selected": selected[0] if selected else None,
                "last_selected": selected[-1] if selected else None,
                "supplied_reference": reference,
                "reference_is_selected": reference[0] in selected,
            }
        )

    recurrent_tests = {
        "totality": all(len(row["selected"]) == 1 for row in recurrent_rows),
        "invariance": not cyclic_failures,
        "identification": all(
            row["selected"] == row["supplied_reference"]
            for row in recurrent_rows
        ),
    }
    close_tests = {
        "totality": all(row["selected_count"] == 1 for row in close_rows),
        "identification": all(
            row["selected_count"] == 1
            and row["first_selected"] == row["supplied_reference"][0]
            for row in close_rows
        ),
    }
    recurrent_counterexamples = [
        {
            "phase": row["phase"],
            "available": len(row["alternatives"]),
            "selected": list(row["selected"]),
            "supplied_reference": list(row["supplied_reference"]),
        }
        for row in recurrent_rows
    ]
    ok = (
        [len(row["selected"]) for row in recurrent_rows] == [0, 0, 0, 0]
        and sum(len(row["alternatives"]) for row in recurrent_rows) == 12
        and recurrent_tests
        == {
            "totality": False,
            "invariance": True,
            "identification": False,
        }
        and not cyclic_failures
        and len(close_rows) == 2
        and all(row["active_pre"] == 508 for row in close_rows)
        and all(row["active_post"] == 510 for row in close_rows)
        and all(row["alternative_count"] == 508 * 510 for row in close_rows)
        and [row["selected_count"] for row in close_rows] == [508, 508]
        and close_tests == {"totality": False, "identification": False}
    )
    return ok, {
        "candidate_1": {
            "tests": recurrent_tests,
            "exact_totality_counterexamples": recurrent_counterexamples,
            "alternatives_exhausted": 12,
        },
        "candidate_2": {
            "tests": close_tests,
            "survivor_census": close_rows,
            "total_alternatives_exhausted": sum(
                row["alternative_count"] for row in close_rows
            ),
        },
    }


def own_run_orbit(
    data: tuple[int, ...],
    program: tuple[object, ...],
    position: int,
    *,
    reverse: bool = False,
    q_order: tuple[int, ...] | None = None,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    stations = len(program)
    if not 0 <= position < stations:
        raise ValueError("token position outside program")
    if q_order is not None and tuple(sorted(q_order)) != tuple(range(stations)):
        raise ValueError("Q order is not a station permutation")
    output = data
    for step in range(stations):
        live = (
            (position - step - 1) % stations
            if reverse
            else (position + step) % stations
        )
        if q_order is None:
            macro = K.mapped_macro(program[live])
            if reverse:
                macro = tuple(reversed(macro))
            output = K.A.apply_semantic(output, macro)
        else:
            for station in q_order:
                if station == live:
                    macro = K.mapped_macro(program[station])
                    if reverse:
                        macro = tuple(reversed(macro))
                    output = K.A.apply_semantic(output, macro)
    rail_a = tuple(int(index == position) for index in range(stations))
    rail_b = (0,) * stations
    return output, rail_a, rail_b


def own_dirty(after: tuple[int, ...], bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    dirty_bank_wires = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    return any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for wire in dirty_bank_wires
            ),
            any(any(link) for link in links),
        )
    )


def own_enforcement_selector(
    program: tuple[object, ...],
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
    alternatives: tuple[int, ...],
    *,
    q_order: tuple[int, ...] | None = None,
) -> tuple[tuple[int, ...], dict[str, int]]:
    selected = []
    exclusions = {
        "wrong_postimage_or_rails": 0,
        "failed_inverse_or_dirty": 0,
        "survived": 0,
    }
    for position in alternatives:
        tokens = tuple(
            int(index == position) for index in range(len(program))
        )
        zeros = (0,) * len(program)
        after, rail_a, rail_b = own_run_orbit(
            before, program, position, q_order=q_order
        )
        if after != expected or rail_a != tokens or rail_b != zeros:
            exclusions["wrong_postimage_or_rails"] += 1
            continue
        restored, inverse_a, inverse_b = own_run_orbit(
            after,
            program,
            position,
            reverse=True,
            q_order=q_order,
        )
        if (
            restored != before
            or inverse_a != rail_a
            or inverse_b != rail_b
            or own_dirty(after, bank_count)
        ):
            exclusions["failed_inverse_or_dirty"] += 1
            continue
        selected.append(position)
        exclusions["survived"] += 1
    return tuple(selected), exclusions


def own_epoch_fixtures(bank_count: int) -> tuple[dict[str, object], ...]:
    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        expected = K.A.apply_semantic(
            before, K.M.global_allocator_word(bank_count)
        )
        rows.append(
            {
                "bank_count": bank_count,
                "event": event,
                "direction": direction,
                "program": program,
                "before": before,
                "expected": expected,
            }
        )
        state = expected
    return tuple(rows)


def winner_recount() -> tuple[bool, dict[str, object]]:
    rows = []
    totals = {
        "wrong_postimage_or_rails": 0,
        "failed_inverse_or_dirty": 0,
        "survived": 0,
    }
    for bank_count in (2, 5, 12):
        for fixture in own_epoch_fixtures(bank_count):
            program = fixture["program"]
            alternatives = tuple(range(len(program)))
            selected, exclusions = own_enforcement_selector(
                program,
                fixture["before"],
                fixture["expected"],
                bank_count,
                alternatives,
            )
            for key, value in exclusions.items():
                totals[key] += value
            rows.append(
                {
                    "bank_count": bank_count,
                    "event": fixture["event"],
                    "alternatives": len(alternatives),
                    "selected": selected,
                    "supplied_choice": (0,),
                }
            )
    fixture_counts = {
        str(bank_count): sum(row["bank_count"] == bank_count for row in rows)
        for bank_count in (2, 5, 12)
    }
    alternatives_exhausted = sum(row["alternatives"] for row in rows)
    survivor_counts = [len(row["selected"]) for row in rows]
    identification_failures = [
        (row["bank_count"], row["event"], row["selected"])
        for row in rows
        if row["selected"] != row["supplied_choice"]
    ]
    ok = (
        len(rows) == 38
        and fixture_counts == {"2": 4, "5": 10, "12": 24}
        and alternatives_exhausted == 2578
        and survivor_counts == [1] * 38
        and not identification_failures
        and totals["survived"] == 38
        and sum(totals.values()) == alternatives_exhausted
    )
    return ok, {
        "epochs_exhausted": len(rows),
        "fixture_counts_by_banks": fixture_counts,
        "alternatives_exhausted": alternatives_exhausted,
        "survivor_count_range": [
            min(survivor_counts), max(survivor_counts)
        ],
        "identification_failures": identification_failures,
        "per_alternative_exclusion_totals": totals,
        "choice_digest": digest(
            [
                (row["bank_count"], row["event"], row["selected"])
                for row in rows
            ]
        ),
    }


def uniqueness_attack() -> tuple[bool, dict[str, object]]:
    rotation_rows = []
    ties = []
    nulls = []
    alternatives_attacked = 0
    for bank_count in (2, 5, 12):
        fixture = own_epoch_fixtures(bank_count)[0]
        program = fixture["program"]
        stations = len(program)
        for shift in range(stations):
            rotated = program[shift:] + program[:shift]
            alternatives = tuple(range(stations))
            selected, _exclusions = own_enforcement_selector(
                rotated,
                fixture["before"],
                fixture["expected"],
                bank_count,
                alternatives,
            )
            expected_image = ((stations - shift) % stations,)
            row = {
                "bank_count": bank_count,
                "shift": shift,
                "selected": selected,
                "expected_image": expected_image,
            }
            rotation_rows.append(row)
            alternatives_attacked += stations
            if len(selected) > 1:
                ties.append(row)
            elif not selected:
                nulls.append(row)

    geometry_variants = 0
    geometry_failures = []
    frames = K.C712.C709.F.base.proper_cubic_frames()
    translations = ((3, -2, 1), (-5, 4, 2))
    for bank_count in (2, 5, 12):
        _program, track = K.held_physical_program_and_track(bank_count)
        station_sites = track[::2]
        source_site = station_sites[0]
        for frame_index, frame in enumerate(frames):
            moved = tuple(
                tuple(int(value) for value in frame @ site)
                for site in station_sites
            )
            source_image = tuple(int(value) for value in frame @ source_site)
            geometry_variants += 1
            if len(set(moved)) != len(station_sites) or source_image != moved[0]:
                geometry_failures.append(
                    ("frame", bank_count, frame_index)
                )
        for translation in translations:
            moved = tuple(
                tuple(
                    site[axis] + translation[axis] for axis in range(3)
                )
                for site in station_sites
            )
            source_image = tuple(
                source_site[axis] + translation[axis] for axis in range(3)
            )
            geometry_variants += 1
            if len(set(moved)) != len(station_sites) or source_image != moved[0]:
                geometry_failures.append(
                    ("translation", bank_count, translation)
                )

    conjugation_failures = [
        row for row in rotation_rows
        if row["selected"] != row["expected_image"]
    ]
    ok = (
        len(rotation_rows) == 137
        and alternatives_attacked == 11 * 11 + 35 * 35 + 91 * 91
        and geometry_variants == 78
        and not ties
        and not nulls
        and not conjugation_failures
        and not geometry_failures
    )
    public = {
        "declared_bounded_family": {
            "representative_epoch_cyclic_boundary_permutations": len(
                rotation_rows
            ),
            "per_alternative_exclusions_recounted": alternatives_attacked,
            "proper_cubic_frame_images": 72,
            "translation_images": 6,
            "total_constructed_variants": len(rotation_rows)
            + geometry_variants,
        },
        "ties_found": len(ties),
        "null_survivor_variants": len(nulls),
        "conjugation_failures": len(conjugation_failures)
        + len(geometry_failures),
        "result": (
            "TIE FOUND — FIXTURE-SCOPE TOTALITY REFUTED"
            if ties
            else "NO TIES IN THE EXHAUSTED BOUNDED FAMILY"
        ),
        "refutes_fixture_scope_totality": bool(ties),
        "_rotation_rows": rotation_rows,
        "_geometry_failures": geometry_failures,
    }
    return ok, public


def invariance_recount(
    attack: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    rotation_rows = attack["_rotation_rows"]
    cyclic_failures = [
        {
            "bank_count": row["bank_count"],
            "shift": row["shift"],
            "selected": row["selected"],
            "expected": row["expected_image"],
        }
        for row in rotation_rows
        if row["selected"] != row["expected_image"]
    ]
    q_order_failures = []
    q_cases = 0
    for bank_count in (2, 5, 12):
        for fixture in own_epoch_fixtures(bank_count):
            program = fixture["program"]
            reverse_order = tuple(reversed(range(len(program))))
            selected, _ = own_enforcement_selector(
                program,
                fixture["before"],
                fixture["expected"],
                bank_count,
                (0,),
                q_order=reverse_order,
            )
            q_cases += 1
            if selected != (0,):
                q_order_failures.append(
                    (bank_count, fixture["event"], selected)
                )
    geometry_failures = attack["_geometry_failures"]
    ok = (
        len(rotation_rows) == 137
        and not cyclic_failures
        and q_cases == 38
        and not q_order_failures
        and not geometry_failures
    )
    return ok, {
        "cyclic_boundary_conjugations": len(rotation_rows),
        "cyclic_failures": cyclic_failures,
        "Q_station_order_conjugations": q_cases,
        "Q_station_order_failures": q_order_failures,
        "proper_cubic_frame_conjugations": 72,
        "translation_conjugations": 6,
        "spatial_failures": geometry_failures,
    }


def discipline(
    extracted: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    loaded_files = {
        Path(module.__file__).resolve()
        for module in tuple(sys.modules.values())
        if getattr(module, "__file__", None)
    }
    primary_imported = (
        PRIMARY_MODULE in sys.modules or PRIMARY_PATH.resolve() in loaded_files
    )
    boundary = extracted["boundary"]
    boundary_keys = list(boundary)
    expected_keys = list(EXPECTED_BOUNDARY)
    conditions = extracted["conditions_verbatim"]
    ok = (
        AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == "docs/ACTUAL_SELECTOR_STRETCH_CYCLE750_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        and AUDIT_INPUT_PATHS == EXPECTED_AUDIT_INPUT_PATHS
        and not primary_imported
        and boundary == EXPECTED_BOUNDARY
        and boundary_keys == expected_keys
        and conditions == EXPECTED_CONDITIONS
        and boundary["fixture_scope_only"] is True
        and boundary[
            "source_boundary_and_orientation_remain_supplied"
        ] is True
        and boundary["autonomous_genesis_or_enforcement_derived"] is False
        and boundary["w3_closed"] is False
    )
    return ok, {
        "blocklist": list(BLOCKLIST),
        "blocklist_clean": not primary_imported,
        "boundary_keys_verbatim": boundary_keys,
        "fixture_scope_only": boundary["fixture_scope_only"],
        "supplied_genesis_orientation_source": {
            "one_token_and_clean_genesis":
                conditions[0] == EXPECTED_CONDITIONS[0]
                and conditions[3] == EXPECTED_CONDITIONS[3],
            "source_and_orientation":
                boundary[
                    "source_boundary_and_orientation_remain_supplied"
                ],
            "autonomous_genesis_or_enforcement_derived":
                boundary["autonomous_genesis_or_enforcement_derived"],
        },
        "W3_as_wall_still_open_pending_composition":
            boundary["w3_closed"] is False,
    }


def public_detail(value: object) -> object:
    if not isinstance(value, dict):
        return value
    return {
        key: item for key, item in value.items()
        if not key.startswith("_")
    }


def emit(label: str, passed: bool, detail: object) -> None:
    print(
        "PASS" if passed else "FAIL",
        label,
        "::",
        json.dumps(
            public_detail(detail),
            sort_keys=True,
            separators=(",", ":"),
            default=str,
        ),
    )


def main() -> int:
    failures = 0
    results: dict[str, dict[str, object]] = {}

    def run(label: str, function, *args):
        nonlocal failures
        try:
            passed, detail = function(*args)
        except Exception as exc:
            passed = False
            detail = {
                "exception": type(exc).__name__,
                "message": str(exc),
            }
        failures += not passed
        results[label] = detail
        emit(label, passed, detail)
        return detail

    extracted = run("extraction", extraction)
    run("failing_candidates_recount", failing_candidates_recount)
    run("winner_recount", winner_recount)
    attack = run("uniqueness_attack", uniqueness_attack)
    run("invariance_recount", invariance_recount, attack)
    run("discipline", discipline, extracted)

    elapsed = monotonic() - START
    runtime_ok = elapsed < AUDIT_TIMEOUT_SEC
    failures += not runtime_ok
    emit(
        "runtime",
        runtime_ok,
        {
            "runtime_seconds": round(elapsed, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_contract_bytes_lt": 150000,
        },
    )
    emit(
        "terminal",
        failures == 0,
        {
            "certificate_failures": failures,
            "result": (
                "CYCLE750_ACTUAL_INDEPENDENT_CHECK_PASS"
                if failures == 0
                else "CYCLE750_ACTUAL_INDEPENDENT_CHECK_FAIL"
            ),
        },
    )
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
