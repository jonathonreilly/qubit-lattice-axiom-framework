#!/usr/bin/env python3
"""Independent bounded checker for Cycle 735 separated-pair control.

Cycle 735 is parsed as inert AST data.  Cycle 719 is the only project
primary imported, and is used directly to reproduce the controller orbits.
"""
from __future__ import annotations

import ast
import json
import sys
from time import perf_counter
from typing import Any

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STDOUT_LIMIT_BYTES = 150 * 1024

FROZEN_CENSUS = {
    "separated_pairs": 44,
    "translation_identities": 484,
    "orbits": 44,
    "steps": 484,
    "station_checks": 5324,
    "occupied_checks": 968,
    "invariant_violations": 0,
    "adjacency_step0_violations": 22,
}
FROZEN_BOUNDARY = {
    "separated_pair_lawful_control": True,
    "lawful_distance_domain": [2, 3, 4, 5],
    "two_source_composition_ring11": True,
    "scope_language": {
        "renewal": "W4 renewal untouched",
        "sources": "two sources only",
        "geometry": "ring-11 only",
    },
}
FROZEN_CYCLE735_PRIMARY_INPUTS = (
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
FROZEN_CONVENTION = (
    "positive-shortest representative d=2..5; d and 11-d "
    "are the same unordered separation after endpoint exchange"
)
FROZEN_W4_STATEMENT = (
    "bounded separated multi-source composition on the held fixture: "
    "two sources move at ring-11 scope with supplies declared; "
    "W4's renewal component is untouched"
)
FROZEN_CYCLE734_WALL = "ownership_uniqueness_at_adjacent_Q_sites"
BLOCKLISTED_PRIMARY_CYCLES = (735, 734, 732, 731, 730, 724)

TEMPLATE_LAYOUT = {
    "stations": 11,
    "a_base": 0,
    "ref_base": 11,
    "full_width": 22,
}


def k_surface_signature() -> tuple[tuple[str, int], ...]:
    """Detect rebinding, insertion, or deletion of attributes on K."""

    return tuple(sorted((name, id(value)) for name, value in K.__dict__.items()))


K_SURFACE_BEFORE = k_surface_signature()


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise ValueError(f"expected one function {name!r}, found {len(matches)}")
    return matches[0]


def assigned_expression(
    statements: list[ast.stmt], name: str
) -> ast.expr:
    for statement in statements:
        if (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
            and statement.targets[0].id == name
        ):
            return statement.value
        if (
            isinstance(statement, ast.AnnAssign)
            and isinstance(statement.target, ast.Name)
            and statement.target.id == name
            and statement.value is not None
        ):
            return statement.value
    raise ValueError(f"assignment {name!r} not found")


def module_literal(tree: ast.Module, name: str) -> Any:
    return ast.literal_eval(assigned_expression(tree.body, name))


def returned_dict(function: ast.FunctionDef) -> ast.Dict:
    rows = [
        statement.value
        for statement in function.body
        if isinstance(statement, ast.Return)
        and isinstance(statement.value, ast.Dict)
    ]
    if len(rows) != 1:
        raise ValueError(
            f"expected one direct returned dict in {function.name!r}"
        )
    return rows[0]


def dict_expressions(node: ast.Dict) -> dict[str, ast.expr]:
    output: dict[str, ast.expr] = {}
    for key, value in zip(node.keys, node.values):
        if key is None:
            raise ValueError("dict unpacking is outside the extraction domain")
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str):
            raise ValueError("non-string report key")
        output[literal_key] = value
    return output


