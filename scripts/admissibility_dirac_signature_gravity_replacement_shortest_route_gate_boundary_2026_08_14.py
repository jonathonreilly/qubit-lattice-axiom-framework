#!/usr/bin/env python3
"""Block 76: screen the shortest local gravity replacement routes.

This runner does not search a broad coefficient space.  It checks the exact
minimal Ward/compatibility row on the reflected twenty-two-edge carrier, the
first Dirac constraint gate, and the smallest three- and six-section
connection extensions.  The surviving route is a changed local
incidence-derivative ADM/Fierz--Pauli carrier, not another scalar repair of the
Block-74 raw-edge marginal.
"""

from __future__ import annotations

import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import brentq
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_SIGNATURE_GRAVITY_REPLACEMENT_SHORTEST_ROUTE_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK49_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK53_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_"
    "UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK67_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_"
    "SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK75_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_"
    "CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_SIGNATURE_GRAVITY_REPLACEMENT_SHORTEST_ROUTE_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_curvature_gravity_physical_reconstruction_cut_gate_boundary_2026_08_14.py",
    "scripts/admissibility_dirac_signature_gravity_replacement_shortest_route_gate_boundary_2026_08_14.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402
import admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11 as block49  # noqa: E402
import admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11 as block53  # noqa: E402
import admissibility_reflected_curvature_gravity_physical_reconstruction_cut_gate_boundary_2026_08_14 as block75  # noqa: E402


MU = 1.0 / 1024.0
GRID_SIZE = 9
TOL = 1.0e-10


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 168 else detail[:165] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def matrix_rank(matrix: np.ndarray, tolerance: float = 1.0e-9) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tolerance))


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def minimal_ward_certificate(mutation: str) -> tuple[int, sp.Matrix, sp.Matrix]:
    """Coefficient-match the natural one-cell four-edge Ward ansatz."""
    zi, zt = sp.symbols("zi zt")
    a, b, c0, ct, d0, di = sp.symbols("a b c0 ct d0 di")
    xi = (
        a * (zi * zt - 1)
        + b * (zi - zt)
        + (c0 + ct * zt) * (zi - 1)
    )
    xt = (
        a * (zi * zt - 1)
        - b * (zi - zt)
        + (d0 + di * zi) * (zt - 1)
    )
    equations = []
    for expression in (xi, xt):
        polynomial = sp.Poly(sp.expand(expression), zi, zt)
        equations.extend(polynomial.coeff_monomial(term) for term in (1, zi, zt, zi * zt))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(
        equations, (a, b, c0, ct, d0, di)
    )
    kernel = coefficient_matrix.nullspace()
    candidate = sp.Matrix((1, 1, -1, -1, -1, -1))
    if mutation == "erase_unique":
        candidate[1] = 0
    return len(kernel), coefficient_matrix * candidate, kernel[0]


def line_factor(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=complex)
    result = np.ones(values.shape, dtype=complex)
    nonzero = np.abs(values) > 1.0e-12
    result[nonzero] = np.expm1(1j * values[nonzero]) / (1j * values[nonzero])
    return result


def exact_compatibility(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mutation: str,
) -> np.ndarray:
    directions = np.asarray(union.directions, dtype=float)
    raw = block49.curvature_intertwiner(union, np.zeros(4))
    factors = line_factor(directions @ np.asarray(momentum, dtype=complex))
    if mutation == "localize_compatibility":
        factors = np.ones_like(factors)
    return raw @ np.diag(1.0 / factors)


def relative_edge_modes(union: block48.ReflectionUnion) -> np.ndarray:
    (_, pair_to_union, _), _ = block48.union_reflection_split(union)
    pairs = np.zeros((20, 3), dtype=float)
    for column, spatial in enumerate(range(3)):
        component = block48.HCOMPS.index((spatial, 3))
        pairs[component, column] = 1.0
        pairs[len(block48.HCOMPS) + component, column] = -1.0
    return pair_to_union @ pairs


