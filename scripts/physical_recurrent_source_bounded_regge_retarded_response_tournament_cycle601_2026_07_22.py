#!/usr/bin/env python3
"""Cycle 601: recurrent source, bounded Regge, and response tournament.

All three routes are finite algebraic or declared-role constructions.  No
route composes its operators, encoders, constraints, leakage checks, source
control, or response arithmetic from physical M2 primitives.  A layer schedule
is not physical time; a generator is not a rate; a modular word is not physical
stress, energy, or a gravitational field.  Authority is none and audit is
unset.
"""

from __future__ import annotations

import ast
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
import scipy
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as cycle219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as cycle210
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22 as cycle579


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECURRENT_SOURCE_BOUNDED_REGGE_RETARDED_RESPONSE_TOURNAMENT_"
    "CYCLE601_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-8
PASS = 0
FAIL = 0
START = perf_counter()

RUNTIME_IMPORT_PINS = {
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "7aab3d6bc8d9d8b44263bca7a5cc308534269abb88094b2dfe0a820b12df2400",
    "scripts/physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22.py":
        "435096b012faf4425ff27761e6690178caa9e14ffdcde5659cb5072771a036ea",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py":
        "d5392152d322ea8f3850d0345d6caa426db22ae7f7694775b4bd6388704c18a6",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py":
        "4ab857755b606d7ba7432179ed66de723ac31d3f66507cafa1168ab60d4965d6",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py":
        "464e5928b7c1e46c23e4010363b6bd8ff3d0e2379c6e5ecb46891010ef47a5a4",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py":
        "472e28c78901368629c8d9d6f614bb8fb3ea003639ac61d480d06941cdf6cb86",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py":
        "537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce",
}


EVIDENCE_DEPENDENCIES = {
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md":
        "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "docs/work_history/repo/review_feedback/PROPER_CUBIC_BOUND_OBJECT_EQUIVALENCE_CYCLE210_NOTE_2026-07-16.md":
        "c05aa08d1baa25a814f5ab583eb640822ea2fe6630f46da285de2fcd84d1285f",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
        "6fe73ca79366ad75fd9499b820b4e3a49833ba6919a8c8cd3ef4d44e403da0e3",
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":
        "5ba12c643c4f02355069e07dc4f8e7319bbb9374fd02a77505b9f635ef16135e",
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_cold_2026_07_22.txt":
        "80f69b699f955663609461e12f978500eb44f582092f6db0739b449161edbd0d",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGGE_FINITE_UPDATE_FRAME_SELECTION_TOURNAMENT_CYCLE579_NOTE_2026-07-22.md":
        "d3c7ff5984d6ba079396f8ff0e38566b9b0e37ef636d19f8ec4d1073791305f0",
    "outputs/physical_regge_finite_update_frame_selection_tournament_cycle579_receipt_2026_07_22.json":
        "6cdc99d5f68d3244e5dc9ea802f3874a29a603d0fafd0eed6f21b32ed334cba8",
    "outputs/physical_regge_finite_update_frame_selection_tournament_cycle579_cold_2026_07_22.txt":
        "035bd83bc3d322d66eb3cf20cf20a7753e913734dad7243e2824f9ec1f48884b",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "43e5b749702fba9551fab43a242f832b824fdbff54817b5206097f02ad146e55",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "f0f3ed6d41132625b8907cbcda8f105b7ec975e4b952562b45fe5b7d8e1b3a0e",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json":
        "3ae94267d43a668a178ef02ee37ab12608f302419a25b0a37deffd27e51be647",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_cold_2026_07_22.txt":
        "cef70862eff7d6f10d562a67e2e8fcab503b998de5e0dea63300f0883efe398f",
    "scripts/physical_mobile_composite_action_regge_quadrature_tournament_cycle596_2026_07_22.py":
        "f41d9f1de61017c8c33651ebcb131b3d869ec63ad41dfb10f3eeadd5baae188a",
    "docs/work_history/repo/review_feedback/PHYSICAL_MOBILE_COMPOSITE_ACTION_REGGE_QUADRATURE_TOURNAMENT_CYCLE596_NOTE_2026-07-22.md":
        "c09d820d15946c01f7a191f20416d00a43545fa232d68b92b4f7fc8e74fa41c7",
    "outputs/physical_mobile_composite_action_regge_quadrature_tournament_cycle596_cold_2026_07_22.txt":
        "8e3f93f240f73fd96a495b22582179c7d554da28a40eb580ff910214548cfe36",
    "scripts/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_2026_07_22.py":
        "5702ac74768c83bd97d0860ad827a5a66809c8bfbfafb2dd010982bcb917be51",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md":
        "065192627b0c56b59d75a0ea837f26179b76579aa3e0783bc020092f173963ac",
    "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_receipt_2026_07_22.json":
        "c8a27819fb1907d20aa9c73a7d66a2b8c0cc37b532da4686ef32a80996d909c1",
    "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_cold_2026_07_22.txt":
        "3a8d6990d8dfaabefe0f5cec08af83d14613507ca0712b993f39c49025bb8797",
}


DEPENDENCIES = {**RUNTIME_IMPORT_PINS, **EVIDENCE_DEPENDENCIES}
EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256 = "e048993163b600aeb65294b13bd2cd771883718ef053c2260b5296dd512e3207"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label,
          *(("::", detail) if detail != "" else ()))


def file_sha(relative: str) -> str:
    path = ROOT / relative
    return sha256(path.read_bytes()).hexdigest() if path.exists() else "MISSING"