def safe_math(node: ast.AST, environment: dict[str, Any]) -> Any:
    """Evaluate only the tiny literal/arithmetic census language."""

    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        if node.id not in environment:
            raise ValueError(f"unknown census name {node.id!r}")
        return environment[node.id]
    if isinstance(node, ast.Tuple):
        return tuple(safe_math(item, environment) for item in node.elts)
    if isinstance(node, ast.List):
        return [safe_math(item, environment) for item in node.elts]
    if isinstance(node, ast.UnaryOp):
        value = safe_math(node.operand, environment)
        if isinstance(node.op, ast.USub):
            return -value
        if isinstance(node.op, ast.UAdd):
            return +value
        raise ValueError("unsupported unary census operator")
    if isinstance(node, ast.BinOp):
        left = safe_math(node.left, environment)
        right = safe_math(node.right, environment)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Pow):
            return left**right
        if isinstance(node.op, ast.Mod):
            return left % right
        if isinstance(node.op, ast.FloorDiv):
            return left // right
        raise ValueError("unsupported binary census operator")
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "len"
        and len(node.args) == 1
        and not node.keywords
    ):
        return len(safe_math(node.args[0], environment))
    raise ValueError(f"unsafe census expression {type(node).__name__}")


def direct_numeric_environment(
    function: ast.FunctionDef, initial: dict[str, Any]
) -> dict[str, Any]:
    environment = dict(initial)
    for statement in function.body:
        if (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
        ):
            try:
                value = safe_math(statement.value, environment)
            except (TypeError, ValueError, ZeroDivisionError):
                continue
            environment[statement.targets[0].id] = value
    return environment


def has_zero_comparison(function: ast.FunctionDef, name: str) -> bool:
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Name)
            and node.left.id == name
            and len(node.ops) == len(node.comparators) == 1
            and isinstance(node.ops[0], ast.Eq)
            and isinstance(node.comparators[0], ast.Constant)
            and node.comparators[0].value == 0
        ):
            return True
    return False


def template_shape_exact(function: ast.FunctionDef) -> bool:
    expected = ast.parse(
        '''
def separated_pair_creation_word(layout, position, d):
    stations = layout["stations"]
    return (
        K.A.x(layout["a_base"] + position % stations),
        K.A.x(layout["a_base"] + (position + d) % stations),
    ) + tuple(
        K.A.x(layout["ref_base"] + (position + edge) % stations)
        for edge in range(1, d + 1)
    )
'''
    ).body[0]
    if not isinstance(expected, ast.FunctionDef):
        return False
    actual_arguments = tuple(argument.arg for argument in function.args.args)
    argument_discipline = (
        actual_arguments == ("layout", "position", "d")
        and not function.args.posonlyargs
        and not function.args.kwonlyargs
        and function.args.vararg is None
        and function.args.kwarg is None
        and not function.args.defaults
        and not function.decorator_list
    )
    actual_body = list(function.body)
    if (
        actual_body
        and isinstance(actual_body[0], ast.Expr)
        and isinstance(actual_body[0].value, ast.Constant)
        and isinstance(actual_body[0].value.value, str)
    ):
        actual_body = actual_body[1:]
    actual_dump = ast.dump(
        ast.Module(body=actual_body, type_ignores=[]),
        include_attributes=False,
    )
    expected_dump = ast.dump(
        ast.Module(body=expected.body, type_ignores=[]),
        include_attributes=False,
    )
    return argument_discipline and actual_dump == expected_dump


def dotted_name(node: ast.AST) -> str:
    parts: list[str] = []
    current = node
    while isinstance(current, ast.Attribute):
        parts.append(current.attr)
        current = current.value
    if isinstance(current, ast.Name):
        parts.append(current.id)
    else:
        raise ValueError("unsupported dotted call target")
    return ".".join(reversed(parts))


def eval_template_integer(
    node: ast.AST, environment: dict[str, Any]
) -> int:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.Name):
        value = environment[node.id]
        if not isinstance(value, int):
            raise ValueError("template integer name did not contain an integer")
        return value
    if (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "layout"
    ):
        key = ast.literal_eval(node.slice)
        value = environment["layout"][key]
        if not isinstance(value, int):
            raise ValueError("layout entry was not an integer")
        return value
    if isinstance(node, ast.BinOp):
        left = eval_template_integer(node.left, environment)
        right = eval_template_integer(node.right, environment)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Mod):
            return left % right
    raise ValueError(f"unsupported template integer AST {ast.dump(node)}")


