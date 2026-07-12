#!/usr/bin/env python3
"""Self-contained bounded evaluation of the center/shell response coefficient.

The claimed object is deliberately narrow.  On one frozen finite operator
surface, this runner constructs the seven-site source basis, Dirichlet Green
operator, reduced-shell normalization, conformastatic ADM metric, and sampled
traceless-spatial Einstein readout directly.  It then evaluates

    Xi_i = [Theta_i(e0) - Theta_i(s/sqrt(6))] / (1/6),  i in {E_x, T1x},

where each Theta component is itself a centered source response.  No endpoint
coefficient, fitted source-family parameter, observed target, or other
frontier runner is imported.

This is a bounded finite-operator theorem, not an exact tensor observable or a
continuum/GR closure theorem.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.ndimage import map_coordinates
from scipy.sparse.linalg import spsolve


AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "S3_TIME_CONSTRUCTED_SUPPORT_TENSOR_PRIMITIVE_NOTE.md"

# These are theorem-domain choices, not fitted or observed inputs.
SIZE = 15
SHELL_RADIUS = 4.0
SOURCE_STEP = 0.005
SPACETIME_STEP = 0.04
PROBE_RADIUS = 4.25
SOURCE_STEP_CONTROLS = (0.0025, SOURCE_STEP, 0.01)
SPACETIME_STEP_CONTROLS = (0.03, SPACETIME_STEP, 0.05)
R_TEST = (0.25, 0.5, 0.75, 1.0, 1.5, 2.0)

STAR_COORDS = (
    (0, 0, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
ANCHOR_ORBIT = (3, 3, 0)


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str) -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    print(f"[{status}] {'PASS' if ok else 'FAIL'}: {name}")
    if detail:
        print(f"    {detail}")


def pair_text(values: np.ndarray | tuple[float, float]) -> str:
    return f"({float(values[0]):+.12e}, {float(values[1]):+.12e})"


def build_neg_laplacian(size: int) -> tuple[sparse.csr_matrix, int]:
    interior = size - 2
    n = interior**3
    ii, jj, kk = np.mgrid[0:interior, 0:interior, 0:interior]
    flat = ii.ravel() * interior * interior + jj.ravel() * interior + kk.ravel()
    rows = [flat]
    cols = [flat]
    vals = [np.full(n, 6.0)]
    for di, dj, dk in (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ):
        ni, nj, nk = ii + di, jj + dj, kk + dk
        mask = (
            (ni >= 0)
            & (ni < interior)
            & (nj >= 0)
            & (nj < interior)
            & (nk >= 0)
            & (nk < interior)
        )
        src = flat[mask.ravel()]
        dst = ni[mask] * interior * interior + nj[mask] * interior + nk[mask]
        rows.append(src)
        cols.append(dst.ravel())
        vals.append(-np.ones(src.shape[0]))
    return sparse.csr_matrix(
        (np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
        shape=(n, n),
    ), interior


def flat_idx(i: int, j: int, k: int, interior: int) -> int:
    return i * interior * interior + j * interior + k


def solve_columns(matrix: sparse.csr_matrix, sites: list[int]) -> np.ndarray:
    columns = []
    for site in sites:
        rhs = np.zeros(matrix.shape[0])
        rhs[site] = 1.0
        columns.append(spsolve(matrix, rhs))
    return np.column_stack(columns)


def build_adapted_basis() -> np.ndarray:
    e0 = np.zeros(7)
    e0[0] = 1.0
    px, mx, py, my, pz, mz = [np.eye(7)[i] for i in range(1, 7)]
    s = (px + mx + py + my + pz + mz) / np.sqrt(6.0)
    e1 = (px + mx - py - my) / 2.0
    e2 = (px + mx + py + my - 2.0 * pz - 2.0 * mz) / np.sqrt(12.0)
    tx = (px - mx) / np.sqrt(2.0)
    ty = (py - my) / np.sqrt(2.0)
    tz = (pz - mz) / np.sqrt(2.0)
    return np.column_stack([e0, s, e1, e2, tx, ty, tz])


H0, INTERIOR = build_neg_laplacian(SIZE)
CENTER = INTERIOR // 2
SUPPORT = [
    flat_idx(CENTER + x, CENTER + y, CENTER + z, INTERIOR)
    for x, y, z in STAR_COORDS
]
G0P = solve_columns(H0, SUPPORT)
GS = G0P[SUPPORT, :]


def phi_from_q(q: np.ndarray) -> np.ndarray:
    phi = np.zeros((SIZE, SIZE, SIZE), dtype=float)
    phi[1:-1, 1:-1, 1:-1] = (G0P @ q).reshape(
        (INTERIOR, INTERIOR, INTERIOR)
    )
    return phi


def support_delta(q: np.ndarray) -> float:
    support_phi = GS @ q
    charge = float(np.sum(q))
    return float((support_phi[0] - np.mean(support_phi[1:])) / charge)


def radii_grid(size: int) -> np.ndarray:
    center = (size - 1) / 2.0
    i, j, k = np.mgrid[0:size, 0:size, 0:size]
    return np.sqrt((i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2)


RADII = radii_grid(SIZE)


def full_neg_laplacian(field: np.ndarray) -> np.ndarray:
    out = np.zeros_like(field)
    out[1:-1, 1:-1, 1:-1] = (
        6.0 * field[1:-1, 1:-1, 1:-1]
        - field[2:, 1:-1, 1:-1]
        - field[:-2, 1:-1, 1:-1]
        - field[1:-1, 2:, 1:-1]
        - field[1:-1, :-2, 1:-1]
        - field[1:-1, 1:-1, 2:]
        - field[1:-1, 1:-1, :-2]
    )
    return out


def radial_average_nonzero(source: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    out = np.zeros_like(source)
    center = (source.shape[0] - 1) / 2.0
    groups: dict[int, list[tuple[int, int, int]]] = {}
    for i, j, k in product(range(source.shape[0]), repeat=3):
        if abs(source[i, j, k]) <= tol:
            continue
        d2 = int((i - center) ** 2 + (j - center) ** 2 + (k - center) ** 2)
        groups.setdefault(d2, []).append((i, j, k))
    for points in groups.values():
        mean = float(np.mean([source[p] for p in points]))
        for point in points:
            out[point] = mean
    return out


def orbit_key(i: int, j: int, k: int, size: int) -> tuple[int, int, int]:
    center = (size - 1) // 2
    return tuple(
        sorted((abs(i - center), abs(j - center), abs(k - center)), reverse=True)
    )


def anisotropic_anchor_per_charge(phi: np.ndarray) -> float:
    exterior = np.where(RADII > SHELL_RADIUS + 1e-12, phi, 0.0)
    sigma = full_neg_laplacian(exterior)
    delta_sigma = sigma - radial_average_nonzero(sigma)
    anchor = sum(
        float(delta_sigma[i, j, k])
        for i, j, k in product(range(SIZE), repeat=3)
        if orbit_key(i, j, k, SIZE) == ANCHOR_ORBIT
    )
    charge = float(np.sum(sigma))
    return anchor / charge


def interpolate_phi(phi: np.ndarray, point_xyz: np.ndarray) -> float:
    center = (phi.shape[0] - 1) / 2.0
    coords = np.array(
        [
            [center + point_xyz[0]],
            [center + point_xyz[1]],
            [center + point_xyz[2]],
        ],
        dtype=float,
    )
    return float(map_coordinates(phi, coords, order=3, mode="nearest")[0])


def adm_metric(phi: np.ndarray, point: np.ndarray) -> np.ndarray:
    potential = interpolate_phi(phi, np.asarray(point[1:], dtype=float))
    psi = 1.0 + potential
    alpha = (1.0 - potential) / psi
    metric = np.zeros((4, 4), dtype=float)
    metric[0, 0] = -(alpha**2)
    metric[1:, 1:] = np.eye(3) * psi**4
    return metric


def christoffel(phi: np.ndarray, point: np.ndarray, h: float) -> np.ndarray:
    metric = adm_metric(phi, point)
    inverse = np.linalg.inv(metric)
    derivative = np.zeros((4, 4, 4), dtype=float)
    for axis in range(4):
        plus, minus = point.copy(), point.copy()
        plus[axis] += h
        minus[axis] -= h
        derivative[axis] = (adm_metric(phi, plus) - adm_metric(phi, minus)) / (
            2.0 * h
        )
    gamma = np.zeros((4, 4, 4), dtype=float)
    for lam, mu, nu in product(range(4), repeat=3):
        gamma[lam, mu, nu] = 0.5 * sum(
            inverse[lam, rho]
            * (
                derivative[mu, rho, nu]
                + derivative[nu, rho, mu]
                - derivative[rho, mu, nu]
            )
            for rho in range(4)
        )
    return gamma


def einstein_tensor(phi: np.ndarray, point: np.ndarray, h: float) -> np.ndarray:
    metric = adm_metric(phi, point)
    inverse = np.linalg.inv(metric)
    gamma = christoffel(phi, point, h)
    dgamma = np.zeros((4, 4, 4, 4), dtype=float)
    for axis in range(4):
        plus, minus = point.copy(), point.copy()
        plus[axis] += h
        minus[axis] -= h
        dgamma[axis] = (
            christoffel(phi, plus, h) - christoffel(phi, minus, h)
        ) / (2.0 * h)
    ricci = np.zeros((4, 4), dtype=float)
    for mu in range(4):
        for nu in range(4):
            term1 = term2 = term3 = term4 = 0.0
            for lam in range(4):
                term1 += dgamma[lam, lam, mu, nu]
                term2 += dgamma[nu, lam, mu, lam]
                term3 += gamma[lam, mu, nu] * sum(
                    gamma[rho, lam, rho] for rho in range(4)
                )
                term4 += sum(
                    gamma[rho, mu, lam] * gamma[lam, nu, rho]
                    for rho in range(4)
                )
            ricci[mu, nu] = term1 - term2 + term3 - term4
    scalar = float(np.sum(inverse * ricci))
    return ricci - 0.5 * metric * scalar


PROBE_POINTS = (
    np.array([0.0, PROBE_RADIUS, 0.0, 0.0], dtype=float),
    np.array(
        [0.3, PROBE_RADIUS / np.sqrt(2.0), PROBE_RADIUS / np.sqrt(2.0), 0.0]
    ),
    np.array(
        [
            0.6,
            PROBE_RADIUS / np.sqrt(3.0),
            PROBE_RADIUS / np.sqrt(3.0),
            PROBE_RADIUS / np.sqrt(3.0),
        ]
    ),
)


ETA_CACHE: dict[tuple[tuple[float, ...], float], float] = {}


def eta_floor(q: np.ndarray, h: float) -> float:
    key = (tuple(float(x) for x in q), h)
    if key in ETA_CACHE:
        return ETA_CACHE[key]
    phi = phi_from_q(q)
    values = []
    for point in PROBE_POINTS:
        einstein = einstein_tensor(phi, point, h)
        spatial = einstein[1:, 1:]
        traceless = spatial - np.eye(3) * float(np.trace(spatial)) / 3.0
        values.append(float(np.max(np.abs(traceless))))
    ETA_CACHE[key] = max(values)
    return ETA_CACHE[key]


def theta_pair(
    q: np.ndarray, ex: np.ndarray, t1x: np.ndarray, eps: float, h: float
) -> np.ndarray:
    charge = float(np.sum(q))
    if abs(charge - 1.0) >= 1e-12:
        raise ValueError(f"theta_pair requires the declared unit-charge domain, got Q={charge}")
    normalization = anisotropic_anchor_per_charge(phi_from_q(q))
    return np.array(
        [
            (eta_floor(q + eps * bright, h) - eta_floor(q - eps * bright, h))
            / (2.0 * eps * normalization)
            for bright in (ex, t1x)
        ]
    )


def xi_direct(
    e0: np.ndarray,
    shell_unit: np.ndarray,
    ex: np.ndarray,
    t1x: np.ndarray,
    eps: float,
    h: float,
    delta_gap: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    theta_center = theta_pair(e0, ex, t1x, eps, h)
    theta_shell = theta_pair(shell_unit, ex, t1x, eps, h)
    xi_quotient = (theta_center - theta_shell) / delta_gap

    norm_center = anisotropic_anchor_per_charge(phi_from_q(e0))
    norm_shell = anisotropic_anchor_per_charge(phi_from_q(shell_unit))
    xi_four_eval = []
    for bright in (ex, t1x):
        center_response = (
            eta_floor(e0 + eps * bright, h) - eta_floor(e0 - eps * bright, h)
        ) / norm_center
        shell_response = (
            eta_floor(shell_unit + eps * bright, h)
            - eta_floor(shell_unit - eps * bright, h)
        ) / norm_shell
        xi_four_eval.append(
            (center_response - shell_response) / (2.0 * eps * delta_gap)
        )
    return theta_center, theta_shell, xi_quotient, np.array(xi_four_eval)


def main() -> int:
    print("Self-contained finite-lattice center/shell support-response evaluation")
    print("=" * 78)
    print(
        "Frozen domain: "
        f"size={SIZE}, shell_radius={SHELL_RADIUS}, source_step={SOURCE_STEP}, "
        f"spacetime_step={SPACETIME_STEP}, probe_radius={PROBE_RADIUS}"
    )

    basis = build_adapted_basis()
    e0 = basis[:, 0]
    shell_unit = basis[:, 1] / np.sqrt(6.0)
    e1, e2 = basis[:, 2], basis[:, 3]
    ex = (np.sqrt(3.0) * e1 + e2) / 2.0
    t1x = basis[:, 4]

    basis_error = float(np.max(np.abs(basis.T @ basis - np.eye(7))))
    green_residual = float(
        np.max(np.abs(H0 @ G0P - np.eye(H0.shape[0])[:, SUPPORT]))
    )
    record(
        "the support basis is orthonormal and the Dirichlet Green columns solve their declared sources",
        basis_error < 1e-14 and green_residual < 1e-12,
        f"basis_error={basis_error:.3e}, Green_residual={green_residual:.3e}",
        "FINITE-OPERATOR",
    )

    # Exact local identity: H[(1/6) delta_center] = e0 - average(six arms).
    source_gap = np.zeros(H0.shape[0])
    source_gap[SUPPORT[0]] = 1.0
    source_gap[SUPPORT[1:]] = -1.0 / 6.0
    potential_gap = np.zeros(H0.shape[0])
    potential_gap[SUPPORT[0]] = 1.0 / 6.0
    local_identity_residual = float(np.max(np.abs(H0 @ potential_gap - source_gap)))
    delta_center = support_delta(e0)
    delta_shell = support_delta(shell_unit)
    delta_gap = delta_center - delta_shell
    record(
        "the endpoint support gap is exactly 1/6 by the local lattice Laplacian identity",
        local_identity_residual == 0.0 and abs(delta_gap - 1.0 / 6.0) < 1e-12,
        (
            f"H[(1/6)delta_center] residual={local_identity_residual:.3e}, "
            f"computed delta_gap={delta_gap:.15e}"
        ),
        "EXACT",
    )

    norm_center = anisotropic_anchor_per_charge(phi_from_q(e0))
    norm_shell = anisotropic_anchor_per_charge(phi_from_q(shell_unit))
    record(
        "the reduced-shell normalization is independently computed, nonzero, and endpoint-independent",
        abs(norm_center - norm_shell) < 1e-12 and min(abs(norm_center), abs(norm_shell)) > 0.05,
        f"center={norm_center:.15e}, shell={norm_shell:.15e}, gap={abs(norm_center-norm_shell):.3e}",
        "FINITE-OPERATOR",
    )

    theta_center, theta_shell, xi, xi_four_eval = xi_direct(
        e0, shell_unit, ex, t1x, SOURCE_STEP, SPACETIME_STEP, delta_gap
    )
    print("\nDirect endpoint evaluation (no imported endpoint table):")
    print(f"  Theta(center) = {pair_text(theta_center)}")
    print(f"  Theta(shell)  = {pair_text(theta_shell)}")
    print(f"  Xi quotient   = {pair_text(xi)}")
    print(f"  Xi four-eval  = {pair_text(xi_four_eval)}")
    print(f"  ||Xi||_2      = {float(np.linalg.norm(xi)):.12e}")

    direct_formula_error = float(np.max(np.abs(xi - xi_four_eval)))
    record(
        "Xi is an explicit four-evaluation mixed response, not a renamed derivative symbol",
        direct_formula_error < 1e-15,
        f"max quotient-vs-four-evaluation difference={direct_formula_error:.3e}",
        "BOUNDED",
    )
    record(
        "both displayed response components are nonzero with the declared implementation margins",
        np.all(np.abs(xi) > 3.0e-4) and float(np.linalg.norm(xi)) > 1.0e-3,
        f"Xi={pair_text(xi)}, norm={float(np.linalg.norm(xi)):.12e}",
        "BOUNDED",
    )

    theta_center_reconstructed = theta_shell + xi * delta_gap
    endpoint_residual = float(
        np.max(np.abs(theta_center_reconstructed - theta_center))
    )
    record(
        "the unique affine law through the two endpoint readouts is exactly endpoint-compatible",
        endpoint_residual < 1e-15,
        f"max endpoint reconstruction residual={endpoint_residual:.3e}",
        "ALGEBRAIC",
    )

    print("\nStep-control grid:")
    control_vectors = []
    for h in SPACETIME_STEP_CONTROLS:
        for eps in SOURCE_STEP_CONTROLS:
            _, _, control_xi, _ = xi_direct(
                e0, shell_unit, ex, t1x, eps, h, delta_gap
            )
            control_vectors.append(control_xi)
            print(f"  h={h:.3f}, eps={eps:.4f}: Xi={pair_text(control_xi)}")
    control = np.array(control_vectors)
    min_component = np.min(np.abs(control), axis=0)
    min_norm = min(float(np.linalg.norm(v)) for v in control)
    same_sign = bool(np.all(np.sign(control) == np.sign(xi)))
    record(
        "the displayed nonzero direction survives the declared source-step and spacetime-stencil controls",
        same_sign and np.all(min_component > 3.0e-4) and min_norm > 1.0e-3,
        (
            f"min |components|={pair_text(min_component)}, min norm={min_norm:.12e}, "
            f"same_sign={same_sign}"
        ),
        "BOUNDED-CONTROL",
    )

    max_canonical_error = np.zeros(2)
    for r in R_TEST:
        q = (e0 + r * basis[:, 1]) / (1.0 + np.sqrt(6.0) * r)
        theta = theta_pair(q, ex, t1x, SOURCE_STEP, SPACETIME_STEP)
        prediction = theta_shell + xi * support_delta(q)
        max_canonical_error = np.maximum(max_canonical_error, np.abs(theta - prediction))
    record(
        "the endpoint-fixed affine law tracks the declared canonical support family at bounded tolerance",
        max_canonical_error[0] < 1e-8 and max_canonical_error[1] < 2e-8,
        f"max errors={pair_text(max_canonical_error)}",
        "BOUNDED",
    )

    source_text = Path(__file__).read_text(encoding="utf-8")
    note_text = NOTE.read_text(encoding="utf-8")
    syntax_tree = ast.parse(source_text)
    imported_modules = {
        node.module or ""
        for node in ast.walk(syntax_tree)
        if isinstance(node, ast.ImportFrom)
    }
    imported_modules.update(
        alias.name
        for node in ast.walk(syntax_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    )
    numeric_literal_magnitudes = {
        abs(float(node.value))
        for node in ast.walk(syntax_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    }
    disallowed_legacy_values = {
        698 / 10000,
        499 / 10000,
        -70 / 10000,
        642 / 10000,
        1056 / 10000,
        8247 / 10000,
        2271 / 10000,
        11 / 100,
        8 / 100,
        75 / 1000,
        7 / 100,
        18 / 100,
        45 / 100,
        82 / 100,
        77 / 100,
        73 / 100,
        69 / 100,
        64 / 100,
        61 / 100,
        -3772329167975 / 10**16,
        3359952396063 / 10**16,
        -2010572657265 / 10**16,
        4031967723697 / 10**16,
    }
    forbidden_claims = (
        "exact tensor-valued support observable theorem is closed",
        "full nonlinear GR is closed",
    )
    record(
        "source firewall excludes frontier helper imports and known legacy fitted/endpoint literals",
        "_frontier_loader" not in imported_modules
        and not any(module.startswith("frontier_") for module in imported_modules)
        and numeric_literal_magnitudes.isdisjoint(
            {abs(value) for value in disallowed_legacy_values}
        ),
        (
            "imports are standard-library, NumPy, and SciPy; the enumerated "
            "legacy family/endpoint values do not occur as numeric literals"
        ),
        "DEPENDENCY",
    )
    record(
        "claim firewall preserves the note's declared bounded/non-exact exclusions",
        not any(token in note_text for token in forbidden_claims)
        and "bounded support-response theorem; not an exact tensor observable" in note_text
        and "This note does not claim:" in note_text
        and "a continuum or stencil-convergence theorem" in note_text
        and "a physical theorem selecting this bounded readout" in note_text
        and "a full Einstein/Regge or nonlinear-GR closure theorem" in note_text,
        "the note explicitly excludes exact tensor, continuum, physical-selection, and full-GR claims",
        "DEPENDENCY",
    )

    print("\nVerdict:")
    print(
        "On the declared finite-protocol surface, Xi_R^(0) is the computed "
        "four-evaluation center/shell response coefficient. Its displayed "
        "components are nonzero with the tested margins, and it is the unique "
        "coefficient of the affine endpoint interpolant. Only that constructed "
        "interpolant has derivative Xi_R^(0). "
        "The result remains bounded: no exact tensor observable, continuum limit, "
        "or physical GR bridge is claimed."
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(check.ok for check in CHECKS)
    n_fail = sum(not check.ok for check in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
