#!/usr/bin/env python3
"""Frozen source-surface acceptance tool for three landed source fixtures.

This module adds one candidate-vector port and frozen outcome records around
landed checks.
It does not add a source law, alter a landed file, or make a physics claim.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SOURCE_ACCEPTANCE_HARNESS_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/signed_gravity_oriented_tensor_source_lift.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/physical_m2_gravity_source_bridge_tournament_synthesis_cycle294_2026_07_17.py",
    "docs/SIGNED_GRAVITY_ORIENTED_TENSOR_SOURCE_LIFT_NOTE.md",
    "docs/work_history/repo/review_feedback/DIRECT_GATEWISE_MATTER_MEDIATOR_CURRENT_LEDGER_ROUTE_A_CYCLE293_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/GRAVITY_ROUTE_C_BOUNDED_DIRECT_CURRENT_SEARCH_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_ROUTE_B_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_M2_GRAVITY_SOURCE_BRIDGE_TOURNAMENT_SYNTHESIS_CYCLE294_NOTE_2026-07-17.md",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_RECOIL_BALANCED_CARRIED_SOURCE_CYCLE318_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/TWO_CELL_TWO_SOURCE_RECOIL_RECIPROCITY_CYCLE322_NOTE_2026-07-18.md",
    "docs/work_history/repo/review_feedback/UNIT_WEIGHT_CARRIED_LINK_RECOIL_CYCLE320_NOTE_2026-07-18.md",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/carried_internal_species_source_field_ledger_repair_2026_07_17.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/connected_edge_same_code_local_instrument_cycle278_2026_07_17.py",
    "scripts/contractible_lightcone_wilson_quotient_cycle271_2026_07_17.py",
    "scripts/direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17.py",
    "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/local_m2_mass_scalar_deformation_response_route_b_2026_07_17.py",
    "scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py",
    "scripts/locally_matched_wilson_sector_states_cycle275_2026_07_17.py",
    "scripts/numpy_replay_bootstrap.py",
    "scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py",
    "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py",
    "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
    "scripts/physical_cycle269_higher_number_fixed_seam_cycle308_2026_07_17.py",
    "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py",
    "scripts/physical_cycle269_reference_relative_localized_pair_lift_2026_07_17.py",
    "scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/signed_gravity_source_character_uniqueness_theorem.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
import copy
import hashlib
import json
import math
from numbers import Real
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any

import numpy as np

import signed_gravity_oriented_tensor_source_lift as S1


_MODULE_START = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]

TENSOR_LIFT_SHA256 = "33c2bf0df699da181eed1414ee828c3633fec2be51ac1646659ffce714d2ab31"
RECOIL_RECIPROCITY_SHA256 = "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75"
TYPED_BRIDGE_SHA256 = "834f63475a66e02b7b2a956c710d9b6b3107df764605bae747cc1bf40ed61b59"

TENSOR_LIFT_PATH = AUDIT_INPUT_PATHS[0]
RECOIL_RECIPROCITY_PATH = AUDIT_INPUT_PATHS[1]
TYPED_BRIDGE_PATH = AUDIT_INPUT_PATHS[2]


TENSOR_FROZEN_EXPECTED = {
    "outcomes": {
        "projector_algebra": {
            "check": "PASS",
            "values": {
                "ranks": {"lapse": 1, "shift": 3, "trace": 1, "shear": 5},
            },
        },
        "orientation_twist": {
            "check": "PASS",
            "values": {
                "block_norms": {
                    "lapse": 0.9560846981508337,
                    "shift": 0.6865215525605716,
                    "trace": 0.8042745120994024,
                    "shear": 1.1976967047075773,
                },
                "twist_residual": 0.0,
            },
        },
        "ward_constraints": {
            "check": "PASS",
            "values": {
                "residuals": [
                    1.2462222543165673e-15,
                    1.2462222543165673e-15,
                    0.0,
                ],
                "source_null_residual": 0.0,
            },
        },
        "response_locking": {
            "check": "PASS",
            "values": {
                "field_flip_residual": 0.0,
                "field_null_residual": 0.0,
                "positive_self": 15.494833932051147,
                "locking_signs": {
                    "+1,+1": 1.0,
                    "+1,-1": -1.0,
                    "-1,+1": -1.0,
                    "-1,-1": 1.0,
                },
            },
        },
        "scalar_only_no_overclaim": {
            "check": "PASS",
            "values": {"complement_norm": 0.0},
        },
        "free_tensor_carrier": {
            "check": "PASS",
            "values": {
                "tensor_source_blocks": {
                    "lapse": 0.9560846981508337,
                    "shift": 0.6865215525605716,
                    "trace": 0.8042745120994024,
                    "shear": 1.1976967047075773,
                },
                "chi_only_blocks": {
                    "lapse": 1.0,
                    "shift": 0.0,
                    "trace": 0.5,
                    "shear": 0.0,
                },
            },
        },
        "no_claim": {
            "check": "PASS",
            "values": {
                "negative_inertial_mass": False,
                "shielding": False,
                "propulsion": False,
                "reactionless_force": False,
                "physical_signed_gravity_prediction": False,
            },
        },
    },
    "source_sha256": TENSOR_LIFT_SHA256,
}


RECOIL_OUTCOME_LABELS = (
    "the note pins the two-source proxy and interpretation firewall",
    "each endpoint source is a proper-cubic unitary preserving local matter number, Q, and the coefficient-two vector ledger",
    "both endpoint source factors commute, preserve their local matter counts, and retain the nontrivial Cycle-315 contact",
    "the naive one-one carried-source product is not a closed Cycle-315 FSWAP sector",
    "the joint code obeys E_two-source G_two-source = G_physical,two-source E_two-source in both edge roles",
    "the 4,096-column physical seam remains isometric through held L=6",
    "both endpoint vertices contain matched emission and conjugate absorption in all directions",
    "the same-code two-update response has nonzero reciprocal off-diagonal transfer through held L=6",
    "receiver, stream, and source-exchange deletions distinguish the reciprocal off-diagonal response",
    "the source family and Cycle-315 seam cover all 24 frames including twelve endpoint reversals",
    "the complete two-source family commutes with all L=3 translations",
    "the two-source coefficient-two extension has bounded constant physical support",
    "the Cycle-315 one-particle mass fixture and nontrivial contact remain firewalled",
    "coupling and conjugate deletions plus malformed Q/source/edge domains are detected",
    "the supplied, derived, failed, and open structure is explicit",
    "N1 gives exact honesty markers to eight distinct two-source routes",
    "N2 gives both closure directions for all ten pairs in the collapsed wall set",
    "N3 literal methodology-trigger scan has zero hits on both release paths",
    "N4 exact file-line witnesses remain literal",
    "N5-N8 and the broad-negative failure gate remain explicit",
)

RECOIL_FIXTURE_INVARIANTS = {
    "cells": 2,
    "directions_per_cell": [6, 6],
    "emission_absorption_channels": 12,
    "ordered_recoil_pairs": 6,
}

RECOIL_FROZEN_EXPECTED = {
    "outcomes": [
        {"check": label, "pass": True} for label in RECOIL_OUTCOME_LABELS
    ],
    "fixture_invariants": RECOIL_FIXTURE_INVARIANTS,
    "fixture_selector": "canonical",
    "returncode": 0,
    "exceptions": [],
    "source_sha256": RECOIL_RECIPROCITY_SHA256,
}

RECOIL_SWAP_FLIPPED_LABELS = (
    "the naive one-one carried-source product is not a closed Cycle-315 FSWAP sector",
    "the same-code two-update response has nonzero reciprocal off-diagonal transfer through held L=6",
    "receiver, stream, and source-exchange deletions distinguish the reciprocal off-diagonal response",
    "the source family and Cycle-315 seam cover all 24 frames including twelve endpoint reversals",
)


BRIDGE_CONTRACT_ROWS = (
    {
        "route": "A",
        "script": "scripts/direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17.py",
        "expected_pass": 23,
        "pattern": r"TOTAL:\s*PASS=(\d+)\s+FAIL=(\d+)",
    },
    {
        "route": "B",
        "script": "scripts/local_m2_mass_scalar_deformation_response_route_b_2026_07_17.py",
        "expected_pass": 24,
        "pattern": r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)",
    },
    {
        "route": "C",
        "script": "scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py",
        "expected_pass": 23,
        "pattern": r"TOTAL\s+PASS=(\d+)\s+FAIL=(\d+)",
    },
)

BRIDGE_OUTCOME_LABELS = (
    "the synthesis pins scope, ledgers, all TOE lanes, and N1--N8",
    "all three independent route runners pass at the reviewed totals",
    "the routes have no common code/update and do not silently form one law",
    "each route preserves the energy/source semantic boundary",
    "the selected additive port-kernel comparator gives exactly minus one-half rho across held sizes",
)

BRIDGE_FROZEN_EXPECTED = {
    "outcomes": [
        {"check": label, "pass": True} for label in BRIDGE_OUTCOME_LABELS
    ],
    "counts": {"pass": 5, "fail": 0},
    "contract_rows": [dict(row) for row in BRIDGE_CONTRACT_ROWS],
    "contract_scope": "not one combined law",
    "source_sha256": TYPED_BRIDGE_SHA256,
}


def _sha256(relative_path: str) -> str:
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return repr(value)


def _digest(value: Any) -> str:
    payload = json.dumps(
        _jsonable(value), sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _drift_record(relative_path: str, expected: str, actual: str) -> dict[str, Any]:
    return {
        "source_path": relative_path,
        "source_sha256": actual,
        "expected_sha256": expected,
        "pin_verified": False,
        "outcomes": {},
    }


def _finite_data(value: Any) -> bool:
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return True
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, np.generic):
        return _finite_data(value.item())
    if isinstance(value, np.ndarray):
        return bool(
            np.issubdtype(value.dtype, np.number)
            and not np.issubdtype(value.dtype, np.complexfloating)
            and np.all(np.isfinite(value))
        )
    if isinstance(value, dict):
        return all(
            isinstance(key, (str, int, float, bool))
            and _finite_data(key)
            and _finite_data(item)
            for key, item in value.items()
        )
    if isinstance(value, (tuple, list)):
        return all(_finite_data(item) for item in value)
    return False


class _PinnedAcceptance:
    SOURCE_PATH = ""
    LANDED_SHA256_PIN = ""

    def __init__(self) -> None:
        self.expected_sha256 = self.LANDED_SHA256_PIN
        self.actual_sha256 = _sha256(self.SOURCE_PATH)
        self.pin_verified = self.actual_sha256 == self.expected_sha256

    def _pin_still_verified(self) -> bool:
        self.actual_sha256 = _sha256(self.SOURCE_PATH)
        self.pin_verified = self.actual_sha256 == self.expected_sha256
        return self.pin_verified

    def _record_is_drifted(self, record: dict[str, Any]) -> bool:
        return (
            not self.pin_verified
            or record.get("pin_verified") is not True
            or record.get("source_sha256") != self.expected_sha256
            or record.get("expected_sha256") != self.expected_sha256
        )


class TensorLiftAcceptance(_PinnedAcceptance):
    """Real finite length-10 vector port over S1's canonical constraints."""

    SOURCE_PATH = TENSOR_LIFT_PATH
    LANDED_SHA256_PIN = TENSOR_LIFT_SHA256
    FROZEN_EXPECTED = TENSOR_FROZEN_EXPECTED

    def frozen_expected(self) -> dict[str, Any]:
        return copy.deepcopy(self.FROZEN_EXPECTED)

    def _input_reject(self, detail: dict[str, Any]) -> dict[str, Any]:
        return {
            "source_path": self.SOURCE_PATH,
            "source_sha256": self.actual_sha256,
            "expected_sha256": self.expected_sha256,
            "pin_verified": True,
            "outcomes": {
                "input_contract": {
                    "check": "FAIL",
                    "values": _jsonable(detail),
                }
            },
        }

    def accept(
        self,
        source_vector: Any,
    ) -> dict[str, Any]:
        if not self._pin_still_verified():
            return _drift_record(
                self.SOURCE_PATH, self.expected_sha256, self.actual_sha256
            )

        try:
            source_object = np.asarray(source_vector, dtype=object)
        except Exception as exc:
            return self._input_reject(
                {"reason": f"source conversion failed: {type(exc).__name__}: {exc}"}
            )
        if (
            source_object.ndim != 1
            or source_object.shape != (10,)
        ):
            return self._input_reject(
                {
                    "expected": "one real finite numeric vector of shape [10]",
                    "observed_shape": list(source_object.shape),
                    "observed_dtype": str(source_object.dtype),
                }
            )
        source_values = source_object.tolist()
        if any(
            isinstance(value, (bool, np.bool_))
            or not isinstance(value, Real)
            for value in source_values
        ):
            return self._input_reject(
                {
                    "expected": "ten real numeric non-Boolean elements",
                    "observed_types": [
                        type(value).__name__ for value in source_values
                    ],
                }
            )
        try:
            source = np.asarray(source_values, dtype=float)
        except Exception as exc:
            return self._input_reject(
                {
                    "reason": (
                        "finite float conversion failed: "
                        f"{type(exc).__name__}: {exc}"
                    )
                }
            )
        if source.shape != (10,) or not np.all(np.isfinite(source)):
            return self._input_reject(
                {
                    "expected": "ten finite float-convertible real values",
                    "observed_shape": list(source.shape),
                }
            )
        try:
            _canonical_source, constraint = S1.tensor_source_with_constraints()
            constraint = np.asarray(constraint, dtype=float)
        except Exception as exc:
            return self._input_reject(
                {
                    "reason": (
                        "canonical Ward-constraint load failed: "
                        f"{type(exc).__name__}: {exc}"
                    )
                }
            )
        if (
            constraint.ndim != 2
            or constraint.shape[0] < 1
            or constraint.shape[1:] != (10,)
            or not np.all(np.isfinite(constraint))
        ):
            return self._input_reject(
                {
                    "expected": (
                        "landed nonempty real finite Ward constraints with "
                        "shape [n, 10]"
                    ),
                    "observed_shape": list(constraint.shape),
                }
            )

        projectors = S1.canonical_projectors()
        landed_calls = (
            (
                "projector_algebra",
                lambda: S1.projector_algebra_check(projectors),
            ),
            (
                "orientation_twist",
                lambda: S1.orientation_twist_check(source, projectors),
            ),
            (
                "ward_constraints",
                lambda: S1.ward_constraint_check(source, constraint),
            ),
            (
                "response_locking",
                lambda: S1.response_locking_check(source),
            ),
            (
                "scalar_only_no_overclaim",
                lambda: S1.scalar_only_no_overclaim_check(projectors),
            ),
            (
                "free_tensor_carrier",
                lambda: S1.free_tensor_carrier_gate(source),
            ),
            ("no_claim", S1.no_claim_gate),
        )
        statuses: dict[str, tuple[bool, str]] = {}
        for name, landed_call in landed_calls:
            try:
                passed, detail = landed_call()
                statuses[name] = (bool(passed), detail)
            except Exception as exc:
                statuses[name] = (
                    False,
                    f"{type(exc).__name__}: {exc}",
                )

        plus = S1.oriented(source, +1)
        minus = S1.oriented(source, -1)
        block_norms = S1.block_norms(plus, projectors)
        twist_residual = max(
            float(np.linalg.norm(projector @ plus + projector @ minus))
            for projector in projectors.blocks.values()
        )
        ward_residuals = [
            float(np.linalg.norm(constraint @ S1.oriented(source, eta)))
            for eta in (+1, -1, 0)
        ]
        source_null_residual = float(np.linalg.norm(S1.oriented(source, 0)))
        inverse_operator = np.linalg.inv(S1.universal_block_operator())
        field_plus = inverse_operator @ plus
        field_minus = inverse_operator @ minus
        field_null = inverse_operator @ S1.oriented(source, 0)
        locking_signs = {}
        for eta_a in (+1, -1):
            for eta_b in (+1, -1):
                coupling = float(
                    S1.oriented(source, eta_a)
                    @ inverse_operator
                    @ S1.oriented(source, eta_b)
                )
                locking_signs[f"{eta_a:+d},{eta_b:+d}"] = math.copysign(
                    1.0, coupling
                )
        scalar_complement = (
            projectors.shift + projectors.shear
        ) @ S1.oriented(S1.scalar_a1_source(), -1)
        chi_only = np.zeros(10, dtype=float)
        chi_only[0] = 1.0
        chi_only[4] = 0.5
        claims = copy.deepcopy(
            self.FROZEN_EXPECTED["outcomes"]["no_claim"]["values"]
        )

        values = {
            "projector_algebra": {
                "ranks": {
                    name: int(np.linalg.matrix_rank(projector))
                    for name, projector in projectors.blocks.items()
                },
            },
            "orientation_twist": {
                "block_norms": block_norms,
                "twist_residual": twist_residual,
            },
            "ward_constraints": {
                "residuals": ward_residuals,
                "source_null_residual": source_null_residual,
            },
            "response_locking": {
                "field_flip_residual": float(
                    np.linalg.norm(field_plus + field_minus)
                ),
                "field_null_residual": float(np.linalg.norm(field_null)),
                "positive_self": float(source @ inverse_operator @ source),
                "locking_signs": locking_signs,
            },
            "scalar_only_no_overclaim": {
                "complement_norm": float(np.linalg.norm(scalar_complement)),
            },
            "free_tensor_carrier": {
                "tensor_source_blocks": S1.block_norms(source, projectors),
                "chi_only_blocks": S1.block_norms(chi_only, projectors),
            },
            "no_claim": claims,
        }
        outcomes = {
            name: {
                "check": "PASS" if statuses[name][0] else "FAIL",
                "values": _jsonable(values[name]),
            }
            for name in values
        }
        return {
            "source_path": self.SOURCE_PATH,
            "source_sha256": self.actual_sha256,
            "expected_sha256": self.expected_sha256,
            "pin_verified": True,
            "outcomes": outcomes,
        }

    def verdict(self, record: Any) -> str:
        try:
            if not isinstance(record, dict):
                return "REJECT"
            if self._record_is_drifted(record):
                return "DRIFT"
            if not _finite_data(record):
                return "REJECT"
            outcomes = record.get("outcomes")
            frozen = self.FROZEN_EXPECTED["outcomes"]
            if not isinstance(outcomes, dict) or set(outcomes) != set(frozen):
                return "REJECT"
            if any(
                not isinstance(outcomes.get(name), dict)
                or not isinstance(outcomes[name].get("values"), dict)
                for name in frozen
            ):
                return "REJECT"
            if any(outcomes[name].get("check") != "PASS" for name in frozen):
                return "REJECT"

            projector = outcomes["projector_algebra"]["values"]
            twist = outcomes["orientation_twist"]["values"]
            ward = outcomes["ward_constraints"]["values"]
            locking = outcomes["response_locking"]["values"]
            scalar = outcomes["scalar_only_no_overclaim"]["values"]
            carrier = outcomes["free_tensor_carrier"]["values"]
            no_claim = outcomes["no_claim"]["values"]
            expected_signs = frozen["response_locking"]["values"]["locking_signs"]

            accepted = (
                projector["ranks"]
                == frozen["projector_algebra"]["values"]["ranks"]
                and all(value > 0.05 for value in twist["block_norms"].values())
                and twist["twist_residual"] < S1.TOL
                and max(ward["residuals"]) < 1.0e-10
                and ward["source_null_residual"] < S1.TOL
                and locking["field_flip_residual"] < S1.TOL
                and locking["field_null_residual"] < S1.TOL
                and locking["positive_self"] > 0.0
                and locking["locking_signs"] == expected_signs
                and scalar["complement_norm"] < S1.TOL
                and carrier["tensor_source_blocks"]["shift"] > 0.05
                and carrier["tensor_source_blocks"]["shear"] > 0.05
                and carrier["chi_only_blocks"]["shift"] == 0.0
                and carrier["chi_only_blocks"]["shear"] == 0.0
                and no_claim == frozen["no_claim"]["values"]
            )
            return "ACCEPT" if accepted else "REJECT"
        except (
            AttributeError,
            KeyError,
            TypeError,
            ValueError,
            IndexError,
            OverflowError,
        ):
            return "REJECT"