def extracted_x_gate(
    node: ast.AST, environment: dict[str, Any]
) -> tuple[str, int]:
    if (
        not isinstance(node, ast.Call)
        or dotted_name(node.func) != "K.A.x"
        or len(node.args) != 1
        or node.keywords
    ):
        raise ValueError("template gate is not a unary K.A.x call")
    return ("X", eval_template_integer(node.args[0], environment))


def extracted_template_specs(
    function: ast.FunctionDef,
    layout: dict[str, int],
    position: int,
    distance: int,
) -> tuple[tuple[str, int], ...]:
    """Interpret only the AST grammar admitted by template_shape_exact."""

    if not template_shape_exact(function):
        raise ValueError("Cycle 735 template AST shape drifted")
    environment: dict[str, Any] = {
        "layout": layout,
        "position": position,
        "d": distance,
        "stations": layout["stations"],
    }
    return_node = next(
        statement
        for statement in function.body
        if isinstance(statement, ast.Return)
    )
    if not isinstance(return_node.value, ast.BinOp):
        raise ValueError("template return is not a concatenation")
    left = return_node.value.left
    right = return_node.value.right
    if not isinstance(left, ast.Tuple):
        raise ValueError("template head is not a tuple")
    output = [extracted_x_gate(gate, environment) for gate in left.elts]
    if (
        not isinstance(right, ast.Call)
        or not isinstance(right.func, ast.Name)
        or right.func.id != "tuple"
        or len(right.args) != 1
        or not isinstance(right.args[0], ast.GeneratorExp)
    ):
        raise ValueError("template tail is not tuple(generator)")
    generator = right.args[0]
    if len(generator.generators) != 1:
        raise ValueError("template has more than one generator")
    comprehension = generator.generators[0]
    if (
        not isinstance(comprehension.target, ast.Name)
        or comprehension.target.id != "edge"
        or comprehension.ifs
        or comprehension.is_async
        or not isinstance(comprehension.iter, ast.Call)
        or not isinstance(comprehension.iter.func, ast.Name)
        or comprehension.iter.func.id != "range"
    ):
        raise ValueError("template generator shape drifted")
    bounds = [
        eval_template_integer(argument, environment)
        for argument in comprehension.iter.args
    ]
    for edge in range(*bounds):
        environment["edge"] = edge
        output.append(extracted_x_gate(generator.elt, environment))
    return tuple(output)


def own_template_specs(
    layout: dict[str, int], position: int, distance: int
) -> tuple[tuple[str, int], ...]:
    stations = layout["stations"]
    head = (
        ("X", layout["a_base"] + position % stations),
        ("X", layout["a_base"] + (position + distance) % stations),
    )
    reference = tuple(
        ("X", layout["ref_base"] + (position + edge) % stations)
        for edge in range(1, distance + 1)
    )
    return head + reference


def simulate_x_specs(
    initial: int, specs: tuple[tuple[str, int], ...]
) -> int:
    state = initial
    for kind, wire in specs:
        if kind != "X" or wire < 0:
            raise ValueError(("outside own X simulator domain", kind, wire))
        state ^= 1 << wire
    return state


def expected_template_mask(
    layout: dict[str, int], position: int, distance: int
) -> int:
    stations = layout["stations"]
    value = 1 << (layout["a_base"] + position % stations)
    value |= 1 << (
        layout["a_base"] + (position + distance) % stations
    )
    for edge in range(1, distance + 1):
        value |= 1 << (
            layout["ref_base"] + (position + edge) % stations
        )
    return value


def translate_specs(
    specs: tuple[tuple[str, int], ...],
    layout: dict[str, int],
    shift: int,
) -> tuple[tuple[str, int], ...]:
    stations = layout["stations"]
    translated = []
    for kind, wire in specs:
        if layout["a_base"] <= wire < layout["a_base"] + stations:
            wire = layout["a_base"] + (
                wire - layout["a_base"] + shift
            ) % stations
        elif layout["ref_base"] <= wire < layout["ref_base"] + stations:
            wire = layout["ref_base"] + (
                wire - layout["ref_base"] + shift
            ) % stations
        else:
            raise ValueError(("template wire outside translated banks", wire))
        translated.append((kind, wire))
    return tuple(translated)


