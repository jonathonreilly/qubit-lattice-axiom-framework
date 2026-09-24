#!/usr/bin/env python3
"""Independent finite sanity checks; the quantified proof is in PRE.md.

No source runner or root campaign derivation is imported.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import scipy.linalg as la
import sympy as sp


ROOT = Path(__file__).resolve().parent


def exact_psd(matrix: sp.Matrix) -> bool:
    for count in range(1, matrix.rows + 1):
        for inds in itertools.combinations(range(matrix.rows), count):
            minor = sp.simplify(matrix.extract(inds, inds).det())
            if minor.is_nonnegative is not True:
                return False
    return True


def exact_checks() -> dict:
    i = sp.I
    q = sp.Matrix([[1, i], [2, -1], [0, 1]])
    b = sp.Matrix([[1, i, 0], [-i, 0, 2], [0, 2, -1]])
    delta, kappa = sp.Rational(2, 3), sp.Rational(5, 4)
    qbar, bbar = sp.Integer(4), sp.Integer(4)
    alpha = kappa * delta / (kappa**2 + delta**2 * (qbar**2 + bbar**2))
    eye = sp.eye(5)
    generator = sp.zeros(2).row_join(-i * delta * q.H).col_join(
        (-i * delta * q).row_join(-kappa * sp.eye(3) - i * delta * b)
    )
    correction = sp.zeros(2).row_join(-i * q.H / 2).col_join(
        (i * q / 2).row_join(sp.zeros(3))
    )
    metric = eye + alpha * correction
    direct = sp.simplify(generator.H * metric + metric * generator)
    predicted = (-alpha * delta * q.H * q).row_join(
        alpha * q.H * (i * kappa * sp.eye(3) - delta * b) / 2
    ).col_join(
        (alpha * (-i * kappa * sp.eye(3) - delta * b) * q / 2).row_join(
            alpha * delta * q * q.H - 2 * kappa * sp.eye(3)
        )
    )
    target_loss = sp.diag(alpha * delta * q.H * q / 2, kappa * sp.eye(3))
    results = {
        "B_is_Hermitian": b.H == b,
        "declared_Q_bound_by_Frobenius": sum(abs(v)**2 for v in q) <= qbar**2,
        "declared_B_bound_by_Frobenius": sum(abs(v)**2 for v in b) <= bbar**2,
        "differential_identity_exact": sp.simplify(direct - predicted) == sp.zeros(5),
        "H_ge_three_quarters_I_exact": exact_psd(metric - 3 * eye / 4),
        "H_le_five_quarters_I_exact": exact_psd(5 * eye / 4 - metric),
        "dissipation_inequality_exact": exact_psd(-direct - target_loss),
    }
    wrong_metric = eye - alpha * correction
    wrong_derivative = sp.simplify(generator.H * wrong_metric + wrong_metric * generator)
    results["wrong_cross_sign_rejected_exact"] = (wrong_derivative[0, 0] > 0) is sp.S.true
    defective = sp.Matrix([[0, -i / 2], [-i / 2, -1]])
    nilpotent = defective + sp.eye(2) / 2
    results["defective_generator_exact"] = nilpotent != sp.zeros(2) and nilpotent**2 == sp.zeros(2)
    symbol_s, symbol_a, symbol_delta = sp.symbols("s a delta", nonzero=True)
    branch = -symbol_delta**2 * symbol_s**2 / symbol_a - symbol_delta**4 * symbol_s**4 / symbol_a**3
    residual = sp.expand(branch**2 + symbol_a * branch + symbol_delta**2 * symbol_s**2)
    results["scalar_slow_branch_through_fourth_order_exact"] = all(
        residual.coeff(symbol_s, power) == 0 for power in range(6)
    )
    assert all(results.values()), results
    return {k: bool(v) for k, v in results.items()}


def numerical_checks() -> dict:
    rng = np.random.default_rng(2026092417)
    rows = []
    spectra = [(1, 1, [0.0]), (1, 1, [0.5]), (2, 3, [0.0, 1.0]),
               (2, 3, [1e-5, 1.0]), (3, 5, [0.1, 0.7, 1.0]),
               (5, 8, [0.0, 0.0, 0.01, 0.1, 1.0])]
    for n, m, singular_values in spectra:
        uq, _ = la.qr(rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m)))
        vq, _ = la.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
        q = uq[:, :n] @ np.diag(singular_values) @ vq.conj().T
        raw_b = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
        b = (raw_b + raw_b.conj().T) / 2
        for delta, kappa in [(0.1, 3.0), (1.0, 1.0), (7.0, 0.2)]:
            qbar = max(1.0, la.norm(q, 2))
            bbar = la.norm(b, 2)
            alpha = kappa * delta / (kappa**2 + delta**2 * (qbar**2 + bbar**2))
            rate_factor = 2 * alpha * delta / 5
            generator = np.block([[np.zeros((n, n)), -1j * delta * q.conj().T],
                                  [-1j * delta * q, -kappa * np.eye(m) - 1j * delta * b]])
            metric = np.eye(n + m) + alpha * np.block([
                [np.zeros((n, n)), -0.5j * q.conj().T],
                [0.5j * q, np.zeros((m, m))]])
            derivative = generator.conj().T @ metric + metric @ generator
            target_loss = la.block_diag(alpha * delta * q.conj().T @ q / 2, kappa * np.eye(m))
            residual_max = float(la.eigvalsh(derivative + target_loss)[-1])
            assert residual_max < 1e-10 * max(1.0, la.norm(generator, 2))
            mine, maxe = la.eigvalsh(metric)[[0, -1]]
            assert mine >= 0.75 - 1e-12 and maxe <= 1.25 + 1e-12
            sigma_min = min(singular_values)
            exponent = rate_factor * sigma_min**2
            ratios = []
            for time in [0.0, 0.01, 0.3, 1.0, 3.0, 10.0, 30.0]:
                actual = la.norm(la.expm(time * generator), 2)**2
                bound = (5.0 / 3.0) * np.exp(-exponent * time)
                assert actual <= 1 + 1e-10
                assert actual <= bound * (1 + 1e-10)
                ratios.append(actual / bound)
            kernel_indices = [j for j, value in enumerate(singular_values) if value == 0]
            kernel_residual = 0.0
            if kernel_indices:
                dark_kernel = vq[:, kernel_indices]
                kernel_projector = la.block_diag(dark_kernel @ dark_kernel.conj().T, np.zeros((m, m)))
                kernel_residual = max(la.norm(generator @ kernel_projector, 2),
                                      la.norm(kernel_projector @ generator, 2))
                assert kernel_residual < 1e-10
            rows.append({"dark_dim": n, "bright_dim": m, "singular_values": singular_values,
                         "delta": delta, "kappa": kappa, "residual_max_eigenvalue": residual_max,
                         "metric_min": float(mine), "metric_max": float(maxe),
                         "largest_ratio_to_claimed_bound": max(ratios),
                         "kernel_reduction_residual": float(kernel_residual),
                         "nonnormal_commutator_norm": float(la.norm(generator.conj().T @ generator - generator @ generator.conj().T, 2))})
    q = np.array([[0.5]])
    generator = np.array([[0.0, -0.5j], [-0.5j, -1.0]])
    alpha = 1 / 1.25
    metric = np.eye(2) + alpha * np.array([[0.0, -0.25j], [0.25j, 0.0]])
    mutation = generator.copy()
    mutation[1, 0] *= -1
    bad_max = float(la.eigvalsh(mutation.conj().T @ metric + metric @ mutation)[-1])
    assert bad_max > 0
    return {"cases": rows, "wrong_coupling_sign_positive_metric_derivative": bad_max,
            "scope": "Finite sanity checks, not proof of all matrices or of the physical phase geometry."}


def main() -> None:
    pins = json.loads((ROOT / "SOURCE_PINS.json").read_text())
    for entry in pins["sources"]:
        path = Path(entry["snapshot"])
        assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    data = {"source_snapshots_verified": True, "exact_checks": exact_checks(),
            "numerical_checks": numerical_checks()}
    (ROOT / "INDEPENDENT_BLOCK_CHECKS.json").write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({"source_snapshots_verified": True,
                      "exact_checks": data["exact_checks"],
                      "numerical_cases": len(data["numerical_checks"]["cases"]),
                      "wrong_coupling_sign_positive_metric_derivative": data["numerical_checks"]["wrong_coupling_sign_positive_metric_derivative"]}, indent=2))


if __name__ == "__main__":
    main()