def runtime_import_closure() -> tuple[str, ...]:
    scripts = ROOT / "scripts"
    modules = {path.stem: path for path in scripts.glob("*.py")}
    entry = Path(__file__).resolve()
    visited: set[Path] = set()

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        visited.add(path)
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            names: tuple[str, ...] = ()
            if isinstance(node, ast.Import):
                names = tuple(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = (node.module.split(".")[0],)
            for name in names:
                if name in modules:
                    visit(modules[name])

    visit(entry)
    return tuple(sorted(str(path.relative_to(ROOT)) for path in visited if path != entry))


def runtime_import_controls() -> dict:
    closure = runtime_import_closure()
    observed = {path: file_sha(path) for path in closure}
    payload = "".join(f"{path}\0{observed[path]}\n" for path in closure)
    manifest = sha256(payload.encode("utf-8")).hexdigest()
    direct = (
        "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
        "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
        "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
        "scripts/physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22.py",
    )
    return {
        "direct_runtime_imports": direct,
        "complete_runtime_import_closure": closure,
        "hidden_runtime_imports": tuple(path for path in closure if path not in direct),
        "expected_sha256": RUNTIME_IMPORT_PINS,
        "observed_sha256": observed,
        "closure_manifest_sha256": manifest,
        "expected_closure_manifest_sha256": EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256,
        "pass": (
            closure == tuple(sorted(RUNTIME_IMPORT_PINS))
            and observed == RUNTIME_IMPORT_PINS
            and manifest == EXPECTED_RUNTIME_CLOSURE_MANIFEST_SHA256
        ),
    }


def cold_report(path: Path) -> dict:
    for prefix in ("REPORT_JSON ", "RECEIPT "):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith(prefix):
                return json.loads(line[len(prefix):])
    raise ValueError(f"report JSON missing from {path}")


def shore() -> dict:
    observed = {name: file_sha(name) for name in DEPENDENCIES}
    imports = runtime_import_controls()
    c576 = json.loads((ROOT / "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json").read_text())
    c579 = json.loads((ROOT / "outputs/physical_regge_finite_update_frame_selection_tournament_cycle579_receipt_2026_07_22.json").read_text())
    c590 = json.loads((ROOT / "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json").read_text())
    c596 = cold_report(ROOT / "outputs/physical_mobile_composite_action_regge_quadrature_tournament_cycle596_cold_2026_07_22.txt")
    c598 = json.loads((ROOT / "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_receipt_2026_07_22.json").read_text())
    fixtures = c590["retained_fixtures"]
    b596 = c596["inherited_boundary_controls"]
    boundary = {
        "Cycle576_authority_audit_tests": [c576["authority"], c576["audit"], c576["tests_passed"], c576["tests_total"]],
        "Cycle576_physical_M2_primitive_composition_closed": c576["scope_boundary"]["physical_M2_primitive_composition_closed"],
        "Cycle576_physical_intertwiner_measured": c576["scope_boundary"]["physical_intertwiner_measured"],
        "Cycle576_physical_code_leakage_measured": c576["scope_boundary"]["physical_code_leakage_measured"],
        "Cycle576_resource_identified_as_physical_stress_or_energy": c576["scope_boundary"]["resource_identified_as_physical_stress_or_energy"],
        "Cycle579_authority_audit_tests": [c579["authority"], c579["audit"], c579["tests_passed"], c579["tests_total"]],
        "Cycle579_physical_M2_primitive_composition_closed": c579["scope_boundary"]["physical_M2_primitive_composition_closed"],
        "Cycle579_physical_intertwiner_measured": c579["scope_boundary"]["physical_intertwiner_measured"],
        "Cycle579_physical_code_leakage_measured": c579["scope_boundary"]["physical_code_leakage_measured"],
        "Cycle579_literal_physical_M2_layout_compiled": c579["scope_boundary"]["literal_physical_M2_layout_compiled"],
        "Cycle579_target_exponential_exact_bounded_depth_compiled": c579["scope_boundary"]["target_exponential_exact_bounded_depth_compiled"],
        "Cycle590_authority_audit_tests": [c590["authority"], c590["audit"], c590["tests_passed"], c590["tests_passed"] + c590["tests_failed"]],
        "Cycle590_physical_encoder_composed": c590["route_B_conditional_M2_macro_blueprint"]["physical_encoder_composed_from_M2_primitives"],
        "Cycle590_physical_update_composed": c590["route_B_conditional_M2_macro_blueprint"]["physical_update_composed_from_M2_primitives"],
        "Cycle590_physical_code_leakage_evaluated": c590["route_B_conditional_M2_macro_blueprint"]["physical_code_leakage_evaluated"],
        "Cycle590_global_N_le_3_cutoff_locally_enforced": c590["route_B_conditional_M2_macro_blueprint"]["global_N_le_3_cutoff_locally_enforced"],
        "Cycle590_fixtures": fixtures,
        "Cycle596_authority_audit_tests": [c596["authority"], c596["audit"], c596["tests_passed"], c596["tests_total"]],
        "Cycle596_author_artifact_status_accepted": b596["author_artifact_status_accepted"],
        "Cycle596_audit_verdict_inferred": b596["audit_verdict_inferred_from_dependency"],
        "Cycle596_q_beta_N_is_alternative_to_J_beta": b596["Cycle594_q_beta_N_is_alternative_to_J_beta"],
        "Cycle596_pair_physical_M2_composed": c596["route_A"]["physical_M2_primitive_composition_evaluated"],
        "Cycle596_pair_physical_EG_evaluated": c596["route_A"]["physical_E_and_G_composition_evaluated"],
        "Cycle596_pair_contact_executed": c596["route_A"]["contact_gate_executed_in_route_A_update"],
        "Cycle596_solver_control_composed": c596["retained_solver_and_typed_clock"]["coherent_branch_to_solver_control_composition_evaluated"],
        "Cycle598_authority_audit_tests": [c598["authority"], c598["audit"], c598["tests_passed"], c598["tests_passed"] + c598["tests_failed"]],
        "Cycle598_conditional_role_layout_is_physical_site_compiler": c598["shore"]["conditional_role_layout_is_physical_site_compiler"],
        "Cycle598_gauge_preparation_supplied": c598["shore"]["gauge_preparation_supplied"],
        "Cycle598_physical_encoder_composed": c598["shore"]["physical_encoder_composed"],
        "Cycle598_physical_update_composed": c598["shore"]["physical_update_composed"],
        "Cycle598_physical_code_leakage_evaluated": c598["shore"]["physical_code_leakage_evaluated"],
        "Cycle598_host_scheduled_construction_is_physical_preparation": c598["route_C_uniform_fiber_preparation"]["host_scheduled_affine_construction_is_physical_preparation"],
        "Cycle598_unique_carrier_genesis_locally_enforced": c598["route_B_root_free_mobile_capacity"]["unique_one_carrier_per_species_genesis_locally_enforced"],
        "author_artifact_status_accepted": False,
        "audit_verdict_inferred_from_dependencies": False,
    }
    boundary["pass"] = (
        boundary["Cycle576_authority_audit_tests"] == ["none", "unset", 13, 13]
        and boundary["Cycle579_authority_audit_tests"] == ["none", "unset", 13, 13]
        and boundary["Cycle590_authority_audit_tests"] == ["none", "unset", 7, 7]
        and boundary["Cycle596_authority_audit_tests"] == ["none", "unset", 21, 21]
        and boundary["Cycle598_authority_audit_tests"] == ["none", "unset", 7, 7]
        and max(fixtures.values()) < TOL
        and not any((
            boundary["Cycle576_physical_M2_primitive_composition_closed"],
            boundary["Cycle576_physical_intertwiner_measured"],
            boundary["Cycle576_physical_code_leakage_measured"],
            boundary["Cycle576_resource_identified_as_physical_stress_or_energy"],
            boundary["Cycle579_physical_M2_primitive_composition_closed"],
            boundary["Cycle579_physical_intertwiner_measured"],
            boundary["Cycle579_physical_code_leakage_measured"],
            boundary["Cycle579_literal_physical_M2_layout_compiled"],
            boundary["Cycle579_target_exponential_exact_bounded_depth_compiled"],
            boundary["Cycle590_physical_encoder_composed"],
            boundary["Cycle590_physical_update_composed"],
            boundary["Cycle590_physical_code_leakage_evaluated"],
            boundary["Cycle590_global_N_le_3_cutoff_locally_enforced"],
            boundary["Cycle596_author_artifact_status_accepted"],
            boundary["Cycle596_audit_verdict_inferred"],
            boundary["Cycle596_pair_physical_M2_composed"],
            boundary["Cycle596_pair_physical_EG_evaluated"],
            boundary["Cycle596_pair_contact_executed"],
            boundary["Cycle596_solver_control_composed"],
            boundary["Cycle598_conditional_role_layout_is_physical_site_compiler"],
            boundary["Cycle598_physical_encoder_composed"],
            boundary["Cycle598_physical_update_composed"],
            boundary["Cycle598_physical_code_leakage_evaluated"],
            boundary["Cycle598_host_scheduled_construction_is_physical_preparation"],
            boundary["Cycle598_unique_carrier_genesis_locally_enforced"],
            boundary["author_artifact_status_accepted"],
            boundary["audit_verdict_inferred_from_dependencies"],
        ))
        and boundary["Cycle596_q_beta_N_is_alternative_to_J_beta"]
        and boundary["Cycle598_gauge_preparation_supplied"]
    )
    check("exact final dependencies are byte-pinned", observed == DEPENDENCIES,
          {name: {"expected": DEPENDENCIES[name], "observed": observed[name]}
           for name in DEPENDENCIES if DEPENDENCIES[name] != observed[name]})
    check("complete runtime import closure is direct-pinned", imports["pass"], imports)
    check("C576/C579/C590/C596/C598 physical, source, preparation, q_beta/J_beta and no-author boundaries pass",
          boundary["pass"], boundary)
    return {"expected": DEPENDENCIES, "observed": observed,
            "runtime_import_controls": imports, "inherited_boundary_controls": boundary}


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 601", "period-2", "not stationary",
        "source schedule is supplied", "q=4", "midpoint", "unitary redistribution",
        "givens", "declared bounded layout", "held l5", "held l7", "out-family l9",
        "schedule is not time", "modular word", "not gravity", "not physical energy",
        "generator is not a rate", "all 24", "all 576", "leakage", "deletion",
        "physical m2 primitive composition: not evaluated", "physical e/g: not evaluated",
        "physical leakage: not evaluated", "local sector enforcement: not compiled",
        "q_beta n is alternative to j_beta", "author artifact status accepted: false",
        "host-scheduled preparation is not physical preparation", "runtime import closure",
        "n1 —", "n8 —", "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note states the scoped construction and full N1-N8 negative gate", not missing, missing)


# ---------------------------------------------------------------------------
# Route A: a uniform, intrinsic, period-two recurrent mobile composite.


DIRECTIONS = np.asarray(cycle210.DIRECTIONS, dtype=int)
REVERSE = np.asarray([
    int(np.where(np.all(DIRECTIONS == -direction, axis=1))[0][0])
    for direction in DIRECTIONS
])


def composite_coin(beta: float) -> np.ndarray:
    coin = cycle219.common_species(beta).coin
    reverse = np.zeros((6, 6), dtype=complex)
    reverse[REVERSE, np.arange(6)] = 1
    result = np.zeros((12, 12), dtype=complex)
    result[6:, :6] = coin
    result[:6, 6:] = reverse
    return result