def extraction(tree: ast.Module) -> dict[str, Any]:
    ring = module_literal(tree, "RING_STATIONS")
    expected_count = module_literal(tree, "EXPECTED_COUNT")
    distances = module_literal(tree, "LAWFUL_DISTANCES")
    adjacent = module_literal(tree, "ADJACENT_CONTROL_DISTANCE")
    source_audit = module_literal(tree, "AUDIT_INPUT_PATHS")
    template = function_node(tree, "separated_pair_creation_word")
    exactness_fn = function_node(tree, "separated_template_exactness")
    translation_fn = function_node(tree, "translation_covariance_all_d")
    orbit_fn = function_node(tree, "invariant_full_orbit")
    adjacency_fn = function_node(tree, "adjacency_control")
    main_fn = function_node(tree, "main")

    module_environment = {
        "RING_STATIONS": ring,
        "EXPECTED_COUNT": expected_count,
        "LAWFUL_DISTANCES": distances,
        "ADJACENT_CONTROL_DISTANCE": adjacent,
    }
    exactness_fields = dict_expressions(returned_dict(exactness_fn))
    translation_fields = dict_expressions(returned_dict(translation_fn))
    convention = ast.literal_eval(exactness_fields["convention"])
    exact_pairs = safe_math(
        exactness_fields["expected_cases"], module_environment
    )
    identities = safe_math(
        translation_fields["expected_identities"], module_environment
    )
    orbit_environment = direct_numeric_environment(
        orbit_fn, module_environment
    )
    adjacency_fields = dict_expressions(returned_dict(adjacency_fn))
    adjacent_violations = safe_math(
        adjacency_fields["expected_violations"], module_environment
    )
    extracted_census = {
        "separated_pairs": exact_pairs,
        "translation_identities": identities,
        "orbits": orbit_environment["expected_cases"],
        "steps": orbit_environment["expected_boundary_steps"],
        "station_checks": orbit_environment["expected_station_checks"],
        "occupied_checks": orbit_environment["expected_occupied_checks"],
        "invariant_violations": 0,
        "adjacency_step0_violations": adjacent_violations,
    }

    boundary_node = assigned_expression(main_fn.body, "boundary")
    if not isinstance(boundary_node, ast.Dict):
        raise ValueError("Cycle 735 boundary is not a literal-key dict")
    boundary_expressions = dict_expressions(boundary_node)
    required_boundary_expressions = {
        "separated_pair_lawful_control": "separated_lawful",
        "lawful_distance_domain": "lawful_domain",
        "two_source_composition_ring11": "composition_lawful",
    }
    boundary_bindings_exact = all(
        key in boundary_expressions
        and isinstance(boundary_expressions[key], ast.Name)
        and boundary_expressions[key].id == value
        for key, value in required_boundary_expressions.items()
    )
    w4_statement = ast.literal_eval(
        assigned_expression(main_fn.body, "w4_statement")
    )
    w4_untouched = ast.literal_eval(
        boundary_expressions["W4_renewal_component_untouched"]
    )
    source_constants = tuple(
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    boundary = {
        "separated_pair_lawful_control": True,
        "lawful_distance_domain": list(distances),
        "two_source_composition_ring11": True,
    }
    passed = all(
        (
            ring == 11,
            expected_count == 2,
            distances == (2, 3, 4, 5),
            adjacent == 1,
            source_audit == FROZEN_CYCLE735_PRIMARY_INPUTS,
            template_shape_exact(template),
            convention == FROZEN_CONVENTION,
            "d and 11-d" in convention,
            extracted_census == FROZEN_CENSUS,
            has_zero_comparison(orbit_fn, "invariant_violations"),
            boundary_bindings_exact,
            boundary
            == {
                key: FROZEN_BOUNDARY[key]
                for key in (
                    "separated_pair_lawful_control",
                    "lawful_distance_domain",
                    "two_source_composition_ring11",
                )
            },
            w4_statement == FROZEN_W4_STATEMENT,
            w4_untouched is True,
            FROZEN_CYCLE734_WALL in source_constants,
        )
    )
    return {
        "pass": passed,
        "ring_stations": ring,
        "expected_count": expected_count,
        "distances": distances,
        "adjacent_control_distance": adjacent,
        "convention": convention,
        "census": extracted_census,
        "boundary": boundary,
        "source_AUDIT_INPUT_PATHS": source_audit,
        "AUDIT_literal_eval": True,
        "template_AST_exact": template_shape_exact(template),
        "boundary_bindings_exact": boundary_bindings_exact,
        "W4_statement": w4_statement,
    }


def template_recount(
    tree: ast.Module, extracted: dict[str, Any]
) -> dict[str, Any]:
    template = function_node(tree, "separated_pair_creation_word")
    distances = tuple(extracted["distances"])
    stations = int(extracted["ring_stations"])
    failures: list[tuple[Any, ...]] = []
    cases = 0
    identities = 0
    for distance in distances:
        for position in range(stations):
            source_specs = extracted_template_specs(
                template, TEMPLATE_LAYOUT, position, distance
            )
            own_specs = own_template_specs(
                TEMPLATE_LAYOUT, position, distance
            )
            observed = simulate_x_specs(0, source_specs)
            expected = expected_template_mask(
                TEMPLATE_LAYOUT, position, distance
            )
            cases += 1
            if (
                source_specs != own_specs
                or observed != expected
                or len(source_specs) != distance + 2
                or any(kind != "X" for kind, _wire in source_specs)
            ):
                failures.append(("bit_exact", position, distance))
            for shift in range(stations):
                identities += 1
                translated = translate_specs(
                    source_specs, TEMPLATE_LAYOUT, shift
                )
                target = extracted_template_specs(
                    template,
                    TEMPLATE_LAYOUT,
                    (position + shift) % stations,
                    distance,
                )
                if translated != target:
                    failures.append(
                        ("translation", position, distance, shift)
                    )
    return {
        "pass": (
            cases == FROZEN_CENSUS["separated_pairs"]
            and identities == FROZEN_CENSUS["translation_identities"]
            and not failures
        ),
        "bit_exact_cases": cases,
        "translation_identities": identities,
        "failures": failures[:12],
        "own_simulator": "integer XOR bitmask",
    }


def occupied(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, bit in enumerate(bits) if bit)


def own_ownership_violations(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
) -> tuple[dict[str, Any], ...]:
    """Cycle-734 invariant, independently evaluated at every occupied A site."""

    stations = len(a)
    if len(b) != stations or len(work) != stations:
        raise ValueError("rail widths disagree")
    rows = []
    for station in range(stations):
        if not a[station]:
            continue
        left = (station - 1) % stations
        right = (station + 1) % stations
        reasons = []
        if b[station]:
            reasons.append("own_B")
        if work[station]:
            reasons.append("own_work")
        if a[left]:
            reasons.append("left_A")
        if b[left]:
            reasons.append("left_B")
        if a[right]:
            reasons.append("right_A")
        if b[right]:
            reasons.append("right_B")
        if reasons:
            rows.append({"station": station, "reasons": tuple(reasons)})
    return tuple(rows)


def unordered_ring_distance(sites: tuple[int, ...], stations: int) -> int:
    if len(sites) != 2:
        return -1
    forward = (sites[1] - sites[0]) % stations
    return min(forward, stations - forward)


def invariant_orbit_recount(
    extracted: dict[str, Any]
) -> dict[str, Any]:
    stations = int(extracted["ring_stations"])
    distances = tuple(extracted["distances"])
    program = K.interleaved_program(2)
    banks, links = K.B.chain_genesis(2)
    data = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    allocator = K.M.global_allocator_word(2)
    twice_expected = K.A.apply_semantic(
        K.A.apply_semantic(data, allocator), allocator
    )
    blank = (0,) * stations
    failures: list[tuple[Any, ...]] = []
    pair_keys: set[tuple[int, int]] = set()
    orbits = steps = station_checks = occupied_checks = 0
    invariant_violations = distance_failures = closure_failures = 0
    trace_failures = composition_failures = direct_disagreements = 0

    if len(program) != stations:
        failures.append(("program_stations", len(program), stations))
    for distance in distances:
        for position in range(stations):
            token_positions = (
                position,
                (position + distance) % stations,
            )
            pair_keys.add(tuple(sorted(token_positions)))
            initial_a = tuple(
                int(site in token_positions) for site in range(stations)
            )
            current_data = data
            a = initial_a
            b = blank
            work = blank
            orbits += 1
            expected_trace = []
            for step in range(stations):
                steps += 1
                station_checks += stations
                sites = occupied(a)
                occupied_checks += len(sites)
                violations = own_ownership_violations(a, b, work)
                invariant_violations += len(violations)
                expected_sites = tuple(
                    sorted(
                        (
                            (position + step) % stations,
                            (position + distance + step) % stations,
                        )
                    )
                )
                if (
                    sites != expected_sites
                    or unordered_ring_distance(sites, stations) != distance
                ):
                    distance_failures += 1
                expected_trace.append(
                    (
                        expected_sites,
                        tuple(
                            sorted(
                                (
                                    (position + step + 1) % stations,
                                    (
                                        position
                                        + distance
                                        + step
                                        + 1
                                    )
                                    % stations,
                                )
                            )
                        ),
                        0,
                    )
                )
                current_data, a, b = K.apply_controller_step(
                    current_data, program, a, b
                )

            output, final_a, final_b, trace = K.run_orbit(
                data, program, token_positions=token_positions
            )
            if trace != tuple(expected_trace):
                trace_failures += 1
            if output != twice_expected:
                composition_failures += 1
            if final_a != initial_a or any(final_b):
                closure_failures += 1
            if (
                current_data != output
                or a != final_a
                or b != final_b
            ):
                direct_disagreements += 1

    observed = {
        "orbits": orbits,
        "steps": steps,
        "station_checks": station_checks,
        "occupied_checks": occupied_checks,
        "invariant_violations": invariant_violations,
    }
    expected = {
        key: FROZEN_CENSUS[key]
        for key in (
            "orbits",
            "steps",
            "station_checks",
            "occupied_checks",
            "invariant_violations",
        )
    }
    passed = (
        len(pair_keys) == FROZEN_CENSUS["separated_pairs"]
        and observed == expected
        and distance_failures == 0
        and closure_failures == 0
        and trace_failures == 0
        and composition_failures == 0
        and direct_disagreements == 0
        and not failures
    )
    return {
        "pass": passed,
        "census": observed,
        "unique_pairs": len(pair_keys),
        "distance_failures": distance_failures,
        "closure_failures": closure_failures,
        "trace_failures": trace_failures,
        "composition_failures": composition_failures,
        "direct_step_disagreements": direct_disagreements,
        "failures": failures[:12],
    }


def adjacency_boundary_recount(
    extracted: dict[str, Any]
) -> dict[str, Any]:
    stations = int(extracted["ring_stations"])
    distance = int(extracted["adjacent_control_distance"])
    blank = (0,) * stations
    violation_rows = 0
    reason_count = 0
    failures: list[tuple[Any, ...]] = []
    for position in range(stations):
        a = tuple(
            int(
                station
                in (position, (position + distance) % stations)
            )
            for station in range(stations)
        )
        rows = own_ownership_violations(a, blank, blank)
        reasons = tuple(
            reason for row in rows for reason in row["reasons"]
        )
        violation_rows += len(rows)
        reason_count += len(reasons)
        if (
            len(rows) != 2
            or len(reasons) != 2
            or any(
                reason not in ("left_A", "right_A")
                for reason in reasons
            )
        ):
            failures.append((position, rows))
    return {
        "pass": (
            distance == 1
            and violation_rows
            == FROZEN_CENSUS["adjacency_step0_violations"]
            and reason_count
            == FROZEN_CENSUS["adjacency_step0_violations"]
            and FROZEN_CYCLE734_WALL
            == "ownership_uniqueness_at_adjacent_Q_sites"
            and not failures
        ),
        "distance": distance,
        "positions": stations,
        "step": 0,
        "violations": violation_rows,
        "neighbor_A_reasons": reason_count,
        "frozen_Cycle734_wall": FROZEN_CYCLE734_WALL,
        "failures": failures[:12],
    }


def count_parity_verdict(
    a_mask: int, b_mask: int, h: int, expected_count: int
) -> dict[str, Any]:
    a_count = a_mask.bit_count()
    b_count = b_mask.bit_count()
    parity_ok = (a_count + b_count) % 2 == h
    count_ok = a_count == expected_count
    return {
        "A_count": a_count,
        "B_count": b_count,
        "h": h,
        "count_ok": count_ok,
        "parity_ok": parity_ok,
        "accepted": count_ok and parity_ok,
    }


def source_count_witness_domain(tree: ast.Module) -> tuple[int, ...]:
    function = function_node(tree, "count_witness_rows")
    matches = []
    for node in ast.walk(function):
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "count"
        ):
            try:
                value = ast.literal_eval(node.iter)
            except (ValueError, TypeError):
                continue
            if isinstance(value, tuple):
                matches.append(value)
    if len(matches) != 1:
        raise ValueError("frozen count-witness domain was not unique")
    return matches[0]


