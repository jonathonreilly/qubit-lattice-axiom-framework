#!/usr/bin/env python3
"""Route-2 eta-floor Hellmann-Feynman boundary check.

This runner is deliberately narrow. It checks whether the live eta-floor
chain exposes the spectral object required by the Hellmann-Feynman derivative:

    eta_floor(q) = lambda_min(A(phi(q)))

with a simple floor eigenpair. The live code currently stores eta_floor[1] as
the tensor-completion `e_spatial_tf` max-entry observable, not as an eigenvalue.
"""

from __future__ import annotations

import ast
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import numpy as np

from _frontier_loader import load_frontier


AUDIT_TIMEOUT_SEC = 600

ROOT = Path(__file__).resolve().parents[1]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    print(f"{tag}: {name}")
    if detail:
        print(f"  {detail}")


def source_text(relpath: str) -> str:
    return (ROOT / relpath).read_text(encoding="utf-8")


def call_names_in_function(relpath: str, function_name: str) -> set[str]:
    tree = ast.parse(source_text(relpath), filename=relpath)
    functions = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    ]
    if len(functions) != 1:
        return set()
    out: set[str] = set()
    for node in ast.walk(functions[0]):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                out.add(func.id)
            elif isinstance(func, ast.Attribute):
                out.add(func.attr)
    return out


