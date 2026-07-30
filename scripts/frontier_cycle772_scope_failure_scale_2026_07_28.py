#!/usr/bin/env python3
"""Cycle 772: scale the Cycle-766 E0/E1 scope failures without refitting.

The Cycle-766 assignment is a frozen comparator.  This runner reads that
runner only as text/AST, imports the unchanged Cycle-763 construction, and
continues its complete fixture epoch uniformly.  Every census is finite
trajectory DATA.  No branch makes a weight, convergence, or family-win claim.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle763_symmetry_broken_ensembles_2026_07_28 as C763
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


COMPARATOR_PATH = (
    "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py"
)
COMPARATOR_MODULE_BLOCKLIST = (
    "frontier_cycle766_family_winning_mapping_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "d2205d1ed26f3aa1ea531502470fb6fcc91bffec3b94fb6781e9154442eb5724",
    AUDIT_INPUT_PATHS[1]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[2]:
        "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
    COMPARATOR_PATH:
        "f315180920ad6321ee41a32763f4a2606267e2bf7220f6a52cd42ce5e5382d66",
}
STDOUT_LIMIT_BYTES = 150 * 1024
SCALE_LADDER = (1, 4, 16, 64, 256)
FROZEN_ASSIGNMENT = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
PERMUTED_ASSIGNMENT_CONTROL = (
    (1, 2, 0),
    (2, 0, 1),
    (0, 1, 2),
)
EXPECTED_1X_COUNTS = (
    (13, 128, 68),
    (232, 97, 1),
    (146, 5, 432),
    (391, 230, 501),
)
EXPECTED_1X_BORN_TV_HEX = (
    "0x1.9a1c50c983fb1p-2",
    "0x1.b3344dce20805p-2",
    "0x1.4078ace570601p-2",
    "0x1.2eeecb23145d0p-6",
)
EXPECTED_1X_UNIFORM_TV_HEX = (
    "0x1.1dce302dba971p-2",
    "0x1.7a91d7a91d7a8p-2",
    "0x1.a172058fe18e2p-2",
    "0x1.06d84ca9c106ep-3",
)
EXPECTED_1X_ALIGN_FLAGS = (False, False, True, True)
SCOPE_NAMES = ("E0", "E1", "E2", "pooled")
VERDICT_VOCABULARY = (
    "SAMPLE_CONSISTENT",
    "MECHANISM_CONSISTENT",
    "MIXED",
    "CONTENT_DEGENERATE",
)
SCALING_FUNCTION_NAMES = (
    "scale_fixture_epochs",
    "generate_scaled_events",
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(label: str, condition: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def top_level_imports(tree: ast.Module) -> tuple[str, ...]:
    imported = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    return tuple(imported)


def source_contains_ast(
    nodes: tuple[ast.AST, ...],
    expected: str,
) -> bool:
    return any(ast.unparse(node) == expected for node in nodes)


def extract_cycle766_comparator() -> dict[str, object]:
    """Extract only the frozen Cycle-766 comparator contract from source."""
    path = ROOT / COMPARATOR_PATH
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    functions = top_level_functions(tree)
    main_nodes = tuple(ast.walk(functions["main"]))
    distance_nodes = tuple(ast.walk(functions["distance_metrics"]))
    scope_nodes = tuple(ast.walk(functions["scope_metrics"]))
    rank_nodes = tuple(ast.walk(functions["rank_range"]))
    anchor_nodes = tuple(
        ast.walk(functions["anchors_and_baselines_certificate"])
    )

    frozen_binding = source_contains_ast(
        main_nodes,
        "frozen_mapping = maximal['per_stratum_mapping']",
    )
    held_binding = source_contains_ast(
        main_nodes,
        "held_candidate = C763.C757._trace_candidate(trine_effects)",
    )
    tv_binding = source_contains_ast(distance_nodes, "tv = l1 / 2.0")
    strict_alignment = any(
        isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Lt)
        and "distance_metrics(counts, held_candidate)['TV']"
        in ast.unparse(node)
        and "distance_metrics(counts, uniform)['TV']"
        in ast.unparse(node)
        for node in scope_nodes
    )
    uniform_binding = any(
        isinstance(node, (ast.Assign, ast.AnnAssign))
        and "Fraction(1, len(EFFECT_IDS))" in ast.unparse(node)
        for node in scope_nodes
    )
    tie_tolerance_binding = any(
        isinstance(node, ast.Attribute)
        and ast.unparse(node) == "B317.TOL"
        for node in rank_nodes
    )
    frozen_hex_binding = any(
        isinstance(node, ast.Attribute)
        and ast.unparse(node)
        == "C763.C757.C748.FROZEN_HELD_CANDIDATE_HEX"
        for node in anchor_nodes
    )
    imported_names = top_level_imports(tree)
    blocklisted_imports = tuple(
        name
        for name in imported_names
        if name in COMPARATOR_MODULE_BLOCKLIST
    )
    return {
        "assignment": FROZEN_ASSIGNMENT,
        "assignment_origin": (
            "Cycle-766 reported result supplied verbatim to Cycle 772; "
            "AST verifies the source freezes maximal.per_stratum_mapping"
        ),
        "blocklisted_imports": blocklisted_imports,
        "comparator_sha256": file_sha256(path),
        "frozen_assignment_binding": frozen_binding,
        "frozen_held_candidate_hex_binding": frozen_hex_binding,
        "held_candidate_binding": held_binding,
        "imported_names": imported_names,
        "rank_tie_tolerance_binding": tie_tolerance_binding,
        "scope_alignment_is_strict": strict_alignment,
        "tv_is_half_l1": tv_binding,
        "uniform_binding": uniform_binding,
    }


def scale_fixture_epochs(
    base_fixtures: tuple[dict[str, object], ...],
    scale: int,
) -> tuple[dict[str, object], ...]:
    """Continue complete landed fixture epochs; never select event rows."""
    epoch_span = sum(
        int(row["alternative_count"]) for row in base_fixtures
    )
    scaled = []
    for replica in range(scale):
        for original in base_fixtures:
            row = dict(original)
            row["fixture_index"] = (
                int(original["fixture_index"])
                + replica * len(base_fixtures)
            )
            row["full_family_offset"] = (
                int(original["full_family_offset"])
                + replica * epoch_span
            )
            scaled.append(row)
    return tuple(scaled)


def generate_scaled_events(
    base_fixtures: tuple[dict[str, object], ...],
    primitive_multiplicities: tuple[int, ...],
    scale: int,
) -> tuple[
    tuple[dict[str, object], ...],
    tuple[dict[str, object], ...],
    dict[str, object],
]:
    fixtures = scale_fixture_epochs(base_fixtures, scale)
    identity_seed_permutation = tuple(
        range(len(C763.EFFECT_IDS))
    )
    events, stats = C763.build_seeded_family(
        fixtures,
        primitive_multiplicities,
        identity_seed_permutation,
        family_mode="cycle772-generator-uniform-scale",
    )
    return fixtures, events, stats


def count_assignment(
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    effect_domain = tuple(range(len(mapping)))
    rows = [
        [int() for _effect_index in effect_domain]
        for _stratum_index in effect_domain
    ]
    for event in events:
        stratum_index = int(event["associated_effect_index"])
        feature_index = (
            int(event["global_epoch_ordinal"])
            + int(event["actual_selected_alternative"])
        ) % len(effect_domain)
        mapped_index = mapping[stratum_index][feature_index]
        rows[stratum_index][mapped_index] += True
    per_scope = tuple(tuple(row) for row in rows)
    pooled = tuple(
        sum(row[effect_index] for row in per_scope)
        for effect_index in effect_domain
    )
    return per_scope + (pooled,)


def distance_metrics(
    counts: tuple[int, ...],
    target: tuple[float, ...],
) -> dict[str, object]:
    size = sum(counts)
    simplex = tuple(Fraction(count, size) for count in counts)
    residuals = tuple(
        float(observed) - expected
        for observed, expected in zip(
            simplex,
            target,
            strict=True,
        )
    )
    tv = sum(abs(value) for value in residuals) / 2.0
    return {
        "residual_hex": tuple(value.hex() for value in residuals),
        "simplex": tuple(str(value) for value in simplex),
        "TV": tv,
        "TV_hex": tv.hex(),
    }


def scope_rows(
    scale: int,
    counts: tuple[tuple[int, ...], ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    uniform = tuple(
        float(Fraction(1, len(C763.EFFECT_IDS)))
        for _effect_id in C763.EFFECT_IDS
    )
    rows = []
    for scope, scope_counts in zip(
        SCOPE_NAMES,
        counts,
        strict=True,
    ):
        born = distance_metrics(scope_counts, held_candidate)
        uniform_metrics = distance_metrics(scope_counts, uniform)
        sample_size = sum(scope_counts)
        rows.append(
            {
                "align": born["TV"] < uniform_metrics["TV"],
                "Born_TV": born["TV"],
                "Born_TV_hex": born["TV_hex"],
                "counts": scope_counts,
                "sample_size": sample_size,
                "scale": scale,
                "scope": scope,
                "simplex": born["simplex"],
                "TV_resolution_band": float(
                    Fraction(1, sample_size)
                ),
                "uniform_TV": uniform_metrics["TV"],
                "uniform_TV_hex": uniform_metrics["TV_hex"],
            }
        )
    return tuple(rows)


def evaluate_scale(
    scale: int,
    base_fixtures: tuple[dict[str, object], ...],
    primitive_multiplicities: tuple[int, ...],
    held_candidate: tuple[float, ...],
    mapping: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    fixtures, events, generator_stats = generate_scaled_events(
        base_fixtures,
        primitive_multiplicities,
        scale,
    )
    counts = count_assignment(events, mapping)
    rows = scope_rows(scale, counts, held_candidate)
    epoch_span = sum(
        int(row["alternative_count"]) for row in base_fixtures
    )
    relabel_fields = ("fixture_index", "full_family_offset")
    content_novelty = {
        "distinct_event_content": len({
            digest({
                **{
                    key: value
                    for key, value in event.items()
                    if key not in relabel_fields
                    and key != "global_epoch_ordinal"
                },
                "mapping_residue": (
                    int(event["global_epoch_ordinal"])
                    + int(event["actual_selected_alternative"])
                ) % len(C763.EFFECT_IDS),
            })
            for event in events
        }),
        "distinct_selector_inputs": len({
            digest({
                key: value
                for key, value in fixture.items()
                if key not in relabel_fields
            })
            for fixture in fixtures
        }),
        "raw_event_count": len(events),
    }
    return {
        "content_novelty": content_novelty,
        "counts": counts,
        "epoch_span": epoch_span,
        "fixture_count": len(fixtures),
        "generated_event_count": len(events),
        "generation_digest": generator_stats["row_digest"],
        "mapping": mapping,
        "scale": scale,
        "scope_rows": rows,
        "scope_sample_sizes": tuple(sum(row) for row in counts),
        "summary_digest": digest(
            {
                "counts": counts,
                "fixture_count": len(fixtures),
                "generated_event_count": len(events),
                "generation_digest": generator_stats["row_digest"],
                "mapping": mapping,
                "rows": rows,
                "scale": scale,
            }
        ),
    }


def scaling_ast_firewall() -> dict[str, object]:
    path = Path(__file__).resolve()
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    functions = top_level_functions(tree)
    scaling_nodes = tuple(
        child
        for name in SCALING_FUNCTION_NAMES
        for child in ast.walk(functions[name])
    )
    numeric_constants = tuple(
        ast.unparse(node)
        for node in scaling_nodes
        if isinstance(node, ast.Constant)
        and type(node.value) in {int, float, complex}
    )
    conditional_nodes = tuple(
        type(node).__name__
        for node in scaling_nodes
        if isinstance(
            node,
            (
                ast.If,
                ast.IfExp,
                ast.Match,
                ast.While,
            ),
        )
    )
    filtered_comprehensions = tuple(
        ast.unparse(node)
        for node in scaling_nodes
        if isinstance(
            node,
            (
                ast.ListComp,
                ast.SetComp,
                ast.DictComp,
                ast.GeneratorExp,
            ),
        )
        and any(generator.ifs for generator in node.generators)
    )
    forbidden_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in scaling_nodes
                if isinstance(node, ast.Call)
                and ast.unparse(node.func)
                in {
                    "filter",
                    "random.choice",
                    "random.sample",
                    "np.random.choice",
                }
            }
        )
    )
    imported_names = top_level_imports(tree)
    direct_landed_imports = tuple(
        name
        for name in imported_names
        if name.startswith("frontier_cycle")
        or name.startswith("physical_contact")
    )
    assignments = {
        target.id: node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets
            if isinstance(node, ast.Assign)
            else (node.target,)
        )
        if isinstance(target, ast.Name)
    }
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    ladder_node = assignments["SCALE_LADDER"]
    literal_inputs = (
        isinstance(audit_node, ast.Tuple)
        and bool(audit_node.elts)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
    )
    literal_ladder = (
        isinstance(ladder_node, ast.Tuple)
        and tuple(ast.literal_eval(ladder_node)) == SCALE_LADDER
    )
    required_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in scaling_nodes
                if isinstance(node, ast.Call)
            }
        )
    )
    return {
        "blocklisted_module_in_sys_modules": tuple(
            name
            for name in COMPARATOR_MODULE_BLOCKLIST
            if name in sys.modules
        ),
        "conditional_nodes": conditional_nodes,
        "direct_landed_imports": direct_landed_imports,
        "filtered_comprehensions": filtered_comprehensions,
        "forbidden_calls": forbidden_calls,
        "literal_audit_inputs": literal_inputs,
        "literal_scale_ladder": literal_ladder,
        "numeric_constants_outside_declared_ladder":
            numeric_constants,
        "required_calls": required_calls,
    }


def trajectory_verdict(
    trajectory: tuple[dict[str, object], ...],
) -> tuple[str, dict[str, object]]:
    evidence = {}
    sample_flags = []
    mechanism_flags = []
    for scope in SCOPE_NAMES[:2]:
        rows = tuple(
            result["scope_rows"][SCOPE_NAMES.index(scope)]
            for result in trajectory
        )
        consecutive = tuple(
            {
                "current_scale": current["scale"],
                "delta_Born_TV":
                    current["Born_TV"] - previous["Born_TV"],
                "material_decrease": (
                    current["Born_TV"]
                    < previous["Born_TV"]
                    - previous["TV_resolution_band"]
                    - current["TV_resolution_band"]
                ),
                "material_worsening": (
                    current["Born_TV"]
                    > previous["Born_TV"]
                    + previous["TV_resolution_band"]
                    + current["TV_resolution_band"]
                ),
                "previous_scale": previous["scale"],
                "resolution_sum": (
                    previous["TV_resolution_band"]
                    + current["TV_resolution_band"]
                ),
            }
            for previous, current in zip(
                rows,
                rows[1:],
            )
        )
        endpoint_material_decrease = (
            rows[-1]["Born_TV"]
            < rows[0]["Born_TV"]
            - rows[0]["TV_resolution_band"]
            - rows[-1]["TV_resolution_band"]
        )
        no_material_worsening = not any(
            row["material_worsening"] for row in consecutive
        )
        no_material_decrease = not any(
            row["material_decrease"] for row in consecutive
        )
        fails_at_every_scale = all(not row["align"] for row in rows)
        sample_scope = (
            endpoint_material_decrease
            and no_material_worsening
        )
        mechanism_scope = (
            fails_at_every_scale
            and no_material_decrease
        )
        sample_flags.append(sample_scope)
        mechanism_flags.append(mechanism_scope)
        evidence[scope] = {
            "consecutive_steps": consecutive,
            "endpoint_Born_TV": (
                rows[0]["Born_TV"],
                rows[-1]["Born_TV"],
            ),
            "endpoint_material_decrease":
                endpoint_material_decrease,
            "fails_at_every_scale": fails_at_every_scale,
            "mechanism_scope": mechanism_scope,
            "no_material_decrease": no_material_decrease,
            "no_material_worsening": no_material_worsening,
            "sample_scope": sample_scope,
        }
    if all(sample_flags):
        verdict = "SAMPLE_CONSISTENT"
    elif all(mechanism_flags):
        verdict = "MECHANISM_CONSISTENT"
    else:
        verdict = "MIXED"
    novelty_rows = tuple(
        {
            "scale": result["scale"],
            **result["content_novelty"],
        }
        for result in trajectory
        if "content_novelty" in result
    )
    selector_inputs = tuple(
        row["distinct_selector_inputs"] for row in novelty_rows
    )
    raw_counts = tuple(
        row["raw_event_count"] for row in novelty_rows
    )
    content_degenerate = bool(
        novelty_rows
        and len(set(selector_inputs)) == 1
        and raw_counts[-1] > raw_counts[0]
    )
    evidence["content_novelty"] = {
        "content_degenerate": content_degenerate,
        "rows": novelty_rows,
    }
    if content_degenerate:
        evidence["verdict_if_novelty_ignored"] = verdict
        verdict = "CONTENT_DEGENERATE"
    evidence["resolution_band_interpretation"] = (
        "1/N is a deterministic one-event TV resolution, not a "
        "probability, sampling model, confidence interval, or weight"
    )
    evidence["rule"] = {
        "CONTENT_DEGENERATE": (
            "distinct selector inputs are constant across the ladder "
            "while raw events multiply; the trajectory carries no "
            "scaled novelty and neither the SAMPLE nor the MECHANISM "
            "inference is licensed on this generator at this fixture "
            "scope"
        ),
        "MECHANISM_CONSISTENT": (
            "E0 and E1 fail alignment at every scale and neither has a "
            "consecutive Born-TV decrease larger than adjacent 1/N "
            "resolution bands"
        ),
        "MIXED": "anything else",
        "SAMPLE_CONSISTENT": (
            "E0 and E1 have a materially lower endpoint and no "
            "consecutive worsening larger than adjacent 1/N bands"
        ),
    }
    return verdict, evidence


def module_paths() -> tuple[str, ...]:
    return tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (C763, F750, B317)
    )


def main() -> int:
    started = perf_counter()
    audited_paths = AUDIT_INPUT_PATHS + (COMPARATOR_PATH,)
    input_sha_before = {
        relative: file_sha256(ROOT / relative)
        for relative in audited_paths
    }
    comparator = extract_cycle766_comparator()
    firewall = scaling_ast_firewall()

    trine_effects, forcing_data, captured_b317 = (
        C763.load_landed_apparatus()
    )
    seed_surface = C763.extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    held_candidate = C763.C757._trace_candidate(trine_effects)
    base_fixtures = C763.fixture_epochs()
    primitive_multiplicities = tuple(
        seed_surface["primitive_multiplicities"]
    )

    trajectory = tuple(
        evaluate_scale(
            scale,
            base_fixtures,
            primitive_multiplicities,
            held_candidate,
            FROZEN_ASSIGNMENT,
        )
        for scale in SCALE_LADDER
    )
    verdict, verdict_evidence = trajectory_verdict(trajectory)

    largest_control = evaluate_scale(
        SCALE_LADDER[-1],
        base_fixtures,
        primitive_multiplicities,
        held_candidate,
        PERMUTED_ASSIGNMENT_CONTROL,
    )
    determinism_repeat = {
        scale: evaluate_scale(
            scale,
            base_fixtures,
            primitive_multiplicities,
            held_candidate,
            FROZEN_ASSIGNMENT,
        )
        for scale in (SCALE_LADDER[0], SCALE_LADDER[-1])
    }

    input_sha_after = {
        relative: file_sha256(ROOT / relative)
        for relative in audited_paths
    }
    comparator_bindings = (
        comparator["frozen_assignment_binding"]
        and comparator["frozen_held_candidate_hex_binding"]
        and comparator["held_candidate_binding"]
        and comparator["rank_tie_tolerance_binding"]
        and comparator["scope_alignment_is_strict"]
        and comparator["tv_is_half_l1"]
        and comparator["uniform_binding"]
    )
    anchor_detail = {
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "Born_candidate": held_candidate,
        "Born_candidate_hex": tuple(
            value.hex() for value in held_candidate
        ),
        "comparator": comparator,
        "frozen_assignment": FROZEN_ASSIGNMENT,
        "input_sha256": input_sha_after,
        "module_identity": {
            "B317_is_C763_B317": B317 is C763.B317,
            "F750_is_C763_F750": F750 is C763.F750,
        },
        "module_paths": module_paths(),
        "rank_tie_tolerance_from_766": B317.TOL,
    }
    check(
        "CERTIFICATE A landed anchors and blocklisted 766 AST comparator",
        input_sha_before == input_sha_after == EXPECTED_SHA256
        and module_paths() == AUDIT_INPUT_PATHS
        and B317 is C763.B317
        and F750 is C763.F750
        and captured_b317.count("PASS ") == 7
        and "FAIL " not in captured_b317
        and comparator["assignment"] == FROZEN_ASSIGNMENT
        and comparator["comparator_sha256"]
        == EXPECTED_SHA256[COMPARATOR_PATH]
        and comparator_bindings
        and not comparator["blocklisted_imports"]
        and not firewall["blocklisted_module_in_sys_modules"]
        and tuple(value.hex() for value in held_candidate)
        == C763.C757.C748.FROZEN_HELD_CANDIDATE_HEX,
        anchor_detail,
    )

    actual_sizes = tuple(
        {
            "fixture_count": result["fixture_count"],
            "generated_event_count":
                result["generated_event_count"],
            "scale": result["scale"],
            "scope_sample_sizes":
                result["scope_sample_sizes"],
        }
        for result in trajectory
    )
    base_epoch_span = sum(
        int(row["alternative_count"]) for row in base_fixtures
    )
    generator_uniform = all(
        result["fixture_count"]
        == len(base_fixtures) * result["scale"]
        and result["epoch_span"] == base_epoch_span
        and result["generated_event_count"]
        == sum(result["counts"][0])
        + sum(result["counts"][1])
        + sum(result["counts"][2])
        and result["scope_sample_sizes"][-1]
        == result["generated_event_count"]
        for result in trajectory
    )
    firewall_ok = (
        firewall["literal_audit_inputs"]
        and firewall["literal_scale_ladder"]
        and not firewall["numeric_constants_outside_declared_ladder"]
        and not firewall["conditional_nodes"]
        and not firewall["filtered_comprehensions"]
        and not firewall["forbidden_calls"]
        and "C763.build_seeded_family" in firewall["required_calls"]
        and "scale_fixture_epochs" in firewall["required_calls"]
    )
    check(
        "CERTIFICATE B generator-uniform scaling AST firewall",
        firewall_ok
        and generator_uniform
        and tuple(result["scale"] for result in trajectory)
        == SCALE_LADDER
        and tuple(sorted(SCALE_LADDER)) == SCALE_LADDER
        and len(set(SCALE_LADDER)) == len(SCALE_LADDER),
        {
            "actual_sizes": actual_sizes,
            "base_fixture_count": len(base_fixtures),
            "complete_epoch_span": base_epoch_span,
            "firewall": firewall,
            "ladder_declared_up_front": SCALE_LADDER,
            "post_hoc_event_filtering": False,
            "scaling_rule": (
                "repeat every complete landed fixture epoch; advance "
                "fixture_index and full_family_offset by their complete "
                "landed spans; invoke unchanged C763.build_seeded_family"
            ),
        },
    )

    one_x_rows = trajectory[0]["scope_rows"]
    one_x_exact = (
        trajectory[0]["scale"] == SCALE_LADDER[0] == 1
        and trajectory[0]["counts"] == EXPECTED_1X_COUNTS
        and tuple(row["Born_TV_hex"] for row in one_x_rows)
        == EXPECTED_1X_BORN_TV_HEX
        and tuple(row["uniform_TV_hex"] for row in one_x_rows)
        == EXPECTED_1X_UNIFORM_TV_HEX
        and tuple(row["align"] for row in one_x_rows)
        == EXPECTED_1X_ALIGN_FLAGS
    )
    check(
        "CERTIFICATE C exact Cycle-766 1x per-scope table",
        one_x_exact,
        {
            "actual": one_x_rows,
            "expected_align_flags": EXPECTED_1X_ALIGN_FLAGS,
            "expected_Born_TV_hex": EXPECTED_1X_BORN_TV_HEX,
            "expected_counts": EXPECTED_1X_COUNTS,
            "expected_uniform_TV_hex":
                EXPECTED_1X_UNIFORM_TV_HEX,
        },
    )

    full_trajectory = tuple(
        row
        for result in trajectory
        for row in result["scope_rows"]
    )
    e2_and_pooled_all_scales = all(
        len(result["scope_rows"]) == len(SCOPE_NAMES)
        and result["scope_rows"][2]["scope"] == "E2"
        and result["scope_rows"][3]["scope"] == "pooled"
        for result in trajectory
    )
    boundary = {
        "family_win_bar_re_evaluated": False,
        "family_win_bar_status": "FROZEN_NOT_EVALUATED",
        "simplex_promoted_to_weight": False,
        "trajectory_role": "finite generator trajectory DATA",
        "weight_claim_made": False,
    }
    check(
        "CERTIFICATE D full trajectory and frozen three-way verdict",
        verdict in VERDICT_VOCABULARY
        and len(full_trajectory)
        == len(SCALE_LADDER) * len(SCOPE_NAMES)
        and e2_and_pooled_all_scales
        and one_x_rows[2]["align"]
        and one_x_rows[3]["align"]
        and boundary["family_win_bar_re_evaluated"] is False
        and boundary["weight_claim_made"] is False
        and boundary["simplex_promoted_to_weight"] is False,
        {
            "boundary": boundary,
            "trajectory": full_trajectory,
            "verdict": verdict,
            "verdict_evidence": verdict_evidence,
            "verdict_vocabulary": VERDICT_VOCABULARY,
        },
    )
    OUTPUT_LINES.append(
        "DATA FULL_TRAJECTORY :: " + compact(full_trajectory)
    )
    OUTPUT_LINES.append(
        "DATA THREE_WAY_VERDICT :: "
        + compact(
            {
                "evidence": verdict_evidence,
                "verdict": verdict,
            }
        )
    )

    candidate_largest = trajectory[-1]
    candidate_pooled = candidate_largest["scope_rows"][-1]
    control_pooled = largest_control["scope_rows"][-1]
    permutation_sensitive = (
        PERMUTED_ASSIGNMENT_CONTROL != FROZEN_ASSIGNMENT
        and largest_control["counts"][-1]
        != candidate_largest["counts"][-1]
        and control_pooled["Born_TV_hex"]
        != candidate_pooled["Born_TV_hex"]
        and abs(
            control_pooled["Born_TV"]
            - candidate_pooled["Born_TV"]
        ) > B317.TOL
    )
    determinism = all(
        determinism_repeat[scale]["summary_digest"]
        == trajectory[SCALE_LADDER.index(scale)]["summary_digest"]
        and determinism_repeat[scale]["counts"]
        == trajectory[SCALE_LADDER.index(scale)]["counts"]
        and determinism_repeat[scale]["generation_digest"]
        == trajectory[SCALE_LADDER.index(scale)][
            "generation_digest"
        ]
        for scale in determinism_repeat
    )
    runtime_seconds = perf_counter() - started
    stdout_preflight_bytes = len(
        compact(
            {
                "checks_so_far": CHECKS,
                "trajectory": full_trajectory,
                "verdict_evidence": verdict_evidence,
            }
        ).encode("utf-8")
    ) + len("\n".join(OUTPUT_LINES).encode("utf-8"))
    check(
        "CERTIFICATE E permutation determinism runtime and stdout controls",
        permutation_sensitive
        and determinism
        and runtime_seconds < AUDIT_TIMEOUT_SEC
        and stdout_preflight_bytes < STDOUT_LIMIT_BYTES // 2,
        {
            "determinism": {
                str(scale): {
                    "first_digest":
                        trajectory[SCALE_LADDER.index(scale)][
                            "summary_digest"
                        ],
                    "repeat_digest":
                        determinism_repeat[scale]["summary_digest"],
                }
                for scale in determinism_repeat
            },
            "largest_scale_permutation_control": {
                "candidate_assignment": FROZEN_ASSIGNMENT,
                "candidate_pooled_Born_TV":
                    candidate_pooled["Born_TV"],
                "candidate_pooled_counts":
                    candidate_largest["counts"][-1],
                "control_assignment":
                    PERMUTED_ASSIGNMENT_CONTROL,
                "control_pooled_Born_TV":
                    control_pooled["Born_TV"],
                "control_pooled_counts":
                    largest_control["counts"][-1],
                "sensitive": permutation_sensitive,
            },
            "runtime_seconds": runtime_seconds,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_preflight_bytes": stdout_preflight_bytes,
        },
    )

    endpoints = {
        scope: {
            "Born_TV_1x":
                trajectory[0]["scope_rows"][
                    SCOPE_NAMES.index(scope)
                ]["Born_TV"],
            "Born_TV_largest":
                trajectory[-1]["scope_rows"][
                    SCOPE_NAMES.index(scope)
                ]["Born_TV"],
        }
        for scope in SCOPE_NAMES[:2]
    }
    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "boundary": boundary,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "endpoints": endpoints,
        "frozen_assignment": FROZEN_ASSIGNMENT,
        "ladder": SCALE_LADDER,
        "pass": all(CHECKS.values()),
        "runtime_seconds": runtime_seconds,
        "scope_sizes": actual_sizes,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "verdict": verdict,
        "weight_claim_made": False,
    }
    report["terminal"] = (
        "CYCLE772_SCOPE_FAILURE_SCALE_PASS"
        if report["pass"]
        else "CYCLE772_SCOPE_FAILURE_SCALE_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)
    output = (
        "\n".join(OUTPUT_LINES)
        + "\n"
        + compact(report)
        + "\n"
    )
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