def composite_step(state: np.ndarray, beta: float) -> tuple[np.ndarray, np.ndarray]:
    """Coin then literal Cycle-230 axial stream; return post-coin and output."""
    length = state.shape[0]
    local = np.einsum("ab,xyzb->xyza", composite_coin(beta), state)
    output = np.zeros_like(local)
    for phase in range(2):
        for direction, velocity in enumerate(DIRECTIONS):
            output[..., 6 * phase + direction] = np.roll(
                local[..., 6 * phase + direction], tuple(int(v) for v in velocity), axis=(0, 1, 2)
            )
    return local, output


def composite_inverse(state: np.ndarray, beta: float) -> np.ndarray:
    unstreamed = np.zeros_like(state)
    for phase in range(2):
        for direction, velocity in enumerate(DIRECTIONS):
            unstreamed[..., 6 * phase + direction] = np.roll(
                state[..., 6 * phase + direction], tuple(int(-v) for v in velocity), axis=(0, 1, 2)
            )
    return np.einsum("ab,xyzb->xyza", composite_coin(beta).conj().T, unstreamed)


def density(state: np.ndarray) -> np.ndarray:
    return np.sum(abs(state) ** 2, axis=-1)


def continuity_residual(local: np.ndarray, streamed: np.ndarray) -> float:
    outgoing = density(local)
    incoming = density(streamed)
    divergence = outgoing.copy()
    for phase in range(2):
        for direction, velocity in enumerate(DIRECTIONS):
            flow = abs(local[..., 6 * phase + direction]) ** 2
            divergence -= np.roll(flow, tuple(int(v) for v in velocity), axis=(0, 1, 2))
    return float(np.max(abs(incoming - outgoing + divergence)))


def direction_permutation(frame: np.ndarray) -> np.ndarray:
    return np.asarray([
        int(np.where(np.all(DIRECTIONS == frame @ direction, axis=1))[0][0])
        for direction in DIRECTIONS
    ])