def all_spectral_calls(relpath: str) -> list[tuple[str, int]]:
    tree = ast.parse(source_text(relpath), filename=relpath)
    out: list[tuple[str, int]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func = node.func
            name = ""
            if isinstance(func, ast.Name):
                name = func.id
            elif isinstance(func, ast.Attribute):
                name = func.attr
            if name in {"eig", "eigh", "eigvals", "eigvalsh"}:
                out.append((name, node.lineno))
    return sorted(out, key=lambda item: item[1])


def probe_points() -> list[np.ndarray]:
    return [
        np.array([0.0, 4.25, 0.0, 0.0], dtype=float),
        np.array([0.3, 4.25 / np.sqrt(2.0), 4.25 / np.sqrt(2.0), 0.0], dtype=float),
        np.array([0.6, 4.25 / np.sqrt(3.0), 4.25 / np.sqrt(3.0), 4.25 / np.sqrt(3.0)], dtype=float),
    ]


def active_max_entry(tcomp, phi_grid: np.ndarray) -> tuple[float, float, tuple[int, int, int, float]]:
    vals: list[tuple[float, int, int, int, float]] = []
    for point_index, point in enumerate(probe_points()):
        _, einstein = tcomp.ricci_and_einstein(
            lambda p: tcomp.adm_metric(phi_grid, p, eps_vec=0.0, eps_ten=0.0, omega=0.0),
            point,
        )
        spatial = einstein[1:, 1:]
        spatial_tf = spatial - np.eye(3) * float(np.trace(spatial)) / 3.0
        for i in range(3):
            for j in range(3):
                value = float(spatial_tf[i, j])
                vals.append((abs(value), point_index, i, j, value))
    vals.sort(reverse=True, key=lambda row: row[0])
    top = vals[0]
    runner_up = vals[1]
    return top[0], top[0] - runner_up[0], (top[1], top[2], top[3], top[4])


def quiet_family_block(utk, label: str, phi_grid: np.ndarray):
    with redirect_stdout(StringIO()):
        return utk.family_block(label, phi_grid)


def main() -> int:
    print("Route-2 eta-floor Hellmann-Feynman boundary check")
    print("=" * 72)

    support_src = source_text("scripts/frontier_tensor_support_center_excess_law.py")
    boundary_src = source_text("scripts/frontier_tensor_boundary_drive_two_channel.py")
    kernel_src = source_text("scripts/frontier_tensor_universal_kernel.py")
    tensor_src = source_text("scripts/frontier_tensorial_einstein_regge_completion.py")

    check(
        "support eta_floor delegates to tensor_metrics(phi_from_q(q))[0]",
        "return float(two.tensor_metrics(phi_from_q(q))[0])" in support_src,
        "scripts/frontier_tensor_support_center_excess_law.py",
    )
    check(
        "boundary tensor_metrics returns blk.eta_floor[1] as its first metric",
        "float(blk.eta_floor[1])" in boundary_src
        and "float(blk.eta_floor[1] / abs(blk.scalar_action))" in boundary_src,
        "scripts/frontier_tensor_boundary_drive_two_channel.py",
    )
    check(
        "family_block stores eta_floor as np.array([0.0, base.e_spatial_tf])",
        "eta_floor = np.array([0.0, base.e_spatial_tf], dtype=float)" in kernel_src,
        "scripts/frontier_tensor_universal_kernel.py",
    )
    check(
        "e_spatial_tf is the max absolute trace-free spatial Einstein entry",
        "spatial_tf = spatial - np.eye(3) * float(np.trace(spatial)) / 3.0" in tensor_src
        and "e_spatial_tf = float(np.max(np.abs(spatial_tf)))" in tensor_src,
        "scripts/frontier_tensorial_einstein_regge_completion.py",
    )

    spectral_in_eta_path = {
        "support.eta_floor": call_names_in_function(
            "scripts/frontier_tensor_support_center_excess_law.py",
            "eta_floor",
        )
        & {"eig", "eigh", "eigvals", "eigvalsh"},
        "boundary.tensor_metrics": call_names_in_function(
            "scripts/frontier_tensor_boundary_drive_two_channel.py",
            "tensor_metrics",
        )
        & {"eig", "eigh", "eigvals", "eigvalsh"},
        "kernel.family_block": call_names_in_function(
            "scripts/frontier_tensor_universal_kernel.py",
            "family_block",
        )
        & {"eig", "eigh", "eigvals", "eigvalsh"},
        "tensor.probe_family": call_names_in_function(
            "scripts/frontier_tensorial_einstein_regge_completion.py",
            "probe_family",
        )
        & {"eig", "eigh", "eigvals", "eigvalsh"},
        "tensor.max_tensorial_components": call_names_in_function(
            "scripts/frontier_tensorial_einstein_regge_completion.py",
            "max_tensorial_components",
        )
        & {"eig", "eigh", "eigvals", "eigvalsh"},
    }
    check(
        "no eig/eigh/eigvalsh call participates in the eta_floor assembly path",
        all(not calls for calls in spectral_in_eta_path.values()),
        str(spectral_in_eta_path),
    )
    kernel_spectral_calls = all_spectral_calls("scripts/frontier_tensor_universal_kernel.py")
    kernel_main_spectral_calls = call_names_in_function(
        "scripts/frontier_tensor_universal_kernel.py",
        "main",
    ) & {"eig", "eigh", "eigvals", "eigvalsh"}
    check(
        "the only spectral call in the universal-kernel file is K_univ diagnostics outside family_block",
        len(kernel_spectral_calls) == 1
        and kernel_spectral_calls[0][0] == "eigvalsh"
        and kernel_main_spectral_calls == {"eigvalsh"}
        and spectral_in_eta_path["kernel.family_block"] == set(),
        f"spectral calls = {kernel_spectral_calls}",
    )

    same = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
    two = load_frontier("tensor_two_channel", "frontier_tensor_boundary_drive_two_channel.py")
    utk = load_frontier("tensor_universal_kernel", "frontier_tensor_universal_kernel.py")
    tcomp = load_frontier("tensor_completion", "frontier_tensorial_einstein_regge_completion.py")

    basis = same.build_adapted_basis()
    e0 = basis[:, 0]
    s_unit = basis[:, 1] / np.sqrt(6.0)
    e1 = basis[:, 2]
    e2 = basis[:, 3]
    ex = (np.sqrt(3.0) * e1 + e2) / 2.0
    t1x = basis[:, 4]

    q_combo = 0.7 * e0 - 0.2 * s_unit + 0.05 * ex - 0.03 * t1x
    phi_combo = two.phi_from_q(q_combo)
    phi_linear = (
        0.7 * two.phi_from_q(e0)
        - 0.2 * two.phi_from_q(s_unit)
        + 0.05 * two.phi_from_q(ex)
        - 0.03 * two.phi_from_q(t1x)
    )
    linearity_error = float(np.max(np.abs(phi_combo - phi_linear)))
    check(
        "q to phi is linear on the endpoint and bright-channel directions",
        linearity_error < 1.0e-14,
        f"max linearity error = {linearity_error:.3e}",
    )

    endpoint_rows = []
    for label, q in (("center e0", e0), ("shell s/sqrt6", s_unit)):
        phi = two.phi_from_q(q)
        blk = quiet_family_block(utk, label, phi)
        base = tcomp.probe_family("base", phi, eps_vec=0.0, eps_ten=0.0, omega=0.0)
        metric_eta = two.tensor_metrics(phi)[0]
        top_abs, active_gap, active_entry = active_max_entry(tcomp, phi)
        endpoint_rows.append((label, blk, base, metric_eta, top_abs, active_gap, active_entry))
        print(
            f"OBS: {label}: eta_floor[1]={blk.eta_floor[1]:.18e}, "
            f"e_spatial_tf={base.e_spatial_tf:.18e}, active_max_gap={active_gap:.3e}, "
            f"active_entry=(point={active_entry[0]}, i={active_entry[1]}, j={active_entry[2]}, "
            f"value={active_entry[3]:+.18e})"
        )

    check(
        "dynamic endpoint evaluation confirms eta_floor[0] is zero and eta_floor[1] equals e_spatial_tf",
        all(
            abs(float(blk.eta_floor[0])) < 1.0e-18
            and abs(float(blk.eta_floor[1]) - float(base.e_spatial_tf)) < 1.0e-18
            and abs(float(metric_eta) - float(base.e_spatial_tf)) < 1.0e-18
            for _label, blk, base, metric_eta, _top_abs, _active_gap, _active_entry in endpoint_rows
        ),
        "checked at q=e0 and q=s/sqrt(6)",
    )
    check(
        "implemented nonspectral max envelope is not tied at the two endpoint backgrounds",
        all(active_gap > 1.0e-8 for _label, _blk, _base, _metric, _top_abs, active_gap, _entry in endpoint_rows),
        "this is a max-entry gap, not a spectral eigenvalue gap",
    )

    first_blk = endpoint_rows[0][1]
    spectral_attrs = [
        name
        for name in ("operator", "spectrum", "eigenvalues", "eigenvectors", "floor_eigenvector", "psi")
        if hasattr(first_blk, name)
    ]
    check(
        "FamilyBlock exposes no A(phi), spectrum, or floor eigenvector for Hellmann-Feynman",
        spectral_attrs == [],
        f"exposed spectral attrs = {spectral_attrs}",
    )
    check(
        "spectral-simplicity and eigenvector-residual checks are inapplicable on the live object",
        spectral_attrs == [] and all(not calls for calls in spectral_in_eta_path.values()),
        "the branch stops before assembling beta_E, beta_T by Hellmann-Feynman",
    )
    check(
        "no exact-slope t_balance is emitted by this runner",
        True,
        "without A(phi), lambda_min, and psi, any Hellmann-Feynman t_balance would be fabricated",
    )

    print("=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
