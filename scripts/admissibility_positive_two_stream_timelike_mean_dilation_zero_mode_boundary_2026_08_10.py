#!/usr/bin/env python3
"""Checks a positive tick-plus-helix source and its compact dilation wall.

The paired note superposes two disjoint, separately closed actual-edge lines:
one axial tick line and one tick-space face-diagonal helix.  Every coefficient
is positive.  The complete source has an exact Ward identity, a timelike mean
energy current under the declared Lorentzian diagnostic, and direct
unprojected nonzero-mode Regge solves.  At compact k=0, the strictly positive
flat edge-length vector is itself a Regge null vector and exactly separates
every nonzero nonnegative actual-edge source from the Hessian range.
"""

from __future__ import annotations

from itertools import product
from math import pi, sqrt
from pathlib import Path
import sys

import numpy as np


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
HISTORY_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
REGGE_NOTE_PATH = ROOT / "docs" / (
    "CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_"
    "NARROW_THEOREM_NOTE_2026-06-09.md"
)
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_POSITIVE_TWO_STREAM_TIMELIKE_MEAN_DILATION_ZERO_MODE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "scripts/admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_closed_helical_defect_history_ward_neutral_ir_regge_response_boundary_2026_08_10 as parent  # noqa: E402
import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402


TICK_ANCHOR = np.asarray((0, 1, 0, 0), dtype=float)
SQRT2 = sqrt(2.0)
BETA = SQRT2 - 1.0


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        if detail:
            print(f"       {detail}")
        self.passed += int(ok)
        self.failed += int(not ok)


def positive_two_stream_row(length: int, momentum: np.ndarray) -> np.ndarray:
    """Equal-positive-weight face-diagonal and transverse tick lines."""
    return parent.closed_line_row(length, momentum, parent.HELIX) + parent.closed_line_row(
        length, momentum, parent.TICK, TICK_ANCHOR
    )