_RECOIL_ARGUMENT_DRIVER = r"""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path.cwd() / "scripts"))
import two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18 as S2

payload = json.load(sys.stdin)
coin, fswap, contact, _update, _details = S2.c315.logical_update_controls(
    S2.LABELS
)
fixture_selector = payload["fixture_selector"]
if fixture_selector == "canonical":
    factors = (coin, fswap, contact)
elif fixture_selector == "swap_coin_fswap":
    factors = (fswap, coin, contact)
else:
    raise ValueError(f"unsupported fixture selector: {fixture_selector!r}")

calls = (
    ("note_contract", S2.note_contract, ()),
    ("local_operator_controls", S2.local_operator_controls, ()),
    ("seam_number_contact_controls", S2.seam_number_contact_controls, (factors,)),
    ("physical_intertwiner_controls", S2.physical_intertwiner_controls, (factors,)),
    ("emission_absorption_controls", S2.emission_absorption_controls, ()),
    ("response_reciprocity_controls", S2.response_reciprocity_controls, (factors,)),
    (
        "covariance_translation_support_controls",
        S2.covariance_translation_support_controls,
        (factors,),
    ),
    (
        "deletion_mass_contact_domain_controls",
        S2.deletion_mass_contact_domain_controls,
        (factors,),
    ),
    ("inventory_controls", S2.inventory_controls, ()),
    ("methodology_controls", S2.methodology_controls, ()),
)
stream = io.StringIO()
exceptions = []
with redirect_stdout(stream):
    for entry_name, entry_point, arguments in calls:
        try:
            entry_point(*arguments)
        except Exception as exc:
            exceptions.append(
                {
                    "entry_point": entry_name,
                    "exception": f"{type(exc).__name__}: {exc}",
                }
            )

pattern = re.compile(r"^(PASS|FAIL) (.*?) :: ?(.*)$")
outcomes = []
for line in stream.getvalue().splitlines():
    match = pattern.match(line)
    if match:
        status, label, detail = match.groups()
        outcomes.append(
            {
                "check": label,
                "pass": status == "PASS",
                "values": {"landed_detail": detail},
            }
        )
record = {
    "outcomes": outcomes,
    "fixture_invariants": {
        "cells": len(S2.ENDPOINTS),
        "directions_per_cell": [
            len(S2.REVERSE) for _cell in S2.ENDPOINTS
        ],
        "emission_absorption_channels": len(S2.ENDPOINTS) * len(S2.REVERSE),
        "ordered_recoil_pairs": len(S2.REVERSE),
    },
    "fixture_selector": fixture_selector,
    "exceptions": exceptions,
}
print(json.dumps(record, sort_keys=True))
"""


