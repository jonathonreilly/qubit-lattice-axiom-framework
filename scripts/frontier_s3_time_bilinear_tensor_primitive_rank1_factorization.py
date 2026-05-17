#!/usr/bin/env python3
"""Rank-1 outer-product factorization of the bilinear carrier `K_R`.

This is the paired runner for the source note
`docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_RANK1_FACTORIZATION_NOTE_2026-05-17.md`.

Scope (positive narrow theorem, class A, polynomial-identity arithmetic):

Under the same named admitted inputs as the parent definition note
`docs/S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` (i.e.
`delta_A1` from the retained-bounded
`frontier_tensor_support_center_excess_law.py`; `(u_E, u_T)` as linear
functionals in the adapted basis from `frontier_same_source_metric_ansatz_scan.py`),
the symbolic carrier

    K_R(q) := [[u_E(q),           u_T(q)],
               [delta_A1(q)u_E(q), delta_A1(q)u_T(q)]]

factors algebraically as the rank-1 outer product

    K_R(q) = w(q) v(q)^T,    w(q) = (1, delta_A1(q))^T,
                              v(q) = (u_E(q), u_T(q))^T,

and the following five structural properties (R1)-(R5) follow by polynomial
identity. This runner verifies each at floating-point precision on a grid
of seven-site star-support `q` values (canonical A1 family + bright and dark
perturbations of varying amplitude). Each verification is class A
(polynomial-identity substitution); the runner does NOT promote any of the
three named open gaps in the parent note above class-D finite-grid status.

Hard rules: A_min only. All inputs are imported from the same cited
authorities used by the parent runner. No new primitives.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from _frontier_loader import load_frontier


same = load_frontier("same_source_metric", "frontier_same_source_metric_ansatz_scan.py")
center = load_frontier("tensor_center_excess", "frontier_tensor_support_center_excess_law.py")


# Numerical tolerance for algebraic identities (polynomial-identity scale).
ABS_TOL = 1e-12

# Test grid: canonical A1 family (multiple r), bright/dark perturbations at
# multiple amplitudes. Same support as the parent runner.
R_GRID = [0.0, 0.25, 0.5, 1.0, 1.5, 2.0]
BRIGHT_AMPLITUDES = [0.0, 0.02, 0.10, 0.25, 0.50]
DARK_AMPLITUDES = [0.0, 0.02, 0.10, 0.25, 0.50]


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


# Build adapted basis from the canonical helper.
basis = same.build_adapted_basis()
e0 = basis[:, 0]
s = basis[:, 1]
e1 = basis[:, 2]
e2 = basis[:, 3]
t1x = basis[:, 4]
t1y = basis[:, 5]
t1z = basis[:, 6]
e_x = (np.sqrt(3.0) * e1 + e2) / 2.0
e_perp = (-e1 + np.sqrt(3.0) * e2) / 2.0
s_unit = s / np.sqrt(6.0)


def a1_background(r: float) -> np.ndarray:
    return (e0 + r * s) / (1.0 + np.sqrt(6.0) * r)


def delta_a1(q: np.ndarray) -> float:
    return float(center.support_delta(q))


def bright_coords(q: np.ndarray) -> tuple[float, float]:
    return float(np.dot(e_x, q)), float(np.dot(t1x, q))


def w_col(q: np.ndarray) -> np.ndarray:
    """Scaling-channel column w(q) = (1, delta_A1(q))^T."""
    return np.array([1.0, delta_a1(q)], dtype=float)


def v_col(q: np.ndarray) -> np.ndarray:
    """Bright-channel column v(q) = (u_E(q), u_T(q))^T."""
    u_e, u_t = bright_coords(q)
    return np.array([u_e, u_t], dtype=float)


def k_r(q: np.ndarray) -> np.ndarray:
    """Bilinear carrier K_R(q) defined per the parent note."""
    u_e, u_t = bright_coords(q)
    d = delta_a1(q)
    return np.array(
        [
            [u_e, u_t],
            [d * u_e, d * u_t],
        ],
        dtype=float,
    )


def k_r_factored(q: np.ndarray) -> np.ndarray:
    """K_R(q) computed via the rank-1 factorization w(q) v(q)^T."""
    return np.outer(w_col(q), v_col(q))


def build_q_grid() -> list[tuple[str, np.ndarray]]:
    """Return labeled (q_label, q) pairs covering A1 + bright/dark perturbations."""
    samples: list[tuple[str, np.ndarray]] = []
    for r in R_GRID:
        q_a = a1_background(r)
        samples.append((f"A1(r={r:.2f})", q_a))
        for amp in BRIGHT_AMPLITUDES:
            if amp == 0.0:
                continue
            for label, vec in [("E_x", e_x), ("T1x", t1x)]:
                samples.append((f"A1(r={r:.2f})+{amp:.2f}*{label}", q_a + amp * vec))
        for amp in DARK_AMPLITUDES:
            if amp == 0.0:
                continue
            for label, vec in [("E_perp", e_perp), ("T1y", t1y), ("T1z", t1z)]:
                samples.append((f"A1(r={r:.2f})+{amp:.2f}*{label}", q_a + amp * vec))
        # Mixed bright+dark perturbations
        for amp in [0.10, 0.25]:
            samples.append(
                (
                    f"A1(r={r:.2f})+{amp:.2f}*(E_x+T1x+E_perp)",
                    q_a + amp * (e_x + t1x + e_perp),
                )
            )
    return samples


def check_factorization(samples: list[tuple[str, np.ndarray]]) -> float:
    """Identity: K_R(q) = w(q) v(q)^T."""
    max_err = 0.0
    for _, q in samples:
        err = float(np.max(np.abs(k_r(q) - k_r_factored(q))))
        max_err = max(max_err, err)
    return max_err


def check_r1_rank(samples: list[tuple[str, np.ndarray]]) -> tuple[float, int, int]:
    """R1: rank of K_R(q) <= 1 (smallest singular value ~ 0).
    Returns (max sigma_2, n_rank_1, n_rank_0).
    """
    max_sigma2 = 0.0
    n_rank_1 = 0
    n_rank_0 = 0
    for _, q in samples:
        u, sigma, vt = np.linalg.svd(k_r(q))
        sigma2 = float(sigma[1])
        max_sigma2 = max(max_sigma2, sigma2)
        v = v_col(q)
        if float(np.linalg.norm(v)) > 1e-12:
            n_rank_1 += 1
        else:
            n_rank_0 += 1
    return max_sigma2, n_rank_1, n_rank_0


def check_r2_determinant(samples: list[tuple[str, np.ndarray]]) -> float:
    """R2: det K_R(q) = 0."""
    max_det = 0.0
    for _, q in samples:
        max_det = max(max_det, float(abs(np.linalg.det(k_r(q)))))
    return max_det


def check_r3_column_proportional(samples: list[tuple[str, np.ndarray]]) -> float:
    """R3: u_T * col_1 = u_E * col_2 (cross-product form, never divides by zero)."""
    max_err = 0.0
    for _, q in samples:
        kr = k_r(q)
        col1 = kr[:, 0]
        col2 = kr[:, 1]
        u_e, u_t = bright_coords(q)
        # u_T * col_1 should equal u_E * col_2 as 2-vectors.
        err = float(np.max(np.abs(u_t * col1 - u_e * col2)))
        max_err = max(max_err, err)
    return max_err


def check_r3_row_proportional(samples: list[tuple[str, np.ndarray]]) -> float:
    """R3 row form: row_2 = delta_A1(q) * row_1."""
    max_err = 0.0
    for _, q in samples:
        kr = k_r(q)
        row1 = kr[0, :]
        row2 = kr[1, :]
        d = delta_a1(q)
        err = float(np.max(np.abs(row2 - d * row1)))
        max_err = max(max_err, err)
    return max_err


def check_r4_bright_channel_separation() -> tuple[float, float, float]:
    """R4: under decoupling, partial_{E_x} K_R = w(q) (1, 0); partial_{T1x} K_R = w(q) (0, 1).
    Uses finite differences with multiple step sizes.
    """
    max_ex_err = 0.0
    max_tx_err = 0.0
    # Use a small step + exact closed-form using bilinearity
    for r in R_GRID:
        q_a = a1_background(r)
        w_q = w_col(q_a)
        # Exact finite-difference identity at any amplitude (E_x, T1x are linear
        # in the bright coordinates and delta_A1 is admitted to be blind):
        # K_R(q + h E_x) - K_R(q) = h * w(q) * (1,0)  (exact under decoupling)
        # We check at multiple step sizes.
        for h in [0.02, 0.10, 0.25]:
            diff_ex = k_r(q_a + h * e_x) - k_r(q_a)
            target_ex = h * np.outer(w_q, np.array([1.0, 0.0]))
            err_ex = float(np.max(np.abs(diff_ex - target_ex)))
            max_ex_err = max(max_ex_err, err_ex)
            diff_tx = k_r(q_a + h * t1x) - k_r(q_a)
            target_tx = h * np.outer(w_q, np.array([0.0, 1.0]))
            err_tx = float(np.max(np.abs(diff_tx - target_tx)))
            max_tx_err = max(max_tx_err, err_tx)
    # Auxiliary scaling-channel: partial_{delta} K_R = e_2 v^T = [[0,0],[u_E,u_T]]
    # This is the formal symbolic partial derivative treating delta_A1 as a free
    # symbol. We check it by constructing K_R(q) with an artificially shifted
    # delta value (treating delta as an independent symbol).
    max_delta_err = 0.0
    for r in R_GRID:
        q_a = a1_background(r)
        v_q = v_col(q_a)
        d = delta_a1(q_a)
        # Build K_R with shifted delta (treating delta as a free symbol)
        for dh in [0.01, 0.05, 0.1]:
            d_shift = d + dh
            kr_shift = np.array(
                [
                    [v_q[0], v_q[1]],
                    [d_shift * v_q[0], d_shift * v_q[1]],
                ],
                dtype=float,
            )
            kr_base = np.array(
                [
                    [v_q[0], v_q[1]],
                    [d * v_q[0], d * v_q[1]],
                ],
                dtype=float,
            )
            diff = kr_shift - kr_base
            target = dh * np.outer(np.array([0.0, 1.0]), v_q)
            err = float(np.max(np.abs(diff - target)))
            max_delta_err = max(max_delta_err, err)
    return max_ex_err, max_tx_err, max_delta_err


def check_r5_singular_values(samples: list[tuple[str, np.ndarray]]) -> tuple[float, float]:
    """R5: sigma_1 = ||w|| * ||v|| and sigma_2 = 0."""
    max_sigma1_err = 0.0
    max_sigma2 = 0.0
    for _, q in samples:
        u, sigma, vt = np.linalg.svd(k_r(q))
        w_q = w_col(q)
        v_q = v_col(q)
        target_sigma1 = float(np.linalg.norm(w_q) * np.linalg.norm(v_q))
        max_sigma1_err = max(max_sigma1_err, float(abs(sigma[0] - target_sigma1)))
        max_sigma2 = max(max_sigma2, float(sigma[1]))
    return max_sigma1_err, max_sigma2


def check_factor_separability() -> float:
    """R5 second form: explicit scaling-channel / bright-channel factor pieces:
    sigma_1 = sqrt(1 + delta_A1^2) * sqrt(u_E^2 + u_T^2).
    """
    max_err = 0.0
    for r in R_GRID:
        q_a = a1_background(r)
        for amp in [0.0, 0.10, 0.25]:
            for label, vec in [("0", np.zeros(7)), ("E_x", e_x), ("T1x", t1x)]:
                q = q_a + amp * vec
                d = delta_a1(q)
                u_e, u_t = bright_coords(q)
                scaling_norm = float(np.sqrt(1.0 + d * d))
                bright_norm = float(np.sqrt(u_e * u_e + u_t * u_t))
                target = scaling_norm * bright_norm
                _, sigma, _ = np.linalg.svd(k_r(q))
                err = float(abs(sigma[0] - target))
                max_err = max(max_err, err)
    return max_err


def main() -> int:
    print("Bilinear carrier K_R rank-1 outer-product factorization")
    print("=" * 78)

    samples = build_q_grid()
    print(f"Test grid size: {len(samples)} samples (A1 family x bright/dark perturbations)")

    # Factorization identity check
    factor_err = check_factorization(samples)
    print(f"\nFactorization identity K_R(q) = w(q) v(q)^T: max err = {factor_err:.3e}")

    # R1: rank-1
    max_sigma2_r1, n_r1, n_r0 = check_r1_rank(samples)
    print(f"\n(R1) Rank-1 universality:")
    print(f"  max sigma_2 across {len(samples)} samples = {max_sigma2_r1:.3e}")
    print(f"  rank-exactly-1 samples (||v(q)|| > 0): {n_r1}")
    print(f"  rank-0 samples (v(q) == 0): {n_r0}")

    # R2: determinant
    max_det = check_r2_determinant(samples)
    print(f"\n(R2) det K_R(q) = 0: max |det| = {max_det:.3e}")

    # R3: row/col proportionality
    max_col_prop = check_r3_column_proportional(samples)
    max_row_prop = check_r3_row_proportional(samples)
    print(f"\n(R3) Column proportionality (u_T col_1 - u_E col_2): max err = {max_col_prop:.3e}")
    print(f"(R3) Row proportionality (row_2 - delta_A1 row_1): max err = {max_row_prop:.3e}")

    # R4: channel separation
    max_ex, max_tx, max_delta = check_r4_bright_channel_separation()
    print(f"\n(R4) Channel separation (under admitted decoupling fact):")
    print(f"  partial_E_x K_R - w (1,0): max err = {max_ex:.3e}")
    print(f"  partial_T1x K_R - w (0,1): max err = {max_tx:.3e}")
    print(f"  partial_delta K_R - e_2 v^T: max err = {max_delta:.3e}")

    # R5: singular values
    max_sigma1, max_sigma2_r5 = check_r5_singular_values(samples)
    print(f"\n(R5) Singular-value factorization:")
    print(f"  sigma_1 - ||w|| ||v||: max err = {max_sigma1:.3e}")
    print(f"  sigma_2: max = {max_sigma2_r5:.3e}")
    max_factor = check_factor_separability()
    print(f"  sigma_1 - sqrt(1+delta^2) sqrt(u_E^2+u_T^2): max err = {max_factor:.3e}")

    # Record results
    record(
        "[class A, polynomial-identity] rank-1 factorization identity K_R(q) = w(q) v(q)^T holds at machine precision across A1 + bright/dark perturbations",
        factor_err < ABS_TOL,
        f"max factorization err = {factor_err:.3e} (tol = {ABS_TOL:.0e})",
    )
    record(
        "[class A, polynomial-identity] R1: K_R(q) has rank <= 1 universally (sigma_2 ~ 0) and rank exactly 1 when ||v(q)|| > 0",
        max_sigma2_r1 < ABS_TOL,
        f"max sigma_2 = {max_sigma2_r1:.3e}; rank-1 samples = {n_r1}; rank-0 samples = {n_r0}",
    )
    record(
        "[class A, polynomial-identity] R2: det K_R(q) = 0 universally",
        max_det < ABS_TOL,
        f"max |det| = {max_det:.3e}",
    )
    record(
        "[class A, polynomial-identity] R3 column form: u_T col_1 = u_E col_2 universally",
        max_col_prop < ABS_TOL,
        f"max err = {max_col_prop:.3e}",
    )
    record(
        "[class A, polynomial-identity] R3 row form: row_2 = delta_A1 row_1 universally",
        max_row_prop < ABS_TOL,
        f"max err = {max_row_prop:.3e}",
    )
    record(
        "[class A, polynomial-identity under admitted decoupling] R4 bright-channel: partial_E_x K_R = w(q) (1,0)",
        max_ex < ABS_TOL,
        f"max err = {max_ex:.3e} (uses admitted decoupling fact; same status as parent runner's class-D grid shadow)",
    )
    record(
        "[class A, polynomial-identity under admitted decoupling] R4 bright-channel: partial_T1x K_R = w(q) (0,1)",
        max_tx < ABS_TOL,
        f"max err = {max_tx:.3e} (uses admitted decoupling fact; same status as parent runner's class-D grid shadow)",
    )
    record(
        "[class A, polynomial-identity] R4 scaling-channel: partial_delta K_R = e_2 v^T (formal symbolic derivative)",
        max_delta < ABS_TOL,
        f"max err = {max_delta:.3e}",
    )
    record(
        "[class A, polynomial-identity] R5 singular value: sigma_1 = ||w|| * ||v|| (numerical SVD)",
        max_sigma1 < ABS_TOL,
        f"max err = {max_sigma1:.3e}",
    )
    record(
        "[class A, polynomial-identity] R5 collapse: sigma_2 = 0 (numerical SVD)",
        max_sigma2_r5 < ABS_TOL,
        f"max sigma_2 = {max_sigma2_r5:.3e}",
    )
    record(
        "[class A, polynomial-identity] R5 factor separation: sigma_1 = sqrt(1+delta_A1^2) * sqrt(u_E^2 + u_T^2)",
        max_factor < ABS_TOL,
        f"max err = {max_factor:.3e}",
    )

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = sum(not c.ok for c in CHECKS)
    print(f"PASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")

    print(
        "\nVerdict (class-A scope, positive narrow theorem):"
        "\n  Under the named admitted inputs of the parent definition note, the"
        "\n  symbolic carrier K_R(q) factors algebraically as the rank-1 outer"
        "\n  product w(q) v(q)^T with w = (1, delta_A1)^T and v = (u_E, u_T)^T."
        "\n  The five structural properties (R1)-(R5) hold by polynomial identity"
        "\n  at machine precision on the seven-site star support. The three named"
        "\n  open theorem targets in the parent note (decoupling, aligned-bright"
        "\n  identification, physical-primitive bridge) remain upstream and are"
        "\n  not closed by this runner."
    )

    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
