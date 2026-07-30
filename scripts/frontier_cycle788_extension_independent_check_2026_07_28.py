#!/usr/bin/env python3
"""Cycle 788 independent adversarial check: attack declared supplies."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_TEXT_PATH = (
    ROOT / "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py"
)
BLOCKLISTED_MODULE = (
    "frontier_cycle788_selector_scope_extension_2026_07_28"
)
START = monotonic()
PASS = 0
FAIL = 0
STDOUT_BYTES = 0


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname == BLOCKLISTED_MODULE:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py":
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py":
        "5a45d24c439fe5dc4903c1064213ad8a287ed489ed5736f7a18b34e4cc03db5f",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py":
        "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def emit(*parts: object) -> None:
    global STDOUT_BYTES
    line = " ".join(str(part) for part in parts)
    STDOUT_BYTES += len((line + "\n").encode("utf-8"))
    print(line)


def check(label: str, condition: bool, detail: object) -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        emit("PASS", label, "::", compact(detail))
    else:
        FAIL += 1
        emit("FAIL", label, "::", compact(detail))
    return condition


def assignment_nodes(tree: ast.Module) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
            for target in targets:
                if isinstance(target, ast.Name):
                    found[target.id] = node.value
    return found


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(f"missing function {name}")


def function_assignments(node: ast.FunctionDef) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for child in node.body:
        if isinstance(child, (ast.Assign, ast.AnnAssign)):
            targets = (
                child.targets
                if isinstance(child, ast.Assign)
                else (child.target,)
            )
            for target in targets:
                if isinstance(target, ast.Name):
                    found[target.id] = child.value
    return found


def rendered_text(node: ast.AST, environment: dict[str, object]) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant):
                parts.append(str(value.value))
            elif isinstance(value, ast.FormattedValue):
                if isinstance(value.value, ast.Name):
                    parts.append(str(environment[value.value.id]))
                else:
                    raise AssertionError(ast.dump(value.value))
            else:
                raise AssertionError(ast.dump(value))
        return "".join(parts)
    raise AssertionError(ast.dump(node))


def extract_primary_text_claims() -> dict[str, object]:
    source = PRIMARY_TEXT_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    top = assignment_nodes(tree)
    extension = function_node(tree, "extension_fixture")
    local = function_assignments(extension)
    inherited_node = local["inherited_supplies"]
    new_node = local["new_supplies"]
    if not isinstance(inherited_node, ast.List) or not isinstance(new_node, ast.List):
        raise AssertionError("primary supplies are not literal lists")
    inherited = [
        rendered_text(item, {"bank_count": 3, "width": 3})
        for item in inherited_node.elts
    ]
    new = []
    for item in new_node.elts:
        if not isinstance(item, ast.Dict):
            raise AssertionError(ast.dump(item))
        rendered = {
            str(key.value): rendered_text(value, {"bank_count": 3, "width": 3})
            for key, value in zip(item.keys, item.values)
            if isinstance(key, ast.Constant)
        }
        new.append(rendered)
    expected_bank2 = ast.literal_eval(top["EXPECTED_BANK2_IDENTITY"])
    candidates = tuple(ast.literal_eval(top["NEW_CANDIDATES"]))
    return {
        "inherited": inherited,
        "new": new,
        "candidate_order": candidates,
        "expected_bank2_identity": expected_bank2,
        "primary_sha256": sha256(source.encode("utf-8")).hexdigest(),
    }


def literal_input_and_blocklist_audit() -> dict[str, object]:
    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source)
    top = assignment_nodes(own_tree)
    audit_node = top["AUDIT_INPUT_PATHS"]
    declared_node = top["DECLARED_INPUT_PATHS"]
    imported_names = []
    for node in own_tree.body:
        if isinstance(node, ast.Import):
            imported_names.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported_names.append(node.module or "")
    return {
        "audit_tuple_is_literal": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "declared_aliases_audit": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "all_audit_paths_exist": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "primary_import_ast_blocked": BLOCKLISTED_MODULE not in imported_names,
        "primary_not_loaded": BLOCKLISTED_MODULE not in sys.modules,
        "runtime_import_blocker_installed": PRIMARY_BLOCKER in sys.meta_path,
        "imported_landed_modules": [
            name for name in imported_names if name.startswith("frontier_")
            or name.startswith("protected_")
            or name.startswith("physical_")
        ],
    }


def source_anchors() -> dict[str, str]:
    return {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }


def call_name(node: ast.Call) -> str:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return ""


def ranges_over_name(node: ast.AST, name: str) -> bool:
    return any(
        isinstance(child, ast.Call)
        and call_name(child) == "range"
        and any(
            isinstance(descendant, ast.Name) and descendant.id == name
            for argument in child.args
            for descendant in ast.walk(argument)
        )
        for child in ast.walk(node)
    )


def tuple_loop_values(node: ast.AST) -> list[tuple[int, ...]]:
    values = []
    for child in ast.walk(node):
        if isinstance(child, ast.For) and isinstance(child.iter, ast.Tuple):
            try:
                value = tuple(ast.literal_eval(child.iter))
            except (ValueError, TypeError):
                continue
            if all(isinstance(item, int) for item in value):
                values.append(value)
    return values


def constructor_generality_audit() -> dict[str, object]:
    selector_tree = ast.parse(
        (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    )
    controller_tree = ast.parse(
        (ROOT / AUDIT_INPUT_PATHS[3]).read_text(encoding="utf-8")
    )
    interleaved = function_node(controller_tree, "interleaved_program")
    held = function_node(controller_tree, "held_certificate")
    physical = function_node(
        controller_tree, "held_physical_program_and_track"
    )
    epochs = function_node(selector_tree, "k_epoch_fixtures")
    census = function_node(selector_tree, "enforcement_candidate_census")

    branch_constants = sorted(
        {
            int(child.comparators[0].value)
            for child in ast.walk(physical)
            if isinstance(child, ast.Compare)
            and isinstance(child.left, ast.Name)
            and child.left.id == "bank_count"
            and len(child.ops) == len(child.comparators) == 1
            and isinstance(child.ops[0], ast.Eq)
            and isinstance(child.comparators[0], ast.Constant)
            and isinstance(child.comparators[0].value, int)
        }
    )
    physical_has_else_raise = any(
        isinstance(child, ast.Raise)
        and isinstance(child.exc, ast.Call)
        and call_name(child.exc) == "ValueError"
        for child in ast.walk(physical)
    )
    checks = {
        "interleaved_program_parameter_bank_count":
            interleaved.args.args[0].arg == "bank_count"
            and ranges_over_name(interleaved, "bank_count"),
        "held_certificate_parameter_bank_count":
            held.args.args[0].arg == "bank_count"
            and ranges_over_name(held, "bank_count"),
        "k_epoch_fixtures_parameter_bank_count":
            epochs.args.args[0].arg == "bank_count"
            and ranges_over_name(epochs, "bank_count"),
        "physical_fixture_branches_exactly_2_5_12":
            branch_constants == [2, 5, 12] and physical_has_else_raise,
        "cycle750_census_holds_2_5_12":
            (2, 5, 12) in tuple_loop_values(census),
    }
    return {
        "classification": (
            "c_mixed"
            if all(checks.values())
            else "primary_c_verdict_not_verified"
        ),
        "logical_constructor_finding": (
            "interleaved_program(bank_count), held_certificate(bank_count), "
            "and k_epoch_fixtures(bank_count) range over bank_count"
        ),
        "physical_fixture_finding": (
            "held_physical_program_and_track(bank_count) has only explicit "
            "2/5/12 branches and an else ValueError; Cycle 750 separately "
            "censuses the literal tuple (2,5,12)"
        ),
        "physical_branch_constants": branch_constants,
        "checks": checks,
    }


def own_epoch_fixtures(
    bank_count: int,
    *,
    event_phase: int = 0,
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...], tuple[int, ...]], ...]:
    banks, links = K719.B.chain_genesis(bank_count)
    state = K719.M.pack_state(banks, links)
    word = K719.M.global_allocator_word(bank_count)
    rows = []
    for event in range(2 * bank_count):
        direction = (
            (1, 0) if (event + event_phase) % 2 == 0 else (0, 1)
        )
        before = K719.M.prepare_endpoint(state, direction)
        expected = K719.A.apply_semantic(before, word)
        rows.append((event, direction, before, expected))
        state = expected
    return tuple(rows)


def rotate_left(values: tuple, amount: int) -> tuple:
    amount %= len(values)
    return values[amount:] + values[:amount]


def q_order(stations: int, mode: str) -> tuple[int, ...] | None:
    if mode == "ascending":
        return None
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return tuple(range(0, stations, 2)) + tuple(range(1, stations, 2))
    raise ValueError(mode)


def advance_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(len(a)):
        a[station], b[station] = b[station], a[station]
    for station in range(len(a)):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def retreat_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in reversed(range(len(a))):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    for station in reversed(range(len(a))):
        a[station], b[station] = b[station], a[station]
    return tuple(a), tuple(b)


def apply_live_macros(
    data: tuple[int, ...],
    program: tuple,
    a_tokens: tuple[int, ...],
    *,
    reverse: bool,
    order_mode: str,
) -> tuple[int, ...]:
    order = q_order(len(program), order_mode)
    if order is None:
        order = (
            tuple(reversed(range(len(program))))
            if reverse
            else tuple(range(len(program)))
        )
    output = data
    for station in order:
        if a_tokens[station]:
            word = K719.mapped_macro(program[station])
            if reverse:
                word = tuple(reversed(word))
            output = K719.A.apply_semantic(output, word)
    return output


def run_rq_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    order_mode: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    stations = len(program)
    a = tuple(int(index == token_position) for index in range(stations))
    b = (0,) * stations
    output = data
    for _step in range(stations):
        if reverse:
            output = apply_live_macros(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
            a, b = retreat_rails(a, b)
        else:
            a, b = advance_rails(a, b)
            output = apply_live_macros(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
    return output, a, b


def run_choice_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    layer_order: str,
    order_mode: str,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    if layer_order == "Q_then_R":
        station_order = q_order(len(program), order_mode)
        orders = (
            None
            if station_order is None
            else (station_order,) * len(program)
        )
        output, a, b, _trace = K719.run_orbit(
            data,
            program,
            token_positions=(token_position,),
            reverse=reverse,
            q_orders=orders,
        )
        return output, a, b
    if layer_order == "R_then_Q":
        return run_rq_orbit(
            data,
            program,
            token_position=token_position,
            reverse=reverse,
            order_mode=order_mode,
        )
    raise ValueError(layer_order)


def postimage_clean(after: tuple[int, ...], bank_count: int) -> bool:
    banks, links = K719.M.unpack_state(after, bank_count)
    bank_dirty = any(
        bank[wire]
        for bank in banks
        for wire in (
            K719.A.POINTER,
            K719.A.U_TO_V,
            K719.A.V_TO_U,
            K719.A.DIRECTION_OK,
            *K719.A.FRESH,
            *K719.A.ZERO_WORK,
            K719.A.TOKEN_OK,
        )
    )
    return not any(
        (
            after[K719.R3.X.SOURCE_POINTER],
            bank_dirty,
            any(any(link) for link in links),
        )
    )


def station_exclusions(
    program: tuple,
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
    position: int,
    *,
    layer_order: str,
    order_mode: str,
) -> dict[str, bool]:
    tokens = tuple(int(index == position) for index in range(len(program)))
    zeros = (0,) * len(program)
    after, rail_a, rail_b = run_choice_orbit(
        before,
        program,
        token_position=position,
        reverse=False,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    restored, inverse_a, inverse_b = run_choice_orbit(
        after,
        program,
        token_position=position,
        reverse=True,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    return {
        "composition": after == expected,
        "rail": rail_a == tokens and rail_b == zeros,
        "inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "postimage": postimage_clean(after, bank_count),
    }


def selector_battery(
    bank_count: int,
    *,
    program_rotation: int = 0,
    event_phase: int = 0,
    layer_order: str = "Q_then_R",
    order_mode: str = "ascending",
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    program = rotate_left(base_program, program_rotation)
    fixtures = own_epoch_fixtures(bank_count, event_phase=event_phase)
    rows = []
    masks: Counter[str] = Counter()
    landed_mismatches = []
    for event, direction, before, expected in fixtures:
        selected = []
        event_masks: Counter[str] = Counter()
        for position in range(len(program)):
            criteria = station_exclusions(
                program,
                before,
                expected,
                bank_count,
                position,
                layer_order=layer_order,
                order_mode=order_mode,
            )
            failed = tuple(name for name, passed in criteria.items() if not passed)
            mask = "+".join(failed) if failed else "survivor"
            masks[mask] += 1
            event_masks[mask] += 1
            if not failed:
                selected.append(position)
        selected_tuple = tuple(selected)
        if (
            program_rotation == 0
            and event_phase == 0
            and layer_order == "Q_then_R"
            and order_mode == "ascending"
        ):
            landed = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                tuple(range(len(program))),
            )
            if selected_tuple != landed:
                landed_mismatches.append(event)
        adapter = tuple(
            (alternative, int(alternative in selected_tuple))
            for alternative in range(len(program))
        )
        rows.append(
            {
                "event": event,
                "direction": list(direction),
                "selected": list(selected_tuple),
                "actual_members": [
                    alternative for alternative, flag in adapter if flag
                ],
                "exclusion_masks": dict(sorted(event_masks.items())),
            }
        )
    signature = [row["selected"] for row in rows]
    return {
        "banks": bank_count,
        "epochs": len(rows),
        "program_stations": len(program),
        "alternatives_exhausted": len(rows) * len(program),
        "selector_outputs": rows,
        "survivor_signature": signature,
        "selected_count_range": [
            min(len(row) for row in signature),
            max(len(row) for row in signature),
        ],
        "tie_epochs": [
            row["event"] for row in rows if len(row["selected"]) > 1
        ],
        "empty_epochs": [
            row["event"] for row in rows if not row["selected"]
        ],
        "exclusion_mask_census": dict(sorted(masks.items())),
        "landed_selector_mismatches": landed_mismatches,
        "settings": {
            "program_rotation": program_rotation,
            "event_phase": event_phase,
            "layer_order": layer_order,
            "order_mode": order_mode,
        },
    }


def relative_track(track: tuple[tuple[int, int, int], ...]) -> tuple:
    origin = track[0]
    return tuple(
        tuple(site[axis] - origin[axis] for axis in range(3))
        for site in track
    )


def track_is_lawful(track: tuple, stations: int) -> bool:
    return (
        len(track) == 2 * stations
        and len(set(track)) == len(track)
        and all(
            sum(abs(a - b) for a, b in zip(left, right)) == 1
            for left, right in zip(track, track[1:] + track[:1])
        )
    )


def rectangle_for_bank3(
    *,
    width: int = 3,
    origin: tuple[int, int, int] = (-26, -7, -4),
    traversal: str = "canonical",
) -> tuple:
    stations = len(K719.interleaved_program(3))
    height = stations - width + 2
    track = K719.rectangle_track(width, height, origin=origin)
    if traversal == "reverse_from_source":
        track = track[:1] + tuple(reversed(track[1:]))
    elif traversal == "axis_swap":
        ox, oy, oz = origin
        track = tuple((ox + z - oz, y, oz + x - ox) for x, y, z in track)
    elif traversal != "canonical":
        raise ValueError(traversal)
    return track


def variation_record(
    choice: str,
    battery: dict[str, object],
    *,
    track: tuple | None = None,
) -> dict[str, object]:
    return {
        "choice": choice,
        "settings": battery["settings"],
        "signature": battery["survivor_signature"],
        "selected_count_range": battery["selected_count_range"],
        "ties": battery["tie_epochs"],
        "empty": battery["empty_epochs"],
        "lawful_track": (
            True
            if track is None
            else track_is_lawful(track, int(battery["program_stations"]))
        ),
    }


def run_supply_attack(primary: dict[str, object]) -> dict[str, object]:
    base = selector_battery(3)
    base_signature = base["survivor_signature"]
    stations = int(base["program_stations"])
    supplies = []

    source_rows = []
    for source_index in (0, 1, stations - 1):
        rotation = (-source_index) % stations
        battery = selector_battery(3, program_rotation=rotation)
        source_rows.append(
            variation_record(
                f"source_station_index={source_index}",
                battery,
            )
        )
    supplies.append(
        {
            "supply_id": "inherited_1",
            "declared_verbatim": primary["inherited"][0],
            "variations": source_rows,
        }
    )

    orientation_rows = []
    for rotation in (0, 1, stations - 1):
        battery = selector_battery(3, program_rotation=rotation)
        orientation_rows.append(
            variation_record(f"left_rotation={rotation}", battery)
        )
    supplies.append(
        {
            "supply_id": "inherited_2",
            "declared_verbatim": primary["inherited"][1],
            "variations": orientation_rows,
        }
    )

    order_rows = []
    for layer_order, order_mode in (
        ("Q_then_R", "ascending"),
        ("Q_then_R", "descending"),
        ("Q_then_R", "even_then_odd"),
        ("R_then_Q", "ascending"),
    ):
        battery = selector_battery(
            3,
            layer_order=layer_order,
            order_mode=order_mode,
        )
        order_rows.append(
            variation_record(
                f"layers={layer_order};Q_order={order_mode}",
                battery,
            )
        )
    supplies.append(
        {
            "supply_id": "inherited_3",
            "declared_verbatim": primary["inherited"][2],
            "variations": order_rows,
        }
    )

    event_rows = []
    for phase in (0, 1):
        battery = selector_battery(3, event_phase=phase)
        event_rows.append(
            variation_record(f"event_direction_phase={phase}", battery)
        )
    supplies.append(
        {
            "supply_id": "inherited_4",
            "declared_verbatim": primary["inherited"][3],
            "variations": event_rows,
        }
    )

    family_rows = []
    for traversal in ("canonical", "reverse_from_source", "axis_swap"):
        track = rectangle_for_bank3(traversal=traversal)
        battery = selector_battery(3)
        family_rows.append(
            variation_record(
                f"rectangle_traversal={traversal}",
                battery,
                track=track,
            )
        )
    supplies.append(
        {
            "supply_id": "new_1",
            "declared_verbatim": primary["new"][0],
            "variations": family_rows,
        }
    )

    width_rows = []
    for width in range(2, stations + 1):
        height = stations - width + 2
        track = rectangle_for_bank3(width=width)
        battery = selector_battery(3)
        width_rows.append(
            variation_record(
                f"rectangle_dimensions={width}x{height}",
                battery,
                track=track,
            )
        )
    supplies.append(
        {
            "supply_id": "new_2",
            "declared_verbatim": primary["new"][1],
            "variations": width_rows,
        }
    )

    origin_rows = []
    origins = (
        (-26, -7, -4),
        (-17, -7, 4),
        (-19, -7, 4),
        (0, 0, 0),
        (-23, -9, -3),
    )
    for origin in origins:
        track = rectangle_for_bank3(origin=origin)
        battery = selector_battery(3)
        origin_rows.append(
            variation_record(
                f"origin={origin}",
                battery,
                track=track,
            )
        )
    supplies.append(
        {
            "supply_id": "new_3",
            "declared_verbatim": primary["new"][2],
            "variations": origin_rows,
        }
    )

    selecting = []
    neutral = []
    for supply in supplies:
        signatures = {
            compact(row["signature"]) for row in supply["variations"]
        }
        supply["variation_count"] = len(supply["variations"])
        supply["distinct_survivor_signatures"] = len(signatures)
        supply["classification"] = (
            "SELECTS" if len(signatures) > 1 else "NEUTRAL"
        )
        supply["all_variations_lawful"] = all(
            row["lawful_track"] for row in supply["variations"]
        )
        if supply["classification"] == "SELECTS":
            selecting.append(supply["supply_id"])
        else:
            neutral.append(supply["supply_id"])
    return {
        "verdict": "SUPPLY_SELECTS" if selecting else "SUPPLY_NEUTRAL",
        "base_signature": base_signature,
        "base_battery": base,
        "supplies": supplies,
        "supply_count": len(supplies),
        "variation_count": sum(
            int(supply["variation_count"]) for supply in supplies
        ),
        "selecting_supply_ids": selecting,
        "neutral_supply_ids": neutral,
    }


def cyclic_recount(bank_count: int) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    _event, _direction, before, expected = own_epoch_fixtures(bank_count)[0]
    failures = []
    for rotation in range(len(base_program)):
        result = selector_battery(
            bank_count,
            program_rotation=rotation,
        )
        observed = tuple(result["survivor_signature"][0])
        expected_survivor = ((len(base_program) - rotation) % len(base_program),)
        if observed != expected_survivor:
            failures.append(
                {
                    "rotation": rotation,
                    "observed": list(observed),
                    "expected": list(expected_survivor),
                }
            )
    return {
        "cases": len(base_program),
        "failures": failures,
        "fixture_before_sha256": sha256(bytes(before)).hexdigest(),
        "fixture_expected_sha256": sha256(bytes(expected)).hexdigest(),
    }


def spatial_recount(track: tuple) -> dict[str, object]:
    station_sites = track[::2]
    source = station_sites[0]
    frames = K719.C712.C709.F.base.proper_cubic_frames()
    frame_failures = []
    for index, frame in enumerate(frames):
        moved = tuple(
            tuple(int(value) for value in frame @ site)
            for site in station_sites
        )
        selected = tuple(int(value) for value in frame @ source)
        if len(set(moved)) != len(moved) or selected != moved[0]:
            frame_failures.append(index)
    shifts = ((3, -2, 1), (-5, 4, 2))
    translation_failures = []
    for shift in shifts:
        moved = tuple(
            tuple(site[axis] + shift[axis] for axis in range(3))
            for site in station_sites
        )
        selected = tuple(
            source[axis] + shift[axis] for axis in range(3)
        )
        if len(set(moved)) != len(moved) or selected != moved[0]:
            translation_failures.append(shift)
    return {
        "proper_cubic_frame_cases": len(frames),
        "frame_failures": frame_failures,
        "translation_cases": len(shifts),
        "translation_failures": translation_failures,
        "rail_cycle_NN_failures": sum(
            sum(abs(a - b) for a, b in zip(left, right)) != 1
            for left, right in zip(track, track[1:] + track[:1])
        ),
    }


def q_order_recount(bank_count: int, base: dict[str, object]) -> dict[str, object]:
    descending = selector_battery(bank_count, order_mode="descending")
    return {
        "cases": int(base["epochs"]),
        "failures": [
            event
            for event, (left, right) in enumerate(
                zip(
                    base["survivor_signature"],
                    descending["survivor_signature"],
                )
            )
            if left != right
        ],
    }


def bank2_identity_recount(
    expected_identity: dict[str, object],
) -> dict[str, object]:
    program, track = K719.held_physical_program_and_track(2)
    base = selector_battery(2)
    cyclic = cyclic_recount(2)
    spatial = spatial_recount(track)
    q_control = q_order_recount(2, base)
    held_raw = K719.held_certificate(2)
    held = {
        key: value
        for key, value in held_raw.items()
        if key not in ("state", "chain")
    }
    projection = {
        "banks": 2,
        "epochs": base["epochs"],
        "program_stations": len(program),
        "alternatives_exhausted": base["alternatives_exhausted"],
        "selected_count_range": base["selected_count_range"],
        "selector_outputs": base["survivor_signature"],
        "exclusion_mask_census": base["exclusion_mask_census"],
        "q_station_order_cases": q_control["cases"],
        "q_station_order_failures": q_control["failures"],
        "cyclic_cases": cyclic["cases"],
        "cyclic_failures": cyclic["failures"],
        "proper_cubic_frame_cases": spatial["proper_cubic_frame_cases"],
        "spatial_translation_cases": spatial["translation_cases"],
        "spatial_failures": {
            "rail_cycle_NN_failures": spatial["rail_cycle_NN_failures"],
            "frame_failures": spatial["frame_failures"],
            "translation_failures": spatial["translation_failures"],
        },
        "held": held,
    }
    return {
        "observed": projection,
        "expected_from_primary_text": expected_identity,
        "identity_exact": projection == expected_identity,
        "base_landed_selector_mismatches":
            base["landed_selector_mismatches"],
    }


def logical_admission_row(bank_count: int) -> dict[str, object]:
    errors = []
    metrics = {}
    try:
        program = K719.interleaved_program(bank_count)
        metrics["program_stations"] = len(program)
    except Exception as exc:
        errors.append(f"interleaved_program:{type(exc).__name__}:{exc}")
        program = ()
    try:
        banks, links = K719.B.chain_genesis(bank_count)
        metrics["banks_built"] = len(banks)
        metrics["links_built"] = len(links)
        state = K719.M.pack_state(banks, links)
        metrics["state_wires"] = len(state)
    except Exception as exc:
        errors.append(f"chain_genesis_pack:{type(exc).__name__}:{exc}")
    try:
        word = K719.M.global_allocator_word(bank_count)
        metrics["law_gates"] = len(word)
    except Exception as exc:
        errors.append(f"global_allocator_word:{type(exc).__name__}:{exc}")
    metrics["epoch_condition"] = 2 * bank_count
    held_summary = None
    if not errors and bank_count >= 0:
        try:
            held = K719.held_certificate(bank_count)
            held_summary = {
                key: held[key]
                for key in (
                    "events",
                    "logical_failures",
                    "fixed_word_failures",
                    "inverse_failures",
                    "postimage_failures",
                    "token_return_failures",
                )
            }
        except Exception as exc:
            errors.append(f"held_certificate:{type(exc).__name__}:{exc}")
    try:
        K719.held_physical_program_and_track(bank_count)
        physical = "admitted"
    except Exception as exc:
        physical = f"{type(exc).__name__}:{exc}"
    return {
        "banks": bank_count,
        "general_logical_admitted": not errors,
        "metrics": metrics,
        "held_summary": held_summary,
        "held_physical_fixture": physical,
        "errors": errors,
    }


def admission_audit(primary: dict[str, object]) -> dict[str, object]:
    candidate_order = tuple(primary["candidate_order"])
    candidate_rows = [
        logical_admission_row(bank_count)
        for bank_count in candidate_order
    ]
    lower_rows = [logical_admission_row(bank_count) for bank_count in (0, 1, 2)]
    first_tried = next(
        (
            row["banks"]
            for row in candidate_rows
            if row["general_logical_admitted"]
        ),
        None,
    )
    positive_unheld = [
        row["banks"]
        for row in lower_rows + candidate_rows
        if row["banks"] > 0
        and row["banks"] not in (2, 5, 12)
        and row["general_logical_admitted"]
    ]
    smallest_positive_unheld = min(positive_unheld) if positive_unheld else None
    bank1_battery = selector_battery(1)
    bank1_new_events = (
        int(bank1_battery["epochs"])
        if bank1_battery["selected_count_range"] == [1, 1]
        and not bank1_battery["tie_epochs"]
        and not bank1_battery["empty_epochs"]
        else 0
    )
    return {
        "candidate_order": list(candidate_order),
        "candidate_rows": candidate_rows,
        "lower_boundary_rows": lower_rows,
        "first_admitted_in_primary_tried_order": first_tried,
        "smallest_positive_unheld_admitted": smallest_positive_unheld,
        "three_is_smallest_only_within_tried_order": (
            first_tried == 3 and smallest_positive_unheld != 3
        ),
        "primary_global_smallest_claim_matches":
            smallest_positive_unheld == 3,
        "bank1_selector_signature": bank1_battery["survivor_signature"],
        "bank1_new_selector_events": bank1_new_events,
        "bank0_note": (
            "the landed calls also accept bank_count=0 vacuously, but zero is "
            "excluded from the positive bank-size comparison"
        ),
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    primary = extract_primary_text_claims()
    for index, supplied in enumerate(primary["inherited"], start=1):
        emit(
            "DECLARED_SUPPLY_VERBATIM",
            f"inherited_{index}",
            "::",
            compact(supplied),
        )
    for index, supplied in enumerate(primary["new"], start=1):
        emit(
            "DECLARED_SUPPLY_VERBATIM",
            f"new_{index}",
            "::",
            compact(supplied),
        )

    supply = run_supply_attack(primary)
    for row in supply["supplies"]:
        emit(
            "SUPPLY_VARIATION_TABLE",
            row["supply_id"],
            row["classification"],
            "::",
            compact(
                {
                    "declared_verbatim": row["declared_verbatim"],
                    "variation_count": row["variation_count"],
                    "distinct_survivor_signatures":
                        row["distinct_survivor_signatures"],
                    "all_variations_lawful": row["all_variations_lawful"],
                    "variations": row["variations"],
                }
            ),
        )
    emit(
        supply["verdict"],
        "LOUD_FINDING",
        "::",
        compact(
            {
                "supply_count": supply["supply_count"],
                "variation_count": supply["variation_count"],
                "selecting_supply_ids": supply["selecting_supply_ids"],
                "neutral_supply_ids": supply["neutral_supply_ids"],
                "base_signature": supply["base_signature"],
                "finding_verbatim": (
                    "The bank-3 extension is supply-dependent: a different "
                    "lawful supplied source/orientation or Q/R layer choice "
                    "changes which alternatives survive; the six events are "
                    "convention-bearing."
                    if supply["verdict"] == "SUPPLY_SELECTS"
                    else "All bounded natural alternatives preserve the "
                    "bank-3 survivor set; the supplied choices are neutral."
                ),
            }
        ),
    )
    supply_complete = (
        supply["supply_count"] == 7
        and supply["variation_count"] == 38
        and all(
            supply_row["variation_count"] >= 2
            and supply_row["all_variations_lawful"]
            and all(
                len(variation["signature"]) == 6
                for variation in supply_row["variations"]
            )
            for supply_row in supply["supplies"]
        )
        and supply["verdict"] in {"SUPPLY_SELECTS", "SUPPLY_NEUTRAL"}
    )
    check(
        "CERTIFICATE_A_SUPPLY_FIDELITY_ATTACK",
        supply_complete,
        {
            "verdict": supply["verdict"],
            "supply_count": supply["supply_count"],
            "variation_count": supply["variation_count"],
            "selecting_supply_ids": supply["selecting_supply_ids"],
            "neutral_supply_ids": supply["neutral_supply_ids"],
        },
    )

    roles = constructor_generality_audit()
    emit(
        "CONSTRUCTOR_GENERALITY_FINDING_VERBATIM",
        "::",
        roles["logical_constructor_finding"],
    )
    emit(
        "PHYSICAL_FIXTURE_FINDING_VERBATIM",
        "::",
        roles["physical_fixture_finding"],
    )
    emit("C_VERDICT_FINDING", "::", roles["classification"])
    check(
        "CERTIFICATE_B_C_VERDICT_AUDIT",
        roles["classification"] == "c_mixed"
        and all(roles["checks"].values()),
        roles,
    )

    bank3 = supply["base_battery"]
    landed_fixtures = S750.k_epoch_fixtures(3)
    own_fixtures = own_epoch_fixtures(3)
    fixtures_exact = all(
        (
            own_event == landed_event
            and own_direction == landed_direction
            and landed_program == K719.interleaved_program(3)
            and own_before == landed_before
            and own_expected == landed_expected
        )
        for (
            own_event,
            own_direction,
            own_before,
            own_expected,
        ), (
            landed_event,
            landed_direction,
            landed_program,
            landed_before,
            landed_expected,
        ) in zip(own_fixtures, landed_fixtures)
    )
    bank3_expected_signature = [[0]] * 6
    bank3_recount_pass = (
        fixtures_exact
        and bank3["epochs"] == 6
        and bank3["program_stations"] == 19
        and bank3["alternatives_exhausted"] == 114
        and bank3["survivor_signature"] == bank3_expected_signature
        and bank3["selected_count_range"] == [1, 1]
        and not bank3["tie_epochs"]
        and not bank3["empty_epochs"]
        and not bank3["landed_selector_mismatches"]
        and bank3["exclusion_mask_census"]
        == {"composition+postimage": 108, "survivor": 6}
    )
    emit(
        "BANK3_BATTERY_RECOUNT",
        "::",
        compact(
            {
                "epochs": bank3["epochs"],
                "program_stations": bank3["program_stations"],
                "alternatives_exhausted": bank3["alternatives_exhausted"],
                "survivor_signature": bank3["survivor_signature"],
                "tie_epochs": bank3["tie_epochs"],
                "empty_epochs": bank3["empty_epochs"],
                "exclusion_mask_census": bank3["exclusion_mask_census"],
                "own_fixtures_equal_landed": fixtures_exact,
                "own_vs_landed_selector_mismatches":
                    bank3["landed_selector_mismatches"],
            }
        ),
    )
    check(
        "CERTIFICATE_C_BANK3_FULL_BATTERY_RECOUNT",
        bank3_recount_pass,
        {
            "six_unique_survivors_zero_ties_zero_empty":
                bank3_recount_pass,
            "survivor_signature": bank3["survivor_signature"],
            "exclusion_mask_census": bank3["exclusion_mask_census"],
        },
    )

    admission = admission_audit(primary)
    admission_disagrees = (
        admission["first_admitted_in_primary_tried_order"] == 3
        and admission["smallest_positive_unheld_admitted"] == 1
        and admission["bank1_selector_signature"] == [[0], [0]]
        and admission["bank1_new_selector_events"] == 2
        and admission["three_is_smallest_only_within_tried_order"]
        and not admission["primary_global_smallest_claim_matches"]
    )
    emit(
        "ADMISSION_DISAGREEMENT"
        if admission_disagrees
        else "ADMISSION_AGREEMENT",
        "LOUD_FINDING",
        "::",
        compact(admission),
    )
    check(
        "CERTIFICATE_D_ADMISSION_TABLE_AUDIT",
        admission_disagrees
        or (
            admission["first_admitted_in_primary_tried_order"] == 3
            and admission["smallest_positive_unheld_admitted"] == 3
        )
        or (
            admission["first_admitted_in_primary_tried_order"] == 1
            and admission["smallest_positive_unheld_admitted"] == 1
            and admission["bank1_new_selector_events"] == 2
        ),
        {
            "audit_outcome": (
                "DISAGREEMENT: bank 1 is the smallest positive unheld "
                "landed-logical admission and supplies two earlier unique "
                "selector events"
                if admission_disagrees
                else "AGREEMENT: bank 3 is smallest"
            ),
            "first_in_tried_order":
                admission["first_admitted_in_primary_tried_order"],
            "smallest_positive_unheld":
                admission["smallest_positive_unheld_admitted"],
            "bank1_new_selector_events":
                admission["bank1_new_selector_events"],
        },
    )

    controls = literal_input_and_blocklist_audit()
    anchors = source_anchors()
    bank2 = bank2_identity_recount(primary["expected_bank2_identity"])
    repeated_supply = run_supply_attack(primary)
    repeated_bank3 = selector_battery(3)
    deterministic = (
        repeated_supply == supply
        and repeated_bank3 == bank3
    )
    stable = {
        "supply": supply,
        "roles": roles,
        "bank3": bank3,
        "admission": admission,
        "bank2": bank2,
        "anchors": anchors,
        "controls": controls,
    }
    report_sha = sha256(compact(stable).encode("utf-8")).hexdigest()
    elapsed = monotonic() - START
    output_reserve = 8192
    bounds = (
        elapsed < AUDIT_TIMEOUT_SEC
        and STDOUT_BYTES + output_reserve < STDOUT_LIMIT_BYTES
    )
    control_pass = (
        all(controls.values())
        and anchors == EXPECTED_INPUT_SHA256
        and bank2["identity_exact"]
        and not bank2["base_landed_selector_mismatches"]
        and deterministic
        and bounds
    )
    check(
        "CERTIFICATE_E_CONTROLS_ANCHORS_BLOCKLIST_DETERMINISM_BOUNDS",
        control_pass,
        {
            "audit_input_paths": list(AUDIT_INPUT_PATHS),
            "input_controls": controls,
            "sha256": anchors,
            "sha_anchors_exact": anchors == EXPECTED_INPUT_SHA256,
            "bank2_identity_exact": bank2["identity_exact"],
            "bank2_observed": bank2["observed"],
            "deterministic": deterministic,
            "report_sha256": report_sha,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_certificate_e": STDOUT_BYTES,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "reserved_terminal_bytes": output_reserve,
        },
    )
    emit(
        "SUMMARY",
        "::",
        compact(
            {
                "status": "PASS" if FAIL == 0 else "FAIL",
                "supply_verdict": supply["verdict"],
                "supply_count": supply["supply_count"],
                "variation_count": supply["variation_count"],
                "selecting_supply_ids": supply["selecting_supply_ids"],
                "bank3_signature": bank3["survivor_signature"],
                "bank3_ties": bank3["tie_epochs"],
                "bank3_empty": bank3["empty_epochs"],
                "admission_primary_matches":
                    admission["primary_global_smallest_claim_matches"],
                "smallest_positive_unheld_admitted":
                    admission["smallest_positive_unheld_admitted"],
                "bank1_new_selector_events":
                    admission["bank1_new_selector_events"],
                "bank2_identity_exact": bank2["identity_exact"],
                "deterministic": deterministic,
                "pass_count": PASS,
                "fail_count": FAIL,
                "report_sha256": report_sha,
                "runtime_seconds": round(elapsed, 6),
                "stdout_bytes_final_upper_bound": STDOUT_BYTES + 2048,
            }
        ),
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