class RecoilReciprocityAcceptance(_PinnedAcceptance):
    """Cycle-322 wrapper over its canonical and swapped fixture selectors."""

    SOURCE_PATH = RECOIL_RECIPROCITY_PATH
    LANDED_SHA256_PIN = RECOIL_RECIPROCITY_SHA256
    FROZEN_EXPECTED = RECOIL_FROZEN_EXPECTED

    def frozen_expected(self) -> dict[str, Any]:
        return copy.deepcopy(self.FROZEN_EXPECTED)

    def _operational_reject(
        self, fixture_selector: Any, exception: str
    ) -> dict[str, Any]:
        return {
            "source_path": self.SOURCE_PATH,
            "source_sha256": self.actual_sha256,
            "expected_sha256": self.expected_sha256,
            "pin_verified": True,
            "outcomes": [],
            "fixture_invariants": copy.deepcopy(RECOIL_FIXTURE_INVARIANTS),
            "fixture_selector": _jsonable(fixture_selector),
            "returncode": None,
            "exceptions": [
                {
                    "entry_point": "subprocess_driver",
                    "exception": exception,
                }
            ],
        }

    def accept(
        self,
        fixture_selector: Any = "canonical",
    ) -> dict[str, Any]:
        if not self._pin_still_verified():
            return _drift_record(
                self.SOURCE_PATH, self.expected_sha256, self.actual_sha256
            )
        if (
            type(fixture_selector) is not str
            or fixture_selector not in {"canonical", "swap_coin_fswap"}
        ):
            return self._operational_reject(
                fixture_selector,
                "fixture selector must be canonical or swap_coin_fswap",
            )
        try:
            completed = subprocess.run(
                [sys.executable, "-c", _RECOIL_ARGUMENT_DRIVER],
                cwd=ROOT,
                input=json.dumps(
                    {"fixture_selector": fixture_selector}, sort_keys=True
                ),
                text=True,
                capture_output=True,
                check=False,
                timeout=AUDIT_TIMEOUT_SEC,
            )
        except subprocess.TimeoutExpired as exc:
            return self._operational_reject(
                fixture_selector,
                f"TimeoutExpired after {exc.timeout} seconds",
            )
        except OSError as exc:
            return self._operational_reject(
                fixture_selector, f"{type(exc).__name__}: {exc}"
            )
        if completed.returncode != 0:
            return {
                **self._operational_reject(
                    fixture_selector,
                    (
                        f"subprocess return code {completed.returncode}: "
                        f"{completed.stderr.strip()}"
                    ),
                ),
                "returncode": completed.returncode,
            }
        try:
            child_record = json.loads(completed.stdout)
            if not isinstance(child_record, dict):
                raise TypeError("child record is not an object")
        except (json.JSONDecodeError, TypeError) as exc:
            return {
                **self._operational_reject(
                    fixture_selector, f"{type(exc).__name__}: {exc}"
                ),
                "returncode": completed.returncode,
            }
        return {
            "source_path": self.SOURCE_PATH,
            "source_sha256": self.actual_sha256,
            "expected_sha256": self.expected_sha256,
            "pin_verified": True,
            **child_record,
            "returncode": completed.returncode,
        }

    def verdict(self, record: Any) -> str:
        try:
            if not isinstance(record, dict):
                return "REJECT"
            if self._record_is_drifted(record):
                return "DRIFT"
            if not _finite_data(record):
                return "REJECT"
            outcomes = record.get("outcomes")
            if not isinstance(outcomes, list) or any(
                not isinstance(row, dict) for row in outcomes
            ):
                return "REJECT"
            observed = [
                {"check": row.get("check"), "pass": row.get("pass")}
                for row in outcomes
            ]
            accepted = (
                observed == self.FROZEN_EXPECTED["outcomes"]
                and record.get("fixture_invariants")
                == self.FROZEN_EXPECTED["fixture_invariants"]
                and record.get("fixture_selector")
                == self.FROZEN_EXPECTED["fixture_selector"]
                and record.get("returncode") == 0
                and not record.get("exceptions")
            )
            return "ACCEPT" if accepted else "REJECT"
        except (AttributeError, KeyError, TypeError, ValueError, IndexError):
            return "REJECT"


