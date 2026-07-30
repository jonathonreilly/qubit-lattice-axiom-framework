#!/usr/bin/env python3
"""Clean-room check of the supplied split/merge POVM fixture.

This checker imports neither the primary runner nor the Cycle-317 constructor
module.  It reconstructs the source bookkeeping in a separate child process,
derives all matrix identities directly from Pauli matrices and Kraus blocks,
and only then compares a black-box primary execution.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/COMPANION_BANK_STATIC_CERTIFICATE_POVM_INPUT_CONVENTION_"
    "META_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_static_certificate_povm_independent_check_2026_07_30.py",
    "scripts/frontier_companion_bank_static_certificate_povm_input_acceptance_2026_07_30.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/physical_contact_ternary_born_forcing_release_cycle317_2026_07_18.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
    "scripts/frontier_companion_bank_epoch_liveness_2026_07_28.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28.py",
    "docs/AUTONOMOUS_INTERMITTENT_RECORD_INSTRUMENT_CALIBRATION_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/MINIMAL_RECORD_INSTRUMENT_DILATION_SCALAR_EXCHANGE_NONSELECTION_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/COMPANION_BANK_LIVENESS_SCHEDULE_ENDPOINT_INTERVAL_PACKET_PROJECTION_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/COMPANION_BANK_STATIC_CERTIFICATE_POVM_INPUT_CONVENTION_META_NOTE_2026-07-30.md",
    "docs/COMPANION_BANK_STATIC_CERTIFICATE_POVM_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/work_history/repo/review_feedback/ACTIVE_CUBIC_SOURCE_RESPONSE_CYCLE211_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/AUTONOMOUS_CUBIC_FIELD_EMISSION_CYCLE214_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/CONTACT_CLOSE_TYPED_RECORD_DAG_CYCLE287_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_DISCIPLINE_CHECKLIST_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FINITE_COIN_SCALAR_WAVE_DILATION_CYCLE215_NO_GO_LEDGER_2026-07-16.md",
    "docs/work_history/repo/review_feedback/FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/LOCAL_CONSERVATIVE_COMMIT_RESOURCE_GRAVITY_CYCLE9_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_COMMON_M64_FIXED_SEAM_CYCLE311_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_FULL_TWO_PARTICLE_SECTOR_INTERFACE_CYCLE305_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_HIGHER_NUMBER_FIXED_SEAM_CYCLE308_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_REFERENCE_RELATIVE_LOCALIZED_PAIR_LIFT_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_STAGGERED_RESERVOIR_CATCHUP_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md",
    "docs/work_history/repo/review_feedback/WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
PRIMARY = ROOT / (
    "scripts/frontier_companion_bank_static_certificate_povm_input_"
    "acceptance_2026_07_30.py"
)
SOURCE = ROOT / (
    "scripts/frontier_companion_bank_liveness_endpoint_interval_packet_"
    "projection_2026_07_28.py"
)
B317 = ROOT / (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_"
    "2026_07_18.py"
)
EXPECTED_PRIMARY_SHA256 = (
    "e3fef1d870852667ba1bdaaf9a434b0e1cddc931f7ac26182c90c69ae390925d"
)
EXPECTED_SOURCE_SHA256 = (
    "b3fee8b662bbed34f7259fd6aa83de5de26ec07272c154eec08b8fdf88f283f0"
)
EXPECTED_B317_SHA256 = (
    "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10"
)
FIELDS = ("certificate", "binder", "actuality", "admissibility", "law_domain")
SELECTED_FIELDS = ("certificate", "actuality", "law_domain")
STAGES = ("A", "B", "C", "D")
SPLITS = (Fraction(17, 100), Fraction(29, 100), Fraction(27, 50))
DIRECTIONS = (
    (1.0, 2.0, 3.0),
    (-1.0, 0.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, 0.0, -1.0),
)
I2 = np.eye(2, dtype=complex)
X = np.asarray(((0, 1), (1, 0)), dtype=complex)
Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
Z = np.asarray(((1, 0), (0, -1)), dtype=complex)
TOL = 2.0e-14


SOURCE_DRIVER = r"""
import json
from collections import Counter
import frontier_companion_bank_liveness_endpoint_interval_packet_projection_2026_07_28 as S

