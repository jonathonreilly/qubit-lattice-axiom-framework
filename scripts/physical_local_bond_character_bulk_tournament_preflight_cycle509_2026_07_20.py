#!/usr/bin/env python3
"""Cycle 509 pre-held contract: local bond current, character, and bulk routes.

This executable performs cheap contracts only.  It evolves no interacting
science row and no held row.  Route A freezes a discrete CAR bond-current
field and its free-stream continuity identity.  Route B freezes a separate
global translation-character response.  Route C freezes an honest
multi-mediator open-cluster specification and terminal implementation/resource
obligations.  Authority none; audit unset; no refit.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from hashlib import sha256
from itertools import product
import json
import os
from pathlib import Path
import re
import resource
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import generated_beta_phase_register_cycle220_2026_07_16 as c220
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_BOND_CHARACTER_BULK_TOURNAMENT_PREFLIGHT_CYCLE509_NOTE_2026-07-20.md"
)
RESOURCE_SCOUT_RUNNER = ROOT / "scripts/physical_local_bond_character_ab_resource_scout_cycle509_2026_07_20.py"
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 3
PASS = 0
FAIL = 0

EMITTER_COUPLING = 0.02
SCATTERING_COUPLING = 0.02
CONTACT_COUPLING = c230.COUPLING
DISPLAYED_EMITTER_COUPLING = 0.02
DISPLAYED_SCATTERING_COUPLING = 0.02
DISPLAYED_CONTACT_COUPLING = 0.37
COEFFICIENT_LAW = "B-linear-linear"
SOURCE_FUNCTION = "M_plus(source)"
PROBE_FUNCTION = "M_plus(probe)"
ANGLE_CEILING = 0.35

NUMERIC_TOLERANCE = 1e-10
RUNNER_TOLERANCE = 1e-8
FIELD_ZERO_TOLERANCE = 1e-12
SIGNAL_ABSOLUTE_FLOOR = 1e-10
NUMERIC_SIGNAL_MULTIPLIER = 10.0
CHARACTER_MAGNITUDE_FLOOR = 0.05
SOURCE_LEDGER_TOLERANCE = 1e-8
BAND_FLOOR = 0.05
AXIAL_SEAM_CEILING = 0.02
CONTACT_FLOOR = 0.01
ROW_WALL_CEILING_SECONDS = 600
ROW_RSS_CEILING_BYTES = 3_000_000_000
ROUTE_C_SCOUT_WALL_CEILING_SECONDS = 1200
ROUTE_C_SCOUT_RSS_CEILING_BYTES = 3_000_000_000

ROUTE_A_SAMPLE_SURFACE = "post-CAR-stream/pre-contact/pre-collision"
ROUTE_B_SAMPLE_SURFACE = "after-complete-update-word"
FUTURE_SCOUT_AUTHORIZATION_ENV = "CYCLE509_SCOUT_AUTHORIZATION"
FUTURE_SCOUT_AUTHORIZATION_TOKEN = "root-cycle509-revision2-scout-after-dry-review-2026-07-20"
FUTURE_TRAIN_AUTHORIZATION_ENV = "CYCLE509_TRAIN_AUTHORIZATION"
FUTURE_TRAIN_AUTHORIZATION_TOKEN = "root-cycle509-revision2-train-after-dry-review-2026-07-20"

DECLARED_HISTORICAL_IDENTIFIERS = {
    "revision1_runner_sha256": "be886bd745c7110a600f5abfdfd8aba2ad71d8cd889263c3ce7829739e4c8625",
    "revision1_note_sha256": "0868301115cf30b1397ae1f40310a7e69efa4b34aa85783dc4696b0bb4b611c3",
}
QUARANTINED_RESOURCE_EVIDENCE = {
    "failed_scout_transcript_sha256": "30995f09cac05b09abf5aec59a7018cac18bd45ae1ec8a14ab702a5b36a55c34",
    "resource_transcript_sha256": "e019f76b5a71d5b2a216f5d70db75eabfeec1bd998a2a03466fe22f8f4bf7102",
    "resource_runner_sha256": "fdb48e5bd2c7ec63f3e1c51a5296214675c6d68e0650fa5e722f961332f670bf",
    "resource_transcript_retained_scope": (
        "compute/runtime/numerical/continuity evidence only; "
        "Route-A response/covariance invalid from substep mismatch; "
        "Route-B canonical diagnostic zero-weight"
    ),
}
LOCAL_TRANSCRIPT_CANDIDATES = {
    "failed_scout_transcript_sha256": Path("/tmp/cycle509-ab-resource-scout-canonical-20260720.log"),
    "resource_transcript_sha256": Path("/tmp/cycle509-ab-resource-scout-corrected-canonical-20260720.log"),
}
CLI_MODES = ("contract-preflight",)

TRAIN_BETAS = (-2 * np.pi / 9, -4 * np.pi / 9, -2 * np.pi / 3)
HELD_BETAS = (0.0, -8 * np.pi / 9)
MIDDLE_BETA = -4 * np.pi / 9
DELETIONS = (
    "emitter", "collision", "mediator-stream", "contact", "probe-coin",
    "source-mass-factor", "probe-mass-factor",
)

SOURCE_HASHES = {
    "cycle210": (
        ROOT / "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    ),
    "cycle219": (
        ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    ),
    "cycle220": (
        ROOT / "scripts/generated_beta_phase_register_cycle220_2026_07_16.py",
        "252708e5adf782d9ad2869add0d64fa757d9d0473d054ee548e98e31d5f7276f",
    ),
    "cycle230": (
        ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    ),
    "cycle441": (
        ROOT / "scripts/coherent_multibeta_physical_mass_controller_tournament_cycle441_2026_07_19.py",
        "c274f75ff2b2fe427f04598b84a01247765c562f7ab014ffee2d63af2f27b5d4",
    ),
    "cycle501": (
        ROOT / "scripts/physical_reciprocal_mediator_contact_dressed_tournament_cycle501_2026_07_20.py",
        "7e8a88c5b0cdd576d868a3932d820da7f9cf985b10de498c83d34eb35daa959d",
    ),
}

EXPECTED_TRAIN_MANIFEST_SHA256 = "d235ce413eaba7ac62c9100d45ef93824c246a4646f4cd9316c5a0191f1c73d8"
EXPECTED_HELD_MANIFEST_SHA256 = "7dcaf19fb91b49bbe6528f124e4f428d7d54774390ff608e6afef5841657facf"

POSITIVE_DIRECTIONS = (0, 2, 4)
NEGATIVE_DIRECTIONS = (1, 3, 5)
REVERSE = (1, 0, 3, 2, 5, 4)


@dataclass(frozen=True)
class CorridorGeometry:
    name: str
    side: int
    source_cell: tuple[int, int, int]
    probe_center: tuple[int, int, int]
    outgoing_direction: int
    depth: int
    response_window: tuple[int, ...]
    causal_axis: int
    causal_slab: tuple[int, ...]
    front_anchor_cuts: tuple[int, ...]
    fixed_probe_cut: int
    mirrored: bool
    held: bool


@dataclass(frozen=True)
class BulkGeometry:
    name: str
    side: int
    probe_center: tuple[int, int, int]
    source_radius: int
    source_cells: tuple[tuple[int, int, int], ...]
    inward_directions: tuple[int, ...]
    mediator_charge: int
    depth: int
    response_window: tuple[int, ...]
    boundary: str
    held: bool


TRAIN_CANONICAL = CorridorGeometry(
    "train-canonical-3D-L25", 25, (12, 12, 12), (8, 12, 12), 1, 5,
    (2, 3, 4, 5), 0, (8, 9, 10, 11, 12), (12, 11, 10, 9), 9, False, False,
)
TRAIN_MIRRORED = CorridorGeometry(
    "train-mirrored-3D-L25", 25, (12, 12, 12), (16, 12, 12), 0, 5,
    (2, 3, 4, 5), 0, (12, 13, 14, 15, 16), (13, 14, 15, 16), 16, True, False,
)
HELD_CANONICAL = CorridorGeometry(
    "blind-held-canonical-3D-L27", 27, (13, 13, 13), (9, 13, 13), 1, 5,
    (2, 3, 4, 5), 0, (9, 10, 11, 12, 13), (13, 12, 11, 10), 10, False, True,
)
HELD_MIRRORED = CorridorGeometry(
    "blind-held-mirrored-3D-L27", 27, (13, 13, 13), (17, 13, 13), 0, 5,
    (2, 3, 4, 5), 0, (13, 14, 15, 16, 17), (14, 15, 16, 17), 17, True, True,
)


def octahedral_sources(center: tuple[int, int, int], radius: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple(int(x) for x in (np.asarray(center) - radius * direction))
        for direction in c210.DIRECTIONS
    )


ROUTE_C_TRAIN = BulkGeometry(
    "train-open-octahedral-Q6-L15", 15, (7, 7, 7), 4,
    octahedral_sources((7, 7, 7), 4), tuple(range(6)), 6, 5, (2, 3, 4, 5),
    "open", False,
)
ROUTE_C_HELD = BulkGeometry(
    "blind-held-open-octahedral-Q6-L19", 19, (9, 9, 9), 5,
    octahedral_sources((9, 9, 9), 5), tuple(range(6)), 6, 6, (3, 4, 5, 6),
    "open", True,
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def emit(label: str, detail: object) -> None:
    """Emit a frozen declaration without misreporting it as an executed test."""
    print("DECLARATION", label, "::", detail)


def present_authorization_variables(environ: object) -> tuple[str, ...]:
    """Return auth names by membership, so an explicitly empty value is present."""
    return tuple(
        name for name in (FUTURE_SCOUT_AUTHORIZATION_ENV, FUTURE_TRAIN_AUTHORIZATION_ENV)
        if name in environ
    )


def reject_authorization_environment(environ: object) -> None:
    present = present_authorization_variables(environ)
    if present:
        print("REJECT contract-preflight forbids authorization-variable presence ::", present)
        raise SystemExit(2)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def beta_name(beta: float) -> str:
    names = {
        round(0.0, 12): "0",
        round(-2 * np.pi / 9, 12): "-2pi/9",
        round(-4 * np.pi / 9, 12): "-4pi/9",
        round(-2 * np.pi / 3, 12): "-2pi/3",
        round(-8 * np.pi / 9, 12): "-8pi/9",
    }
    return names[round(float(beta), 12)]


def manifest_digest(rows: list[dict]) -> str:
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return sha256(payload).hexdigest()


def corridor_packet(geometry: CorridorGeometry) -> dict:
    """Exact supplied A/B two-CAR wedge and parked-Q1 preparation."""
    axis = geometry.causal_axis
    unit = np.eye(3, dtype=int)[axis]
    cells = tuple(
        tuple(int(value) for value in (np.asarray(geometry.probe_center) + offset * unit))
        for offset in (-1, 0, 1)
    )
    envelope = tuple(float(value / np.sqrt(6.0)) for value in (1, 2, 1))
    return {
        "cells": cells,
        "envelope_exact": "(1,2,1)/sqrt(6)",
        "envelope": envelope,
        "positive_direction": POSITIVE_DIRECTIONS[axis],
        "negative_direction": NEGATIVE_DIRECTIONS[axis],
        "CAR_state": "antisymmetric wedge of envelope(+axis) and envelope(-axis)",
        "CAR_number": 2,
        "mediator_state": "one parked Q1 mode at the declared source",
        "mediator_Q": 1,
    }


def corridor_row(
    disposition: str,
    role: str,
    route: str,
    source_beta: float,
    probe_beta: float,
    geometry: CorridorGeometry,
    deletion: str = "none",
) -> dict:
    return {
        "disposition": disposition,
        "role": role,
        "route": route,
        "coefficient_law": COEFFICIENT_LAW,
        "source_beta": beta_name(source_beta),
        "probe_beta": beta_name(probe_beta),
        "geometry": asdict(geometry),
        "exact_packet": corridor_packet(geometry),
        "deletion": deletion,
        "deletion_applies_symmetrically_to": "interacting-and-matched-free",
        "free_partner": True,
        "repeat_free": True,
        "retain_full_field": route == "A-local-bond-current",
        "aggregate_norm_is_diagnostic_only": True,
        "route_sample_surface": (
            ROUTE_A_SAMPLE_SURFACE if route == "A-local-bond-current"
            else ROUTE_B_SAMPLE_SURFACE
        ),
        "authorization_required": True,
        "row_selector": False,
        "refit": False,
    }


def bulk_row(
    disposition: str,
    role: str,
    source_beta: float,
    probe_beta: float,
    geometry: BulkGeometry,
    deletion: str = "none",
) -> dict:
    return {
        "disposition": disposition,
        "role": role,
        "route": "C-open-octahedral-multimediator",
        "coefficient_law": COEFFICIENT_LAW,
        "source_beta": beta_name(source_beta),
        "probe_beta": beta_name(probe_beta),
        "geometry": asdict(geometry),
        "deletion": deletion,
        "implementation_status": "specification-only-pre-science",
        "exact_packet": "Route-C octahedral Q6 matter/preparation remains a frozen implementation obligation",
        "deletion_applies_symmetrically_to": "interacting-and-matched-free",
        "free_partner": True,
        "repeat_free": True,
        "authorization_required": True,
        "row_selector": False,
        "refit": False,
    }


def row_manifests() -> tuple[list[dict], list[dict]]:
    train: list[dict] = []
    for route in ("A-local-bond-current", "B-global-translation-character"):
        for source_beta in TRAIN_BETAS:
            for probe_beta in TRAIN_BETAS:
                train.append(corridor_row(
                    "train", "primary-mass-grid", route, source_beta, probe_beta,
                    TRAIN_CANONICAL,
                ))
        train.append(corridor_row(
            "train", "mirrored-direction-control", route, MIDDLE_BETA, MIDDLE_BETA,
            TRAIN_MIRRORED,
        ))
        for deletion in DELETIONS:
            train.append(corridor_row(
                "train", "selected-deletion", route, MIDDLE_BETA, MIDDLE_BETA,
                TRAIN_CANONICAL, deletion,
            ))

    train.append(bulk_row(
        "train", "implementation-resource-scout-sentinel", MIDDLE_BETA, MIDDLE_BETA,
        ROUTE_C_TRAIN,
    ))
    for deletion in DELETIONS:
        train.append(bulk_row(
            "train", "specified-deletion-terminal-obligation", MIDDLE_BETA,
            MIDDLE_BETA, ROUTE_C_TRAIN, deletion,
        ))

    held: list[dict] = []
    for route in ("A-local-bond-current", "B-global-translation-character"):
        for source_beta in HELD_BETAS:
            for probe_beta in HELD_BETAS:
                held.append(corridor_row(
                    "blind-held", "blind-held-mass-grid", route, source_beta,
                    probe_beta, HELD_CANONICAL,
                ))
        held.append(corridor_row(
            "blind-held", "blind-held-mirrored-direction-control", route,
            HELD_BETAS[-1], HELD_BETAS[-1], HELD_MIRRORED,
        ))
    for beta in HELD_BETAS:
        held.append(bulk_row(
            "blind-held", "blind-held-size-mass-control", beta, beta,
            ROUTE_C_HELD,
        ))
    return train, held


def held_limit_classification(row: dict) -> str:
    """Classify exact decoupling limits without changing frozen manifest JSON."""
    source_zero = row["source_beta"] == "0"
    probe_zero = row["probe_beta"] == "0"
    if source_zero:
        return "zero-source-no-emission-null-response"
    if probe_zero:
        return "positive-source-zero-probe-active-source-null-transfer"
    return "positive-positive-transfer-scaling-test"


def mass_stack() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    register = c220.cyclic_shift(9)
    identity = np.eye(9, dtype=complex)
    mass = 3j * (register - identity) @ np.linalg.solve(register + identity, identity)
    mass = np.asarray((mass + mass.conj().T) / 2)
    values, vectors = np.linalg.eigh(mass)
    positive_values = np.where(values > NUMERIC_TOLERANCE, values, 0.0)
    positive = (vectors * positive_values) @ vectors.conj().T
    return register, mass, positive


def beta_ray(register: np.ndarray, target: float) -> np.ndarray:
    beta, _value, vector = min(
        c220.register_eigenpairs(register),
        key=lambda row: abs(np.angle(np.exp(1j * (row[0] - target)))),
    )
    if abs(np.angle(np.exp(1j * (beta - target)))) > 2e-12:
        raise ValueError("beta is absent from the nine-cycle register")
    return vector


def factor_contracts() -> None:
    hashes = {name: path.is_file() and file_sha(path) == expected
              for name, (path, expected) in SOURCE_HASHES.items()}
    check("all predecessor hashes match exactly", all(hashes.values()), hashes)

    equality = {
        "displayed_emitter_equals_executable": DISPLAYED_EMITTER_COUPLING == EMITTER_COUPLING,
        "displayed_scattering_equals_executable": DISPLAYED_SCATTERING_COUPLING == SCATTERING_COUPLING,
        "displayed_contact_equals_imported_Cycle230": DISPLAYED_CONTACT_COUPLING == c230.COUPLING,
        "executable_contact_equals_imported_Cycle230": CONTACT_COUPLING == c230.COUPLING,
        "displayed_contact_is_0.37": DISPLAYED_CONTACT_COUPLING == 0.37,
        "coefficient_law_is_B_linear_linear": COEFFICIENT_LAW == "B-linear-linear",
        "source_function_is_M_plus": SOURCE_FUNCTION == "M_plus(source)",
        "probe_function_is_M_plus": PROBE_FUNCTION == "M_plus(probe)",
    }
    check("every displayed factor is bound to its executable constant/function", all(equality.values()), equality)

    register, mass, positive = mass_stack()
    rows = []
    residuals = []
    maximum_angle = 0.0
    for disposition, betas in (("train", TRAIN_BETAS), ("held-contract-only", HELD_BETAS)):
        for beta in betas:
            ray = beta_ray(register, beta)
            observed_raw = float(np.vdot(ray, positive @ ray).real)
            observed = 0.0 if abs(observed_raw) < NUMERIC_TOLERANCE else observed_raw
            expected = max(0.0, float(-3 * np.tan(beta / 2)))
            residuals.append(abs(observed - expected))
            maximum_angle = max(maximum_angle, EMITTER_COUPLING * observed, SCATTERING_COUPLING * observed)
            rows.append({
                "disposition": disposition,
                "beta": beta_name(beta),
                "M_plus": observed,
                "emitter_angle": EMITTER_COUPLING * observed,
                "collision_angle": SCATTERING_COUPLING * observed,
            })
    check(
        "operator-first M_plus rays bind every emitter/scattering factor and obey angle ceiling",
        max(residuals) < RUNNER_TOLERANCE and maximum_angle < ANGLE_CEILING
        and rows[-2]["M_plus"] < NUMERIC_TOLERANCE,
        {"rows": rows, "maximum_mass_residual": max(residuals), "maximum_angle": maximum_angle},
    )
    check(
        "Cycle219 coin beta rays remain unitary under the exact train/held menu",
        max(np.linalg.norm(c219.common_species(beta).coin.conj().T @ c219.common_species(beta).coin - np.eye(6))
            for beta in TRAIN_BETAS + HELD_BETAS) < RUNNER_TOLERANCE,
    )

    train_mass_rows = []
    for beta in TRAIN_BETAS:
        species = c219.common_species(beta)
        principal_rest_mass = c219.rest_mass(species)
        train_mass_rows.append({
            "beta": beta_name(beta),
            "analytic_mass": species.analytic_mass,
            "principal_rest_mass": principal_rest_mass,
            "rest_phase": species.rest_phase,
            "residual": abs(principal_rest_mass - species.analytic_mass),
        })
    held_alias_species = c219.common_species(HELD_BETAS[-1])
    held_principal_rest_mass = c219.rest_mass(held_alias_species)
    check(
        "Cycle219 principal rest-mass fixture is retained only on the safe train branch",
        max(row["residual"] for row in train_mass_rows) < RUNNER_TOLERANCE
        and max(abs(row["rest_phase"]) for row in train_mass_rows) < np.pi,
        train_mass_rows,
    )
    check(
        "held -8pi/9 remains a supplied M_plus factor coordinate with unresolved principal mass alias",
        held_alias_species.analytic_mass > 17.0
        and held_alias_species.rest_phase > np.pi
        and abs(held_principal_rest_mass - held_alias_species.analytic_mass) > 1.0,
        {
            "beta": "-8pi/9",
            "M_plus_factor_coordinate": held_alias_species.analytic_mass,
            "rest_phase": held_alias_species.rest_phase,
            "principal_rest_mass": held_principal_rest_mass,
            "physical_mass_or_inertia_result": None,
        },
    )


def stream_occupation(occupation: np.ndarray) -> np.ndarray:
    side = occupation.shape[0]
    output = np.zeros_like(occupation)
    for direction, vector in enumerate(c210.DIRECTIONS):
        moved = occupation[..., direction]
        for axis, amount in enumerate(vector):
            if amount:
                moved = np.roll(moved, int(amount), axis=axis)
        output[..., direction] = moved
    if output.shape != (side, side, side, 6):
        raise RuntimeError("invalid occupation shape")
    return output


def local_bond_field(post_stream: np.ndarray) -> np.ndarray:
    """j_a(r)=n_post(r,+a)-n_post(r-e_a,-a), a=x,y,z."""
    output = np.empty(post_stream.shape[:3] + (3,), dtype=float)
    for axis, (positive, negative) in enumerate(zip(POSITIVE_DIRECTIONS, NEGATIVE_DIRECTIONS)):
        output[..., axis] = (
            post_stream[..., positive] - np.roll(post_stream[..., negative], 1, axis=axis)
        )
    return output


def plane_bond_field(post_stream: np.ndarray) -> np.ndarray:
    local = local_bond_field(post_stream)
    side = post_stream.shape[0]
    output = np.empty((3, side), dtype=float)
    for axis in range(3):
        transverse = tuple(value for value in range(3) if value != axis)
        output[axis] = np.sum(local[..., axis], axis=transverse)
    return output


def plane_density(occupation: np.ndarray, axis: int) -> np.ndarray:
    transverse = tuple(value for value in range(3) if value != axis)
    return np.sum(occupation, axis=transverse + (3,))


def continuity_residual(pre_stream: np.ndarray) -> float:
    post_stream = stream_occupation(pre_stream)
    current = plane_bond_field(post_stream)
    residual = 0.0
    for axis in range(3):
        change = plane_density(post_stream, axis) - plane_density(pre_stream, axis)
        divergence = current[axis] - np.roll(current[axis], -1)
        residual = max(residual, float(np.max(abs(change - divergence))))
    return residual


def rotate_occupation(occupation: np.ndarray, frame: np.ndarray) -> np.ndarray:
    side = occupation.shape[0]
    center = side // 2
    output = np.zeros_like(occupation)
    permutation = c210.direction_permutation(frame)
    for cell in product(range(side), repeat=3):
        moved_cell = tuple(int(x) for x in ((frame @ (np.asarray(cell) - center) + center) % side))
        for direction in range(6):
            moved_direction = int(np.argmax(permutation[:, direction]))
            output[moved_cell + (moved_direction,)] = occupation[cell + (direction,)]
    return output


def frame_cell(cell: tuple[int, int, int], frame: np.ndarray, side: int) -> tuple[int, int, int]:
    center = side // 2
    return tuple(int(x) for x in ((frame @ (np.asarray(cell) - center) + center) % side))


def carried_bond_cut(
    cut: int, center: tuple[int, int, int], source_axis: int, frame: np.ndarray
) -> tuple[int, int, int]:
    """Carry the +axis-oriented bond `(cut-1,cut)` through a centered frame."""
    source_vector = np.eye(3, dtype=int)[source_axis]
    moved = frame @ source_vector
    target_axis = int(np.argmax(abs(moved)))
    orientation = int(moved[target_axis])
    offset = int(cut - center[source_axis])
    target_cut = int(
        center[target_axis] + offset
        if orientation > 0 else center[target_axis] - offset + 1
    )
    return target_axis, orientation, target_cut


def current_field_contracts() -> None:
    side = 5
    maximum_basis_continuity = 0.0
    for cell in product(range(side), repeat=3):
        for direction in range(6):
            occupation = np.zeros((side, side, side, 6), dtype=float)
            occupation[cell + (direction,)] = 1.0
            maximum_basis_continuity = max(maximum_basis_continuity, continuity_residual(occupation))
    check(
        "free CAR stream obeys the exhaustive discrete plane-continuity identity",
        maximum_basis_continuity < NUMERIC_TOLERANCE,
        {
            "identity": "rho_post[a,c]-rho_pre[a,c]=J_a(c)-J_a(c+1)",
            "J_x(c)": "sum_yz[n_post(c,y,z,+x)-n_post(c-1,y,z,-x)]",
            "basis_columns": side**3 * 6,
            "maximum_residual": maximum_basis_continuity,
        },
    )

    rng = np.random.default_rng(509)
    post = rng.random((side, side, side, 6))
    original = local_bond_field(post)
    maximum_covariance = 0.0
    for frame in c210.proper_cubic_frames():
        rotated = rotate_occupation(post, frame)
        rotated_field = local_bond_field(rotated)
        for axis, positive_direction in enumerate(POSITIVE_DIRECTIONS):
            moved_vector = frame @ c210.DIRECTIONS[positive_direction]
            moved_direction = int(np.where(np.all(c210.DIRECTIONS == moved_vector, axis=1))[0][0])
            target_axis = moved_direction // 2
            positive_orientation = moved_direction % 2 == 0
            for cell in product(range(side), repeat=3):
                if positive_orientation:
                    target_cell = frame_cell(cell, frame, side)
                    expected = original[cell + (axis,)]
                else:
                    predecessor = tuple(int(x) for x in ((np.asarray(cell) - c210.DIRECTIONS[positive_direction]) % side))
                    target_cell = frame_cell(predecessor, frame, side)
                    expected = -original[cell + (axis,)]
                maximum_covariance = max(
                    maximum_covariance,
                    abs(rotated_field[target_cell + (target_axis,)] - expected),
                )
    check(
        "the local bond-field definition transports under all 24 proper-cubic frames",
        maximum_covariance < NUMERIC_TOLERANCE,
        {
            "maximum_all24_local_field_definition_residual": maximum_covariance,
            "response_or_full_word_covariance_executed": False,
        },
    )

    emit(
        "frozen full-field primacy and diagnostic boundaries",
        {
            "retained_local_field": "delta_j_a(x,y,z,t) for all cells, axes, and frozen updates",
            "retained_plane_field": "delta_J_a(c,t) for all axes, planes, and frozen updates",
            "primary_front_path": tuple(zip(TRAIN_CANONICAL.response_window, TRAIN_CANONICAL.front_anchor_cuts)),
            "primary_fixed_probe_cut": TRAIN_CANONICAL.fixed_probe_cut,
            "diagnostic_only": ("L1/L2/Linf field norms", "sum_d d_x<n_d>"),
        },
    )


def geometry_contracts() -> None:
    rows = []
    passed = True
    carried_endpoint_rows = []
    carried_endpoints_pass = True
    for canonical, mirrored in ((TRAIN_CANONICAL, TRAIN_MIRRORED), (HELD_CANONICAL, HELD_MIRRORED)):
        for geometry in (canonical, mirrored):
            displacement = np.asarray(geometry.probe_center) - np.asarray(geometry.source_cell)
            outgoing = c210.DIRECTIONS[geometry.outgoing_direction]
            points_to_probe = np.dot(displacement, outgoing) > 0 and np.count_nonzero(displacement) == 1
            direction_sign = int(outgoing[geometry.causal_axis])
            expected_anchors = tuple(
                geometry.source_cell[geometry.causal_axis]
                + direction_sign * (update - 1)
                + int(direction_sign < 0)
                for update in geometry.response_window
            )
            inside = all(0 < value < geometry.side - 1 for value in geometry.causal_slab + geometry.front_anchor_cuts)
            packet = corridor_packet(geometry)
            packet_cells = tuple(
                tuple(int(value) for value in (
                    np.asarray(geometry.probe_center)
                    + offset * np.eye(3, dtype=int)[geometry.causal_axis]
                ))
                for offset in (-1, 0, 1)
            )
            packet_valid = (
                packet["cells"] == packet_cells
                and abs(sum(value * value for value in packet["envelope"]) - 1.0) < NUMERIC_TOLERANCE
                and packet["positive_direction"] == POSITIVE_DIRECTIONS[geometry.causal_axis]
                and packet["negative_direction"] == NEGATIVE_DIRECTIONS[geometry.causal_axis]
                and packet["CAR_number"] == 2 and packet["mediator_Q"] == 1
            )
            passed &= points_to_probe and expected_anchors == geometry.front_anchor_cuts and inside and packet_valid
            rows.append({
                "geometry": geometry.name,
                "source": geometry.source_cell,
                "probe": geometry.probe_center,
                "outgoing": tuple(int(x) for x in outgoing),
                "front_anchors": tuple(zip(geometry.response_window, geometry.front_anchor_cuts)),
                "causal_slab": geometry.causal_slab,
                "points_to_probe": bool(points_to_probe),
                "packet_valid": bool(packet_valid),
            })
        passed &= (
            canonical.probe_center[0] - canonical.source_cell[0]
            == -(mirrored.probe_center[0] - mirrored.source_cell[0])
            and canonical.outgoing_direction == REVERSE[mirrored.outgoing_direction]
        )
        mirror_frame = np.diag((-1, -1, 1))
        carried_front = tuple(
            carried_bond_cut(cut, canonical.source_cell, canonical.causal_axis, mirror_frame)
            for cut in canonical.front_anchor_cuts
        )
        carried_fixed = carried_bond_cut(
            canonical.fixed_probe_cut, canonical.source_cell, canonical.causal_axis,
            mirror_frame,
        )
        passed &= (
            all(axis == mirrored.causal_axis and orientation == -1 for axis, orientation, _cut in carried_front)
            and tuple(cut for _axis, _orientation, cut in carried_front) == mirrored.front_anchor_cuts
            and carried_fixed == (mirrored.causal_axis, -1, mirrored.fixed_probe_cut)
        )

        for frame in c210.proper_cubic_frames():
            for cut in canonical.front_anchor_cuts + (canonical.fixed_probe_cut,):
                axis, orientation, target_cut = carried_bond_cut(
                    cut, canonical.source_cell, canonical.causal_axis, frame
                )
                passed &= axis in range(3) and orientation in (-1, 1)
                passed &= 0 < target_cut < canonical.side
                source_low = list(canonical.source_cell)
                source_high = list(canonical.source_cell)
                source_low[canonical.causal_axis] = cut - 1
                source_high[canonical.causal_axis] = cut
                moved_low = frame_cell(tuple(source_low), frame, canonical.side)
                moved_high = frame_cell(tuple(source_high), frame, canonical.side)
                target_low = list(canonical.source_cell)
                target_high = list(canonical.source_cell)
                target_low[axis] = target_cut - 1
                target_high[axis] = target_cut
                expected_endpoints = (
                    (tuple(target_low), tuple(target_high))
                    if orientation > 0 else (tuple(target_high), tuple(target_low))
                )
                endpoint_match = (moved_low, moved_high) == expected_endpoints
                carried_endpoints_pass &= endpoint_match
                carried_endpoint_rows.append({
                    "geometry": canonical.name,
                    "cut": cut,
                    "target_axis": axis,
                    "orientation": orientation,
                    "target_cut": target_cut,
                    "moved_endpoints": (moved_low, moved_high),
                    "expected_endpoints": expected_endpoints,
                    "match": endpoint_match,
                })
    check(
        "direction reversal uses a mirrored source-probe geometry and never launches away from the probe",
        passed,
        rows,
    )
    check(
        "all24 carried-bond cuts agree endpoint-by-endpoint with centered frame_cell transport",
        carried_endpoints_pass and len(carried_endpoint_rows) == 2 * 24 * 5,
        {
            "endpoint_cases": len(carried_endpoint_rows),
            "all_match": carried_endpoints_pass,
        },
    )

    sources = set(ROUTE_C_TRAIN.source_cells)
    held_sources = set(ROUTE_C_HELD.source_cells)
    route_c_pairs = set(zip(ROUTE_C_TRAIN.source_cells, ROUTE_C_TRAIN.inward_directions))
    held_route_c_pairs = set(zip(ROUTE_C_HELD.source_cells, ROUTE_C_HELD.inward_directions))
    route_c = {
        "train_six_distinct_sources": len(sources) == 6,
        "held_six_distinct_sources": len(held_sources) == 6,
        "train_Q6": ROUTE_C_TRAIN.mediator_charge == 6,
        "held_Q6": ROUTE_C_HELD.mediator_charge == 6,
        "open_boundaries": ROUTE_C_TRAIN.boundary == ROUTE_C_HELD.boundary == "open",
        "held_larger": ROUTE_C_HELD.side > ROUTE_C_TRAIN.side,
        "proper_cubic_source_orbit": all(
            {
                frame_cell(cell, frame, ROUTE_C_TRAIN.side)
                for cell in ROUTE_C_TRAIN.source_cells
            } == sources
            for frame in c210.proper_cubic_frames()
        ),
        "every_direction_points_inward": all(
            tuple(
                int(value) for value in (
                    np.asarray(cell)
                    + ROUTE_C_TRAIN.source_radius * c210.DIRECTIONS[direction]
                )
            ) == ROUTE_C_TRAIN.probe_center
            for cell, direction in route_c_pairs
        ),
        "proper_cubic_paired_source_direction_orbit": all(
            {
                (
                    frame_cell(cell, frame, ROUTE_C_TRAIN.side),
                    int(np.argmax(c210.direction_permutation(frame)[:, direction])),
                )
                for cell, direction in route_c_pairs
            } == route_c_pairs
            for frame in c210.proper_cubic_frames()
        ),
        "held_every_direction_points_inward": all(
            tuple(
                int(value) for value in (
                    np.asarray(cell)
                    + ROUTE_C_HELD.source_radius * c210.DIRECTIONS[direction]
                )
            ) == ROUTE_C_HELD.probe_center
            for cell, direction in held_route_c_pairs
        ),
        "held_proper_cubic_paired_source_direction_orbit": all(
            {
                (
                    frame_cell(cell, frame, ROUTE_C_HELD.side),
                    int(np.argmax(c210.direction_permutation(frame)[:, direction])),
                )
                for cell, direction in held_route_c_pairs
            } == held_route_c_pairs
            for frame in c210.proper_cubic_frames()
        ),
    }
    check(
        "Route C is a genuine localized 3D Q6 open-cluster specification",
        all(route_c.values()),
        {**route_c, "train": asdict(ROUTE_C_TRAIN), "held_contract_only": asdict(ROUTE_C_HELD)},
    )


JointMode = tuple[tuple[int, int, int], int]
JointState = tuple[tuple[tuple[int, int, int], int] | None, JointMode, JointMode]


def canonical_joint_pair(left: JointMode, right: JointMode) -> tuple[JointMode, JointMode] | None:
    if left == right:
        return None
    return (left, right) if left < right else (right, left)


def dense_coin_stream_mode(mode: JointMode) -> tuple[JointMode, ...]:
    cell, _incoming = mode
    return tuple(
        (
            tuple(int(value) for value in (np.asarray(cell) + c210.DIRECTIONS[outgoing])),
            outgoing,
        )
        for outgoing in range(6)
    )


def emit_boolean_support(states: set[JointState], source: tuple[int, int, int], outgoing: int) -> set[JointState]:
    source_key = (source, outgoing)
    output: set[JointState] = set()
    for mediator, left, right in states:
        if mediator in (None, source_key):
            output.add((None, left, right))
            output.add((source_key, left, right))
        else:
            output.add((mediator, left, right))
    return output


def car_dense_stream_boolean(states: set[JointState]) -> set[JointState]:
    output: set[JointState] = set()
    for mediator, left, right in states:
        for moved_left in dense_coin_stream_mode(left):
            for moved_right in dense_coin_stream_mode(right):
                pair = canonical_joint_pair(moved_left, moved_right)
                if pair is not None:
                    output.add((mediator, pair[0], pair[1]))
    return output


def collision_boolean_support(
    states: set[JointState], tainted: set[JointState]
) -> tuple[set[JointState], set[JointState], set[tuple[int, int, int]]]:
    """Generic-nonzero collision support; common contact creates no taint seed."""
    output = set(states)
    output_taint = set(tainted)
    collision_cells: set[tuple[int, int, int]] = set()
    for state in states:
        mediator, left, right = state
        if mediator is None:
            continue
        cell, direction = mediator
        old_mode = (cell, REVERSE[direction])
        new_mode = (cell, direction)
        if old_mode not in (left, right):
            continue
        partner = right if left == old_mode else left
        pair = canonical_joint_pair(new_mode, partner)
        if pair is None:
            continue
        scattered: JointState = ((cell, REVERSE[direction]), pair[0], pair[1])
        output.add(scattered)
        output_taint.add(state)
        output_taint.add(scattered)
        collision_cells.add(cell)
    return output, output_taint, collision_cells


def mediator_stream_boolean(states: set[JointState]) -> set[JointState]:
    output: set[JointState] = set()
    for mediator, left, right in states:
        if mediator is None:
            target = None
        else:
            cell, direction = mediator
            target = (
                tuple(int(value) for value in (np.asarray(cell) + c210.DIRECTIONS[direction])),
                direction,
            )
        output.add((target, left, right))
    return output


def tainted_bonds(states: set[JointState]) -> set[tuple[int, tuple[int, int, int]]]:
    result: set[tuple[int, tuple[int, int, int]]] = set()
    for _mediator, left, right in states:
        for cell, direction in (left, right):
            axis = direction // 2
            anchor = np.asarray(cell).copy()
            if direction % 2 == 1:
                anchor += np.eye(3, dtype=int)[axis]
            result.add((axis, tuple(int(value) for value in anchor)))
    return result


def boolean_joint_cone_fixture() -> dict:
    """Small exact-Boolean fixture for the separately carried structural cone."""
    source = (4, 0, 0)
    probe = (0, 0, 0)
    outgoing = 1
    packet_cells = tuple((offset, 0, 0) for offset in (-1, 0, 1))
    support: set[JointState] = {
        (None, pair[0], pair[1])
        for left_cell in packet_cells for right_cell in packet_cells
        for pair in [canonical_joint_pair((left_cell, 0), (right_cell, 1))]
        if pair is not None
    }
    taint: set[JointState] = set()
    rows = []
    previous_collision_cells: set[tuple[int, int, int]] = set()
    for update in range(1, 4):
        support = emit_boolean_support(support, source, outgoing)
        taint = emit_boolean_support(taint, source, outgoing)
        support = car_dense_stream_boolean(support)
        taint = car_dense_stream_boolean(taint)
        # This is the Route-A sample: post-CAR stream and before common contact/collision.
        sample_bonds = tainted_bonds(taint)
        rows.append({
            "update": update,
            "joint_support_states": len(support),
            "sample_tainted_joint_states": len(taint),
            "sample_tainted_bonds": len(sample_bonds),
            "sample_x_cuts": tuple(sorted({cell[0] for axis, cell in sample_bonds if axis == 0})),
            "prior_collision_cells": tuple(sorted(previous_collision_cells)),
        })
        support, taint, collision_cells = collision_boolean_support(support, taint)
        previous_collision_cells |= collision_cells
        support = mediator_stream_boolean(support)
        taint = mediator_stream_boolean(taint)
    return {"source": source, "probe": probe, "outgoing": outgoing, "rows": rows}


def causal_cone_contracts() -> None:
    fixture = boolean_joint_cone_fixture()
    rows = fixture["rows"]
    check(
        "a separate exact-Boolean joint recursion certifies a conservative structural interaction-difference bond cone",
        rows[0]["sample_tainted_joint_states"] == 0
        and rows[1]["sample_tainted_joint_states"] == 0
        and rows[2]["sample_tainted_joint_states"] > 0
        and 3 in rows[2]["sample_x_cuts"]
        and rows[1]["prior_collision_cells"] == ()
        and rows[2]["prior_collision_cells"] != (),
        {
            "fixture": fixture,
            "semantics": (
                "emitter support; exact-symbolic dense coin stream; common contact no seed; "
                "collision old/new direction taint; mediator reversal+stream"
            ),
            "claim_scope": "structural upper-bound cone, not exact amplitude support",
            "amplitude_pruning_can_certify_cone": False,
        },
    )


def circular_chord_distance(left: complex, right: complex) -> float:
    return float(abs(left / abs(left) - right / abs(right)))


def route_a_response_statistic(front_trace: tuple[float, ...]) -> float:
    """R_A is the peak absolute interaction-minus-free front trace."""
    if len(front_trace) != len(TRAIN_CANONICAL.response_window):
        raise ValueError("Route-A response statistic requires the four preregistered front samples")
    return float(np.max(np.abs(np.asarray(front_trace, dtype=float))))


def route_b_response_statistic(response_phasors: tuple[complex, ...]) -> float:
    """R_B is the peak unit-phasor chord from the matched-free identity."""
    if len(response_phasors) != len(TRAIN_CANONICAL.response_window):
        raise ValueError("Route-B response statistic requires four response phasors")
    if any(abs(abs(value) - 1.0) > NUMERIC_TOLERANCE for value in response_phasors):
        raise ValueError("Route-B response statistic requires unit response phasors")
    return float(max(abs(value - 1.0) for value in response_phasors))


def finite_angle_response_factor(source_mass: float, probe_mass: float) -> float:
    return float(
        np.sin(EMITTER_COUPLING * source_mass) ** 2
        * abs(np.sin(SCATTERING_COUPLING * probe_mass))
    )


def swap_log_residual(
    response_source_probe: float,
    response_probe_source: float,
    factor_source_probe: float,
    factor_probe_source: float,
) -> float:
    values = (
        response_source_probe, response_probe_source,
        factor_source_probe, factor_probe_source,
    )
    if any(value <= 0.0 for value in values):
        raise ValueError("swap-log residual is defined only for positive responses and factors")
    return float(abs(np.log(
        (response_source_probe / response_probe_source)
        / (factor_source_probe / factor_probe_source)
    )))


def circular_phase_morphology(response_phasors: tuple[complex, ...], numeric_residuals: tuple[float, ...]) -> dict:
    if len(response_phasors) != 4 or any(abs(abs(value) - 1.0) > NUMERIC_TOLERANCE for value in response_phasors):
        raise ValueError("Route-B morphology requires four unit response phasors")
    floor = max(SIGNAL_ABSOLUTE_FLOOR, NUMERIC_SIGNAL_MULTIPLIER * max(numeric_residuals, default=0.0))
    chords = np.asarray([value - 1.0 for value in response_phasors], dtype=complex)
    magnitudes = abs(chords)
    peak = float(np.max(magnitudes))
    peak_index = int(np.argmax(magnitudes))
    active = magnitudes >= floor
    longest = 0
    run = 0
    for value in active:
        run = run + 1 if value else 0
        longest = max(longest, run)
    tail_ratio = float(np.mean(magnitudes[-2:]) / peak) if peak else 0.0
    tail_denominator = float(np.sum(magnitudes[-2:]))
    tail_coherence = float(abs(np.sum(chords[-2:])) / tail_denominator) if tail_denominator else 0.0
    cumulative_scale = float(max(np.max(abs(np.cumsum(chords))), floor))
    last_to_peak = float(magnitudes[-1] / peak) if peak else 0.0
    last_to_cumulative = float(magnitudes[-1] / cumulative_scale)
    sustained = (
        peak >= floor and longest >= 3 and tail_ratio >= 0.50 and tail_coherence >= 0.90
    )
    impulse = (
        peak >= floor and not sustained and peak_index <= 1
        and last_to_peak <= 0.10 and last_to_cumulative <= 0.10
    )
    classification = (
        "sustained" if sustained else "impulse" if impulse
        else "transient-unresolved" if peak >= floor else "null"
    )
    return {
        "classification": classification,
        "chord_peak": peak,
        "tail_chord_direction_coherence": tail_coherence,
        "principal_angles_diagnostic_only": tuple(float(np.angle(value)) for value in response_phasors),
    }


def observable_and_classifier_contracts() -> None:
    across_cut = (
        np.exp(1j * (np.pi - 0.01)),
        np.exp(1j * (-np.pi + 0.01)),
    )
    circular_fixture = {
        "chord_distance": circular_chord_distance(*across_cut),
        "linear_principal_difference": abs(float(np.angle(across_cut[0]) - np.angle(across_cut[1]))),
        "carried_conjugacy_residual": abs(np.conj(across_cut[0]) - np.exp(-1j * (np.pi - 0.01))),
    }
    source_mass, probe_mass = 2.0, 3.0
    factor_source_probe = finite_angle_response_factor(source_mass, probe_mass)
    factor_probe_source = finite_angle_response_factor(probe_mass, source_mass)
    response_source_probe = 7.0 * factor_source_probe
    response_probe_source = 7.0 * factor_probe_source
    statistic_fixture = {
        "R_A": route_a_response_statistic((0.0, -0.25, 0.5, -0.125)),
        "R_B": route_b_response_statistic((1.0 + 0.0j, 1.0j, -1.0 + 0.0j, -1.0j)),
        "swap_log_residual": swap_log_residual(
            response_source_probe, response_probe_source,
            factor_source_probe, factor_probe_source,
        ),
    }
    contracts = {
        "route_A_primary": {
            "object": "full interaction-minus-free local/plane bond-current field",
            "sample_surface": ROUTE_A_SAMPLE_SURFACE,
            "front_path": tuple(zip(TRAIN_CANONICAL.response_window, TRAIN_CANONICAL.front_anchor_cuts)),
            "fixed_probe_cut": TRAIN_CANONICAL.fixed_probe_cut,
            "update_2": "exact pre-first-collision baseline; response floor applies as a required null",
            "sustained_samples": "updates 3,4,5 supply the three possible consecutive active samples",
            "morphology": "same frozen 4-sample sustained/impulse/null rules on predeclared readouts",
            "aggregate_field_norms": "diagnostic-only",
            "global_direction_current": "diagnostic-only; cannot rescue local field",
            "response_statistic": "R_A=max_t |delta_J_front(c_t,t)| on the preregistered front trace",
        },
        "route_B_primary": {
            "object": "delta_q_a(t)=Arg(z_a,int conj(z_a,free))",
            "sample_surface": ROUTE_B_SAMPLE_SURFACE,
            "scope": "global/nonlocal phase-like translation character",
            "branch": "unit response phasor is primary; principal (-pi,pi] angle is diagnostic only",
            "morphology": "complex chord amplitude/direction coherence; no linear classifier across principal cut",
            "carried_rule": "response phasor maps to its complex conjugate under axis reversal",
            "character_floor": CHARACTER_MAGNITUDE_FLOOR,
            "not": ("local current", "momentum", "force", "energy", "gravity"),
            "response_statistic": "R_B=max_t |u_t-1|, the unit-phasor chord peak",
        },
        "route_C_terminal": {
            "object": "six-source octahedral mediator-Fock open cluster",
            "collision": "single exponential of summed local Cycle501 direction-exchange generator",
            "implementation": "not implemented; resource scout must precede science",
            "science_before_implementation_gate": False,
        },
        "deletion_audit": {
            "mediator-stream": (
                "maximum mediator displacement<=1e-8 AND front-path response<=row floor "
                "AND fixed-probe response<=row floor"
            ),
            "route_A_contact_or_probe_coin_full_field_change": (
                "D_X=max_(a,c,t)|delta_J_intact-delta_J_deleted| on the full retained field"
            ),
            "route_A_dispositions": (
                "invalid", "coexistence-only", "full-field-sensitive", "primary-sensitive"
            ),
            "route_A_primary_sensitive": (
                "valid deletion plus preregistered front/fixed trace distance above floor; "
                "only this supports load-bearing-primary"
            ),
            "route_B_deletion_distance": "max_t |u_intact(t)-u_deleted(t)| on unit response phasors",
            "route_B_morphology": "circular chord classifier only",
            "sensitive": "structural deletion valid and route-specific distance>=comparison floor",
            "coexistence-only": "structural deletion valid and D_X<comparison floor",
            "invalid": "structural deletion or row technical gates fail",
            "route_A_primary_closure": (
                "does not require contact/coin sensitivity; reports the disposition separately"
            ),
            "load_bearing_contact_or_coin_claim": "requires sensitive",
            "symmetric_matched_free": True,
            "source_factor_distance_A": "max primary front/fixed absolute trace distance",
            "probe_factor_distance_A": "max primary front/fixed absolute trace distance",
            "source_factor_distance_B": "max response-phasor chord distance",
            "probe_factor_distance_B": "max response-phasor chord distance",
            "source_ledger_tolerance": SOURCE_LEDGER_TOLERANCE,
        },
        "response_floor": "max(1e-10,10*max numerical residual)",
        "factor_comparison": {
            "F": "sin^2(0.02 M_plus(source))*|sin(0.02 M_plus(probe))|",
            "positive_swap_residual": (
                "abs(log((R(ms,mp)/R(mp,ms))/(F(ms,mp)/F(mp,ms))))"
            ),
        },
        "no_refit": True,
        "future_execution_authorization": {
            "scout_env": FUTURE_SCOUT_AUTHORIZATION_ENV,
            "scout_exact_token": FUTURE_SCOUT_AUTHORIZATION_TOKEN,
            "train_env": FUTURE_TRAIN_AUTHORIZATION_ENV,
            "train_exact_token": FUTURE_TRAIN_AUTHORIZATION_TOKEN,
            "dry_rejects_authorization_presence": True,
            "row_selector": False,
            "refit": False,
        },
        "circular_fixture": circular_fixture,
    }
    check(
        "circular chord and carried-conjugacy fixtures avoid the principal-angle cut",
        circular_fixture["chord_distance"] < 0.03
        and circular_fixture["linear_principal_difference"] > 6.0
        and circular_fixture["carried_conjugacy_residual"] < NUMERIC_TOLERANCE,
        circular_fixture,
    )
    check(
        "Route-A/Route-B response statistics and positive swap-log residual execute their exact formulas",
        abs(statistic_fixture["R_A"] - 0.5) < NUMERIC_TOLERANCE
        and abs(statistic_fixture["R_B"] - 2.0) < NUMERIC_TOLERANCE
        and statistic_fixture["swap_log_residual"] < NUMERIC_TOLERANCE,
        statistic_fixture,
    )
    emit("frozen observable, deletion, classifier, and future-authorization declarations", contracts)


def manifest_contracts() -> tuple[list[dict], list[dict]]:
    train, held = row_manifests()
    train_digest, held_digest = manifest_digest(train), manifest_digest(held)
    train_roles = {role: sum(row["role"] == role for row in train) for role in sorted({row["role"] for row in train})}
    held_roles = {role: sum(row["role"] == role for row in held) for role in sorted({row["role"] for row in held})}
    held_limits = {
        label: sum(held_limit_classification(row) == label for row in held)
        for label in (
            "zero-source-no-emission-null-response",
            "positive-source-zero-probe-active-source-null-transfer",
            "positive-positive-transfer-scaling-test",
        )
    }
    checks = {
        "train_hash": train_digest == EXPECTED_TRAIN_MANIFEST_SHA256,
        "held_hash": held_digest == EXPECTED_HELD_MANIFEST_SHA256,
        "disjoint": not {json.dumps(row, sort_keys=True) for row in train} & {json.dumps(row, sort_keys=True) for row in held},
        "all_free_repeat_no_refit": all(row["free_partner"] and row["repeat_free"] and not row["refit"] for row in train + held),
        "route_A_full_field": all(row["retain_full_field"] for row in train + held if row["route"] == "A-local-bond-current"),
        "AB_exact_packet_frozen": all(
            isinstance(row.get("exact_packet"), dict)
            and row["exact_packet"]["envelope_exact"] == "(1,2,1)/sqrt(6)"
            and row["exact_packet"]["CAR_number"] == 2
            and row["exact_packet"]["mediator_Q"] == 1
            for row in train + held
            if row["route"] in ("A-local-bond-current", "B-global-translation-character")
        ),
        "sample_surfaces_are_route_exact": all(
            row["route_sample_surface"] == (
                ROUTE_A_SAMPLE_SURFACE if row["route"] == "A-local-bond-current"
                else ROUTE_B_SAMPLE_SURFACE
            )
            for row in train + held
            if row["route"] in ("A-local-bond-current", "B-global-translation-character")
        ),
        "symmetric_deletion_authorization_no_selector": all(
            row["deletion_applies_symmetrically_to"] == "interacting-and-matched-free"
            and row["authorization_required"] and row["row_selector"] is False
            for row in train + held
        ),
        "cli_contract_preflight_only": CLI_MODES == ("contract-preflight",),
        "held_exact_limit_partition": held_limits == {
            "zero-source-no-emission-null-response": 5,
            "positive-source-zero-probe-active-source-null-transfer": 2,
            "positive-positive-transfer-scaling-test": 5,
        },
    }
    check(
        "immutable train/held manifests are disjoint, deletion-complete, and refit-free",
        all(checks.values()),
        {
            **checks,
            "train_rows": len(train), "held_rows": len(held),
            "train_sha256": train_digest, "held_sha256": held_digest,
            "train_roles": train_roles, "held_roles": held_roles,
            "held_exact_limit_classification": held_limits,
        },
    )
    local_transcript_verification = {
        key: {
            "path": str(path),
            "present": path.is_file(),
            "matches_when_present": (
                file_sha(path) == QUARANTINED_RESOURCE_EVIDENCE[key]
                if path.is_file() else None
            ),
        }
        for key, path in LOCAL_TRANSCRIPT_CANDIDATES.items()
    }
    current_resource_runner_matches = (
        RESOURCE_SCOUT_RUNNER.is_file()
        and file_sha(RESOURCE_SCOUT_RUNNER)
        == QUARANTINED_RESOURCE_EVIDENCE["resource_runner_sha256"]
    )
    check(
        "the current old scout runner and any locally present quarantined transcripts match their identifiers",
        current_resource_runner_matches
        and all(
            row["matches_when_present"] is not False
            for row in local_transcript_verification.values()
        ),
        {
            "current_resource_runner_matches": current_resource_runner_matches,
            "local_transcripts": local_transcript_verification,
        },
    )
    emit(
        "declared historical identifiers; no executable Revision-1 artifact verification",
        DECLARED_HISTORICAL_IDENTIFIERS,
    )
    emit("quarantined resource-evidence disposition", QUARANTINED_RESOURCE_EVIDENCE)
    return train, held


def domain_deletion_resource_contracts() -> None:
    requirements = {
        "routes_A_B_domains": "matter N=2; source-register Q=1; mediator global Q=1",
        "route_C_domain": "matter N=2; mediator directional-Fock global Q=6; each local directional mode hard-core",
        "lawful_rejections": (
            "Pauli-duplicate CAR", "matter N!=2", "source Q!=1", "mediator Q mismatch",
            "Route-C duplicate directional occupation", "malformed geometry/axis/beta",
        ),
        "technical_gates": {
            "norm_inverse_number_Q_lawful_free_repeat": RUNNER_TOLERANCE,
            "free_substep_continuity": NUMERIC_TOLERANCE,
            "all24_field_definition_covariance_executed_here": NUMERIC_TOLERANCE,
            "supplied_factor_scope": (
                "inherited certificate identities bound by exact predecessor hashes; "
                "no factor-covariance execution here"
            ),
            "future_full_carried_word_and_mirror_trajectory": "mandatory science gate",
            "structural_upper_bound_cone_leakage": FIELD_ZERO_TOLERANCE,
            "cube_or_open_boundary_shell": FIELD_ZERO_TOLERANCE,
            "dynamic_band_floor": BAND_FLOOR,
            "dynamic_axial_seam_ceiling": AXIAL_SEAM_CEILING,
            "dynamic_contact_floor": CONTACT_FLOOR,
            "character_magnitude_floor": CHARACTER_MAGNITUDE_FLOOR,
        },
        "deletions_each_route": DELETIONS,
        "factor_deletions_require_observed_effect": True,
        "mediator_stream_deletion": {
            "maximum_mediator_displacement": RUNNER_TOLERANCE,
            "front_path_response": "<=row signal floor",
            "fixed_probe_response": "<=row signal floor",
        },
        "contact_probe_coin_disposition": {
            "route_A_comparison": "full-field and preregistered-primary distances reported separately",
            "route_A_dispositions": (
                "invalid", "coexistence-only", "full-field-sensitive", "primary-sensitive"
            ),
            "route_B_comparison": "maximum circular response-phasor chord distance",
            "sensitive": ">=route-specific comparison floor",
            "coexistence-only": "<comparison floor with valid structural deletion",
            "metadata_only_pass_forbidden": True,
            "primary_current_closure_requires_sensitivity": False,
            "load_bearing_primary_claim_requires_primary_sensitivity": True,
            "matched_free_uses_same_deletion": True,
        },
        "mirrored_control": "carried response agrees; lab x sign reverses",
        "ordinary_row_resource": {
            "seconds": ROW_WALL_CEILING_SECONDS, "RSS_bytes": ROW_RSS_CEILING_BYTES, "swaps": 0,
        },
        "route_C_mandatory_scout": {
            "only_row": "train implementation-resource-scout-sentinel",
            "seconds": ROUTE_C_SCOUT_WALL_CEILING_SECONDS,
            "RSS_bytes": ROUTE_C_SCOUT_RSS_CEILING_BYTES,
            "response_quarantined": True,
            "science_rows_counted": 0,
        },
        "future_authorization_gate": {
            "scout": (FUTURE_SCOUT_AUTHORIZATION_ENV, FUTURE_SCOUT_AUTHORIZATION_TOKEN),
            "train": (FUTURE_TRAIN_AUTHORIZATION_ENV, FUTURE_TRAIN_AUTHORIZATION_TOKEN),
            "dry_rejects_presence_even_empty": True,
            "selector": None,
            "refit": False,
        },
        "mass_scope": {
            "Cycle219_principal_fixture": "safe train branch only",
            "held_minus_8pi_over_9": "supplied M_plus factor coordinate; principal mass alias unresolved",
        },
    }
    emit("frozen leakage, deletion, lawful-domain, covariance-scope, and resource controls", requirements)


def no_go_discipline_contracts() -> None:
    walls = {
        "W_A": "post-CAR local-current evaluator and response",
        "W_B": "complete-word translation-character evaluator and response",
        "W_C": "Q6 computational operator/sparse/resource implementation, excluding A/B compiler",
        "W_AB_compile": "physical-M2 compilation of A/B composite factors",
        "W_source": "autonomous preparation and conserved normalization",
        "W_cal": "physical units and empirical observable calibration",
    }
    names = tuple(walls)
    pairs = tuple(
        {
            "left": names[left], "right": names[right],
            "closure_relation": "not-established",
            "independence_claimed": False,
        }
        for left in range(len(names)) for right in range(left + 1, len(names))
    )
    emit(
        "N2 separately tracked conditions; no closure relation established",
        {
            "walls": walls,
            "pairs": pairs,
            "pair_count": len(pairs),
            "negative_claim": False,
        },
    )


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle509 note exists and binds the executable", False, "missing note")
        return
    text = normalized(NOTE)
    required = (
        "formal pre-held contract only",
        "revision history and resource-evidence disposition",
        "declared historical identifiers only",
        "clean clone does not fail preflight",
        "contact[0.37]",
        "imported cycle230 coupling == 0.37",
        "emitter = 0.02 m_plus(source)",
        "collision = 0.02 m_plus(probe)",
        "post-car/pre-contact/pre-collision",
        "after the complete update word",
        "(1,2,1)/sqrt(6)",
        "j_x(c)=sum_yz[n_post(c,+x)-n_post(c-1,-x)]",
        "full field is retained",
        "aggregate norms are diagnostic only",
        "global direction current is diagnostic only",
        "global/nonlocal and phase-like",
        "unit response phasors",
        "linear principal-angle deletion cut",
        "r_a = max_t |delta_j_front(c_t,t)|",
        "r_b = max_t |u_t-1|",
        "s_swap = abs(log((r(m_s,m_p)/r(m_p,m_s)) /(f(m_s,m_p)/f(m_p,m_s))))",
        "mirrored geometry",
        "fixed incoming cuts",
        "frame_cell",
        "structural upper-bound cone",
        "numerical block pruning cannot certify this cone",
        "zero source factor",
        "positive source / zero probe",
        "positive-positive held rows",
        "null fixed-probe and front-path response",
        "primary-sensitive",
        "full-field-sensitive",
        "coexistence-only",
        "primary current closure does not require contact or probe-coin sensitivity",
        "source-ledger tolerance",
        "local bond-field-definition covariance",
        "inherited certificate identities bound by exact predecessor hashes",
        "full carried-word covariance",
        "cycle509_scout_authorization",
        "cycle509_train_authorization",
        "dry/contract mode rejects the presence of either token",
        "even an explicitly empty authorization variable is rejected",
        "held row menu, roles, and count remain unchanged",
        "separately tracked; no closure relation established",
        "negative_claim=false",
        "route c implementation is not complete",
        "no science train",
        "no held evolution",
        "no refit",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = tuple(value for value in required if value not in text)
    match = re.search(r"preflight runner sha256:\s*([0-9a-f]{64})", text)
    declared = match.group(1) if match else None
    check(
        "the note binds exact factors, observables, scope, and runner hash",
        not missing and declared == file_sha(Path(__file__)),
        {"missing": missing, "declared_runner_sha256": declared, "actual_runner_sha256": file_sha(Path(__file__))},
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=CLI_MODES, required=True)
    arguments = parser.parse_args()
    if arguments.mode != "contract-preflight":
        raise SystemExit("Cycle509 exposes cheap contract-preflight only")
    reject_authorization_environment(os.environ)
    check(
        "contract-preflight starts with both future authorization variables absent",
        present_authorization_variables(os.environ) == (),
        {
            "checked_by_environment_membership": (
                FUTURE_SCOUT_AUTHORIZATION_ENV, FUTURE_TRAIN_AUTHORIZATION_ENV
            ),
            "empty_value_counts_as_present": True,
        },
    )
    print("CYCLE509 REVISION", REVISION, "FORMAL PRE-HELD CONTRACT ONLY")
    print("AUTHORITY", AUTHORITY, "AUDIT", AUDIT)
    factor_contracts()
    current_field_contracts()
    geometry_contracts()
    causal_cone_contracts()
    observable_and_classifier_contracts()
    train, held = manifest_contracts()
    domain_deletion_resource_contracts()
    no_go_discipline_contracts()
    note_contract()
    print("MANIFEST_SUMMARY", {
        "train_rows": len(train), "held_rows_contract_only": len(held),
        "train_sha256": manifest_digest(train), "held_sha256": manifest_digest(held),
        "science_train_rows_executed": 0, "held_rows_executed": 0, "refit": False,
    })
    print("RESOURCE_PRECHECK", {
        "maximum_RSS_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if sys.platform == "darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024,
        "swaps": resource.getrusage(resource.RUSAGE_SELF).ru_nswap,
    })
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "science_rows": 0, "held_rows": 0})
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
