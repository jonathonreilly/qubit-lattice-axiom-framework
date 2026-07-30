#!/usr/bin/env python3
"""Cycle 802 independent adversarial check: recount and attack supplies.

The Cycle 802, 788, and 766 primaries are text-only, runtime-blocklisted
references.  The fixture and ensemble rows are rebuilt from landed modules;
the stronger supply probe transports every Cycle-793 selecting variation into
the seeded ensemble rows and asks whether the frozen table changes.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import importlib.abc
import json
from math import gcd, lcm
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
TEXT_ONLY_PATHS = (
    "scripts/frontier_cycle802_enlarged_born_table_2026_07_28.py",
    "/private/tmp/cycle802-pinned-inputs/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "/private/tmp/cycle802-pinned-inputs/frontier_cycle766_family_winning_mapping_2026_07_28.py",
    "/private/tmp/cycle802-pinned-inputs/frontier_cycle788_selector_scope_extension_2026_07_28.py",
)
PRIMARY_MODULE_BLOCKLIST = (
    "frontier_cycle802_enlarged_born_table_2026_07_28",
    "frontier_cycle788_selector_scope_extension_2026_07_28",
    "frontier_cycle766_family_winning_mapping_2026_07_28",
)
C788_CHECKER_COMMIT = "608c1a8adc0f321c0f2320b3e089828506e04329"
C788_CHECKER_REF = "origin/physics-loop/proof-grade-blockF6-20260729"
C788_CHECKER_PATH = (
    "scripts/frontier_cycle788_extension_independent_check_2026_07_28.py"
)
C793_CHECKER_COMMIT = "c5b8cde48bc237efd05986bbdbea756718f2055d"
C793_CHECKER_REF = "origin/physics-loop/proof-grade-blockF7-20260729"
C793_CHECKER_PATH = (
    "scripts/frontier_cycle793_balance_independent_check_2026_07_28.py"
)

EXPECTED_INPUT_SHA256 = {
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py":
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    "scripts/protected_recurrent_actual_history_selection_cycle335_2026_07_18.py":
        "5a45d24c439fe5dc4903c1064213ad8a287ed489ed5736f7a18b34e4cc03db5f",
    "scripts/physical_transition_occurrence_close_tournament_cycle332_2026_07_18.py":
        "de7883fe45ce248427e8e44294d77fce56394e5ed14724e9056a65b43e0a4415",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py":
        "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
}
EXPECTED_TEXT_SHA256 = {
    "cycle802":
        "9670fdfcbd0b982484811abe5d91d7099afb815bcc5d5ee2929dc41633ab0fdd",
    "cycle763":
        "d2205d1ed26f3aa1ea531502470fb6fcc91bffec3b94fb6781e9154442eb5724",
    "cycle766":
        "f315180920ad6321ee41a32763f4a2606267e2bf7220f6a52cd42ce5e5382d66",
    "cycle788":
        "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    "cycle788_checker":
        "345ae7c423c529b080ce87647909472453f64119282aa41b8aa4ffbecbf4286e",
    "cycle793_checker":
        "4f96f4b862dce8d0221ff47c9f9b4e761d55ee5285cd6c8de984d22d70463399",
}

LANDED_BANKS = (2, 5, 12)
EXTENSION_BANKS = (1, 3)
ENLARGED_BANKS = LANDED_BANKS + EXTENSION_BANKS
EFFECT_IDS = (
    "cycle317-contact-trine-E0",
    "cycle317-contact-trine-E1",
    "cycle317-contact-trine-E2",
)
FROZEN_ASSIGNMENT = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
FROZEN_ASSIGNMENT_SHA256 = (
    "9ae3a8423176ba4b10daebe31239c0dfe362500241361d9bf376ac01a4cb73fc"
)
HELD_CANDIDATE_HEX = (
    "0x1.70aa1d46ad8b4p-2",
    "0x1.b20e697317e2bp-3",
    "0x1.b64eadffc6837p-2",
)
SCOPE_NAMES = ("E0", "E1", "E2", "pooled")
EXPECTED_38_COUNTS = (
    (13, 128, 68),
    (232, 97, 1),
    (146, 5, 432),
    (391, 230, 501),
)
EXPECTED_38_BORN_TV_HEX = (
    "0x1.9a1c50c983fb1p-2",
    "0x1.b3344dce20805p-2",
    "0x1.4078ace570601p-2",
    "0x1.2eeecb23145d0p-6",
)
EXPECTED_38_UNIFORM_TV_HEX = (
    "0x1.1dce302dba971p-2",
    "0x1.7a91d7a91d7a8p-2",
    "0x1.a172058fe18e2p-2",
    "0x1.06d84ca9c106ep-3",
)
EXPECTED_38_ALIGN = (False, False, True, True)
EXPECTED_CLAIMED_ROUNDED_DELTAS = {
    "E0": {"Born": "+0.046"},
    "E1": {"Born": "-0.021", "uniform": "+0.014"},
    "E2": {"Born": "+0.013"},
    "pooled": {"Born": "-0.005", "uniform": "-0.008"},
}
EXPECTED_ALIGN_TRANSITIONS = {
    "E0": (False, False),
    "E1": (False, False),
    "E2": (True, True),
    "pooled": (True, True),
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Reject any attempt to import a blocklisted primary."""

    def find_spec(self, fullname, path=None, target=None):
        if fullname in PRIMARY_MODULE_BLOCKLIST:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def resolve_path(path: str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else ROOT / candidate


def file_sha256(path: str) -> str:
    return sha256(resolve_path(path).read_bytes()).hexdigest()


def check(label: str, condition: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def source_tree(path: str) -> tuple[str, ast.Module]:
    source = resolve_path(path).read_text(encoding="utf-8")
    return source, ast.parse(source, filename=path)


def git_source(commit: str, path: str) -> str:
    return subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(("missing function", name))


def assignment_nodes(tree: ast.AST) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        for target in targets:
            if isinstance(target, ast.Name):
                found[target.id] = node.value
    return found


def same_function_ast(left: ast.FunctionDef, right: ast.FunctionDef) -> bool:
    return ast.dump(left, include_attributes=False) == ast.dump(
        right, include_attributes=False
    )


def normalized_function(tree: ast.Module, name: str) -> str:
    return " ".join(ast.unparse(function_node(tree, name)).split())


def reference_sources() -> tuple[dict[str, object], dict[str, ast.Module]]:
    labels = ("cycle802", "cycle763", "cycle766", "cycle788")
    sources: dict[str, str] = {}
    trees: dict[str, ast.Module] = {}
    for label, path in zip(labels, TEXT_ONLY_PATHS, strict=True):
        source, tree = source_tree(path)
        sources[label] = source
        trees[label] = tree
    sources["cycle788_checker"] = git_source(
        C788_CHECKER_COMMIT, C788_CHECKER_PATH
    )
    sources["cycle793_checker"] = git_source(
        C793_CHECKER_COMMIT, C793_CHECKER_PATH
    )
    trees["cycle788_checker"] = ast.parse(sources["cycle788_checker"])
    trees["cycle793_checker"] = ast.parse(sources["cycle793_checker"])
    anchors = {
        label: sha256(source.encode("utf-8")).hexdigest()
        for label, source in sources.items()
    }
    refs = {
        "cycle788_checker": subprocess.run(
            ("git", "rev-parse", C788_CHECKER_REF),
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip(),
        "cycle793_checker": subprocess.run(
            ("git", "rev-parse", C793_CHECKER_REF),
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip(),
    }
    return {
        "sha256": anchors,
        "expected_sha256": EXPECTED_TEXT_SHA256,
        "resolved_refs": refs,
        "expected_refs": {
            "cycle788_checker": C788_CHECKER_COMMIT,
            "cycle793_checker": C793_CHECKER_COMMIT,
        },
        "handling": "text_AST_only_never_imported",
    }, trees


def own_source_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=__file__)
    assignments = assignment_nodes(tree)
    audit = assignments["AUDIT_INPUT_PATHS"]
    declared = assignments["DECLARED_INPUT_PATHS"]
    imports = []
    landed_imports = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
                if alias.name.startswith(
                    ("frontier_", "protected_", "physical_")
                ):
                    landed_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(audit, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit.elts
            )
            and tuple(ast.literal_eval(audit)) == AUDIT_INPUT_PATHS
        ),
        "DECLARED_INPUT_PATHS_alias": (
            isinstance(declared, ast.Name)
            and declared.id == "AUDIT_INPUT_PATHS"
        ),
        "all_AUDIT_INPUT_PATHS_exist": all(
            resolve_path(path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "all_text_paths_exist": all(
            resolve_path(path).is_file() for path in TEXT_ONLY_PATHS
        ),
        "blocklisted_primary_AST_imports": sorted(
            set(imports).intersection(PRIMARY_MODULE_BLOCKLIST)
        ),
        "direct_landed_imports": landed_imports,
    }


def exercise_runtime_blocklist() -> dict[str, object]:
    attempts = {}
    for module in PRIMARY_MODULE_BLOCKLIST:
        try:
            __import__(module)
        except ImportError as exc:
            attempts[module] = {
                "blocked": str(exc) == f"BLOCKLIST forbids import of {module}",
                "message": str(exc),
            }
        else:
            attempts[module] = {
                "blocked": False,
                "message": "IMPORT_UNEXPECTEDLY_SUCCEEDED",
            }
    return {
        "finder_installed": PRIMARY_BLOCKER in sys.meta_path,
        "attempts": attempts,
        "none_loaded": all(
            module not in sys.modules for module in PRIMARY_MODULE_BLOCKLIST
        ),
    }


def function_assignments(node: ast.FunctionDef) -> dict[str, ast.AST]:
    found: dict[str, ast.AST] = {}
    for child in node.body:
        if not isinstance(child, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            child.targets if isinstance(child, ast.Assign) else (child.target,)
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
            elif (
                isinstance(value, ast.FormattedValue)
                and isinstance(value.value, ast.Name)
            ):
                parts.append(str(environment[value.value.id]))
            else:
                raise AssertionError(ast.dump(value))
        return "".join(parts)
    raise AssertionError(ast.dump(node))


def declared_supplies(tree: ast.Module) -> dict[str, object]:
    extension = function_node(tree, "extension_fixture")
    local = function_assignments(extension)
    inherited_node = local["inherited_supplies"]
    new_node = local["new_supplies"]
    if not isinstance(inherited_node, ast.List) or not isinstance(
        new_node, ast.List
    ):
        raise AssertionError("extension supplies are not literal lists")
    inherited = tuple(
        rendered_text(item, {"bank_count": 3, "width": 3})
        for item in inherited_node.elts
    )
    new_rows = []
    for item in new_node.elts:
        if not isinstance(item, ast.Dict):
            raise AssertionError(ast.dump(item))
        new_rows.append(
            {
                str(key.value): rendered_text(
                    value, {"bank_count": 3, "width": 3}
                )
                for key, value in zip(item.keys, item.values, strict=True)
                if isinstance(key, ast.Constant)
            }
        )
    return {"inherited": inherited, "new": tuple(new_rows)}


def construction_ast_audit(trees: dict[str, ast.Module]) -> dict[str, object]:
    generator_names = (
        "load_landed_apparatus",
        "extract_landed_seed_surface",
        "fixture_epochs",
        "mapped_event",
        "build_seeded_family",
    )
    c763_exact = {
        name: same_function_ast(
            function_node(trees["cycle802"], name),
            function_node(trees["cycle763"], name),
        )
        for name in generator_names
    }
    supplies_802 = declared_supplies(trees["cycle802"])
    supplies_788 = declared_supplies(trees["cycle788"])
    supply_constants = {
        node.value
        for node in ast.walk(
            function_node(
                trees["cycle788"], "ported_checker_supply_variation_table"
            )
        )
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    main802 = function_node(trees["cycle802"], "main")
    honest_node = next(
        value
        for name, value in assignment_nodes(main802).items()
        if name == "honest_keys"
    )
    if not isinstance(honest_node, ast.Dict):
        raise AssertionError("honest_keys is not a dict")
    honest_literals = {
        str(key.value): value.value
        for key, value in zip(
            honest_node.keys, honest_node.values, strict=True
        )
        if isinstance(key, ast.Constant)
        and isinstance(value, ast.Constant)
    }
    checker788 = normalized_function(
        trees["cycle788_checker"], "run_supply_attack"
    )
    source_checks = {
        "source_station_choices_exact": (
            "for source_index in (0, 1, stations - 1):" in checker788
            and "rotation = -source_index % stations" in checker788
        ),
        "left_rotation_choices_exact": (
            "for rotation in (0, 1, stations - 1):" in checker788
        ),
        "layer_and_Q_order_choices_exact": all(
            fragment in checker788
            for fragment in (
                "('Q_then_R', 'ascending')",
                "('Q_then_R', 'descending')",
                "('Q_then_R', 'even_then_odd')",
                "('R_then_Q', 'ascending')",
            )
        ),
        "checker_classifies_by_distinct_survivor_signatures": (
            "'SELECTS' if len(signatures) > 1 else 'NEUTRAL'"
            in checker788
        ),
    }
    build802 = function_node(trees["cycle802"], "build_seeded_family")
    build_call_names = sorted(
        {
            (
                node.func.id
                if isinstance(node.func, ast.Name)
                else node.func.attr
                if isinstance(node.func, ast.Attribute)
                else ast.unparse(node.func)
            )
            for node in ast.walk(build802)
            if isinstance(node, ast.Call)
        }
    )
    return {
        "cycle763_generator_AST_exact": c763_exact,
        "cycle788_extension_fixture_AST_exact": same_function_ast(
            function_node(trees["cycle802"], "extension_fixture"),
            function_node(trees["cycle788"], "extension_fixture"),
        ),
        "declared_supplies_802": supplies_802,
        "declared_supplies_788": supplies_788,
        "declared_supplies_exact": supplies_802 == supplies_788,
        "selecting_supply_ids_present": all(
            supply_id in supply_constants
            for supply_id in ("inherited_1", "inherited_2", "inherited_3")
        ),
        "neutral_supply_ids_present": all(
            supply_id in supply_constants
            for supply_id in (
                "inherited_4", "new_1", "new_2", "new_3"
            )
        ),
        "cycle788_checker_source_checks": source_checks,
        "build_seeded_family_call_names": build_call_names,
        "new_selection_rule_calls": tuple(
            name for name in build_call_names if "selector" in name.lower()
        ),
        "honest_literals": honest_literals,
    }


def primitive_multiplicities() -> tuple[int, ...]:
    source, tree = source_tree(AUDIT_INPUT_PATHS[4])
    target = function_node(
        tree, "mixed_projective_forcing_basis_controls"
    )
    calls = tuple(
        node
        for node in ast.walk(target)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "split_projector_isometry"
        and len(node.args) >= len(EFFECT_IDS)
        and isinstance(node.args[1], ast.Tuple)
        and len(node.args[1].elts) == len(EFFECT_IDS)
    )
    if len(calls) != 1:
        raise AssertionError(("ray split AST call count", len(calls)))
    tokens = tuple(
        ast.get_source_segment(source, item)
        for item in calls[0].args[1].elts
    )
    if any(token is None for token in tokens):
        raise AssertionError("missing split coefficient source segment")
    coefficients = tuple(Fraction(str(token)) for token in tokens)
    denominator = lcm(
        *(coefficient.denominator for coefficient in coefficients)
    )
    cleared = tuple(
        coefficient.numerator
        * (denominator // coefficient.denominator)
        for coefficient in coefficients
    )
    divisor = gcd(*cleared)
    return tuple(value // divisor for value in cleared)


def own_fixture_rows(
    bank_counts: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    rows = []
    full_family_offset = 0
    fixture_index = 0
    for bank_count in bank_counts:
        for event, direction, program, before, expected in (
            S750.k_epoch_fixtures(bank_count)
        ):
            alternatives = tuple(range(len(program)))
            selected = S750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            rows.append(
                {
                    "alternative_count": len(program),
                    "bank_count": bank_count,
                    "direction": tuple(direction),
                    "fixture_event": event,
                    "fixture_index": fixture_index,
                    "full_family_offset": full_family_offset,
                    "program": program,
                    "unrotated_selected": tuple(selected),
                }
            )
            fixture_index += 1
            full_family_offset += len(program)
    return tuple(rows)


def own_seeded_rows(
    fixtures: tuple[dict[str, object], ...],
    primitive: tuple[int, ...],
    selected_by_fixture: dict[int, tuple[int, ...]] | None = None,
) -> tuple[dict[str, int], ...]:
    rows = []
    selected_by_fixture = selected_by_fixture or {}
    for fixture in fixtures:
        stations = int(fixture["alternative_count"])
        associated = int(fixture["full_family_offset"]) % len(EFFECT_IDS)
        seed_effect = associated
        quota = min(primitive[seed_effect], stations)
        fixture_index = int(fixture["fixture_index"])
        selected_signature = selected_by_fixture.get(
            fixture_index, tuple(fixture["unrotated_selected"])
        )
        if len(selected_signature) != 1:
            raise AssertionError(
                ("non-singleton fixture selector", fixture_index)
            )
        base_selected = int(selected_signature[0])
        for local_seed_ordinal in range(quota):
            shift = (seed_effect + local_seed_ordinal) % stations
            actual = (base_selected - shift) % stations
            global_ordinal = int(fixture["full_family_offset"]) + shift
            rows.append(
                {
                    "actual_selected_alternative": actual,
                    "associated_effect_index": associated,
                    "bank_count": int(fixture["bank_count"]),
                    "fixture_event": int(fixture["fixture_event"]),
                    "fixture_index": fixture_index,
                    "global_epoch_ordinal": global_ordinal,
                    "program_shift": shift,
                    "seed_effect_index": seed_effect,
                    "seed_quota": quota,
                }
            )
    return tuple(rows)


def own_counts(
    rows: tuple[dict[str, int], ...],
) -> tuple[tuple[int, ...], ...]:
    census = [[0, 0, 0] for _stratum in EFFECT_IDS]
    for row in rows:
        stratum = int(row["associated_effect_index"])
        feature = (
            int(row["global_epoch_ordinal"])
            + int(row["actual_selected_alternative"])
        ) % len(EFFECT_IDS)
        mapped = FROZEN_ASSIGNMENT[stratum][feature]
        census[stratum][mapped] += 1
    per_scope = tuple(tuple(row) for row in census)
    pooled = tuple(
        sum(row[effect] for row in per_scope)
        for effect in range(len(EFFECT_IDS))
    )
    return per_scope + (pooled,)


def exact_tv(
    counts: tuple[int, ...],
    target: tuple[Fraction, ...],
) -> Fraction:
    size = sum(counts)
    simplex = tuple(Fraction(count, size) for count in counts)
    return sum(
        (
            abs(observed - expected)
            for observed, expected in zip(simplex, target, strict=True)
        ),
        start=Fraction(0, 1),
    ) / 2


def primary_float_tv(
    counts: tuple[int, ...],
    target: tuple[float, ...],
) -> float:
    size = sum(counts)
    simplex = tuple(Fraction(count, size) for count in counts)
    residuals = tuple(
        float(observed) - expected
        for observed, expected in zip(simplex, target, strict=True)
    )
    return sum(abs(value) for value in residuals) / 2.0


def scope_table(
    counts: tuple[tuple[int, ...], ...],
) -> tuple[dict[str, object], ...]:
    held_float = tuple(
        float.fromhex(value) for value in HELD_CANDIDATE_HEX
    )
    held_exact = tuple(Fraction.from_float(value) for value in held_float)
    uniform_exact = (Fraction(1, 3),) * len(EFFECT_IDS)
    uniform_float = (float(Fraction(1, 3)),) * len(EFFECT_IDS)
    rows = []
    for scope, scope_counts in zip(SCOPE_NAMES, counts, strict=True):
        born_exact = exact_tv(scope_counts, held_exact)
        uniform_exact_tv = exact_tv(scope_counts, uniform_exact)
        born_float = primary_float_tv(scope_counts, held_float)
        uniform_float_tv = primary_float_tv(scope_counts, uniform_float)
        rows.append(
            {
                "scope": scope,
                "counts": scope_counts,
                "sample_size": sum(scope_counts),
                "Born_TV_exact": str(born_exact),
                "Born_TV_float_hex": born_float.hex(),
                "uniform_TV_exact": str(uniform_exact_tv),
                "uniform_TV_float_hex": uniform_float_tv.hex(),
                "align_exact": born_exact < uniform_exact_tv,
                "align_primary_float": born_float < uniform_float_tv,
            }
        )
    return tuple(rows)


def side_by_side_exact(
    landed: tuple[dict[str, object], ...],
    enlarged: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    rows = []
    for old, new in zip(landed, enlarged, strict=True):
        born_delta = (
            Fraction(str(new["Born_TV_exact"]))
            - Fraction(str(old["Born_TV_exact"]))
        )
        uniform_delta = (
            Fraction(str(new["uniform_TV_exact"]))
            - Fraction(str(old["uniform_TV_exact"]))
        )
        count_delta = tuple(
            int(after) - int(before)
            for before, after in zip(
                old["counts"], new["counts"], strict=True
            )
        )
        born_float_delta = (
            float.fromhex(str(new["Born_TV_float_hex"]))
            - float.fromhex(str(old["Born_TV_float_hex"]))
        )
        uniform_float_delta = (
            float.fromhex(str(new["uniform_TV_float_hex"]))
            - float.fromhex(str(old["uniform_TV_float_hex"]))
        )
        rows.append(
            {
                "scope": old["scope"],
                "table_38": old,
                "table_46": new,
                "delta": {
                    "counts": count_delta,
                    "sample_size": (
                        int(new["sample_size"]) - int(old["sample_size"])
                    ),
                    "Born_TV_exact": str(born_delta),
                    "Born_TV_rounded_signed":
                        f"{float(born_delta):+.3f}",
                    "Born_TV_primary_float_hex": born_float_delta.hex(),
                    "uniform_TV_exact": str(uniform_delta),
                    "uniform_TV_rounded_signed":
                        f"{float(uniform_delta):+.3f}",
                    "uniform_TV_primary_float_hex":
                        uniform_float_delta.hex(),
                    "align_from": bool(old["align_exact"]),
                    "align_to": bool(new["align_exact"]),
                    "align_changed": (
                        bool(old["align_exact"])
                        != bool(new["align_exact"])
                    ),
                },
            }
        )
    return tuple(rows)


# The next nine functions are verbatim AST copies of the Cycle-793 independent
# checker's lawful selecting-supply machinery.
def rotate_left(values: tuple, amount: int) -> tuple:
    amount %= len(values)
    return values[amount:] + values[:amount]


def q_order(stations: int, mode: str) -> tuple[int, ...] | None:
    if mode == "ascending":
        return None
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return (
            tuple(range(0, stations, 2))
            + tuple(range(1, stations, 2))
        )
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


def run_r_then_q_orbit(
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


def run_varied_orbit(
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
        return run_r_then_q_orbit(
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


def station_trial(
    program: tuple,
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
    position: int,
    *,
    layer_order: str,
    order_mode: str,
) -> tuple[dict[str, bool], tuple[int, ...]]:
    tokens = tuple(
        int(index == position) for index in range(len(program))
    )
    zeros = (0,) * len(program)
    after, rail_a, rail_b = run_varied_orbit(
        before,
        program,
        token_position=position,
        reverse=False,
        layer_order=layer_order,
        order_mode=order_mode,
    )
    restored, inverse_a, inverse_b = run_varied_orbit(
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
    }, after


def selecting_variations(stations: int) -> dict[str, list[dict[str, object]]]:
    """Literal reimplementation of the three SELECT supplies in Check 788."""
    source_rows = []
    for source_index in (0, 1, stations - 1):
        source_rows.append(
            {
                "choice": f"source_station_index={source_index}",
                "program_rotation": (-source_index) % stations,
                "layer_order": "Q_then_R",
                "order_mode": "ascending",
            }
        )
    orientation_rows = []
    for rotation in (0, 1, stations - 1):
        orientation_rows.append(
            {
                "choice": f"left_rotation={rotation}",
                "program_rotation": rotation,
                "layer_order": "Q_then_R",
                "order_mode": "ascending",
            }
        )
    order_rows = []
    for layer_order, order_mode in (
        ("Q_then_R", "ascending"),
        ("Q_then_R", "descending"),
        ("Q_then_R", "even_then_odd"),
        ("R_then_Q", "ascending"),
    ):
        order_rows.append(
            {
                "choice": (
                    f"layers={layer_order};Q_order={order_mode}"
                ),
                "program_rotation": 0,
                "layer_order": layer_order,
                "order_mode": order_mode,
            }
        )
    return {
        "inherited_1": source_rows,
        "inherited_2": orientation_rows,
        "inherited_3": order_rows,
    }


def varied_orientation_signature(
    bank_count: int,
    settings: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    program = rotate_left(
        base_program, int(settings["program_rotation"])
    )
    banks, links = K719.B.chain_genesis(bank_count)
    state = K719.M.pack_state(banks, links)
    allocator = K719.M.global_allocator_word(bank_count)
    selected_signature = []
    orientation_signature = []
    identity_signature = []
    event_failures = []
    for event in range(2 * bank_count):
        mode = (1, 0) if event % 2 == 0 else (0, 1)
        before = K719.M.prepare_endpoint(state, mode)
        expected = K719.A.apply_semantic(before, allocator)
        survivors = []
        for position in range(len(program)):
            criteria, after = station_trial(
                program,
                before,
                expected,
                bank_count,
                position,
                layer_order=str(settings["layer_order"]),
                order_mode=str(settings["order_mode"]),
            )
            if all(criteria.values()):
                survivors.append((position, after))
        selected_signature.append(
            [position for position, _after in survivors]
        )
        event_orientations = []
        event_identities = []
        for _position, after in survivors:
            after_banks, after_links = K719.M.unpack_state(
                after, bank_count
            )
            chain, _decode_order = K719.B.decode_local_graph(
                after_banks, after_links
            )
            event_orientations.append(int(chain.cells[event].orientation))
            event_identities.append(int(chain.cells[event].identity))
        orientation_signature.append(event_orientations)
        identity_signature.append(event_identities)
        if len(survivors) != 1:
            event_failures.append(
                {
                    "event": event,
                    "survivors": selected_signature[-1],
                }
            )
        state = expected
    return {
        "selected_signature": selected_signature,
        "orientation_signature": orientation_signature,
        "identity_signature": identity_signature,
        "event_failures": event_failures,
        "program_stations": len(program),
    }


def supply_machinery_ast_audit(
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    names = (
        "rotate_left",
        "q_order",
        "advance_rails",
        "retreat_rails",
        "apply_live_macros",
        "run_r_then_q_orbit",
        "run_varied_orbit",
        "postimage_clean",
        "station_trial",
        "selecting_variations",
        "varied_orientation_signature",
    )
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    return {
        name: same_function_ast(
            function_node(own_tree, name),
            function_node(trees["cycle793_checker"], name),
        )
        for name in names
    }


def primary_claim_surface(tree: ast.Module) -> dict[str, object]:
    assignments = assignment_nodes(tree)
    names = (
        "LANDED_BANK_COUNTS",
        "EXTENSION_BANK_COUNTS",
        "FROZEN_ASSIGNMENT",
        "FROZEN_ASSIGNMENT_SHA256",
        "HELD_CANDIDATE_HEX",
        "EXPECTED_38_COUNTS",
        "EXPECTED_38_BORN_TV_HEX",
        "EXPECTED_38_UNIFORM_TV_HEX",
        "EXPECTED_38_ALIGN",
    )
    surface = {
        name: ast.literal_eval(assignments[name])
        for name in names
    }
    surface["ENLARGED_BANK_COUNTS_AST"] = ast.unparse(
        assignments["ENLARGED_BANK_COUNTS"]
    )
    return surface


def add_scope_counts(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            int(a) + int(b)
            for a, b in zip(left_row, right_row, strict=True)
        )
        for left_row, right_row in zip(left, right, strict=True)
    )


def supply_probe(
    landed_counts: tuple[tuple[int, ...], ...],
    new_fixtures: tuple[dict[str, object], ...],
    baseline_new_rows: tuple[dict[str, int], ...],
    primitive: tuple[int, ...],
) -> dict[str, object]:
    baseline_new_counts = own_counts(baseline_new_rows)
    baseline_new_digest = digest(baseline_new_rows)
    baseline_table = scope_table(
        add_scope_counts(landed_counts, baseline_new_counts)
    )
    rows = []
    signatures: dict[int, dict[str, list[str]]] = {}
    orientation_changes = []
    for bank in EXTENSION_BANKS:
        stations = len(K719.interleaved_program(bank))
        signatures[bank] = {}
        bank_fixtures = tuple(
            fixture
            for fixture in new_fixtures
            if int(fixture["bank_count"]) == bank
        )
        for supply_id, variations in selecting_variations(stations).items():
            signatures[bank][supply_id] = []
            for settings in variations:
                result = varied_orientation_signature(bank, settings)
                selected_signature = result["selected_signature"]
                signatures[bank][supply_id].append(
                    compact(selected_signature)
                )
                selected_by_fixture = {
                    int(fixture["fixture_index"]): tuple(
                        selected_signature[int(fixture["fixture_event"])]
                    )
                    for fixture in bank_fixtures
                }
                varied_rows = own_seeded_rows(
                    new_fixtures,
                    primitive,
                    selected_by_fixture,
                )
                varied_counts = own_counts(varied_rows)
                enlarged_counts = add_scope_counts(
                    landed_counts, varied_counts
                )
                varied_table = scope_table(enlarged_counts)
                orientations = [
                    values[0]
                    for values in result["orientation_signature"]
                    if len(values) == 1
                ]
                expected_orientations = [
                    1 if event % 2 == 0 else -1
                    for event in range(2 * bank)
                ]
                orientation_changed = (
                    bool(result["event_failures"])
                    or orientations != expected_orientations
                )
                row = {
                    "bank": bank,
                    "supply_id": supply_id,
                    "choice": settings["choice"],
                    "settings": {
                        key: settings[key]
                        for key in (
                            "program_rotation",
                            "layer_order",
                            "order_mode",
                        )
                    },
                    "selected_signature": selected_signature,
                    "orientation_signature":
                        result["orientation_signature"],
                    "identity_signature": result["identity_signature"],
                    "event_failures": result["event_failures"],
                    "orientation_changed": orientation_changed,
                    "new_ensemble_counts": varied_counts,
                    "new_ensemble_rows_sha256": digest(varied_rows),
                    "ensemble_rows_changed":
                        digest(varied_rows) != baseline_new_digest,
                    "enlarged_table_changed": varied_table != baseline_table,
                    "table_46": varied_table,
                }
                rows.append(row)
                if orientation_changed:
                    orientation_changes.append(row)
    classifications = {
        bank: {
            supply_id: (
                "SELECTS"
                if len(set(supply_signatures)) > 1
                else "NEUTRAL"
            )
            for supply_id, supply_signatures in bank_rows.items()
        }
        for bank, bank_rows in signatures.items()
    }
    ensemble_changes = [
        row for row in rows if row["ensemble_rows_changed"]
    ]
    table_changes = [
        row for row in rows if row["enlarged_table_changed"]
    ]
    complete = all(
        (
            len(rows) == len(EXTENSION_BANKS) * (3 + 3 + 4),
            all(
                verdict == "SELECTS"
                for bank_rows in classifications.values()
                for verdict in bank_rows.values()
            ),
            all(not row["event_failures"] for row in rows),
            all(
                identities == [event]
                for row in rows
                for event, identities in enumerate(
                    row["identity_signature"]
                )
            ),
            not orientation_changes,
        )
    )
    if not complete:
        verdict = "SUPPLY_PROBE_INCOMPLETE"
        finding = (
            "The selecting-supply ensemble probe was incomplete; no "
            "invariance conclusion is licensed."
        )
        caveat = "LOUD CAVEAT: SUPPLY PROBE INCOMPLETE."
    elif table_changes:
        verdict = "ENSEMBLE_TABLE_SENSITIVE_WITH_ORIENTATION_INVARIANT"
        finding = (
            "Cycle 793 orientation-invariance does not extend to the "
            "Cycle 802 ensemble table: lawful selecting-supply variations "
            "change the surviving station, the seeded ensemble rows, and "
            "at least one frozen-assignment table entry."
        )
        caveat = (
            "LOUD CAVEAT: ORIENTATION INVARIANCE IS NOT ENSEMBLE-ROW "
            "INVARIANCE.  The 4/4 new-event orientation balance survives, "
            "but the enlarged Born table is supply-sensitive."
        )
    elif ensemble_changes:
        verdict = "ENSEMBLE_ROWS_SENSITIVE_TABLE_COUNTS_INVARIANT"
        finding = (
            "Lawful selecting-supply variations change seeded ensemble "
            "rows but cancel in every frozen-assignment table count."
        )
        caveat = (
            "LOUD CAVEAT: EVENT-ROW CONTENT IS SUPPLY-SENSITIVE EVEN "
            "THOUGH THIS FINITE TABLE CENSUS IS INVARIANT."
        )
    else:
        verdict = "ENSEMBLE_ROWS_INVARIANT_ON_EXHAUSTED_VARIATIONS"
        finding = (
            "All 20 lawful selecting-supply variations preserve both the "
            "new seeded ensemble rows and the frozen enlarged table."
        )
        caveat = (
            "LOUD CAVEAT: INVARIANCE IS FINITE TO THE EXHAUSTED 788/793 "
            "VARIATION SET; THE SELECTING SUPPLIES REMAIN DECLARED."
        )
    return {
        "verdict": verdict,
        "finding": finding,
        "loud_caveat": caveat,
        "complete": complete,
        "baseline_new_counts": baseline_new_counts,
        "baseline_new_rows_sha256": baseline_new_digest,
        "classifications": classifications,
        "variation_count": len(rows),
        "ensemble_row_change_count": len(ensemble_changes),
        "table_change_count": len(table_changes),
        "orientation_change_count": len(orientation_changes),
        "variation_rows": rows,
    }


def run_core(trees: dict[str, ast.Module]) -> dict[str, object]:
    primitive = primitive_multiplicities()
    landed_fixtures = own_fixture_rows(LANDED_BANKS)
    enlarged_fixtures = own_fixture_rows(ENLARGED_BANKS)
    landed_rows = own_seeded_rows(landed_fixtures, primitive)
    enlarged_rows = own_seeded_rows(enlarged_fixtures, primitive)
    new_fixtures = enlarged_fixtures[len(landed_fixtures):]
    new_rows = tuple(
        row
        for row in enlarged_rows
        if int(row["fixture_index"]) >= len(landed_fixtures)
    )
    landed_counts = own_counts(landed_rows)
    enlarged_counts = own_counts(enlarged_rows)
    landed_table = scope_table(landed_counts)
    enlarged_table = scope_table(enlarged_counts)
    side_by_side = side_by_side_exact(landed_table, enlarged_table)
    construction = construction_ast_audit(trees)
    supply_ast = supply_machinery_ast_audit(trees)
    supply = supply_probe(
        landed_counts,
        new_fixtures,
        new_rows,
        primitive,
    )
    return {
        "primitive_multiplicities": primitive,
        "landed_fixture_count": len(landed_fixtures),
        "enlarged_fixture_count": len(enlarged_fixtures),
        "landed_prefix_exact": (
            enlarged_fixtures[:len(landed_fixtures)]
            == landed_fixtures
        ),
        "new_fixture_count": len(new_fixtures),
        "new_bank_sequence": tuple(
            int(fixture["bank_count"]) for fixture in new_fixtures
        ),
        "new_selector_outputs": tuple(
            fixture["unrotated_selected"] for fixture in new_fixtures
        ),
        "new_fixture_row_counts": tuple(
            sum(
                int(row["fixture_index"]) == int(fixture["fixture_index"])
                for row in new_rows
            )
            for fixture in new_fixtures
        ),
        "landed_row_count": len(landed_rows),
        "enlarged_row_count": len(enlarged_rows),
        "new_row_count": len(new_rows),
        "landed_rows_sha256": digest(landed_rows),
        "enlarged_rows_sha256": digest(enlarged_rows),
        "new_rows_sha256": digest(new_rows),
        "landed_counts": landed_counts,
        "enlarged_counts": enlarged_counts,
        "landed_table": landed_table,
        "enlarged_table": enlarged_table,
        "side_by_side": side_by_side,
        "construction_ast": construction,
        "supply_ast": supply_ast,
        "supply": supply,
    }


def main() -> int:
    input_sha_before = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    reference_before, trees = reference_sources()
    own_audit = own_source_audit()
    blocklist = exercise_runtime_blocklist()
    claim_surface = primary_claim_surface(trees["cycle802"])
    first = run_core(trees)

    primary_surface_exact = all(
        (
            claim_surface["LANDED_BANK_COUNTS"] == LANDED_BANKS,
            claim_surface["EXTENSION_BANK_COUNTS"] == EXTENSION_BANKS,
            claim_surface["ENLARGED_BANK_COUNTS_AST"]
            == "LANDED_BANK_COUNTS + EXTENSION_BANK_COUNTS",
            claim_surface["FROZEN_ASSIGNMENT"] == FROZEN_ASSIGNMENT,
            claim_surface["FROZEN_ASSIGNMENT_SHA256"]
            == FROZEN_ASSIGNMENT_SHA256,
            claim_surface["HELD_CANDIDATE_HEX"]
            == HELD_CANDIDATE_HEX,
            claim_surface["EXPECTED_38_COUNTS"] == EXPECTED_38_COUNTS,
            claim_surface["EXPECTED_38_BORN_TV_HEX"]
            == EXPECTED_38_BORN_TV_HEX,
            claim_surface["EXPECTED_38_UNIFORM_TV_HEX"]
            == EXPECTED_38_UNIFORM_TV_HEX,
            claim_surface["EXPECTED_38_ALIGN"] == EXPECTED_38_ALIGN,
        )
    )
    identity_pass = all(
        (
            primary_surface_exact,
            digest(FROZEN_ASSIGNMENT) == FROZEN_ASSIGNMENT_SHA256,
            first["landed_fixture_count"] == 38,
            first["landed_row_count"] == 1122,
            first["landed_counts"] == EXPECTED_38_COUNTS,
            tuple(
                row["Born_TV_float_hex"]
                for row in first["landed_table"]
            ) == EXPECTED_38_BORN_TV_HEX,
            tuple(
                row["uniform_TV_float_hex"]
                for row in first["landed_table"]
            ) == EXPECTED_38_UNIFORM_TV_HEX,
            tuple(
                row["align_exact"] for row in first["landed_table"]
            ) == EXPECTED_38_ALIGN,
            all(
                row["align_exact"] == row["align_primary_float"]
                for row in first["landed_table"]
            ),
        )
    )
    identity_finding = (
        "The independent 38-event census reproduces all frozen Cycle-766 "
        "counts, all primary-compatible TV hex values, and every align flag "
        "exactly."
        if identity_pass
        else (
            "REFUTATION: the 38-event identity control does not reproduce "
            "the frozen Cycle-766 table under independent census arithmetic."
        )
    )
    check(
        "CERTIFICATE_A_IDENTITY_CONTROL",
        identity_pass,
        {
            "finding": identity_finding,
            "frozen_assignment_sha256": digest(FROZEN_ASSIGNMENT),
            "primary_claim_surface_exact": primary_surface_exact,
            "table_38": first["landed_table"],
        },
    )
    OUTPUT_LINES.append("FINDING_IDENTITY " + identity_finding)

    construction = first["construction_ast"]
    construction_pass = all(
        (
            all(construction["cycle763_generator_AST_exact"].values()),
            construction["cycle788_extension_fixture_AST_exact"],
            construction["declared_supplies_exact"],
            construction["selecting_supply_ids_present"],
            construction["neutral_supply_ids_present"],
            all(
                construction[
                    "cycle788_checker_source_checks"
                ].values()
            ),
            not construction["new_selection_rule_calls"],
            first["primitive_multiplicities"] == (17, 29, 54),
            first["landed_prefix_exact"],
            first["new_fixture_count"] == 8,
            first["new_bank_sequence"] == (1, 1, 3, 3, 3, 3, 3, 3),
            first["new_selector_outputs"] == ((0,),) * 8,
            first["new_row_count"] == 116,
            sum(first["new_fixture_row_counts"]) == 116,
            all(count > 0 for count in first["new_fixture_row_counts"]),
        )
    )
    construction_finding = (
        "The eight extension fixtures enter through an AST-identical "
        "Cycle-763 generator with no added selector call; their 116 seeded "
        "rows and the Cycle-788 declared supply layer are independently "
        "recounted."
        if construction_pass
        else (
            "REFUTATION: the new-event construction is not an exact "
            "Cycle-763-generator continuation with the declared Cycle-788 "
            "supply layer."
        )
    )
    check(
        "CERTIFICATE_B_NEW_EVENT_CONSTRUCTION_AUDIT",
        construction_pass,
        {
            "finding": construction_finding,
            "construction_AST": construction,
            "new_bank_sequence": first["new_bank_sequence"],
            "new_fixture_row_counts": first["new_fixture_row_counts"],
            "new_ensemble_row_count": first["new_row_count"],
            "new_ensemble_rows_sha256": first["new_rows_sha256"],
            "primitive_multiplicities":
                first["primitive_multiplicities"],
        },
    )
    OUTPUT_LINES.append("FINDING_CONSTRUCTION " + construction_finding)

    side_by_side = first["side_by_side"]
    rounded_claims_pass = all(
        row["delta"][f"{metric}_TV_rounded_signed"] == expected
        for row in side_by_side
        for metric, expected in EXPECTED_CLAIMED_ROUNDED_DELTAS[
            str(row["scope"])
        ].items()
    )
    align_pass = all(
        (
            row["delta"]["align_from"],
            row["delta"]["align_to"],
        ) == EXPECTED_ALIGN_TRANSITIONS[str(row["scope"])]
        and row["delta"]["align_changed"] is False
        for row in side_by_side
    )
    table_pass = all(
        (
            first["enlarged_fixture_count"] == 46,
            first["enlarged_row_count"] == 1238,
            first["enlarged_row_count"] - first["landed_row_count"]
            == first["new_row_count"] == 116,
            first["enlarged_table"][-1]["sample_size"] == 1238,
            rounded_claims_pass,
            align_pass,
            all(
                row["align_exact"] == row["align_primary_float"]
                for row in first["enlarged_table"]
            ),
            tuple(
                sum(
                    int(first["enlarged_counts"][stratum][effect])
                    for stratum in range(3)
                )
                for effect in range(3)
            ) == first["enlarged_counts"][-1],
            construction["honest_literals"].get("decides_nothing")
            is True,
            construction["honest_literals"].get(
                "first_new_content_point"
            ) is True,
        )
    )
    table_finding = (
        "The enlarged 46-event table agrees with the primary: 1,238 rows, "
        "116 new rows, every exact rational TV/count delta, all advertised "
        "three-decimal moves, and all false/false or true/true align flags."
        if table_pass
        else (
            "REFUTATION: at least one enlarged-table count, exact TV, "
            "advertised delta, honest key, or align transition disagrees."
        )
    )
    check(
        "CERTIFICATE_C_ENLARGED_TABLE_RECOUNT",
        table_pass,
        {
            "finding": table_finding,
            "enlarged_ensemble_rows": first["enlarged_row_count"],
            "new_ensemble_rows": first["new_row_count"],
            "honest_literals": construction["honest_literals"],
            "rounded_claims_pass": rounded_claims_pass,
            "align_pass": align_pass,
        },
    )
    for row in side_by_side:
        OUTPUT_LINES.append(
            "DATA EXACT_SIDE_BY_SIDE "
            + str(row["scope"])
            + " :: "
            + compact(row)
        )
    OUTPUT_LINES.append("FINDING_TABLE " + table_finding)

    supply = first["supply"]
    supply_pass = all(
        (
            all(first["supply_ast"].values()),
            supply["complete"],
            supply["variation_count"] == 20,
            supply["orientation_change_count"] == 0,
            supply["verdict"] != "SUPPLY_PROBE_INCOMPLETE",
        )
    )
    check(
        "CERTIFICATE_D_SUPPLY_SENSITIVITY_PROBE",
        supply_pass,
        {
            "finding": supply["finding"],
            "loud_caveat": supply["loud_caveat"],
            "machinery_AST_exact": first["supply_ast"],
            "classifications": supply["classifications"],
            "variation_count": supply["variation_count"],
            "ensemble_row_change_count":
                supply["ensemble_row_change_count"],
            "table_change_count": supply["table_change_count"],
            "orientation_change_count":
                supply["orientation_change_count"],
            "verdict": supply["verdict"],
        },
    )
    for row in supply["variation_rows"]:
        OUTPUT_LINES.append(
            "DATA SUPPLY_VARIATION :: " + compact(row)
        )
    OUTPUT_LINES.append("FINDING_SUPPLY_SENSITIVITY " + supply["finding"])
    OUTPUT_LINES.append(supply["loud_caveat"])

    repeated = run_core(trees)
    input_sha_after = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    reference_after, _trees_after = reference_sources()
    elapsed = monotonic() - START
    deterministic = first == repeated
    stdout_before_e = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    )
    controls_pass = all(
        (
            own_audit["literal_AUDIT_INPUT_PATHS"],
            own_audit["DECLARED_INPUT_PATHS_alias"],
            own_audit["all_AUDIT_INPUT_PATHS_exist"],
            own_audit["all_text_paths_exist"],
            not own_audit["blocklisted_primary_AST_imports"],
            blocklist["finder_installed"],
            blocklist["none_loaded"],
            all(
                row["blocked"]
                for row in blocklist["attempts"].values()
            ),
            input_sha_before == input_sha_after
            == EXPECTED_INPUT_SHA256,
            reference_before == reference_after,
            reference_before["sha256"] == EXPECTED_TEXT_SHA256,
            reference_before["resolved_refs"]
            == reference_before["expected_refs"],
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
            stdout_before_e + 16 * 1024 < STDOUT_LIMIT_BYTES,
        )
    )
    check(
        "CERTIFICATE_E_CONTROLS_DETERMINISM_AND_BOUNDS",
        controls_pass,
        {
            "finding": (
                "All SHA anchors, literal input paths, runtime import "
                "blockers, input stability, repeat digest, runtime, and "
                "stdout bounds hold."
                if controls_pass
                else (
                    "REFUTATION: at least one SHA, blocklist, determinism, "
                    "runtime, or stdout control failed."
                )
            ),
            "blocklist": blocklist,
            "deterministic": deterministic,
            "first_digest": digest(first),
            "input_sha256": input_sha_before,
            "reference_anchors": reference_before,
            "repeat_digest": digest(repeated),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "runtime_seconds": round(elapsed, 6),
            "stdout_before_certificate_e": stdout_before_e,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    report = {
        "cycle": 802,
        "role": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "pass": all(CHECKS.values()),
        "certificates": dict(CHECKS),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "identity_agrees": identity_pass,
        "enlarged_recount_agrees": table_pass,
        "supply_sensitivity_verdict": supply["verdict"],
        "supply_table_change_count": supply["table_change_count"],
        "orientation_change_count": supply["orientation_change_count"],
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE802_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if all(CHECKS.values())
            else "CYCLE802_INDEPENDENT_ADVERSARIAL_CHECK_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    output = "\n".join(OUTPUT_LINES) + "\nSUMMARY_JSON " + compact(report) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