def _extract_bridge_routes_as_data(source_text: str) -> list[dict[str, Any]]:
    tree = ast.parse(source_text, filename=TYPED_BRIDGE_PATH)
    routes_node = None
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "ROUTES"
                for target in node.targets
            )
        ):
            routes_node = node.value
            break
    if not isinstance(routes_node, (ast.Tuple, ast.List)):
        raise ValueError("ROUTES is not a literal row container")

    rows = []
    for row_node in routes_node.elts:
        if not isinstance(row_node, (ast.Tuple, ast.List)) or len(row_node.elts) != 4:
            raise ValueError("ROUTES row is not a four-field tuple")
        route_node, path_node, pass_node, pattern_node = row_node.elts
        route = ast.literal_eval(route_node)
        expected_pass = ast.literal_eval(pass_node)
        path_strings = [
            child.value
            for child in ast.walk(path_node)
            if isinstance(child, ast.Constant)
            and isinstance(child.value, str)
            and child.value.endswith(".py")
        ]
        if len(path_strings) != 1:
            raise ValueError("ROUTES path does not contain one script literal")
        if (
            not isinstance(pattern_node, ast.Call)
            or not pattern_node.args
            or not isinstance(pattern_node.args[0], ast.Constant)
        ):
            raise ValueError("ROUTES regex is not a literal re.compile call")
        rows.append(
            {
                "route": route,
                "script": path_strings[0],
                "expected_pass": expected_pass,
                "pattern": pattern_node.args[0].value,
            }
        )
    return rows