def transform_composite(state: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = state.shape[0]
    perm = direction_permutation(frame)
    output = np.zeros_like(state)
    for site in product(range(length), repeat=3):
        centered = np.asarray([value if value <= length // 2 else value - length for value in site])
        target = tuple(int(value % length) for value in frame @ centered)
        for phase in range(2):
            output[target][6 * phase + perm] = state[site][6 * phase + np.arange(6)]
    return output


def route_a() -> dict:
    rows = []
    maximum_period = maximum_inverse = maximum_continuity = maximum_covariance = 0.0
    minimum_motion = math.inf
    for label, beta, length, held in (("TRAIN_L2", -0.3, 2, False), ("HELD_L3", -0.35, 3, True)):
        scalar = np.ones(6, dtype=complex) / math.sqrt(6)
        state = np.zeros((length, length, length, 12), dtype=complex)
        state[(0, 0, 0, slice(0, 6))] = scalar
        local1, step1 = composite_step(state, beta)
        local2, step2 = composite_step(step1, beta)
        period = float(np.linalg.norm(step2 - np.vdot(state.ravel(), step2.ravel()) * state))
        inverse = float(np.linalg.norm(composite_inverse(step1, beta) - state))
        cont = max(continuity_residual(local1, step1), continuity_residual(local2, step2))
        motion = float(1 - density(step1)[0, 0, 0])
        covariance = 0.0
        for frame in cycle576.FRAMES:
            covariance = max(covariance, float(np.linalg.norm(
                transform_composite(composite_step(state, beta)[1], frame)
                - composite_step(transform_composite(state, frame), beta)[1]
            )))
        maximum_period = max(maximum_period, period)
        maximum_inverse = max(maximum_inverse, inverse)
        maximum_continuity = max(maximum_continuity, cont)
        maximum_covariance = max(maximum_covariance, covariance)
        minimum_motion = min(minimum_motion, motion)
        rows.append({
            "fixture": label, "length": length, "beta": beta, "held": held,
            "step1_origin_density": float(density(step1)[0, 0, 0]),
            "step1_support_cells": int(np.sum(density(step1) > 1e-12)),
            "step2_origin_density": float(density(step2)[0, 0, 0]),
            "step2_support_cells": int(np.sum(density(step2) > 1e-12)),
            "period_two_ray_residual": period, "inverse_residual": inverse,
            "continuity_residual_both_substeps": cont, "all24_covariance_residual": covariance,
        })

    coin = composite_coin(-0.3)
    delete_toggle = coin.copy(); delete_toggle[6:, :6] = 0
    delete_reversal = coin.copy(); delete_reversal[:6, 6:] = 0
    scalar_phase0 = np.r_[np.ones(6) / math.sqrt(6), np.zeros(6)]
    scalar_phase1 = np.r_[np.zeros(6), np.ones(6) / math.sqrt(6)]
    deletion = min(
        float(np.linalg.norm((coin - delete_toggle) @ scalar_phase0)),
        float(np.linalg.norm((coin - delete_reversal) @ scalar_phase1)),
    )

    rng = np.random.default_rng(601)
    random_state = rng.normal(size=(3, 3, 3, 12)) + 1j * rng.normal(size=(3, 3, 3, 12))
    random_state /= np.linalg.norm(random_state)
    random_inverse = float(np.linalg.norm(composite_inverse(composite_step(random_state, -0.3)[1], -0.3) - random_state))

    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    group_missing = 0
    direction_product_residual = 0
    for left in frames:
        for right in frames:
            group_missing += int(tuple((left @ right).reshape(-1)) not in lookup)
            p_left, p_right, p_both = map(direction_permutation, (left, right, left @ right))
            composed = p_left[p_right]
            direction_product_residual = max(direction_product_residual, int(np.max(abs(composed - p_both))))

    original_coin = cycle219.common_species(-0.3).coin
    phase0_to_phase1_coin_residual = float(np.linalg.norm(coin[6:, :6] - original_coin))
    # Explicit one-matter/one-binder declared sector: 6*12 pair basis states.
    encoding = np.zeros((72, 12), dtype=complex)
    for phase in range(2):
        for direction in range(6):
            logical = 6 * phase + direction
            ambient_index = 12 * direction + logical
            encoding[ambient_index, logical] = 1
    projector = encoding @ encoding.conj().T
    ambient_coin = encoding @ coin @ encoding.conj().T + np.eye(72) - projector
    intertwining = float(np.linalg.norm(ambient_coin @ encoding - encoding @ coin))
    ambient_unitarity = float(np.linalg.norm(ambient_coin.conj().T @ ambient_coin - np.eye(72)))
    code_leakage = float(np.linalg.norm((np.eye(72) - projector) @ ambient_coin @ encoding))
    local_constraint_commutator = float(np.linalg.norm(ambient_coin @ projector - projector @ ambient_coin))
    output = {
        "object": "intrinsic phase-tagged matter+binder pair under one translation-uniform local rule",
        "disposition": "CONSTRUCTIVE_PERIOD_TWO_RECURRENT_NOT_STATIONARY",
        "rows": rows,
        "maximum_period_two_ray_residual": maximum_period,
        "maximum_inverse_residual": max(maximum_inverse, random_inverse),
        "maximum_two_substep_continuity_residual": maximum_continuity,
        "minimum_step_one_departure_from_origin": minimum_motion,
        "maximum_all24_covariance_residual": maximum_covariance,
        "all576_products": len(frames) ** 2,
        "all576_missing_products": group_missing,
        "all576_direction_product_residual": direction_product_residual,
        "minimum_toggle_or_reversal_deletion_signal": deletion,
        "phase0_to_phase1_actual_Cycle219_coin_block_residual": phase0_to_phase1_coin_residual,
        "declared_pair_encoding": "E|p,d>=|one matter d, one binder(p,d)>; E K=(EKE^dag+I-EE^dag)E",
        "declared_pair_ambient_dimension": 72,
        "encoding_isometry_residual": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(12))),
        "declared_ambient_coin_intertwining_residual": intertwining,
        "declared_ambient_coin_unitarity_residual": ambient_unitarity,
        "declared_code_leakage_residual": code_leakage,
        "declared_pair_projector_commutator": local_constraint_commutator,
        "local_support_declared_two_level_roles": 18,
        "additional_declared_two_level_roles_per_cell": 13,
        "local_matching_projector": "matter direction equals its phase/direction binder label; this declared projector is invariant under the ambient block",
        "local_pair_constraint_enforcement_compiled": False,
        "physical_M2_primitive_composition_evaluated": False,
        "physical_E_and_G_composition_evaluated": False,
        "physical_code_leakage_evaluated": False,
        "physical_bounded_layout_or_depth_compiled": False,
        "global_one_pair_count_and_preparation_supplied": True,
        "exact_pinned_Cycle590_matter_law_preserved_per_pair_update": False,
        "full_joint_Cycle590_plus_pair_EG_executed": False,
        "Cycle590_mass_contact_seam_role": "separately byte-pinned regression shore only",
        "initial_supply": "localized scalar matter, phase-0 binder occupation, and empty seed rail",
        "no_external_head_or_host_timing": True,
        "no_supplied_trajectory": True,
        "intrinsic_phase_bit_is_physical_time": False,
        "stationary_source_constructed": False,
    }
    check("route A is mobile on substep one and recurrent on substep two", minimum_motion > 0.5 and maximum_period < TOL, rows)
    check("route A is reversible, locally continuous, and all24/all576 covariant",
          output["maximum_inverse_residual"] < TOL and maximum_continuity < TOL
          and maximum_covariance < TOL and group_missing == direction_product_residual == 0, output)
    check("route A declared block needs its intrinsic toggle/reversal and uses the actual Cycle219 coin as its phase-0 to phase-1 block",
          deletion > 0.5 and phase0_to_phase1_coin_residual < TOL and intertwining < TOL
          and ambient_unitarity < TOL and code_leakage < TOL and local_constraint_commutator < TOL,
          {"deletion": deletion, "phase0_to_phase1_coin": phase0_to_phase1_coin_residual,
           "intertwining": intertwining, "unitarity": ambient_unitarity,
           "leakage": code_leakage, "constraint": local_constraint_commutator})
    return output


# ---------------------------------------------------------------------------
# Route B: q=4 midpoint line quadrature plus literal finite two-mode circuits.


Q = 4
MIDPOINTS = np.asarray([(j + 0.5) / Q for j in range(Q)])


def exact_line(z: float) -> complex:
    return complex(np.exp(0.5j * z) * np.sinc(z / (2 * math.pi)))


def midpoint_line(z: float) -> complex:
    return complex(np.mean(np.exp(1j * MIDPOINTS * z)))


def polar_code(matrix: np.ndarray) -> np.ndarray:
    gram = matrix.conj().T @ matrix
    values, vectors = np.linalg.eigh(gram)
    return matrix @ vectors @ np.diag(1 / np.sqrt(values)) @ vectors.conj().T


def midpoint_map(momentum3: np.ndarray) -> np.ndarray:
    base = cycle576.regge.metric_map(np.zeros(4))
    factors = np.asarray([midpoint_line(float(momentum3 @ np.asarray(direction[:3])))
                          for direction in cycle576.regge.DIRS15])
    return factors[:, None] * base


def midpoint_encoding(momentum3: np.ndarray) -> np.ndarray:
    base = polar_code(cycle576.regge.metric_map(np.zeros(4)))
    blocks = []
    for sample, midpoint in enumerate(MIDPOINTS):
        phases = np.asarray([np.exp(1j * midpoint * momentum3 @ np.asarray(direction[:3]))
                             for direction in cycle576.regge.DIRS15])
        scale = np.ones(15) / math.sqrt(Q)
        # The purely temporal edge has z=0 and needs no spatial subdivision:
        # it occupies sample zero; its other three rails are bounded vacua.
        scale[0] = 1.0 if sample == 0 else 0.0
        blocks.append((phases * scale)[:, None] * base)
    return np.vstack(blocks)


def recombined_midpoint_encoding(momentum3: np.ndarray, fanout: np.ndarray) -> np.ndarray:
    """Unitary dilation: midpoint average on body sample 0, garbage retained."""
    routed = midpoint_encoding(momentum3).reshape(Q, 15, 10)
    recombined = routed.copy()
    for edge in range(1, 15):  # edge zero is purely temporal and bypasses q
        recombined[:, edge, :] = fanout.conj().T @ routed[:, edge, :]
    return recombined.reshape(Q * 15, 10)


def unitary_completion() -> np.ndarray:
    code = polar_code(cycle576.regge.metric_map(np.zeros(4)))
    complement = null_space(code.conj().T)
    return np.column_stack((code, complement))


def givens_factorization(unitary: np.ndarray) -> tuple[list, np.ndarray, float]:
    work = unitary.copy()
    gates = []
    for column in range(unitary.shape[0]):
        for row in range(unitary.shape[0] - 1, column, -1):
            a, b = work[row - 1, column], work[row, column]
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            if radius < 1e-14:
                continue
            gate = np.asarray(((np.conj(a) / radius, np.conj(b) / radius),
                               (-b / radius, a / radius)), dtype=complex)
            work[[row - 1, row], :] = gate @ work[[row - 1, row], :]
            gates.append((row - 1, row, gate))
    reconstruction = work.copy()
    for left, right, gate in reversed(gates):
        reconstruction[[left, right], :] = gate.conj().T @ reconstruction[[left, right], :]
    return gates, work, float(np.linalg.norm(reconstruction - unitary))


def fanout_unitary() -> tuple[np.ndarray, list[float]]:
    state = np.zeros(Q, dtype=complex); state[0] = 1
    total = np.eye(Q, dtype=complex)
    angles = []
    # Sequentially retain sqrt(remaining/q) on rail zero and peel 1/sqrt(q).
    for target in range(1, Q):
        remaining = Q - target + 1
        sine = 1 / math.sqrt(remaining)
        cosine = math.sqrt(1 - sine * sine)
        gate = np.eye(Q, dtype=complex)
        gate[np.ix_((0, target), (0, target))] = ((cosine, -sine), (sine, cosine))
        total = gate @ total
        angles.append(math.asin(sine))
    return total, angles


def bloch_product(momentum4: np.ndarray, diagonal_types: list, regge_types: list) -> np.ndarray:
    result = np.eye(15, dtype=complex)
    diagonal = np.zeros(15)
    for (_, left, _), coefficient in diagonal_types:
        diagonal[left] += float(coefficient.real)
    result = np.diag(np.exp(-1j * cycle579.UPDATE_ANGLE * diagonal)) @ result
    for (displacement, left, right), coefficient in regge_types:
        phase_coefficient = coefficient * np.exp(1j * momentum4 @ np.asarray(displacement))
        h = np.zeros((15, 15), dtype=complex)
        h[left, right] += phase_coefficient
        h[right, left] += np.conj(phase_coefficient)
        magnitude = abs(phase_coefficient)
        gate = np.eye(15, dtype=complex)
        if left == right:
            gate[left, left] = np.exp(-1j * cycle579.UPDATE_ANGLE * h[left, left].real)
        else:
            c = math.cos(cycle579.UPDATE_ANGLE * magnitude)
            s = math.sin(cycle579.UPDATE_ANGLE * magnitude)
            gate[left, left] = gate[right, right] = c
            gate[left, right] = -1j * s * phase_coefficient / magnitude
            gate[right, left] = -1j * s * np.conj(phase_coefficient) / magnitude
        result = gate @ result
    return result


def route_b() -> dict:
    q_kernel, d_kernel, kernel_controls = cycle579.exact_local_kernels()
    diagonal_types, regge_types, _ = cycle579.interaction_types(q_kernel, d_kernel)
    layer_rows = []
    train_layers = None
    for length in (3, 5, 7):
        layers, _, controls = cycle579.build_factor_layers(length, 0.0, diagonal_types, regge_types, [])
        if length == 3:
            train_layers = layers
        layer_rows.append({"length": length, **controls})

    completion = unitary_completion()
    givens, diagonal_remainder, givens_residual = givens_factorization(completion)
    diagonal_offdiag = float(np.linalg.norm(diagonal_remainder - np.diag(np.diag(diagonal_remainder))))
    fanout, fanout_angles = fanout_unitary()
    fanout_uniform = float(np.linalg.norm(abs(fanout[:, 0]) - np.ones(Q) / math.sqrt(Q)))
    fanout_inverse = float(np.linalg.norm(fanout.conj().T @ fanout - np.eye(Q)))

    fixtures = (("TRAIN_L3", 3, False), ("HELD_L5", 5, True),
                ("HELD_L7", 7, True), ("OUT_FAMILY_L9", 9, True))
    rows = []
    low_errors = []
    max_isometry = max_map_error = max_inverse = max_product_leakage = 0.0
    min_delete = math.inf
    max_null_error = 0
    for label, length, held in fixtures:
        momentum3 = np.asarray((2 * math.pi / length, 0.0, 0.0))
        exact = cycle576.regge.metric_map(np.r_[momentum3, 0.0])
        approximate = midpoint_map(momentum3)
        encoding = recombined_midpoint_encoding(momentum3, fanout)
        isometry = float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(10)))
        map_error = float(np.linalg.norm(approximate - exact))
        low_errors.append(map_error)
        edge = cycle576.base_edge_hessian(np.r_[momentum3, 0.0])
        ambient_generator = np.zeros((60, 60), dtype=complex)
        ambient_generator[:15, :15] = edge
        code = encoding.conj().T @ ambient_generator @ encoding
        code = (code + code.conj().T) / 2
        values = np.linalg.eigvalsh(code)
        cutoff = 1e-9 * max(float(np.max(abs(values))), 1.0)
        null_count = int(np.sum(abs(values) < cutoff))
        product15 = bloch_product(np.r_[momentum3, 0.0], diagonal_types, regge_types)
        product60 = np.eye(60, dtype=complex)
        product60[:15, :15] = product15
        leakage = float(np.linalg.norm((np.eye(60) - encoding @ encoding.conj().T) @ product60 @ encoding))
        inverse = float(np.linalg.norm(product60.conj().T @ product60 - np.eye(60)))
        z = float(momentum3 @ np.asarray((1, 1, 1)))
        deleted = midpoint_line(z) - np.exp(1j * MIDPOINTS[-1] * z) / Q
        deletion = float(abs(deleted - midpoint_line(z)))
        high_z = math.pi * 3
        rows.append({
            "fixture": label, "length": length, "held": held,
            "low_mode": momentum3.tolist(), "low_mode_metric_map_error": map_error,
            "coherent_body_map_error_in_polar_coordinates": float(np.linalg.norm(
                encoding[:15] - np.asarray([
                    exact_line(float(momentum3 @ np.asarray(direction[:3])))
                    for direction in cycle576.regge.DIRS15
                ])[:, None] * polar_code(cycle576.regge.metric_map(np.zeros(4)))
            )),
            "low_mode_body_line_error": abs(midpoint_line(z) - exact_line(z)),
            "full_BZ_body_line_error_at_z_3pi": abs(midpoint_line(high_z) - exact_line(high_z)),
            "code_isometry_residual": isometry, "code_null_count": null_count,
            "four_null_eigenvalue_residual": float(np.max(np.sort(abs(values))[:4])),
            "raw_ordered_product_code_leakage": leakage,
            "raw_ordered_product_inverse_residual": inverse,
            "delete_one_midpoint_amplitude_signal": deletion,
        })
        max_isometry = max(max_isometry, isometry)
        max_map_error = max(max_map_error, map_error)
        max_inverse = max(max_inverse, inverse)
        max_product_leakage = max(max_product_leakage, leakage)
        min_delete = min(min_delete, deletion)
        max_null_error = max(max_null_error, abs(null_count - 4))

    slopes = [math.log(low_errors[i] / low_errors[i + 1]) / math.log(fixtures[i + 1][1] / fixtures[i][1])
              for i in range(len(low_errors) - 1)]
    max_disp = kernel_controls["maximum_absolute_displacement"]
    # Explicit integer coordinates for a denominator-eight refined declared
    # block.  Each role's home is at `anchor`; spatial edge sample j is at
    # anchor+(2j+1)B v/8.  Thus its coarse Bloch phase is exactly the midpoint
    # phase.  The time-only edge uses one active rail and three bounded vacua.
    frames = cycle576.FRAMES
    block_scale = 128
    coords = {}
    for frame in range(24):
        sector_frame = frames[frame]
        for sample in range(Q):
            for edge in range(15):
                track = 15 * frame + edge
                anchor = np.asarray((track % 8, (track // 8) % 8, track // 64), dtype=int)
                spatial = sector_frame @ np.asarray(cycle576.regge.DIRS15[edge][:3])
                if np.any(spatial):
                    coords[(frame, sample, edge)] = anchor + (2 * sample + 1) * (block_scale // 8) * spatial
                else:
                    coords[(frame, sample, edge)] = anchor + np.asarray((0, sample, 0))
    unique_coordinates = len({tuple(value) for value in coords.values()})
    preparation_span = max(float(np.linalg.norm(coords[(frame, sample, edge)]
                                                       - np.asarray(((15 * frame + edge) % 8,
                                                                     ((15 * frame + edge) // 8) % 8,
                                                                     (15 * frame + edge) // 64))))
                           for frame in range(24) for sample in range(Q) for edge in range(15))
    product_span = math.sqrt(3) * block_scale * max_disp + 2 * preparation_span + math.sqrt(123)
    factor_depth = layer_rows[0]["layers"]
    preparation_depth = len(givens) + 1 + 2 * (Q - 1)
    total_depth = 2 * preparation_depth + factor_depth

    # Match the hand-built 15x15 Bloch product used for the leakage audit to
    # the literal Cycle579 sparse matching execution at the train momentum.
    train_k = np.asarray((2 * math.pi / 3, 0.0, 0.0, 0.0))
    rng = np.random.default_rng(601579)
    edge_vector = rng.normal(size=15) + 1j * rng.normal(size=15)
    edge_vector /= np.linalg.norm(edge_vector)
    bloch_state = np.zeros(16 * 3 ** 3, dtype=complex)
    for site in product(range(3), repeat=3):
        cell = (site[0] * 3 + site[1]) * 3 + site[2]
        bloch_state[16 * cell + 1:16 * cell + 16] = (
            np.exp(1j * train_k[:3] @ np.asarray(site)) * edge_vector / 3 ** 1.5
        )
    sparse_output = cycle579.lie_product(bloch_state, train_layers, 1)
    bloch_output = bloch_product(train_k, diagonal_types, regge_types) @ edge_vector
    predicted = np.zeros_like(bloch_state)
    for site in product(range(3), repeat=3):
        cell = (site[0] * 3 + site[1]) * 3 + site[2]
        predicted[16 * cell + 1:16 * cell + 16] = (
            np.exp(1j * train_k[:3] @ np.asarray(site)) * bloch_output / 3 ** 1.5
        )
    bloch_matching_residual = float(np.linalg.norm(sparse_output - predicted))

    lookup = {tuple(frame.reshape(-1)): i for i, frame in enumerate(frames)}
    group_missing = sum(tuple((left @ right).reshape(-1)) not in lookup for left in frames for right in frames)
    # The covariant object is the co-present frame orbit, not a claim that one
    # triangulation's 15 positive representatives are closed under rotations.
    # Sector g carries displacements g v_e; h sends it to sector hg and keeps e.
    frame_sector_displacement_residual = 0
    for left in frames:
        for sector in frames:
            for displacement in q_kernel:
                spatial = np.asarray(displacement[:3])
                frame_sector_displacement_residual = max(
                    frame_sector_displacement_residual,
                    int(np.max(abs(left @ (sector @ spatial) - (left @ sector) @ spatial))),
                )

    output = {
        "object": "actual Cycle576 15-edge Regge kernel with a q=4 midpoint line-factor approximation",
        "disposition": "CONSTRUCTIVE_DECLARED_TWO_MODE_BLOCKS_FOR_APPROXIMATE_MAP; PHYSICAL_LOWERING_AND_EXACT_IMAGE_TERMINALS_OPEN",
        "frozen_before_rows": {"q": Q, "train": [3], "held": [5, 7], "out_family": [9]},
        "approximation_law": "f_q(z)=q^-1 sum_j exp(i(j+1/2)z/q); fixed-mode error O(L^-2/q^2), full-BZ error does not vanish at fixed q",
        "rows": rows,
        "observed_low_mode_error_slopes": slopes,
        "maximum_code_isometry_residual": max_isometry,
        "maximum_raw_ordered_product_inverse_residual": max_inverse,
        "maximum_raw_ordered_product_code_leakage": max_product_leakage,
        "minimum_midpoint_deletion_signal": min_delete,
        "maximum_null_count_error_from_four": max_null_error,
        "kernel_controls": kernel_controls,
        "factor_layer_rows": layer_rows,
        "metric_polar_unitary_completion_dimension": 15,
        "metric_polar_two_mode_Givens_gates": len(givens),
        "metric_polar_Givens_reconstruction_residual": givens_residual,
        "metric_polar_triangular_offdiagonal_residual": diagonal_offdiag,
        "fanout_two_mode_Givens_gates_per_edge": Q - 1,
        "recombination_two_mode_Givens_gates_per_edge": Q - 1,
        "fanout_spatial_edges": 14,
        "time_edge_active_sample_rails": 1,
        "fanout_angles_radians": fanout_angles,
        "fanout_uniform_amplitude_residual": fanout_uniform,
        "fanout_inverse_residual": fanout_inverse,
        "no_cloning": "on each spatial edge one excitation is unitarily redistributed across four routed paths, inverse-Givens recombined onto one body rail plus three retained orthogonal garbage rails, and exactly recovered by the inverse; the z=0 temporal edge uses one active rail",
        "declared_two_level_sample_roles_per_cell": 24 * 15 * Q,
        "declared_refinement_denominator": 8,
        "exact_midpoint_phase_from_refined_displacement": True,
        "declared_layout_unique_role_coordinates": unique_coordinates,
        "all24_frame_sectors_declared": 24,
        "all576_products": 576,
        "all576_missing_products": int(group_missing),
        "all24_frame_sector_displacement_residual": int(frame_sector_displacement_residual),
        "declared_layout_max_preparation_distance": preparation_span,
        "declared_layout_max_product_distance_upper_bound": product_span,
        "declared_two_mode_preparation_factor_count": preparation_depth,
        "declared_Regge_product_factor_count": factor_depth,
        "declared_prepare_product_unprepare_factor_count": total_depth,
        "literal_sparse_to_Bloch_product_residual": bloch_matching_residual,
        "declared_layout_and_factor_count_independent_of_L": True,
        "physical_M2_primitive_composition_evaluated": False,
        "physical_E_and_G_composition_evaluated": False,
        "physical_code_leakage_evaluated": False,
        "physical_nearest_neighbor_routing_compiled": False,
        "physical_bounded_layout_or_depth_compiled": False,
        "local_one_excitation_sector_enforcement_compiled": False,
        "factor_order_is_a_supplied_schedule_not_time": True,
        "target_exponential_exact": False,
        "midpoint_map_realization": "unitary dilation: coherent average on sample-0 body rail, orthogonal quadrature garbage retained; actual Regge product acts on body rails only",
        "exact_line_factor_at_fixed_q": False,
        "raw_product_preserves_approximate_metric_image": max_product_leakage < TOL,
    }
    check("route B algebraically factors the metric isometry, unitary redistribution, and inverse into declared two-mode blocks",
          givens_residual < TOL and diagonal_offdiag < TOL and fanout_uniform < TOL and fanout_inverse < TOL,
          {"gates": len(givens), "reconstruction": givens_residual, "fanout": fanout_uniform})
    check("route B has a declared bounded coordinate/factor-count blueprint with all24/all576 closure",
          all(not row["matching_failures"] for row in layer_rows)
          and len(set(row["layers"] for row in layer_rows)) == 1
          and group_missing == frame_sector_displacement_residual == 0
          and unique_coordinates == 24 * 15 * Q and total_depth > 0
          and bloch_matching_residual < TOL, output)
    check("route B honest terminal audit detects fixed-q approximation and raw-image leakage",
          min(slopes) > 1.5 and rows[-1]["full_BZ_body_line_error_at_z_3pi"] > 1e-3
          and max_product_leakage > 1e-5 and min_delete > 1e-3, rows)
    return output


# ---------------------------------------------------------------------------
# Route C: reversible local modular response controlled by the recurrent source.


WORD_BITS = 20
MODULUS = 1 << WORD_BITS
SOURCE_CHARGE = 17


def laplacian(field: np.ndarray) -> np.ndarray:
    result = 6 * field
    for direction in DIRECTIONS:
        result -= np.roll(field, tuple(int(v) for v in direction), axis=(0, 1, 2))
    return result


def wave_step(previous: np.ndarray, current: np.ndarray, source: np.ndarray, sign: int) -> tuple[np.ndarray, np.ndarray]:
    following = (2 * current - previous - laplacian(current) + sign * source) % MODULUS
    return current.copy(), following


def wave_inverse(current: np.ndarray, following: np.ndarray, source: np.ndarray, sign: int) -> tuple[np.ndarray, np.ndarray]:
    previous = (2 * current - laplacian(current) + sign * source - following) % MODULUS
    return previous, current.copy()


def signed(field: np.ndarray) -> np.ndarray:
    return np.where(field >= MODULUS // 2, field - MODULUS, field).astype(np.int64)


def source_field(length: int, direction: int, step: int) -> np.ndarray:
    output = np.zeros((length, length, length), dtype=np.int64)
    if step % 2:
        site = tuple(int(value % length) for value in DIRECTIONS[direction])
    else:
        site = (0, 0, 0)
    output[site] = SOURCE_CHARGE
    return output


def response_run(length: int, direction: int, sign: int, advanced: bool, steps: int = 4) -> tuple[np.ndarray, np.ndarray, list]:
    previous = np.zeros((length,) * 3, dtype=np.int64)
    current = np.zeros_like(previous)
    history = []
    for step in range(steps):
        source = source_field(length, direction, step + int(advanced))
        previous, current = wave_step(previous, current, source, sign)
        history.append((previous.copy(), current.copy(), source.copy()))
    return previous, current, history


def static_green(length: int) -> np.ndarray:
    rho = np.zeros((length,) * 3); rho[0, 0, 0] = 1; rho -= 1 / length ** 3
    rho_hat = np.fft.fftn(rho)
    freq = 2 * math.pi * np.fft.fftfreq(length)
    denominator = np.zeros_like(rho)
    for index in product(range(length), repeat=3):
        denominator[index] = 6 - 2 * sum(math.cos(freq[index[axis]]) for axis in range(3))
    solution_hat = np.zeros_like(rho_hat)
    mask = denominator > 1e-12
    solution_hat[mask] = rho_hat[mask] / denominator[mask]
    return np.fft.ifftn(solution_hat).real


def rotate_scalar(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]
    output = np.zeros_like(field)
    for site in product(range(length), repeat=3):
        centered = np.asarray([value if value <= length // 2 else value - length for value in site])
        target = tuple(int(value % length) for value in frame @ centered)
        output[target] = field[site]
    return output


def route_c() -> dict:
    rows = []
    max_inverse = max_covariance = max_sign = 0
    min_order_signal = math.inf
    fingerprints = []
    for label, length, held in (("TRAIN_L3", 3, False), ("HELD_L5", 5, True), ("OUT_FAMILY_L7", 7, True)):
        prev_r, retarded, history = response_run(length, 0, +1, False)
        _, advanced, _ = response_run(length, 0, +1, True)
        _, negative, _ = response_run(length, 0, -1, False)
        sign_residual = int(np.max(abs(signed(retarded) + signed(negative))))
        source_last = history[-1][2]
        restored_previous, restored_current = wave_inverse(history[-1][0], history[-1][1], source_last, +1)
        inverse = max(int(np.max(abs(restored_previous - history[-2][0]))),
                      int(np.max(abs(restored_current - history[-2][1]))))
        order_signal = int(np.max(abs(signed(retarded) - signed(advanced))))
        far = tuple([length // 2] * 3)
        green = static_green(length)
        rows.append({
            "fixture": label, "length": length, "held": held, "updates": 4,
            "retarded_origin_word": int(signed(retarded)[0, 0, 0]),
            "retarded_forward_neighbor_word": int(signed(retarded)[tuple(DIRECTIONS[0] % length)]),
            "retarded_nonzero_cells": int(np.sum(signed(retarded) != 0)),
            "advanced_origin_word": int(signed(advanced)[0, 0, 0]),
            "advanced_forward_neighbor_word": int(signed(advanced)[tuple(DIRECTIONS[0] % length)]),
            "retarded_vs_advanced_order_signal": order_signal,
            "sign_flip_residual": sign_residual, "inverse_residual_integer": inverse,
            "finite_update_far_response": int(signed(retarded)[far]),
            "static_zero_mean_Green_far_value": float(green[far]),
        })
        max_inverse = max(max_inverse, inverse)
        max_sign = max(max_sign, sign_residual)
        min_order_signal = min(min_order_signal, order_signal)

    for direction in range(6):
        fingerprints.append(tuple(signed(response_run(7, direction, +1, False)[1]).ravel()))
    distinct_fingerprints = len(set(fingerprints))
    branch_gram = np.asarray([[float(left == right) for right in fingerprints]
                              for left in fingerprints])
    formal_fingerprint_label_gram_residual = float(np.linalg.norm(branch_gram - np.eye(6)))

    length = 5
    prior = np.arange(length ** 3, dtype=np.int64).reshape((length,) * 3) % 31
    current = (3 * prior + 7) % 47
    for frame in cycle576.FRAMES:
        left = rotate_scalar(wave_step(prior, current, source_field(length, 0, 0), +1)[1], frame)
        perm = direction_permutation(frame)[0]
        right = wave_step(rotate_scalar(prior, frame), rotate_scalar(current, frame),
                          source_field(length, int(perm), 0), +1)[1]
        max_covariance = max(max_covariance, int(np.max(abs(left - right))))

    zero = np.zeros((7,) * 3, dtype=np.int64)
    deleted = wave_step(zero, zero, zero, +1)[1]
    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): i for i, frame in enumerate(frames)}
    group_missing = sum(tuple((left @ right).reshape(-1)) not in lookup for left in frames for right in frames)
    output = {
        "object": "two-register signed modular radius-one wave response driven by a supplied period-two directional source schedule",
        "disposition": "CONSTRUCTIVE_INTEGER_REVERSIBLE_RESPONSE; SOURCE_CONTROL_COMPOSITION_RETARDED_ORDER_SIGN_AND_PHYSICAL_LOWERING_OPEN",
        "rows": rows,
        "maximum_exact_inverse_integer_residual": max_inverse,
        "maximum_sign_flip_integer_residual": max_sign,
        "minimum_retarded_vs_advanced_order_signal": min_order_signal,
        "source_deleted_zero_response": bool(np.max(abs(deleted)) == 0),
        "six_direction_branch_field_fingerprints": distinct_fingerprints,
        "formal_fingerprint_label_Gram_residual": formal_fingerprint_label_gram_residual,
        "coherent_quantum_source_control_composed": False,
        "route_A_carrier_to_response_control_composition_evaluated": False,
        "source_schedule_is_host_constructed": True,
        "source_schedule_is_supplied": True,
        "no_supplied_trajectory": False,
        "source_charge_continuity_residual": 0,
        "maximum_all24_covariance_integer_residual": max_covariance,
        "all576_products": 576,
        "all576_missing_products": int(group_missing),
        "declared_binary_field_roles_per_cell": 3 * WORD_BITS,
        "declared_local_arithmetic_role_support": 3,
        "analytic_ripple_factor_count_upper_bound": 16 * WORD_BITS,
        "physical_M2_primitive_composition_evaluated": False,
        "physical_E_and_G_composition_evaluated": False,
        "physical_code_leakage_evaluated": False,
        "physical_bounded_layout_or_depth_compiled": False,
        "local_modular_word_sector_enforcement_compiled": False,
        "modular_overflow": "none: arithmetic is exactly Z/(2^20); integer-to-physical-sign identification is supplied",
        "retarded_factor_order_selected_by_old_substrate": False,
        "response_sign_selected_by_old_substrate": False,
        "schedule_index_is_physical_time": False,
        "control_is_a_Record": False,
        "response_is_gravity": False,
        "static_zero_mean_comparator": "finite four-update support is zero beyond graph radius four while the separately computed static zero-mean cubic Green comparator is nonzero there; no Cycle596 solver-control composition is evaluated and q_beta N remains alternative to J_beta",
        "comparison_to_Cycle451": "typed off/receiver-zero/delay/advance outcomes remain 4:4,4:4,3:4,5:4; this construction does not choose the physical word sign or retarded order",
    }
    check("route C is an exactly reversible radius-one response with deletion and sign controls",
          max_inverse == max_sign == 0 and output["source_deleted_zero_response"], rows)
    check("route C distinguishes retarded/advanced integer schedules and six directional fingerprints without claiming coherent source control",
          min_order_signal > 0 and distinct_fingerprints == 6
          and formal_fingerprint_label_gram_residual == 0
          and not output["coherent_quantum_source_control_composed"], output)
    check("route C scalar stencil is all24/all576 covariant and keeps the static comparison distinct",
          max_covariance == 0 and group_missing == 0
          and abs(rows[-1]["static_zero_mean_Green_far_value"]) > 1e-8
          and rows[-1]["finite_update_far_response"] == 0, rows[-1])
    return output


def no_go_audit(routes: dict) -> dict:
    families = (
        {"family": "phase-tagged pair block", "object": "12-mode pair code",
         "mechanism": "intrinsic phase toggle plus reversal", "terminal": "period-two mobile recurrence",
         "marker": "ATTEMPTED", "result": "positive on the declared one-pair block; physical lowering, genesis and stationarity open"},
        {"family": "selected-anchor binder block", "object": "Cycle594 declared binder/buffer block",
         "mechanism": "pre/post-stream capture", "terminal": "mobile source",
         "marker": "RULED OUT BY PRIOR", "result": "only the selected-anchor immobile fixture fails the mobility terminal; other bound-pair mechanisms remain live"},
        {"family": "fixed-q midpoint line block", "object": "q=4 one-excitation sample roles",
         "mechanism": "unitary two-mode redistribution/recombination", "terminal": "bounded exact Regge line map",
         "marker": "ATTEMPTED", "result": "bounded declared factorization is positive; exact line and raw-image invariance fail on the fixtures"},
        {"family": "finite-torus DFT line code", "object": "Cycle596 exact sinc DFT roles",
         "mechanism": "size-indexed exact Fourier quadrature", "terminal": "constant overhead in that family",
         "marker": "RULED OUT BY PRIOR", "result": "Cycle596 L3/L4/L5/L7 counts rule out constant overhead only for its exact DFT family"},
        {"family": "raw Regge matching product", "object": "Cycle579 15-edge factor list",
         "mechanism": "translated disjoint matchings in supplied order", "terminal": "exact target exponential and physical compiler",
         "marker": "ATTEMPTED", "result": "logical sparse/product agreement is positive; target exponential, physical primitives and layout remain open"},
        {"family": "modular leapfrog response", "object": "two signed modular field words",
         "mechanism": "radius-one reversible integer recurrence", "terminal": "selected physical retarded response",
         "marker": "ATTEMPTED", "result": "integer inverse and schedule distinction positive; source-control composition, sign/order and physical lowering open"},
        {"family": "static zero-mean Green comparator", "object": "cubic Laplacian inverse",
         "mechanism": "paid-zero-mode static Fourier solve", "terminal": "finite-step retarded propagation",
         "marker": "RULED OUT BY PRIOR", "result": "a static solve is not a finite-step response; it remains a separate comparator rather than a failed dynamic law"},
    )
    walls = {
        "W_genesis": "the recurrent block's localized scalar and phase-0 binder are supplied",
        "W_stationary": "route A is exactly recurrent with period two, not stationary",
        "W_exact_line": "fixed q approximates rather than exactly realizes the sinc line factor",
        "W_image_invariance": "the raw ordered Regge product leaks from the approximate metric image",
        "W_response_order": "retarded and advanced integer schedules are both admitted",
        "W_response_identification": "modular sign is not tied to an operational response observable; q_beta N remains alternative to J_beta",
        "W_physical_lowering": "all C601 M2 primitive, physical E/G, leakage, routing and depth compositions are unevaluated",
        "W_source_control_composition": "route C replays a supplied directional schedule rather than composing the route-A carrier",
        "W_local_sector_enforcement": "one-pair, one-excitation and modular-word lawful sectors are supplied rather than locally enforced",
    }
    names = tuple(walls)
    pairs = tuple(
        {"left": names[i], "right": names[j], "left_implies_right": False,
         "right_implies_left": False, "independent": True}
        for i in range(len(names)) for j in range(i + 1, len(names))
    )
    hidden = [
        "phase-0 initialization", "global one-pair count and preparation", "no joint Cycle590-plus-pair physical compiler", "q=4 fixed before fixtures",
        "24 declared frame sectors", "factor order schedule", "20-bit modular alphabet",
        "source charge 17", "host-constructed directional source schedule", "retarded versus advanced ordering", "integer-word sign convention",
    ]
    partial = [
        "period-two mobile recurrence closes a code-level immobility residual without closing genesis, stationarity, sector enforcement or physical lowering",
        "q=4 closes finite algebraic factor count and declared coordinate bounds without exact sinc, image invariance, physical routing or primitive composition",
        "modular wave closes reversible integer propagation without composing the source, lowering the arithmetic, or selecting response sign/arrow",
    ]
    steelman = (
        "A controlled physical primitive compiler could lower the recurrent pair and explicitly compose it with the Cycle590 matter/contact/seam law; "
        "a continued-fraction or finite-state transfer identity could realize the sinc restriction with fixed auxiliary state, and a jointly designed Regge product could preserve that image. "
        "Finally an autonomous quantum source-control circuit, not the current host schedule, could drive a locally enforced field sector and an operational clock discriminator could select one response order."
    )
    echo = {
        "Cycle579": "exact raw-kernel matching and logical product traces, while physical primitives/layout and exact target exponential remain open",
        "Cycle596": "exact finite DFT quadrature with size growth and explicit physical E/G/layout/enforcement boundaries",
        "Cycle598": "logical root-free capacity and host-scheduled uniformization with physical preparation/enforcement false",
        "new_evidence": "period-two declared recurrence, fixed-q algebraic factorization/coordinate bounds, and reversible integer response",
        "repeated_wall": "physical lowering, exact line-map, source composition and response selection repeat; repetition is not a theorem",
    }
    output = {
        "N1_alternative_route_enumeration": families,
        "normalized_family_count": len(families),
        "qualifying_attempted_or_ruled_out_route_count": len(families),
        "unclosed_constructive_routes": (
            "physical primitive lowering and joint Cycle590 composition",
            "finite-state rational/continued-fraction exact-line encoder",
            "jointly invariant Regge product",
            "autonomous quantum source-control and clock-order discriminator",
        ),
        "N2_pairwise_wall_independence": pairs,
        "N2_collapsed_walls": walls,
        "N3_hidden_wall_scan": hidden,
        "N4_residual_matching": (
            {"witness": "Cycle579", "witness_residual": "logical product factorization, target exponential and physical compilation open", "current_residual": "q=4 declared factorization and raw-product leakage", "match": "logical factorization comparator only; no physical closure inferred"},
            {"witness": "Cycle590", "witness_residual": "conditional logical macro with supplied global cutoff and unevaluated physical E/G/leakage", "current_residual": "separate recurrent one-pair block", "match": "fixtures only; no joint compiler or cutoff enforcement claimed"},
            {"witness": "Cycle596", "witness_residual": "DFT size growth, physical lowering open, q_beta N alternative to J_beta", "current_residual": "fixed-q approximation and modular response", "match": "size comparator and source-identity boundary only; not evidence for exact fixed-state impossibility"},
            {"witness": "Cycle598", "witness_residual": "logical root-free capacity with supplied genesis and host preparation", "current_residual": "supplied C601 sectors and host source schedule", "match": "preparation/enforcement boundary only"},
        ),
        "N5_rhetoric_audit": "period-two is per supplied one-pair block; Givens/layout data are declared role/factor coordinates, not physical M2 gates; response is an integer schedule, not coherent source control or gravity; fixed-q failure is not a universal exact-line no-go",
        "N6_partial_closure_paths": partial,
        "N7_concrete_steelman": steelman,
        "N8_cross_cycle_echo": echo,
        "gate_status": "FAIL",
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "disposition": "partial constructions with narrow route-specific falsifiers and live physical/source alternatives",
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }
    check("N1-N8 audit blocks a broad negative and any axiom-pressure claim",
          len(families) >= 5 and len(pairs) == 36
          and len(hidden) >= 5 and len(partial) >= 3
          and output["gate_status"] == "FAIL"
          and not output["shared_route_independent_obstruction"] and not output["axiom_pressure"], output)
    return output


def main() -> None:
    pins = shore()
    note_contract()
    a = route_a()
    b = route_b()
    c = route_c()
    routes = {"route_A": a, "route_B": b, "route_C": c}
    no_go = no_go_audit(routes)
    inventory = {
        "supplied_candidate_laws": [
            "Cycle219 beta coin and Cycle230 stream/contact/seam", "intrinsic phase-toggle/reversal binder law",
            "Cycle576 raw Regge kernel and Cycle579 update angle/factor ordering", "q=4 midpoint quadrature",
            "20-bit modular leapfrog response, source charge 17, sign, and factor ordering",
        ],
        "supplied_initial_state_or_sector": [
            "Cycle590 declared N<=3 logical code domain as a separate exact-pinned regression shore only",
            "localized scalar source, global one-pair count, and phase-0 co-moving binder for the unjoined recurrent rule",
            "one-excitation metric/sample role sector", "24 declared frame sectors", "zero field words",
            "host-constructed selected-direction period-two source schedule for Route C",
        ],
        "not_derived": [
            "physical M2 primitive composition, physical E/G/leakage, NN routing, bounded physical layout/depth, or local sector enforcement for any C601 route",
            "joint Cycle590-plus-recurrent-pair compiler", "per-update preservation of the exact-pinned matter law by the recurrent rule",
            "stationarity", "source genesis", "exact bounded sinc compiler", "raw Regge image invariance",
            "target exponential", "physical response sign", "retarded arrow", "word-to-metric calibration",
            "Route-A-carrier-to-Route-C-control composition", "coherent quantum source control",
            "backreaction", "Lorentz covariance", "Born probabilities", "Records",
        ],
        "terminology_guards": {
            "wrapped_phase_is_energy": False, "generator_is_rate": False, "schedule_is_time": False,
            "control_is_Record": False, "modular_response_is_gravity": False,
        },
    }
    six_wall = {
        "C_ref": "UNCHANGED: frames remain supplied; all24/all576 proper-cubic covariance closes for the candidates, not Lorentz/reference genesis",
        "C_num": "UNCHANGED: local one-pair/one-excitation sectors and modular words are supplied lawful domains; role counts are not physical-M2 cost theorems",
        "C_wrap": "UNCHANGED: no wrapped phase is interpreted as physical energy or rate",
        "C_int": "PARTIAL: Cycle590 mass/contact/seam pass only as a separately pinned shore; no joint pair-plus-Cycle590 physical EG/contact update was executed; q_beta N remains alternative to J_beta",
        "C_local": "PARTIAL: period-two recurrence and q=4 factor/coordinate bounds close at declared code/role level; physical primitives, routing, E/G, leakage, enforcement, exact line image and stationarity remain open",
        "C_source": "PARTIAL: a supplied period-two directional schedule drives a reversible integer response; Route-A control composition, genesis, stationary limit, physical sign, stress identity and retarded selection remain open",
    }
    maturity = {
        "operational_quantum_records": 4.65,
        "time": 3.80,
        "inertia_matter": 4.87,
        "gravity_source": 4.15,
        "Born_probability": 3.65,
    }
    check("all C601 physical-M2 composition, physical E/G/leakage, routing, enforcement and source-control claims remain open",
          not any((
              a["physical_M2_primitive_composition_evaluated"],
              a["physical_E_and_G_composition_evaluated"],
              a["physical_code_leakage_evaluated"],
              a["local_pair_constraint_enforcement_compiled"],
              b["physical_M2_primitive_composition_evaluated"],
              b["physical_E_and_G_composition_evaluated"],
              b["physical_code_leakage_evaluated"],
              b["physical_nearest_neighbor_routing_compiled"],
              b["local_one_excitation_sector_enforcement_compiled"],
              c["physical_M2_primitive_composition_evaluated"],
              c["physical_E_and_G_composition_evaluated"],
              c["physical_code_leakage_evaluated"],
              c["local_modular_word_sector_enforcement_compiled"],
              c["coherent_quantum_source_control_composed"],
              c["route_A_carrier_to_response_control_composition_evaluated"],
          )))
    receipt = {
        "cycle": 601, "authority": AUTHORITY, "audit": AUDIT,
        "status": "declared code/role constructive partials; physical/source composition open; no shared no-go or axiom pressure",
        "author_artifact_status_accepted": False,
        "audit_verdict_inferred_from_dependencies": False,
        "pins": pins, "route_A_recurrent_source": a,
        "route_B_bounded_Regge": b, "route_C_local_response": c,
        "inventory": inventory, "six_wall_ledger": six_wall, "maturity_0_to_5": maturity,
        "no_go_discipline": no_go,
        "strongest_constructive_result": (
            "one uniform 18-declared-role-support block yields an all24-covariant period-two mobile matter+binder code; "
            "independently, q=4 yields exact algebraic two-mode factorization and constant declared-coordinate/factor-count bounds for an approximate Regge line map"
        ),
        "optimal_next_campaign": (
            "compile the pair, q=4 blocks and modular response into actual physical M2 primitives with local sector enforcement and explicit source-control composition; "
            "in parallel design a finite-state rational/continued-fraction exact-line encoder and invariant Regge product"
        ),
        "tests_passed": PASS, "tests_failed": FAIL,
        "pass": FAIL == 0, "elapsed_seconds": perf_counter() - START,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                                 * (1024 if sys.platform.startswith("linux") else 1)),
    }
    print("RECEIPT", json.dumps(receipt, sort_keys=True))
    print("SUMMARY", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": receipt["elapsed_seconds"], "maximum_RSS_bytes": receipt["maximum_RSS_bytes"],
        "route_A": a["disposition"], "route_B": b["disposition"], "route_C": c["disposition"],
        "broad_negative_gate": no_go["broad_negative_gate"], "axiom_pressure": False,
    }, sort_keys=True))
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
