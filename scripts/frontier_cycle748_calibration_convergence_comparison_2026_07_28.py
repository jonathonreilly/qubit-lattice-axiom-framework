#!/usr/bin/env python3
"""Cycle 748: finite declared-family calibration convergence comparison.

This runner is data-side only.  It passes declared typed test rows through the
Cycle-744 exact-simplex port and compares those simplexes with a separately
frozen fixed-sigma trace candidate on a Cycle-317-derived contact-trine menu.
No row is represented as a realized outcome, and no empirical value is
promoted to a weight or used to select a trace law.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/CALIBRATION_CONVERGENCE_COMPARISON_CYCLE748_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
import json
from math import sqrt
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle744_weight_receiver_sharpening_2026_07_28 as C744
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


PASS = 0
FAIL = 0

M_LADDER = (8, 32, 128, 512)
TOLERANCE_LADDER = (0.06, 0.02, 0.002, 0.001)
MENU_ID = "cycle748-cycle317-contact-trine"
PROGRAM_ID = "cycle748-finite-declared-comparison"
EFFECT_IDS = (
    "cycle317-contact-trine-E0",
    "cycle317-contact-trine-E1",
    "cycle317-contact-trine-E2",
)

# These are supplied candidate values, frozen independently of every declared
# census.  Their exact binary64 spellings are checked against Tr(sigma E) on
# the landed Cycle-317 contact-trine effects, but the census never selects or
# rewrites them.
FROZEN_HELD_CANDIDATE_VALUES = (
    0.36002393478282646,
    0.21194155104147802,
    0.42803451417569555,
)
FROZEN_HELD_CANDIDATE_HEX = (
    "0x1.70aa1d46ad8b4p-2",
    "0x1.b20e697317e2bp-3",
    "0x1.b64eadffc6837p-2",
)
FROZEN_SIGMA_BLOCH = (0.21, -0.32, 0.41)

# One supplied outcome_index per declared test row.  The four comparison
# families are exact prefixes of this declaration; this is data, not output
# from a Cycle-317 trial or from a stochastic generator.
DECLARED_CONVERGING_OUTCOME_SEQUENCE = (
    2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2,
    0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1,
    2, 0, 2, 0, 1, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0,
    1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 2, 1, 2, 0, 1, 2, 0, 2, 0, 2, 1, 0, 2,
    0, 2, 1, 0, 2, 1, 2, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 1, 2, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0,
    2, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1,
    2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0,
    1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2,
    0, 1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0,
    2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1, 2,
    0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0,
    2, 2, 0, 1, 2, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 1, 2, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 1,
    2, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0,
    2, 1, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2,
    0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 0, 2, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0,
    2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 0, 2, 2, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1,
)
DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE = (0,) * 512

FROZEN_EXPECTED_COUNTS = (
    (8, (3, 2, 3)),
    (32, (11, 7, 14)),
    (128, (46, 27, 55)),
    (512, (184, 109, 219)),
)
FROZEN_EXPECTED_RESIDUAL_HEX = (
    (
        8,
        (
            "0x1.eabc572a4e980p-7",
            "0x1.37c65a33a0754p-5",
            "-0x1.b2756ffe341b8p-5",
        ),
        "0x1.b2756ffe341b8p-5",
        "0x1.125251e0b9fb4p-4",
    ),
    (
        32,
        (
            "-0x1.0aa1d46ad8b40p-6",
            "0x1.be32d19d03aa0p-8",
            "0x1.362a40072f920p-7",
        ),
        "0x1.0aa1d46ad8b40p-6",
        "0x1.480104b054664p-6",
    ),
    (
        128,
        (
            "-0x1.543a8d5b16800p-11",
            "-0x1.0734b98bf1580p-10",
            "0x1.b15200397c900p-10",
        ),
        "0x1.b15200397c900p-10",
        "0x1.0b6304367bba7p-9",
    ),
    (
        512,
        (
            "-0x1.543a8d5b16800p-11",
            "0x1.f1968ce81d500p-11",
            "-0x1.3ab7ff1a0dc00p-12",
        ),
        "0x1.f1968ce81d500p-11",
        "0x1.377e32a4a3982p-10",
    ),
)
FROZEN_EXPECTED_DISAGREEMENTS = (
    (8, (0, 2, 3, 3)),
    (32, (0, 0, 3, 3)),
    (128, (0, 0, 0, 2)),
    (512, (0, 0, 0, 0)),
)
FROZEN_CONTROL_RESIDUAL_HEX = (
    "0x1.47aaf15ca93a6p-1",
    "-0x1.b20e697317e2bp-3",
    "-0x1.b64eadffc6837p-2",
)

PROMOTION_BOUNDARY_VERBATIM = (
    "The flow stops being data and becomes a **weight claim** at the first semantic promotion that:",
    "- identifies `f_i` with `w(E_i)`, returns it through a calibration/weight field, or uses it downstream as the effect functional;",
    "- selects the fixed `sigma`, the trace form, or the Born law because declared profiles agree with it;",
    "- calls `_declared_rows` output a derived physical occurrence/Record corpus; or",
    "- turns finite agreement, even exact agreement, into a derivation of a limit law.",
)
TRACK_A_DEPENDENCY = (
    "Track A’s scope resolution of the named `record_outcome_orbit_occupancy` "
    "no-go, followed by a lawful actual-member/occurrence → typed-Record "
    "formation source"
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _landed_contact_trine() -> tuple[tuple[np.ndarray, ...], str]:
    capture = io.StringIO()
    with redirect_stdout(capture):
        fixtures = B317.physical_subcode_controls()
        _kraus, effects = B317.contact_trine_controls(fixtures[3])
    return effects, capture.getvalue()


def _recompute_held_candidate(
    effects: tuple[np.ndarray, ...],
) -> tuple[float, ...]:
    bloch = np.asarray(FROZEN_SIGMA_BLOCH, dtype=float)
    sigma = (
        B317.I2
        + bloch[0] * B317.X
        + bloch[1] * B317.Y
        + bloch[2] * B317.Z
    ) / 2
    return tuple(float(np.trace(sigma @ effect).real) for effect in effects)


def anchor_certificate(
    effects: tuple[np.ndarray, ...],
    captured_b317_checks: str,
    input_sha_before: dict[str, str],
) -> dict:
    metrics = B317.menu_metrics(effects)
    imported_paths = {
        "cycle744": str(Path(C744.__file__).resolve().relative_to(ROOT)),
        "cycle317": str(Path(B317.__file__).resolve().relative_to(ROOT)),
    }
    port_api = {
        name: callable(getattr(C744, name, None))
        for name in (
            "receive_occurrence_records",
            "compare_empirical_to_landed",
        )
    }
    schema_api = {
        name: getattr(C744, name, None) is not None
        for name in (
            "MenuProgramIdentity",
            "RecordRow",
            "ExposureDeclaration",
            "EffectIdentityMetadata",
            "EmpiricalPortResult",
            "ComparatorRow",
        )
    }
    recomputed = _recompute_held_candidate(effects)
    detail = {
        "apparatus_call_chain": (
            "B317.physical_subcode_controls",
            "B317.contact_trine_controls(fixtures[3])",
            "B317.derived_effects",
        ),
        "apparatus_execution_is_one_trial": False,
        "captured_b317_pass_lines": captured_b317_checks.count("PASS "),
        "effect_count": len(effects),
        "effect_origin": "landed_cycle317_derived_effects",
        "held_candidate_hex": tuple(value.hex() for value in recomputed),
        "imported_paths": imported_paths,
        "menu_metrics": metrics,
        "per_run_outcome_callable": None,
        "port_api": port_api,
        "schema_api": schema_api,
    }
    condition = (
        tuple(imported_paths.values()) == AUDIT_INPUT_PATHS
        and all(port_api.values())
        and all(schema_api.values())
        and len(effects) == len(EFFECT_IDS) == 3
        and metrics["normalization"] < B317.TOL
        and metrics["minimum_eigenvalue"] > -B317.TOL
        and tuple(value.hex() for value in recomputed)
        == FROZEN_HELD_CANDIDATE_HEX
        and tuple(value.hex() for value in FROZEN_HELD_CANDIDATE_VALUES)
        == FROZEN_HELD_CANDIDATE_HEX
        and captured_b317_checks.count("PASS ") == 4
        and "FAIL " not in captured_b317_checks
        and input_sha_before
        == {relative: _sha256(ROOT / relative) for relative in AUDIT_INPUT_PATHS}
    )
    check("A anchors: Cycle-744 port and Cycle-317 contact-trine menu are frozen", condition, detail)
    return detail


def _declared_master_rows(
    family_name: str,
    outcome_sequence: tuple[int, ...],
) -> tuple[C744.RecordRow, ...]:
    exposure_id = f"cycle748-{family_name}-nested-exposure"
    return tuple(
        C744.RecordRow(
            record_id=f"cycle748-{family_name}-r{index:04d}",
            menu_id=MENU_ID,
            program_id=PROGRAM_ID,
            outcome_index=outcome_index,
            effect_id=EFFECT_IDS[outcome_index],
            exposure_id=exposure_id,
            record_kind="declared_apparatus_test_row",
            provenance=f"cycle748-declared-family:{family_name}",
        )
        for index, outcome_index in enumerate(outcome_sequence)
    )


def _receive_family(
    family_name: str,
    master_rows: tuple[C744.RecordRow, ...],
) -> dict[int, C744.EmpiricalPortResult]:
    identity = C744.MenuProgramIdentity(MENU_ID, PROGRAM_ID)
    metadata = C744.EffectIdentityMetadata(
        coarse_grainings=(
            ("all", (0, 1, 2)),
            ("first-two", (0, 1)),
            ("third", (2,)),
        ),
        same_effect_classes=tuple((effect_id,) for effect_id in EFFECT_IDS),
    )
    received = {}
    for size in M_LADDER:
        exposure = C744.ExposureDeclaration(
            exposure_id=f"cycle748-{family_name}-nested-exposure",
            menu_id=MENU_ID,
            program_id=PROGRAM_ID,
            trial_total=size,
            per_effect_eligible_trials=(size,) * len(EFFECT_IDS),
            sampling_protocol="complete-exclusive-common-exposure",
            provenance=f"cycle748-declared-exposure:{family_name}",
        )
        received[size] = C744.receive_occurrence_records(
            identity,
            EFFECT_IDS,
            master_rows[:size],
            exposure,
            metadata,
        )
    return received


def family_construction_certificate(
    converging_rows: tuple[C744.RecordRow, ...],
    control_rows: tuple[C744.RecordRow, ...],
) -> dict:
    families = {
        "declared-convergence": converging_rows,
        "declared-miscalibrated-control": control_rows,
    }
    nested_checks = {
        name: all(
            rows[:smaller] == rows[:larger][:smaller]
            for smaller, larger in zip(
                M_LADDER[:-1], M_LADDER[1:], strict=True
            )
        )
        for name, rows in families.items()
    }
    detail = {
        "M_sequence": M_LADDER,
        "family_lengths": {name: len(rows) for name, rows in families.items()},
        "nested_exact_prefixes": nested_checks,
        "record_kind": "declared_apparatus_test_row",
        "run_family_origin": "declared_not_occurrence_derived",
        "typed_rows": {
            name: all(type(row) is C744.RecordRow for row in rows)
            for name, rows in families.items()
        },
        "unique_record_ids": {
            name: len({row.record_id for row in rows}) == len(rows)
            for name, rows in families.items()
        },
    }
    condition = (
        len(DECLARED_CONVERGING_OUTCOME_SEQUENCE) == M_LADDER[-1]
        and len(DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE) == M_LADDER[-1]
        and set(DECLARED_CONVERGING_OUTCOME_SEQUENCE) <= {0, 1, 2}
        and set(DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE) == {0}
        and all(nested_checks.values())
        and all(detail["typed_rows"].values())
        and all(detail["unique_record_ids"].values())
        and all(
            row.record_kind == "declared_apparatus_test_row"
            and row.menu_id == MENU_ID
            and row.program_id == PROGRAM_ID
            and row.effect_id == EFFECT_IDS[row.outcome_index]
            and bool(row.provenance)
            for rows in families.values()
            for row in rows
        )
    )
    check("B family construction: nested typed declared-row families are exact", condition, detail)
    return detail


def simplex_certificate(
    converging: dict[int, C744.EmpiricalPortResult],
    control: dict[int, C744.EmpiricalPortResult],
) -> dict:
    families = {
        "declared-convergence": converging,
        "declared-miscalibrated-control": control,
    }
    detail = {
        family: {
            str(size): {
                "coarse_counts": result.coarse_counts,
                "counts": result.counts,
                "simplex": tuple(str(value) for value in result.simplex),
                "simplex_sum": str(
                    sum(result.simplex, start=Fraction(0, 1))
                ),
            }
            for size, result in results.items()
        }
        for family, results in families.items()
    }
    condition = (
        tuple((size, result.counts) for size, result in converging.items())
        == FROZEN_EXPECTED_COUNTS
        and all(
            result.counts == (size, 0, 0)
            for size, result in control.items()
        )
        and all(
            sum(result.counts) == size
            and all(type(value) is Fraction for value in result.simplex)
            and sum(result.simplex, start=Fraction(0, 1)) == Fraction(1, 1)
            and dict(result.coarse_counts)["all"] == size
            and dict(result.coarse_counts)["first-two"]
            == result.counts[0] + result.counts[1]
            and result.same_effect_classes
            == tuple((effect_id,) for effect_id in EFFECT_IDS)
            for results in families.values()
            for size, result in results.items()
        )
    )
    check("C simplex exactness: every declared family has an exact Fraction simplex", condition, detail)
    return detail


def _comparison_table(
    empirical_by_size: dict[int, C744.EmpiricalPortResult],
) -> tuple[dict, ...]:
    table = []
    for size, empirical in empirical_by_size.items():
        comparator_rows = {
            tolerance: C744.compare_empirical_to_landed(
                empirical,
                FROZEN_HELD_CANDIDATE_VALUES,
                tolerance=tolerance,
            )
            for tolerance in TOLERANCE_LADDER
        }
        residuals = tuple(
            row.residual for row in comparator_rows[TOLERANCE_LADDER[0]]
        )
        comparisons = tuple(
            {
                "aggregate": (
                    "agreement"
                    if all(row.verdict == "agreement" for row in rows)
                    else "disagreement"
                ),
                "disagreement_count": sum(
                    row.verdict == "disagreement" for row in rows
                ),
                "effect_verdicts": tuple(row.verdict for row in rows),
                "tolerance": tolerance,
            }
            for tolerance, rows in comparator_rows.items()
        )
        table.append(
            {
                "M": size,
                "comparisons": comparisons,
                "counts": empirical.counts,
                "residual_hex": tuple(value.hex() for value in residuals),
                "residual_l2_hex": sqrt(
                    sum(value * value for value in residuals)
                ).hex(),
                "residual_max_abs_hex": max(
                    abs(value) for value in residuals
                ).hex(),
                "simplex_exact": tuple(
                    str(value) for value in empirical.simplex
                ),
            }
        )
    return tuple(table)


def comparison_table_certificate(
    table: tuple[dict, ...],
) -> dict:
    residual_freeze = tuple(
        (
            row["M"],
            row["residual_hex"],
            row["residual_max_abs_hex"],
            row["residual_l2_hex"],
        )
        for row in table
    )
    disagreement_freeze = tuple(
        (
            row["M"],
            tuple(
                comparison["disagreement_count"]
                for comparison in row["comparisons"]
            ),
        )
        for row in table
    )
    by_tolerance = {
        str(tolerance): tuple(
            row["comparisons"][tolerance_index]["disagreement_count"]
            for row in table
        )
        for tolerance_index, tolerance in enumerate(TOLERANCE_LADDER)
    }
    observed_monotonicity = {
        tolerance: all(
            left >= right
            for left, right in zip(counts[:-1], counts[1:], strict=True)
        )
        for tolerance, counts in by_tolerance.items()
    }
    max_residuals = tuple(
        float.fromhex(row["residual_max_abs_hex"]) for row in table
    )
    canonical_table = json.dumps(
        table, sort_keys=True, separators=(",", ":")
    )
    detail = {
        "comparison_kind": "finite_declared_census_vs_held_trace_candidate",
        "convergence_table": table,
        "held_candidate_origin": "fixed_sigma_trace_candidate",
        "held_candidate_values": FROZEN_HELD_CANDIDATE_VALUES,
        "observed_disagreement_counts_by_tolerance": by_tolerance,
        "observed_monotonicity_not_law": observed_monotonicity,
        "table_sha256": hashlib.sha256(canonical_table.encode()).hexdigest(),
        "tolerance_ladder": TOLERANCE_LADDER,
    }
    condition = (
        residual_freeze == FROZEN_EXPECTED_RESIDUAL_HEX
        and disagreement_freeze == FROZEN_EXPECTED_DISAGREEMENTS
        and all(observed_monotonicity.values())
        and all(
            left > right
            for left, right in zip(
                max_residuals[:-1], max_residuals[1:], strict=True
            )
        )
        and all(
            comparison["aggregate"] in {"agreement", "disagreement"}
            for row in table
            for comparison in row["comparisons"]
        )
    )
    check("D comparison table: frozen finite DATA reruns with zero drift", condition, detail)
    print("DATA tolerance_ladder", json.dumps(TOLERANCE_LADDER))
    print("DATA convergence_table", canonical_table)
    return detail


def control_certificate(control_table: tuple[dict, ...]) -> dict:
    residual_rows = tuple(row["residual_hex"] for row in control_table)
    disagreement_rows = tuple(
        tuple(
            comparison["disagreement_count"]
            for comparison in row["comparisons"]
        )
        for row in control_table
    )
    residual_norms = tuple(
        float.fromhex(row["residual_l2_hex"]) for row in control_table
    )
    detail = {
        "control": "deliberately_miscalibrated_all_rows_in_slot_0",
        "control_diverges_detected": True,
        "finite_ladder_definition": (
            "every declared tolerance comparison disagrees and the residual "
            "norm does not decrease over the finite M ladder"
        ),
        "not_an_asymptotic_claim": True,
        "residual_hex_by_M": residual_rows,
        "tolerance_disagreement_counts_by_M": disagreement_rows,
    }
    condition = (
        all(row == FROZEN_CONTROL_RESIDUAL_HEX for row in residual_rows)
        and all(
            all(count > 0 for count in disagreement_counts)
            for disagreement_counts in disagreement_rows
        )
        and all(
            left <= right
            for left, right in zip(
                residual_norms[:-1], residual_norms[1:], strict=True
            )
        )
        and residual_norms[-1] > 0.7
    )
    check("E miscalibrated control: finite divergence from the held candidate is detected", condition, detail)
    return detail


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    targets = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
    return tuple(targets)


def firewall_certificate() -> dict:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    imported_attribute_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in {"C744", "B317"}
    )
    imported_setattrs = tuple(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id in {"C744", "B317"}
    )
    forbidden_promotion_targets = tuple(
        sorted(
            {
                node.id
                for target in _assignment_targets(tree)
                for node in ast.walk(target)
                if isinstance(node, ast.Name)
                and isinstance(node.ctx, ast.Store)
                and (
                    node.id.lower() == "weight"
                    or node.id.lower().endswith("_weight")
                    or "calibrated_weight" in node.id.lower()
                )
            }
        )
    )
    data_function_names = (
        "_declared_master_rows",
        "_receive_family",
        "family_construction_certificate",
        "simplex_certificate",
    )
    candidate_function_names = ("_recompute_held_candidate",)
    data_to_candidate_hits = tuple(
        sorted(
            {
                node.id
                for name in data_function_names
                for node in ast.walk(functions[name])
                if isinstance(node, ast.Name)
                and node.id
                in {
                    "FROZEN_HELD_CANDIDATE_VALUES",
                    "FROZEN_SIGMA_BLOCH",
                    "_recompute_held_candidate",
                }
            }
        )
    )
    candidate_to_data_hits = tuple(
        sorted(
            {
                node.id
                for name in candidate_function_names
                for node in ast.walk(functions[name])
                if isinstance(node, ast.Name)
                and node.id
                in {
                    "DECLARED_CONVERGING_OUTCOME_SEQUENCE",
                    "DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE",
                    "_declared_master_rows",
                    "_receive_family",
                }
            }
        )
    )
    selection_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(functions["_recompute_held_candidate"])
        if isinstance(node, ast.Call)
        and ast.unparse(node.func)
        in {"min", "max", "sorted", "np.argmin", "np.argmax"}
    )
    deliverable_name = Path(__file__).name
    reverse_dependency_hits = {
        relative: (
            deliverable_name
            in (ROOT / relative).read_text(encoding="utf-8")
        )
        for relative in AUDIT_INPUT_PATHS
    }
    file_write_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"write_text", "write_bytes", "unlink", "rename"}
    )
    detail = {
        "candidate_to_declared_data_ast_hits": candidate_to_data_hits,
        "data_to_candidate_ast_hits": data_to_candidate_hits,
        "empirical_to_weight_assignment_targets": forbidden_promotion_targets,
        "file_write_calls": file_write_calls,
        "imported_module_attribute_writes": imported_attribute_writes,
        "imported_module_setattr_calls": imported_setattrs,
        "reverse_input_dependency_hits": reverse_dependency_hits,
        "trace_candidate_selection_calls": selection_calls,
    }
    condition = (
        not imported_attribute_writes
        and not imported_setattrs
        and not forbidden_promotion_targets
        and not data_to_candidate_hits
        and not candidate_to_data_hits
        and not selection_calls
        and not any(reverse_dependency_hits.values())
        and not file_write_calls
    )
    check("F firewall audits: AST is clean in both data/candidate directions and writes neither input", condition, detail)
    return detail


def honest_boundary() -> dict:
    return {
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "comparison_only": True,
        "promotion_boundary_verbatim": PROMOTION_BOUNDARY_VERBATIM,
        "simplex_promoted_to_weight": False,
        "supplies": {
            "apparatus_surface": "cycle317",
            "calibration_map": False,
            "declared_typed_test_rows": True,
            "effect_origin": "landed_cycle317_derived_effects",
            "exposure_sampling_provenance": True,
            "frozen_fixed_sigma_trace_candidate": True,
            "occurrence_generator": False,
            "per_run_outcome_callable": None,
            "run_family_origin": "declared_not_occurrence_derived",
            "selected_occurrence_law": False,
        },
        "track_a_dependency": TRACK_A_DEPENDENCY,
        "track_a_dependency_recorded": True,
        "w6_closed": False,
        "weight_claim_made": False,
    }


def boundary_certificate() -> dict:
    boundary = honest_boundary()
    condition = (
        boundary["comparison_only"] is True
        and boundary["weight_claim_made"] is False
        and boundary["born_law_selected"] is False
        and boundary["track_a_dependency_recorded"] is True
        and boundary["track_a_dependency"] == TRACK_A_DEPENDENCY
        and boundary["promotion_boundary_verbatim"]
        == PROMOTION_BOUNDARY_VERBATIM
        and boundary["simplex_promoted_to_weight"] is False
        and boundary["asymptotic_convergence_claimed"] is False
        and boundary["supplies"]["calibration_map"] is False
        and boundary["supplies"]["occurrence_generator"] is False
        and boundary["supplies"]["selected_occurrence_law"] is False
    )
    check("G honest boundary: comparison-only, no weight/Born-law claim, Track A recorded", condition, boundary)
    return boundary


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()

    input_sha_before = {
        relative: _sha256(ROOT / relative) for relative in AUDIT_INPUT_PATHS
    }
    effects, captured_b317_checks = _landed_contact_trine()
    anchors = anchor_certificate(
        effects, captured_b317_checks, input_sha_before
    )

    converging_rows = _declared_master_rows(
        "convergence", DECLARED_CONVERGING_OUTCOME_SEQUENCE
    )
    control_rows = _declared_master_rows(
        "miscalibrated-control", DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE
    )
    family_construction = family_construction_certificate(
        converging_rows, control_rows
    )

    converging = _receive_family("convergence", converging_rows)
    control = _receive_family("miscalibrated-control", control_rows)
    simplex = simplex_certificate(converging, control)

    convergence_table = _comparison_table(converging)
    comparison = comparison_table_certificate(convergence_table)
    control_result = control_certificate(_comparison_table(control))
    firewall = firewall_certificate()
    boundary = boundary_certificate()

    input_sha_after = {
        relative: _sha256(ROOT / relative) for relative in AUDIT_INPUT_PATHS
    }
    check(
        "A anchors remain byte-stable after the comparison",
        input_sha_before == input_sha_after,
        input_sha_after,
    )

    runtime_sec = perf_counter() - started
    certificate = {
        "anchors": anchors,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "boundary": boundary,
        "comparison": comparison,
        "control": control_result,
        "declared_input_paths": DECLARED_INPUT_PATHS,
        "family_construction": family_construction,
        "fail": FAIL,
        "input_sha256": input_sha_after,
        "note_path": NOTE_PATH,
        "pass": PASS,
        "result": "PASS" if FAIL == 0 else "FAIL",
        "runtime_sec": runtime_sec,
        "simplex": simplex,
    }
    print(json.dumps(certificate, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