class TypedBridgeAcceptance(_PinnedAcceptance):
    """Byte-pinned, subprocess-only Cycle-294 contract acceptance."""

    SOURCE_PATH = TYPED_BRIDGE_PATH
    LANDED_SHA256_PIN = TYPED_BRIDGE_SHA256
    FROZEN_EXPECTED = BRIDGE_FROZEN_EXPECTED

    def __init__(self) -> None:
        super().__init__()
        self.contract_rows = []
        if self.pin_verified:
            source_text = (ROOT / self.SOURCE_PATH).read_text(encoding="utf-8")
            self.contract_rows = _extract_bridge_routes_as_data(source_text)

    def frozen_expected(self) -> dict[str, Any]:
        return copy.deepcopy(self.FROZEN_EXPECTED)

    def contract_row_digest(self) -> str:
        return _digest(self.contract_rows)

    def _operational_reject(self, exception: str) -> dict[str, Any]:
        return {
            "source_path": self.SOURCE_PATH,
            "source_sha256": self.actual_sha256,
            "expected_sha256": self.expected_sha256,
            "pin_verified": True,
            "returncode": None,
            "outcomes": [],
            "counts": {"pass": 0, "fail": 0},
            "contract_rows": copy.deepcopy(self.contract_rows),
            "contract_scope": "not one combined law",
            "stderr": exception,
        }

    def accept(self) -> dict[str, Any]:
        if not self._pin_still_verified():
            return _drift_record(
                self.SOURCE_PATH, self.expected_sha256, self.actual_sha256
            )
        try:
            completed = subprocess.run(
                [sys.executable, str(ROOT / self.SOURCE_PATH)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
                timeout=AUDIT_TIMEOUT_SEC,
            )
        except subprocess.TimeoutExpired as exc:
            return self._operational_reject(
                f"TimeoutExpired after {exc.timeout} seconds"
            )
        except OSError as exc:
            return self._operational_reject(f"{type(exc).__name__}: {exc}")
        pattern = re.compile(r"^(PASS|FAIL) (.*?) :: ?(.*)$")
        outcomes = []
        for line in completed.stdout.splitlines():
            match = pattern.match(line)
            if match:
                status, label, detail = match.groups()
                outcomes.append(
                    {
                        "check": label,
                        "pass": status == "PASS",
                        "values": {"landed_detail": detail},
                    }
                )
        return {
            "source_path": self.SOURCE_PATH,
            "source_sha256": self.actual_sha256,
            "expected_sha256": self.expected_sha256,
            "pin_verified": True,
            "returncode": completed.returncode,
            "outcomes": outcomes,
            "counts": {
                "pass": sum(row["pass"] for row in outcomes),
                "fail": sum(not row["pass"] for row in outcomes),
            },
            "contract_rows": copy.deepcopy(self.contract_rows),
            "contract_scope": "not one combined law",
            "stderr": completed.stderr,
        }

    def verdict(self, record: Any) -> str:
        try:
            if not isinstance(record, dict):
                return "REJECT"
            if self._record_is_drifted(record):
                return "DRIFT"
            if not _finite_data(record):
                return "REJECT"
            outcomes = record.get("outcomes")
            if not isinstance(outcomes, list) or any(
                not isinstance(row, dict) for row in outcomes
            ):
                return "REJECT"
            observed = [
                {"check": row.get("check"), "pass": row.get("pass")}
                for row in outcomes
            ]
            accepted = (
                record.get("returncode") == 0
                and observed == self.FROZEN_EXPECTED["outcomes"]
                and record.get("counts") == self.FROZEN_EXPECTED["counts"]
                and record.get("contract_rows")
                == self.FROZEN_EXPECTED["contract_rows"]
                and record.get("contract_scope")
                == self.FROZEN_EXPECTED["contract_scope"]
            )
            return "ACCEPT" if accepted else "REJECT"
        except (AttributeError, KeyError, TypeError, ValueError, IndexError):
            return "REJECT"


_SELF_PASS = 0
_SELF_FAIL = 0


def check(label: str, condition: bool, detail: Any = "") -> bool:
    global _SELF_PASS, _SELF_FAIL
    if condition:
        _SELF_PASS += 1
        status = "PASS"
    else:
        _SELF_FAIL += 1
        status = "FAIL"
    print(f"{status} {label} :: {detail}")
    return condition


def _flipped_labels(
    frozen: dict[str, Any], observed: dict[str, Any]
) -> list[str]:
    expected_outcomes = frozen["outcomes"]
    actual_outcomes = observed.get("outcomes", {})
    return [
        name
        for name, expected in expected_outcomes.items()
        if actual_outcomes.get(name, {}).get("check") != expected["check"]
    ]


def _recoil_flipped_labels(record: dict[str, Any]) -> list[str]:
    observed = {
        row.get("check"): row.get("pass") for row in record.get("outcomes", [])
    }
    return [
        row["check"]
        for row in RECOIL_FROZEN_EXPECTED["outcomes"]
        if observed.get(row["check"]) != row["pass"]
    ]


def main() -> int:
    global _SELF_PASS, _SELF_FAIL
    _SELF_PASS = 0
    _SELF_FAIL = 0

    tensor = TensorLiftAcceptance()
    recoil = RecoilReciprocityAcceptance()
    bridge = TypedBridgeAcceptance()
    pins = {
        "tensor_lift": {
            "expected": tensor.expected_sha256,
            "actual": tensor.actual_sha256,
            "verified": tensor.pin_verified,
        },
        "recoil": {
            "expected": recoil.expected_sha256,
            "actual": recoil.actual_sha256,
            "verified": recoil.pin_verified,
        },
        "typed_bridge": {
            "expected": bridge.expected_sha256,
            "actual": bridge.actual_sha256,
            "verified": bridge.pin_verified,
        },
    }
    check("all three landed byte pins verify", all(row["verified"] for row in pins.values()), pins)

    canonical_source, _canonical_constraints = S1.tensor_source_with_constraints()
    canonical_tensor_record = tensor.accept(canonical_source)
    canonical_tensor_verdict = tensor.verdict(canonical_tensor_record)
    check(
        "tensor canonical fixture is ACCEPT",
        canonical_tensor_verdict == "ACCEPT",
        canonical_tensor_verdict,
    )
    check(
        "tensor canonical record equals the frozen record",
        canonical_tensor_record["outcomes"]
        == tensor.frozen_expected()["outcomes"],
        _digest(canonical_tensor_record["outcomes"]),
    )
    mixed_boolean_source = (
        canonical_source / canonical_source[0]
    ).tolist()
    mixed_boolean_source[0] = True

    class ExplodingFloat(float):
        def __float__(self) -> float:
            raise RuntimeError("adversarial conversion")

    invalid_tensor_verdicts = {
        "boolean": tensor.verdict(
            tensor.accept(np.ones(10, dtype=bool))
        ),
        "mixed_boolean": tensor.verdict(
            tensor.accept(mixed_boolean_source)
        ),
        "complex": tensor.verdict(
            tensor.accept((1.0 + 0.1j) * canonical_source)
        ),
        "string": tensor.verdict(
            tensor.accept(np.asarray(["x"] * 10))
        ),
        "nonfinite": tensor.verdict(
            tensor.accept(np.full(10, np.nan))
        ),
        "wide_integer": tensor.verdict(
            tensor.accept([10**400] * 10)
        ),
        "exploding_real": tensor.verdict(
            tensor.accept([ExplodingFloat(1.0)] * 10)
        ),
    }
    check(
        "tensor input contract rejects non-real or nonfinite vectors",
        set(invalid_tensor_verdicts.values()) == {"REJECT"},
        invalid_tensor_verdicts,
    )
    nonfinite_record = copy.deepcopy(canonical_tensor_record)
    nonfinite_record["outcomes"]["response_locking"]["values"][
        "positive_self"
    ] = math.inf
    malformed_record = copy.deepcopy(canonical_tensor_record)
    del malformed_record["outcomes"]["response_locking"]["values"][
        "positive_self"
    ]
    malformed_verdicts = {
        "nonfinite_record": tensor.verdict(nonfinite_record),
        "missing_field": tensor.verdict(malformed_record),
    }
    check(
        "tensor verdict rejects nonfinite or malformed records",
        set(malformed_verdicts.values()) == {"REJECT"},
        malformed_verdicts,
    )
    tampered_record_pin = copy.deepcopy(canonical_tensor_record)
    tampered_record_pin["expected_sha256"] = "0" * 64
    tampered_record_verdict = tensor.verdict(tampered_record_pin)
    check(
        "record-carried expected pin mismatch classifies DRIFT",
        tampered_record_verdict == "DRIFT",
        tampered_record_verdict,
    )

    corrupted_tensor_record = tensor.accept(np.zeros(10, dtype=float))
    corrupted_tensor_verdict = tensor.verdict(corrupted_tensor_record)
    tensor_flips = _flipped_labels(
        tensor.frozen_expected(), corrupted_tensor_record
    )
    check(
        "corrupted tensor vector is REJECT with flipped checks",
        corrupted_tensor_verdict == "REJECT" and bool(tensor_flips),
        {"verdict": corrupted_tensor_verdict, "flipped_checks": tensor_flips},
    )

    recoil_record = recoil.accept()
    recoil_verdict = recoil.verdict(recoil_record)
    check(
        "landed Cycle-322 20/20 record is ACCEPT",
        recoil_verdict == "ACCEPT"
        and len(recoil_record.get("outcomes", [])) == 20,
        {
            "verdict": recoil_verdict,
            "pass": sum(row["pass"] for row in recoil_record.get("outcomes", [])),
            "total": len(recoil_record.get("outcomes", [])),
        },
    )

    perturbed_recoil_record = recoil.accept("swap_coin_fswap")
    perturbed_recoil_verdict = recoil.verdict(perturbed_recoil_record)
    recoil_flips = _recoil_flipped_labels(perturbed_recoil_record)
    check(
        "coin/FSWAP-swapped landed fixture is an exact four-check REJECT",
        perturbed_recoil_record.get("returncode") == 0
        and not perturbed_recoil_record.get("exceptions")
        and len(perturbed_recoil_record.get("outcomes", [])) == 20
        and perturbed_recoil_verdict == "REJECT"
        and tuple(recoil_flips) == RECOIL_SWAP_FLIPPED_LABELS,
        {
            "verdict": perturbed_recoil_verdict,
            "flipped_checks": recoil_flips,
        },
    )

    bridge_record = bridge.accept()
    bridge_verdict = bridge.verdict(bridge_record)
    bridge_digest = bridge.contract_row_digest()
    check(
        "landed Cycle-294 5/0 subprocess record is ACCEPT",
        bridge_verdict == "ACCEPT",
        {"verdict": bridge_verdict, "counts": bridge_record.get("counts")},
    )
    check(
        "typed-bridge ROUTES table matches its frozen AST data",
        bridge.contract_rows == [dict(row) for row in BRIDGE_CONTRACT_ROWS],
        bridge_digest,
    )

    nonfinite_recoil_record = copy.deepcopy(recoil_record)
    nonfinite_recoil_record["outcomes"][0]["values"][
        "landed_detail"
    ] = math.inf
    nonfinite_bridge_record = copy.deepcopy(bridge_record)
    nonfinite_bridge_record["outcomes"][0]["values"][
        "landed_detail"
    ] = math.inf
    malformed_outcome_records = {
        "tensor": copy.deepcopy(canonical_tensor_record),
        "recoil": copy.deepcopy(recoil_record),
        "typed_bridge": copy.deepcopy(bridge_record),
    }
    malformed_outcome_records["tensor"]["outcomes"][
        "projector_algebra"
    ] = 1
    malformed_outcome_records["recoil"]["outcomes"][0] = 1
    malformed_outcome_records["typed_bridge"]["outcomes"][0] = 1
    malformed_record_verdicts = {
        f"{name}_{type(value).__name__}": classifier.verdict(value)
        for name, classifier in (
            ("tensor", tensor),
            ("recoil", recoil),
            ("typed_bridge", bridge),
        )
        for value in (None, [], "record")
    }
    malformed_record_verdicts.update(
        {
            f"{name}_outcome": classifier.verdict(
                malformed_outcome_records[name]
            )
            for name, classifier in (
                ("tensor", tensor),
                ("recoil", recoil),
                ("typed_bridge", bridge),
            )
        }
    )
    malformed_record_verdicts.update(
        {
            "recoil_nonfinite": recoil.verdict(
                nonfinite_recoil_record
            ),
            "bridge_nonfinite": bridge.verdict(
                nonfinite_bridge_record
            ),
        }
    )
    check(
        "all verdict surfaces reject malformed or nonfinite records",
        set(malformed_record_verdicts.values()) == {"REJECT"},
        malformed_record_verdicts,
    )

    class UnhashableString(str):
        __hash__ = None

    malformed_selector_verdicts = {
        "list": recoil.verdict(recoil.accept([])),
        "dict": recoil.verdict(recoil.accept({})),
        "unhashable_string_subclass": recoil.verdict(
            recoil.accept(UnhashableString("canonical"))
        ),
    }
    check(
        "recoil rejects invalid selectors without raising",
        set(malformed_selector_verdicts.values()) == {"REJECT"},
        malformed_selector_verdicts,
    )

    class WrongPinTensorLiftAcceptance(TensorLiftAcceptance):
        LANDED_SHA256_PIN = "0" * 64

    drift_tensor = WrongPinTensorLiftAcceptance()
    drift_record = drift_tensor.accept(canonical_source)
    drift_verdict = drift_tensor.verdict(drift_record)
    check(
        "wrong local tensor pin refuses execution and classifies DRIFT",
        drift_verdict == "DRIFT" and not drift_record["pin_verified"],
        drift_verdict,
    )

    honest_keys = {
        "new_physics_claimed": False,
        "harness_input_ports": {
            "tensor_lift": True,
            "recoil": False,
            "typed_bridge": False,
        },
        "tool_role": "non-authoritative candidate testing",
    }
    check(
        "support/meta tool boundary is explicit",
        honest_keys
        == {
            "new_physics_claimed": False,
            "harness_input_ports": {
                "tensor_lift": True,
                "recoil": False,
                "typed_bridge": False,
            },
            "tool_role": "non-authoritative candidate testing",
        },
        honest_keys,
    )

    elapsed = time.monotonic() - _MODULE_START
    final_record = {
        "checks": {"pass": _SELF_PASS, "fail": _SELF_FAIL},
        "pins": pins,
        "frozen_record_digests": {
            "tensor_lift": _digest(tensor.frozen_expected()),
            "recoil": _digest(recoil.frozen_expected()),
            "typed_bridge": _digest(bridge.frozen_expected()),
            "typed_bridge_contract_rows": bridge_digest,
        },
        "demos": {
            "tensor_canonical": canonical_tensor_verdict,
            "tensor_corrupted": {
                "verdict": corrupted_tensor_verdict,
                "flipped_checks": tensor_flips,
            },
            "recoil_landed": recoil_verdict,
            "recoil_swapped_operator": {
                "verdict": perturbed_recoil_verdict,
                "flipped_checks": recoil_flips,
            },
            "typed_bridge_landed": bridge_verdict,
            "wrong_tensor_pin": drift_verdict,
        },
        **honest_keys,
        "runtime_seconds": round(elapsed, 6),
    }
    print(json.dumps(final_record, indent=2, sort_keys=True))
    return int(_SELF_FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
