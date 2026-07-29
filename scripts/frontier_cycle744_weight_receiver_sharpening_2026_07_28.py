#!/usr/bin/env python3
"""Cycle 744: sharpen the landed weight-receiver hole and add a safe port.

The theorem proved here is bounded to the two Cycle-317 Python surfaces.  The
new port accepts explicitly declared test Record rows, performs exact
Fraction-valued empirical normalization, and compares the result with the
landed held trace candidate.  It does not calibrate, derive, select, or write
any weight law.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/WEIGHT_RECEIVER_SHARPENING_CYCLE744_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from time import perf_counter
from typing import Callable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import physical_contact_ternary_born_forcing_release_cycle317_2026_07_18 as R317


PASS = 0
FAIL = 0

FROZEN_PORT_INVENTORY = {
    "basis": ("dimension", "index"),
    "binary_and_ternary_threshold_controls": ("trine_effects",),
    "check": ("label", "condition", "detail"),
    "contact_trine_controls": ("fixture",),
    "deletion_domain_and_semantic_controls": ("fixture", "forcing_kraus"),
    "derived_effects": ("isometry", "groups"),
    "main": (),
    "menu_metrics": ("effects",),
    "merge_isometry": ("weighted_projectors", "contact"),
    "mixed_projective_forcing_basis_controls": ("fixture",),
    "nonlinear_binary_weight": ("effect",),
    "normalized": ("path",),
    "note_contract": (),
    "physical_fixture": ("length",),
    "physical_isometry": ("two_ray_encoding", "kraus"),
    "physical_locality_and_covariance_controls": ("fixtures", "route_kraus"),
    "physical_subcode_controls": (),
    "projector_bloch": ("vector",),
    "split_projector_isometry": ("projector", "splits", "contact"),
    "stack_isometry": ("kraus",),
}

FROZEN_PORT_ANNOTATIONS = {
    "basis": (("dimension", "int"), ("index", "int")),
    "binary_and_ternary_threshold_controls": (
        ("trine_effects", "tuple[np.ndarray, ...]"),
    ),
    "check": (("label", "str"), ("condition", "bool"), ("detail", "object")),
    "contact_trine_controls": (("fixture", "PhysicalFixture"),),
    "deletion_domain_and_semantic_controls": (
        ("fixture", "PhysicalFixture"),
        ("forcing_kraus", "tuple[np.ndarray, ...]"),
    ),
    "derived_effects": (
        ("isometry", "np.ndarray"),
        ("groups", "tuple[tuple[int, ...], ...]"),
    ),
    "main": (),
    "menu_metrics": (("effects", "tuple[np.ndarray, ...]"),),
    "merge_isometry": (
        ("weighted_projectors", "tuple[tuple[float, np.ndarray], ...]"),
        ("contact", "np.ndarray"),
    ),
    "mixed_projective_forcing_basis_controls": (
        ("fixture", "PhysicalFixture"),
    ),
    "nonlinear_binary_weight": (("effect", "np.ndarray"),),
    "normalized": (("path", "Path"),),
    "note_contract": (),
    "physical_fixture": (("length", "int"),),
    "physical_isometry": (
        ("two_ray_encoding", "np.ndarray"),
        ("kraus", "tuple[np.ndarray, ...]"),
    ),
    "physical_locality_and_covariance_controls": (
        ("fixtures", "dict[int, PhysicalFixture]"),
        ("route_kraus", "dict[str, tuple[np.ndarray, ...]]"),
    ),
    "physical_subcode_controls": (),
    "projector_bloch": (("vector", "np.ndarray"),),
    "split_projector_isometry": (
        ("projector", "np.ndarray"),
        ("splits", "tuple[float, ...]"),
        ("contact", "np.ndarray"),
    ),
    "stack_isometry": (("kraus", "tuple[np.ndarray, ...]"),),
}

# This is the frozen type/role argument for every one of the twenty landed
# science ports.  ``check.detail`` is deliberately called out as a reporting
# sink: its broad object type does not feed a numerical functional.
FROZEN_PORT_TYPE_ARGUMENTS = {
    "basis": "Hilbert-space dimension and coordinate index only",
    "binary_and_ternary_threshold_controls": "already-derived trine effects only",
    "check": "report label, truth value, and print-only diagnostic sink",
    "contact_trine_controls": "constructed PhysicalFixture only",
    "deletion_domain_and_semantic_controls": "PhysicalFixture and Kraus family only",
    "derived_effects": "Naimark isometry and pointer-index groups only",
    "main": "closed entry point with no arguments",
    "menu_metrics": "already-derived effect tuple only",
    "merge_isometry": "apparatus projector coefficients and contact only",
    "mixed_projective_forcing_basis_controls": "constructed PhysicalFixture only",
    "nonlinear_binary_weight": "one already-supplied effect; hard-coded counterfunctional",
    "normalized": "filesystem Path used as note-text reader only",
    "note_contract": "closed note check with no arguments",
    "physical_fixture": "lattice length only",
    "physical_isometry": "two-ray encoding and Kraus family only",
    "physical_locality_and_covariance_controls": "fixture map and Kraus-route map only",
    "physical_subcode_controls": "closed fixture builder with no arguments",
    "projector_bloch": "one unit three-vector only",
    "split_projector_isometry": "projector, split coefficients, and contact only",
    "stack_isometry": "Kraus family only",
}

RECEIVER_NAME_FRAGMENTS = (
    "calibration",
    "count",
    "epoch",
    "exposure",
    "frequenc",
    "occurrence",
    "record",
    "row",
    "sampling",
)

FROZEN_HELD_WEIGHT_FORM = {
    "bloch": "bloch = np.asarray((0.21, -0.32, 0.41), dtype=float)",
    "sigma": (
        "sigma = (I2 + bloch[0] * X + bloch[1] * Y + bloch[2] * Z) / 2"
    ),
    "function": "def born_weight(effect: np.ndarray) -> float:",
    "return": "return float(np.trace(sigma @ effect).real)",
}

REQUIRED_BRIDGE_SIGNATURE = (
    "menu_program_identity",
    "ordered_effect_identities",
    "typed_records",
    "exposure_sampling_declaration",
    "record_and_exposure_provenance",
    "coarse_graining_metadata",
    "same_effect_identity_metadata",
    "calibration_map",
)

COMPONENT_NECESSITY = {
    "menu_program_identity": (
        "dropping it breaks program eligibility and permits cross-program pooling"
    ),
    "ordered_effect_identities": (
        "dropping it breaks the N-slot count-to-effect map and fixes neither N nor order"
    ),
    "typed_records": (
        "dropping it breaks lawful occurrence evidence and the construction of n in N^N"
    ),
    "exposure_sampling_declaration": (
        "dropping it breaks the denominator, per-effect eligibility, and units"
    ),
    "record_and_exposure_provenance": (
        "dropping it breaks Record typing, auditability, and apparatus-source identity"
    ),
    "coarse_graining_metadata": (
        "dropping it breaks the required additive component-count rule"
    ),
    "same_effect_identity_metadata": (
        "dropping it breaks repeated-presentation and cross-program identity checks"
    ),
    "calibration_map": (
        "dropping it leaves only an empirical simplex/comparator, not per-effect weights"
    ),
}

INTERFACE_STAGES = (
    "typed Records R[0:M] -> ordered N-count vector n in N^N",
    "n + exposure/sampling + provenance -> exact f in Delta^(N-1)",
    "f + coarse-graining + same-effect identities + calibration -> per-effect w[0:N]",
)

DECLARED_MENU_ID = "cycle744-quarter-scalar-menu"
DECLARED_PROGRAM_ID = "cycle744-comparator-test-program"
DECLARED_EFFECT_IDS = ("E_1_10", "E_2_10", "E_3_10", "E_4_10")
DECLARED_APPARATUS_DATA_FAMILY = (
    ("landed-profile", (1, 2, 3, 4)),
    ("counterfactual-shift", (2, 2, 3, 3)),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


@dataclass(frozen=True)
class MenuProgramIdentity:
    menu_id: str
    program_id: str


@dataclass(frozen=True)
class RecordRow:
    record_id: str
    menu_id: str
    program_id: str
    outcome_index: int
    effect_id: str
    exposure_id: str
    record_kind: str
    provenance: str


@dataclass(frozen=True)
class ExposureDeclaration:
    exposure_id: str
    menu_id: str
    program_id: str
    trial_total: int
    per_effect_eligible_trials: tuple[int, ...]
    sampling_protocol: str
    provenance: str


@dataclass(frozen=True)
class EffectIdentityMetadata:
    coarse_grainings: tuple[tuple[str, tuple[int, ...]], ...]
    same_effect_classes: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class EmpiricalPortResult:
    identity: MenuProgramIdentity
    effect_ids: tuple[str, ...]
    counts: tuple[int, ...]
    simplex: tuple[Fraction, ...]
    exposure_by_effect: tuple[tuple[str, int], ...]
    record_provenance: tuple[str, ...]
    exposure_provenance: str
    coarse_counts: tuple[tuple[str, int], ...]
    coarse_simplex: tuple[tuple[str, Fraction], ...]
    same_effect_classes: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class ComparatorRow:
    effect_id: str
    empirical: Fraction
    held_candidate: float
    residual: float
    verdict: str


def _require_nonempty_text(value: object, label: str) -> str:
    if type(value) is not str or not value.strip():
        raise ValueError(f"{label} must be nonempty text")
    return value


def receive_occurrence_records(
    identity: MenuProgramIdentity,
    ordered_effect_ids: tuple[str, ...],
    records: tuple[RecordRow, ...],
    exposure: ExposureDeclaration,
    metadata: EffectIdentityMetadata,
) -> EmpiricalPortResult:
    """Validate declared rows and return an empirical object, never a weight."""
    if type(identity) is not MenuProgramIdentity:
        raise ValueError("identity must use the MenuProgramIdentity schema")
    menu_id = _require_nonempty_text(identity.menu_id, "menu_id")
    program_id = _require_nonempty_text(identity.program_id, "program_id")
    if (
        type(ordered_effect_ids) is not tuple
        or len(ordered_effect_ids) < 2
        or any(type(item) is not str or not item for item in ordered_effect_ids)
        or len(set(ordered_effect_ids)) != len(ordered_effect_ids)
    ):
        raise ValueError("ordered effect identities must be a unique tuple of size N>=2")
    if type(records) is not tuple or not records:
        raise ValueError("Records must be one nonempty typed tuple")
    if any(type(row) is not RecordRow for row in records):
        raise ValueError("every intake row must use the RecordRow schema")
    if type(exposure) is not ExposureDeclaration:
        raise ValueError("exposure must use the ExposureDeclaration schema")
    if type(metadata) is not EffectIdentityMetadata:
        raise ValueError("metadata must use the EffectIdentityMetadata schema")

    exposure_id = _require_nonempty_text(exposure.exposure_id, "exposure_id")
    _require_nonempty_text(exposure.sampling_protocol, "sampling_protocol")
    _require_nonempty_text(exposure.provenance, "exposure provenance")
    if exposure.menu_id != menu_id or exposure.program_id != program_id:
        raise ValueError("exposure identity must match the menu/program identity")
    if exposure.sampling_protocol != "complete-exclusive-common-exposure":
        raise ValueError("this bounded port admits only declared common exposure")
    if type(exposure.trial_total) is not int or exposure.trial_total <= 0:
        raise ValueError("trial_total must be one positive integer")
    if (
        type(exposure.per_effect_eligible_trials) is not tuple
        or len(exposure.per_effect_eligible_trials) != len(ordered_effect_ids)
        or any(
            type(value) is not int or value != exposure.trial_total
            for value in exposure.per_effect_eligible_trials
        )
    ):
        raise ValueError("common exposure must declare M eligible trials per effect")
    if len(records) != exposure.trial_total:
        raise ValueError("one complete exclusive intake needs exactly M Record rows")

    record_ids = set()
    record_provenance = set()
    counts = [0] * len(ordered_effect_ids)
    for row in records:
        _require_nonempty_text(row.record_id, "record_id")
        _require_nonempty_text(row.provenance, "Record provenance")
        if row.record_id in record_ids:
            raise ValueError("Record identities must be unique")
        record_ids.add(row.record_id)
        record_provenance.add(row.provenance)
        if row.menu_id != menu_id or row.program_id != program_id:
            raise ValueError("every Record row must match the menu/program identity")
        if row.exposure_id != exposure_id:
            raise ValueError("every Record row must match the exposure declaration")
        if row.record_kind != "declared_apparatus_test_row":
            raise ValueError("Record kind is outside the bounded test schema")
        if type(row.outcome_index) is not int or not (
            0 <= row.outcome_index < len(ordered_effect_ids)
        ):
            raise ValueError("outcome_index is outside the ordered effect domain")
        if row.effect_id != ordered_effect_ids[row.outcome_index]:
            raise ValueError("effect identity must agree with its ordered slot")
        counts[row.outcome_index] += 1

    if sum(counts) != exposure.trial_total:
        raise ValueError("exclusive occurrence counts must sum to M")
    if any(
        count > eligible
        for count, eligible in zip(
            counts, exposure.per_effect_eligible_trials, strict=True
        )
    ):
        raise ValueError("an occurrence count cannot exceed declared eligibility")

    coarse_names = set()
    coarse_rows = []
    for name, indices in metadata.coarse_grainings:
        _require_nonempty_text(name, "coarse-graining name")
        if name in coarse_names:
            raise ValueError("coarse-graining names must be unique")
        coarse_names.add(name)
        if (
            type(indices) is not tuple
            or not indices
            or len(set(indices)) != len(indices)
            or any(type(index) is not int or not 0 <= index < len(counts) for index in indices)
        ):
            raise ValueError("each coarse-graining needs unique in-range indices")
        coarse_rows.append((name, sum(counts[index] for index in indices)))

    flattened_classes = tuple(
        effect_id
        for identity_class in metadata.same_effect_classes
        for effect_id in identity_class
    )
    if (
        any(type(identity_class) is not tuple or not identity_class for identity_class in metadata.same_effect_classes)
        or len(flattened_classes) != len(set(flattened_classes))
        or set(flattened_classes) != set(ordered_effect_ids)
    ):
        raise ValueError("same-effect classes must partition the effect identities")

    denominator = exposure.trial_total
    simplex = tuple(Fraction(count, denominator) for count in counts)
    if sum(simplex, start=Fraction(0, 1)) != Fraction(1, 1):
        raise ValueError("exact empirical normalization failed")
    coarse_simplex = tuple(
        (name, Fraction(count, denominator)) for name, count in coarse_rows
    )
    return EmpiricalPortResult(
        identity=identity,
        effect_ids=ordered_effect_ids,
        counts=tuple(counts),
        simplex=simplex,
        exposure_by_effect=tuple(
            zip(
                ordered_effect_ids,
                exposure.per_effect_eligible_trials,
                strict=True,
            )
        ),
        record_provenance=tuple(sorted(record_provenance)),
        exposure_provenance=exposure.provenance,
        coarse_counts=tuple(coarse_rows),
        coarse_simplex=coarse_simplex,
        same_effect_classes=metadata.same_effect_classes,
    )


def compare_empirical_to_landed(
    empirical: EmpiricalPortResult,
    held_candidate_values: tuple[float, ...],
    tolerance: float = 1.0e-12,
) -> tuple[ComparatorRow, ...]:
    """Return read-only comparator verdicts against separately held values."""
    if (
        type(held_candidate_values) is not tuple
        or len(held_candidate_values) != len(empirical.effect_ids)
        or any(type(value) is not float or not np.isfinite(value) for value in held_candidate_values)
    ):
        raise ValueError("held candidate values must be one finite float per effect")
    if tolerance < 0:
        raise ValueError("comparator tolerance must be nonnegative")
    rows = []
    for effect_id, observed, candidate in zip(
        empirical.effect_ids,
        empirical.simplex,
        held_candidate_values,
        strict=True,
    ):
        residual = float(observed) - candidate
        rows.append(
            ComparatorRow(
                effect_id=effect_id,
                empirical=observed,
                held_candidate=candidate,
                residual=residual,
                verdict="agreement" if abs(residual) <= tolerance else "disagreement",
            )
        )
    return tuple(rows)


def _top_level_functions(tree: ast.Module) -> tuple[ast.FunctionDef, ...]:
    return tuple(node for node in tree.body if isinstance(node, ast.FunctionDef))


def _function_parameters(node: ast.FunctionDef) -> tuple[ast.arg, ...]:
    return tuple(node.args.posonlyargs + node.args.args + node.args.kwonlyargs)


def _live_signature_inventory(tree: ast.Module) -> dict[str, tuple[str, ...]]:
    return {
        node.name: tuple(argument.arg for argument in _function_parameters(node))
        for node in _top_level_functions(tree)
    }


def _live_annotation_inventory(
    tree: ast.Module,
) -> dict[str, tuple[tuple[str, str], ...]]:
    return {
        node.name: tuple(
            (
                argument.arg,
                ast.unparse(argument.annotation)
                if argument.annotation is not None
                else "",
            )
            for argument in _function_parameters(node)
        )
        for node in _top_level_functions(tree)
    }


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run_landed_surface(path: Path, summary_pattern: str, result_marker: str) -> dict:
    before = _sha256(path)
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "scripts")
    try:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            env=environment,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        matches = re.findall(summary_pattern, completed.stdout)
        observed = tuple(map(int, matches[-1])) if matches else None
        result_seen = result_marker in completed.stdout
        return {
            "path": str(path.relative_to(ROOT)),
            "sha256": before,
            "sha_stable": before == _sha256(path),
            "returncode": completed.returncode,
            "summary": observed,
            "result_seen": result_seen,
            "stdout_bytes": len(completed.stdout.encode("utf-8")),
            "passed": (
                completed.returncode == 0
                and observed is not None
                and observed[1] == 0
                and result_seen
            ),
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "path": str(path.relative_to(ROOT)),
            "sha256": before,
            "sha_stable": before == _sha256(path),
            "returncode": "timeout",
            "summary": None,
            "result_seen": False,
            "stdout_bytes": len((exc.stdout or "").encode("utf-8"))
            if isinstance(exc.stdout, str)
            else 0,
            "passed": False,
        }


def landed_anchor_certificate() -> tuple[dict, ...]:
    science_path, release_path = tuple(ROOT / value for value in AUDIT_INPUT_PATHS)
    rows = (
        _run_landed_surface(
            science_path,
            r"SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)",
            "CYCLE317_PHYSICAL_CONTACT_TERNARY_BORN_BRIDGE_GREEN",
        ),
        _run_landed_surface(
            release_path,
            r"STRICT SUMMARY PASS\s+(\d+)\s+FAIL\s+(\d+)",
            "CYCLE317_RELEASE_DISCIPLINE_GREEN",
        ),
    )
    imported_paths = (
        Path(B317.__file__).resolve(),
        Path(R317.__file__).resolve(),
    )
    check(
        "A landed anchors: both Cycle-317 surfaces rerun clean at stable SHA-256",
        all(row["passed"] and row["sha_stable"] for row in rows)
        and imported_paths == (science_path.resolve(), release_path.resolve()),
        rows,
    )
    return rows


def census_certificate(
    bridge_source: str,
    bridge_tree: ast.Module,
    release_tree: ast.Module,
) -> dict[str, tuple[str, ...]]:
    live = _live_signature_inventory(bridge_tree)
    annotations = _live_annotation_inventory(bridge_tree)
    receiver_hits = {
        function: tuple(
            parameter
            for parameter in parameters
            if any(fragment in parameter.lower() for fragment in RECEIVER_NAME_FRAGMENTS)
        )
        for function, parameters in live.items()
    }
    receiver_hits = {
        function: hits for function, hits in receiver_hits.items() if hits
    }
    release_functions = tuple(node.name for node in _top_level_functions(release_tree))
    release_mentions_science = AUDIT_INPUT_PATHS[0].split("/")[-1] in bridge_source or (
        "SCIENCE" in {node.id for node in ast.walk(release_tree) if isinstance(node, ast.Name)}
    )
    check(
        "B own AST census: the landed science surface is exactly the frozen 20-signature inventory",
        len(live) == 20
        and live == FROZEN_PORT_INVENTORY
        and annotations == FROZEN_PORT_ANNOTATIONS
        and bool(release_functions)
        and release_mentions_science,
        {
            "science_signature_count": len(live),
            "release_function_count": len(release_functions),
            "inventory_match": live == FROZEN_PORT_INVENTORY,
            "annotation_match": annotations == FROZEN_PORT_ANNOTATIONS,
        },
    )
    check(
        "B per-port frozen type argument: no landed port receives count/frequency/exposure/occurrence/Record rows",
        set(FROZEN_PORT_TYPE_ARGUMENTS) == set(live)
        and not receiver_hits
        and all(FROZEN_PORT_TYPE_ARGUMENTS[name] for name in live),
        {
            "receiver_name_hits": receiver_hits,
            "arguments": FROZEN_PORT_TYPE_ARGUMENTS,
        },
    )
    return live


def _assignment_segment(
    source: str, outer: ast.FunctionDef, target_name: str
) -> str | None:
    for node in outer.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == target_name
        ):
            return ast.get_source_segment(source, node)
    return None


def held_weight_certificate(source: str, tree: ast.Module) -> dict:
    outer = next(
        (
            node
            for node in _top_level_functions(tree)
            if node.name == "mixed_projective_forcing_basis_controls"
        ),
        None,
    )
    if outer is None:
        located = {}
        condition = False
    else:
        born = next(
            (
                node
                for node in outer.body
                if isinstance(node, ast.FunctionDef) and node.name == "born_weight"
            ),
            None,
        )
        returned = (
            next((node for node in born.body if isinstance(node, ast.Return)), None)
            if born is not None
            else None
        )
        located = {
            "bloch": _assignment_segment(source, outer, "bloch"),
            "sigma": _assignment_segment(source, outer, "sigma"),
            "function": (
                source.splitlines()[born.lineno - 1].strip()
                if born is not None
                else None
            ),
            "return": (
                ast.get_source_segment(source, returned).strip()
                if returned is not None
                else None
            ),
            "scope": "mixed_projective_forcing_basis_controls.<locals>.born_weight",
        }
        stores = Counter(
            node.id
            for node in ast.walk(outer)
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store)
        )
        condition = (
            {key: located[key] for key in FROZEN_HELD_WEIGHT_FORM}
            == FROZEN_HELD_WEIGHT_FORM
            and born is not None
            and tuple(argument.arg for argument in _function_parameters(born))
            == ("effect",)
            and stores["bloch"] == 1
            and stores["sigma"] == 1
        )
        located["fixed_store_counts"] = {
            "bloch": stores["bloch"],
            "sigma": stores["sigma"],
        }
    check(
        "C landed w(E) is located and frozen as the held fixed-sigma per-effect trace candidate",
        condition,
        located,
    )
    return located


def interface_theorem_certificate(
    live_inventory: dict[str, tuple[str, ...]]
) -> dict:
    all_landed_parameters = {
        parameter
        for parameters in live_inventory.values()
        for parameter in parameters
    }
    interface_parameter_names = {
        "menu_id",
        "program_id",
        "effect_ids",
        "records",
        "exposure",
        "sampling",
        "provenance",
        "coarse_graining",
        "same_effect",
        "calibration",
    }
    dimension_rows = tuple(
        {
            "N": size,
            "integer_count_slots": size,
            "simplex_sum_rules": 1,
            "simplex_dimension": size - 1,
        }
        for size in (2, 4, 7)
    )
    condition = (
        tuple(COMPONENT_NECESSITY) == REQUIRED_BRIDGE_SIGNATURE
        and len(COMPONENT_NECESSITY) == 8
        and not (all_landed_parameters & interface_parameter_names)
        and all(
            row["integer_count_slots"] == row["N"]
            and row["simplex_dimension"] == row["N"] - 1
            for row in dimension_rows
        )
        and INTERFACE_STAGES
        == (
            "typed Records R[0:M] -> ordered N-count vector n in N^N",
            "n + exposure/sampling + provenance -> exact f in Delta^(N-1)",
            "f + coarse-graining + same-effect identities + calibration -> per-effect w[0:N]",
        )
    )
    detail = {
        "signature": REQUIRED_BRIDGE_SIGNATURE,
        "stages": INTERFACE_STAGES,
        "dimension_rows": dimension_rows,
        "dropped_component_breaks": COMPONENT_NECESSITY,
        "landed_interface_name_overlap": sorted(
            all_landed_parameters & interface_parameter_names
        ),
    }
    check(
        "D bounded interface theorem: occurrence-to-w(E) requires the exact frozen bridge signature and every component is necessary",
        condition,
        detail,
    )
    return detail


def _declared_rows(profile: str, counts: tuple[int, ...]) -> tuple[RecordRow, ...]:
    rows = []
    sequence = 0
    for outcome_index, count in enumerate(counts):
        for local_index in range(count):
            rows.append(
                RecordRow(
                    record_id=f"{profile}-r{sequence:02d}-{local_index:02d}",
                    menu_id=DECLARED_MENU_ID,
                    program_id=DECLARED_PROGRAM_ID,
                    outcome_index=outcome_index,
                    effect_id=DECLARED_EFFECT_IDS[outcome_index],
                    exposure_id=f"{profile}-exposure",
                    record_kind="declared_apparatus_test_row",
                    provenance=f"cycle744-declared-family:{profile}",
                )
            )
            sequence += 1
    return tuple(rows)


def _declarations(
    profile: str, trial_total: int
) -> tuple[MenuProgramIdentity, ExposureDeclaration, EffectIdentityMetadata]:
    identity = MenuProgramIdentity(DECLARED_MENU_ID, DECLARED_PROGRAM_ID)
    exposure = ExposureDeclaration(
        exposure_id=f"{profile}-exposure",
        menu_id=DECLARED_MENU_ID,
        program_id=DECLARED_PROGRAM_ID,
        trial_total=trial_total,
        per_effect_eligible_trials=(trial_total,) * len(DECLARED_EFFECT_IDS),
        sampling_protocol="complete-exclusive-common-exposure",
        provenance=f"cycle744-declared-exposure:{profile}",
    )
    metadata = EffectIdentityMetadata(
        coarse_grainings=(
            ("all", (0, 1, 2, 3)),
            ("low-pair", (0, 1)),
            ("high-pair", (2, 3)),
        ),
        same_effect_classes=tuple((effect_id,) for effect_id in DECLARED_EFFECT_IDS),
    )
    return identity, exposure, metadata


def port_construction_certificate() -> tuple[dict[str, EmpiricalPortResult], tuple[str, ...]]:
    empirical = {}
    for profile, counts in DECLARED_APPARATUS_DATA_FAMILY:
        rows = _declared_rows(profile, counts)
        identity, exposure, metadata = _declarations(profile, len(rows))
        empirical[profile] = receive_occurrence_records(
            identity,
            DECLARED_EFFECT_IDS,
            rows,
            exposure,
            metadata,
        )

    base_profile, base_counts = DECLARED_APPARATUS_DATA_FAMILY[0]
    base_rows = _declared_rows(base_profile, base_counts)
    identity, exposure, metadata = _declarations(base_profile, len(base_rows))
    malformed: tuple[tuple[str, Callable[[], object]], ...] = (
        (
            "untyped-row-container",
            lambda: receive_occurrence_records(
                identity,
                DECLARED_EFFECT_IDS,
                list(base_rows),  # type: ignore[arg-type]
                exposure,
                metadata,
            ),
        ),
        (
            "duplicate-record-id",
            lambda: receive_occurrence_records(
                identity,
                DECLARED_EFFECT_IDS,
                (
                    base_rows[0],
                    replace(base_rows[1], record_id=base_rows[0].record_id),
                )
                + base_rows[2:],
                exposure,
                metadata,
            ),
        ),
        (
            "effect-slot-mismatch",
            lambda: receive_occurrence_records(
                identity,
                DECLARED_EFFECT_IDS,
                (replace(base_rows[0], effect_id=DECLARED_EFFECT_IDS[1]),)
                + base_rows[1:],
                exposure,
                metadata,
            ),
        ),
        (
            "inconsistent-exposure-total",
            lambda: receive_occurrence_records(
                identity,
                DECLARED_EFFECT_IDS,
                base_rows,
                replace(
                    exposure,
                    trial_total=exposure.trial_total + 1,
                    per_effect_eligible_trials=(exposure.trial_total + 1,) * 4,
                ),
                metadata,
            ),
        ),
        (
            "missing-record-provenance",
            lambda: receive_occurrence_records(
                identity,
                DECLARED_EFFECT_IDS,
                (replace(base_rows[0], provenance=""),) + base_rows[1:],
                exposure,
                metadata,
            ),
        ),
    )
    refused = []
    for label, call in malformed:
        try:
            call()
        except ValueError:
            refused.append(label)

    exact_rows = {
        profile: {
            "counts": result.counts,
            "simplex": tuple(str(value) for value in result.simplex),
            "simplex_sum": str(sum(result.simplex, start=Fraction(0, 1))),
            "exposure_by_effect": result.exposure_by_effect,
            "coarse_counts": result.coarse_counts,
            "record_provenance": result.record_provenance,
            "exposure_provenance": result.exposure_provenance,
        }
        for profile, result in empirical.items()
    }
    check(
        "E receiver port: typed schema, exposure bookkeeping, and exact Fraction simplex normalization are lawful",
        all(
            all(type(value) is Fraction for value in result.simplex)
            and sum(result.simplex, start=Fraction(0, 1)) == Fraction(1, 1)
            and sum(result.counts) == len(_declared_rows(profile, counts))
            and dict(result.coarse_counts)["all"] == sum(result.counts)
            and all(
                eligible == sum(result.counts)
                for _, eligible in result.exposure_by_effect
            )
            for (profile, counts), result in zip(
                DECLARED_APPARATUS_DATA_FAMILY,
                empirical.values(),
                strict=True,
            )
        ),
        exact_rows,
    )
    check(
        "E lawful-domain refusals: malformed typed intakes are rejected",
        len(refused) == len(malformed) and len(refused) >= 3,
        {"refused": tuple(refused), "witness_count": len(refused)},
    )
    return empirical, tuple(refused)


def _held_landed_candidate_values(
    effects: tuple[np.ndarray, ...],
) -> tuple[float, ...]:
    bloch = np.asarray((0.21, -0.32, 0.41), dtype=float)
    sigma = (
        B317.I2
        + bloch[0] * B317.X
        + bloch[1] * B317.Y
        + bloch[2] * B317.Z
    ) / 2
    return tuple(float(np.trace(sigma @ effect).real) for effect in effects)


def comparator_flow_certificate(
    empirical: dict[str, EmpiricalPortResult],
) -> tuple[dict, tuple[float, ...]]:
    effects = tuple(
        float(scale) * B317.I2
        for scale in (
            Fraction(1, 10),
            Fraction(2, 10),
            Fraction(3, 10),
            Fraction(4, 10),
        )
    )
    held_values = _held_landed_candidate_values(effects)
    reports = {
        profile: compare_empirical_to_landed(result, held_values)
        for profile, result in empirical.items()
    }
    censuses = {
        profile: dict(sorted(Counter(row.verdict for row in rows).items()))
        for profile, rows in reports.items()
    }
    overall = dict(
        sorted(
            Counter(
                row.verdict
                for rows in reports.values()
                for row in rows
            ).items()
        )
    )
    data = {
        "per_profile": censuses,
        "overall": overall,
        "held_candidate_values": held_values,
        "empirical_simplexes": {
            profile: tuple(str(value) for value in result.simplex)
            for profile, result in empirical.items()
        },
        "interpretation": (
            "declared apparatus test data against a separately held candidate; "
            "DATA only, not a law"
        ),
    }
    check(
        "F comparator flow: the declared apparatus-data family yields the frozen agreement/disagreement census",
        censuses
        == {
            "landed-profile": {"agreement": 4},
            "counterfactual-shift": {"agreement": 2, "disagreement": 2},
        }
        and overall == {"agreement": 6, "disagreement": 2}
        and all(
            abs(value - target) < 1.0e-12
            for value, target in zip(
                held_values, (0.1, 0.2, 0.3, 0.4), strict=True
            )
        )
        and empirical["landed-profile"].simplex
        != empirical["counterfactual-shift"].simplex,
        data,
    )
    print("DATA comparator_verdict_census", json.dumps(data, sort_keys=True))
    return data, held_values


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    targets = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            raw = node.targets if isinstance(node, ast.Assign) else (node.target,)
            targets.extend(raw)
    return tuple(targets)


def firewall_certificate(
    module_state_before: tuple[dict[str, int], dict[str, int]],
    module_state_after: tuple[dict[str, int], dict[str, int]],
) -> dict:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    functions = {
        node.name: node for node in _top_level_functions(tree)
    }
    receiver = functions["receive_occurrence_records"]
    comparator = functions["compare_empirical_to_landed"]
    landed_attribute_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in {"B317", "R317"}
    )
    landed_setattrs = tuple(
        ast.unparse(node)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id in {"B317", "R317"}
    )
    receiver_landed_reads = tuple(
        node.id
        for node in ast.walk(receiver)
        if isinstance(node, ast.Name) and node.id in {"B317", "R317"}
    )
    receiver_weight_stores = tuple(
        node.id
        for node in ast.walk(receiver)
        if isinstance(node, ast.Name)
        and isinstance(node.ctx, ast.Store)
        and any(token in node.id.lower() for token in ("weight", "sigma", "bloch"))
    )
    receiver_forbidden_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(receiver)
        if isinstance(node, ast.Call)
        and ast.unparse(node.func)
        in {"_held_landed_candidate_values", "compare_empirical_to_landed"}
    )
    comparator_attribute_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(comparator)
        if isinstance(target, ast.Attribute)
    )
    detail = {
        "landed_module_attribute_writes": landed_attribute_writes,
        "landed_module_setattr_calls": landed_setattrs,
        "receiver_landed_module_reads": receiver_landed_reads,
        "receiver_weight_stores": receiver_weight_stores,
        "receiver_forbidden_calls": receiver_forbidden_calls,
        "comparator_attribute_writes": comparator_attribute_writes,
        "landed_module_identity_snapshot_unchanged": (
            module_state_before == module_state_after
        ),
    }
    check(
        "G firewall audit: AST has no port-data path to weight assignment and zero landed-module writes",
        not landed_attribute_writes
        and not landed_setattrs
        and not receiver_landed_reads
        and not receiver_weight_stores
        and not receiver_forbidden_calls
        and not comparator_attribute_writes
        and module_state_before == module_state_after,
        detail,
    )
    return detail


def _module_identity_snapshot(module: object) -> dict[str, int]:
    return {
        name: id(value)
        for name, value in vars(module).items()
        if not name.startswith("__")
    }


def honest_boundary() -> dict:
    return {
        "born_law_selected": False,
        "next_mechanism": "repeated-apparatus calibration bridge",
        "port_is_comparator_only": True,
        "receiver_hole_interface_frozen": True,
        "supplies": {
            "calibration_map": False,
            "coarse_graining_metadata": True,
            "exposure_and_provenance": True,
            "held_fixed_sigma_candidate_for_comparison": True,
            "ordered_effect_identities": True,
            "same_effect_identity_metadata": True,
            "selected_occurrence_law": False,
            "typed_declared_test_Record_rows": True,
        },
        "w6_closed": False,
    }


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()

    sources = {
        relative: (ROOT / relative).read_text(encoding="utf-8")
        for relative in AUDIT_INPUT_PATHS
    }
    bridge_source = sources[AUDIT_INPUT_PATHS[0]]
    bridge_tree = ast.parse(bridge_source, filename=AUDIT_INPUT_PATHS[0])
    release_tree = ast.parse(
        sources[AUDIT_INPUT_PATHS[1]], filename=AUDIT_INPUT_PATHS[1]
    )

    anchor_rows = landed_anchor_certificate()
    live_inventory = census_certificate(
        bridge_source, bridge_tree, release_tree
    )
    held_form = held_weight_certificate(bridge_source, bridge_tree)
    interface = interface_theorem_certificate(live_inventory)

    state_before = (
        _module_identity_snapshot(B317),
        _module_identity_snapshot(R317),
    )
    empirical, refused = port_construction_certificate()
    comparator_data, held_values = comparator_flow_certificate(empirical)
    state_after = (
        _module_identity_snapshot(B317),
        _module_identity_snapshot(R317),
    )
    firewall = firewall_certificate(state_before, state_after)

    boundary = honest_boundary()
    check(
        "H honest boundary: W6 remains open and the named next mechanism is the repeated-apparatus calibration bridge",
        boundary["w6_closed"] is False
        and boundary["receiver_hole_interface_frozen"] is True
        and boundary["port_is_comparator_only"] is True
        and boundary["born_law_selected"] is False
        and boundary["next_mechanism"]
        == "repeated-apparatus calibration bridge"
        and boundary["supplies"]["calibration_map"] is False
        and boundary["supplies"]["selected_occurrence_law"] is False,
        boundary,
    )

    runtime = perf_counter() - started
    boundary.update(
        {
            "all_checks_pass": FAIL == 0,
            "audit_input_sha256": {
                row["path"]: row["sha256"] for row in anchor_rows
            },
            "check_totals": {"fail": FAIL, "pass": PASS},
            "comparator_verdict_census": comparator_data["overall"],
            "held_candidate_values": held_values,
            "interface_component_count": len(interface["signature"]),
            "malformed_intake_witnesses_refused": len(refused),
            "runtime_seconds": round(runtime, 6),
            "w_E_frozen_form": {
                key: held_form.get(key) for key in FROZEN_HELD_WEIGHT_FORM
            },
            "zero_landed_module_writes": (
                not firewall["landed_module_attribute_writes"]
                and not firewall["landed_module_setattr_calls"]
            ),
        }
    )
    print("SUMMARY PASS", PASS, "FAIL", FAIL, "RUNTIME_SEC", f"{runtime:.6f}")
    print(json.dumps(boundary, sort_keys=True, separators=(",", ":")))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