def dirac_data(
    union: block48.ReflectionUnion,
    wave_number: float,
    mu: float,
) -> tuple[tuple[int, ...], tuple[tuple[int, int, int], ...], int, float, np.ndarray]:
    q = np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
    metric_zero = block49.union_line_metric_map(union, np.zeros(4))
    nonmetric = null_space(metric_zero.T, rcond=1.0e-12)
    effective, complement, symbol = block75.constant_nonmetric_schur(
        union, q, nonmetric, mu
    )
    spatial = block75.SPATIAL_EMBEDDING
    temporal = block75.TEMPORAL_EMBEDDING
    spatial_block = spatial.T @ effective @ spatial
    mixing = spatial.T @ effective @ temporal
    temporal_block = temporal.T @ effective @ temporal
    reduced = spatial_block - mixing @ np.linalg.pinv(
        temporal_block, rcond=1.0e-10
    ) @ mixing.conj().T
    left_null = null_space(temporal_block.conj().T, rcond=1.0e-10)
    constraint = left_null.conj().T @ (temporal.T @ effective @ spatial)
    return (
        tuple(matrix_rank(item) for item in (symbol, complement, effective, temporal_block, reduced)),
        tuple(inertia(item) for item in (effective, temporal_block, reduced)),
        matrix_rank(constraint),
        float(np.linalg.norm(constraint)),
        np.linalg.eigvalsh(0.5 * (temporal_block + temporal_block.conj().T)),
    )


def derive_one_mode_mu(union: block48.ReflectionUnion) -> float:
    """Locate the hostile k=.4 lapse-null coefficient from its own equation."""
    metric_zero = block49.union_line_metric_map(union, np.zeros(4))
    nonmetric = null_space(metric_zero.T, rcond=1.0e-12)
    q = np.asarray((0.4, 0.0, 0.0, 0.0), dtype=complex)

    def lapse_entry(mu: float) -> float:
        effective, _, _ = block75.constant_nonmetric_schur(
            union, q, nonmetric, float(mu)
        )
        temporal = block75.TEMPORAL_EMBEDDING
        temporal_block = temporal.T @ effective @ temporal
        return float(temporal_block[0, 0].real)

    return float(brentq(lapse_entry, -0.20, -0.15, xtol=1.0e-14, rtol=1.0e-14))


def tuned_static_census(union: block48.ReflectionUnion, mu: float) -> tuple[int, int, float, float]:
    negative_static = 0
    negative_kinetic = 0
    minimum_static = np.inf
    minimum_kinetic = np.inf
    for integer_mode in np.ndindex((GRID_SIZE, GRID_SIZE, GRID_SIZE)):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        if np.all(centered == 0):
            continue
        k = 2.0 * np.pi * centered / GRID_SIZE
        static, kinetic = block75.tt_forms(union, k, mu, None)
        static_minimum = float(np.linalg.eigvalsh(static)[0])
        kinetic_minimum = float(np.linalg.eigvalsh(kinetic)[0])
        negative_static += int(static_minimum < -1.0e-7)
        negative_kinetic += int(kinetic_minimum < -1.0e-5)
        minimum_static = min(minimum_static, static_minimum)
        minimum_kinetic = min(minimum_kinetic, kinetic_minimum)
    return negative_static, negative_kinetic, minimum_static, minimum_kinetic


def direction_row(
    union: block48.ReflectionUnion,
    spatial: np.ndarray,
    momentum: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, complex]:
    """Return T_v^+, T_v^- and their exact gauge variation scale."""
    v = np.asarray(spatial, dtype=int)
    t = np.asarray((0, 0, 0, 1), dtype=int)
    v4 = np.concatenate((v, (0,)))
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    q = np.asarray(momentum, dtype=complex)
    a = complex(v @ q[:3])
    b = complex(q[3])
    plus = np.zeros(len(union.directions), dtype=complex)
    minus = np.zeros_like(plus)
    plus[index[tuple(v4 + t)]] = np.sqrt(float(v @ v) + 1.0)
    plus[index[tuple(v4)]] = -np.sqrt(float(v @ v))
    plus[index[tuple(t)]] = -np.exp(1j * a)
    minus[index[tuple(v4 - t)]] = np.sqrt(float(v @ v) + 1.0) * np.exp(1j * b)
    minus[index[tuple(v4)]] = -np.sqrt(float(v @ v)) * np.exp(1j * b)
    minus[index[tuple(t)]] = -1.0
    center = np.exp(-0.5j * (a + b))
    return center * plus, center * minus, center