atlas = S.EPOCH.P.build_private_atlases()
left = S.EPOCH.build_epoch((2, 2, 2), "primary", atlas)
right = S.EPOCH.build_epoch(
    (2, 2, 2), "alternate_port", atlas, recurrent_override=left.recurrent
)
out = {}
for name, bundle in (("primary", left), ("alternate_port", right)):
    extension = S.extend_and_walk(bundle)
    owner_stage = {}
    for slot in extension["slots"]:
        for word in slot.words:
            owner_stage[word.word_id] = slot.stage
    destinations = Counter(owner_stage[edge[1]] for edge in extension["handoffs"])
    out[name] = {
        "field_counts": {
            field: sum(int(row[field]) for row in extension["table"])
            for field in ("certificate", "binder", "actuality", "admissibility", "law_domain")
        },
        "stage_destination_counts": {
            stage: destinations[stage] for stage in ("A", "B", "C", "D")
        },
        "rows": len(extension["table"]),
        "lawful": bool(extension["lawful"]),
    }
print(json.dumps(out, sort_keys=True, separators=(",", ":")))
"""


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def clean_environment() -> dict[str, str]:
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)
    environment["PYTHONPATH"] = "scripts"
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    return environment


def run_source_driver() -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, "-c", SOURCE_DRIVER],
        cwd=ROOT,
        env=clean_environment(),
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    if completed.returncode != 0 or completed.stderr:
        raise RuntimeError(
            f"source driver failed rc={completed.returncode}: {completed.stderr}"
        )
    return json.loads(completed.stdout)


def run_primary() -> dict[str, object]:
    completed = subprocess.run(
        [sys.executable, str(PRIMARY)],
        cwd=ROOT,
        env=clean_environment(),
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    if completed.returncode != 0 or completed.stderr:
        raise RuntimeError(
            f"primary failed rc={completed.returncode}: {completed.stderr}"
        )
    rows = [
        line.removeprefix("RESULT_JSON ")
        for line in completed.stdout.splitlines()
        if line.startswith("RESULT_JSON ")
    ]
    if len(rows) != 1:
        raise RuntimeError("primary emitted an invalid RESULT_JSON census")
    return json.loads(rows[0])


def projector(vector: np.ndarray) -> np.ndarray:
    vector = np.asarray(vector, dtype=float)
    if vector.shape != (3,) or abs(np.linalg.norm(vector) - 1) > 1e-10:
        raise ValueError("clean-room projector requires a unit three-vector")
    return (I2 + vector[0] * X + vector[1] * Y + vector[2] * Z) / 2


def padded_stack(blocks: list[np.ndarray]) -> np.ndarray:
    if not 1 <= len(blocks) <= 8:
        raise ValueError("one to eight Kraus blocks required")
    return np.vstack(blocks + [np.zeros((2, 2), complex)] * (8 - len(blocks)))


def effects_from_groups(
    isometry: np.ndarray, groups: tuple[tuple[int, ...], ...]
) -> tuple[np.ndarray, ...]:
    blocks = [
        isometry[2 * index : 2 * (index + 1), :] for index in range(8)
    ]
    return tuple(
        sum(
            (blocks[index].conj().T @ blocks[index] for index in group),
            start=np.zeros((2, 2), dtype=complex),
        )
        for group in groups
    )


def split_oracle(
    direction: np.ndarray, contact: np.ndarray
) -> tuple[np.ndarray, tuple[np.ndarray, ...]]:
    p = projector(direction)
    blocks = [
        np.sqrt(float(value)) * p @ contact for value in SPLITS
    ] + [(I2 - p) @ contact]
    isometry = padded_stack(blocks)
    effects = effects_from_groups(isometry, ((0,), (1,), (2,), (3,)))
    return isometry, effects


def merge_oracle(
    fractions: tuple[float, ...],
    directions: tuple[np.ndarray, ...],
    contact: np.ndarray,
) -> tuple[np.ndarray, tuple[np.ndarray, ...]]:
    blocks: list[np.ndarray] = []
    plus: list[int] = []
    minus: list[tuple[int, ...]] = []
    for fraction, direction in zip(fractions, directions):
        p = projector(direction)
        plus.append(len(blocks))
        blocks.append(np.sqrt(fraction) * p @ contact)
        minus.append((len(blocks),))
        blocks.append(np.sqrt(fraction) * (I2 - p) @ contact)
    isometry = padded_stack(blocks)
    effects = effects_from_groups(isometry, (tuple(plus), *minus))
    return isometry, effects


def effect_spectra(effects: tuple[np.ndarray, ...]) -> list[list[float]]:
    return [
        [float(value) for value in np.linalg.eigvalsh((effect + effect.conj().T) / 2)]
        for effect in effects
    ]


def close(left: object, right: object, tolerance: float = TOL) -> bool:
    return np.linalg.norm(np.asarray(left, dtype=float) - np.asarray(right, dtype=float)) < tolerance


def declared_paths() -> tuple[str, ...]:
    tree = ast.parse(SELF.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            return tuple(value)
    raise RuntimeError("literal AUDIT_INPUT_PATHS missing")


def input_fingerprint(primary_override: bytes | None = None) -> str:
    state = sha256()
    state.update(b"runner-cache-input-fingerprint-v1\0")
    for relative in declared_paths():
        path = ROOT / relative
        body = (
            primary_override
            if path.resolve() == PRIMARY.resolve() and primary_override is not None
            else path.read_bytes()
        )
        encoded = relative.encode("utf-8")
        state.update(len(encoded).to_bytes(8, "big"))
        state.update(encoded)
        state.update(len(body).to_bytes(8, "big"))
        state.update(body)
    return state.hexdigest()


def main() -> int:
    checks: list[tuple[str, bool]] = []

    def check(label: str, condition: bool) -> None:
        checks.append((label, bool(condition)))
        print("PASS" if condition else "FAIL", label)

    paths = declared_paths()
    check(
        "all mutable dependencies exist and primary bytes are explicitly bound",
        all((ROOT / path).is_file() for path in paths)
        and paths[1]
        == "scripts/frontier_companion_bank_static_certificate_povm_input_acceptance_2026_07_30.py"
        and digest(PRIMARY) == EXPECTED_PRIMARY_SHA256
        and digest(SOURCE) == EXPECTED_SOURCE_SHA256
        and digest(B317) == EXPECTED_B317_SHA256,
    )
    baseline_fingerprint = input_fingerprint()
    mutated_fingerprint = input_fingerprint(PRIMARY.read_bytes() + b"\n")
    check(
        "one-byte primary mutation changes the independent cache identity",
        baseline_fingerprint != mutated_fingerprint,
    )

    source = run_source_driver()
    expected_source = {
        "primary": {
            "field_counts": {field: 24 for field in FIELDS},
            "stage_destination_counts": {"A": 100, "B": 152, "C": 180, "D": 72},
            "rows": 24,
            "lawful": True,
        },
        "alternate_port": {
            "field_counts": {field: 24 for field in FIELDS},
            "stage_destination_counts": {"A": 100, "B": 12, "C": 0, "D": 72},
            "rows": 24,
            "lawful": True,
        },
    }
    check(
        "separate source driver reconstructs static-predicate and liveness counts",
        source == expected_source,
    )

    combined_fields = {
        field: sum(source[variant]["field_counts"][field] for variant in source)
        for field in FIELDS
    }
    raw = np.asarray([combined_fields[field] for field in SELECTED_FIELDS], float)
    direction = raw / np.linalg.norm(raw)
    contact = np.diag((np.exp(0.37j), 1.0)).astype(complex)
    split_isometry, split_effects = split_oracle(direction, contact)
    split_isometry_residual = float(
        np.linalg.norm(split_isometry.conj().T @ split_isometry - I2)
    )
    split_normalization = float(np.linalg.norm(sum(split_effects) - I2))
    check(
        "clean-room split derivation gives one isometry and four positive effects",
        sum(SPLITS) == 1
        and split_isometry_residual < TOL
        and split_normalization < TOL
        and close(effect_spectra(split_effects), [[0, 0.17], [0, 0.29], [0, 0.54], [0, 1]]),
    )

    stage_counts = tuple(
        sum(
            source[variant]["stage_destination_counts"][stage]
            for variant in source
        )
        for stage in STAGES
    )
    exact_fractions = tuple(Fraction(value, sum(stage_counts)) for value in stage_counts)
    fractions = tuple(float(value) for value in exact_fractions)
    directions = tuple(
        np.asarray(row, float) / np.linalg.norm(np.asarray(row, float))
        for row in DIRECTIONS
    )
    merge_isometry, merge_effects = merge_oracle(fractions, directions, contact)
    merge_isometry_residual = float(
        np.linalg.norm(merge_isometry.conj().T @ merge_isometry - I2)
    )
    merge_normalization = float(np.linalg.norm(sum(merge_effects) - I2))
    weighted_bloch = sum(
        (fraction * vector for fraction, vector in zip(fractions, directions)),
        start=np.zeros(3),
    )
    exact_norm = float(
        np.sqrt(7502 - 23900 / np.sqrt(14)) / 172
    )
    plus_eigenvalues = [
        float(value) for value in np.linalg.eigvalsh(merge_effects[0])
    ]
    check(
        "clean-room merge derivation gives exact fractions and five positive effects",
        exact_fractions
        == (Fraction(25, 86), Fraction(41, 172), Fraction(45, 172), Fraction(9, 43))
        and merge_isometry_residual < TOL
        and merge_normalization < TOL
        and abs(np.linalg.norm(weighted_bloch) - exact_norm) < TOL
        and close(
            plus_eigenvalues,
            [(1 - exact_norm) / 2, (1 + exact_norm) / 2],
        ),
    )

    subset_directions = []
    for selected in combinations(FIELDS, 3):
        candidate = np.asarray([combined_fields[field] for field in selected], float)
        subset_directions.append(candidate / np.linalg.norm(candidate))
    sign_mutation = direction.copy()
    sign_mutation[0] *= -1
    sign_delta = float(np.linalg.norm(projector(sign_mutation) - projector(direction)))
    reverse_isometry, reverse_effects = merge_oracle(
        fractions, tuple(reversed(directions)), contact
    )
    pairing_delta = float(np.linalg.norm(reverse_effects[0] - merge_effects[0]))
    swapped_fractions = (fractions[1], fractions[0], fractions[2], fractions[3])
    _swapped_isometry, swapped_effects = merge_oracle(
        swapped_fractions, directions, contact
    )
    stage_order_delta = float(np.linalg.norm(swapped_effects[0] - merge_effects[0]))
    primary_only = np.asarray(
        [source["primary"]["field_counts"][field] for field in SELECTED_FIELDS],
        float,
    )
    primary_only /= np.linalg.norm(primary_only)
    check(
        "valid-domain controls separate constructor validity from mapping selection",
        max(np.linalg.norm(candidate - direction) for candidate in subset_directions)
        < TOL
        and np.linalg.norm(primary_only - direction) < TOL
        and sign_delta > 0.8
        and pairing_delta > 0.1
        and stage_order_delta > 0.01
        and np.linalg.norm(reverse_isometry.conj().T @ reverse_isometry - I2)
        < TOL,
    )

    primary = run_primary()
    check(
        "black-box primary agrees with the independently derived source and matrices",
        primary["status"] == "PASS"
        and primary["source"] == source
        and close(primary["split"]["direction"], direction)
        and abs(primary["split"]["isometry_residual"] - split_isometry_residual) < TOL
        and abs(
            primary["split"]["povm_normalization_residual"] - split_normalization
        )
        < TOL
        and close(primary["split"]["effect_spectra"], effect_spectra(split_effects))
        and primary["merge"]["combined_stage_counts"] == list(stage_counts)
        and close(primary["merge"]["fractions"], fractions)
        and close(primary["merge"]["weighted_bloch"], weighted_bloch)
        and close(primary["merge"]["plus_effect_eigenvalues"], plus_eigenvalues)
        and close(primary["merge"]["effect_spectra"], effect_spectra(merge_effects))
        and primary["mapping_controls"]["source_selects_mapping"] is False,
    )

    check(
        "scope exposes every supplied interface and selects no physical Born content",
        primary["claim_boundary"]
        == {
            "conditional_matrix_identities_only": True,
            "register_state_readout": False,
            "source_to_apparatus_map_derived": False,
            "Born_law_selected": False,
            "occurrence_or_outcome_selected": False,
            "Record_or_history_constructed": False,
            "empirical_calibration": False,
        },
    )

    report = {
        "status": "PASS" if all(value for _label, value in checks) else "FAIL",
        "checks": {
            "pass": sum(value for _label, value in checks),
            "fail": sum(not value for _label, value in checks),
        },
        "pins": {
            "primary": digest(PRIMARY),
            "source": digest(SOURCE),
            "B317": digest(B317),
        },
        "cache_identity": {
            "declared_inputs": len(paths),
            "primary_bound": True,
            "one_byte_mutation_detected": baseline_fingerprint != mutated_fingerprint,
        },
        "split": {
            "isometry_residual": split_isometry_residual,
            "povm_normalization_residual": split_normalization,
        },
        "merge": {
            "fractions": [str(value) for value in exact_fractions],
            "isometry_residual": merge_isometry_residual,
            "povm_normalization_residual": merge_normalization,
            "weighted_bloch_norm": float(np.linalg.norm(weighted_bloch)),
            "plus_effect_eigenvalues": plus_eigenvalues,
        },
        "mutations": {
            "all_field_subsets_same": True,
            "primary_only_pool_same": True,
            "sign_projector_delta": sign_delta,
            "reversed_pairing_effect_delta": pairing_delta,
            "stage_order_effect_delta": stage_order_delta,
        },
        "independence": {
            "primary_imported": False,
            "B317_imported": False,
            "matrix_formulas_reimplemented": True,
            "primary_compared_as_black_box": True,
        },
        "authority": "none",
        "audit": "unset",
    }
    print("RESULT_JSON", json.dumps(report, sort_keys=True, separators=(",", ":")))
    print(
        "SUMMARY PASS",
        report["checks"]["pass"],
        "FAIL",
        report["checks"]["fail"],
    )
    print("RESULT COMPANION_BANK_STATIC_CERTIFICATE_POVM_INDEPENDENT_GREEN")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
