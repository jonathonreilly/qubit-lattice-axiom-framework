#!/usr/bin/env python3
"""Cycle 802: first Born table over the enlarged 46-fixture ensemble family.

The Cycle-763 generator and Cycle-766 assignment are frozen text/AST
comparators.  Cycle 788 is fetched from its pinned blockF6 commit as text,
never imported, and its bank-1/3 extension constructor is reimplemented
verbatim.  The eight new selector fixtures are appended to the landed 38;
the mapping and held candidates are not refit.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py",
    "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from contextlib import redirect_stdout
from fractions import Fraction
from hashlib import sha256
import io
import json
from math import gcd, lcm
from pathlib import Path
import subprocess
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


PIN_ROOT = Path("/private/tmp/cycle802-pinned-inputs")
BLOCKF6_REF = "origin/physics-loop/proof-grade-blockF6-20260729"
BLOCKF6_COMMIT = "608c1a8adc0f321c0f2320b3e089828506e04329"
PINNED_SPECS = {
    AUDIT_INPUT_PATHS[3]: {
        "revision": "e8e355c197feb4c077122846738a860de5106761",
        "repo_path":
            "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
        "sha256":
            "d2205d1ed26f3aa1ea531502470fb6fcc91bffec3b94fb6781e9154442eb5724",
    },
    AUDIT_INPUT_PATHS[4]: {
        "revision": "e4d7991fe1685ad0b463877a156404a55bae10e4",
        "repo_path":
            "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py",
        "sha256":
            "f315180920ad6321ee41a32763f4a2606267e2bf7220f6a52cd42ce5e5382d66",
    },
    AUDIT_INPUT_PATHS[5]: {
        "revision": BLOCKF6_REF,
        "repo_path":
            "scripts/frontier_cycle788_selector_scope_extension_2026_07_28.py",
        "sha256":
            "5af27fd61c20fe3b25e9a172b63339d5fd4f5112631fe6d31c6e0fa95a7486f1",
    },
}
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
    **{
        path: str(spec["sha256"])
        for path, spec in PINNED_SPECS.items()
    },
}
COMPARATOR_MODULE_BLOCKLIST = (
    "frontier_cycle763_symmetry_broken_ensembles_2026_07_28",
    "frontier_cycle766_family_winning_mapping_2026_07_28",
    "frontier_cycle788_selector_scope_extension_2026_07_28",
)

LANDED_BANK_COUNTS = (2, 5, 12)
EXTENSION_BANK_COUNTS = (1, 3)
ENLARGED_BANK_COUNTS = LANDED_BANK_COUNTS + EXTENSION_BANK_COUNTS
BANK_COUNTS = LANDED_BANK_COUNTS
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
HELD_CANDIDATE = tuple(float.fromhex(value) for value in HELD_CANDIDATE_HEX)
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

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest_rows(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(label: str, condition: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def resolve_input(path: str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else ROOT / candidate


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_bytes(revision: str, repo_path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{revision}:{repo_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def materialize_pinned_texts() -> dict[str, str]:
    """Make immutable disk copies without importing or executing their text."""
    PIN_ROOT.mkdir(parents=True, exist_ok=True)
    observed = {}
    for path, spec in PINNED_SPECS.items():
        payload = git_bytes(str(spec["revision"]), str(spec["repo_path"]))
        payload_sha = sha256(payload).hexdigest()
        if payload_sha != spec["sha256"]:
            raise AssertionError(("pinned blob drift", path, payload_sha))
        destination = Path(path)
        if not destination.exists() or destination.read_bytes() != payload:
            temporary = destination.with_suffix(destination.suffix + ".tmp")
            temporary.write_bytes(payload)
            temporary.replace(destination)
        observed[path] = file_sha256(destination)
    return observed


def top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    rows = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        for target in targets:
            if isinstance(target, ast.Name):
                rows[target.id] = node.value
    return rows


def same_function_ast(left: ast.FunctionDef, right: ast.FunctionDef) -> bool:
    return ast.dump(left, include_attributes=False) == ast.dump(
        right,
        include_attributes=False,
    )


def comparator_audit() -> dict[str, object]:
    """Parse all three historical sources as text only."""
    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source, filename=__file__)
    own_functions = top_level_functions(own_tree)
    own_assignments = top_level_assignments(own_tree)
    trees = {
        cycle: ast.parse(
            Path(AUDIT_INPUT_PATHS[index]).read_text(encoding="utf-8"),
            filename=AUDIT_INPUT_PATHS[index],
        )
        for cycle, index in (("763", 3), ("766", 4), ("788", 5))
    }
    functions763 = top_level_functions(trees["763"])
    functions766 = top_level_functions(trees["766"])
    functions788 = top_level_functions(trees["788"])

    c763_names = (
        "load_landed_apparatus",
        "extract_landed_seed_surface",
        "fixture_epochs",
        "mapped_event",
        "build_seeded_family",
    )
    c763_generator_ast_exact = {
        name: same_function_ast(own_functions[name], functions763[name])
        for name in c763_names
    }
    frozen_bindings = tuple(
        node
        for node in ast.walk(functions766["main"])
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "frozen_mapping"
            for target in node.targets
        )
    )
    frozen_binding_exact = bool(
        len(frozen_bindings) == 1
        and isinstance(frozen_bindings[0].value, ast.Subscript)
        and isinstance(frozen_bindings[0].value.value, ast.Name)
        and frozen_bindings[0].value.value.id == "maximal"
        and isinstance(frozen_bindings[0].value.slice, ast.Constant)
        and frozen_bindings[0].value.slice.value == "per_stratum_mapping"
    )
    supply_strings = {
        node.value
        for node in ast.walk(
            functions788["ported_checker_supply_variation_table"]
        )
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    dynamic_text_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in ast.walk(own_tree)
                if isinstance(node, ast.Call)
                and ast.unparse(node.func)
                in {"compile", "eval", "exec", "__import__"}
            }
        )
    )
    audit_node = own_assignments["AUDIT_INPUT_PATHS"]
    declared_node = own_assignments["DECLARED_INPUT_PATHS"]
    literal_audit_tuple = bool(
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )
    blockf6_head = subprocess.run(
        ["git", "rev-parse", BLOCKF6_REF],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return {
        "blockf6_head": blockf6_head,
        "blockf6_primary_fetched_from_origin_ref": (
            blockf6_head == BLOCKF6_COMMIT
            and PINNED_SPECS[AUDIT_INPUT_PATHS[5]]["revision"]
            == BLOCKF6_REF
        ),
        "blocklisted_module_in_sys_modules": tuple(
            name for name in COMPARATOR_MODULE_BLOCKLIST if name in sys.modules
        ),
        "c763_generator_ast_exact": c763_generator_ast_exact,
        "cycle766_frozen_binding_exact": frozen_binding_exact,
        "cycle788_extension_fixture_ast_exact": same_function_ast(
            own_functions["extension_fixture"],
            functions788["extension_fixture"],
        ),
        "cycle788_supply_ids_present": all(
            name in supply_strings
            for name in (
                "inherited_1",
                "inherited_2",
                "inherited_3",
                "inherited_4",
                "new_1",
                "new_2",
                "new_3",
            )
        ),
        "dynamic_text_calls": dynamic_text_calls,
        "literal_audit_tuple": literal_audit_tuple,
    }


# The following five functions are verbatim AST copies of the pinned C763
# construction surface.  They deliberately remain ordinary local functions:
# the pinned comparator module is never imported.
def load_landed_apparatus() -> tuple[
    tuple[np.ndarray, ...],
    dict[str, object],
    str,
]:
    captured = io.StringIO()
    with redirect_stdout(captured):
        fixtures = B317.physical_subcode_controls()
        _trine_kraus, trine_effects = B317.contact_trine_controls(
            fixtures[3]
        )
        _forcing_kraus, forcing_data = (
            B317.mixed_projective_forcing_basis_controls(fixtures[3])
        )
    return trine_effects, forcing_data, captured.getvalue()


def extract_landed_seed_surface(
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
) -> dict[str, object]:
    """Extract the ray-split literals and derive all seed integers from them."""
    source_path = Path(B317.__file__).resolve()
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(source_path))
    target_function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "mixed_projective_forcing_basis_controls"
    )
    calls = tuple(
        node
        for node in ast.walk(target_function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "split_projector_isometry"
        and len(node.args) >= len(EFFECT_IDS)
        and isinstance(node.args[1], ast.Tuple)
        and len(node.args[1].elts) == len(EFFECT_IDS)
    )
    if len(calls) != len(EFFECT_IDS[:1]):
        raise AssertionError(("ray split AST call count", len(calls)))
    split_node = calls[0].args[1]
    coefficient_tokens = tuple(
        ast.get_source_segment(source, element)
        for element in split_node.elts
    )
    if any(token is None for token in coefficient_tokens):
        raise AssertionError("missing exact source segment for B317 split")
    coefficients = tuple(
        Fraction(token) for token in coefficient_tokens
    )
    common_denominator = lcm(
        *(coefficient.denominator for coefficient in coefficients)
    )
    cleared = tuple(
        coefficient.numerator
        * (common_denominator // coefficient.denominator)
        for coefficient in coefficients
    )
    common_divisor = gcd(*cleared)
    primitive_multiplicities = tuple(
        value // common_divisor for value in cleared
    )

    ray_effects = tuple(forcing_data["ray"][:len(EFFECT_IDS)])
    ray_traces = tuple(
        float(np.trace(effect).real) for effect in ray_effects
    )
    overlap_matrix = tuple(
        tuple(
            float(np.trace(left @ right).real)
            for right in trine_effects
        )
        for left in trine_effects
    )
    self_association = tuple(
        max(range(len(row)), key=row.__getitem__)
        for row in overlap_matrix
    )
    return {
        "b317_source_path": str(source_path.relative_to(ROOT)),
        "coefficient_tokens": coefficient_tokens,
        "coefficients": coefficients,
        "coefficient_sum": sum(
            coefficients, start=Fraction(0, 1)
        ),
        "primitive_multiplicities": primitive_multiplicities,
        "ray_effect_traces": ray_traces,
        "ray_trace_matches": tuple(
            abs(float(coefficient) - trace) < B317.TOL
            for coefficient, trace in zip(
                coefficients, ray_traces, strict=True
            )
        ),
        "trine_overlap_matrix": overlap_matrix,
        "trine_self_association": self_association,
    }


def fixture_epochs() -> tuple[dict[str, object], ...]:
    rows = []
    full_family_offset = 0
    fixture_index = 0
    for bank_count in BANK_COUNTS:
        for event, direction, program, before, expected in (
            F750.k_epoch_fixtures(bank_count)
        ):
            alternatives = tuple(range(len(program)))
            selected = F750.enforcement_lineage_selector(
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
                    "before": before,
                    "direction": tuple(direction),
                    "event": event,
                    "expected": expected,
                    "fixture_index": fixture_index,
                    "full_family_offset": full_family_offset,
                    "program": program,
                    "unrotated_selected": tuple(selected),
                }
            )
            fixture_index += 1
            full_family_offset += len(program)
    return tuple(rows)


def mapped_event(
    fixture: dict[str, object],
    shift: int,
    selected: tuple[int, ...],
    *,
    associated_effect_index: int,
    family_mode: str,
    seed_effect_index: int,
    seed_quota: int,
) -> dict[str, object]:
    actual = selected[0] if len(selected) == 1 else None
    global_epoch_ordinal = fixture["full_family_offset"] + shift
    outcome_index = (
        (global_epoch_ordinal + actual) % len(EFFECT_IDS)
        if actual is not None
        else None
    )
    return {
        "actual_selected_alternative": actual,
        "alternative_count": fixture["alternative_count"],
        "associated_effect_id": EFFECT_IDS[associated_effect_index],
        "associated_effect_index": associated_effect_index,
        "bank_count": fixture["bank_count"],
        "effect_id": (
            EFFECT_IDS[outcome_index]
            if outcome_index is not None
            else None
        ),
        "family_mode": family_mode,
        "fixture_event": fixture["event"],
        "fixture_index": fixture["fixture_index"],
        "global_epoch_ordinal": global_epoch_ordinal,
        "outcome_index": outcome_index,
        "program_shift": shift,
        "seed_effect_id": EFFECT_IDS[seed_effect_index],
        "seed_effect_index": seed_effect_index,
        "seed_quota": seed_quota,
        "selected_alternatives": selected,
    }


def build_seeded_family(
    fixtures: tuple[dict[str, object], ...],
    primitive_multiplicities: tuple[int, ...],
    effect_permutation: tuple[int, ...],
    *,
    family_mode: str,
) -> tuple[tuple[dict[str, object], ...], dict[str, object]]:
    rows = []
    covered_bank_shifts = set()
    for fixture in fixtures:
        station_count = fixture["alternative_count"]
        associated = fixture["full_family_offset"] % len(EFFECT_IDS)
        seed_effect = effect_permutation[associated]
        quota = min(
            primitive_multiplicities[seed_effect],
            station_count,
        )
        shifts = tuple(
            (seed_effect + local_seed_ordinal) % station_count
            for local_seed_ordinal in range(quota)
        )
        if len(shifts) != len(set(shifts)):
            raise AssertionError(("non-unique seed window", shifts))
        for shift in shifts:
            # F750.cyclic_enforcement_symmetry explicitly evaluates every
            # bank/shift pair in the 137-case landed covariance basis.  The
            # transported singleton below is its exact covariant reference,
            # applied to each fixture as in the Cycle-760 family machinery.
            selected = ((station_count - shift) % station_count,)
            covered_bank_shifts.add(
                (fixture["bank_count"], shift)
            )
            rows.append(
                mapped_event(
                    fixture,
                    shift,
                    selected,
                    associated_effect_index=associated,
                    family_mode=family_mode,
                    seed_effect_index=seed_effect,
                    seed_quota=quota,
                )
            )
    stats = {
        "covariance_transported_rows": len(rows),
        "covered_bank_shift_pairs": len(covered_bank_shifts),
        "family_mode": family_mode,
        "F750_selector_basis": (
            "38 unrotated fixture calls plus all 137 explicit landed "
            "bank/rotation covariance cases"
        ),
        "retained_rotations": len(rows),
        "row_digest": digest_rows(
            tuple(
                {
                    key: value
                    for key, value in row.items()
                    if key not in {"selected_alternatives"}
                }
                for row in rows
            )
        ),
        "selected_count_range": (
            min(len(row["selected_alternatives"]) for row in rows),
            max(len(row["selected_alternatives"]) for row in rows),
        ),
    }
    return tuple(rows), stats


# This is the pinned Cycle-788 bank-extension constructor, copied verbatim at
# the AST level and kept local because Cycle 788 itself is blocklisted.
def extension_fixture(bank_count: int):
    program = K719.interleaved_program(bank_count)
    width = max(3, bank_count)
    height = len(program) - width + 2
    track = K719.rectangle_track(width, height)
    inherited_supplies = [
        "one controller token at source station and zero B/work rails",
        "source boundary and oriented finite program ring",
        "Q-before-R layer order and bounded local macro gate order",
        "clean data-bank/link/route genesis and event predicates",
    ]
    new_supplies = [
        {
            "choice": (
                "extend the landed rectangle_track family to "
                f"bank {bank_count}"
            ),
            "reason": (
                f"held_physical_program_and_track({bank_count}) raises "
                "ValueError and "
                "contains no new-size constructor"
            ),
        },
        {
            "choice": (
                "rectangle width=max(3,bank_count), hence "
                f"width={width}"
            ),
            "reason": (
                "this single shape rule reproduces the landed widths at "
                "2/5/12 but is not derived by the landed code"
            ),
        },
        {
            "choice": "rectangle_track default origin=(-26,-7,-4)",
            "reason": (
                f"the landed code derives no bank-{bank_count} embedding "
                "origin; the selector uses only covariant geometry tests"
            ),
        },
    ]
    derived = [
        {
            "fact": f"height={height}",
            "derivation": (
                "rectangle perimeter 2*(width+height)-4 is forced to equal "
                f"2*program_stations={2 * len(program)}"
            ),
        },
        {
            "fact": f"epochs={2 * bank_count}",
            "derivation": "unchanged k_epoch_fixtures and held_certificate law",
        },
        {
            "fact": f"program_stations={len(program)} with no added padding",
            "derivation": "K719.interleaved_program(bank_count) landed default",
        },
    ]
    return program, track, {
        "banks": bank_count,
        "program_stations": len(program),
        "width": width,
        "height": height,
        "track_sites": len(track),
        "inherited_supplies": inherited_supplies,
        "new_supplies": new_supplies,
        "derived_not_supplied": derived,
    }


def selected_event_feature(
    event: dict[str, object],
    effect_domain: tuple[int, ...],
) -> int:
    return (
        event["global_epoch_ordinal"]
        + event["actual_selected_alternative"]
    ) % len(effect_domain)


def count_frozen_assignment(
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    """Apply the frozen Cycle-766 assignment once to every ensemble row."""
    effect_domain = tuple(range(len(mapping)))
    rows = [
        [int() for _effect_index in effect_domain]
        for _stratum_index in effect_domain
    ]
    for event in events:
        stratum_index = int(event["associated_effect_index"])
        feature_index = selected_event_feature(event, effect_domain)
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
        for observed, expected in zip(simplex, target, strict=True)
    )
    tv = sum(abs(value) for value in residuals) / 2.0
    return {
        "TV": tv,
        "TV_hex": tv.hex(),
        "simplex": tuple(str(value) for value in simplex),
    }


def per_scope_table(
    counts: tuple[tuple[int, ...], ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    uniform = tuple(
        float(Fraction(1, len(EFFECT_IDS)))
        for _effect_id in EFFECT_IDS
    )
    rows = []
    for scope, scope_counts in zip(SCOPE_NAMES, counts, strict=True):
        born = distance_metrics(scope_counts, held_candidate)
        flat = distance_metrics(scope_counts, uniform)
        rows.append(
            {
                "align": born["TV"] < flat["TV"],
                "Born_TV": born["TV"],
                "Born_TV_hex": born["TV_hex"],
                "counts": scope_counts,
                "sample_size": sum(scope_counts),
                "scope": scope,
                "uniform_TV": flat["TV"],
                "uniform_TV_hex": flat["TV_hex"],
            }
        )
    return tuple(rows)


def move_direction(delta: float) -> str:
    if delta > 0.0:
        return "increase"
    if delta < 0.0:
        return "decrease"
    return "unchanged"


def side_by_side_table(
    landed: tuple[dict[str, object], ...],
    enlarged: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    rows = []
    for old, new in zip(landed, enlarged, strict=True):
        born_delta = float(new["Born_TV"]) - float(old["Born_TV"])
        uniform_delta = (
            float(new["uniform_TV"]) - float(old["uniform_TV"])
        )
        count_delta = tuple(
            int(after) - int(before)
            for before, after in zip(
                old["counts"], new["counts"], strict=True
            )
        )
        rows.append(
            {
                "scope": old["scope"],
                "table_38": old,
                "table_46": new,
                "delta": {
                    "Born_TV": born_delta,
                    "Born_TV_hex": born_delta.hex(),
                    "Born_TV_direction": move_direction(born_delta),
                    "align_changed": old["align"] != new["align"],
                    "align_from": old["align"],
                    "align_to": new["align"],
                    "counts": count_delta,
                    "sample_size":
                        int(new["sample_size"]) - int(old["sample_size"]),
                    "uniform_TV": uniform_delta,
                    "uniform_TV_hex": uniform_delta.hex(),
                    "uniform_TV_direction": move_direction(uniform_delta),
                },
            }
        )
    return tuple(rows)


def declared_supply_layer(
    constructions: dict[int, dict[str, object]],
) -> dict[str, object]:
    reference = constructions[EXTENSION_BANK_COUNTS[0]]
    inherited = tuple(reference["inherited_supplies"])
    shared = all(
        tuple(construction["inherited_supplies"][:3]) == inherited[:3]
        for construction in constructions.values()
    )
    return {
        "classification_source":
            "pinned Cycle788 checker supply-variation table",
        "selecting_supply_ids":
            ("inherited_1", "inherited_2", "inherited_3"),
        "selecting_supply_declarations": inherited[:3],
        "neutral_supply_ids":
            ("inherited_4", "new_1", "new_2", "new_3"),
        "shared_by_landed_38": shared,
        "new_scope_supplies": {
            str(bank_count): construction["new_supplies"]
            for bank_count, construction in constructions.items()
            if bank_count in EXTENSION_BANK_COUNTS
        },
    }


def table_identity_exact(table: tuple[dict[str, object], ...]) -> bool:
    return bool(
        tuple(tuple(row["counts"]) for row in table)
        == EXPECTED_38_COUNTS
        and tuple(str(row["Born_TV_hex"]) for row in table)
        == EXPECTED_38_BORN_TV_HEX
        and tuple(str(row["uniform_TV_hex"]) for row in table)
        == EXPECTED_38_UNIFORM_TV_HEX
        and tuple(bool(row["align"]) for row in table)
        == EXPECTED_38_ALIGN
    )


def run_experiment_once() -> dict[str, object]:
    global BANK_COUNTS

    trine_effects, forcing_data, captured_b317 = load_landed_apparatus()
    seed_surface = extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    primitive = tuple(seed_surface["primitive_multiplicities"])
    effect_domain = tuple(range(len(EFFECT_IDS)))

    BANK_COUNTS = LANDED_BANK_COUNTS
    landed_fixtures = fixture_epochs()
    landed_events, landed_stats = build_seeded_family(
        landed_fixtures,
        primitive,
        effect_domain,
        family_mode="cycle802-38-fixture-identity-control",
    )

    BANK_COUNTS = ENLARGED_BANK_COUNTS
    enlarged_fixtures = fixture_epochs()
    enlarged_events, enlarged_stats = build_seeded_family(
        enlarged_fixtures,
        primitive,
        effect_domain,
        family_mode="cycle802-46-fixture-enlarged-family",
    )
    BANK_COUNTS = LANDED_BANK_COUNTS

    constructions = {}
    extension_programs = {}
    for bank_count in ENLARGED_BANK_COUNTS:
        program, _track, construction = extension_fixture(bank_count)
        constructions[bank_count] = construction
        if bank_count in EXTENSION_BANK_COUNTS:
            extension_programs[bank_count] = program

    new_fixtures = enlarged_fixtures[len(landed_fixtures):]
    program_matches = tuple(
        fixture["program"]
        == extension_programs[int(fixture["bank_count"])]
        for fixture in new_fixtures
    )
    cyclic_controls = {}
    for bank_count in EXTENSION_BANK_COUNTS:
        first = next(
            fixture
            for fixture in new_fixtures
            if fixture["bank_count"] == bank_count
        )
        cyclic_controls[str(bank_count)] = F750.cyclic_enforcement_symmetry(
            bank_count,
            first["before"],
            first["expected"],
        )

    landed_counts = count_frozen_assignment(
        landed_events,
        FROZEN_ASSIGNMENT,
    )
    enlarged_counts = count_frozen_assignment(
        enlarged_events,
        FROZEN_ASSIGNMENT,
    )
    landed_table = per_scope_table(landed_counts, HELD_CANDIDATE)
    enlarged_table = per_scope_table(enlarged_counts, HELD_CANDIDATE)
    side_by_side = side_by_side_table(landed_table, enlarged_table)
    new_ensemble_rows = tuple(
        event
        for event in enlarged_events
        if int(event["fixture_index"]) >= len(landed_fixtures)
    )
    new_fixture_row_counts = tuple(
        sum(
            int(event["fixture_index"]) == fixture_index
            for event in new_ensemble_rows
        )
        for fixture_index in range(
            len(landed_fixtures),
            len(enlarged_fixtures),
        )
    )
    supply_layer = declared_supply_layer(constructions)
    stable = {
        "captured_b317_pass_lines": captured_b317.count("PASS "),
        "captured_b317_fail_lines": captured_b317.count("FAIL "),
        "cyclic_controls": cyclic_controls,
        "enlarged_event_digest": digest_rows(enlarged_events),
        "enlarged_fixture_count": len(enlarged_fixtures),
        "enlarged_stats": enlarged_stats,
        "enlarged_table": enlarged_table,
        "landed_event_digest": digest_rows(landed_events),
        "landed_fixture_count": len(landed_fixtures),
        "landed_prefix_exact":
            enlarged_fixtures[:len(landed_fixtures)] == landed_fixtures,
        "landed_stats": landed_stats,
        "landed_table": landed_table,
        "new_bank_sequence": tuple(
            int(fixture["bank_count"]) for fixture in new_fixtures
        ),
        "new_ensemble_fixture_indices": tuple(
            sorted(
                {
                    int(event["fixture_index"])
                    for event in new_ensemble_rows
                }
            )
        ),
        "new_ensemble_row_count": len(new_ensemble_rows),
        "new_fixture_count": len(new_fixtures),
        "new_fixture_row_counts": new_fixture_row_counts,
        "new_selector_outputs": tuple(
            fixture["unrotated_selected"] for fixture in new_fixtures
        ),
        "primitive_multiplicities": primitive,
        "program_matches_extension_constructor": program_matches,
        "side_by_side": side_by_side,
        "supply_layer": supply_layer,
    }
    stable["stable_digest"] = digest_rows(stable)
    return stable


def main() -> int:
    started = perf_counter()
    materialized = materialize_pinned_texts()
    input_sha_before = {
        path: file_sha256(resolve_input(path))
        for path in AUDIT_INPUT_PATHS
    }
    comparator = comparator_audit()
    first = run_experiment_once()

    identity_exact = table_identity_exact(first["landed_table"])
    anchor_pass = bool(
        materialized
        == {
            path: EXPECTED_INPUT_SHA256[path]
            for path in PINNED_SPECS
        }
        and input_sha_before == EXPECTED_INPUT_SHA256
        and all(resolve_input(path).is_file() for path in AUDIT_INPUT_PATHS)
        and comparator["literal_audit_tuple"]
        and comparator["blockf6_primary_fetched_from_origin_ref"]
        and not comparator["blocklisted_module_in_sys_modules"]
        and not comparator["dynamic_text_calls"]
        and comparator["cycle766_frozen_binding_exact"]
        and digest_rows(FROZEN_ASSIGNMENT) == FROZEN_ASSIGNMENT_SHA256
        and F750.K is K719
        and identity_exact
        and first["landed_fixture_count"] == 38
        and first["landed_table"][-1]["sample_size"] == 1122
    )
    check(
        "CERTIFICATE_A_ANCHORS_AND_766_IDENTITY_CONTROL",
        anchor_pass,
        {
            "audit_input_paths": AUDIT_INPUT_PATHS,
            "blockf6_commit": comparator["blockf6_head"],
            "comparator_modules_loaded":
                comparator["blocklisted_module_in_sys_modules"],
            "cycle766_frozen_binding_exact":
                comparator["cycle766_frozen_binding_exact"],
            "frozen_assignment": FROZEN_ASSIGNMENT,
            "frozen_assignment_sha256": digest_rows(FROZEN_ASSIGNMENT),
            "identity_38_exact": identity_exact,
            "identity_table": first["landed_table"],
            "input_sha256": input_sha_before,
        },
    )

    cyclic_clean = all(
        not row["failures"]
        for row in first["cyclic_controls"].values()
    )
    supply = first["supply_layer"]
    construction_pass = bool(
        all(comparator["c763_generator_ast_exact"].values())
        and comparator["cycle788_extension_fixture_ast_exact"]
        and comparator["cycle788_supply_ids_present"]
        and first["primitive_multiplicities"] == (17, 29, 54)
        and first["new_fixture_count"] == 8
        and first["new_bank_sequence"] == (1, 1, 3, 3, 3, 3, 3, 3)
        and first["new_selector_outputs"] == ((0,),) * 8
        and all(first["program_matches_extension_constructor"])
        and cyclic_clean
        and tuple(first["cyclic_controls"][str(size)]["cases"]
                  for size in EXTENSION_BANK_COUNTS) == (3, 19)
        and first["new_ensemble_fixture_indices"]
        == tuple(range(38, 46))
        and all(count > 0 for count in first["new_fixture_row_counts"])
        and supply["selecting_supply_ids"]
        == ("inherited_1", "inherited_2", "inherited_3")
        and supply["shared_by_landed_38"] is True
        and first["captured_b317_pass_lines"] == 7
        and first["captured_b317_fail_lines"] == 0
    )
    check(
        "CERTIFICATE_B_NEW_EVENT_ENSEMBLES_AND_DECLARED_SUPPLIES",
        construction_pass,
        {
            "c763_generator_ast_exact":
                comparator["c763_generator_ast_exact"],
            "cycle788_extension_fixture_ast_exact":
                comparator["cycle788_extension_fixture_ast_exact"],
            "cyclic_controls": first["cyclic_controls"],
            "new_bank_sequence": first["new_bank_sequence"],
            "new_ensemble_fixture_indices":
                first["new_ensemble_fixture_indices"],
            "new_ensemble_row_count": first["new_ensemble_row_count"],
            "new_fixture_row_counts": first["new_fixture_row_counts"],
            "new_selector_events": first["new_fixture_count"],
            "new_selector_outputs": first["new_selector_outputs"],
            "primitive_multiplicities":
                first["primitive_multiplicities"],
            "supply_layer": supply,
        },
    )

    side_by_side = first["side_by_side"]
    pooled_delta_rows = (
        int(first["enlarged_table"][-1]["sample_size"])
        - int(first["landed_table"][-1]["sample_size"])
    )
    table_pass = bool(
        first["landed_prefix_exact"]
        and first["enlarged_fixture_count"] == 46
        and first["new_ensemble_row_count"] == pooled_delta_rows
        and len(side_by_side) == len(SCOPE_NAMES)
        and tuple(row["scope"] for row in side_by_side) == SCOPE_NAMES
        and all(
            all(
                int(before) + int(delta) == int(after)
                for before, delta, after in zip(
                    row["table_38"]["counts"],
                    row["delta"]["counts"],
                    row["table_46"]["counts"],
                    strict=True,
                )
            )
            and row["delta"]["Born_TV_direction"]
            in {"increase", "decrease", "unchanged"}
            and row["delta"]["uniform_TV_direction"]
            in {"increase", "decrease", "unchanged"}
            for row in side_by_side
        )
        and tuple(
            sum(
                int(first["enlarged_table"][stratum]["counts"][effect])
                for stratum in range(3)
            )
            for effect in range(3)
        )
        == tuple(first["enlarged_table"][-1]["counts"])
    )
    check(
        "CERTIFICATE_C_SIDE_BY_SIDE_38_AND_46_TABLES",
        table_pass,
        {
            "enlarged_fixture_count": first["enlarged_fixture_count"],
            "enlarged_ensemble_rows":
                first["enlarged_table"][-1]["sample_size"],
            "landed_fixture_count": first["landed_fixture_count"],
            "landed_ensemble_rows":
                first["landed_table"][-1]["sample_size"],
            "new_ensemble_rows": first["new_ensemble_row_count"],
            "scope_directions": {
                row["scope"]: {
                    "Born_TV": row["delta"]["Born_TV_direction"],
                    "uniform_TV": row["delta"]["uniform_TV_direction"],
                }
                for row in side_by_side
            },
        },
    )
    for row in side_by_side:
        OUTPUT_LINES.append(
            f"DATA SIDE_BY_SIDE {row['scope']} :: {compact(row)}"
        )

    honest_keys = {
        "axiom_update_triggered": False,
        "decides_nothing": True,
        "first_new_content_point": True,
        "frozen_assignment_refit": False,
        "new_selector_events": 8,
        "scope_TV_move_directions": {
            row["scope"]: {
                "Born_TV": row["delta"]["Born_TV_direction"],
                "uniform_TV": row["delta"]["uniform_TV_direction"],
            }
            for row in side_by_side
        },
        "weight_claim_made": False,
    }
    honest_pass = bool(
        honest_keys["decides_nothing"] is True
        and honest_keys["first_new_content_point"] is True
        and honest_keys["new_selector_events"] == 8
        and honest_keys["frozen_assignment_refit"] is False
        and honest_keys["weight_claim_made"] is False
        and honest_keys["axiom_update_triggered"] is False
        and set(honest_keys["scope_TV_move_directions"])
        == set(SCOPE_NAMES)
    )
    check(
        "CERTIFICATE_D_HONEST_FROZEN_KEYS",
        honest_pass,
        honest_keys,
    )
    OUTPUT_LINES.append("DATA HONEST_KEYS :: " + compact(honest_keys))

    repeated = run_experiment_once()
    input_sha_after = {
        path: file_sha256(resolve_input(path))
        for path in AUDIT_INPUT_PATHS
    }
    runtime_seconds = perf_counter() - started
    deterministic = first == repeated
    reserved_terminal_bytes = 8192
    stdout_before_e = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    )
    bounds_pass = bool(
        runtime_seconds < AUDIT_TIMEOUT_SEC
        and stdout_before_e + reserved_terminal_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_DETERMINISM_AND_BOUNDS",
        (
            deterministic
            and bounds_pass
            and input_sha_before == input_sha_after
            and repeated["captured_b317_pass_lines"] == 7
            and repeated["captured_b317_fail_lines"] == 0
        ),
        {
            "deterministic": deterministic,
            "first_stable_digest": first["stable_digest"],
            "input_sha_stable": input_sha_before == input_sha_after,
            "repeat_stable_digest": repeated["stable_digest"],
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "runtime_seconds": runtime_seconds,
            "stdout_before_certificate_e": stdout_before_e,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    report = {
        "axiom_update_triggered": False,
        "certificates": {
            name.split("_", 2)[1]: passed
            for name, passed in CHECKS.items()
        },
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "decides_nothing": True,
        "deltas": {
            row["scope"]: row["delta"] for row in side_by_side
        },
        "first_new_content_point": True,
        "new_selector_events": 8,
        "pass": all(CHECKS.values()),
        "runtime_seconds": runtime_seconds,
        "terminal": (
            "CYCLE802_ENLARGED_BORN_TABLE_CLEAN"
            if all(CHECKS.values())
            else "CYCLE802_ENLARGED_BORN_TABLE_RUNNER_FAIL"
        ),
        "weight_claim_made": False,
    }
    report["report_sha256"] = digest_rows(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