V3 = tuple(np.eye(3, dtype=int))
V6 = V3 + (
    np.asarray((1, 1, 0)),
    np.asarray((1, 0, 1)),
    np.asarray((0, 1, 1)),
)


def sinc_derivative(value: float) -> float:
    if abs(value) < 1.0e-7:
        return -value / 3.0 + value**3 / 30.0
    return float((value * np.cos(value) - np.sin(value)) / value**2)


def connection_weight(value: float) -> complex:
    half = 0.5 * float(value)
    sinc = 1.0 if abs(half) < 1.0e-12 else float(np.sin(half) / half)
    return sinc / 4.0 + sinc_derivative(half) / (4.0j)


def contraction_row(direction: np.ndarray) -> np.ndarray:
    x, y, z = np.asarray(direction, dtype=float)
    return np.asarray((x * x, y * y, z * z, np.sqrt(2.0) * x * y,
                       np.sqrt(2.0) * x * z, np.sqrt(2.0) * y * z))


def connection_map(momentum: np.ndarray, directions=V6) -> np.ndarray:
    k = np.asarray(momentum, dtype=float)
    return np.asarray(
        [connection_weight(float(k @ v)) * contraction_row(v) for v in directions],
        dtype=complex,
    )


def tt_connection_singulars(momentum: np.ndarray, directions=V6) -> np.ndarray:
    tt = null_space(block53.tt_constraint(momentum), rcond=1.0e-11)
    return np.linalg.svd(connection_map(momentum, directions) @ tt, compute_uv=False)


def connection_zone_minimum(mutation: str) -> tuple[int, float]:
    directions = V6[:-1] if mutation == "drop_yz" else V6
    deficient = 0
    minimum = np.inf
    for integer_mode in np.ndindex((GRID_SIZE, GRID_SIZE, GRID_SIZE)):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        if np.all(centered == 0):
            continue
        k = 2.0 * np.pi * centered / GRID_SIZE
        singulars = tt_connection_singulars(k, directions)
        deficient += int(len(singulars) < 2 or singulars[-1] < 1.0e-10)
        minimum = min(minimum, float(singulars[-1]))
    return deficient, minimum