def count2_spotcheck(
    tree: ast.Module, extracted: dict[str, Any]
) -> dict[str, Any]:
    stations = int(extracted["ring_stations"])
    distances = tuple(extracted["distances"])
    expected_count = int(extracted["expected_count"])
    source_witnesses = source_count_witness_domain(tree)
    sample_positions = (0, 5, 10)
    sample_failures = []
    sample_cases = 0
    for distance in distances:
        for position in sample_positions:
            sites = (position, (position + distance) % stations)
            a_mask = sum(1 << site for site in sites)
            verdict = count_parity_verdict(
                a_mask, 0, 0, expected_count
            )
            sample_cases += 1
            if not verdict["accepted"]:
                sample_failures.append((position, distance, verdict))
    witnesses = {
        count: count_parity_verdict(
            (1 << count) - 1,
            0,
            count & 1,
            expected_count,
        )
        for count in (1, 3)
    }
    witnesses_refused = all(
        row["parity_ok"]
        and not row["count_ok"]
        and not row["accepted"]
        for row in witnesses.values()
    )
    source_strings = tuple(
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    return {
        "pass": (
            expected_count == 2
            and source_witnesses == (0, 1, 3, 4)
            and "all_0_1_3_4_count_witnesses_refused"
            in source_strings
            and sample_cases == 12
            and not sample_failures
            and witnesses_refused
        ),
        "expected_count": expected_count,
        "sample_family_cases": sample_cases,
        "sample_failures": sample_failures,
        "count_1_and_3_witnesses": witnesses,
        "source_frozen_witness_domain": source_witnesses,
    }


def discipline(
    extracted: dict[str, Any], started: float
) -> dict[str, Any]:
    blocked_loaded = []
    for name in sorted(sys.modules):
        leaf = name.rsplit(".", 1)[-1]
        if any(
            leaf.startswith(f"frontier_cycle{cycle}_")
            for cycle in BLOCKLISTED_PRIMARY_CYCLES
        ):
            blocked_loaded.append(name)
    scope = FROZEN_BOUNDARY["scope_language"]
    elapsed = perf_counter() - started
    k_unchanged = k_surface_signature() == K_SURFACE_BEFORE
    audit_tuple_exact = AUDIT_INPUT_PATHS == (
        "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    )
    frozen_tables_exact = (
        extracted["census"] == FROZEN_CENSUS
        and extracted["boundary"]
        == {
            key: FROZEN_BOUNDARY[key]
            for key in (
                "separated_pair_lawful_control",
                "lawful_distance_domain",
                "two_source_composition_ring11",
            )
        }
    )
    scope_exact = scope == {
        "renewal": "W4 renewal untouched",
        "sources": "two sources only",
        "geometry": "ring-11 only",
    }
    return {
        "pass": (
            k_unchanged
            and not blocked_loaded
            and audit_tuple_exact
            and frozen_tables_exact
            and scope_exact
            and elapsed < AUDIT_TIMEOUT_SEC
        ),
        "K_attribute_surface_unchanged": k_unchanged,
        "K_attribute_writes": 0 if k_unchanged else "detected",
        "blocklisted_primary_imports": blocked_loaded,
        "AUDIT_INPUT_PATHS_pure_literal_value": AUDIT_INPUT_PATHS,
        "frozen_tables_literal": frozen_tables_exact,
        "scope_language": scope,
        "runtime_below_timeout": elapsed < AUDIT_TIMEOUT_SEC,
    }


def honest_certificate(
    label: str, function: Any, *args: Any
) -> dict[str, Any]:
    try:
        result = function(*args)
        if not isinstance(result, dict) or "pass" not in result:
            raise TypeError("certificate did not return a pass-bearing dict")
        return result
    except Exception as error:
        return {
            "pass": False,
            "error": f"{type(error).__name__}: {error}",
            "certificate": label,
        }


def render_output(
    results: list[tuple[str, dict[str, Any]]],
    started: float,
) -> tuple[str, dict[str, Any]]:
    elapsed = perf_counter() - started
    checks = {label: bool(detail["pass"]) for label, detail in results}
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "pass": all(checks.values()),
        "runtime_seconds": round(elapsed, 6),
        "frozen_census": FROZEN_CENSUS,
        "boundary": FROZEN_BOUNDARY,
        "certificates": {
            label: detail for label, detail in results
        },
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_bytes": 0,
    }
    prefix = [
        f"{'PASS' if detail['pass'] else 'FAIL'} {label}"
        for label, detail in results
    ]
    prefix.append(
        f"{report['checks_passed']}/{report['checks_total']} certificates PASS"
    )
    terminal = (
        "CYCLE735_SEPARATED_PAIR_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE735_SEPARATED_PAIR_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    for _iteration in range(4):
        body = json.dumps(
            report, sort_keys=True, separators=(",", ":"), default=str
        )
        text = "\n".join(prefix + ["SUMMARY_JSON " + body, terminal]) + "\n"
        report["stdout_bytes"] = len(text.encode())
    body = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(prefix + ["SUMMARY_JSON " + body, terminal]) + "\n"
    return text, report


def main() -> int:
    started = perf_counter()
    try:
        with open(AUDIT_INPUT_PATHS[0], "r", encoding="utf-8") as handle:
            primary_source = handle.read()
        tree = ast.parse(primary_source, filename=AUDIT_INPUT_PATHS[0])
    except Exception as error:
        failure = {
            "pass": False,
            "error": f"{type(error).__name__}: {error}",
        }
        results = [
            (name, dict(failure))
            for name in (
                "extraction",
                "template_recount",
                "invariant_orbit_recount",
                "adjacency_boundary_recount",
                "count2_spotcheck",
                "discipline",
            )
        ]
        text, _report = render_output(results, started)
        sys.stdout.write(text)
        return 1

    extracted = honest_certificate("extraction", extraction, tree)
    template = honest_certificate(
        "template_recount", template_recount, tree, extracted
    )
    orbit = honest_certificate(
        "invariant_orbit_recount",
        invariant_orbit_recount,
        extracted,
    )
    adjacency = honest_certificate(
        "adjacency_boundary_recount",
        adjacency_boundary_recount,
        extracted,
    )
    count2 = honest_certificate(
        "count2_spotcheck", count2_spotcheck, tree, extracted
    )
    bounded_discipline = honest_certificate(
        "discipline", discipline, extracted, started
    )
    results = [
        ("extraction", extracted),
        ("template_recount", template),
        ("invariant_orbit_recount", orbit),
        ("adjacency_boundary_recount", adjacency),
        ("count2_spotcheck", count2),
        ("discipline", bounded_discipline),
    ]
    text, report = render_output(results, started)
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(
            "FAIL stdout_under_150KB\n"
            + json.dumps(
                {
                    "pass": False,
                    "stdout_bytes": len(text.encode()),
                    "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
                },
                sort_keys=True,
            )
            + "\n"
        )
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