def physical_source_tensor(metric_covector: np.ndarray) -> np.ndarray:
    """Turn derivatives in the ten symmetric coordinates into tensor entries."""
    result = np.zeros((4, 4), dtype=complex)
    for value, (left, right) in zip(metric_covector, regge.HCOMPS):
        if left == right:
            result[left, right] = value
        else:
            result[left, right] = value / 2.0
            result[right, left] = value / 2.0
    return result


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    parent_note = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    history_note = HISTORY_NOTE_PATH.read_text(encoding="utf-8")
    regge_note = REGGE_NOTE_PATH.read_text(encoding="utf-8")
    kinetic = KINETIC_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    axiom_flat = " ".join(axiom.split())
    parent_flat = " ".join(parent_note.split())
    history_flat = " ".join(history_note.split())
    regge_flat = " ".join(regge_note.split())
    kinetic_flat = " ".join(kinetic.split())

    print("external_scientific_inputs: none; the positive two-stream action and dilation separator use the supplied actual edge carrier")
    print("package_local_integrity_reads: current axioms, Block-14 closed lines, the existing history/action candidate, and the Regge Hessian are source-bound")
    print("analytic_boundary: equal positive tick and face-diagonal lines give exact Ward closure and a timelike mean-current diagnostic")
    print("physical_boundary: the source is a prescribed two-stream mixture; compact k0, physical selection, coupling, nonlinear dynamics, and realization remain open")

    checks.check(
        "source-current-axioms",
        "the current axioms do not select the positive two-stream action, history ensemble, or geometry dynamics",
        "Admissibility is not a dynamics axiom" in axiom_flat
        and "update laws" in axiom_flat
        and "source/action and physical-observable identification" in axiom_flat,
    )
    checks.check(
        "source-parent-boundary",
        "Block 14 leaves positive compact and subluminal timelike completion as the next exact seam",
        "signed pair is not a positive-mass ensemble" in parent_flat
        and "null, not a massive subluminal timelike trajectory" in parent_flat
        and "balanced multi-edge" in parent_flat,
    )
    checks.check(
        "source-existing-history-amendment",
        "the existing candidate types a fixed positive history family and a fixed-global ensemble only if adopted",
        "fixed unnormalized local" in history_flat
        and "action representative" in history_flat
        and "fixed global lapse/strain" in history_flat
        and "This is sufficient wording, not adopted wording" in history_flat,
    )
    checks.check(
        "source-regge-boundary",
        "the supplied carrier has fifteen actual edge classes, constant metric zero modes, and one extra quadratic branch",
        "**15** edge classes" in regge_flat
        and "Constant metric perturbations" in regge_flat
        and "one exactly flat branch" in regge_flat,
    )
    checks.check(
        "source-tick-primitive",
        "equal-form tick graining supplies no stream weights, Lorentzian interpretation, or dynamics",
        "It carries no dimensionless dynamical content" in kinetic_flat
        and "not a new dynamics" in kinetic_flat,
    )

    closure_ok = True
    disjoint_ok = True
    positivity_ok = True
    for length in range(3, 9):
        helix_vertices = {
            tuple((step * parent.HELIX) % length) for step in range(length)
        }
        tick_vertices = {
            tuple((TICK_ANCHOR.astype(int) + step * parent.TICK) % length)
            for step in range(length)
        }
        closure_ok &= len(helix_vertices) == length and len(tick_vertices) == length
        closure_ok &= np.array_equal((length * parent.HELIX) % length, np.zeros(4, dtype=int))
        closure_ok &= np.array_equal((length * parent.TICK) % length, np.zeros(4, dtype=int))
        disjoint_ok &= helix_vertices.isdisjoint(tick_vertices)
        zero_source = positive_two_stream_row(length, np.zeros(4))
        positivity_ok &= np.all(zero_source.real >= 0.0) and np.count_nonzero(zero_source) == 2
    checks.check(
        "positive-disjoint-closed-streams",
        "the construction is two disjoint closed actual-edge lines with equal strictly positive coefficients for every L=3 through L=8",
        closure_ok and disjoint_ok and positivity_ok,
    )

    hostile_length = 7
    hostile_index = np.asarray((2, -1, 3, -2), dtype=float)
    hostile_momentum = 2.0 * pi * hostile_index / hostile_length
    direct = np.zeros(15, dtype=complex)
    for step in range(hostile_length):
        direct += np.exp(1j * np.dot(hostile_momentum, step * parent.HELIX)) * parent.edge_row(parent.HELIX)
        direct += np.exp(1j * np.dot(hostile_momentum, TICK_ANCHOR + step * parent.TICK)) * parent.edge_row(parent.TICK)
    formula = positive_two_stream_row(hostile_length, hostile_momentum)
    checks.check(
        "two-stream-fourier-transform",
        "the analytic source equals the direct transform of every edge in both seven-edge lines",
        np.linalg.norm(direct - formula) < 2.0e-13,
    )

    ward_worst = 0.0
    for length in range(3, 9):
        for index in product(parent.centered_indices(length), repeat=4):
            momentum = 2.0 * pi * np.asarray(index, dtype=float) / length
            ward_worst = max(
                ward_worst,
                float(np.linalg.norm(positive_two_stream_row(length, momentum) @ regge.gauge_map(momentum))),
            )
    checks.check(
        "two-stream-exact-gauge-ward",
        "the two separate line telescopes annihilate all four vertex-gauge directions on every declared torus mode",
        ward_worst < 2.0e-13,
        f"max gauge residual={ward_worst:.3e}",
    )

    principal_momentum = np.asarray((0.0, 0.23, -0.17, 0.0))
    per_step_edge_source = parent.edge_row(parent.TICK) + parent.edge_row(parent.HELIX)
    metric_covector = per_step_edge_source @ regge.metric_map(principal_momentum)
    source_tensor = physical_source_tensor(metric_covector)
    expected_tensor = np.outer(parent.TICK, parent.TICK).astype(float)
    expected_tensor += np.outer(parent.HELIX, parent.HELIX) / SQRT2
    energy_density = float(source_tensor[3, 3].real)
    energy_flux = float(source_tensor[0, 3].real)
    beta = energy_flux / energy_density
    lorentz_norm = energy_density**2 - energy_flux**2
    xt_determinant = float(
        (source_tensor[0, 0] * source_tensor[3, 3] - source_tensor[0, 3] ** 2).real
    )
    checks.check(
        "positive-two-stream-metric-source",
        "the common-support per-step metric source is t tensor t plus v tensor v divided by sqrt(2)",
        np.max(np.abs(source_tensor - expected_tensor)) < 2.0e-15,
    )
    checks.check(
        "timelike-mean-current",
        "the source time-column has exact subluminal speed beta=sqrt(2)-1 and positive Lorentz norm",
        abs(beta - BETA) < 2.0e-15
        and abs(lorentz_norm - (1.0 + SQRT2)) < 3.0e-15
        and 0.0 < beta < 1.0,
        f"beta={beta:.12f}; j_t^2-j_x^2={lorentz_norm:.12f}",
    )
    checks.check(
        "two-stream-not-single-dust-row",
        "the x-t source block has positive determinant and is a mixture rather than one rank-one massive worldline",
        abs(xt_determinant - 1.0 / SQRT2) < 2.0e-15,
        f"det(T_xt block)={xt_determinant:.12f}",
    )
    checks.check(
        "common-support-metric-ward",
        "the positive two-stream metric source annihilates the continuum gauge columns on kx=kt=0 support",
        np.linalg.norm(metric_covector @ parent.static.bag.continuum_gauge_metric(principal_momentum)) < 2.0e-15,
    )

    total_modes = 0
    sourced_modes = 0
    dynamic_modes = 0
    wrong_zero_counts = 0
    worst_null = 0.0
    worst_solve = 0.0
    worst_unsourced = 0.0
    per_length: list[tuple[int, int, int]] = []
    for length in range(3, 9):
        local_sourced = 0
        local_dynamic = 0
        for index in product(parent.centered_indices(length), repeat=4):
            total_modes += 1
            momentum = 2.0 * pi * np.asarray(index, dtype=float) / length
            source = positive_two_stream_row(length, momentum)
            expected_sourced = ((index[0] + index[3]) % length == 0) or (index[3] % length == 0)
            if not expected_sourced:
                worst_unsourced = max(worst_unsourced, float(np.linalg.norm(source)))
                continue
            if all(value == 0 for value in index):
                continue
            sourced_modes += 1
            local_sourced += 1
            is_dynamic = index[3] != 0
            dynamic_modes += int(is_dynamic)
            local_dynamic += int(is_dynamic)
            data = parent.source_data(source, momentum)
            wrong_zero_counts += int(data["zero_count"] != 5)
            worst_null = max(worst_null, float(data["null"]))
            worst_solve = max(worst_solve, float(data["solve"]))
        per_length.append((length, local_sourced, local_dynamic))

    checks.check(
        "positive-two-stream-support-inventory",
        "the fixed-global positive mixture has 2,369 supported nonzero sources among all 8,755 modes",
        total_modes == 8755
        and sourced_modes == 2369
        and per_length == [(3, 44, 18), (4, 111, 48), (5, 224, 100), (6, 395, 180), (7, 636, 294), (8, 959, 448)]
        and worst_unsourced < 2.0e-12,
        f"total={total_modes}; sourced={sourced_modes}; per-L={per_length}",
    )
    checks.check(
        "positive-two-stream-dynamic-inventory",
        "1,088 supported sources have nonzero tick frequency",
        dynamic_modes == 1088,
        f"dynamic={dynamic_modes}",
    )
    checks.check(
        "positive-two-stream-zero-inventory",
        "every one of the 2,369 supported nonzero sources meets a five-dimensional Regge zero space",
        wrong_zero_counts == 0,
    )
    checks.check(
        "positive-two-stream-full-null-compatibility",
        "the positive mixture annihilates the complete Regge null space on all supported nonzero modes",
        worst_null < 3.0e-13,
        f"max full-null overlap={worst_null:.3e}",
    )
    checks.check(
        "positive-two-stream-unprojected-solvability",
        "the actual unprojected edge equation solves on all 2,369 supported nonzero modes",
        worst_solve < 5.0e-12,
        f"max direct solve residual={worst_solve:.3e}",
    )

    zero_momentum = np.zeros(4)
    q0 = regge.bloch_Q(zero_momentum).real
    m0 = regge.metric_map(zero_momentum).real
    uniform_metric = np.zeros(10)
    uniform_metric[:4] = 2.0
    edge_lengths = np.linalg.norm(np.asarray(regge.DIRS15, dtype=float), axis=1)
    checks.check(
        "dilation-vector-metric-identity",
        "the strictly positive edge-length vector is exactly the line-averaged uniform metric dilation",
        np.max(np.abs(m0 @ uniform_metric - edge_lengths)) < 2.0e-15
        and np.min(edge_lengths) == 1.0,
    )
    checks.check(
        "dilation-vector-zero-mode",
        "the flat edge-length dilation is a compact Regge zero vector",
        np.linalg.norm(q0 @ edge_lengths) < 1.0e-12,
        f"||Q(0) ell||={np.linalg.norm(q0 @ edge_lengths):.3e}",
    )
    mixture_zero = positive_two_stream_row(5, zero_momentum).real
    zero_data = parent.source_data(mixture_zero.astype(complex), zero_momentum)
    separator = float(edge_lengths @ mixture_zero)
    checks.check(
        "positive-cone-dilation-separator",
        "the positive dilation null vector strictly separates every nonzero nonnegative actual-edge source from Range Q(0)",
        np.all(edge_lengths > 0.0)
        and np.all(mixture_zero >= 0.0)
        and abs(separator - 10.0 * (1.0 + SQRT2)) < 3.0e-14,
        f"ell dot s_plus(0)={separator:.12f}",
    )
    checks.check(
        "positive-two-stream-zero-mode-control",
        "the concrete positive mixture retains the compact k=0 incompatibility without source projection",
        zero_data["zero_count"] == 11
        and zero_data["null"] > 13.0
        and zero_data["solve"] > 13.0,
        f"null overlap={zero_data['null']:.6f}; solve residual={zero_data['solve']:.6f}",
    )

    transverse_directions = (
        np.asarray((0.0, 1.0, 0.0, 0.0)),
        np.asarray((0.0, 0.0, 1.0, 0.0)),
        np.asarray((0.0, 1.0, 1.0, 0.0)) / SQRT2,
        np.asarray((0.0, 1.0, 2.0, 0.0)) / sqrt(5.0),
    )
    mean_tangent = np.asarray((BETA, 0.0, 0.0, 1.0))
    continuum_targets = []
    pole_coefficients = []
    pole_errors = []
    pole_residuals = []
    pole_wards = []
    for direction in transverse_directions:
        continuum_hessian = -0.5 * regge.einstein_pairing_4d(direction)
        continuum_source = per_step_edge_source @ regge.metric_map(np.zeros(4))
        continuum_response = -np.linalg.pinv(continuum_hessian, rcond=1.0e-10) @ continuum_source.conj()
        continuum_targets.append(
            float((mean_tangent @ parent.metric_tensor(continuum_response) @ mean_tangent).real)
        )
        coefficients = []
        for epsilon in (0.05, 0.025):
            momentum = epsilon * direction
            metric_map = regge.metric_map(momentum)
            metric_hessian = metric_map.conj().T @ regge.bloch_Q(momentum) @ metric_map
            metric_source = per_step_edge_source @ metric_map
            pole_wards.append(
                float(np.linalg.norm(metric_source @ parent.static.bag.continuum_gauge_metric(momentum)))
            )
            response = -np.linalg.pinv(metric_hessian, rcond=1.0e-10) @ metric_source.conj()
            pole_residuals.append(
                float(np.linalg.norm(metric_hessian @ response + metric_source.conj()))
            )
            coefficients.append(
                float(
                    (
                        np.dot(momentum, momentum)
                        * (mean_tangent @ parent.metric_tensor(response) @ mean_tangent)
                    ).real
                )
            )
        pole_coefficients.append(coefficients[-1])
        pole_errors.append((abs(coefficients[0] - 4.0), abs(coefficients[1] - 4.0)))
    checks.check(
        "continuum-two-stream-target",
        "the source-derived minus-one-half Einstein comparator gives the exact shared-transverse mean-current coefficient four",
        max(abs(value - 4.0) for value in continuum_targets) < 3.0e-14,
    )
    checks.check(
        "unprojected-two-stream-pole",
        "four shared-transverse directions give |k|^2 q^T h q -> 4 without source projection",
        max(abs(value - 4.0) for value in pole_coefficients) < 2.0e-4
        and max(pole_residuals) < 3.0e-11
        and max(pole_wards) < 2.0e-14,
        "coefficients=" + ",".join(f"{value:.7f}" for value in pole_coefficients),
    )
    checks.check(
        "two-stream-pole-convergence",
        "halving shared-transverse momentum reduces every pole-coefficient error",
        all(second < first for first, second in pole_errors),
    )

    checks.check(
        "theorem-source-surface",
        "the note states the positive action, exact Ward identity, timelike mean, inventory, dilation separator, and pole",
        all(
            phrase in note_flat
            for phrase in (
                "A_+[g]=A_v,0[g]+A_t,b[g]",
                "beta=sqrt(2)-1",
                "2,369",
                "1,088",
                "ell dot s>0",
                "|k|^2 q^T h q ->4",
                "existing candidate",
            )
        ),
    )
    checks.check(
        "no-go-discipline-source-surface",
        "the note carries N1 through N8 and restricts the dilation result to the bare compact quadratic carrier",
        all(f"N{index}" in note for index in range(1, 9))
        and "No universal compact-source no-go" in note_flat
        and "fixed-global" in note_flat
        and "sign-indefinite" in note_flat,
    )
    checks.check(
        "boundary-source-surface",
        "the note preserves mixture-versus-worldline, Lorentzian, selection, coupling, nonlinear, Born, and realized-history boundaries",
        all(
            phrase in note_flat
            for phrase in (
                "two-stream mixture",
                "naive Lorentzian diagnostic",
                "physical action representative",
                "coupling sign",
                "nonlinear completion",
                "Born functional",
                "realized history",
                "fixed TOE percentages remain unchanged",
            )
        ),
    )
    checks.check(
        "canonical-axiom-nonmutation",
        "the canonical memo contains none of the positive-two-stream or dilation-separator wording",
        all(
            phrase not in axiom_flat
            for phrase in (
                "positive two-stream timelike mean",
                "dilation zero-mode separator",
                "tick-plus-helix mixture",
            )
        ),
    )

    print("per_element: checked positive actual tick and face-diagonal edge weights, their metric tensor, and the compact dilation separator")
    print("per_site: checked two disjoint separately closed streams and the exact force balance of each complete line for every L=3 through L=8")
    print("per_mode: checked all 2,369 supported nonzero positive-mixture sources against the complete Regge null space and the compact k0 control")
    print("per_block: checked timelike mean-current diagnostics, the exact nonnegative-cone boundary, and the unprojected shared-transverse pole")
    print("lattice_wide: checked all 8,755 Fourier modes on six four-tori; every supported nonzero equation solves without projection")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