def ir_connection_masses(direction: np.ndarray) -> np.ndarray:
    k = 1.0e-7 * np.asarray(direction, dtype=float)
    tt = null_space(block53.tt_constraint(k), rcond=1.0e-11)
    pulled = connection_map(k) @ tt
    return np.linalg.eigvalsh(pulled.conj().T @ pulled)


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    block49_note = flat(BLOCK49_PATH)
    block53_note = flat(BLOCK53_PATH)
    block67_note = flat(BLOCK67_PATH)
    block75_note = flat(BLOCK75_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axiom boundary and four exact parent interfaces are read without promoting a replacement law",
        all(path.exists() for path in (
            NOTE_PATH, AXIOM_PATH, BLOCK49_PATH, BLOCK53_PATH, BLOCK67_PATH,
            BLOCK75_PATH, PREMISE_PATH,
        ))
        and "admissibility is not a dynamics axiom" in axiom
        and "three-component orientation-shift intertwiner" in block49_note
        and "positive shadow energy" in block53_note
        and "signed, conserved" in block67_note
        and "opposite-residue companion" in block75_note,
    )

    kernel_dimension, ward_residual, kernel_vector = minimal_ward_certificate(mutation)
    normalized_kernel = sp.simplify(kernel_vector / kernel_vector[0])
    checks.check(
        "minimal-four-edge-ward-row-unique",
        "the one-cell four-edge multi-affine Ward ansatz has only the existing Block-49 row",
        kernel_dimension == 1
        and ward_residual == sp.zeros(8, 1)
        and normalized_kernel == sp.Matrix((1, 1, -1, -1, -1, -1)),
        f"kernel dimension={kernel_dimension}; normalized coefficients={tuple(normalized_kernel)}",
    )

    union = block48.build_reflection_union()
    compatibility_error = 0.0
    gauge_error = 0.0
    for momentum in (
        np.asarray((0.31, -0.22, 0.17, 0.43)),
        np.asarray((0.40, 0.00, 0.00, 0.00)),
        np.asarray((1.20, -0.50, 0.30, 0.70)),
    ):
        compatibility = exact_compatibility(union, momentum, mutation)
        compatibility_error = max(
            compatibility_error,
            float(np.max(np.abs(compatibility @ block49.union_line_metric_map(union, momentum)))),
        )
        gauge_error = max(
            gauge_error,
            float(np.max(np.abs(compatibility @ block48.union_gauge_map(union, momentum)))),
        )
    relative_singulars = np.linalg.svd(
        exact_compatibility(union, np.zeros(4), "") @ relative_edge_modes(union),
        compute_uv=False,
    )
    checks.check(
        "exact-common-metric-compatibility-row",
        "the unique minimal inverse-line-factor row annihilates metric and gauge images and lifts three relative modes",
        compatibility_error < 5.0e-15
        and gauge_error < 5.0e-15
        and np.max(np.abs(relative_singulars - 2.0)) < 1.0e-12,
        f"|CM|={compatibility_error:.3e}; |CG|={gauge_error:.3e}; relative singulars={relative_singulars}",
    )

    probe = 0.41
    nonperiodicity = abs(line_factor(np.asarray((probe,)))[0] - line_factor(np.asarray((probe + 2.0 * np.pi,)))[0])
    near_pole = abs(1.0 / line_factor(np.asarray((2.0 * np.pi - 1.0e-7,)))[0])
    if mutation == "erase_pole":
        near_pole = 1.0
    checks.check(
        "minimal-compatibility-is-nonlocal-and-zone-singular",
        "the required inverse line factor is nonperiodic in raw momentum and diverges at a diagonal-zone corner",
        nonperiodicity > 0.9 and near_pole > 1.0e7,
        f"|F(q)-F(q+2pi)|={nonperiodicity:.6f}; |1/F(2pi-1e-7)|={near_pole:.3e}",
    )

    tuned_mu = derive_one_mode_mu(union)
    dirac_mu = tuned_mu if mutation == "restore_constraint" else MU
    ranks, inertias, constraint_rank, constraint_norm, _ = dirac_data(union, 0.4, dirac_mu)
    checks.check(
        "compatibility-alone-fails-dirac-gate",
        "exact kinematic compatibility does not restore the missing Hamiltonian row of the supplied action",
        ranks == (18, 12, 6, 3, 3)
        and inertias == ((4, 2, 4), (2, 1, 1), (2, 1, 3))
        and constraint_rank == 0
        and constraint_norm < 1.0e-10,
        f"ranks={ranks}; inertias={inertias}; constraint rank/norm={constraint_rank}/{constraint_norm:.3e}",
    )

    fitted_mu = MU if mutation == "promote_fit" else tuned_mu
    fit04 = dirac_data(union, 0.4, fitted_mu)
    fit08 = dirac_data(union, 0.8, fitted_mu)
    census = tuned_static_census(union, fitted_mu)
    checks.check(
        "one-mode-scalar-repair-does-not-generalize",
        "the scalar coefficient restoring the k=.4 constraint loses it at k=.8 and is full-zone indefinite",
        fit04[0][3] == 2
        and fit04[2] == 1
        and fit04[3] > 0.05
        and fit08[0][3] == 3
        and fit08[2] == 0
        and abs(float(fit08[4][-2]) + 0.00408197237) < 1.0e-7
        and census[0:2] == (318, 174)
        and census[2] < -40.0
        and census[3] < -1000.0,
        f"derived mu={tuned_mu:.15f}; k=.4 temporal/constraint ranks={fit04[0][3]}/{fit04[2]}; k=.8={fit08[0][3]}/{fit08[2]}; L9 negatives={census[0]}/{census[1]}",
    )

    q = np.asarray((0.37, 0.0, 0.0, 0.29))
    plus, minus, center = direction_row(union, np.asarray((1, 0, 0)), q)
    gauge = block48.union_gauge_map(union, q)
    plus_gauge = plus @ gauge
    minus_gauge = minus @ gauge
    shared_residual = float(np.max(np.abs(plus_gauge + minus_gauge)))
    if mutation == "same_sign":
        shared_residual = float(np.max(np.abs(plus_gauge - minus_gauge)))
    axis_cross = tt_connection_singulars(np.asarray((0.4, 0.0, 0.0)), V3)
    checks.check(
        "three-section-connection-has-axial-tt-obstruction",
        "a shared compensator makes three connection channels gauge invariant but their axial TT rank is only one",
        abs(center) > 0.9
        and shared_residual < 2.0e-15
        and axis_cross[0] > 0.24
        and axis_cross[-1] < 1.0e-12,
        f"shared gauge residual={shared_residual:.3e}; axial TT singulars={axis_cross}",
    )

    deficient, minimum = connection_zone_minimum(mutation)
    r_matrix = np.asarray([contraction_row(v) for v in V6])
    axis_singulars = tt_connection_singulars(np.asarray((0.4, 0.0, 0.0)))
    checks.check(
        "six-section-extension-is-kinematically-complete",
        "six directional contractions are invertible and cover both TT coordinates on every nonzero L=9 mode",
        abs(np.linalg.det(r_matrix) - 2.0 * np.sqrt(2.0)) < 1.0e-12
        and deficient == 0
        and minimum > 0.129
        and axis_singulars[-1] > 0.35,
        f"det R={np.linalg.det(r_matrix):.12f}; deficient={deficient}/728; min singular={minimum:.9f}; axis={axis_singulars}",
    )

    axis_mass = ir_connection_masses((1.0, 0.0, 0.0))
    face_mass = ir_connection_masses((1.0, 1.0, 0.0))
    body_mass = ir_connection_masses((1.0, 1.0, 1.0))
    sign_plus = np.linalg.eigvalsh(
        (connection_map((0.7, 0.2, 0.4)) @ null_space(block53.tt_constraint((0.7, 0.2, 0.4)), rcond=1.0e-11)).conj().T
        @ (connection_map((0.7, 0.2, 0.4)) @ null_space(block53.tt_constraint((0.7, 0.2, 0.4)), rcond=1.0e-11))
    )
    sign_minus = np.linalg.eigvalsh(
        (connection_map((-0.7, 0.2, 0.4)) @ null_space(block53.tt_constraint((-0.7, 0.2, 0.4)), rcond=1.0e-11)).conj().T
        @ (connection_map((-0.7, 0.2, 0.4)) @ null_space(block53.tt_constraint((-0.7, 0.2, 0.4)), rcond=1.0e-11))
    )
    route_condition = (
        np.max(np.abs(axis_mass - (1.0 / 8.0, 1.0 / 8.0))) < 1.0e-8
        and np.max(np.abs(face_mass - (1.0 / 16.0, 1.0 / 8.0))) < 1.0e-8
        and np.max(np.abs(body_mass - (1.0 / 24.0, 1.0 / 24.0))) < 1.0e-8
        and np.max(np.abs(sign_plus - sign_minus)) > 1.0e-4
    )
    if mutation == "claim_equal_norm":
        route_condition = False
    checks.check(
        "six-section-equal-norm-is-not-a-selected-gravity-law",
        "the minimal extension is IR anisotropic and lacks signed proper-cubic completion at finite momentum",
        route_condition,
        f"IR masses axis={axis_mass}, face={face_mass}, body={body_mass}; sign-flip split={np.max(np.abs(sign_plus-sign_minus)):.3e}",
    )

    scope_ok = all(
        phrase in note
        for phrase in (
            "partial-narrowing",
            "larger-support laurent syzygy",
            "changed carrier",
            "incidence-derivative adm/fierz--pauli",
            "zero toe percentage movement",
            "n1 -- alternative route enumeration",
            "n8 -- cross-cycle echo",
        )
    )
    if mutation == "claim_complete":
        scope_ok = False
    checks.check(
        "portfolio-and-no-go-scope-boundary",
        "the result stops scalar fitting, preserves live alternative carriers, and assigns no TOE or axiom authority",
        scope_ok,
    )

    print(
        "ROUTE: stop same-support scalar/three-connection fitting; advance exact local incidence-derivative ADM/Fierz--Pauli with Block67 source and Block53 TT quotient"
    )
    print(
        f"CERTIFICATE: ward_kernel=1 compatibility_errors={compatibility_error:.2e}/{gauge_error:.2e} tuned_L9_negative={census[0]}/{census[1]} W6_min={minimum:.9f}"
    )
    print(
        "SCOPE: bounded family cut and positive route ranking; no universal gravity no-go, selected action, axiom amendment, retention, or TOE movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
